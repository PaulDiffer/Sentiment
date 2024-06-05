"""La librería TextBlob de Python es una herramienta poderosa para el procesamiento del lenguaje natural 
(NLP, por sus siglas en inglés). Ofrece una interfaz simple para realizar tareas comunes de NLP, 
como tokenización, análisis de sentimientos, clasificación de texto, traducción y más."""

from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = "Positivo"
    elif polarity < 0:
        sentiment = "Negativo"
    else:
        sentiment = "Neutro"
        
    print(f"Text {text}")
    print(f"Polaridad {polarity}")
    print(f"Sentimiento {sentiment}")
    
text_example = "I love you"
analyze_sentiment(text_example)