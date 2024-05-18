# Llama_models_projects
Repository to go through projects using Llama3, from introducing it into the data stream and combining it with other models to rag and finetuning. In the first example we focus on using Llama3 in a data stream, with regular expression response extraction and batch analysis.

**Film_categorisation_LLama3.ipynb** -> Example of using Llama3 for movie categorisation, this mini-project includes validation, regular expressions and use of various language models combined to give batch output.

**PDFQuery_LangChain.ipynb** -> Use of an online vector database (Cassandra) to store the documents where a query will later be made. To do this, an embedding is made with nomic-embed-text, which will then be passed to the vectiral database, and then we will make the queries and see which documents have been used to answer the query.

**Llama3Streamlit_app** -> Streamlit application where we can query a local model to make a blog entry, we could combine this with any of the previous cases to give better functionalities.

<div align="center">
  <img src="https://github.com/Zauler/Llama_models_projects/blob/main/Llama3Streamlit_app/App_running.png?raw=true" />
</div>

**Gemimi_Streamlit_app** -> Streamlit application where you can upload your invoices to get data on this image, a possible alternative to this flow would be to use the same model to always get the same data from a series of images and return this response in a specific document type. 

<div align="center">
In this first image we can see what it looks like before entering an invoice. 


  <img src="https://github.com/Zauler/Llama_models_projects/blob/main/Gemimi_Streamlit_app/Invoice_1.png" />


In the second image we can see an example of a query with an invoice found on the internet.



  <img src="https://github.com/Zauler/Llama_models_projects/blob/main/Gemimi_Streamlit_app/Invoice_2.png" />
</div>
