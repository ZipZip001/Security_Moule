def set_defense_skill_requirement(complexity, long_term, types):
    skill_req = 1

    for t in types:
        if t in ["Prevention", "Response"]:
            skill_req += 1

    if complexity == "medium":
        skill_req += 1
    elif complexity == "high":
        skill_req += 2

    if long_term:
        skill_req += 1

    return max(skill_req, 0)
