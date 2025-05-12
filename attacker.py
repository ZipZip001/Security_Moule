# attacker.py

import socket
import json
from datetime import datetime
from attack_calculator_1 import calculate_success_chance
from defense_calculator_2 import calculate_defense_success_chance
from atk_detection_calculation_3 import set_attack_detection_chance
from def_detection_calculation_4 import set_defense_detection_chance
from atk_skill_calculation_5 import set_attack_skill_requirement
from def_skill_calculation_6 import set_defense_skill_requirement

HOST = 'localhost'
PORT = 11111

def log_to_file(message):
    with open("game_log.txt", "a", encoding='utf-8') as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {message}\n")

attacker_info = {
    "skill": 3,
    "insight": 4,
    "long_term": True,
    "has_admin": True,
    "has_physical_access": False
}

defender_info = {
    "skill": 2,
    "insight": 3,
    "long_term": True,
    "has_admin": True
}

action = {
    "name": "Initial Access - Spearphishing",
    "tactics": ["Initial Access", "Discovery"],
    "support_tactics": ["Command and Control"],
    "skill_req": 2,
    "admin_required": True,
    "physical_access": False,
    "detectable": True
}

data = {
    "action": action,
    "attacker": attacker_info,
    "defender": defender_info
}

# Calculate all metrics
atk_chance = calculate_success_chance(data)
def_chance = calculate_defense_success_chance(data)
atk_detection = set_attack_detection_chance(action, "visible", attacker_info["skill"], attacker_info["insight"])
def_detection = set_defense_detection_chance(action, "visible", defender_info["skill"], defender_info["insight"])
atk_skill_req = set_attack_skill_requirement("medium", "specific", "admin", False, ["InitialAccess", "Execution"])
def_skill_req = set_defense_skill_requirement("medium", True, ["Prevention", "Response"])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(json.dumps(data).encode())

# Ghi vào game_log.txt
log_to_file(f"-------------------------------------------------------------")
log_to_file(f"[ATTACKER] Action: {action['name']}")
log_to_file(f"[ATTACKER] Success Chance: {atk_chance * 100:.2f}%")
log_to_file(f"[DEFENDER] Success Chance: {def_chance * 100:.2f}%")
log_to_file(f"[ATTACKER] Detection Chance: {atk_detection * 100:.2f}%")
log_to_file(f"[DEFENDER] Detection Chance: {def_detection * 100:.2f}%")
log_to_file(f"[ATTACKER] Skill Requirement: {atk_skill_req}")
log_to_file(f"[DEFENDER] Skill Requirement: {def_skill_req}")
