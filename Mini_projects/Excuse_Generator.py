from random import choice
import PySimpleGUI as sg

def updateText():
    return f'{dictr["excuse"]}{choice(dictr["intro"])}{choice(dictr["scapegoat"])}{choice(dictr["delay"])}'

dictr = {
    "welcome": "Hello stranger and welcome to your random excuse generator                                ",

    "intro": ["Sorry I can't come ", "Please forgive my absence ", "This is going to sound crazy but ", "Get this : " , "I can't go because ", 
    "I know you're going to hate me but ", "I was minding my own business and boom! ", "I feel terrible but ","I regretfully cannot attend ",
     "This is going to sound like and excuse but ","I wanted to come so badly but ","This has never happened to me before but "],

    "scapegoat": ["my nephew ","the ghost of Hitler ","the Pope ","my ex ","a high school marching band ","Dan Rather ","Putin ","a sad clown ",
    "the kid from Air Bud ","a professional cricket team ","my Tinder date ","My mother ","Obama ","some homeless guy ","chinese exchange student ",
    "my parrot ","Selena Gomez ","japanese prime minister ","Olenna Tyrell ", "my dog ","my cat ","my goldfish ","my hamster ","my pet turtle ","my pet snake ",
    "Joe Biden "],

    "delay": ["just shit the bed","died in front of me ","won't stop telling me knock knock jokes","is having a nervous breakdown","gave me syphilis",
    "poured lemonade in my gas tank","stabbed me","found my box of human teeth","stole my bicycle","posted my nudes on Instagram","broke my hand",
    "burned down my house","fired me from my job","tried to assasinate me","got stuck in a washing mashine","scratched my car","burned down my house","stole my edibles",
    "knocked out my grandma","just drank all my beers",                                                                                                                       ],

    "excuse": "Your excuse is: "
}

sg.theme('DarkAmber')  

#[sg.Text(updateText(), key='-ex-')],

layout = [  
    [sg.Text(dictr["welcome"])],
    [sg.Multiline(size=(60,5), disabled=True, autoscroll=False, key='-ex-')],
    [sg.Button('Refresh', key='-xx-')],
    [sg.Button('Bye Boss', key='-out-')]
]

window = sg.Window('Excuse Generator', layout, margins=(100, 40))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '-out-': 
        break
    if event == '-xx-':
        window['-ex-'].Update(updateText())
    

window.close()