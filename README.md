# RAG using Gemini

Install Python 3.9

after that create environment with

C:\Users\User\\.pyenv\pyenv-win\versions\3.9.13\python -m venv .venv


Venv name: .venv
python version: 3.9

To activate do:
.\\.venv\Scripts\activate

To deactivate do:
deactivate


After activating the environment it is time to install the requirements

For that, please run the following command:
pip install -r requirements.txt

Once done installing the requirements, create a file named ".env" and define the variable "GEMINI_API_KEY" within it.

Once the variable has been defined, you can run the server by running "uvicorn main:app"



References:

https://ai.google.dev/gemini-api/docs/embeddings
