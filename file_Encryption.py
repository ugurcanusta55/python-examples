encryption_library = {'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
                      'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
                      'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
                      'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
                      'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
                      't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'}
input_file = open('input_file.dat','r')
fb = input_file.read()
print(fb)
yfb = ''
for ch in fb:
    if not ch in encryption_library.keys():
        yfb += ch
    else:
        yfb += encryption_library[ch]
print(yfb)
output_file = open('output_file.dat','w')
output_file.write(yfb)
output_file.close()



