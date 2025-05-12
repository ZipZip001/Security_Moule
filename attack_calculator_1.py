# attack_calculator_1.py

def calculate_success_chance(data):
    action = data['action']
    attacker = data['attacker']

    success_chance = 0.5
    tactics = action['tactics']
    support_tactics = action.get('support_tactics', [])

    for tactic in tactics:
        if tactic == "Reconnaissance":
            success_chance += 0.2
        elif tactic in ["Resource Dev.", "Discovery"]:
            success_chance += 0.1
        elif tactic in ["Execution", "Lateral Movement", "Collection", "Impact"]:
            success_chance += 0.0
        elif tactic in ["Initial Access", "Persistence", "Privilege Escalation", "Credential Access"]:
            success_chance -= 0.1

    if action["skill_req"] == 2:
        success_chance += 0.1
    if action["skill_req"] == 1:
        success_chance += 0.2
    if attacker["long_term"]:
        success_chance += 0.1
    if action["physical_access"] and not attacker["has_physical_access"]:
        success_chance -= 0.2
    if action["admin_required"] and attacker["has_admin"]:
        success_chance += 0.2

    for st in support_tactics:
        if st in tactics:
            success_chance += 0.1

    success_chance += 0.05 * attacker["skill"]
    success_chance += 0.02 * attacker["insight"]

    return round(min(success_chance, 1.0), 2)
