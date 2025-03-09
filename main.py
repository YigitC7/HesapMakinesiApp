import customtkinter as ctk
from functools import partial

class MainWindow:
    def __init__(self,Window):
        self.Window = Window
        self.Window.minsize(410,400)
        self.Window.maxsize(410,400)
        self.Window.geometry('410x400')
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
        def main_panel_add_fonk(deger):
            self.main_panel.insert("end",deger)

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
        
        def sil_fonk():
            main_panel_oldData = self.main_panel.get("0.0", ctk.END).strip()
            self.main_panel.delete("1.0","end")
            self.main_panel.insert("0.0",main_panel_oldData[slice(0,-1)])

        class button:
            def __init__(self,
                    text="",
                    width=100,
                    height=70,
                    place_x=1,
                    place_y=1,
                    font=("italic",40),
                    fg_color="",
                    text_color="",
                    hover_color="",
                    panel_read=""
                    ):
                self.text = text
                self.width = width
                self.height = height
                self.place_x = place_x
                self.place_y = place_y
                self.font = font
                self.fg_color = fg_color
                self.text_color = text_color
                self.hover_color = hover_color
                self.panel_read = panel_read

        _Buton_bir_ = button(
            text = "1",
            place_x = 5,
            place_y = 100,
            panel_read = "1"
        )
        self.Buton_bir = ctk.CTkButton(self.Window,
            text=_Buton_bir_.text,
            font=_Buton_bir_.font,
            height=_Buton_bir_.height,
            width=_Buton_bir_.width,
            command=partial(main_panel_add_fonk,_Buton_bir_.panel_read))
        self.Buton_bir.place(x=_Buton_bir_.place_x, y=_Buton_bir_.place_y)

        _Buton_iki_ = button(
            text = "2",
            place_x = 5+105,
            place_y = 100,
            panel_read = "2"
        )
        self.Buton_iki = ctk.CTkButton(self.Window,
            text=_Buton_iki_.text,
            font=_Buton_iki_.font,
            height=_Buton_iki_.height,
            width=_Buton_iki_.width,
            command=partial(main_panel_add_fonk,_Buton_iki_.panel_read))
        self.Buton_iki.place(x=_Buton_iki_.place_x, y=_Buton_iki_.place_y)

        _Buton_uc_ = button(
            text = "3",
            place_x = 110+105,
            place_y = 100,
            panel_read = "3"
        )
        self.Buton_uc = ctk.CTkButton(self.Window,
            text=_Buton_uc_.text,
            font=_Buton_uc_.font,
            height=_Buton_uc_.height,
            width=_Buton_uc_.width,
            command=partial(main_panel_add_fonk,_Buton_uc_.panel_read))
        self.Buton_uc.place(x=_Buton_uc_.place_x, y=_Buton_uc_.place_y)

        _Buton_dort_ = button(
            text = "4",
            place_x = 5,
            place_y = 100+75,
            panel_read = "4"
        )
        self.Buton_dort = ctk.CTkButton(self.Window,
            text=_Buton_dort_.text,
            font=_Buton_dort_.font,
            height=_Buton_dort_.height,
            width=_Buton_dort_.width,
            command=partial(main_panel_add_fonk,_Buton_dort_.panel_read))
        self.Buton_dort.place(x=_Buton_dort_.place_x, y=_Buton_dort_.place_y)

        _Buton_bes_ = button(
            text = "5",
            place_x = 5+105,
            place_y = 100+75,
            panel_read = "5"
        )
        self.Buton_bes = ctk.CTkButton(self.Window,
            text=_Buton_bes_.text,
            font=_Buton_bes_.font,
            height=_Buton_bes_.height,
            width=_Buton_bes_.width,
            command=partial(main_panel_add_fonk,_Buton_bes_.panel_read))
        self.Buton_bes.place(x=_Buton_bes_.place_x, y=_Buton_bes_.place_y)

        _Buton_alti_ = button(
            text = "6",
            place_x = 110+105,
            place_y = 100+75,
            panel_read = "6"
        )
        self.Buton_alti = ctk.CTkButton(self.Window,
            text=_Buton_alti_.text,
            font=_Buton_alti_.font,
            height=_Buton_alti_.height,
            width=_Buton_alti_.width,
            command=partial(main_panel_add_fonk,_Buton_alti_.panel_read))
        self.Buton_alti.place(x=_Buton_alti_.place_x, y=_Buton_alti_.place_y)

        _Buton_yedi_ = button(
            text = "7",
            place_x = 5,
            place_y = 175+75,
            panel_read = "7"
        )
        self.Buton_yedi = ctk.CTkButton(self.Window,
            text=_Buton_yedi_.text,
            font=_Buton_yedi_.font,
            height=_Buton_yedi_.height,
            width=_Buton_yedi_.width,
            command=partial(main_panel_add_fonk,_Buton_yedi_.panel_read))
        self.Buton_yedi.place(x=_Buton_yedi_.place_x, y=_Buton_yedi_.place_y)

        _Buton_sekiz_ = button(
            text = "8",
            place_x = 5+105,
            place_y = 175+75,
            panel_read = "8"
        )
        self.Buton_sekiz = ctk.CTkButton(self.Window,
            text=_Buton_sekiz_.text,
            font=_Buton_sekiz_.font,
            height=_Buton_sekiz_.height,
            width=_Buton_sekiz_.width,
            command=partial(main_panel_add_fonk,_Buton_sekiz_.panel_read))
        self.Buton_sekiz.place(x=_Buton_sekiz_.place_x, y=_Buton_sekiz_.place_y)

        _Buton_dokuz_ = button(
            text = "9",
            place_x = 110+105,
            place_y = 175+75,
            panel_read = "9"
        )
        self.Buton_dokuz = ctk.CTkButton(self.Window,
            text=_Buton_dokuz_.text,
            font=_Buton_dokuz_.font,
            height=_Buton_dokuz_.height,
            width=_Buton_dokuz_.width,
            command=partial(main_panel_add_fonk,_Buton_dokuz_.panel_read))
        self.Buton_dokuz.place(x=_Buton_dokuz_.place_x, y=_Buton_dokuz_.place_y)

        _Buton_nokta_ = button(
            text = ".",
            place_x = 5,
            place_y = 175+75+80,
            height = 60,
            width = 90,
            panel_read = "."
        )
        self.Buton_nokta = ctk.CTkButton(self.Window,
            text=_Buton_nokta_.text,
            font=_Buton_nokta_.font,
            height=_Buton_nokta_.height,
            width=_Buton_nokta_.width,
            command=partial(main_panel_add_fonk,_Buton_nokta_.panel_read))
        self.Buton_nokta.place(x=_Buton_nokta_.place_x, y=_Buton_nokta_.place_y)

        _Buton_sifir_ = button(
            text = "0",
            place_x = 5+105,
            place_y = 175+75+80,
            height = 60,
            panel_read = "0"
        )
        self.Buton_sifir = ctk.CTkButton(self.Window,
            text=_Buton_sifir_.text,
            font=_Buton_sifir_.font,
            height=_Buton_sifir_.height,
            width=_Buton_sifir_.width,
            command=partial(main_panel_add_fonk,_Buton_sifir_.panel_read))
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

        _Buton_arti_ = button(
            text = "+",
            place_x = 330,
            place_y = 100,
            height = 70,
            width = 70,
            fg_color = "#C84153",
            hover_color = "#D36977",
            panel_read = "+"
        )
        self.Buton_arti = ctk.CTkButton(self.Window,
            text=_Buton_arti_.text,
            font=_Buton_arti_.font,
            height=_Buton_arti_.height,
            width=_Buton_arti_.width,
            fg_color=_Buton_arti_.fg_color,
            hover_color=_Buton_arti_.hover_color,
            command=partial(main_panel_add_fonk,_Buton_arti_.panel_read)
            )
        self.Buton_arti.place(x=_Buton_arti_.place_x, y=_Buton_arti_.place_y)

        _Buton_eksi_ = button(
            text = "-",
            place_x = 330,
            place_y = 100+75,
            height = 70,
            width = 70,
            fg_color = "#C84153",
            hover_color = "#D36977",
            panel_read = "-"
        )
        self.Buton_eksi = ctk.CTkButton(self.Window,
            text=_Buton_eksi_.text,
            font=_Buton_eksi_.font,
            height=_Buton_eksi_.height,
            width=_Buton_eksi_.width,
            fg_color=_Buton_eksi_.fg_color,
            hover_color=_Buton_eksi_.hover_color,
            command=partial(main_panel_add_fonk,_Buton_eksi_.panel_read)
            )
        self.Buton_eksi.place(x=_Buton_eksi_.place_x, y=_Buton_eksi_.place_y)

        _Buton_carpi_ = button(
            text = "x",
            place_x = 330,
            place_y = 175+75,
            height = 70,
            width = 70,
            fg_color = "#C84153",
            hover_color = "#D36977",
            panel_read = "*"
        )
        self.Buton_carpi = ctk.CTkButton(self.Window,
            text=_Buton_carpi_.text,
            font=_Buton_carpi_.font,
            height=_Buton_carpi_.height,
            width=_Buton_carpi_.width,
            fg_color=_Buton_carpi_.fg_color,
            hover_color=_Buton_carpi_.hover_color,
            command=partial(main_panel_add_fonk,_Buton_carpi_.panel_read)
            )
        self.Buton_carpi.place(x=_Buton_carpi_.place_x, y=_Buton_carpi_.place_y)

        _Buton_sil_ = button(
            text = "←",
            place_x = 330,
            place_y = 329,
            height = 60,
            width = 70,
            fg_color = "#C84153",
            hover_color = "#D36977",
            font=("italic",30)
        )
        self.Buton_sil = ctk.CTkButton(self.Window,
            text=_Buton_sil_.text,
            font=_Buton_sil_.font,
            height=_Buton_sil_.height,
            width=_Buton_sil_.width,
            fg_color=_Buton_sil_.fg_color,
            hover_color=_Buton_sil_.hover_color,
            command=sil_fonk
            )
        self.Buton_sil.place(x=_Buton_sil_.place_x, y=_Buton_sil_.place_y)

if __name__ == "__main__":
    Window = ctk.CTk()
    app = MainWindow(Window)
    Window.mainloop()