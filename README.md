# **Image Processor**

Este projeto é um pacote Python simples para **processamento de imagens**. Ele oferece funcionalidades para **redimensionar**, **aplicar filtro em escala de cinza** e **aplicar desfoque (blur)** em imagens. O pacote utiliza a biblioteca **Pillow** para manipulação de imagens e pode ser facilmente integrado em outros projetos.

---

## **Funcionalidades**

- **Redimensionar imagens**: Modifica o tamanho da imagem para uma nova largura e altura especificadas.
- **Escala de cinza**: Converte a imagem original para uma versão em tons de cinza.
- **Desfoque (Blur)**: Aplica um filtro de desfoque à imagem original.
  
---

## **Instalação**

Para utilizar o pacote, é necessário ter o Python instalado em sua máquina. Além disso, você precisará instalar a biblioteca **Pillow**, que é utilizada para manipulação de imagens.

### **Passos para instalação**:

1. **Instale o Pillow** usando o seguinte comando no terminal:

   ```bash
   pip install pillow
   ```

---

## **Uso**

Após instalar o Pillow, você pode utilizar o pacote para realizar o processamento de imagens.

### **Exemplo de uso**:

```python
from image_processor import resize_image, apply_grayscale, apply_blur

# Caminho para a imagem de entrada
image_path = 'input_image.jpg'

# Redimensionar imagem
resize_image(image_path, 'output_resized.jpg', (200, 200))

# Converter imagem para escala de cinza
apply_grayscale(image_path, 'output_grayscale.jpg')

# Aplicar filtro de desfoque
apply_blur(image_path, 'output_blurred.jpg')
```

### **Funções disponíveis**:

1. **`resize_image(image_path, output_path, size)`**: Redimensiona a imagem para o tamanho especificado.

   - `image_path`: Caminho da imagem original.
   - `output_path`: Caminho onde a imagem redimensionada será salva.
   - `size`: Tupla contendo o novo tamanho da imagem (largura, altura).

2. **`apply_grayscale(image_path, output_path)`**: Converte a imagem para escala de cinza.

   - `image_path`: Caminho da imagem original.
   - `output_path`: Caminho onde a imagem em escala de cinza será salva.

3. **`apply_blur(image_path, output_path)`**: Aplica um filtro de desfoque na imagem.

   - `image_path`: Caminho da imagem original.
   - `output_path`: Caminho onde a imagem com filtro de desfoque será salva.

---

## **Exemplo de saída**:

Depois de rodar o script de exemplo, você verá três imagens geradas na pasta atual:

- `output_resized.jpg`: A imagem redimensionada.
- `output_grayscale.jpg`: A imagem em escala de cinza.
- `output_blurred.jpg`: A imagem com filtro de desfoque.

---

## **Publicação no PyPI**

Este pacote foi desenvolvido para ser compartilhado e reutilizado. Ele está disponível para instalação via **PyPI** (Python Package Index), tornando fácil integrá-lo em seus próprios projetos. Se você deseja publicar este pacote no PyPI, siga os passos abaixo:

1. Crie um arquivo `setup.py` com as informações do pacote.
2. Use os comandos:

   ```bash
   python setup.py sdist
   twine upload dist/*
   ```

Agora seu pacote estará disponível para ser instalado com:

```bash
pip install image-processor
```

---

## **Contribuição**

Sinta-se à vontade para fazer melhorias ou adicionar novos filtros. Qualquer contribuição é bem-vinda! Para contribuir, basta fazer um **fork** do repositório, criar uma branch para suas alterações e abrir um **pull request**.

---

## **Licença**

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## **Créditos**

Este projeto foi desenvolvido utilizando **Python** e **Pillow** para o processamento de imagens.
