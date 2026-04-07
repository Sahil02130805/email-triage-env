def grade_action(task, action):

    expected = task["expected"]
    score = 0.0

    if action.category == expected.get("category"):
        score += 0.4

    if action.priority == expected.get("priority"):
        score += 0.3

    if "escalate" in expected:
        if action.escalate == expected["escalate"]:
            score += 0.2

    if len(action.response) > 20:
        score += 0.1

    return score, "graded"