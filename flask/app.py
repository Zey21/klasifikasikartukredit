from flask import Flask,render_template,request
import numpy as np
import pickle
import os
app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def web():
    if request.method == 'POST':
        kata = "Hello World"
        angka = 123123
        return render_template('result.html',Say = kata, Numb = angka)
    return render_template('index.html')

@app.route('/home',methods = ['POST','GET'])
def web1():
    if request.method == 'POST':
        kata = "Hello World"
        angka = 123123
        return render_template('result.html',Say = kata, Numb = angka)
    return render_template('index.html')

@app.route('/result',methods = ['POST','GET'])
def web3():
    return render_template('result.html')
@app.route('/fitur',methods = ['POST','GET'])
def web2():
    if request.method == 'POST':
        Card_Category = request.form['Card_Category']
        Gender = request.form['Gender']
        if(Gender == 'M') :
            Gender = [1,0]
        else :
            Gender = [0,1]
        Education_Level = request.form['Education_Level']
        if(Education_Level == 'College') :
            Education_Level = [1,0,0,0,0,0,0]
        elif(Education_Level == 'Doctorate') :
            Education_Level = [0,1,0,0,0,0,0]
        elif(Education_Level == 'Graduate') :
            Education_Level = [0,0,1,0,0,0,0]
        elif(Education_Level == 'Highschool') :
            Education_Level = [0,0,0,1,0,0,0]
        elif(Education_Level == 'PostGraduate') :
            Education_Level = [0,0,0,0,1,0,0]
        elif(Education_Level == 'Uneducated') :
            Education_Level = [0,0,0,0,0,1,0]
        else :
            Education_Level = [0,0,0,0,0,0,1]
        Marital_Status = request.form['Martial_Status']
        if(Marital_Status == 'Divorced') :
            Marital_Status = [1,0,0,0]
        elif(Marital_Status == 'Married') :
            Marital_Status = [0,1,0,0]
        elif(Marital_Status == 'Single') :
            Marital_Status = [0,0,1,0]
        else :
            Marital_Status = [0,0,0,1] 
        Income_Category = request.form['Income_Category']
        if(Income_Category == '1stTier') :
            Income_Category = [1,0,0,0,0,0]
        elif(Income_Category == '2ndTier'):
            Income_Category = [0,1,0,0,0,0]
        elif(Income_Category == '3rdTier'):
            Income_Category = [0,0,1,0,0,0]
        elif(Income_Category == '4thTier'):
            Income_Category = [0,0,0,1,0,0]
        elif(Income_Category == '5thTier'):
            Income_Category = [0,0,0,0,1,0]
        else:
            Income_Category = [0,0,0,0,0,1]
        Customer_Age = int(request.form['Customer_Age'])
        Dependent_Count = int(request.form['Dependent_Count'])
        Month_on_book = int(request.form['Month_on_book'])
        Credit_Limit = int(request.form['Credit_Limit'])
        Total_Revolving_Bal = int(request.form['Total_Revolving_Bal'])
        Avg_Open_to_Buy = int(request.form['Avg_Open_to_Buy'])
        Total_Amt_Chng_Q4_Q1 = int(request.form['Total_Amt_Chng_Q4_Q1'])
        Total_Trans_Amt = int(request.form['Total_Trans_Amt'])
        Total_Trans_Ct = int(request.form['Total_Trans_Ct'])
        Total_Ct_Chng_Q4_Q1 = int(request.form['Total_Ct_Chng_Q4_Q1'])
        Avg_Utilization_Ratio = int(request.form['Avg_Utilization_Ratio'])
        xtest = np.array[[Gender[0], Education_Level[0], Marital_Status[0], Income_Category[0], Customer_Age, Dependent_Count, Month_on_book, Credit_Limit, Total_Revolving_Bal, Avg_Open_to_Buy, Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio]]
        ytest = np.array[[Card_Category]]
        # Naive Bayes Model from pickle
        Bayes_Model = os.path.join('bayes.pickle')
        Temp_Bayes = pickle.load(open(Bayes_Model, 'rb'))
        Predict_Bayes = Temp_Bayes.score(xtest,ytest)*100
        
        # KNN Model from pickle
        KNN_Model = os.path.join('knn.pickle')
        Temp_KNN = pickle.load(open(KNN_Model, 'rb'))
        Predict_KNN = Temp_KNN.score(xtest,ytest)*100
        
        #Decision Tree Model from pickle
        DTC_Model = os.path.join('dtc.pickle')
        Temp_DTC = pickle.load(open(DTC_Model, 'rb'))
        Predict_DTC = Temp_DTC.score(xtest,ytest)*100
        
        return render_template('result.html', Result = Predict_Bayes, Result2 = Predict_KNN, Result3 = Predict_DTC)
        
    return render_template('sub.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
