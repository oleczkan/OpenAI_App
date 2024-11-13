# OpenAI_App

## Aplikacja napisana w Pythonie, która generuje plik HTML na podstawie treści artykułu, używając OpenAI API. Aplikacja strukturyzuje treść w HTML i dodaje miejsca na obrazki, zgodnie z wymaganiami.

## Funkcjonalności
Wczytuje treść artykułu z pliku artykul.txt.
Przesyła treść do OpenAI API, aby wygenerować kod HTML.
Generuje plik artykul.html zawierający strukturalny kod HTML z miejscami na obrazy, opisami alt i podpisami pod obrazkami.


## Instrukcja uruchomienia
Sklonuj repozytorium: git clone https://github.com/oleczkan/OpenAI_App.git i przejdź do katalogu projektu.
Utwórz wirtualne środowisko i zainstaluj wymagane pakiety: python -m venv venv, następnie aktywuj środowisko i zainstaluj wymagania z pliku requirements.txt.
Utwórz plik .env i dodaj swój klucz API OpenAI w formacie: OPENAI_API_KEY=your_openai_api_key_here.
Uruchom aplikację, aby wygenerować plik HTML z przetworzonym artykułem.
Wygenerowany plik HTML znajdziesz w katalogu projektu jako artykul.html. Plik będzie zawierał sformatowaną treść artykułu z miejscami na obrazki.


## Wymagania
Python w wersji 3.x
Biblioteka openai (zainstalowana z pliku requirements.txt)
Plik artykul.txt z treścią artykułu do sformatowania (plik powinien znajdować się w katalogu projektu).
