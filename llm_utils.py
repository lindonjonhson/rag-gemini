from config import GENERATION_MODEL
import google.generativeai as genai

def create_prompt(question, context):
    """Creates a prompt for the Gemini model using the question and retrieved context."""
    prompt = f"""Answer the question based on the context below. Add a field called 'References:', where you will add parts of the context that you used to base your answer.
    Context:
    {context}

    Question: {question}
    """
    return prompt

def generate_answer(prompt, model_name=GENERATION_MODEL):
    """Generates an answer using the Gemini model."""
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating answer: {e}")
        return "I'm sorry, I couldn't generate an answer."