#Make Error log output
#Improve Theme changer
#Save settings (Themes) after restart
#Have history of inputs
#Add Paste button to compare hash inputfield
#Better support for large files (slow currently)
#Make strings automatically update when typing
#Make outputs available in Uppercase letters

##Added loading bar when hashing files with cancel button
##Added comments to code
##Changed copy button from icon to say "Copy"
##Added main() function
##Added Ability to change theme
##Reworded about page
##"Hash Succeeded" popup will stay on top of main window until you close it
##Added an icon to "Hash succeeded" popup
##Added Menubar with button to open Github page, About and settings
##Added filesize check for big files when hashing
##Added filesize field in output to txt with the size of the file in MB
##Added autoclear when submitting as file. Because the old hash would stay when hashing new file, which could be confusing.
##Removed unnecessary clutter in code


import PySimpleGUI as sg
import hashlib
from os import stat
import os
from pyperclip import copy, paste
from webbrowser import open as openwebpage


def main():


    #Create a menubar
    menuBar = [["File", ["Theme", ["Theme Names", "Change Theme"]]],
                    ["Help", ["About", "Github"]]]
    

    #Create Layout of application
    layout = [
        [sg.Menu(menuBar)],
        [sg.Text("Check and Compare Hashes\n", font=(18))],
        [sg.Text("Original String/File", size=(13, 1)), sg.InputText(key="InputText"), sg.FileBrowse("Browse")],
        [sg.Text("Loading Bar Files", size=(13, 1)), sg.ProgressBar(6, orientation='h', size=(29, 20), key='progressbar', bar_color=("green", "white")), sg.Button("Cancel")],
        [sg.Text("\n")],
        [sg.Text("Compare Hash", size=(13, 1)), sg.InputText(key="CheckHash")],
        [sg.Text("\n")],
        [sg.Text("MD5", size=(13, 1)), sg.InputText(key="MD5"), sg.Button("Copy", key=("md5Copy"))],
        [sg.Text("SHA1", size=(13, 1)), sg.InputText(key="SHA1"), sg.Button("Copy", key=("sha1Copy"))], 
        [sg.Text("SHA256", size=(13, 1)), sg.InputText(key="SHA256"), sg.Button("Copy", key=("sha256Copy"))],
        [sg.Text("SHA384", size=(13, 1)), sg.InputText(key="SHA384"), sg.Button("Copy", key=("sha384Copy"))], 
        [sg.Text("SHA512", size=(13, 1)), sg.InputText(key="SHA512"), sg.Button("Copy", key=("sha512Copy"))],
        [sg.Text("\n")],
        [sg.Submit("Submit as String"), sg.Submit("Submit as File"), sg.Button("Compare Hash"), sg.Button("Output to txt"), sg.Button("Clear")]
    ] 

    
    #Create Window
    window = sg.Window("PyHash", layout, icon="D:\Documents\Python Scripts\PyHash\icon.ico")
    progress_bar = window['progressbar']
           

    #Check size of file and return the size in MB
    def checkSize(File):
        try:
            fileInBytes = stat(File).st_size
            return fileInBytes / 1_048_576
        except FileNotFoundError:
            pass


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
                chunk = file.read(1024)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()

    def fileSHA1(File_to_Hash):
        h = hashlib.sha1()
        with open(File_to_Hash, 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()

    def fileSHA256(File_to_Hash):
        h = hashlib.sha256()
        with open(File_to_Hash, 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()

    def fileSHA384(File_to_Hash):
        h = hashlib.sha384()
        with open(File_to_Hash, 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()

    def fileSHA512(File_to_Hash):
        h = hashlib.sha512()
        with open(File_to_Hash, 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()


    #Starts progress bar and hashes files
    def submitAsFile():
        for i in range(6):
            event, values = window.read(timeout=10)
            progress_bar.UpdateBar(i+1)
            if event == 'Cancel'  or event == sg.WIN_CLOSED:
                break
            elif i == 0:
                window["MD5"].update(fileMD5(values["InputText"]))
            elif i == 1:
                window["SHA1"].update(fileSHA1(values["InputText"]))
            elif i == 2:
                window["SHA256"].update(fileSHA256(values["InputText"]))
            elif i == 3:
                window["SHA384"].update(fileSHA384(values["InputText"]))
            elif i == 4:
                window["SHA512"].update(fileSHA512(values["InputText"]))


    #Clears all of the fields
    def clearFields():
        window.FindElement("InputText").update("")
        progress_bar.UpdateBar(0)
        window.FindElement("CheckHash").update("")
        window.FindElement("MD5").update("")
        window.FindElement("SHA1").update("")
        window.FindElement("SHA256").update("")
        window.FindElement("SHA384").update("")
        window.FindElement("SHA512").update("")


    #Event loop
    while True:

        event, values = window.read()


        if event == sg.WINDOW_CLOSED or event == "Exit":
            break


        #Copy text from specified fields to clipboard
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


        #Submits the text in "Submit as String" and checks if it exits. If it extist, hash it and return results in the corresponding text box
        if event == "Submit as String":
            progress_bar.UpdateBar(0)
            window["MD5"].update(md5(values["InputText"]))
            window["SHA1"].update(sha1(values["InputText"]))
            window["SHA256"].update(sha256(values["InputText"]))
            window["SHA384"].update(sha384(values["InputText"]))
            window["SHA512"].update(sha512(values["InputText"]))


        #Submits a file for hashing. It checks if the file is larger than 40 MB. If it is show a warning which tells the user that the hashing may take some time.
        if event == "Submit as File":
            try:
                progress_bar.UpdateBar(0)
                window.FindElement("MD5").update("")
                window.FindElement("SHA1").update("")
                window.FindElement("SHA256").update("")
                window.FindElement("SHA384").update("")
                window.FindElement("SHA512").update("")             
                try:
                    submitAsFile()
                except Exception:
                    sg.popup_timed("ERROR!\nYou exited the hashing process before it was finished\nRESTARTING...", auto_close_duration=3, title="Error", background_color="Red", font=(18), modal=True, icon="D:\Documents\Python Scripts\PyHash\error.ico")
                    window.close()
                    main()

            except Exception:
                sg.popup("ERROR!\nYou didn't select a valid file or filepath", title="Error", background_color="Red", font=(18), modal=True, icon="D:\Documents\Python Scripts\PyHash\error.ico")


        #Outputs the results in a txt file in the folder where this application is located
        if event == "Output to txt":
            if os.path.exists("HashExport.txt"):
                os.remove("HashExport.txt")

            file = open("HashExport.txt", "w")
            if checkSize(values["InputText"]) == None:
                file.write("Original String/File: " + values["InputText"] + "\n\n" +
                "Compare Hash: " + values["CheckHash"] + "\n\n" +

                "MD5:    " + values["MD5"] + "\n" + 
                "SHA1:   " + values["SHA1"] + "\n" + 
                "SHA256: " + values["SHA256"] + "\n" + 
                "SHA384: " + values["SHA384"] + "\n" + 
                "SHA512: " + values["SHA512"])
            else:
                file.write("Original String/File: " + values["InputText"] + "\n\n" +
                "File Size: " + str(round(checkSize(values["InputText"]), 3)) + " MB" + "\n"
                "Compare Hash: " + values["CheckHash"] + "\n\n" +
                "MD5:    " + values["MD5"] + "\n" + 
                "SHA1:   " + values["SHA1"] + "\n" + 
                "SHA256: " + values["SHA256"] + "\n" + 
                "SHA384: " + values["SHA384"] + "\n" + 
                "SHA512: " + values["SHA512"])
            file.close()


        #Compares a hash with the outputs.
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


        #Clears/resets every field
        if event == "Clear":
            clearFields()


        #Change theme. You input the name of the theme and it restarts the window with the new theme
        if event == "Change Theme":
            changeTheme = sg.popup_get_text("The names of themes are in \"File\"->\"Theme Names\"\nPlease input the name of theme (NOT case-sensitive): ", title="Theme", icon="D:\Documents\Python Scripts\PyHash\icon.ico")
            themes = [i.lower() for i in sg.theme_list()]
            try:
                if changeTheme.lower() in themes:
                    window.Close()
                    sg.theme(changeTheme)
                    main()
                else:
                    sg.popup("ERROR\nIncorrect spelling or unavailable theme")
            except AttributeError:
                window.close()
                main()


        #Opens a webpage with the themenames
        if event == "Theme Names":
            openwebpage("https://raw.githubusercontent.com/MatAMel/PyHash/master/themes.jpg")


        #Opens this applications github page
        if event == "Github":
            openwebpage("https://github.com/MatAMel/PyHash")


        #Shows information about this application
        if event == "About":
            sg.popup("PyHash\n"
            "PyHash is a python program to cryptographically hash text and files\n\n"
            "Supported Hash Functions\n"
            "MD5\nSHA1\nSHA256\nSHA384\nSHA512\n\n"
            "Browse\n"
            "The \"Browse\" button opens a file explorer window. When clicking on \"Browse\" please be aware that both the file and filepath can be hashed. This is why there are 2 buttons for hashing.\n\n"
            "Submit as String and Submit as File\n"
            "\"Submit as String\" means that whatever is typed into the input-field is taken literally, even filepaths. Therefore, when you've choosen a file with \"Browse\", please press \"Submit as File\" unless you want the filepath itself to be hashed of course.\n\n"
            "Big Files\n"
            "Big files may take som time to hash. There is a loading bar on files >50MB.\n\n"
            "Output to txt\n"
            "The button \"Output to txt\" outputs the results of the hash in a text file called \"HashExport.txt\" in the folder where this program is located.\n\n"
            "Compare Hash\n"
            "\"Compare Hash\" is a feature to compare any hash with the outputs of your string/file. This is usefull for checking the integrity of files for example.\n\n"
            "Copy Hash Results\n"
            "On the right of the hash output fields there are copy buttons. These copy whatever is in it's respective field to your clipboard with 1 press.\n\n"
            , title="PyHash", modal=False, icon="D:\Documents\Python Scripts\PyHash\icon.ico")


    window.close()


if __name__ == "__main__":
    main()
