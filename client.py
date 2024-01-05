import socket
import threading
from tkinter import *

root = Tk()
root.title("Chat Application")

message = Text(root)
message.pack()

input_user = StringVar()
input_field = Entry(root, text=input_user)
input_field.pack()

def send():
    message = input_field.get()
    client.send(message.encode('utf-8'))
    input_user.set("")
    
send_button = Button(root, text="Send", command=send)
send_button.pack()

#Socket setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

client.send("TestUser".encode('utf-8'))
username = client.recv(1024).decode('utf-8')

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            message.insert(INSERT, message + "\n")
        except:
            print("An error occurred")
            break
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

root.mainloop()