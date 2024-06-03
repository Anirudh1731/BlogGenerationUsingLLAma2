import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


# function to get the response from llam2 model


def getLLamaresponse(input_text,no_words,blog_style):

    llm=CTransformers(model='',model_type='llama',config={'max_new_tokens':256,'temperature':0.01})

    #rompt template

    template=" write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words."

    prompt=PromptTemplate(input_variables=["style","text",'n_words'],template=template)


    #geenerate response


    response=llm(prompt.format(style=blog_style,text=input_text,n_words=no_words))
    print(response)




st.set_page_config(page_title="Generate blogs",page_icon='',layout='centered',initial_sidebar_state='collapsed')

st.header("Gnerate blogs")

input_text=st.text_input("Enter the blog topic")

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input("No of words required")
with col2:
    blog_style=st.selectbox('Writing the blog for',('Researcher','Data Scientist','Common people'))

submit=st.button("Generate")

if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))