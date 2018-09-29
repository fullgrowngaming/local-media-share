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
    return re.findall(fr'#{CHANNEL} :(.*$)', line)[0]


def get_bits(line):
    return int(re.findall(r';bits=(.*?);', line)[0])


def pong(c):
    c.send(PONG.encode('utf-8'))
    print('Sent: PONG')

