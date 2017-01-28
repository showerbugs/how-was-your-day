import click

from commands.create_local_db import create_local_db
from commands.drop_local_db import drop_local_db
from commands.generate_dummy import generate_dummy
from commands.local_config import local_config
from commands.migration import migration
from commands.runserver import runserver


@click.group()
def cli():
    pass


cli.add_command(local_config)
cli.add_command(runserver)
cli.add_command(migration)
cli.add_command(generate_dummy)
cli.add_command(drop_local_db)
cli.add_command(create_local_db)

if __name__ == '__main__':
    cli()
