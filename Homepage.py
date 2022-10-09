#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.set_page_config(
    page_title="Multipage App",
    page_icon="J")

st.title("Resume Page")
st.sidebar.success("Select a page above.")

st.image("homepage_pic.jpg")

st.write("Education: coming soon")
st.write("Work Experience: coming soon")