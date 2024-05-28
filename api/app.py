from flask import Flask, redirect

app = Flask(__name__)

@app.route('/get_image')
def get_image():
    return redirect("https://picsum.photos/200/300")

if __name__ == '__main__':
    app.run(debug=True)
