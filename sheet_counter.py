import cv2
import os
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

def count_sheets(image_path):
    """Counts the number of sheets in a given image.

    Args:
        image_path: Path to the image file.

    Returns:
        Estimated number of sheets in the image.
    """

    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Error reading image: {image_path}")

        # Preprocess the image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 100, 200)

        # Morphological operations to close gaps and remove noise
        kernel = np.ones((3, 3), np.uint8)
        img_closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        # Find contours
        contours, _ = cv2.findContours(img_closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filter contours based on area and shape
        def is_valid_contour(cnt):
            area = cv2.contourArea(cnt)
            perimeter = cv2.arcLength(cnt, True)
            if area > 100 and perimeter > 40:  # Adjust thresholds as needed
                return True
            return False

        filtered_contours = [cnt for cnt in contours if is_valid_contour(cnt)]

        sheet_count = len(filtered_contours)
        return sheet_count

    except Exception as e:
        print(f"Error processing image: {image_path}, Error: {e}")
        return 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('image')
        if file:
            try:
                file_path = os.path.join('dataset', file.filename)
                file.save(file_path)
                sheet_count = count_sheets(file_path)
                os.remove(file_path)
                return render_template('index.html', sheet_count=sheet_count)
            except Exception as e:
                print(f"Error processing image: {e}")
                return render_template('index.html', error_message="An error occurred while processing the image")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
