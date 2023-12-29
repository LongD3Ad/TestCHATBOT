import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

GOOGLE_API_KEY = "zaSyBNAbbpDZXwgBOKgQjvnhijz8_UqbmKwPE"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
messages = []

app = Flask(__name__, static_folder='project/static', template_folder='project/template')

@app.route("/")
def index():
    return render_template('chat.html')

"""@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form["msg"]
    response = CustomChatGem(user_input)
    return jsonify({"msg": response}) """
@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form["msg"]
    response = CustomChatGem(user_input)
    return response

def CustomChatGem(user_input):
    global messages
    error_message = None
    try:
        messages.append({
            "role": "user",
            "parts": [user_input],
        })
        response = model.generate_content(messages)
        messages.append({
            "role": "model",
            "parts": [response.text],
        })
        return response.text
    except Exception as e:
        error_message = "An error occurred: " + str(e)
        return error_message

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
