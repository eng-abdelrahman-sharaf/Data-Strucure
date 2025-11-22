from bst import BST
from avl import AVL
from custom_canvas import Custom_Canvas
import tkinter as tk

if __name__ == "__main__":
    root1 = tk.Tk()
    root1.geometry(f"{int(1920/2)}x1080+0+0")
    root1.title("BST")

    root2 = tk.Tk()
    root2.geometry(f"{int(1920/2)}x1080+{int(1920/2)}+0")
    root2.title("AVL")


    canvas1 = Custom_Canvas(root1, width=1920/2, height=1080, bg='white')
    canvas1.pack(anchor=tk.CENTER)

    canvas2 = Custom_Canvas(root2, width=1920/2, height=1080, bg='white')
    canvas2.pack(anchor=tk.CENTER)

    bst = BST()
    bst.visualize_insertions(range(18) , root1 , canvas1)

    avl = AVL()
    avl.visualize_insertions(range(18) , root2 , canvas2)


    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1) # to correct the blurry view in windows 
    finally:
        root1.mainloop()
        root2.mainloop()