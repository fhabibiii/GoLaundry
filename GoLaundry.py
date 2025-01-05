import paho.mqtt.client as mqtt
import time
import random
import threading

broker_address = "localhost"
port = 3333
idClient = f'python-mqtt-{random.randint(0, 100)}'

def connect():
    def on_connect(client,userdata,flags,RC):
        if (RC == 0):
            print("Connected (type exit to leave)")
            publish(client, "connected_code", username)
        else:
            print("Failed to connect")
    client = mqtt.Client(idClient)
    client.on_connect = on_connect
    client.connect(broker_address,port)
    return client
    
def publish(client, pesan, username):
    i = 0
    msg = f"{username}: {pesan}"
    hasil = client.publish(topik, msg)
    status = hasil[0]
    if status == 0:
        pass
    else:
        print("Failed to send")
    i += 1

def subscribe(client: mqtt):
    def on_message(client, userdate, msg):
        pesan = str(f"{msg.payload.decode()}")
        username, pesan = pesan.split(":")
        if pesan.find("connected_code") != -1:
            print(f"{username} has joined")
        elif pesan.find("exit_code") != -1:
            print(f"{username} has leave")
        elif pesan.find("exit") != -1:
            pass
        else:
            print(f"{msg.payload.decode()}")
    client.subscribe(topik)
    client.on_message = on_message

def run():
    client = connect()
    x = threading.Thread(target = subscribe, args = (client, ))
    x.start()
    y = threading.Thread(target = client.loop_forever, args = (1, ))
    y.start()
    pesan = ""
    while (pesan != "exit"):
        pesan = input()
        if (pesan != ""):
            publish(client, pesan, username)
        time.sleep(1)
    publish(client, "exit_code", username)
    time.sleep(1)
    client.disconnect()
    x.join()
    y.join()

if __name__ == "__main__":
    username = input("Username: ")
    while True:
        print("""
====== GoLaundry ======
1. Laundry Bojong (1 Hari)
2. Laundry Soang (3 Hari)
0. Exit
=======================""")   
        menu = input("Select: ")
        print()
        if menu == "1" or menu == "Laundry Bojong":
            topik = "/Laundry/Bojong/1Hari"
            run()
        elif menu == "2" or menu == "Laundry Soang":
            topik = "/Laundry/Soang/3Hari"
            run()
        elif menu == "0" or menu == "Exit":
            print("Exit The Program")
            break
        else:
            print("Invalid Input")
    exit()