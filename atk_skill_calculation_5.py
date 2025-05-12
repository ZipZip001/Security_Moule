def set_attack_skill_requirement(complexity, target, permissions, interaction, stages):
    skill_req = 1

    for stage in stages:
        if stage == "Reconnaissance":
            if target != "none":
                skill_req += 1
        elif stage in ["InitialAccess", "Execution"]:
            skill_req += 1

    # complexity
    if complexity == "medium":
        skill_req += 1
    elif complexity == "high":
        skill_req += 2

    # permissions
    if permissions == "user":
        skill_req -= 1
    elif permissions == "admin":
        pass
    elif permissions == "system":
        skill_req += 1

    if interaction:
        skill_req -= 1

    return max(skill_req, 0)
