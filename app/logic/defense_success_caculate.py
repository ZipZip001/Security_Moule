def calculate_defense_success_chance(data):
    act = data['action']
    defender = data['defender']
    chance = 0.5

    for tactic in act['tactics']:
        if tactic in ["Eviction", "Isolation"]:
            chance += 0.2
        elif tactic == "Recovery":
            chance += 0.1
        elif tactic in ["Analysis", "Monitoring", "Hardening", "Deception"]:
            continue

    if act["skill_req"] == 2:
        chance += 0.1
    if act["skill_req"] == 1:
        chance += 0.2
    if defender["long_term"]:
        chance += 0.1
    if act.get("admin_required") and defender.get("has_admin"):
        chance -= 0.1

    chance += 0.05 * defender["skill"]
    chance += 0.02 * defender["insight"]

    return round(min(chance, 0.99), 2)