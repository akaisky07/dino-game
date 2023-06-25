from flask import Flask, render_template,request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jump', methods=['POST'])
def jump():
    if request.method == 'POST':
        obstacle_height = random.randint(1, 10)
        dino_jump = int(request.form['jump'])
        if dino_jump >= obstacle_height:
            message = "You cleared the obstacle!"
        else:
            message = "You hit the obstacle!"
        return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

