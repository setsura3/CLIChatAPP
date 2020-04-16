import json
import socket
from collections import defaultdict

PORT = 5000
IP_ADDRESS = '0.0.0.0'
DATABASE = defaultdict(dict)
USER_MSGS = defaultdict(list)
srv_end = socket.socket()
srv_end.bind((IP_ADDRESS, PORT))
srv_end.listen(100)


def request_distributor(connection, addr):
    def remove_client(connection):
        if connection in DATABASE:
            DATABASE.remove(connection)

    def welcome():
        DATABASE[chat_info["user"]] = connection
        connection.send("Welcome! This is a command line chatting system".encode("utf32"))

    def forward():
        if chat_info["forward"] in DATABASE:
            DATABASE[chat_info["forward"]].send(json.dumps(chat_info).encode("utf32"))

    def decision_maker():
        if activity == "login":
            welcome()
        elif activity == "send_msg":
            forward()
        elif activity == "exit":
            remove_client(connection)

    while True:
        chat_info = connection.recv(2048)
        chat_info = json.loads(chat_info.decode("utf32"))
        activity = chat_info.get("activity", "")
        decision_maker()
