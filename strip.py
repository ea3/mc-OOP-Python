string1 = "    Esta cadena es para probar como funciona el metodo strip y tl metodo split    "
x = string1.strip().split()
for word in x:
    if word[0].lower() in 'aeiou':

        print(word[0] + " esta en " + word)
