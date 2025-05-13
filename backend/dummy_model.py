import random

def predict_pollution():
    levels = ['Clean', 'Slightly Polluted', 'Heavily Polluted']
    return {
        'pollution_level': random.choice(levels),
        'confidence': round(random.uniform(0.7, 0.99), 2)
    }
