# defense_calculator_2.py

def calculate_defense_success_chance(data):
    action = data['action']
    defender = data['defender']

    success_chance = 0.5
    tactics = action['tactics']

    for tactic in tactics:
        if tactic in ["Eviction", "Isolation"]:
            success_chance += 0.2
        elif tactic == "Recovery":
            success_chance += 0.1
        elif tactic in ["Analysis", "Monitoring"]:
            success_chance += 0.0
        elif tactic in ["Hardening", "Deception"]:
            continue

    if action["skill_req"] == 2:
        success_chance += 0.1
    if action["skill_req"] == 1:
        success_chance += 0.2
    if defender["long_term"]:
        success_chance += 0.1
    if action.get("admin_required", False) and defender.get("has_admin", False):
        success_chance -= 0.1

    success_chance += 0.05 * defender["skill"]
    success_chance += 0.02 * defender["insight"]

    return round(min(success_chance, 1.0), 2)
