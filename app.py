from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# نحاول نستخدم مكتبة "Mishkal" للتشكيل، ولو مو منصّبة نرجّع النص مثل ما هو
try:
    # بعض إصدارات Mishkal
    # pip name: mishkal  | يعتمد على pyarabic
    from mishkal.tashkeel.tashkeel import Tashkeel
    _mishkal = Tashkeel()
    def add_diacritics(text: str) -> str:
        return _mishkal.tashkeel(text or "")
except Exception:
    def add_diacritics(text: str) -> str:
        return (text or "").strip()

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

if __name__ == "__main__":
    # للتجربة المحلية فقط
    app.run(host="0.0.0.0", port=8000)
