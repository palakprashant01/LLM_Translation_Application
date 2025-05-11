from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

#install and import LangServe
from langserve import add_routes #add_routes will help create APIs


groq_api_key = os.getenv("GROQ_API_KEY")

#Load ChatGroq model
model = ChatGroq(model = "Gemma2-9b-it", groq_api_key = groq_api_key)

#prompt template
#define generic template
generic_template = "Translate the following into {language}:"
prompt = ChatPromptTemplate.from_messages(
    [("system", generic_template), ("user", "{text}")] #we have to give text at runtime
    
)

#create string output parser
parser = StrOutputParser()

#create chain
chain = prompt|model|parser

#app definition
app = FastAPI(title = "Langchain Server", version = "1.0",
              description = "A simple API server using langchain runnable interfaces")

#add chain routes
add_routes(app, chain, path = "/chain")

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host = "localhost", port = 8000)
