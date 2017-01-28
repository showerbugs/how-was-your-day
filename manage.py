import click

from commands.local_config import local_config
from commands.runserver import runserver
from commands.generate_dummy_data import generate_dummy_data


@click.group()
def cli():
    pass


cli.add_command(local_config)
cli.add_command(runserver)
cli.add_command(generate_dummy_data)

if __name__ == '__main__':
    cli()
