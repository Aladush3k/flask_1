from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in str(prof) or 'строитель' in str(prof):
        sxema = ['Инженерные тренажеры', '/static/img/img.png']
    else:
        sxema = ['Научные симуляторы', '/static/img/img_1.png']
    return render_template('training.html', image=sxema[1], text=sxema[0])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

