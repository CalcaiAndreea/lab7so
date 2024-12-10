from flask import Flask, request, jsonify, render_template
import re
from collections import Counter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/salut', methods=['GET'])
def salut():
    return "Salut din containerul Docker!"

@app.route('/api/procesare-text', methods=['GET'])
def procesare_text():
    text = request.args.get('text', '')
    reversed_text = text[::-1]
    return reversed_text

@app.route('/api/procesare-array', methods=['POST'])
def procesare_array():
    try:
        numere = request.get_json()
        if not isinstance(numere, list):
            return jsonify({"error": "Inputul trebuie să fie un array de numere."}), 400
        sorted_numere = sorted(numere)
        return jsonify(sorted_numere)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analiza-text', methods=['POST'])
def analiza_text():
    try:
        data = request.get_json()
        text = data.get('text', '')
        # Eliminăm caracterele non-alfabetice și transformăm textul în litere mici
        sanitized_text = re.sub(r'[^a-zA-Z]', '', text).lower()
        numar_litere = len(sanitized_text)
        frecventa_litere = dict(Counter(sanitized_text))
        # Sortăm frecvența literelor descrescător
        frecventa_litere = dict(sorted(frecventa_litere.items(), key=lambda item: item[1], reverse=True))
        rezultat = {
            "textOriginal": text,
            "numarLitere": numar_litere,
            "frecventaLitere": frecventa_litere
        }
        return jsonify(rezultat)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
