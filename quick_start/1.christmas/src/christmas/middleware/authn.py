from christmas.middleware import token


def init_auth():
    print("start initialization authentication")
    print("token:", token.token())
