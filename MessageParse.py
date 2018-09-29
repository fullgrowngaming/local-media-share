import re

def get_user(line):
    return re.findall(r'display-name=(.*?);', line)[0]


def get_message(line):
    temp = line.split(' :')[2]
    return temp


def bits_parse(line):
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

