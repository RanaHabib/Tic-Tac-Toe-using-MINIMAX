import tkinter as tk
window =tk.Tk()
window.configure(bg = "#FFFFFF")
window.title('Tic Tac Toe')

board =[[0,0,0],
       [0,0,0],
       [0,0,0]]

#Function to define a button
def button(parentWindow):          
    b = tk.Button(
    parentWindow,
    activebackground = "#FF4444",
    bg = "#F1F1F1",
    width = 20,
    height = 10,
    bd = 0)
    return b

def grid():
    for i in range(3):
        for j in range(3):
            board[i][j] = button(window)
            board[i][j].grid(row=i,column=j,padx=5, pady=5, )
            

grid()
window.mainloop()