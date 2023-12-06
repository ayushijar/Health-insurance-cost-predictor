from flask import Flask,request,render_template
from prediction import Predictions
import shutil
import os


des = os.path.abspath('templates')

app = Flask(__name__)


@app.route("/")
def intro():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
    if request.method =='POST':
        try:

            age = int(request.form.get("age"))
            sex = request.form.get("sex")
            bmi = float(request.form.get("bmi"))
            child = int(request.form.get("child"))
            smoke = request.form.get("smoke")
            reg = request.form.get("reg")

            p = Predictions(age,sex,bmi,child,smoke,reg)
            predic = p.predict()

            return render_template('results.html',predic=predic)
    
    
        except Exception as e:

            print("The exception has raised",e)
            return "Something went wrong :("

    else:
        return render_template('index.html')


if __name__ == '__main__':

    app.run(debug=True)