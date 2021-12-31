import os
import sys
import pygraphviz as pgv
from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

g = pgv.AGraph(directed = True,strict = False , nodesep = 2 , ranksep = 2 , rankdir = "LR",splines = "splines",concentrate = True)
node0 = "user"
node1 = "state1"
node2 = "state2"
node3 = "state3"
g.add_node(node0,style = "filled",shape = "circle",color = "#feb64d")
g.add_node(node1,style = "filled",shape = "circle",color = "#CFDBF6")
g.add_node(node2,style = "filled",shape = "circle",color = "#CFDBF6")
#g.add_node(node3,style = "filled",shape = "circle",color = "#CFDBF6")
g.add_edge(node0,node1,color = "#000000",style = "solid",penwidth = 1,label = "advance[is_going_to_state1]")
#g.add_edge(node0,node2,color = "#000000",style = "solid",penwidth = 1,label = "advance[is_going_to_state2]")
#g.add_edge(node0,node3,color = "#000000",style = "solid",penwidth = 1,label = "advance[is_going_to_state3]")

g.add_edge(node1,node0,color = "#000000",style = "solid",penwidth = 1,label = "go_back")
#g.add_edge(node2,node0,color = "#000000",style = "solid",penwidth = 1,label = "go_back")
#g.add_edge(node3,node0,color = "#000000",style = "solid",penwidth = 1,label = "go_back")

g.layout()
#g.draw("因果關係圖.png",prog = "neato")
machine = TocMachine(
    states=["user", "state1", "state2","state3"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state1",
            "conditions": "is_going_to_state1",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state3",
            "conditions": "is_going_to_state3",
        },
        {"trigger": "go_back", "source": ["state1", "state2","state3"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            #send_text_message(event.reply_token, "Not Entering any State")
            send_text_message(event.reply_token, "請輸入想要的拉麵種類 1.豚骨 2.雞白湯 3.二郎系")
    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    #port = os.environ.get("PORT", 8000)
    port = os.getenv("PORT",None)
    app.run(host="0.0.0.0", port=port, debug=True)
