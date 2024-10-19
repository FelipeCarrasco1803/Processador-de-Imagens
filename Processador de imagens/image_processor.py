# image_processor.py

from PIL import Image, ImageFilter
import os

# Funções de processamento de imagem

def resize_image(image_path, output_path, size):
    """
    Redimensiona uma imagem para o tamanho especificado.
    
    :param image_path: Caminho da imagem original
    :param output_path: Caminho onde a imagem redimensionada será salva
    :param size: Tupla (largura, altura) para o novo tamanho
    """
    with Image.open(image_path) as img:
        img_resized = img.resize(size)
        img_resized.save(output_path)
    print(f"Imagem redimensionada salva em {output_path}")

def apply_grayscale(image_path, output_path):
    """
    Aplica o filtro em escala de cinza em uma imagem.
    
    :param image_path: Caminho da imagem original
    :param output_path: Caminho onde a imagem com filtro será salva
    """
    with Image.open(image_path) as img:
        img_grayscale = img.convert("L")
        img_grayscale.save(output_path)
    print(f"Imagem em escala de cinza salva em {output_path}")

def apply_blur(image_path, output_path):
    """
    Aplica um filtro de desfoque (blur) em uma imagem.
    
    :param image_path: Caminho da imagem original
    :param output_path: Caminho onde a imagem com filtro será salva
    """
    with Image.open(image_path) as img:
        img_blurred = img.filter(ImageFilter.BLUR)
        img_blurred.save(output_path)
    print(f"Imagem com desfoque salva em {output_path}")

# Função principal para testes e execução

def main():
    # Testes simples
    image_path = 'input_image.jpg'
    
    # Testa redimensionar
    output_resized = 'output_resized.jpg'
    resize_image(image_path, output_resized, (200, 200))
    
    # Testa escala de cinza
    output_grayscale = 'output_grayscale.jpg'
    apply_grayscale(image_path, output_grayscale)
    
    # Testa desfoque
    output_blurred = 'output_blurred.jpg'
    apply_blur(image_path, output_blurred)
    
if __name__ == '__main__':
    main()
