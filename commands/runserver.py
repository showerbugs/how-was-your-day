import os

from click import command


@command()
def runserver():
    os.system('flask run')
