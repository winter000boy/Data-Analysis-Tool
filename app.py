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
        st.sidebar.subheader("Citizenship Count")
        st.sidebar.write(citizenship_count())

    with col2:
        st.sidebar.subheader("Event Location Region")
        st.sidebar.write(event_location_region())

    with col3:
        st.sidebar.subheader("Hostilities Count")
        st.sidebar.write(hostilities_count)

    with col4:
        st.sidebar.subheader("Non Hostilities Count")
        st.sidebar.write(noHostilitiesCount)



    