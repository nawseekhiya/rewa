from PIL import Image
import io
import random

def predict_pollution(image_bytes=None):
    try:
        img = None
        if image_bytes:
            # Convert bytes to PIL Image
            img = Image.open(io.BytesIO(image_bytes))
            print(f"Processed image: {img.format}, Size: {img.size}")
            
        # Maintain dummy response
        levels = ['Clean', 'Slightly Polluted', 'Heavily Polluted']
        return {
            'pollution_level': random.choice(levels),
            'confidence': round(random.uniform(0.7, 0.99), 2),
            'image_processed': img is not None
        }
        
    except Exception as e:
        print(f"Model error: {str(e)}")
        return {'error': 'Image processing failed'}