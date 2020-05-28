# Hello World GUI application
# python gui_hello_world.py

import tkinter

def hello_world():
    '''
    Add to the window a labal with an Hello World message

    Arguments:
        None
    
    Returns:
        None
    '''
    tkinter.Label(window, text = 'Hello World!').pack()


if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry('256x128')
    window.resizable(0, 0)
    window.title('Hello World!')
    button_widget = tkinter.Button(window, text = 'Say Hello', command = hello_world)
    button_widget.pack()
    tkinter.mainloop()