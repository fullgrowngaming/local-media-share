from Connection import *
from MessageParse import *

c = open_connection()
join_room(c)
read_buffer = ''

while True:
        read_buffer = read_buffer + str(c.recv(1024))
        temp = read_buffer.split('\\r\\n')
        read_buffer = temp.pop()

        for line in temp:
            if ' PRIVMSG #' in line:
                if ';bits=' in line:
                    print(f'{get_user(line)} cheered {bits_parse(line)} bits!')

            elif ' USERNOTICE ' in line:
                if 'msg-id=submysterygift' in line:
                    pass

                if 'msg-id=subgift' in line:
                    parsed_gift_sub = gift_sub_parse(line)
                    print(f'{parsed_gift_sub[0]} gifted {parsed_gift_sub[1]} a tier {parsed_gift_sub[3]} sub!')
                    break

                if 'msg-id=sub' in line:
                    parsed_sub = sub_parse(line)
                    print(f'{parsed_sub[0]} just subscribed with a Tier {parsed_sub[1]}!')

                if 'msg-id=resub' in line:
                    parsed_resub = resub_parse(line)
                    print(f'{parsed_resub[0]} just subscribed for {parsed_resub[1]} months in a row!,'
                          f' (Tier {parsed_resub[2]})')


            elif 'PING :tmi.twitch.tv' in line:
                pong(c)


