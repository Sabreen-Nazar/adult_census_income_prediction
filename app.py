#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import numpy as np


# In[ ]:


app = Flask(__name__)
model = pickle.load(open("model_lr_new.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

#1
        workclass=request.form['workclass']
        
        if( workclass=='Private'):
            Private = 1             
            Self_emp_not_inc = 0     
            Local_gov     = 0       
            workclass_mode    = 0   
            State_gov     = 0       
            Self_emp_inc  = 0       
            Federal_gov   = 0        
            Without_pay   = 0         
            Never_worked   = 0         
   

        elif( workclass=='Self_emp_not_inc'):
            Private = 0             
            Self_emp_not_inc = 1     
            Local_gov     = 0       
            workclass_mode    = 0   
            State_gov     = 0       
            Self_emp_inc  = 0       
            Federal_gov   = 0        
            Without_pay   = 0         
            Never_worked   = 0 

        elif ( workclass=='Local_gov'):
            Private = 0             
            Self_emp_not_inc = 0     
            Local_gov     = 1       
            workclass_mode    = 0   
            State_gov     = 0       
            Self_emp_inc  = 0       
            Federal_gov   = 0        
            Without_pay   = 0         
            Never_worked   = 0 
            
            
        elif( workclass=='workclass_mode'):
            Private = 0             
            Self_emp_not_inc = 0     
            Local_gov     = 0       
            workclass_mode    = 1   
            State_gov     = 0       
            Self_emp_inc  = 0       
            Federal_gov   = 0        
            Without_pay   = 0         
            Never_worked  = 0 

        elif ( workclass=='State_gov'):
            Private = 0             
            Self_emp_not_inc = 0     
            Local_gov     = 0       
            workclass_mode    = 0   
            State_gov     = 1       
            Self_emp_inc  = 0       
            Federal_gov   = 0        
            Without_pay   = 0         
            Never_worked   = 0 
            
        elif ( workclass=='Self_emp_inc'):
            Private = 0             
            Self_emp_not_inc = 0     
            Local_gov     = 0       
            workclass_mode    = 0   
            State_gov     = 0       
            Self_emp_inc  = 1      
            Federal_gov   = 0        
            Without_pay   = 0         
            Never_worked   = 0
            
        elif ( workclass=='Federal_gov'):
            Private = 0             
            Self_emp_not_inc = 0     
            Local_gov     = 0       
            workclass_mode    = 0   
            State_gov     = 0      
            Self_emp_inc  = 0       
            Federal_gov   = 1        
            Without_pay   = 0         
            Never_worked   = 0
            
        elif ( workclass=='Without_pay'):
            Private = 0             
            Self_emp_not_inc = 0     
            Local_gov     = 0       
            workclass_mode    = 0   
            State_gov     = 0       
            Self_emp_inc  = 0       
            Federal_gov   = 0        
            Without_pay   = 1         
            Never_worked   = 0
        
        else:
            Private = 0             
            Self_emp_not_inc = 0     
            Local_gov     = 0       
            workclass_mode    = 0   
            State_gov     = 0       
            Self_emp_inc  = 0       
            Federal_gov   = 0        
            Without_pay   = 0         
            Never_worked   = 1 
            
 #2       
        education=request.form['education']
         
        if( education=='Bachelors'):
             Bachelors = 1             
             HS_grad = 0     
             Higher_Grade     = 0       
             Masters    = 0   
             Some_college     = 0       
             Assoc_acdm  = 0       
             Assoc_voc   = 0        
             Doctorate   = 0         
             Prof_school   = 0         
             Lower_Grade =0
             Preschool =0
    

        elif( education=='HS_grad'):
             Bachelors = 0            
             HS_grad = 1     
             Higher_Grade     = 0       
             Masters    = 0   
             Some_college     = 0       
             Assoc_acdm  = 0       
             Assoc_voc   = 0        
             Doctorate   = 0         
             Prof_school   = 0         
             Lower_Grade =0
             Preschool =0 

        elif ( education=='Higher_Grade'):
             Bachelors = 0            
             HS_grad = 0     
             Higher_Grade     = 1       
             Masters    = 0   
             Some_college     = 0       
             Assoc_acdm  = 0       
             Assoc_voc   = 0        
             Doctorate   = 0         
             Prof_school   = 0         
             Lower_Grade =0
             Preschool =0
             
             
        elif( education=='Masters'):
             Bachelors = 0            
             HS_grad = 0     
             Higher_Grade     = 0       
             Masters    = 1   
             Some_college     = 0       
             Assoc_acdm  = 0       
             Assoc_voc   = 0        
             Doctorate   = 0         
             Prof_school   = 0         
             Lower_Grade =0
             Preschool =0

        elif ( education=='Some_college'):
             Bachelors = 0            
             HS_grad = 0     
             Higher_Grade     = 0       
             Masters    = 0   
             Some_college     = 1       
             Assoc_acdm  = 0       
             Assoc_voc   = 0        
             Doctorate   = 0         
             Prof_school   = 0         
             Lower_Grade =0
             Preschool =0 
             
        elif ( education=='Assoc_acdm'):
             Bachelors = 0            
             HS_grad = 0     
             Higher_Grade     = 0       
             Masters    = 0   
             Some_college     = 0       
             Assoc_acdm  = 1      
             Assoc_voc   = 0        
             Doctorate   = 0         
             Prof_school   = 0         
             Lower_Grade =0
             Preschool =0 
             
        elif ( education=='Assoc_voc'):
             Bachelors = 0            
             HS_grad = 0     
             Higher_Grade     = 0       
             Masters    = 0   
             Some_college     = 0       
             Assoc_acdm  = 0       
             Assoc_voc   = 1        
             Doctorate   = 0         
             Prof_school   = 0         
             Lower_Grade =0
             Preschool =0 
             
        elif ( education=='Doctorate'):
             Bachelors = 0            
             HS_grad = 0     
             Higher_Grade     = 0       
             Masters    = 0   
             Some_college     = 0      
             Assoc_acdm  = 0       
             Assoc_voc   = 0        
             Doctorate   = 1         
             Prof_school   = 0         
             Lower_Grade =0
             Preschool =0 
             
             
        elif ( education=='Prof_school'):
            Bachelors = 0            
            HS_grad = 0     
            Higher_Grade     = 0       
            Masters    = 0   
            Some_college     = 0      
            Assoc_acdm  = 0       
            Assoc_voc   = 0        
            Doctorate   = 0         
            Prof_school   = 1         
            Lower_Grade =0
            Preschool =0
            
        elif ( education=='Lower_Grade'):
            Bachelors = 0            
            HS_grad = 0     
            Higher_Grade     = 0       
            Masters    = 0   
            Some_college     = 0      
            Assoc_acdm  = 0       
            Assoc_voc   = 0        
            Doctorate   = 0        
            Prof_school   = 0         
            Lower_Grade =1
            Preschool =0
         
        else :
             Bachelors = 0            
             HS_grad = 0     
             Higher_Grade     = 0       
             Masters    = 0   
             Some_college     = 0      
             Assoc_acdm  = 0       
             Assoc_voc   = 0        
             Doctorate   = 0         
             Prof_school   = 0         
             Lower_Grade =0
             Preschool =1
         
         
#3      
        sex=request.form['sex']
        
        if( sex=='Male'):
            Male = 1             
            Female = 0     
            

        else:
            Male = 0             
            Female = 1
            
#4
        occupation=request.form['occupation']
         
        if( occupation=='Adm_clerical'):
             Adm_clerical = 1             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 0         
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=0
             
        elif( occupation=='Exec_managerial'):
             Adm_clerical = 0             
             Exec_managerial = 1     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 0         
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=0
             
             
        elif( occupation=='Handlers_cleaners'):
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 1       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 0         
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=0
             
        elif( occupation=='Prof_speciality'):
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 1   
             Other_service     = 0       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 0         
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=0
             
             
        elif( occupation=='Other_service'):
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 1       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 0         
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=0
             
             
        elif( occupation=='Sales'):
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 1       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 0         
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=0
             
             
             
        elif( occupation=='Craft_repair'):
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 0      
             Craft_repair   = 1        
             Transport_moving  = 0         
             Farming_fishing   = 0         
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=0
             
             
        elif( occupation=='Transport_moving'):
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 1         
             Farming_fishing   = 0         
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=0
             
             
        elif( occupation=='Farming_fishing'):
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 1         
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=0
             
             
        elif( occupation=='Machine_op_inspct'):
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 0        
             Machine_op_inspct =1
             Tech_support =0
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=0
             
        elif( occupation=='Tech_support'):
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 0         
             Machine_op_inspct =0
             Tech_support =1
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=0
             
             
        elif( occupation=='Protective_serv'):
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 0         
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=1
             Armed_Forces=0
             Priv_house_serv=0
             
        elif( occupation=='Armed_Forces'):
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 0        
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=0
             Armed_Forces=1
             Priv_house_serv=0
             
        else:
             Adm_clerical = 0             
             Exec_managerial = 0     
             Handlers_cleaners     = 0       
             Prof_specialty    = 0   
             Other_service     = 0       
             Sales  = 0       
             Craft_repair   = 0        
             Transport_moving  = 0         
             Farming_fishing   = 0         
             Machine_op_inspct =0
             Tech_support =0
             Protective_serv=0
             Armed_Forces=0
             Priv_house_serv=1
             
             


        age=request.form['age']
        fnlwgt=request.form['fnlwgt']
        education_num=request.form['education_num']
        capital_gain=request.form['capital_gain']
        capital_loss=request.form['capital_loss']
        hours_per_week=request.form['hours_per_week']
        

        
        arr=np.array([[Private,Self_emp_not_inc,Local_gov,workclass_mode,
                       State_gov,Self_emp_inc,Federal_gov,Without_pay,
                       Never_worked,Bachelors ,HS_grad, Higher_Grade,
                       Masters ,Some_college,Assoc_acdm ,Assoc_voc,
                       Doctorate ,Prof_school, Lower_Grade,Preschool,
                       Male,Female,Adm_clerical, Exec_managerial, Handlers_cleaners,Prof_specialty,
                       Other_service,Sales,Craft_repair,Transport_moving,
                       Farming_fishing,Machine_op_inspct,Tech_support,Protective_serv,
                       Armed_Forces,Priv_house_serv,age,fnlwgt,education_num,
                       capital_gain,capital_loss,hours_per_week
                                    ]])

        pred = model.predict(arr)
        if int(pred)==1:
            prediction='Income is more than 50K'
        else:
            prediction='Income is less that 50K'
            
        return render_template("home.html",prediction_text=prediction)

    #return render_template('home.html',prediction_text=output)


    #return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)#,use_reloader=False


# In[ ]:




