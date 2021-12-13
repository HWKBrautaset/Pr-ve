def cesar_encrypt(text_som_skal_krypteres):
    text_som_skal_krypteres = text_som_skal_krypteres.lower()
    abc = ".,abcdefghij klmnopqrstuvwxyzæøå"
    acb = "åæøxyz t.,uvabcdefghijklmnopqrst"
    kryptert_text = ''
    for i in text_som_skal_krypteres:
        n = 0
        for j in abc:
            if j == i:
                kryptert_text += acb[n]
                break
            n += 1
    return(kryptert_text)

