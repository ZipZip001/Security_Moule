def set_defense_detection_chance(action, action_type, skill, insight):
    detection_chance = 0.5  
    tactics = action.get("tactics", [])

    for tactic in tactics:
        if tactic in ["Eviction", "Isolation"]:
            detection_chance += 0.3  
        elif tactic == "Recovery":
            detection_chance += 0.2  
        elif tactic in ["Analysis", "Monitoring"]:
            detection_chance -= 0.3 
        elif tactic in ["Hardening", "Deception"]:
            continue  

    if action_type == "stealthy":
        detection_chance -= 0.1

    if action_type == "visible":
        detection_chance = min(1.0, 2 * detection_chance)

    detection_chance += 0.05 * skill
    detection_chance += 0.02 * insight

    return round(max(0.0, min(detection_chance, 0.99)), 4)
