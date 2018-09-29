import socket
import re
from Settings import HOST, PORT, PASS, NICK, CHANNEL, PONG

def open_connection():
    c = socket.socket()
    c.connect((HOST, PORT))

    #IRC specific protocol
    c.send(f'PASS {PASS}\r\n'.encode('utf-8'))
    c.send(f'NICK {NICK}\r\n'.encode('utf-8'))
    c.send(f'JOIN #{CHANNEL}\r\n'.encode('utf-8'))

    #request Twitch specific information (subs, cheers, badges, etc.)
    c.send('CAP REQ :twitch.tv/tags\r\n'.encode('utf-8'))
    c.send('CAP REQ :twitch.tv/membership\r\n'.encode('utf-8'))
    c.send('CAP REQ :twitch.tv/commands\r\n'.encode('utf-8'))

    return c


def join_room(c):
    loading = True
    while(loading):
        read_buffer = str(c.recv(1024))
        temp = read_buffer.split('\\r\\n')
        read_buffer = temp.pop()

        for line in temp:
            print(line)
            if "End of" in line:
                print(line)
                print(f'joined room: {CHANNEL}')
                loading = False


def send_message(c, message):
    temp_message = "PRIVMSG #" + CHANNEL + " :" + message
    c.send((temp_message + "\r\n").encode('utf-8'))


def get_user(line):
    return re.findall(r'display-name=(.*?);', line)[0]


def get_message(line):
    temp = line.split(' :')[2]
    return temp


def get_bits(line):
    temp = line.split(' :')
    try:
        return int((re.findall(r';bits=(.*?);', temp[0]))[0])
    except:
        return 'fake'


def gift_sub_parse(line):
    sender = re.findall(r'display-name=(.*?);', line)[0]
    recipient = re.findall(r'msg-param-recipient-display-name=(.*?);', line)[0]
    total_gift_subs = int(re.findall(r'msg-param-sender-count=(.*?);', line)[0])
    tier = re.findall(r'msg-param-sub-plan=(.*?);', line)[0]
    return (sender, recipient, total_gift_subs, tier)


def sub_parse(line):
    subscriber = re.findall(r'display-name=(.*?);', line)[0]
    tier = re.findall(r'msg-param-sub-plan=(.*?);', line)[0]
    return (subscriber, tier)


def resub_parse(line):
    subscriber = re.findall(r'display-name=(.*?);', line)[0]
    duration = re.findall(r'msg-param-months=(.*?);', line)[0]
    tier = re.findall(r'msg-param-sub-plan=(.*?);', line)[0]
    return (subscriber, duration, tier)


def pong(c):
    c.send(PONG.encode('utf-8'))
    print('Sent: PONG')

