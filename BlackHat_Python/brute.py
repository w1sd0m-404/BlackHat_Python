import pyzipper
import sys
from time import sleep
from tqdm import tqdm

banner="""                                                                                                                                                              
                                                               bbbbbbbb                                                                                       
WWWWWWWW                           WWWWWWWWiiii                b::::::b                                                      tttt                             
W::::::W                           W::::::i::::i               b::::::b                                                   ttt:::t                             
W::::::W                           W::::::Wiiii                b::::::b                                                   t:::::t                             
W::::::W                           W::::::W                     b:::::b                                                   t:::::t                             
 W:::::W           WWWWW           W:::::iiiiiiizzzzzzzzzzzzzzzzb:::::bbbbbbbbb   rrrrr   rrrrrrrrr  uuuuuu    uuuuuttttttt:::::ttttttt       eeeeeeeeeeee    
  W:::::W         W:::::W         W:::::Wi:::::iz:::::::::::::::b::::::::::::::bb r::::rrr:::::::::r u::::u    u::::t:::::::::::::::::t     ee::::::::::::ee  
   W:::::W       W:::::::W       W:::::W  i::::iz::::::::::::::zb::::::::::::::::br:::::::::::::::::ru::::u    u::::t:::::::::::::::::t    e::::::eeeee:::::ee
    W:::::W     W:::::::::W     W:::::W   i::::izzzzzzzz::::::z b:::::bbbbb:::::::rr::::::rrrrr::::::u::::u    u::::tttttt:::::::tttttt   e::::::e     e:::::e
     W:::::W   W:::::W:::::W   W:::::W    i::::i      z::::::z  b:::::b    b::::::br:::::r     r:::::u::::u    u::::u     t:::::t         e:::::::eeeee::::::e
      W:::::W W:::::W W:::::W W:::::W     i::::i     z::::::z   b:::::b     b:::::br:::::r     rrrrrru::::u    u::::u     t:::::t         e:::::::::::::::::e 
       W:::::W:::::W   W:::::W:::::W      i::::i    z::::::z    b:::::b     b:::::br:::::r           u::::u    u::::u     t:::::t         e::::::eeeeeeeeeee  
        W:::::::::W     W:::::::::W       i::::i   z::::::z     b:::::b     b:::::br:::::r           u:::::uuuu:::::u     t:::::t    ttttte:::::::e           
         W:::::::W       W:::::::W       i::::::i z::::::zzzzzzzb:::::bbbbbb::::::br:::::r           u:::::::::::::::uu   t::::::tttt:::::e::::::::e          
          W:::::W         W:::::W        i::::::iz::::::::::::::b::::::::::::::::b r:::::r            u:::::::::::::::u   tt::::::::::::::te::::::::eeeeeeee  
           W:::W           W:::W         i::::::z:::::::::::::::b:::::::::::::::b  r:::::r             uu::::::::uu:::u     tt:::::::::::tt ee:::::::::::::e  
            WWW             WWW          iiiiiiizzzzzzzzzzzzzzzzbbbbbbbbbbbbbbbb   rrrrrrr               uuuuuuuu  uuuu       ttttttttttt     eeeeeeeeeeeeee  
                                                                                                                                                              
 
                                                                                                                                                              """

def zipbruter():

    print(banner.center(150,'-'))
    print("\n")
    print("Hello, welcome to 'Wizbrute' tool.".center(150,'-'))
    print("\n")
    print("This tool helps you to crack encrypted zip files".center(150,'-'))
    print("\n")

    #file = input(str("Enter your ZIP file: "))
    #wordlist= input(str("Enter your passwords file: "))
    file="secret.zip"
    wordlist="wordlist.txt"

    #if file[4:] == ".zip" and wordlist[4:] == ".txt":
    print("SALDIRI BAŞLATILIYOR")
    print("Lütfen bekleyiniz.")
    sleep(2)
    fileObject=pyzipper.AESZipFile(file)

    count = len(list(open(wordlist,"rb")))
    print("Total passwords to try: ", count)
    with open(wordlist, "rb") as wordlist:

        for word in tqdm(wordlist, total=count, unit="word"):
            try:
                fileObject.pwd=word.strip()
                fileObject.extractall()
            except:
                print("Trying password ", word.decode().strip())
                continue
            else:
                print("<-- PASSWORD FOUND --> ".center(20,' '))
                print("\n")
                print(word.decode().strip())
                sys.exit(0)
    print("No password match!")
    #else:
    print("Hatalı dosya/dosyalar girdiniz.")
    print("ÇIKIŞ YAPILIYOR...")
    sleep(1)
    sys.exit(1)

zipbruter()