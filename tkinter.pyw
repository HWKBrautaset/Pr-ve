import tkinter as tk
import datetime
root = tk.Tk()
dagen_i_dag = datetime.datetime.now()
knapp = tk.Button(root, text = dagen_i_dag, command = dagen_i_dag)
knapp.pack()


root.mainloop()
