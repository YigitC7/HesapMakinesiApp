import customtkinter as ctk

class MainWindow:
    def __init__(self,Window):
        self.Window = Window
        self.Window.minsize(320,400)
        self.Window.maxsize(700,400)
        self.Window.geometry('700x400')
        self.Window.title("Hesap Makinesi")

        self.Panel()
        self.Buttons()

    def Panel(self):
        class panel():
                def __init__(self,
                    height=0,
                    width=0,
                    pack_padY=3,
                    font=(),
                    color=""
                    ):
                    self.height = height
                    self.width = width
                    self.pack_padY = pack_padY
                    self.font = font
                    self.color = color

        _main_panel_ = panel(
            height = 90,
            width = 800,
            font = ("italic",60),
            color = "#F0F8FF"
        )
        self.main_panel = ctk.CTkTextbox(self.Window,
            height=_main_panel_.height,
            width=_main_panel_.width,
            font=_main_panel_.font,
            fg_color=_main_panel_.color,
            wrap="none")
        self.main_panel.pack(pady=_main_panel_.pack_padY)


    def Buttons(self):
        def Buton_bir_fonk():
            self.main_panel.insert("end","1")

        def Buton_iki_fonk():
            self.main_panel.insert("end","2")

        def Buton_uc_fonk():
            self.main_panel.insert("end","3")

        def Buton_dort_fonk():
            self.main_panel.insert("end","4")

        def Buton_bes_fonk():
            self.main_panel.insert("end","5")

        def Buton_alti_fonk():
            self.main_panel.insert("end","6")

        def Buton_yedi_fonk():
            self.main_panel.insert("end","7")

        def Buton_sekiz_fonk():
            self.main_panel.insert("end","8")

        def Buton_dokuz_fonk():
            self.main_panel.insert("end","9")

        def Buton_sifir_fonk():
            self.main_panel.insert("end","0")

        def Buton_esittir_fonk():
            main_panel_oldData = self.main_panel.get("0.0", ctk.END).strip()
    
            if main_panel_oldData:
                try:
                    result = eval(main_panel_oldData)
            
                    self.main_panel.delete("0.0", ctk.END)
                    self.main_panel.insert("0.0", str(result))
                except Exception as e:
                    self.main_panel.delete("0.0", ctk.END)
                    self.main_panel.delete("1.0", "end")
            else:
                self.main_panel.delete("1.0", "end")

        class button:
            def __init__(self,
                    text="",
                    width=100,
                    height=70,
                    place_x=1,
                    place_y=1,
                    font=("italic",40),
                    fg_color="",
                    text_color=""
                    ):
                self.text = text
                self.width = width
                self.height = height
                self.place_x = place_x
                self.place_y = place_y
                self.font = font
                self.fg_color = fg_color
                self.text_color = text_color

        _Buton_bir_ = button(
            text = "1",
            place_x = 5,
            place_y = 100
        )
        self.Buton_bir = ctk.CTkButton(self.Window,
            text=_Buton_bir_.text,
            font=_Buton_bir_.font,
            height=_Buton_bir_.height,
            width=_Buton_bir_.width,
            command=Buton_bir_fonk)
        self.Buton_bir.place(x=_Buton_bir_.place_x, y=_Buton_bir_.place_y)

        _Buton_iki_ = button(
            text = "2",
            place_x = 5+105,
            place_y = 100
        )
        self.Buton_iki = ctk.CTkButton(self.Window,
            text=_Buton_iki_.text,
            font=_Buton_iki_.font,
            height=_Buton_iki_.height,
            width=_Buton_iki_.width,
            command=Buton_iki_fonk)
        self.Buton_iki.place(x=_Buton_iki_.place_x, y=_Buton_iki_.place_y)

        _Buton_uc_ = button(
            text = "3",
            place_x = 110+105,
            place_y = 100
        )
        self.Buton_uc = ctk.CTkButton(self.Window,
            text=_Buton_uc_.text,
            font=_Buton_uc_.font,
            height=_Buton_uc_.height,
            width=_Buton_uc_.width,
            command=Buton_uc_fonk)
        self.Buton_uc.place(x=_Buton_uc_.place_x, y=_Buton_uc_.place_y)

        _Buton_dort_ = button(
            text = "4",
            place_x = 5,
            place_y = 100+75
        )
        self.Buton_dort = ctk.CTkButton(self.Window,
            text=_Buton_dort_.text,
            font=_Buton_dort_.font,
            height=_Buton_dort_.height,
            width=_Buton_dort_.width,
            command=Buton_dort_fonk)
        self.Buton_dort.place(x=_Buton_dort_.place_x, y=_Buton_dort_.place_y)

        _Buton_bes_ = button(
            text = "5",
            place_x = 5+105,
            place_y = 100+75
        )
        self.Buton_bes = ctk.CTkButton(self.Window,
            text=_Buton_bes_.text,
            font=_Buton_bes_.font,
            height=_Buton_bes_.height,
            width=_Buton_bes_.width,
            command=Buton_bes_fonk)
        self.Buton_bes.place(x=_Buton_bes_.place_x, y=_Buton_bes_.place_y)

        _Buton_alti_ = button(
            text = "6",
            place_x = 110+105,
            place_y = 100+75
        )
        self.Buton_alti = ctk.CTkButton(self.Window,
            text=_Buton_alti_.text,
            font=_Buton_alti_.font,
            height=_Buton_alti_.height,
            width=_Buton_alti_.width,
            command=Buton_alti_fonk)
        self.Buton_alti.place(x=_Buton_alti_.place_x, y=_Buton_alti_.place_y)

        _Buton_yedi_ = button(
            text = "7",
            place_x = 5,
            place_y = 175+75
        )
        self.Buton_yedi = ctk.CTkButton(self.Window,
            text=_Buton_yedi_.text,
            font=_Buton_yedi_.font,
            height=_Buton_yedi_.height,
            width=_Buton_yedi_.width,
            command=Buton_yedi_fonk)
        self.Buton_yedi.place(x=_Buton_yedi_.place_x, y=_Buton_yedi_.place_y)

        _Buton_sekiz_ = button(
            text = "8",
            place_x = 5+105,
            place_y = 175+75
        )
        self.Buton_sekiz = ctk.CTkButton(self.Window,
            text=_Buton_sekiz_.text,
            font=_Buton_sekiz_.font,
            height=_Buton_sekiz_.height,
            width=_Buton_sekiz_.width,
            command=Buton_sekiz_fonk)
        self.Buton_sekiz.place(x=_Buton_sekiz_.place_x, y=_Buton_sekiz_.place_y)

        _Buton_dokuz_ = button(
            text = "9",
            place_x = 110+105,
            place_y = 175+75
        )
        self.Buton_dokuz = ctk.CTkButton(self.Window,
            text=_Buton_dokuz_.text,
            font=_Buton_dokuz_.font,
            height=_Buton_dokuz_.height,
            width=_Buton_dokuz_.width,
            command=Buton_dokuz_fonk)
        self.Buton_dokuz.place(x=_Buton_dokuz_.place_x, y=_Buton_dokuz_.place_y)

        _Buton_nokta_ = button(
            text = ".",
            place_x = 5,
            place_y = 175+75+80,
            height = 60,
            width = 90
        )
        self.Buton_nokta = ctk.CTkButton(self.Window,
            text=_Buton_nokta_.text,
            font=_Buton_nokta_.font,
            height=_Buton_nokta_.height,
            width=_Buton_nokta_.width)
        self.Buton_nokta.place(x=_Buton_nokta_.place_x, y=_Buton_nokta_.place_y)

        _Buton_sifir_ = button(
            text = "0",
            place_x = 5+105,
            place_y = 175+75+80,
            height = 60
        )
        self.Buton_sifir = ctk.CTkButton(self.Window,
            text=_Buton_sifir_.text,
            font=_Buton_sifir_.font,
            height=_Buton_sifir_.height,
            width=_Buton_sifir_.width,
            command=Buton_sifir_fonk)
        self.Buton_sifir.place(x=_Buton_sifir_.place_x, y=_Buton_sifir_.place_y)

        _Buton_esittir_ = button(
            text = "=",
            place_x = 110+110+5,
            place_y = 175+75+80,
            height = 60,
            width = 90
        )
        self.Buton_esittir = ctk.CTkButton(self.Window,
            text=_Buton_esittir_.text,
            font=_Buton_esittir_.font,
            height=_Buton_esittir_.height,
            width=_Buton_esittir_.width,
            command=Buton_esittir_fonk)
        self.Buton_esittir.place(x=_Buton_esittir_.place_x, y=_Buton_esittir_.place_y)

if __name__ == "__main__":
    Window = ctk.CTk()
    app = MainWindow(Window)
    Window.mainloop()