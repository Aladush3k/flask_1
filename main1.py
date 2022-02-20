import json


with open("templates/list.json", "rt", encoding="utf8") as f:
    news_list = json.loads(f.read())
print(news_list)