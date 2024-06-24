from openai import OpenAI
from dotenv import load_dotenv
import os
import re

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  api_key = openai_api_key
)

def get_title(text):
  pattern = r'\*Título de la sentencia\*:\s*(.*?)\n2\.'
  # Search for the pattern in the text
  match = re.search(pattern, text, re.DOTALL)

  # Extract the title if the pattern matches
  if match:
    title = match.group(1).strip()
    print("Título de la sentencia:", title)
  else:
    print("Título de la sentencia not found")

def summarize_text(text):
    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {
          "role": "user",
          "content": f"""
          Sos un abogado especialista en justicia federal. Necesito que analices la siguiente sentencia de la Corte Superema de Justicia de la Nación, me la resumas en no más de 100 palabras y me digas que fue lo que se resolvió.
          Además quiero que lo devuelvas en un formato como el siguiente:
          *Nueva sentencia disponible: *
          
          1. 📜 *Título de la sentencia*:
          2. 🕵🏻‍♀️ *Involucrados*:
          3. 👨🏻‍⚖️ *Resolución*:
          4. 📌 *Resumen ejecutivo*:
          : {text}"""
        }
      ]
    )

    return response.choices[0].message.content