from flask import Flask, url_for, request, render_template
import json
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


@app.route('/list_prof/<list>')
def show_list(list): # незнаю как указать путь до json файла, помогите пожалуйста
    tag = 0
    if list == 'ol':
        tag = 1
    elif list == 'ul':
        tag = 2
    with open("C:/Users/vakva/PycharmProjects/flask_1/static/js/list.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('list.html', news=news_list, tag=tag)

        
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

