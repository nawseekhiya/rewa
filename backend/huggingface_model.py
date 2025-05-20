import requests
from PIL import Image
import io
import base64
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/facebook/deit-base-distilled-patch16-224"
HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

CLEAN_KEYWORDS = [
    'lake', 'ocean', 'sea', 'river', 'stream', 'clear', 'waterfall',
    'swimming pool', 'creek', 'glacier', 'ice', 'beach', 'coast', 'lagoon'
]

SLIGHTLY_POLLUTED_KEYWORDS = [
    'pond', 'mud', 'canal', 'algae', 'reservoir', 'wetland', 'marsh',
    'swamp', 'ditch', 'bayou', 'brackish', 'reed', 'silt', 'estuary'
]

HEAVILY_POLLUTED_KEYWORDS = [
    'sewer', 'garbage', 'waste', 'trash', 'oil', 'sludge', 'drain', 'pollution',
    'plastic', 'toxic', 'industrial', 'chemical', 'dump', 'contaminated', 'dirty'
]


def classify_pollution(label: str):
    label = label.lower()

    for keyword in CLEAN_KEYWORDS:
        if keyword in label:
            return 'Clean'
    for keyword in SLIGHTLY_POLLUTED_KEYWORDS:
        if keyword in label:
            return 'Slightly Polluted'
    for keyword in HEAVILY_POLLUTED_KEYWORDS:
        if keyword in label:
            return 'Heavily Polluted'
    return 'Heavily Polluted'  # fallback if no match

def predict_pollution(image_bytes=None):
    try:
        if image_bytes is None:
            return {'error': 'No image data provided'}

        encoded_image = base64.b64encode(image_bytes).decode("utf-8")
        payload = {
            "inputs": encoded_image
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code != 200:
            return {'error': f"HF API error: {response.status_code}", 'details': response.text}

        predictions = response.json()
        if not isinstance(predictions, list) or not predictions:
            return {'error': 'Unexpected response format', 'raw_response': predictions}

        top_prediction = predictions[0]
        label = top_prediction.get('label', '').lower()
        confidence = top_prediction.get('score', 0)

        level = classify_pollution(label)

        return {
            'pollution_level': level,
            'predicted_label': label,
            'confidence': round(confidence, 2),
            'image_processed': True
        }

    except Exception as e:
        return {'error': f'Processing failed: {str(e)}'}
