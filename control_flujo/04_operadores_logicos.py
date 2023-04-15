# and, or y not
# and devuelve True siempre y cuando todas condiciones sean true
# or devuelve True siempre y cuando una sola de las condiciones sea True
# not devuelve la contraparte de la condiciones, si es True devuelve un False

gas = False
encendido = True
edad = 18

if not gas and (encendido or edad > 18):
    print("Puedes avanzar")
