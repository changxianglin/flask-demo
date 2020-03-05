from application import app,manage
from flask_script import Server
import www


## web server
manage.add_command('runserver', Server( host='0.0.0.0',port=app.config['SERVER_PORT'], use_debugger=True, use_reloader=True))


def main():
    manage.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()