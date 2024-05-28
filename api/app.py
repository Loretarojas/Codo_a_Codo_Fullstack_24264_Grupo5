from flask import Flask, send_from_directory
import os
import random

app = Flask(__name__)

@app.route('/random-photo', methods=['GET'])
def get_random_photo():
    image_folder = os.path.join(app.static_folder, 'images')
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
    random_image = random.choice(image_files)
    return send_from_directory(image_folder, random_image)

if __name__ == '__main__':
    app.run(debug=True)
