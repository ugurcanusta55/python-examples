decryption_library = {'!':'A','@':'B','#':'C','$':'D','%':'E','^':'F','&':'G','*':'H','(':'I',
                      ')':'J','-':'K','_':'L','+':'M','=':'N','`':'O','~':'P','{':'Q','[':'R',
                      '}':'S',']':'T',':':'U',';':'V','"':'W','<':'X','>':'Y','0':'Z','1':'a',
                      '2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','a':'j',
                      'b':'k','c':'l','d':'m','e':'n','f':'o','g':'p','h':'q','i':'r','j':'s',
                      'k':'t','l':'u','m':'v','n':'w','o':'x','p':'y','q':'z'}
output_file = open('output_file.dat','r')
#import file_Encryption
#decryption_library = {v: k for k, v in file_Encryption.encryption_library.items()}
fb = output_file.read()
print(fb)
ybf =''

for ch in fb:
    if ch in decryption_library.keys():
        ybf += decryption_library[ch]
    else:
        ybf += ch
print(ybf)
son_dosya = open('son_hali.dat','w')
son_dosya.write(ybf)
son_dosya.close()
