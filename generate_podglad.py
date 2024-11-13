def generate_podglad():
    with open("szablon.html", 'r', encoding='utf-8') as szablon:
        szablon_content = szablon.read()
    
    with open("artykul.html", 'r', encoding='utf-8') as artykul:
        artykul_content = artykul.read()
    
    # Wstawienie zawartości artykułu do miejsca w body szablonu
    podglad_content = szablon_content.replace("<!-- Wklej tutaj zawartość pliku artykul.html -->", artykul_content)
    
    with open("podglad.html", 'w', encoding='utf-8') as podglad:
        podglad.write(podglad_content)

    print("Podgląd zapisany w pliku podglad.html")

generate_podglad()
