from flask import jsonify

def calculate_attack_success_chance(data):
    atk = data['action']
    attacker = data['attacker']
    chance = 0.5

    for tactic in atk['tactics']:
        if tactic == "Reconnaissance":
            chance += 0.2
        elif tactic in ["Resource Development", "Discovery"]:
            chance += 0.1
        elif tactic in ["Execution", "Lateral Movement", "Collection", "Impact"]:
            continue
        elif tactic in ["Initial Access", "Persistence", "Privilege Escalation", "Credential Access"]:
            chance -= 0.1

    if atk["skill_req"] == 2:
        chance += 0.1
    if atk["skill_req"] == 1:
        chance += 0.2
    if attacker["long_term"]:
        chance += 0.1
    if atk["physical_access"] and not attacker["has_physical_access"]:
        chance -= 0.2
    if atk["admin_required"] and attacker["has_admin"]:
        chance += 0.2

    for st in atk.get("support_tactics", []):
        if st in atk["tactics"]:
            chance += 0.1

    chance += 0.05 * attacker["skill"]
    chance += 0.02 * attacker["insight"]

    return round(min(chance, 0.99), 2)