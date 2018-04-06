# catastro-lib-python

Library developed in python. This library allow to access the public web services of the Portal of Spanish Catastro and obtains the results in json format.


Methods defined here:

### ConsultaDNPLOCJson(provincia, municipio, sigla, calle, numero, bloque=None, escalera=None, planta=None, puerta=None)
    Proporciona la lista de todos los inmuebles coincidentes o sus datos.
     
    Este servicio puede devolver o bien la lista de todos los inmuebles que
    coinciden con los criterios de búsqueda, proporcionando para cada
    inmueble la referencia catastral y su localización
    (bloque/escalera/planta/puerta) o bien, en el caso de que solo exista
    un inmueble con los parámetros de entrada indicados, proporciona los
    datos de un inmueble.
     
    :param str: Nombre de la provincia
    :param str: Nombre del municipio
    :param str: Sigla
    :param str: Nombre de la calle
    :param str,int: Numero del que se quiere conocer los datos
    :param str,int: Opcional,numero de bloque
    :param str: Opcional, numero d'escala
    :param str,int: Opcional, numero de planta
    :param str,int: Opcional, numero de puerta
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

## Class methods defined here:

### ConsultaCPMRCJSon(municipio, srs, rc) from builtins.type
    Proporciona la localizacion de una parcela.
     
    A partir de la RC de una parcela se obtienen las coordenadas X, Y en el
    sistema de referencia en el que está almacenado el dato en la D.G. del
    Catastro, a menos que se especifique lo contrario en el parámetro
    opcional SRS que se indica en la respuesta, así como el domicilio
    (municipio, calle y número o polígono, parcela y unicipio).
     
    :param str: Nombre de la provincia
    :param str: Nombre del municipio
    :param str,int: Sistema de coordenadas
    :param str: Referencia catastral
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaDNPLOCCodigosJson(municipio, sigla, nombrevia, numero, bloque=None, escalera=None, planta=None, puerta=None) from builtins.type
    Proporciona la lista de todos los inmuebles que coinciden.
     
    Este servicio puede devolver o bien la lista de todos los inmuebles que
    coinciden con los criterios de búsqueda, proporcionando para cada
    inmueble la referencia catastral y su localización
    (bloque/escalera/planta/puerta) o bien,en el caso de que solo exista un
    inmueble con los parámetros de entrada indicados, proporciona los datos
    de un inmueble.
     
    :param str: Nombre de la provincia
    :param str: Nombre del municipio
    :param str: Sigla
    :param str: Nombre de la via
    :param str,int: Numero de inmueble
    :param str,int: Numero de bloque
    :param str: Escalera
    :param str,int: Numero de planta
    :param str,int: Numero de puerta
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaDNPPPCodigosJson(municipio, poligono, parcela) from builtins.type
    Proporciona los datos catastrales de un inmueble.
     
    Este servicio es idéntico al de "Consulta de DATOS CATASTRALES NO
    PROTEGIDOS de un inmueble identificado por su localización" en todo
    excepto en los parámetros de entrada.
     
    :param str: Nombre de la provincia
    :param str: Nombre del municipio
    :param str: Codigo del poligono
    :param str: Codigo de la parcela
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaDNPRCCodigosJson(municipio, rc) from builtins.type
    Proporciona los datos catastrales de un inmueble,
     
    Este servicio es idéntico al de "Consulta de DATOS CATASTRALES NO
    PROTEGIDOS de un inmueble identificado por su localización"
    en todo excepto en los parámetros de entrada.
     
    :param str: Nombre de la provincia
    :param str: Nombre del municipio
    :param str: Referencia catastral
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaDNPRCJSon(municipio, rc) from builtins.type
    Proporciona los datos catastrales no protegidos de un inmueble
     
    Este servicio es idéntico al de "Consulta de DATOS CATASTRALES NO
    PROTEGIDOS de un inmueble identificado por su localización" en todo
    excepto en los parámetros de entrada.
     
    :param str: Nombre de la provincia
    :param str: Nombre del municipio
    :param str: Referencia catastral
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaMunicipioCodigosJSon(municipio) from builtins.type
    Proporciona un listado de todos los nombres de los municipios de una provincia.
     
    Proporciona un listado de todos los nombres de los municipios de una
    provincia (parámetro "Provincia"),así como sus códigos (de Hacienda y
    del INE), cuyo nombre Servicios web del Catastro 5 contiene la cadena
    del parámetro de entrada "Municipio".En caso de que este último
    parámetro no tenga ningún valor, el servicio devuelve todos los
    municipios de la provincia.También proporciona información de si existe
    cartografía catastral (urbana o rústica) de cada municipio.
     
    :param str: Nombre de la provincia
    :param str: Nombre del municipio
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaMunicipioJSon(municipio=None) from builtins.type
    Proporciona un listado de todos los municipios de una provincia.
     
    Proporciona un listado de todos los nombres de los municipios de una
    provincia (parámetro "Provincia"),así como sus códigos (de Hacienda
    y del INE), cuyo nombre Servicios web del Catastro 5 contiene la cadena
    del parámetro de entrada "Municipio". En caso de que este último
    parámetro no tenga ningún valor, el servicio devuelve todos los
    municipios de la  provincia.También proporciona información de si
    existe cartografía catastral (urbana o rústica) de cada municipio.
     
    :param str: Nombre de la provincia
    :param str: Opcional , nombre del municipio
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaNumeroCodigosJson(municipio, tipovia, nombrevia, numero) from builtins.type
    Proporciona la referencia catastral de la finca correspondiente.
     
    Proporciona, o bien la referencia catastral de la finca correspondiente
    al contenido del parámetro "Número", en caso de que este exista, o bien
    se devuelve un error ("El número no existe") y se proporciona una lista
    de los números más aproximados al solicitado, en un rango de 5 por arriba
    y 5 por abajo. Por ejemplo, si se solicita el número 10, y en esa vía
    existen los números 2,3,6,7,9,11,15 y 17, se devuelve una lista con los
    números 6,7,9,11 y 15. Junto con la lista de números, se proporcionan
    las referencias catastrales de las fincas.
     
    :param str: Nombre de la provincia
    :param str: Nombre del municipio
    :param str: Tipo de la via
    :param str: Nombre de la via
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaNumeroJSon(municipio, tipovia, nombrevia, numero) from builtins.type
    Proporciona la referencia catastral de la finca correspondiente.
     
    Proporciona,o bien la referencia catastral de la finca correspondiente
    al contenido del parámetro "Número",en caso de que este exista,o bien se
    devuelve un error ("El número no existe") y se proporciona una lista
    de los números más aproximados al solicitado, en un rango de 5 por
    arriba y 5 por abajo. Por ejemplo, si se solicita el número 10, y en
    esa vía existen los números 2,3,6,7,9,11,15 y 17, se devuelve una lista
    con los números 6,7,9,11 y 15.Junto con la lista de números, se
    proporcionan las referencias catastrales de las fincas.
     
    :param str: Nombre de la provincia
    :param str: Nombre del municipio
    :param str: Tipo d ela via
    :param str: Nombre de la via
    :param str,int: Numero del que se desea conocer la referencia
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaProvincia(...) from builtins.type
    Proporciona un listado de todas las provincias de España.
     
    Proporciona un listado de todas las provincias españolas en
    las que tiene competencia la Dirección general del Catastro.
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaProvinciaJSon() from builtins.type
    Proporciona un listado de las provincias.
     
    Proporciona un listado de todas las provincias españolas en las que
    tiene competencia la Dirección general del Catastro.
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaRCCOORDistanciaJson(x, y) from builtins.type
    Proporciona la referencia catastral a partir de unas coordenadas.
     
    A partir de unas coordenadas (X e Y) y su sistema de referencia se
    obtiene la referencia catastral de la parcela localizada en ese
    punto así como el domicilio (municipio, calle y número o polígono,
    parcela y municipio). En caso de no encontrar ninguna referencia
    catastral en dicho punto, se buscará en un área cuadrada de 50
    metros de lado, centrada en dichas coordenadas, y se devolverá
    la lista de referencias catastrales encontradas en dicha área.
     
    :param str,int: Sistema de coordenadas
    :param str,int,float: Coordanda X
    :param str,int,float: Coordanda Y
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaRCCOORJSon(x, y) from builtins.type
    A partir de unas coordenadas se obtiene la referencia catastral.
     
    A partir de unas coordenadas (X e Y) y su sistema de referencia se
    obtiene la referencia catastral de la parcela localizada en ese punto
    así como el domicilio (municipio, calle y número o polígono, parcela y
    municipio).
     
    :param str,int: Sistema de coordenadas
    :param str,int,float: Coordanda x
    :param str,int,float: Coordenada Y
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaViaCodigosJSon(municipio, tipovia=None, nombrevia=None) from builtins.type
    Proporciona un listado de las vías de un municipio
     
    Proporciona un listado de todas las vías de un municipio
    (parámetros "Provincia" y "Municipio"), así como los códigos de las
    mismas según la Dirección General del Catastro (DGC), cuyo nombre
    contiene la cadena del parámetro de entrada "NombreVia" y, en caso
    de que el parámetro "TipoVia" contenga información, existe
    coincidencia en el tipo de la vía. En caso de que el parámetro
    "NombreVia" no tenga ningún valor, el servicio devuelve todas
    las vías del municipio del "TipoVia" indicado.
     
    :param str: Nombre de provincia
    :param str: Nombre del municipio
    :param str: Opcional,Tipo de via
    :param str: Nombre de via
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

### ConsultaViaJSon(municipio, tipovia=None, nombrevia=None) from builtins.type
    Proporciona un listado de todas las vías de un municipio.
     
    Proporciona un listado de todas las vías de un municipio (parámetros
    "Provincia" y "Municipio"), así como los códigos de las mismas según la
    Dirección General del Catastro (DGC) , cuyo nombre contiene la cadena
    del parámetro de entrada "NombreVia" y, en caso de que el parámetro
    "TipoVia" contenga información, existe coincidencia en el tipo de la
    vía. En caso de que el parámetro "NombreVia" no tenga ningún valor, el
    servicio devuelve todas las vías del municipio del "TipoVia" indicado.
     
    :param str: Nombre de la provincia
    :param str: Nombre de municipio
     
    :return: Retorna un dicionario con los datos de la consutla
    :return_type: json

### Consulta_DNPPPJSon(municipio, poligono, parcela) from builtins.type
    Proporciona los datos catastrales no protegidos de un inmueble
     
    Este servicio es idéntico al de "Consulta de DATOS CATASTRALES NO
    PROTEGIDOS de un inmueble identificado por su localización" en todo
    excepto en los parámetros de entrada.
     
    :param str: Nombre de la provincia
    :param str: Nombre del municipio
    :param str: Codigo del poligono
    :param str: Codigo de la parcela
     
    :return: Retorna los datos que devuelve el servicio del catastro formateados en JSON
    :return_type: json

## Data descriptors defined here:

__dict__
    dictionary for instance variables (if defined)

__weakref__
    list of weak references to the object (if defined)

Data and other attributes defined here:

home_url = 'http://ovc.catastro.meh.es/ovcservweb/'