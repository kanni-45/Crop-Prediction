import joblib
import streamlit as st
import os






st.set_page_config(layout="wide")

st.sidebar.title("CSP Project")

Mode=st.sidebar.selectbox('Choose mode',
['About Project','Crop Predictor','Dataset','Range of Crops']
)


if Mode=='Crop Predictor':
    #st.header("Crop Prediction using Machine Learning ")
    st.markdown("<h1 style='text-align: center; color: skyblue; '>Crop Prediction using Machine Learning </h1>", unsafe_allow_html=True)
    st.image(os.path.join('./images','crop2.jpg'),use_column_width=True )
    #st.image(os.path.join('./images','translator2.jpg'),use_column_width=True )

    box1=st.number_input('Enter Nitrogen Value',step=1,value=1)
    box2=st.number_input('Enter Phosphorous Value',step=1,value=1)
    box3=st.number_input('Enter Potassium Value',step=1,value=1)
    box4=st.number_input('Enter Temperature Value',step=1,value=1)
    box5=st.number_input('Enter Humidity Value',step=1,value=1)
    box6=st.number_input('Enter Ph Value',step=1,value=1)
    box7=st.number_input('Enter Rainfall Value',step=1,value=1)

    def data(X,Y,Z,A,B,C,D):



        testing=[[X,Y,Z,A,B,C,D]]

        model=joblib.load('web_page')
        prediction=model.predict(testing)
        #st.success(prediction)


        var=int(prediction)

        if var==0:
            st.success("APPLE is good for this land ")
        elif var==1:
            st.success("BANANA is good for this land ")
        elif var==2:
            st.success("BLACKGRAM is good for this land ")
        elif var==3:
            st.success("CHICKPAE is good for this land ")
        elif var==4:
            st.success("COCONUT is good for this land")
        elif var==5:
            st.success("COFFEE is good for this land")
        elif var==6:
            st.successt("COTTON is good for this land")
        elif var==7:
            st.success("GRAPES is good for this land")
        elif var==8:
            st.success("JUTE is good for this land")
        elif var==9:
            st.success("KIDNEYBEANS is good for this land")
        elif var==10:
            st.success("LENTIL is good for this land")
        elif var==11:
            st.success("MAIZE is good for this land")
        elif var==12:
            st.success("MANGO is good for this land")
        elif var==13:
            st.success("MOTHBEANS is good for this land")
        elif var==14:
            st.success("MUNGBEAN is good for this land ")
        elif var==15:
            st.success("MUSKMELON is good for this land")
        elif var==16:
            st.success("ORANGE is good for this land ")
        elif var==17:
            st.success("PAPAYA is good for this land ")
        elif var==18:
            st.success("PEGIONPEAS is good for this land")
        elif var==19:
            st.success("POMEGRANATE is good for this land")
        elif var==20:
            st.success("RICE is good for this land")
        elif var==21:
            st.success("WATERMELON is good for this land")
        else:
            st.success("code run no match")


    if box1 or box2 or box3 and box4 and box5 and box6 and box7:
        if st.button("click me"):
            data(box1,box2,box3,box4,box5,box6,box7)


#st.write(Crop)

import pandas as pd
dataset=pd.read_csv("Crop_recommendation in csv.csv",header=0)



if Mode=='Dataset':
    dataset.values


if Mode=='Range of Crops':

    Crop=st.selectbox("select crop",['rice','maize','chickpea','kidneybeans','pigeonpeas','mothbeans','mungbean','blackgram','lentil','pomegranate',
'banana','mango','grapes','watermelon','apple','orange','papaya','coconut','cotton','jute','coffee','muskmelon'])


    parameter=st.selectbox("select parameters",['nitrogen','phosphorous','potassium','temperature','humidity','ph','rainfall','all'])








    stores=[]#stores all nitrogen values
    stores1=[]#stores all phosphorous values
    stores2=[]#stores all potassium values
    stores3=[]#stores all temperature values
    stores4=[]#stores all humidity values
    stores5=[]#stores all ph values
    stores6=[]#stores all rainfall values
            

    #TO SELECT ALL ROWS WITH PARTICULAR CROP NAME
    for i in range(len(dataset["Crop"])) :#0,1,.....2200
        if dataset["Crop"][i]==Crop:
            #store is a variable which stores all rows 
            store=dataset[i:i+1]
            nitrogen=str(int(store['N'])).split()
            phosphorous=str(int(store['P'])).split()
            potassium=str(int(store['K'])).split()
            temperature=str(float(store['temperature'])).split()
            humidity=str(float(store['humidity'])).split()
            ph=str(float(store['ph'])).split()
            rainfall=str(float(store['rainfall'])).split()
            stores+=nitrogen
            stores1+=phosphorous
            stores2+=potassium
            stores3+=temperature
            stores4+=humidity
            stores5+=ph
            stores6+=rainfall
            



    def Nitrogen():      
        #TO CONVERT VALUES IN INTEGER FOR NITROGEN
        for k in range(len(stores)):
            stores[k]=int(stores[k])
            
        #SORTING TO GET RANGE  FOR NITROGEN  
        for j in range(len(stores)-2):
            for i in range(len(stores)-1-j):
                if (stores[i]>stores[i+1]):
                    t=stores[i]
                    stores[i]=stores[i+1]
                    stores[i+1]=t
        st.success("range of nitrogen value of {} is :{}-{}".format(Crop, stores[0],stores[-1]))


    def Phosphorous(): 
        #TO CONVERT VALUES IN INTEGER FOR PHOSPHOROUS
        for k in range(len(stores1)):
            stores1[k]=int(stores1[k])
            
        #SORTING TO GET RANGE  FOR PHOSPHOROUS  
        for j in range(len(stores1)-2):
            for i in range(len(stores1)-1-j):
                if (stores1[i]>stores1[i+1]):
                    t=stores1[i]
                    stores1[i]=stores1[i+1]
                    stores1[i+1]=t
        st.success("range of phosphorous value of {} is :{}-{}".format(Crop, stores1[0],stores1[-1]))
        
        

    def Potassium():    
        #TO CONVERT VALUES IN INTEGER FOR POTASSIUM
        for k in range(len(stores2)):
            stores2[k]=int(stores2[k])
            
        #SORTING TO GET RANGE  FOR POTASSIUM 
        for j in range(len(stores2)-2):
            for i in range(len(stores2)-1-j):
                if (stores2[i]>stores2[i+1]):
                    t=stores2[i]
                    stores2[i]=stores2[i+1]
                    stores2[i+1]=t
        st.success("range of potassium value of {} is :{}-{}".format(Crop, stores2[0],stores2[-1]))
        
        


        
    def Temperature():
        #TO CONVERT VALUES IN FLOAT FOR TEMPERATURE
        for k in range(len(stores3)):
            stores3[k]=float(stores3[k])
            
        #SORTING TO GET RANGE  FOR TEMPERATURE 
        for j in range(len(stores3)-2):
            for i in range(len(stores3)-1-j):
                if (stores3[i]>stores3[i+1]):
                    t=stores3[i]
                    stores3[i]=stores3[i+1]
                    stores3[i+1]=t
        st.success("range of temperature value of {} is :{}-{}".format(Crop,stores3[0],stores3[-1]))
        
        
        
    def Humidity():
        #TO CONVERT VALUES IN FLOAT FOR HUMIDITY
        for k in range(len(stores4)):
            stores4[k]=float(stores4[k])
        
        #SORTING TO GET RANGE  FOR PH   
        for j in range(len(stores4)-2):
            for i in range(len(stores4)-1-j):
                if (stores4[i]>stores4[i+1]):
                    t=stores4[i]
                    stores4[i]=stores4[i+1]
                    stores4[i+1]=t
        st.success("range of humidity value of {} is :{}-{}".format(Crop, stores4[0],stores4[-1]))

    def Ph():
        #TO CONVERT VALUES IN FLOAT FOR PH
        for k in range(len(stores5)):
            stores5[k]=float(stores5[k])
        #SORTING TO GET RANGE  FOR PH  
        for j in range(len(stores5)-2):
            for i in range(len(stores5)-1-j):
                if (stores5[i]>stores5[i+1]):
                    t=stores5[i]
                    stores5[i]=stores5[i+1]
                    stores5[i+1]=t
        st.success("range of ph value of {} is:{}-{}".format(Crop,stores5[0],stores5[-1]))

            

    def Rainfall():
        #TO CONVERT VALUES IN FLOAT FOR RAINFALL
        for k in range(len(stores6)):
            stores6[k]=float(stores6[k])

        #SORTING TO GET RANGE  FOR RAINFALL  
        for j in range(len(stores6)-2):
            for i in range(len(stores6)-1-j):
                if (stores6[i]>stores6[i+1]):
                    t=stores6[i]
                    stores6[i]=stores6[i+1]
                    stores6[i+1]=t
        st.success("range of rainfall value of {} is :{}-{}".format(Crop, stores6[0],stores6[-1]))


    ranges=st.button("click me",key=2)

    if ranges:
        if parameter=='nitrogen':
            Nitrogen()
        elif parameter=='phosphorous':
            Phosphorous()
        elif parameter=='potassium':
            Potassium()
        elif parameter=='temperature':
            Temperature()
        elif parameter=='humidity':
            Humidity()
        elif parameter=='ph':
            Ph()
        elif parameter=='rainfall':
            Rainfall()
        elif parameter=='all':
            Nitrogen()
            Phosphorous()
            Potassium()
            Temperature()
            Humidity()
            Ph()
            Rainfall()