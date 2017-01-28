import click

from commands.drop_local_db import drop_local_db
from commands.generate_dummy_data import generate_dummy_data
from commands.local_config import local_config
from commands.runserver import runserver


@click.group()
def cli():
    pass


cli.add_command(local_config)
cli.add_command(runserver)
cli.add_command(generate_dummy_data)
cli.add_command(drop_local_db)

if __name__ == '__main__':
    cli()
