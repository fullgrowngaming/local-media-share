from Connection import *

c = open_connection()
join_room(c)
read_buffer = ''

while True:
        read_buffer = read_buffer + str(c.recv(1024))
        temp = read_buffer.split('\\r\\n')
        read_buffer = temp.pop()

        for line in temp:
            if ' PRIVMSG #' in line:
                #print(f'{get_user(line)}: {get_message(line)}')
                pass
                #to-do
            elif 'PING :tmi.twitch.tv' in line:
                pong(c)
            elif ';bits=' in line:
                print('bit received')
                print(f'{get_user(line)} cheered {get_bits(line)} bits!')

