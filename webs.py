
import re
import csv


#  leer el contenido de una página web desde un archivo local
def leerPaginaWebConBuffer(archivoPagina, tamanoBuffer=1024):
    contenido = ""
    with open(archivoPagina, "r", encoding="utf-8") as archivo:
        while True:
            bloque = archivo.read(tamanoBuffer)
            if not bloque: 
                break
            contenido += bloque
    return contenido


# Análisis del contenido HTML para obtener productos y sus imágenes
def analizarHtmlYExtraerDatos(contenidoHtml):
    expresionRegular = re.compile(
        r'<div class="caption col-12">.*?<p class="pr-4">(.*?)</p>.*?<div class="overflow-hidden".*?<img.*?src="(.*?)"',
        re.DOTALL,
    )
    listaProductos = expresionRegular.findall(contenidoHtml)
    return listaProductos


# Guarda los datos extraídos en un archivo CSV
def guardarEnCsv(datosProductos, nombreArchivo):
    with open(nombreArchivo, "w", newline="", encoding="utf-8") as archivoCsv:
        manejadorCsv = csv.writer(archivoCsv)
        # Encabezados del archivo CSV
        manejadorCsv.writerow(["Nombre del Producto", "URL de la Imagen"])
        manejadorCsv.writerows(datosProductos)  


# Inicia el proceso de carga
contenidoPagina = leerPaginaWebConBuffer("pagina.html")
productosEncontrados = analizarHtmlYExtraerDatos(contenidoPagina)
guardarEnCsv(productosEncontrados, "listadoProductos.csv")

print("CSV creado")
