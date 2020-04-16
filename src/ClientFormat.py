import socket
import json

PORT = 5000
IP_ADDRESS = "10.0.0.102"
user_end = socket.socket()
user_end.connect((IP_ADDRESS, PORT))
home_user = input("Enter your name here: \n")

# login
login_format = {
    "activity":"login",
    "user": home_user
}
user_end.send(json.dumps(login_format).encode("utf32"))
info_recv = user_end.recv(2048)
print(info_recv.decode("utf32"))





