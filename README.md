This application is a simple yet powerful translation tool built using LangChain and the Groq API. It translates text from English into various languages using a language model. The application showcases the capabilities of LangChain, including the use of language models, prompt templates, output parsers, and the LangChain Expression Language (LCEL) to chain components together. Additionally, it provides insights into debugging and tracing with LangSmith and deploying the application with LangServe.

Features:
1. Language Model Integration: Utilizes the Groq API to access advanced language models like Gemma2 for translation tasks.
2. Prompt Templates: Employs customizable prompt templates to enhance the translation process.
3. Output Parsing: Implements output parsers to extract and format the model's responses effectively.
4. LCEL Chaining: Demonstrates the chaining of components using LangChain Expression Language for streamlined processing.
5. API Deployment: Provides a FastAPI-based server to expose the translation functionality as an API endpoint.

We also manage the conversation history using trimmer, prompt templates, etc. These are required while buiding a chatbot to prevent conversations overflowing from the context window of the LLM.
