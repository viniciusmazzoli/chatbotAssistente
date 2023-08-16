import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

openai.api_key = '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'

def get_bot_response(user_message, messages):
    messages.append({'role': 'user', 'content': user_message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=messages
    )
    bot_message = response['choices'][0]['message']['content']
    messages.append({'role': 'assistant', 'content': bot_message})
    return bot_message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        user_message = request.json['message']
        messages = [{'role': 'system', 'content': 'Você é uma infermeira que ira conduzir uma triagem medica,faça uma pergunta a cada resposta do paciente, ate chegar sua conclusao final'}]
        bot_message = get_bot_response(user_message, messages)
        return jsonify({'message': bot_message})
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
