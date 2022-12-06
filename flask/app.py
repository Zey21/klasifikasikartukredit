from flask import Flask,render_template,request, redirect, url_for
import numpy as np
import pickle
import os
app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def web():
    return render_template('index.html')

@app.route('/home',methods = ['POST','GET'])
def web1():
    return render_template('index.html')

@app.route('/fitur',methods = ['POST','GET'])
def fitur():
    if request.method == 'POST':
        Card_Category = request.form['Card_Category']
        # temp = Card_Category
        Gender = request.form['Gender']
        if(Gender == 'M') :
            Gender_1 = 1
            Gender_2 = 0
        else :
            Gender_1 = 0
            Gender_2 = 1
        Education_Level = request.form['Education_Level']
        if(Education_Level == 'College') :
            Education_Level_1 = 1
            Education_Level_2 = 0
            Education_Level_3 = 0
            Education_Level_4 = 0
            Education_Level_5 = 0
            Education_Level_6 = 0
            Education_Level_7 = 0
        elif(Education_Level == 'Doctorate') :
            Education_Level_1 = 0
            Education_Level_2 = 1
            Education_Level_3 = 0
            Education_Level_4 = 0
            Education_Level_5 = 0
            Education_Level_6 = 0
            Education_Level_7 = 0
        elif(Education_Level == 'Graduate') :
            Education_Level_1 = 0
            Education_Level_2 = 0
            Education_Level_3 = 1
            Education_Level_4 = 0
            Education_Level_5 = 0
            Education_Level_6 = 0
            Education_Level_7 = 0
        elif(Education_Level == 'Highschool') :
            Education_Level_1 = 0
            Education_Level_2 = 0
            Education_Level_3 = 0
            Education_Level_4 = 1
            Education_Level_5 = 0
            Education_Level_6 = 0
            Education_Level_7 = 0
        elif(Education_Level == 'PostGraduate') :
            Education_Level_1 = 0
            Education_Level_2 = 0
            Education_Level_3 = 0
            Education_Level_4 = 0
            Education_Level_5 = 1
            Education_Level_6 = 0
            Education_Level_7 = 0
        elif(Education_Level == 'Uneducated') :
            Education_Level_1 = 0
            Education_Level_2 = 0
            Education_Level_3 = 0
            Education_Level_4 = 0
            Education_Level_5 = 0
            Education_Level_6 = 1
            Education_Level_7 = 0
        else :
            Education_Level_1 = 0
            Education_Level_2 = 0
            Education_Level_3 = 0
            Education_Level_4 = 0
            Education_Level_5 = 0
            Education_Level_6 = 0
            Education_Level_7 = 1
        Marital_Status = request.form['Marital_Status']
        if(Marital_Status == 'Divorced') :
            Marital_Status_1 = 1
            Marital_Status_2 = 0
            Marital_Status_3 = 0
            Marital_Status_4 = 0
        elif(Marital_Status == 'Married') :
            Marital_Status_1 = 0
            Marital_Status_2 = 1
            Marital_Status_3 = 0
            Marital_Status_4 = 0
        elif(Marital_Status == 'Single') :
            Marital_Status_1 = 0
            Marital_Status_2 = 0
            Marital_Status_3 = 1
            Marital_Status_4 = 0
        else :
            Marital_Status_1 = 0
            Marital_Status_2 = 0
            Marital_Status_3 = 0
            Marital_Status_4 = 1
        Income_Category = request.form['Income_Category']
        if(Income_Category == '1stTier') :
            Income_Category_1 = 1
            Income_Category_2 = 0
            Income_Category_3 = 0
            Income_Category_4 = 0
            Income_Category_5 = 0
            Income_Category_6 = 0
        elif(Income_Category == '2ndTier'):
            Income_Category_1 = 0
            Income_Category_2 = 1
            Income_Category_3 = 0
            Income_Category_4 = 0
            Income_Category_5 = 0
            Income_Category_6 = 0
        elif(Income_Category == '3rdTier'):
            Income_Category_1 = 0
            Income_Category_2 = 0
            Income_Category_3 = 1
            Income_Category_4 = 0
            Income_Category_5 = 0
            Income_Category_6 = 0
        elif(Income_Category == '4thTier'):
            Income_Category_1 = 0
            Income_Category_2 = 0
            Income_Category_3 = 0
            Income_Category_4 = 1
            Income_Category_5 = 0
            Income_Category_6 = 0
        elif(Income_Category == '5thTier'):
            Income_Category_1 = 0
            Income_Category_2 = 0
            Income_Category_3 = 0
            Income_Category_4 = 0
            Income_Category_5 = 1
            Income_Category_6 = 0
        else:
            Income_Category_1 = 0
            Income_Category_2 = 0
            Income_Category_3 = 0
            Income_Category_4 = 0
            Income_Category_5 = 0
            Income_Category_6 = 1
        Customer_Age = int(request.form['Customer_Age'])
        Dependent_Count = int(request.form['Dependent_Count'])
        Month_on_book = int(request.form['Month_on_book'])
        Credit_Limit = int(request.form['Credit_Limit'])
        Total_Revolving_Bal = int(request.form['Total_Revolving_Bal'])
        Avg_Open_to_Buy = int(request.form['Avg_Open_To_Buy'])
        Total_Amt_Chng_Q4_Q1 = int(request.form['Total_Amt_Chng_Q4_Q1'])
        Total_Trans_Amt = int(request.form['TT_Amt'])
        Total_Trans_Ct = int(request.form['TT_Ct'])
        Total_Ct_Chng_Q4_Q1 = int(request.form['Total_Ct_Chng_Q4_Q1'])
        Avg_Utilization_Ratio = int(request.form['Avg_Utilization_Ratio'])
        X_test = np.array([[Gender_1, Gender_2, Education_Level_1, Education_Level_2, Education_Level_3, Education_Level_4, Education_Level_5, Education_Level_6, Education_Level_7, Marital_Status_1,Marital_Status_2,Marital_Status_3,Marital_Status_4, Income_Category_1,Income_Category_2,Income_Category_3,Income_Category_4,Income_Category_5,Income_Category_6, Customer_Age, Dependent_Count, Month_on_book, Credit_Limit, Total_Revolving_Bal, Avg_Open_to_Buy, Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio]])
        y_test = np.array([[Card_Category]])
        
        # Naive Bayes Model from pickle
        Bayes_Model = os.path.join('bayes.pickle')
        Temp_Bayes = pickle.load(open(Bayes_Model, 'rb'))
        Predict_Bayes = (Temp_Bayes.score(X_test,y_test)*100)
        Kt_Bayes = Temp_Bayes.predict(X_test)
        
        # # KNN Model from pickle
        KNN_Model = os.path.join('knn.pickle')
        Temp_KNN = pickle.load(open(KNN_Model, 'rb'))
        Predict_KNN = (Temp_KNN.score(X_test, y_test)*100)
        Kt_KNN = Temp_KNN.predict(X_test)
        
        #Decision Tree Model from pickle
        DTC_Model = os.path.join('dtc.pickle')
        Temp_DTC = pickle.load(open(DTC_Model, 'rb'))
        Predict_DTC = (Temp_DTC.score(X_test, y_test)*100)
        Kt_DTC = Temp_DTC.predict(X_test)
        
        prediksi = "Naive Bayes :{}{} || KNN :{}{} || Decision Tree :{}{}".format(Predict_Bayes,Kt_Bayes,Predict_KNN,Kt_KNN,Predict_DTC,Kt_DTC)
                
        return redirect(url_for('page', hasil = prediksi))
    else :
        return render_template('sub.html')

@app.route('/<hasil>', methods = ["GET", "POST"])
def page(hasil): 
    return f"<center><h1 style='padding-top: 325px;'>Prediksi Category : {hasil}</h1></center>"
    
if __name__ == '__main__' :
    app.run(debug=True)  

