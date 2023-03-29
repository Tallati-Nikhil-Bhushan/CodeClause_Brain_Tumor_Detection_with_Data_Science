from flask import Flask, render_template, request, redirect
from details import models
import numpy as np
import pickle
from PIL import Image
from keras.models import load_model

app = Flask(__name__,template_folder='templates')

@app.route('/')
def hello_world():
    return render_template('index.html',models=models)

@app.route('/predictor/brain',methods=['GET','POST'])
def bt_predictor():
    if request.method=='POST':

        loaded_model = load_model('./prediction_models/brain_tumor.h5')
        f = request.files['file']
        f.save("./static/images/important.jpeg") 
        img = Image.open("./static/images/important.jpeg")
        x = np.array(img.resize((128,128)))
        x = x.reshape(1,128,128,3)
        res = loaded_model.predict_on_batch(x)
        prediction = np.where(res == np.amax(res))[1][0]
        return render_template('form.html',name="brain",models=models,prediction=prediction)
    
    return render_template('form.html',name="brain",models=models,prediction=-1)

@app.route('/<name>')
def nav_links(name):
    return render_template(f"{name}.html")

if __name__ == '__main__':
    app.run(debug=True,port=8000)
