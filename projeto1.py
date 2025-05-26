from PIL import Image
import numpy as np
import os  # Adicionado para verificar o diretório

def main():
    try:
        # da uma checada no diretório
        print("Diretório atual:", os.getcwd())
        print("Arquivos no diretório:", os.listdir())  # Lista todos os arquivos (opcional)
       
        img = Image.open("gojo-jujutsu.png")

        # Converter a imagem em dados binários
        img_data = np.array(img)
        data = img_data.tobytes()

        print("\nDimensões da imagem:", img_data.shape, "\n")

        # Salva a imagem em binário
        with open("original_img.bin", "wb") as file:
            file.write(data)

    except FileNotFoundError:
        print("/nErro: Arquivo 'gojo-jujutsu.png' não encontrado no diretório atual.")
    except Exception as e:
        print(f"/nErro ao processar a imagem: {e}")
    modified_data = np.frombuffer(data, dtype=np.uint8) . reshape(img_data.shape) 
    modified_data = np.fliplr(modified_data)
    modified_img = Image.fromarray(modified_data)    
    modified_img.show()                              
if __name__ == "__main__":
    main()