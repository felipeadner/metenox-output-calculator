from flask import Flask, request, render_template, send_file
import pandas as pd
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_file():
    file = request.files['file']
    df = pd.read_csv(file)
    # Lógica de processamento do arquivo aqui (como no código anterior)
    # Salva os resultados em um CSV
    result = df.to_csv(index=False)
    return send_file(StringIO(result), attachment_filename="result.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
