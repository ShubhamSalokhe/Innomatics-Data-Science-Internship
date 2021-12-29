import streamlit as st
from PIL import Image

####################### metadata###############################
# profile_image = Image.open('ID1.jpg')
# st.image(profile_image,width = 200)

st.title("SHUBHAM SALOKHE")
st.subheader("ML | DL | Data Science")  
st.write("P O R T F O L I O")


st.info("I seek the kinds of challenges where I fit naturally, what I enjoy. I look for operations-intensive companies that can benefit from significant performance improvement using my data insights. I take floundering raw-number and go build impactful results with a tincture of my Statistical skills that can grow your company.")

st.sidebar.warning('CONTENT')
######################contact details ##############################

if st.sidebar.button('Contact Me'):
    st.success("CONTACT")
    st.write('-------------------------------------------------------')
    st.write(":email: shubhamsalokhe@ymail.com")
    st.write('-------------------------------------------------------')
    st.write('[GitHub](https://github.com/ShubhamSalokhe/),',' [Linkedin](https://www.linkedin.com/in/shubhamsalokhe/)')
    st.write('-------------------------------------------------------')
    st.write(':iphone: +91 855297 4448')
    st.write('-------------------------------------------------------')


#########################   Education ##########################

if st.sidebar.button('EDUCATION'):
    st.success("EDUCATION")

    st.write('-------------------------------------------------------')
    st.subheader('Shivaji University')
    st.text('Bachelor in Mechanical Engineering')
    st.write('-------------------------------------------------------')
    st.subheader('Dr. D. Y. Patil Jr. College, Kolhapur')
    st.text('Higher Secondary Certificate (HSC)')
    st.write('-------------------------------------------------------')
    

#########################   Projects ##########################

if st.sidebar.button('Projects'):
    st.success("PROJECTS")
    st.write('-------------------------------------------------------')
    st.subheader('1. Data Science & Machine Learning (06/2020 - Present)')
    st.markdown('- [Stock Market Predictions using LSTM and Decision Tree Algorithm](https://github.com/ShubhamSalokhe/Stock-Price-Prediction/blob/master/Stock_Market_Prediction_Project%20final%20version.ipynb)',unsafe_allow_html=True)
    st.markdown('- [Email-Spam-Classification using Support Vector Machine](https://github.com/ShubhamSalokhe/Email-Spam-Classification/blob/main/Email%20spam%20classifier%20.ipynb)',unsafe_allow_html=True) 
    st.markdown('- [Exploring_Neighborhoods_in_the_city_of_Toronto](https://github.com/ShubhamSalokhe/Exploring_Neighborhoods_in_the_city_of_Toronto)',unsafe_allow_html=True)
    st.markdown('- [Car-Prediction using RandomForestRegressor](https://github.com/ShubhamSalokhe/Car-Prediction/blob/main/Car%20Prediction.ipynb)',unsafe_allow_html=True)
    st.markdown('- [Exploratory Data Analysis of police dataset](https://github.com/ShubhamSalokhe/Data_Analysis_Projects/blob/main/Police_Data_Analysis/Police_Data_File.ipynb)',unsafe_allow_html=True)
    st.write('-------------------------------------------------------')
    st.subheader('2. Tool geometry & Vibration analysis of single point cutting tool on Traditional Lathe machine (06/2019 - 04/2020)')
    st.write('-------------------------------------------------------') 

######################## Internships ##################################
if st.sidebar.button('iNTERNSHIPS'):
    st.header("INTERNSHIPS")
    st.write('-------------------------------------------------------')
    st.markdown('## **Data Science**')
    st.subheader('Innomatics Research Labs (10/2021 - Present,)')
    st.markdown('- [Sentiment analysis of airline tweets app (Streamlit app) deployment on Heroku cloud platform](https://github.com/ShubhamSalokhe/Innomatics-Data-Science-Internship/tree/master/Heroku%20deployment)',unsafe_allow_html=True)
    st.markdown('- [Sentiment analysis of airline tweets (heroku link)](https://airline-nltk-app.herokuapp.com/)',unsafe_allow_html=True)
    st.markdown('- [Flask Application Development project (URL Shortner)](https://github.com/ShubhamSalokhe/Innomatics-Data-Science-Internship/tree/master/Flask%20Project)',unsafe_allow_html=True)
    st.markdown('- [Implementing K-Nearest Neighbor(KNN) Algorithm from scratch Dataset-"Diamond"](https://github.com/ShubhamSalokhe/Innomatics-Data-Science-Internship/blob/master/KNN_from_scratch/knn_from_scratch.ipynb)',unsafe_allow_html=True)
    st.markdown('- [Descriptive Stats - Both basic and Adv Users](https://github.com/ShubhamSalokhe/Innomatics-Data-Science-Internship/blob/master/Descriptive%20Stats%20-%20Both%20basic%20and%20Adv%20Users/(Descriptive%20Stats%20-%20Both%20basic%20and%20Adv%20Users).ipynb)',unsafe_allow_html=True)
    st.markdown('- [EDA of Fifa 19 Players data (K means Clustring, Principle Component Analysis)](https://github.com/ShubhamSalokhe/Innomatics-Data-Science-Internship/blob/master/Hackathon/Hackerthon.ipynb)',unsafe_allow_html=True)
    st.write('-------------------------------------------------------')
    
    st.markdown('## **Data Science - ML & DL **')
    st.subheader('Innomatics Research Labs (07/2021 - 10/2021)')
    st.text('-EDA of Rainfall Analysis\n-Created Simple Linear Model for Salary dataset\n-Prediction House Price using advance regression techniques')
    st.write('-------------------------------------------------------')

    st.markdown('## **Data Science and Business Analytics**')
    st.subheader('The Spark Foundation (04/2021 - 05/2021)')
    st.text('-Prediction Using Supervised Learning.\n-Unsupervised Learning.\n-Exploratory Data Analysis(EDA).')
    st.write('-------------------------------------------------------')


##################################skills#########################################
if st.sidebar.button('SKILLS'):
    st.success("SKILLS")
    st.markdown("* Data Analysis")
    st.markdown("* Data Science")
    st.markdown("* Machine Learning")
    st.markdown("* Microsoft Office Excel")
    st.markdown("* Python")
    st.markdown("* MATLAB")
    st.markdown("* SQL")
    st.markdown("* Microsoft Office PowerPoint")
    st.markdown("* Microsoft Office Word")
    st.markdown("* AutoCAD")
    st.markdown("* SOLIDWORKS")
    st.markdown("* CATIA")
    st.markdown("* Adobe Photoshop")


################################## CERTIFICATES #########################################

if st.sidebar.button('CERTIFICATES'):
    st.success("CERTIFICATES")

    st.write('-------------------------------------------------------')
    st.subheader('Data Science (06/2020 - 02/2021)')
    st.write('[*IBM Data Science Professional Certificate-Coursera*](https://www.credly.com/badges/45e29fed-66f1-4d7f-9f64-515bc618add4?source=linked_in_profile)', unsafe_allow_html=True)
    st.write('-------------------------------------------------------')
    
    st.subheader('Machine Learning (06/2020 - 09/2020)')
    st.write('[*Stanford University-Coursera*](https://coursera.org/share/3e1888c14a2b63918f350558b4a6e3f9)', unsafe_allow_html=True)
    st.write('-------------------------------------------------------')
    
    st.subheader('AutoCAD (01/2016 - 02/2016)')
    st.write('*2D-Drafting and 3D-Modeling and Drafting*')
    st.write('-------------------------------------------------------')
    
    st.subheader('SolidWorks (06/2019 - 07/2019)')
    st.write('[*SolidWorks, GD & T ,Modeling and Drafting *](https://www.caddcentre.com/caddVerification.php?ddac=ODA3Njg5)', unsafe_allow_html=True)
    st.write('-------------------------------------------------------')

################################## LANGUAGES #########################################


if st.sidebar.button('LANGUAGES'):
    st.success("LANGUAGES")

    st.write('-------------------------------------------------------')
    st.subheader('English')
    st.write('*Professional Working Proficiency*')
    st.write('-------------------------------------------------------')

    st.subheader('Marathi')
    st.write('*Full Professional Proficiency*')
    st.write('-------------------------------------------------------')

    st.subheader('Hindi')
    st.write('*Full Professional Proficiency*')
    st.write('-------------------------------------------------------')

################################## INTERESTS #########################################

if st.sidebar.button('INTERESTS'):
    st.success("INTEREST")
    st.write('-------------------------------------------------------')

    st.markdown("* Sketching")
    st.markdown("* Artificial Intelligence")
    st.markdown("* Gaming")
    st.markdown("* Sport")
    st.markdown("* Travel")
    st.markdown("* Music")
    st.write('-------------------------------------------------------')
