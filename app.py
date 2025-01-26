import pandas as pd
import streamlit as st



st.sidebar.title("Upload Dataset")
Upload_File = st.sidebar.file_uploader("Choose csv file", type='csv')
if Upload_File is not None:
    df = pd.read_csv(Upload_File)

    #SideBar Code
    no_of_event = len(df)
    citizenship_count = df['citizenship'].value_counts
    event_location_region = df['event_location_region'].value_counts
    hostilities_count = df[df['took_part_in_the_hostilities'] == 'yes']['citizenship'].value_counts()
    noHostilitiesCount = df[df['took_part_in_the_hostilities'] == 'No']['citizenship'].value_counts()

    st.sidebar.write("No of Events : ",no_of_event)


    col1,col2,col3,col4 = st.sidebar.columns(4)
    with col1:
        st.subheader("Citizenship Count")
        st.write(citizenship_count())

    with col2:
        st.subheader("Event Location Region")
        st.write(event_location_region())

    with col3:
        st.sidebar.subheader("Hostilities Count")
        st.sidebar.write(hostilities_count)

    with col4:
        st.sidebar.subheader("Non Hostilities Count")
        st.sidebar.write(noHostilitiesCount)

    wepons_counts = df['ammunition'].value_counts
    st.sidebar.subheader("Wepon Counts")
    st.sidebar.write(wepons_counts())



    ## Data Analysis Part
    st.title("Israel Palestine Data Analysis")
    st.write("Data Sample",df)


    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Type of Injuries")
        typeOfInjury = df['type_of_injury'].value_counts()
        st.bar_chart(typeOfInjury)
    
    with col2:
        st.subheader("Distribution By Gender")
        gender = df['gender'].value_counts()
        st.bar_chart(gender, color='#FF0000')


    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Age Distribution of war")
        age = df['age'].describe()
        st.write(age)

    with col2:
        event_location_region = df['event_location_region'].value_counts()
        st.subheader("Event Locations")
        st.bar_chart(event_location_region)
    

    


    


    



    