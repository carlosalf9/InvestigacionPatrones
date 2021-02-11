def Factory(language ="English"):

"""Factory Method"""
localizers = { 
    "French": FrenchLocalizer, 
    "English": EnglishLocalizer, 
    "Spanish": SpanishLocalizer, 
} 

return localizers[language]() 
if name == "main":

f = Factory("French") 
e = Factory("English") 
s = Factory("Spanish") 

message = ["car", "bike", "cycle"] 

for msg in message: 
    print(f.localize(msg)) 
    print(e.localize(msg)) 
    print(s.localize(msg)) 