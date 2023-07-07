
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """ 

 -  serviscan dc id sorgu değisik yazilim  -


""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" id : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n  tokenin bi kismi : {encodedStr}')
os.system('pause >nul') 
