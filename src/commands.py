import click
from flask.cli import with_appcontext

from src import db, app

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db.create_all()
    click.echo('Initialized the database.')

app.cli.add_command(init_db_command)
