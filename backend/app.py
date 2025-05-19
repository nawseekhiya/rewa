from flask import Flask, jsonify, request
from dummy_model import predict_pollution
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    print("\n===== REQUEST DETAILS =====")
    print("Headers:", dict(request.headers))
    
    # Check if request contains multipart/form-data
    if 'multipart/form-data' not in request.content_type:
        print("Invalid content type:", request.content_type)
        return jsonify({'error': 'Invalid content type'}), 400

    # Verify file existence
    if 'image' not in request.files:
        print("No 'image' field in files:", request.files)
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    
    # Check for empty filename
    if image_file.filename == '':
        print("Empty filename received")
        return jsonify({'error': 'No selected file'}), 400

    print("Received file:", image_file)
    print("Filename:", image_file.filename)
    print("Content type:", image_file.content_type)
    
    try:
        # Read image content once
        image_bytes = image_file.read()
        
        # Save for debugging (reset file pointer first)
        image_file.seek(0)
        image_file.save('debug_received_image.jpg')
        print(f"File saved ({len(image_bytes)} bytes)")
        
        # Process image bytes
        result = predict_pollution(image_bytes)
        
        if 'error' in result:
            return jsonify(result), 500
            
        return jsonify(result)
        
    except Exception as e:
        print(f"Processing error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)