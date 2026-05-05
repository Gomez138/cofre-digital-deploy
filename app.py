#app/app.py - Nossa aplicação que precisa de segredos 
 
from flask import Flask, jsonify 
import os 
import logging 
app = Flask(__name__) cd
 
•	Configurando logging (importante para máscaras) 
logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__) 
@app.route('/') 
def home(): 
    return jsonify({ 
        "message": " Cofre Digital Online!", 
        "environment": os.getenv('ENVIRONMENT', 'unknown'), 
        "version": os.getenv('APP_VERSION', '1.0.0') 
 
    }) 
@app.route('/database') 
def database_info(): 
 
•	Simulando conexão com banco (usando segredos) 
    db_host = os.getenv('DB_HOST', 'localhost') 
    db_user = os.getenv('DB_USER', 'user') 
    db_password = os.getenv('DB_PASSWORD', 'SENHA_NAO_CONFIGURADA')
   
     Atenção! Nunca logar senhas reais!  
    logger.info(f"Conectando ao banco: {db_host} com usuário: {db_user}") 
 
    Nunca façam isso: #logger.info(f"Senha: {db_password}")      
    return jsonify({  
        "status": "connected" if db_password != 'SENHA_NAO_CONFIGURADA' else "not_configured", 
        "host": db_host, 
        "user": db_user,
        "password_configured": db_password != 'SENHA_NAO_CONFIGURADA' 
    }) 
@app.route('/api-key') 
def api_key_info(): 
 
