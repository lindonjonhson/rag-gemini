#

Install Python 3.9

after that create environment with

C:\Users\lindo\.pyenv\pyenv-win\versions\3.9.13\python -m venv test


Venv name: test
python version: 3.9

To activate do:
.\.venv\Scripts\activate

To deactivate do:
deactivate


After activating the environment it is time to install the requirements

For that, please run the following command:
pip install -r requirements.txt

Also, please download the pdf file at "https://edis.ifas.ufl.edu/publication/vh021" and place it inside the "data" folder

After setup is done, run  "fill_db.py"

Currently rudding tests on:
gemini embedding
data_storing

They need to do the same thing as fill db


References:

https://ai.google.dev/gemini-api/docs/embeddings
