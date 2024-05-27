import os
import random
from flask import Flask, send_from_directory, render_template

template_folder = os.path.abspath('../html')

app = Flask(__name__, template_folder=template_folder)

IMAGE_FOLDER = os.path.join('static', 'images')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random-photo')
def random_photo():
    images = os.listdir(IMAGE_FOLDER)
    if not images:
        return "No images found", 404
    
    random_image = random.choice(images)
    return send_from_directory(IMAGE_FOLDER, random_image)

if __name__ == '__main__':
    app.run(debug=True)
