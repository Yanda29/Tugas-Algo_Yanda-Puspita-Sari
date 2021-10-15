aku=1500
while aku ==1500:
    import sys
    
    elo= {"jb","lw","lw"}

    print("jb-Jabodetabek\ndw-Pulau Jawa\nlw-Luar Jawa")
    destinasi= input("Tujuan Barang(q-quit)= ")
    if destinasi=="q":
                    sys.exit(0)
    if destinasi == "jb":
            price= 10000
    elif destinasi == "dw":
            price= 25000
    elif destinasi == "lw":
            price=50000
    else:
        print ("Invalid input")
        destinasi= input("Tujuan Barang(q-quit)= ")
    
    
    jb =price= 10000
    dw =price= 25000
    lw =price= 50000
    beban = int(input("Berat Barang = "))
            
    if beban <= 20:
            n = 15000
    elif beban >= 20:
            n = (15000 + ((beban - 20) *1500))
    else:
        print ("Invalid input")
        beban = int(input("Berat Barang = "))

    ppn = int(price+n)/10

    print('====================total================================\n'
    f'tujuan= ,destinasi,     harga= Rp.{price}\n'
    f'Berat=  {beban}kg ,harga= Rp.,{n}\n'
    f'PPN 10%= Rp., {ppn}\n'
    f'Total= Rp.",{price+n+ppn}')
    print("==========================================================")
