def set_defense_detection_chance(action, action_type, skill, insight):
    detection_chance = 0.5  # Initialize base chance
    tactics = action.get("tactics", [])

    # Bước 5–13: Tactics chính
    for tactic in tactics:
        if tactic in ["Eviction", "Isolation"]:
            detection_chance += 0.3  # Response type 1
        elif tactic == "Recovery":
            detection_chance += 0.2  # Response type 2
        elif tactic in ["Analysis", "Monitoring"]:
            detection_chance -= 0.3  # Detection (gây nhầm lẫn nên giảm)
        elif tactic in ["Hardening", "Deception"]:
            continue  # Prevention – không thay đổi

    # Bước 14–16: Stealthy
    if action_type == "stealthy":
        detection_chance -= 0.1

    # Bước 17–19: Visible
    if action_type == "visible":
        detection_chance = min(1.0, 2 * detection_chance)

    # Bước 20–23: Skill & Insight modifiers
    detection_chance += 0.05 * skill
    detection_chance += 0.02 * insight

    return round(max(0.0, min(detection_chance, 0.99)), 4)
