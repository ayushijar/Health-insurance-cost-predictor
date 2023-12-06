import pandas as pd
import pickle


class Predictions():

    def __init__(self,age,sex,bmi,child,smoke,reg):

        self.age= age
        self.sex = sex
        self.bmi = bmi
        self.child = child
        self.smoke = smoke
        self.reg = reg

    def predict(self):

        pkl_in = open("insurance_predict.pkl",'rb')
        reg = pickle.load(pkl_in)
        prediction = reg.predict(pd.DataFrame(data={'age':[self.age],'sex':[self.sex],'bmi':[self.bmi],'children':[self.child],'smoker':[self.smoke],'region':[self.reg]})) 
        
        return(str(prediction[0].round(2)))
