def get_token() -> str:
    with open('Main/token.txt') as f:
        return str(f.read())
