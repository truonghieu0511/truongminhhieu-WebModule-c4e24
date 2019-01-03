from flask import Flask
app = Flask(__name__)
@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    height = height / 100
    bmi = round(weight/(height**2),2)
    if bmi < 16:
        return "BMI của bạn :" + str(bmi) + "quá gầy"
    elif bmi < 18.5:
        return "BMI của bạn :" + str(bmi) + "gầy"
    elif bmi < 25:
        return "BMI của bạn :" + str(bmi) + "bình thường"
    elif bmi < 30:
        return "BMI của bạn :" + str(bmi) + "thừa cân"
    else:
        return "BMI của bạn :" + str(bmi) + "béo phì"
if __name__ == '__main__':
    app.run(debug=True)