from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import flet as ft


def main(page: ft.Page):
    

    def pad(kata):
        padding_length = AES.block_size - len(kata) % AES.block_size
        return kata + (chr(padding_length) * padding_length).encode()

    def unpad(kata):
        padding_length = kata[-1]
        return kata[:-padding_length]

    def encrypt(key, kata):
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_kata = cipher.encrypt(pad(kata))
        return base64.b64encode(cipher.iv + encrypted_kata)

    def decrypt(key, encrypted_kata):
        encrypted_kata = base64.b64decode(encrypted_kata)
        iv = encrypted_kata[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_kata = cipher.decrypt(encrypted_kata[AES.block_size:])
        return unpad(decrypted_kata)

    def gen_key(e):
        inp2.value = get_random_bytes(16)
        page.update()
    


    def enkripsi(e):
        hasil.value=''
        
        v = inp1.value
        kata = v.encode()

        encrypted = encrypt(inp2.value, kata)
        hasil.value = encrypted.decode("utf-8")
        

        page.update()

    def dekripsi(e):
        hasil.value=''

        decrypted = decrypt(inp2.value, inp1.value)
        hasil.value = decrypted.decode("utf-8")
        page.update()
 

    def keluar(e):
        page.window_close() 

    inp1 = ft.TextField(label="Masukkan Teks Enkripsi/Dekripsi",
            width=450,
            bgcolor=ft.colors.TRANSPARENT,
            expand=0)
   
    inp2 = ft.TextField(label="Masukan Kunci",
                        width=450,
                        height=80,
                        border=ft.InputBorder.NONE,
                        bgcolor=ft.colors.TRANSPARENT)
  
    hasil = ft.TextField(label="Hasil Enkripsi/Dekripsi",
                        width=450,
                        height=80,
                        border=ft.InputBorder.NONE,
                        bgcolor=ft.colors.TRANSPARENT, 
                        read_only=True)

    

    enk = ft.ElevatedButton(text="Enkripsi",
                width=220,
                height=37,
                 bgcolor=ft.colors.GREY,
                color=ft.colors.BLACK,
                expand=0,
                on_click=enkripsi
                )
    dek = ft.ElevatedButton(text="Dekripsi",
                width=220,
                height=37,
                 bgcolor=ft.colors.GREY,
                color=ft.colors.BLACK,
                expand=0,
                on_click=dekripsi
                )
    gk = ft.ElevatedButton(text="Generate Key",
                width=450,
                height=37,
                 bgcolor=ft.colors.ORANGE_ACCENT,
                color=ft.colors.BLACK,
                expand=0,
                on_click=gen_key
                )
    keluar = ft.ElevatedButton(text="Keluar",
                width=450,
                height=37,
                bgcolor=ft.colors.RED,
                color=ft.colors.WHITE,
                expand=0,
                on_click=keluar
                )

    baris1 = ft.Container(ft.Row(controls=[inp1]))
    baris2 = ft.Container(ft.Row(controls=[inp2]))
    
    baris3 = ft.Container(ft.Row(controls=[gk]))
    baris4 = ft.Container(ft.Row(controls=[enk, dek]))
    baris5 = ft.Container(ft.Row(controls=[keluar]))

    page.window_center()
    
    page.window_title_bar_hidden = True
    # page.window_frameless = True
    page.window_width=480
    page.window_resizable=0
    page.window_height=450
    page.add(ft.Text("                  Aplikasi Enkripsi Algoritma Rijndael ",
                     font_family="Impact",
                      style=ft.TextThemeStyle.TITLE_LARGE,
                      color=ft.colors.BLUE,
                        ))
    page.add(baris1,baris2,baris3, baris4, hasil)
    page.add(baris5)
    
    
ft.app(target=main)