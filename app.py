from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "你的API_KEY"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("text")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"帮我写一段关于{prompt}的文案"}
        ]
    )

    result = response.choices[0].message.content
    return jsonify({"result": result})

app.run()
