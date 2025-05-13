from flask import Flask, jsonify, request
from dummy_model import predict_pollution
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    # Get dummy prediction
    result = predict_pollution()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
