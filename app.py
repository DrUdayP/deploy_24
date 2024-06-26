import streamlit as st 
import pickle
import pandas as pd
import sklearn
print(sklearn.__version__)

st.set_option('deprecation.showfileUploaderEncoding', False)
try:
    # Load the pickled model
    pickle_in = pickle.load(open("decision_model.pkl", "rb"))
except Exception as e:
    st.error("Error loading the pickled model: {}".format(e))

def predict_note_authentication(UserID, Gender, Age, EstimatedSalary):
    output = pickle_in.predict([[Age, EstimatedSalary]])
    st.write("Purchased:", output)
    if output == 1:
        prediction = "Item will be purchased"
    else:
        prediction = "Item will not be purchased"
    st.write(prediction)
    return prediction

def main():
    html_temp = """
    <div class="" style="background-color:blue;" >
    <div class="clearfix">           
    <div class="col-md-12">
    <center><p style="font-size:40px;color:white;margin-top:10px;">OdinSchool</p></center> 
    <center><p style="font-size:30px;color:white;margin-top:10px;">Course on streamlit</p></center> 
    <center><p style="font-size:25px;color:white;margin-top:10px;"> Project Deployment</p></center> 
    </div>
    </div>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.header("Item Purchase Prediction")
    UserID = st.text_input("UserID", "")
    Gender = st.selectbox('Gender', ('Male', 'Female'))
    Age = st.number_input("Insert Age", 18, 60)
    EstimatedSalary = st.number_input("Insert salary", 15000, 150000)
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(UserID, Gender, Age, EstimatedSalary)
        st.success('Model has predicted {}'.format(result))
    if st.button("About"):
        st.subheader("Developed by Deepak Moud")
        st.subheader("Data scientist and Developer")

if __name__ == '__main__':
    main()
