import click

from commands.local_config import local_config
from commands.runserver import runserver


@click.group()
def cli():
    pass


cli.add_command(local_config)
cli.add_command(runserver)

if __name__ == '__main__':
    cli()
