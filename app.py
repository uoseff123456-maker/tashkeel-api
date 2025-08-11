from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def add_diacritics(text: str) -> str:
    # مؤقتاً: رجّع النص مثل ما هو. بعدين نبدّلها بمُشكِّل فعلي
    # أو نربط خدمة خارجية ونرجع الناتج.
    return text.strip()

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.post("/api/tashkeel")
def tashkeel():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    if not isinstance(text, str):
        return jsonify(error="Field 'text' must be a string"), 400
    result = add_diacritics(text)
    return jsonify(result=result), 200

# لما تنشر على Render/Replit راح يضبط PORT تلقائياً عبر gunicorn
# هذا السطر يفيدك بالتشغيل المحلي فقط
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
