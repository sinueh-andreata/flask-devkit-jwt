import os
from app import app

if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'

    app.run(host='localhost', port=5000, debug=True, use_reloader=True, use_debugger=True)