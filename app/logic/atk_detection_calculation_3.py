def set_attack_detection_chance(action, action_type, skill, insight):
    if not action.get("detectable", False):
        return 0.0

    detection_chance = 0.2  # Initialize base detection chance
    tactics = action.get("tactics", [])
    support_tactics = ["Defense Evasion", "Exfiltration", "Command and Control"]

    # Bước 5–18: Xử lý từng tactic
    for tactic in tactics:
        if tactic == "Reconnaissance":
            continue  # Stage 1: No change
        elif tactic in ["Resource Development", "Discovery"]:
            detection_chance += 0.1  # Stage 2
        elif tactic in ["Initial Access", "Execution", "Lateral Movement"]:
            detection_chance += 0.2  # Stage 3
        elif tactic in ["Persistence", "Privilege Escalation", "Credential Access", "Collection", "Impact"]:
            detection_chance += 0.3  # Stage 3+

    # Bước 19–22: Stealth/visible
    if action_type == "stealthy":
        detection_chance -= 0.1
    elif action_type == "visible":
        detection_chance = min(1.0, 2 * detection_chance)

    # Bước 23–28: Support tactics
    for st in support_tactics:
        if st in tactics:
            detection_chance += 0.1

    # Bước 30–31: Skill & Insight modifiers
    detection_chance -= 0.05 * skill
    detection_chance += 0.02 * insight

    # Bước 32–33: Clamp to [0, 1]
    return round(max(0.0, min(detection_chance, 1.0)), 4)
