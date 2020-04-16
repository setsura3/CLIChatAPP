import json
from CommandChatApp.src.ClientFormat import user_end, home_user

logout = False


def msg_reveiver():
    #constantly receiving requests from client
    while True:
        if not logout:
            try:
                info_recv = user_end.recv(2048)
            except:
                break
            info_recv = info_recv.decode("utf32")
            try:
                info_recv_json = json.loads(info_recv)
                msg = info_recv_json["chat_info"]
                from_user = info_recv_json["from"]
                print("")
                print("You received a message from({}): {}".format(from_user, msg))
            except:
                print("")
                print(info_recv)
        else:
            break

def msg_sender():

    def login_pompt():
        print("Invalid input, do it again!")
        user_input = input("What do you want to do: 1. Send message, 2. Exit")

    def send_msg():
        away_user = input("Type in the username you want to send message to: \n")
        msg = input("What do you want to send to {}: ".format(away_user))
        send_chat_info_format = {
            "activity": "send_msg",
            "forward": away_user,
            "from": home_user,
            "chat_info": msg
        }
        user_end.send(json.dumps(send_chat_info_format).encode("utf32"))

    def exit_app():
        logout = {
            "activity": "logout_option",
            "user": home_user
        }
        user_end.send(json.dumps(logout).encode("utf32"))
        user_end.close()
        print("Bye, I am looking forward to see you again!")

    while True:
        # constantly dealing with sending request from client
        user_input = input("What do you want to do: 1. Send message, 2. Exit \n")
        if user_input not in ["1", "2"]:
            login_pompt()
        elif user_input == "1":
            send_msg()
        elif user_input == "2":
            exit_app()
            break
