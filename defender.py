# defender.py

import socket
import json
from datetime import datetime

HOST = 'localhost'
PORT = 11111

def log_to_file(message):
    with open("game_log.txt", "a", encoding='utf-8') as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - [DEFENDER] {message}\n")

print("🛡️ DEFENDER is listening...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            attack_data = json.loads(data.decode())
            action_name = attack_data['action']['name']
            log_to_file(f"Received attack: {action_name}")
