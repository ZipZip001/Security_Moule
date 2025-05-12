def confidentiality_damage_impact(skill_req, applicability, stages):
    if applicability <= 0:
        return 0

    damage = 0

    for stage in stages:
        if stage == "Reconnaissance":
            damage += 0
        elif stage == "InitialAccess":
            damage += 1
        elif stage == "Execution":
            damage += 2

    if skill_req in [1]:
        damage += 1
    elif skill_req in [2, 3]:
        damage += 2
    elif skill_req in [4, 5]:
        damage += 3

    if applicability == 1:
        damage -= 2
    elif applicability == 2:
        damage -= 1
    elif applicability == 3:
        damage += 1

    return max(damage, 0)
