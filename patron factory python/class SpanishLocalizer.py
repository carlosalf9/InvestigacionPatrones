def __init__(self): 

    self.translations = {"car": "coche", "bike": "bicicleta", 
                         "cycle":"ciclo"} 

def localize(self, msg): 

    """change the message using translations"""
    return self.translations.get(msg, msg) 