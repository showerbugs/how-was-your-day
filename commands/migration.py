import os

from click import command


@command()
def migration():
    os.system('alembic upgrade head')
