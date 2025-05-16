from flask import Blueprint, request, jsonify
from app.logic.attack import calculate_attack_success_chance
from app.logic.defense import calculate_defense_success_chance
from app.logic.atk_detection_calculation_3 import set_attack_detection_chance
from app.logic.def_detection_calculation_4 import set_defense_detection_chance

battle_bp = Blueprint('battle', __name__)

COUNTER_MAP = {
    "User Data Encryption": "Backup Recovery",
    "Persistence": "Process Isolation",
    "Privilege Escalation": "Access Invalidation",
    "Phishing": "Security Awareness Training",
    "Brute Force": "Limit Logon Attempts",
    "Vulnerability Scan": "Host-based IDS / Packet Filtering",
    "Malicious USB Drive": "User Access Pattern Analysis",
    "Whaling": "Sender Reputation Analysis / Auth",
    "Command and Control": "Network Traffic Filtering",
    "Credential Dumping": "Authentication Cache Invalidation",
    "Information Gathering": "Decoy Service",
    "Script Execution": "App Execution Control"
}

@battle_bp.route('/simulate', methods=['POST'])
def simulate_attack_defense():
    data = request.get_json()

    atk_action = data['attacker']['action']
    def_action = data['defender']['action']

    atk_name = atk_action.get("name", "")
    def_name = def_action.get("name", "")

    atk_data = {
        "action": atk_action,
        "attacker": data['attacker']['profile']
    }
    def_data = {
        "action": def_action,
        "defender": data['defender']['profile']
    }

    atk_chance = calculate_attack_success_chance(atk_data)
    def_chance = calculate_defense_success_chance(def_data)

    atk_detection = set_attack_detection_chance(
        atk_data["action"],
        atk_data["action"].get("action_type", "neutral"),
        atk_data["attacker"].get("skill", 0),
        atk_data["attacker"].get("insight", 0)
    )

    def_detection = set_defense_detection_chance(
        def_data["action"],
        def_data["action"].get("action_type", "neutral"),
        def_data["defender"].get("skill", 0),
        def_data["defender"].get("insight", 0)
    )



    if atk_name in COUNTER_MAP and COUNTER_MAP[atk_name] == def_name:
        atk_chance = 0
        def_chance = round(min(def_chance + 0.2, 1.0), 2)
        message = f"'{def_name}' neutralized '{atk_name}'."
    else:
        message = "No direct counter applied."

    return jsonify({
        
        "Tỷ lệ tấn công thành công": atk_chance,
        "Khả năng phát hiện phòng thủ": def_detection,
        "Cơ hội phòng thủ thành công": def_chance,
        "Khả năng phát hiện tấn công:": atk_detection,

        "counter_effect": message
    })