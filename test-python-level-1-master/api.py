#!/usr/bin/env python3
#requeriments requests

import requests
import sys
import time



class Api:
    #Clase que interactua con la API wapitest.

    def __init__(self):
        #Constructor url

        self.url = "http://localhost:8000"

    

    def eleccion(self):
        #Solicita usuario & password y construye diccionario
        self.choice = sys.argv[1]
        if self.choice == 'fisica':
            self.listar_fisicas()
        elif self.choice == 'juridica':
            self.listar_juridicas()
        else:
            
            print('************************************')
            print("Ingrese su opcion al ingresar el script")
            print("fisica / juridica")
            print("ejemplo : python3 api.py fisica")
            print('************************************')
    
    def listar_fisicas(self):

        url = self.url + '/fisica/'
        print(url)
        try:
            self.response = requests.get(url)

            if self.response.ok:
                return self.response 
            else:
                self.response.status_code 
        except:
            print("Sin conexión")    
                           

    def listar_juridicas(self):

        url = self.url + '/juridica/'
        print(url)

        try:
            self.response = requests.get(url)
            
            if self.response.ok:
                return self.response

        except:
            print("Sin conexión")       

    def mostrar(self):
        print(self.response.text)  



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Seleccione  fisica/juridica al ejecutar el script ")
        print("ejemplo : python3 api.py fisica")
        sys.exit(1)

    r = Api()
    r.eleccion()
    r.mostrar()