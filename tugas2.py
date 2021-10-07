def main():

    print("jb-Jabodetabek\ndw-Pulau Jawa\nlw-Luar Jawa")
    destinasi= input("Tujuan Barang(q-quit)= ")

    if destinasi=="q":
                    exit(0)
    beban = int(input("Berat Barang = "))
    if destinasi == "jb":
            harga= 10000
    elif destinasi == "dw":
            harga= 25000
    elif destinasi == "lw":
            harga=50000
    else:
            print ("Invalid input")
            destinasi= input("tujuan barang= ")
            
    if beban <= 20:
            n = 15000
    elif beban >= 20:
            n = beban * 1500

    ppn = (harga+n)/10

    print("------------Rincian Biaya-----------")
    print("1.tujuan= ",destinasi,     "harga= Rp.",harga)
    print("2.Berat=  ",beban,"kg", "harga= Rp.",n)
    print("3.PPN 10%= Rp.", ppn)
    print("4.Total= Rp.",harga+n+ppn)
    print("-------------------------------------")
    main()


main()


