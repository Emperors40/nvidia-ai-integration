
import json
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

@app.route("/api/ai", methods=["POST"])
def ai_endpoint():
    data = request.get_json()
    query = data.get("question")
    
    completion = client.chat.completions.create(
        model="meta/llama-3.3-70b-instruct",
        messages=[{"role": "user", "content": query}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024
    )
    
    answer = "".join(chunk.choices[0].delta.content for chunk in completion if chunk.choices[0].delta.content)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

