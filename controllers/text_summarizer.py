from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    api_key = openai_api_key
)

def summarize_text(text):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {
            "role": "user",
            "content": f"""
            Sos un abogado especialista en justicia federal. Necesito que analices la siguiente sentencia de la Corte Superema de Justicia de la Nación, me la resumas en no más de 100 palabras y me digas que fue lo que se resolvió.
            Además quiero que lo devuelvas en un formato como el siguiente: 
            1. *Título de la sentencia*:
            2. *Involucrados en la causa*:
            3. *Resolución*:
            4. *Resumen ejecutivo*:
            : {text}"""
        }
    ]
    )

    return response.choices[0].message.content