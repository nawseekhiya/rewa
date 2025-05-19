from flask import Flask, jsonify, request
from dummy_model import predict_pollution
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    print("======== INCOMING REQUEST ========")
    print("Request files:", request.files)
    print("Request form:", request.form)
    print("Request data (raw):", request.get_data())

    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    # Optionally save the image for debugging
    image_file = request.files['image']
    image_file.save('debug_uploaded_image.jpg')

    result = predict_pollution()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
