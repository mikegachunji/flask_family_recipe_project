#################
#### imports ####
#################
 
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
 
################
#### config ####
################
 
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
 
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"
 
 
from ffr_env.models import User
 
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
 
####################
#### blueprints ####
####################
 
from ffr_env.users.views import users_blueprint
from ffr_env.recipes.views import recipes_blueprint
 
# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(recipes_blueprint)