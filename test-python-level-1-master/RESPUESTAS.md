# Autor: MAZZURQUE Emiliano

- En la carpeta Mazzurque se encuentra el proyecto de Django que contiene la API. 

- El archivo mazzurque/ejercicio/test.py contiene testeo de la base de datos.  

- El archivo api.py contiene una Api que permite lista las titulares por su tipo.


# Los siguientes son  las request que permitan probar los endpoints utilizando la herramienta curl.


# Creaccion

curl --data "nombre=Julio&apellido=Bevacqua&dni=27259032&cuit=20272590322" http://localhost:8000/fisica/

curl --data "razon=cooperativa industrial&año=1957&cuit=30456789272" http://localhost:8000/juridica/

# Lectura

curl http://localhost:8000/fisica/1/

curl http://localhost:8000/juridica/1/

# Modifación

curl -X PUT --data "nombre=Natalia&apellido=Selidez&dni=33456190&cuit=27334561902" http://localhost:8000/fisica/2/

curl -X PUT --data "razon=Cooperativa textil&año=2010&cuit=30421987043" http://localhost:8000/juridica/2/

# Borrado

curl -X DELETE  http://localhost:8000/fidica/1/

curl -X DELETE  http://localhost:8000/juridica/1/

# Listado

curl http://localhost:8000/fisica/

curl http://localhost:8000/juridica/

