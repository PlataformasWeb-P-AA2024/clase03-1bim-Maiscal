archivo = open('Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r", encoding='utf-8')

# obtener las líneas del archivo
lineas = archivo.readlines()

# obtener los encabezados
encabezados = lineas[0].strip().split("|")

# procesar cada línea del archivo
for linea in lineas[1:]:
    # separar la línea en valores
    linea = linea.strip().split("|")
    
    # crear la página HTML para cada institución
    pagina = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Información de Institución</title>
      </head>
      <body>
      <h1>Información de Institución</h1>
      <ul>
    """
    # agrego un for para recorrer el encabezado correspondiente
    for i, valor in enumerate(linea):
        # excluyo los encabezados 10 -11 - 12
        if i not in  [10, 11, 12]:
             # agrego las sentencias del recorrido con %s
             pagina += "<b>%s:</b> %s<br>" % (encabezados[i], valor)
    pagina += """
      </ul>
      </body>
    </html>
    """
    
    # crear el archivo HTML para cada institución
    archivo_generado = open("%s.html" % linea[0], "w", encoding='utf-8')
    archivo_generado.write(pagina)
    archivo_generado.close()

archivo.close()