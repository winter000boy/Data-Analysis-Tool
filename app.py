import pandas as pd
import streamlit as st



st.sidebar.title("Upload Dataset")
Upload_File = st.sidebar.file_uploader("Choose csv file", type='csv')
if Upload_File is not None:
    df = pd.read_csv(Upload_File)

    citizenship_count = df['citizenship'].value_counts
    event_location_region = df['event_location_region'].value_counts
    hostilities_count = df[df['took_part_in_the_hostilities'] == 'yes']['citizenship'].value_counts()
    noHostilitiesCount = df[df['took_part_in_the_hostilities'] == 'No']['citizenship'].value_counts()
