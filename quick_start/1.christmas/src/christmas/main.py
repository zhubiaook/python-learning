import sys

from christmas import helper
from christmas.middleware import authn


def run():
    print(sys.path)
    helper.init_db()
    authn.init_auth()


if __name__ == "__main__":
    run()
