from customtkinter import *

class Gui():
    def __init__(self) -> None:
        self.root = CTk()

        self.window()
        self.buttons()
        self.labels()

        self.root.mainloop()

    def window(self):
        set_appearance_mode("dark")
        set_default_color_theme("green")
        self.root.geometry("380x560")
        self.root.title("Calculator")
        self.root.iconbitmap()
        self.root.minsize(height=560, width=380)
        self.root.maxsize(height=560, width=380)


    def buttons(self):
        h = 55
        w = 85
        f = ("Courier", 18)
        f_color = "transparent"
        border_c = "white"
        border_w = 1
        x_pos = 20
        y_pos = 220
        hover_c = "grey"
        percentage = CTkButton(self.root,
                            text="%",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            hover_color=hover_c,
                            font=f,
                            )
        ce = CTkButton(self.root,
                            text="CE",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        c = CTkButton(self.root,
                            text="C",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        backspace = CTkButton(self.root,
                            text="BackSpace",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=("Courier", 12),
                            )
        invert = CTkButton(self.root,
                            text="1/x",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        square = CTkButton(self.root,
                            text="x^2",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        sq_root = CTkButton(self.root,
                            text="x^1/2",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        divide = CTkButton(self.root,
                            text="/",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        button7 = CTkButton(self.root,
                            text="7",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        button8 = CTkButton(self.root,
                            text="8",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        button9 = CTkButton(self.root,
                            text="9",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        multiply = CTkButton(self.root,
                            text="x",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        button4 = CTkButton(self.root,
                            text="4",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        button5 = CTkButton(self.root,
                            text="5",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        button6 = CTkButton(self.root,
                            text="6",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        minus = CTkButton(self.root,
                            text="-",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        button1 = CTkButton(self.root,
                            text="1",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        button2 = CTkButton(self.root,
                            text="2",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        button3 = CTkButton(self.root,
                            text="3",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        plus = CTkButton(self.root,
                            text="+",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        # MISSING +/-
        button0 = CTkButton(self.root,
                            text="0",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        point = CTkButton(self.root,
                            text=".",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        equal = CTkButton(self.root,
                            text="=",
                            width=w,
                            height=h,
                            fg_color=f_color,
                            border_color=border_c,
                            border_width=border_w,
                            font=f,
                            )
        
        percentage.place(x=x_pos+w*0, y=y_pos+h*0)
        ce.place(        x=x_pos+w*1, y=y_pos+h*0)
        c.place(         x=x_pos+w*2, y=y_pos+h*0)
        backspace.place( x=x_pos+w*3, y=y_pos+h*0)
        invert.place(    x=x_pos+w*0, y=y_pos+h*1)
        square.place(    x=x_pos+w*1, y=y_pos+h*1)
        sq_root.place(   x=x_pos+w*2, y=y_pos+h*1)
        divide.place(    x=x_pos+w*3, y=y_pos+h*1)
        button7.place(   x=x_pos+w*0, y=y_pos+h*2)
        button8.place(   x=x_pos+w*1, y=y_pos+h*2)
        button9.place(   x=x_pos+w*2, y=y_pos+h*2)
        multiply.place(  x=x_pos+w*3, y=y_pos+h*2)
        button4.place(   x=x_pos+w*0, y=y_pos+h*3)
        button5.place(   x=x_pos+w*1, y=y_pos+h*3)
        button6.place(   x=x_pos+w*2, y=y_pos+h*3)
        minus.place(     x=x_pos+w*3, y=y_pos+h*3)
        button1.place(   x=x_pos+w*0, y=y_pos+h*4)
        button2.place(   x=x_pos+w*1, y=y_pos+h*4)
        button3.place(   x=x_pos+w*2, y=y_pos+h*4)
        plus.place(      x=x_pos+w*3, y=y_pos+h*4)
        button0.place(   x=x_pos+w*1, y=y_pos+h*5)
        point.place(     x=x_pos+w*2, y=y_pos+h*5)
        equal.place(     x=x_pos+w*3, y=y_pos+h*5)

    def labels(self):
        top_label = CTkLabel(self.root, 
                            text="Calculator",
                            font=("Courier", 20),
                            )
        top_label.place(x=10)
        pass


if __name__ == "__main__":
    app = Gui()
