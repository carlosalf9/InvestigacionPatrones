""" simplemente devuelve la versión francesa """

def __init__(self): 

    self.translations = {"car": "voiture", "bike": "bicyclette", 
                         "cycle":"cyclette"} 

def localize(self, message): 

    """cambia el mensaje usando traducciones"""
    return self.translations.get(msg, msg) 