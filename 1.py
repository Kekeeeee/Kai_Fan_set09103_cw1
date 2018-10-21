from flask import Flask, render_template
app = Flask(__name__)

@app.route('/repair.html/')
def repair():
   return render_template('repair.html'), 200

@app.route('/maintain.html/')
def maintain():
    return render_template('maintain.html'), 200

@app.route('/login.html/')
def login():
   return render_template('login.html'), 200

@app.route('/index.html/')
def index():
    return render_template('index.html'), 200

@app.route('/details.html/')
def details():
    return render_template('details.html'), 200

@app.route('/contact.html/')
def contact():
    return render_template('contact.html'), 200

@app.route('/shop.html/')
def shop():
   return render_template('shop.html'), 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
