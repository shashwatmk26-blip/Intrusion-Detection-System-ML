import datetime

def current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def log_attack(attack):

    with open("attack_log.txt","a") as file:

        file.write(current_time()+" : "+attack+"\n")