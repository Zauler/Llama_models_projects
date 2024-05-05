import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
#from langchain.llms import ctransformers ## If you want to import the model direcly you can use this.


## Funtion to get response from Llama3 model


def getLlamaresponse(input_text,no_words,blog_style):
    
    ### Llama3 model 
    llm = Ollama(model="llama3",temperature=0.01)
    ### if you want import it direcly
    #llm=ctransformers(model="pathofthemodel",
    #                  model_type="llama",
    #                  config={"max_new_tokens":256,
    #                          "temperature":0.01})
    
    template = """ 
    Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
    """
    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                            template=template)
    
    ## Generate the response from the Llama3 model
    response = llm.invoke(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words ))
    print(response)
    return response 


st.set_page_config(page_title="Generate Blogs",
                   page_icon="🤖",
                   layout="centered",
                   initial_sidebar_state="collapsed")
st.header("🤖 Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")


## Creating to more columns for additonal 2 fields 

col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of Words")
with col2:
    blog_style = st.selectbox("Writing the blog for",
                              ("Researchers","Data Scientist","Commont people"),index=0)
    
submit= st.button("Generate")

## Final response 
if submit:
    st.write(getLlamaresponse(input_text,no_words,blog_style))