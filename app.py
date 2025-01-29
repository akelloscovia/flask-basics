from flask import Flask
app = Flask(__name__)   #Creating app instance 
@app.route('/')
def home():
  return "Akello_Scovia_emaru"

# if __name__=='_main_':
#      app.run(debug=True) 
