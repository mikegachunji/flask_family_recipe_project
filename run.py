# run.py
 
# Add your settings here... this is a temporary location, as the settings for a Flask app
# should be stored separate from your main program.
DEBUG = True
 
from ffr_env import app
 
if __name__ == "__main__":
   app.run()