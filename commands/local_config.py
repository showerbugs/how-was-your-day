from click import command
from click import prompt
from jinja2 import Environment
from jinja2 import FileSystemLoader


@command()
def local_config():
    user = prompt('Enter your DB user', type=str)
    password = prompt('Enter your DB user\'s password '
                      '(You can pass this step, just push enter)',
                      type=str, default='', show_default=False)
    dbname = prompt('Enter your DB name', type=str, default='howwasyourday')
    dbhost = prompt('Enter your DB host', type=str, default='localhost')
    dbport = prompt('Enter your DB port', type=int, default=5432)
    test_dbname = prompt('Enter your TEST DB name',
                         type=str, default='howwasyourday_test')

    env = Environment(loader=FileSystemLoader('config'))
    tmpl = env.get_template('local.py.tmpl')
    localpy = tmpl.render(user=user, password=password, dbhost=dbhost,
                          dbport=dbport, dbname=dbname, test_dbname=test_dbname)
    with open('config/local.py', 'w') as fp:
        fp.write(localpy)
