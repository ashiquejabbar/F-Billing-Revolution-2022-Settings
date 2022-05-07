import tkinter as tk

def start_gui():
    main_window = MainWindow()
    main_window.set_grid(20,4)
    main_window.root.mainloop()

class MainWindow:
    def __init__(self, root = tk.Tk()):
        self.root = root
        self.root.title('Some Table')
        root.columnconfigure( 0, weight=1 ) # Stretch Column 0 to fit width.
        root.rowconfigure( 0, weight=1 ) # Stretch row 0 to fit height.

        self.canvas = tk.Canvas(root)
        self.canvas.grid(row = 0, column = 0, sticky = 'nsew')
        # Make canvas fit the whole of root. Useful to play with sizes.

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window( 0, 0, window = self.frame, anchor=tk.NW )
        # Makes frame an object in canvas

        self.vbar = tk.Scrollbar(root, orient = 'vertical', command= self.canvas.yview)
        # The scrollbar is a child of root.
        self.vbar.grid(row = 0, column = 1, sticky = 'ns')

        self.canvas.config(yscrollcommand = self.vbar.set)

        self.frame.bind('<Configure>', self.on_config) 
        # Bind on_config to a Frame config event.

    def on_config( self, e ):
        # print(e.widget, e)
        # Set the canvas scrollregion to fit the whole of frame.
        self.canvas.configure(scrollregion=(0, 0, e.width, e.height))

    def set_grid(self, rows, columns):
        for i in range(rows):
            for j in range(columns):
                tk.Label(self.frame, text = str(i)+' : '+str(j), width = 20).grid(row = i, column = j)

if __name__ == '__main__':
    start_gui()