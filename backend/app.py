from flask import Flask, jsonify, request
from huggingface_model import predict_pollution
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']

    if image_file.filename == '':
        return jsonify({'error': 'Empty file'}), 400

    try:
        image_bytes = image_file.read()
        image_file.seek(0)
        image_file.save('debug.jpg')

        result = predict_pollution(image_bytes)

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
