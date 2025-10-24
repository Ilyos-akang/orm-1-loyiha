from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"
db=SQLAlchemy(app)

class Talaba(db.Model):
    id=db.Column (db.Integer, primary_key=True)
    ismi=db.Column(db.String(100),nullable=False)
    t_yil=db.Column(db.String(100),nullable=False)
    kurs=db.Column(db.Integer,nullable=False)
    yunalish=db.Column(db.String(100),nullable=False)
    guruh=db.Column(db.Integer,nullable=False)


    def __repr__(self):
        return f"talabaning ismi:{self.ismi},talabaning tug'ilgan yili:{self.t_yil}, tahsil olayotgan kurs: {self.kurs}, yo'nalish {self.yunalish},  guruh raqami {self.guruh}"
    

@app.route("/",methods=["GET","POST"])
def index():
            if request.method=="POST":
                ismi=request.form.get("ismi")
                t_yil=request.form.get("t_yil")
                kurs=request.form.get("kurs")
                yunalish=request.form.get("yunalish")
                guruh=request.form.get("guruh")

                talaba1=Talaba(ismi=ismi,
                               t_yil=t_yil,
                               kurs=int(kurs),
                               yunalish=yunalish,
                               guruh=int(guruh))
                db.session.add(talaba1)
                db.session.commit()

            return render_template("index.html")
        

if __name__=="__main__":
            with app.app_context():
                db.create_all()
            app.run(debug=True)