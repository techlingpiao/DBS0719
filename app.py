from flask import Flask,request,render_template
import joblib
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("Regression")
        r1 = model1.predict([[rates]])
        
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        
        model3 = joblib.load("randomForest")
        r3 = model3.predict([[rates]])
        
        model4 = joblib.load("gradientBoosting")
        r4 = model4.predict([[rates]])
        
        model5 = joblib.load("svm")
        r5 = model5.predict([[rates]])
        
        model6 = joblib.load("neuralNet")
        r6 = model6.predict([[rates]])
        return (render_template("index.html",result1 = r1 ,result2=r2,result3 = r3 , result4 = r4, result5 = r5,result6=r6))
    else:
        return (render_template("index.html",result1 = "WAITTING", result2 = "WAITTING", result3 = "WAITTING", result4 = "WAITTING", result5 = "WAITTING", result6 = "WAITTING"))
if __name__ == "__main__":
    app.run()