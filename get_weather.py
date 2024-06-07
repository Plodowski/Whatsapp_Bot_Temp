import pathlib
import textwrap
import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyDO_PIXH3ThsyAvr67RWX9d4hI162UbCds'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
pergunta = "Preciso da temperatura do Rio de Janeiro agora com previsão para os póximos 4 dias. Quero que você crie."
resposta = model.generate_content(pergunta)

print(resposta.parts)