from Connection import *

c = open_connection()
join_room(c)
read_buffer = ''

while True:
        read_buffer = read_buffer + str(c.recv(1024))
        temp = read_buffer.split('\\r\\n')
        read_buffer = temp.pop()

        for line in temp:
            print(f'{get_user(line)}: {get_message(line)}')
            if 'PING :tmi.twitch.tv' in line:
                pong(c)

