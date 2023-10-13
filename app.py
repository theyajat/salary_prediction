import pandas as pd
from sklearn import linear_model
import streamlit as st
from matplotlib import pyplot as plt
from plotly import graph_objs as go
import plotly.express as px
import numpy as np
import warnings
warnings.filterwarnings("ignore")

reg=linear_model.LinearRegression()             
df=pd.read_csv('dataset.csv')
correct_password="joker"
#print(df)
X=df[['YearsExperience']]
y=df[['Salary']]
reg.fit(X,y)
#predited_val=reg.predict([[15]])
#print(predited_val)
accuracy=reg.score(X,y)

st.title("Salary Predictor :) ")
nav=st.sidebar.radio("Navigation",["Home","Prediction","Data"])
if nav=="Home":
    st.image("image.png",width=128)
    graph=st.selectbox("What kind of graph you want",["Non-Interactive","Linear Model","Interactive"])

    if graph=="Non-Interactive":
        plt.scatter(X,y)
        plt.xlabel("Years of experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot(plt)
    if graph=="Linear Model":
        plt.plot(X,reg.predict(df[['YearsExperience']]),color='blue')
        plt.scatter(X,y,color='red')
        plt.tight_layout()
        st.pyplot(plt)
    if graph=="Interactive":
        fig = px.scatter(df, x="YearsExperience", y="Salary")
        st.plotly_chart(fig)




if nav==("Prediction"):
    st.header("Know Your Salary...")
    val=st.number_input("Enter your Experience: ",0.00,28.00,step=0.25)
    val=np.array(val).reshape(1,-1)
    pred=reg.predict(val)[0]
    integer_array = pred[0]

    if st.button("Predict"):
        st.success(f"The predicted salary is {(round(integer_array))} $")
        st.success(f"The accuracy of Prediction is {int(accuracy*100)}%")



if nav=="Data":
    def authenticate(password):
        return password == correct_password

    def main():
        st.subheader("You need to Authenticate yourself for the Data...")
        password_input=st.text_input("Enter the password",type="password")

        if st.button("Authenticate"):
            if authenticate(password_input):
                st.success("Authentication Granted, Welcome to the Den")
                st.table(df)
                data=df
                csv_file=data.to_csv(index=False)
                st.download_button(label="Download CSV",data=csv_file,file_name="salary_dataset",mime="test/csv",)


            else:
                st.error("Authentication Denied !!!")
    if __name__ == "__main__":
        main()