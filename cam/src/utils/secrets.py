def get_pushover_token_and_userid():
    with open("/run/secrets/pushover_token", "r") as f:
        secrets=f.readlines()
    token = secrets[0]
    token = token.split("=")[1].strip().rstrip()
    userid = secrets[1]
    userid = userid.split("=")[1].strip().rstrip()
    return token, userid


