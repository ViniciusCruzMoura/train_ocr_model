from easyocr import easyocr

url = "https://jeroen.github.io/images/testocr.png"
custom_model_path = "/home/jdedv/sistemas/EasyOCR/trainer/saved_models/en_filtered"

leitor = easyocr.Reader(['pt'], gpu=True, model_storage_directory=custom_model_path)
lista_de_palavras = leitor.readtext(url, detail=0)

print(' '.join(r for r in lista_de_palavras))
print(lista_de_palavras)