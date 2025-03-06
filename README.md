# Web Scraping con Expresiones Regulares

Este proyecto realiza scraping en páginas web para extraer nombres de productos e imágenes mediante expresiones regulares, buffers y centinelas.

## 📌 Objetivo

Automatizar la extracción de productos de una tienda en línea o de videojuegos, generando un archivo exportable con los nombres y URLs de las imágenes.

## 🚀 Funcionalidades

- Procesamiento de archivos HTML descargados.
- Uso de buffers y centinelas para manejar la información secuencialmente.
- Aplicación de expresiones regulares para extraer datos relevantes.
- Generación de un archivo CSV con los productos y sus imágenes.

## 📂 Estructura del Proyecto

📁 -Web-Scraping-con-Expresiones-Regulares 
── 📄 script.py # Script principal para el scraping 
── 📄 productos.csv # Archivo de salida con los datos extraídos 
── 📄 pagina.html # Archivo HTML descargado para análisis 
── 📄 README.md # Documentación del proyecto


## 🛠️ Instalación y Uso

1. Clona este repositorio:
   ```sh
   git clone https://github.com/DiederichSolis/-Web-Scraping-con-Expresiones-Regulares.git

2. Navega al directorio del proyecto:
   ```sh
   cd -Web-Scraping-con-Expresiones-Regulares

3. Instala los módulos necesarios:
   ```sh
    pip install -r requirements.txt

4. Ejectuta el Script:
   ```sh
   python script.py

📊 Salida Esperada
El script generará un archivo productos.csv con la siguiente estructura:
 ```sh
Nombre del Producto, URL de la Imagen
"Producto 1", "https://example.com/imagen1.jpg"
"Producto 2", "https://example.com/imagen2.jpg"
...

   
