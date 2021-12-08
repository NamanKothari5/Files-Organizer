from tkinter import *  # for creating GUI Window
from tkinter import filedialog  # for displaying selection of files dialog
import os  # perform file operations
import shutil  # move files and make new folder


class GUI(Tk):  # GUI class inherited from class Tk
    def __init__(self):  # making the GUI window using constructer
        super().__init__()
        self.geometry("250x250")  # size of window

    def gettingPath(self):
        self.path = (
            filedialog.askdirectory()
        )  # file dialog will open for selecting the folder on which operation is to performed
        return self.path

    def startButton(self, path_value):
        self.button_Frame = Frame(self)
        self.button_Frame.pack()
        self.start_Button = Button(  # defining the button
            self.button_Frame,
            text="Start the process",
            bg="black",
            fg="white",
            activebackground="blue",
            command=lambda: self.startOperation(path_value),
        ).grid(row=0, column=0)

    def startOperation(self, path_value):
        count = 0  # initially count is zero as no files is scanned for grouping
        os.chdir(path_value)  # changing the directory to desired one
        self.file_list = (
            os.listdir()
        )  # listing all the files already present in the folder
        no_of_files = len(self.file_list)
        if len(self.file_list) == 0:  # if folder is empty
            self.error_label = Label(text="Erroe empty folder").pack()
            exit()
        for file in self.file_list:
            if file.endswith(".png"):  # checking for images
                self.dir_name = "ImageFiles"
                self.new_path = os.path.join(path_value, self.dir_name)
                self.file_list = os.listdir()
                if self.dir_name not in self.file_list:
                    os.mkdir(self.new_path)
                shutil.move(file, self.new_path)

            if file.endswith(".txt") or file.endswith(
                ".pdf"
            ):  # checking for text files
                self.dir_name = "TextFiles"
                self.new_path = os.path.join(path_value, self.dir_name)
                self.file_list = os.listdir()
                if self.dir_name not in self.file_list:
                    os.mkdir(self.new_path)
                shutil.move(file, self.new_path)

            if (
                file.endswith(".cpp")
                or file.endswith(".java")
                or file.endswith(".py")
                or file.endswith(".js")
                or file.endswith(".html")
                or file.endswith(".css")
                or file.endswith(".exe")
                # checking for programming files
            ):
                self.dir_name = "ProgrammingFiles"
                self.new_path = os.path.join(path_value, self.dir_name)
                self.file_list = os.listdir()
                if self.dir_name not in self.file_list:
                    os.mkdir(self.new_path)
                shutil.move(file, self.new_path)

            if file.endswith(".mp4"):
                self.dir_name = "VideoFiles"
                self.new_path = os.path.join(path_value, self.dir_name)
                self.file_list = os.listdir()
                if self.dir_name not in self.file_list:
                    os.mkdir(self.new_path)
                shutil.move(file, self.new_path)

            count = count + 1  # increment the counter if the file is grouped

        if count == no_of_files:
            success = Label(text="Operation Successful!").pack()  # process completed
        else:
            error = Label(text="Failed").pack()  # error


if __name__ == "__main__":
    object = GUI()
    path = object.gettingPath()
    object.startButton(path)
    object.mainloop()
