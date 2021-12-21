from flask import Flask, request, render_template
import time
from datetime import datetime

app = Flask(__name__)


def time_format(t):
    return datetime.fromtimestamp(t)


all_messages = [  # В этом списке хранятся все сообщения чата
    {  # каждое сообщение это словарь с полями text, name и time
        "text": 'Привет всем в чате',
        "name": "Mike",
        "time": time_format(time.time() - 3600)  # типа майк написал сообщение час (3600 сек) назад
    },
]


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/get_messages")  # GET — запрос на чтение данных
def get_messages():
    return {"messages": all_messages}


@app.route("/")
def root():
    return "Hello everyone"


# POST — запрос на изменение данных

@app.route("/send")
def send_message():
    # ToDO Проверить text и name

    text = request.args["text"]
    name = request.args["name"]

    message = {
        "text": text,
        "name": name,
        "time": time_format(time.time()),
    }

    all_messages.append(message)

    return "OK"


app.run()