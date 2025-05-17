def set_attack_detection_chance(action, action_type, skill, insight):
    if not action.get("detectable", False):
        return 0.0

    detection_chance = 0.2  
    tactics = action.get("tactics", [])
    support_tactics = ["Defense Evasion", "Exfiltration", "Command and Control"]

    # Bước 5–18: Xử lý từng tactic
    for tactic in tactics:
        if tactic == "Reconnaissance":
            continue 
        elif tactic in ["Resource Development", "Discovery"]:
            detection_chance += 0.1  
        elif tactic in ["Initial Access", "Execution", "Lateral Movement"]:
            detection_chance += 0.2  
        elif tactic in ["Persistence", "Privilege Escalation", "Credential Access", "Collection", "Impact"]:
            detection_chance += 0.3  


    if action_type == "stealthy":
        detection_chance -= 0.1
    elif action_type == "visible":
        detection_chance = min(1.0, 2 * detection_chance)


    for st in support_tactics:
        if st in tactics:
            detection_chance += 0.1


    detection_chance += 0.05 * skill
    detection_chance += 0.02 * insight

    return round(max(0.0, min(detection_chance, 1.0)), 4)
