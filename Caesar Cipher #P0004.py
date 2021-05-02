# ----- ----- -----
alpha_list=[[i for i in "abcdefghijklmnopqrstuvwxyz"],[i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]]
sd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
bd={'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
sd1={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
bd1={0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

# ----- ----- -----
def encrypt(value,key):
    encrypt_s=""
    for i in value:
        if i in alpha_list[0]:
            v=(sd[i]+key)%26
            encrypt_s+=bd1[v]
        elif i in alpha_list[1]:
            v=(bd[i]+key)%26
            encrypt_s+=sd1[v]
        else: encrypt_s+=i
    return(encrypt_s)

# ----- ----- -----        
def decrypt(value):
    for i in range(1,26):
        print(i," | ",encrypt(value,i))
        v=input("Enter 1 If Decryprion Text Found: ")
        if v=="1":
            print("found")
            break
            
# ----- ----- -----           
# Example for decryption.        
decrypt("CSY AMPP WEC, “H”; LI AMPP WEC, “E”; CSY AMPP WEC, “Z”; LI AMPP WEC, “M”; CSY AMPP WEC, “W.” “HEZMW” MW XLI TEWWASVH XS XLI JMVWX HIKVII. [RSXI: NIJJIVWSR HEZMW AEW TVIWMHIRX SJ XLI GSRJIHIVEGC.”")

# ----- ----- -----
