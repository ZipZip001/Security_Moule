from flask import Blueprint, request, jsonify
from app.logic.attack import calculate_attack_success_chance
from app.logic.defense import calculate_defense_success_chance
from app.logic.atk_detection_calculation_3 import set_attack_detection_chance
from app.logic.def_detection_calculation_4 import set_defense_detection_chance
from app.logic.atk_skill_calculation_5 import set_attack_skill_requirement
from app.logic.def_skill_calculation_6 import set_defense_skill_requirement
from app.logic.damage_impact_calculation_7 import confidentiality_damage_impact
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

@battle_bp.route('/atk_def_chancechance', methods=['POST'])
def simulate_attack_defense():
    data = request.get_json()

    atk_action = data['attacker']['action']
    def_action = data['defender']['action']

    atk_name = atk_action.get("name", "")
    def_name = def_action.get("name", "")

    atk_data = {
        "action": atk_action,
        "attacker": data['attacker']['actor']
    }
    def_data = {
        "action": def_action,
        "defender": data['defender']['actor']
    }

    atk_chance = calculate_attack_success_chance(atk_data)
    def_chance = calculate_defense_success_chance(def_data)

    if atk_name in COUNTER_MAP and COUNTER_MAP[atk_name] == def_name:
        atk_chance = 0
        def_chance = round(min(def_chance + 0.2, 1.0), 2)
        message = f"'{def_name}' neutralized '{atk_name}'."
    else:
        message = "No direct counter applied."

    return jsonify({
        
        "Tỷ lệ tấn công thành công": atk_chance,
        "Cơ hội phòng thủ thành công": def_chance,
        "counter_effect": message
    })

@battle_bp.route('/attack_detection', methods=['POST'])
def attack_detection():
    data = request.get_json()
    chance = set_attack_detection_chance(
        data["action"],
        data.get("action_type", "neutral"),
        data.get("skill", 0),
        data.get("insight", 0)
    )
    return jsonify({"attack_detection_chance": chance})

@battle_bp.route('/defense_detection', methods=['POST'])
def defense_detection():
    data = request.get_json()
    chance = set_defense_detection_chance(
        data["action"],
        data.get("action_type", "neutral"),
        data.get("skill", 0),
        data.get("insight", 0)
    )
    return jsonify({"defense_detection_chance": chance})

@battle_bp.route('/attack_skill_requirement', methods=['POST'])
def attack_skill_requirement():
    data = request.get_json()
    skill = set_attack_skill_requirement(
        data.get("complexity", "low"),
        data.get("target", "none"),
        data.get("permissions", "user"),
        data.get("interaction", False),
        data.get("stages", [])
    )
    return jsonify({"attack_skill_required": skill})

@battle_bp.route('/defense_skill_requirement', methods=['POST'])
def defense_skill_requirement():
    data = request.get_json()
    skill = set_defense_skill_requirement(
        data.get("complexity", "low"),
        data.get("long_term", False),
        data.get("types", [])
    )
    return jsonify({"defense_skill_required": skill})

@battle_bp.route('/confidentiality_damage', methods=['POST'])
def confidentiality_damage():
    data = request.get_json()

    skill_req = data.get("skill_req", 1)
    applicability = data.get("applicability", 1)
    stages = data.get("stages", [])

    damage = confidentiality_damage_impact(skill_req, applicability, stages)

    return jsonify({
        "confidentiality_damage": damage
    })

