import jarvis
#from word2number import  w2n

def extract_numbers_from_text(query):
    l=[]
    for t in query.split(' '):
        try:
             l.append[int(t)]
        except ValueError:
            pass
    return(l)


'''operations = {"thank": thank, "hello": hello,"hi": hello,"hey": hello, "plus": add, "ADD": add, "addition": add, "SUM": add, "MINUS": sub, "SUBTRACTION": sub, "SUBTRACT": sub,
              "DIFFERENCE": sub, "PRODUCT": multiply, "MULTIPLICATION": multiply, "MULTIPLY": multiply}
commands = {"AGE": age, "NAME": myname, "END": end, "EXIT": end, "CLOSE": end, "HI": hi, "HOW": how}
'''