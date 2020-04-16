import threading
from CommandChatApp.src.ClientFunctions import msg_reveiver, msg_sender


if __name__ == "__main__":
    msg_sender = threading.Thread(target=msg_sender)
    msg_receiver = threading.Thread(target=msg_reveiver)
    msg_sender.start()
    msg_receiver.start()
