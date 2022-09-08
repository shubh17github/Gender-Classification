
from flask import Flask,render_template,request
from utils.function import gender_class


app=Flask(__name__)

@app.route('/')
def login():
    return render_template('home.html')


@app.route('/result',methods=['GET','POST'])

def pred():

    if request.method=='POST':
        data=request.form
        long_hair=int(data['LongHair'])
        forehead_width=float(data['ForeheadWidth'])
        forehead_height=float(data['ForeheadHeight'])
        nose_wide=int(data['NoseWide'])
        nose_long =int(data['NoseLong'])
        lips_thin =int(data['LipThin'])
        distance_nose_to_lip=int(data['DistanceNoseLip'])

        gender=gender_class(long_hair,forehead_width,forehead_height,nose_wide,nose_long,lips_thin,distance_nose_to_lip)

        result=gender.predict()
        return render_template('home.html',prediction=result)

if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080)




