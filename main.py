import streamlit as st
import time
st.title('my_process')
my_bar = st.progress(0)

for i in range(100):
    my_bar.progress(i+1)
    time.sleep(0.02)
  
name = st.text_input("")
if st.button("Write Hello"):
  st.write("Hello",name)
  st.balloons()