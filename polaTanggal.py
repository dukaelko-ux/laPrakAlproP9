import re
from datetime import datetime

teks = ('Pada tanggal 1945-08-17 Indonesia merdeka. '
        'Pangeran Diponegoro (TL: 1785-11-11), '
        'Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02).')

pola = r'\d{4}-\d{2}-\d{2}'
tanggal_ditemukan = re.findall(pola, teks)
sekarang = datetime.now()

for tgl in tanggal_ditemukan:
    dt = datetime.strptime(tgl, '%Y-%m-%d')
    selisih = abs((sekarang - dt).days)
    print(f'{dt} selisih {selisih} hari')
