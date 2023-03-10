import streamlit as st
import pandas as pd
import os
import time

# Dashboard functions
def get_datestamp_txt():
    return time.strftime("%Y%m%d")

def get_files_by_day(user, day, dir):
   b_today_training = []

   for file in os.listdir(dir):
      if file.startswith(day) and file.endswith(".csv") and user == file[16:20]:
         b_today_training.append(file)
   return b_today_training

def get_files_by_dir(user, dir):
   c_whole_training = []

   for file in os.listdir(dir):
      if file.endswith(".csv") and user == file[16:20]:
         c_whole_training.append(file)
   return c_whole_training


# Support variables
today = get_datestamp_txt()
actual_user = "U002"
dir_user = os.getcwd() + "\\user_data\\"

# Dashboard data variables
a_recent_training = "20230309_125129_U002_push_up.csv"
b_today_training = get_files_by_day(actual_user, today, dir_user)
c_whole_training = get_files_by_dir(actual_user, dir_user)


# Streamlit tabs
tab1, tab2, tab3 = st.tabs(["A. Recent training", "B. Today's training", "C. Your whole training"])

with tab1:
   st.header("A. Recent training")
   st.text("File: "+ a_recent_training)
   df_a_rt = pd.read_csv(dir_user + a_recent_training)
   #st.table(df_rt)
   st.image("https://i0.wp.com/www.fusioncharts.com/blog/wp-content/uploads/2013/08/Nike-+-web-app1.jpg?resize=616%2C441&ssl=1")

with tab2:
   st.header("B. Today's training")
   st.text("Files (" + str(len(b_today_training)) + "): ")
   st.text(b_today_training)
   #df_b_tt = pd.read_csv()
   st.image("https://i.stack.imgur.com/KEm4K.png")

with tab3:
   st.header("C. Your whole training")
   st.text("Files (" + str(len(c_whole_training)) + "): ")
   st.text(c_whole_training)
   #df_c_wt = pd.read_csv()
   st.image("https://i.imgur.com/2AE3gch.png")