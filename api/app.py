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
    photos_dir = os.path.join(app.static_folder, 'images')  
    photos = os.listdir(photos_dir)
    if not photos:
        return "No photos found", 404
    random_photo = random.choice(photos)
    return send_from_directory(photos_dir, random_photo)

if __name__ == '__main__':
    app.run(debug=True)
