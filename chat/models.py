import openai
from flask import Flask, request, jsonify

openai.api_key = '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'
app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data['question']
    response = generate_response(question)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run()

legal_keywords = ['закон', 'уголовный кодекс', 'гражданский кодекс', 'административный кодекс', 'трудовой кодекс',
                  'налоговый кодекс', 'по закону КР', 'по законам КР', 'по уголовному кодексу', 'что мне грозит']


def is_legal_question(question):
    question = question.lower()
    for keyword in legal_keywords:
        if keyword in question:
            return True
    return False


def generate_response(question):
    if not is_legal_question(question):
        return "Извините, я могу отвечать только на вопросы, связанные с законами Кыргызской Республики."

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=3000,
        n=1,
        stop=None,
    )
    answer = response.choices[0].text.strip()
    return answer


if __name__ == '__main__':
    app.run()
