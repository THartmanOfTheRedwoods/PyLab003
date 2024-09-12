from getopt import gnu_getopt

import lab_chat as lc
from lab_chat import get_peer_node, get_channel


def get_username():
    username = input("Can you tell me your username?")
    username = username.strip().upper()
    return username

def get_group():
    group = input("What is the name of the group you want to join?")
    group = group.strip().upper()
    return group

def get_message():
    message = input("What is the message you want to send?")
    message = message.strip()
    return message
def initialize_chat():
    username = get_username()
    group = get_group()
    n = get_peer_node(username)
    return get_channel(n, group)


def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

start_chat()