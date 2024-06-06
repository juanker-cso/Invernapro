import mysql.connector as mbd
from icecream import ic

dict_vistas = {0:"ver_variedades",1:"nombres",2:"metodos",3:"ver_lotes",4:"cultivo_plantas"}

dict_tablas = {0:"variedades",1:"nombres",2:"metodos",3:"lotes",4:"plantas"}

dict_primaria_vistas = {0:{'a':"id",   'b':"ID"},
                 1:{'a':"nombre",'b':"Nombre"},
                 2:{'a':"id",   'b':"ID"},
                 3:{'a':"`# de lote`", 'b':"Número"},
                 4:{'a':"contLote", 'b':"Lote"}}

dict_primaria = {0:{'a':"id",   'b':"ID"},
                 1:{'a':"nombre",'b':"Nombre"},
                 2:{'a':"id",   'b':"ID"},
                 3:{'a':"cont", 'b':"Número"},
                 4:{'a':"contLote", 'b':"Lote"}}

dict_luces = {0:{'a':"D",'b':"Directa"},
              1:{'a':"A",'b':"Alta"},
              2:{'a':"M",'b':"Media"},
              3:{'a':"B",'b':"Baja"}}

def agregar_datos(db,csv,tabla):
    command = "INSERT INTO {} VALUES ({})"
    cur = db.cursor()
    try:
        cur.execute(command.format(tabla,csv))
    except mbd.Error as err:
        return  str(err.msg)        
    db.commit()
    return "E"

def remove_vocales(cadena):
    """quita vocales y espacios de una cadena"""
    aeiou = {"a","e","i","o","u"," ","A","E","I","O","U",",","."}
    ncadena = ""
    for l in cadena:
        if not (l in aeiou):
            ncadena += l
    return ncadena

def fill_cadena_suffix(cadena:str,n:int,c:str):
    """Rellenar una cadena hasta n caracteres con caracter c"""
    if len(cadena) < n:
        for i in range(len(cadena),n):
            cadena += c
    return cadena

def fill_cadena_prefix(cadena:str,n:int,c:str):
    """Rellena una cadena por en frente con caracter c hasta n"""
    if len(cadena) < n:
        for i in range(len(cadena),n):
            cadena = c + cadena
    return cadena

def get_llave(dictionary:dict,valor:str) -> int:
    """Devuelve el indice de diccionario a partir de un valor
    para llave primaria y luces"""
    for llave, val in dictionary.items():
        if val['a'] == valor:
            return int(llave)
    
def check_id(database,tabla:str,llave:str,valor:str):
    """verifica la existencia de llave = valor en la tabla"""
    cursor = database.cursor()
    cursor.execute("SELECT count(*) FROM {} WHERE {}=%s;".format(tabla,llave),(valor,))
    r = cursor.fetchone()[0]
    if r == 0:
        return False
    return True
