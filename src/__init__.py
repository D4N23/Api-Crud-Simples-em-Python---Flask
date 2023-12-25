from flask import Flask, request

def create_app(test_config=None):
    
    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        
        app.config.from_mapping(
            SECRET_KEY="dev",
            
        )
    else:
        app.config.from_mapping(test_config) 
        
    @app.route('/')
    def home():
        return ("Help me please")

    @app.get('/hello')
    def say_hello():
        return {"message":"Help me please"}  
    
    return app    