import utils

def format_document(doc):
    action = doc.get("action")
    author = doc.get("author")
    to_branch = doc.get("to_branch")
    from_branch = doc.get("from_branch")
    timestamp = utils.format_utc(doc.get("timestamp"))

    if action == "PUSH":
        return f'{author} pushed to "{to_branch}" on {timestamp}'
    elif action == "PULL_REQUEST":
        return f'{author} submitted a pull request from "{from_branch}" to "{to_branch}" on {timestamp}'
    elif action == "MERGE":
        return f'{author} merged branch "{from_branch}" to "{to_branch}" on {timestamp}'
    else:
        return "Unknown action"
