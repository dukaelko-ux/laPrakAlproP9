import re
import random
import string

teks = ('anton@mail.com dimiliki oleh antonius\n'
        'budi@gmail.co.id dimiliki oleh budi anwari\n'
        'slamet@getnada.com dimiliki oleh slamet slumut\n'
        'matahari@tokopedia.com dimiliki oleh toko matahari')

pola_email = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+(?:\.[a-zA-Z]+)+'
email_ditemukan = re.findall(pola_email, teks)

def buat_password(panjang=8):
    karakter = string.ascii_letters + string.digits
    return ''.join(random.choice(karakter) for _ in range(panjang))

for email in email_ditemukan:
    username = email.split('@')[0]
    password = buat_password()
    print(f'{email} username: {username} , password: {password}')
