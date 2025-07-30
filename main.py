import os
from flask import Flask, jsonify, request

app = Flask (__name__)

@app.route('/', methods=['GET'])
def welcome():
  if(request.method == 'GET'):
    app_name = os.getenv('APP_NAME', 'Default Flask App')
    welcome_message = os.getenv('WELCOME_MESSAGE', 'Welcome to my Flask App!')

    data = {
        "app_name": app_name,
        "message": welcome_message
    }
    return jsonify(data)

@app.route('/config', methods=['GET'])
def get_config():
  if(request.method == 'GET'):
    config_data = {
        "app_name": os.getenv('APP_NAME', 'Not Set'),
        "environment": os.getenv('ENVIRONMENT', 'Not Set'),
        "database_url": os.getenv('DATABASE_URL', 'Not Set'),
        "debug_mode": os.getenv('DEBUG_MODE', 'false')
    
    }
    return jsonify(data)
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9001)
