#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import notebook_with_function_V3


# Write the Streamlit application code
def main():
    st.title("Form from audio Application")

    # Prompt the user to start recording
    st.write("Waiting for signal to start recording...")
    start_recording = st.button("Start Recording")

    if start_recording:
        # Call the function to start recording and generate the form URL
        st.write("Speak something...")
        text,form_url = notebook_with_function_V3.one_for_all_V3()
        st.markdown("You said:")
        st.markdown(text)
        st.write("Generating the form URL...")
        st.markdown("Form URL:")
        st.markdown(form_url)

# Run the Streamlit application
if __name__ == '__main__':
    main()


# In[ ]:




