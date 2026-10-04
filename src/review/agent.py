TOOLS = ["lint_diff", "comment"]
WRITES = ("merge", "approve",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    diff = payload.get("diff") or ""; result = ["latest_tag"] if ":latest" in diff else []
    return {"refused": False, "tools": TOOLS, "findings": result, "wrote": False, "applied": False}
