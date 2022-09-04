
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Resto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Resto(db.Model):
    # sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, primary_key = True)
    price = db.Column(db.String(10) ,  nullable=False)
   
    def __repr__(self) -> str:
        return f"{self.title} - {self.price}"

@app.route('/')
def homepage():
    return render_template('index.html')
@app.route('/admin', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        name = request.form['title']
        price =request.form['price']
        r = Resto(title=name, price = price)
        db.session.add(r)
        db.session.commit()
    
    alls = Resto.query.all()
    return render_template('admin.html', alls = alls)

@app.route('/delete/<title>')
def delete(title):
    here = Resto.query.filter_by(title=title).first()
    db.session.delete(here)
    db.session.commit()
    return redirect("/")

@app.route("/order/")
def order():
    alls = Resto.query.all()
    return render_template("order.html", alls=alls)



@app.route('/update/<title>', methods=['GET', 'POST'])
def update(title):
    if request.method=="POST":
        newname = request.form["title"]
        newprice = request.form["price"]
        todo  = Resto.query.filter_by(title=title).first()
        todo.title = newname
        todo.price = newprice  
        db.session.add(todo)
        db.session.commit()
        return redirect("/")    
    change = Resto.query.filter_by(title=title).first()
    return render_template("update.html", change=change)
    
if __name__=="__main__":
    app.run(debug=True)