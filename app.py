import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src import create_app
from src.config import ConfigDev, ConfigProd

config_class = ConfigProd if os.getenv('FLASK_ENV') == 'production' else ConfigDev

app = create_app(config_class)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = config_class.DEBUG
    
    app.run(host='0.0.0.0', port=port, debug=debug)