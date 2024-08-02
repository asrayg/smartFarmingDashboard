from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set your OpenAI API key
openai.api_key = 'sk-proj-2UzzkXtflvX9P3U0XLf8T3BlbkFJ2raQqahCE6H9rzmHEqTe'

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data['message']

    # Call the OpenAI API with the given message
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an advanced AI agricultural assistant specializing in precision soybean farming. Your primary function is to analyze sensor data, integrate it with comprehensive textbook knowledge, and provide highly specific recommendations to optimize soybean yield, quality, and sustainability."},
            {"role": "user", "content": message}
        ]
    )

    reply = response['choices'][0]['message']['content']

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
