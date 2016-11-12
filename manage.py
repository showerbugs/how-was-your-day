import click

from commands.local_config import local_config


@click.group()
def cli():
    pass


cli.add_command(local_config)


if __name__ == '__main__':
    cli()
