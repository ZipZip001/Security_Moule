# attacker.py

from flask import Flask, request, jsonify
from datetime import datetime
from attack_calculator_1 import calculate_success_chance
from defense_calculator_2 import calculate_defense_success_chance
from atk_detection_calculation_3 import set_attack_detection_chance
from def_detection_calculation_4 import set_defense_detection_chance
from atk_skill_calculation_5 import set_attack_skill_requirement
from def_skill_calculation_6 import set_defense_skill_requirement

app = Flask(__name__)

def log_to_file(message):
    with open("game_log.txt", "a", encoding='utf-8') as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {message}\n")

@app.route('/attack', methods=['POST'])
def attack():
    data = request.json

    attacker_info = data.get("attacker")
    defender_info = data.get("defender")
    action = data.get("action")

    atk_chance = calculate_success_chance(data)
    def_chance = calculate_defense_success_chance(data)
    atk_detection = set_attack_detection_chance(action, "visible", attacker_info["skill"], attacker_info["insight"])
    def_detection = set_defense_detection_chance(action, "visible", defender_info["skill"], defender_info["insight"])
    atk_skill_req = set_attack_skill_requirement("medium", "specific", "admin", False, ["InitialAccess", "Execution"])
    def_skill_req = set_defense_skill_requirement("medium", True, ["Prevention", "Response"])

    log_to_file(f"-------------------------------------------------------------")
    log_to_file(f"[ATTACKER] Action: {action['name']}")
    log_to_file(f"[ATTACKER] Success Chance: {atk_chance * 100:.2f}%")
    log_to_file(f"[DEFENDER] Success Chance: {def_chance * 100:.2f}%")
    log_to_file(f"[ATTACKER] Detection Chance: {atk_detection * 100:.2f}%")
    log_to_file(f"[DEFENDER] Detection Chance: {def_detection * 100:.2f}%")
    log_to_file(f"[ATTACKER] Skill Requirement: {atk_skill_req}")
    log_to_file(f"[DEFENDER] Skill Requirement: {def_skill_req}")

    return jsonify({
        "atk_chance": atk_chance,
        "def_chance": def_chance,
        "atk_detection": atk_detection,
        "def_detection": def_detection,
        "atk_skill_req": atk_skill_req,
        "def_skill_req": def_skill_req
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)