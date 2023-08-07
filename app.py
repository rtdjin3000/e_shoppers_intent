# 1. Library imports
import uvicorn
from fastapi import FastAPI, Request
import numpy as np
import pickle
import pandas as pd
from osi import osi

# 2. Create the app object
app = FastAPI()
model = pickle.load(open('osi_gbm.pkl', 'rb'))

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.post('/predict')
def predict(data:osi):
    data=data.dict()
    def Encoding_Month(month):
        num = 0
        if month == 'February':
            num=2
        elif month == 'March'or month == 'April':
            num=5
        elif month == 'May':
            num=6
        elif month == 'June':
            num=4
        elif month == 'July':
            num=3
        elif month == 'August':
            num=0
        elif month == 'September':
            num=9
        elif month == 'October':
            num=8
        elif month == 'November':
            num=7
        elif month == 'Descember' or month=='January':
            num=1
    
        return num

    def Encoding_Visitor(vis):
        num = 0
        if vis == 'Returning Visitor':
            num = 2
        elif vis == 'New Visitor':
            num = 0
        elif vis == 'Other':
            num = 1

        return num

    def Encoding_weekend(Weekend):
        num = 0
        if Weekend == 'True':
            num = 1
        elif Weekend == 'False':
            num = 0
        return num


    mean = [5228.289588354559,
        1350.3003767343155,
        2228.8511406021103,
        1.6308603553860055,
        0.04701054003755943,
        15.070402452799382,
        3.063447445035639,
        5.232506776428069]

    std =  [33855.16236319768,
        11714.049416369837,
        15173.139612558776,
        0.7571679042941348,
        0.169662213903642,
        29.5744024822749,
        2.3508388396800353,
        2.3483951485421475]



    browser = request.form.get('browser')
    pro_page = request.form.get('pro_page')
    pro_time = request.form.get('pro_time')
    inf_page = request.form.get('inf_page')
    inf_time = request.form.get('inf_time')
    adm_page = request.form.get('adm_page')
    adm_time = request.form.get('adm_time')
    visType = request.form.get('visType')
    spec_day = request.form.get('spec_day')
    Region = request.form.get('Region')
    pageValue = request.form.get('pageValue')
    month = request.form.get('month')

    ProductRel_per_dur = float(pro_page)/(float(pro_time)+0.00001)
    Inform_per_dur = float(inf_page)/(float(inf_time)+0.00001)
    Admin_per_dur = float(adm_page)/(float(adm_time)+0.00001)
    Bounce_by_exit = float(ExitRates)+float(BounceRates)
    VisitorType = Encoding_Visitor(visType)
    Weekend = Encoding_weekend(Weekend)
    Month = Encoding_Month(month)


    points = ['ProductRel_per_dur','PageValues','SpecialDay','Month','Admin_per_dur','Inform_per_dur',
       'OperatingSystems','Browser','Region','TrafficType','VisitorType','Weekend','Bounce_by_exit']
    da = [[float(i)] for i in points]
    
    ## Applying standardization
    data = np.asarray(da).T

    data = (data - mean)/std
    output = model.predict(data)

    if output:
        messege = "Model predicts, The revenue will be Generated"
    else:
        messege = "Model predicts revenue will not be generated"
    return render_template('home.html',messege = messege)
  
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)

## uvicorn app:app --reload