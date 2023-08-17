import xmltodict
import os
import json

import xml.etree.ElementTree as ET



def get_xml(file):
    with open(f'nfs/{file}', 'rb') as fd:
        doc = xmltodict.parse(fd)
        return doc
    

def find_key(dictionary, target_key):
    """
    Busca una clave específica dentro de un diccionario anidado.

    :param dictionary: El diccionario en el que se realizará la búsqueda.
    :param target_key: La clave que se desea buscar.
    :return: El valor asociado a la clave si se encuentra, None si no se encuentra.
    """
    if isinstance(dictionary, dict):
        if target_key in dictionary:
            return dictionary[target_key]
        for key, value in dictionary.items():
            result = find_key(value, target_key)
            if result is not None:
                return result
    elif isinstance(dictionary, list):
        for item in dictionary:
            result = find_key(item, target_key)
            if result is not None:
                return result
    return None

def get_info(xml):
    info = xml['NFe']['infNFe']
    return info

def find_id(xml):
    id = find_key(xml, '@Id')
    return id

def find_emisaora(xml):
    dados_emisor= find_key(xml, 'emit')
    return dados_emisor

def find__destinatario(xml):
    dados_destinatario = find_key(xml, 'dest')
    return dados_destinatario

def obtener_claves(diccionario, claves = []):
    
    for clave, valor in diccionario.items():
        #print(clave)
        claves.append(clave)
        if isinstance(valor, dict):
            claves.append(obtener_claves(valor))
    return claves

arquivos = os.listdir('nfs')
xml_dict = [get_xml(arquivo) for arquivo in arquivos]    
print(find_key(xml_dict[1], 'emit'))
#print(find_key(xml_dict[1], 'NFe'))
print(json.dumps(xml_dict[1], indent=4))

# # RANDOM DICTIONARY

# MY_DICT = {
#     'name': 'John',
#     'age': 25,
#     'address': {
#         'street': 'Main Street',
#         'number': 100,
#         'city': 'Any City'
#     }
# }

# for key, value in MY_DICT.items():
#     if isinstance(value, dict):
#         for k, v in value.items():
#             print(k)
#     else:
#         print(key)