import threading

from CommandChatApp.src.ServerFunctions import srv_end, request_distributor

while True:

    info_coordinator, addr = srv_end.accept()
    # start a new thread to isolate connection
    client_thread = threading.Thread(target=request_distributor, args=(info_coordinator, addr))
    client_thread.start()

