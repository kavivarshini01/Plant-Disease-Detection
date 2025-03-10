from PIL import Image
import numpy as np
import io

def preprocess_image(image_file):
    if isinstance(image_file, (bytes, io.BytesIO)):
        image_file = Image.open(image_file)  # Open correctly
    
    image = image_file.convert("RGB")  # Ensure RGB format
    image = image.resize((256, 256))  # Resize to model's expected input size
    image_array = np.array(image) / 255.0  # Normalize pixel values
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    
    return image_array
