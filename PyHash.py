#Make Error log output
#Add support for digest files
#Make loading bar when hashing files
#Only output file hash warning when file > 500MB

import PySimpleGUI as sg
import hashlib
from pyperclip import copy
from py_essentials import hashing as hs

layout = [  
    [sg.Text("Check and Compare Hashes\n", font=(18))],
    [sg.Text("Original String/File", size=(13, 1)), sg.InputText(key="InputText"), sg.FileBrowse("Browse")],
    [sg.Text("\n")],
    [sg.Text("Compare Hash", size=(13, 1)), sg.InputText(key="CheckHash")],
    [sg.Text("\n")],
    [sg.Text("MD5", size=(13, 1)), sg.InputText(key="MD5"), sg.Button(image_filename="D:\Documents\Python Scripts\PyHash\copy.png", key=("md5Copy"), image_size=(20,20), image_subsample=(15))],
    [sg.Text("SHA1", size=(13, 1)), sg.InputText(key="SHA1"), sg.Button(image_filename="D:\Documents\Python Scripts\PyHash\copy.png", key=("sha1Copy"), image_size=(20,20), image_subsample=(15))], 
    [sg.Text("SHA256", size=(13, 1)), sg.InputText(key="SHA256"), sg.Button(image_filename="D:\Documents\Python Scripts\PyHash\copy.png", key=("sha256Copy"), image_size=(20,20), image_subsample=(15))],
    [sg.Text("SHA384", size=(13, 1)), sg.InputText(key="SHA384"), sg.Button(image_filename="D:\Documents\Python Scripts\PyHash\copy.png", key=("sha384Copy"), image_size=(20,20), image_subsample=(15))], 
    [sg.Text("SHA512", size=(13, 1)), sg.InputText(key="SHA512"), sg.Button(image_filename="D:\Documents\Python Scripts\PyHash\copy.png", key=("sha512Copy"), image_size=(20,20), image_subsample=(15))],
    [sg.Text("\n")],
    [sg.Submit("Submit as String"), sg.Submit("Submit as File"), sg.Button("Output to txt"), sg.Button("Compare Hash"), sg.Button("Clear"), sg.Button("Info")]
] 

window = sg.Window("PyHash", layout, icon="D:\Documents\Python Scripts\PyHash\icon.ico")

#Hash Text
def md5(md5_hash):
    return hashlib.md5(md5_hash.encode()).hexdigest()

def sha1(sha1_hash):
    return hashlib.sha1(sha1_hash.encode()).hexdigest() 

def sha256(sha256_hash):
    return hashlib.sha256(sha256_hash.encode()).hexdigest()

def sha384(sha384_hash):
    return hashlib.sha384(sha384_hash.encode()).hexdigest()

def sha512(sha512_hash):
    return hashlib.sha512(sha512_hash.encode()).hexdigest()


#Hash Files
def fileMD5(File_to_Hash):
    h = hashlib.md5()
    with open(File_to_Hash, 'rb') as file:
        while True:
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def fileSHA1(File_to_Hash):
    h = hashlib.sha1()
    with open(File_to_Hash, 'rb') as file:
        while True:
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def fileSHA256(File_to_Hash):
    h = hashlib.sha256()
    with open(File_to_Hash, 'rb') as file:
        while True:
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def fileSHA384(File_to_Hash):
    h = hashlib.sha384()
    with open(File_to_Hash, 'rb') as file:
        while True:
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def fileSHA512(File_to_Hash):
    h = hashlib.sha512()
    with open(File_to_Hash, 'rb') as file:
        while True:
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()



while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "md5Copy":
        copy(values["MD5"])
    elif event == "sha1Copy":
        copy(values["SHA1"])
    elif event == "sha256Copy":
        copy(values["SHA256"])
    elif event == "sha384Copy":
        copy(values["SHA384"])
    elif event == "sha512Copy":
        copy(values["SHA512"])

    if event == "Submit as String":
        if values["InputText"] == "":
            sg.popup("ERROR!\nYou didn't fill out the original string field", title="Error", background_color="Red", font=(18), modal=True, icon="D:\Documents\Python Scripts\PyHash\error.ico")
        else:
            window["MD5"].update(md5(values["InputText"]))
            window["SHA1"].update(sha1(values["InputText"]))
            window["SHA256"].update(sha256(values["InputText"]))
            window["SHA384"].update(sha384(values["InputText"]))
            window["SHA512"].update(sha512(values["InputText"]))

    if event == "Submit as File":
        fileWarning = sg.popup_ok_cancel("Warning!\nBe aware that this can take a few seconds.\n"
        "Big files may make the program unresponsive. This is normal. "
        "Please do not exit the window until it's done.", title="Warning", icon="D:\Documents\Python Scripts\PyHash\error.ico")
        if fileWarning == "OK":                  
            try:
                window["MD5"].update(fileMD5(values["InputText"]))
                window["SHA1"].update(fileSHA1(values["InputText"]))
                window["SHA256"].update(fileSHA256(values["InputText"]))
                window["SHA384"].update(fileSHA384(values["InputText"]))
                window["SHA512"].update(fileSHA512(values["InputText"]))
                sg.popup("Hash succeeded!", title="Success", modal=True)
            except FileNotFoundError:
                sg.popup("ERROR!\nYou didn't select a valid file or filepath", title="Error", background_color="Red", font=(18), modal=True, icon="D:\Documents\Python Scripts\PyHash\error.ico")

    if event == "Output to txt":
        if values["InputText"] == "":
            sg.popup("ERROR!\nYou didn't fill out the original string field", title="Error", background_color="Red", font=(18), modal=True, icon="D:\Documents\Python Scripts\PyHash\error.ico")
        else:
            file = open("HashExport.txt", "w")
            file.write("Original String: " + values["InputText"] + "\n\n" +
            "Compare Hash: " + values["CheckHash"] + "\n\n" +
            "MD5:    " + values["MD5"] + "\n" + 
            "SHA1:   " + values["SHA1"] + "\n" + 
            "SHA256: " + values["SHA256"] + "\n" + 
            "SHA384: " + values["SHA384"] + "\n" + 
            "SHA512: " + values["SHA512"])
            file.close()
    
    if event == "Compare Hash":
        if values["CheckHash"] == "":
            sg.popup("You didn't enter a hash. Please try again.", title="HashCheck", icon="D:\Documents\Python Scripts\PyHash\icon.ico")
        elif values["CheckHash"] == values["MD5"]:
            sg.popup("The hash corresponds to the MD5 output!", title="HashCheck", icon="D:\Documents\Python Scripts\PyHash\icon.ico")
        elif values["CheckHash"] == values["SHA1"]:
            sg.popup("The hash corresponds to the SHA1 output!", title="HashCheck", icon="D:\Documents\Python Scripts\PyHash\icon.ico")
        elif values["CheckHash"] == values["SHA256"]:
            sg.popup("The hash corresponds to the SHA256 output!", title="HashCheck", icon="D:\Documents\Python Scripts\PyHash\icon.ico")
        elif values["CheckHash"] == values["SHA384"]:
            sg.popup("The hash corresponds to the SHA384 output!", title="HashCheck", icon="D:\Documents\Python Scripts\PyHash\icon.ico")
        elif values["CheckHash"] == values["SHA512"]:
            sg.popup("The hash corresponds to the SHA512 output!", title="HashCheck", icon="D:\Documents\Python Scripts\PyHash\icon.ico")
        else:
            sg.popup("None of the hashes match. Please try again.", title="HashCheck", icon="D:\Documents\Python Scripts\PyHash\error.ico")
    
    if event == "Clear":
        window.FindElement("InputText").update("")
        window.FindElement("CheckHash").update("")
        window.FindElement("MD5").update("")
        window.FindElement("SHA1").update("")
        window.FindElement("SHA256").update("")
        window.FindElement("SHA384").update("")
        window.FindElement("SHA512").update("")

    if event == "Info":
        sg.popup("Welcome to PyHash!\nThis is a program developt in python to hash text and files.\n"
        "Here are some things to be aware of.\n\nPyHash supports these hash functions:\nMD5\nSHA1\nSHA256\nSHA384\nSHA512\n\n"
        "When clicking on \"Browse\" please be aware that both the file and filepath can be hashed.\n"
        "This is why there are 2 buttons for hashing.\n\"Submit as String\" means that whatever is typed into the inputfield is taken literally, even filepaths.\n"
        "Therefore, when you've choosen a file with \"Browse\", please press \"Submit as File\" unless you want the filepath itself to be hashed of course.\n\n"
        "Be aware that big files might cause the program to not respond when hashing. Please sit tight and wait instead of closing the window\n\n"
        "The button \"Output to txt\" outputs the results of the hash in a neat txt file in the folder this program is located.\n\n"
        "\"Compare Hash\" is a feature to compare any hash with the outputs of your string/file. This is usefull for checking the integrity of files for example.\n\n"
        "On the right of the hash output fields there are copy buttons. These copy whatever is in it's respective field to your clipboard with 1 press", title="PyHash", modal=False, icon="D:\Documents\Python Scripts\PyHash\icon.ico")

window.close()