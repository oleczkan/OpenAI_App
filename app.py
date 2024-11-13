import openai
import os
from dotenv import load_dotenv
import re

# Wczytanie klucza API z pliku .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_article(file_path):
    """Wczytuje treść artykułu z pliku tekstowego."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_html_content(article_text):
    prompt = f"""
Przekształć poniższy tekst artykułu na format HTML, spełniając następujące wytyczne:
1. Użyj dokładnie podanej treści artykułu, bez modyfikowania nagłówków, tytułów czy opisów obrazków.
2. Użyj tagów HTML do strukturyzacji treści: <h1> dla głównego nagłówka, <h2> dla podsekcji, <p> dla akapitów.
3. W miejscach, które mogą wymagać ilustracji, dodaj tag <img src="image_placeholder.jpg" alt="Dokładny opis grafiki"> z opisem, który można bezpośrednio wykorzystać jako prompt do wygenerowania obrazu.
4. Dodaj podpisy pod grafikami z użyciem tagu <p>, umieszczone bezpośrednio pod każdym obrazkiem.
5. Wygenerowany kod HTML ma zawierać wyłącznie treść do umieszczenia między tagami <body> i </body>, bez dodatkowych znaczników <html>, <head>, ani CSS.

Oto tekst artykułu do sformatowania:

{article_text}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that formats articles to HTML."},
            {"role": "user", "content": prompt}
        ]
    )
    content = response['choices'][0]['message']['content'].strip()
    
    # Usuń potencjalne znaczniki Markdown, jeśli występują
    content = re.sub(r"^```html|```$", "", content, flags=re.MULTILINE)
    return content.strip()

def save_to_file(content, file_name="artykul.html"):
    """Zapisuje wygenerowany kod HTML do pliku."""
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    article_text = read_article('artykul.txt')
    html_content = generate_html_content(article_text)
    save_to_file(html_content)
    print("Kod HTML zapisany w pliku artykul.html")

if __name__ == "__main__":
    main()
