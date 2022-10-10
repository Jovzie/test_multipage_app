#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.set_page_config(
    page_title="Multipage App",
    page_icon="J")
st.sidebar.success("Select a page above.")

st.title("Resume")
st.subheader("Jovana Vukovic")
st.write("jovana.vukovic@eastern.edu")


st.image("homepage_pic.jpg")

st.subheader("Education")
st.write("M.S., Data Science, Eastern University (expected graduation 2022)")
st.write("Ph.D., Experimental Psychology, University of Aberdeen (2010)")
st.write("Hon.B.Sc., Biology major, Psychology & Philosophy minors, University of Toronto (2005)")
st.write("Associate Diploma of The Royal Conservatory of Music, Voice Performance (2004)")
st.write("Associate Diploma of The Royal Conservatory of Music, Flute Performance (2003)")
st.write("RYT500, My Vinyasa Practice (expected 2024)")
st.write("RYT200, The Yoga Sanctuary of Toronto (2011)")
st.write("NAR Realtor, Florida (2019)")


st.subheader("Work Experience")
st.write("Associate Professor of Psychology, Broward College (2021-present)")
st.write("Assistant Professor of Psychology, Broward College (2016-2021)")
st.write("Assistant Professor of Psychology, West Texas A & M University (2012-2016)")
st.write("Postdoctoral Researcher, Durham University, (2010-2011)")
st.write("TA, Unversity of Aberdeen (2008-2010)")

st.subheader("Recent Volunteer Work")
st.write("Corresponding Secretary, The Opera Society - Affiliate of Florida Grand Opera (2021-current)")



st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.write("(All images on this website have been retrieved from https://pixabay.com/)")