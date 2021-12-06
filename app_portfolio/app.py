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
    st.text('Stock Market Predictions using LSTM and Decision Tree Algorithm\n-Email-Spam-Classification using Support Vector Machine \n-Exploring_Neighborhoods_in_the_city_of_Toronto\n-Car-Prediction using RandomForestRegressor\n-Exploratory Data Analysis of police dataset')
    st.write('-------------------------------------------------------')
    st.subheader('2. Tool geometry & Vibration analysis of single point cutting tool on Traditional Lathe machine (06/2019 - 04/2020)')
    st.write('-------------------------------------------------------') 

######################## Internships ##################################
if st.sidebar.button('iNTERNSHIPS'):
    st.header("INTERNSHIPS")
    st.write('-------------------------------------------------------')
    st.markdown('## **Data Science**')
    st.subheader('Innomatics Research Labs (10/2021 - Present,)')
    st.text('-EDA of Fifa 19 Players data (K means Clustring, Principle Component Analysis )  \n-Descriptive Stats - Both basic and Adv Users\n-Application Development project (URL Shortner)')
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
    st.subheader('Data Science (06/2020 - 02/2021')
    st.write('*IBM Data Science Professional Certificate-Coursera*')
    st.write('-------------------------------------------------------')
    
    st.subheader('Machine Learning (06/2020 - 09/2020)')
    st.write('*Stanford University-Coursera*')
    st.write('-------------------------------------------------------')
    
    st.subheader('AutoCAD (01/2016 - 02/2016)')
    st.write('*2D-Drafting and 3D-Modeling and Drafting*')
    st.write('-------------------------------------------------------')
    
    st.subheader('SolidWorks (06/2019 - 07/2019)')
    st.write('*GD & T ,Modeling and Drafting*')
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
