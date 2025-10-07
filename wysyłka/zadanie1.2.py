lista_zakupow=[("roquefort"), ("stilton"), ("brie"),("gouda"), ("edam"), ("parmezan"), ("mozarella"),("czechosłowacki ser z owczego mleka")]
lista_cen1=[12.50, 11.24, 9.30, 8.55, 11.00,16.50, 14.00, 122.32]
raporty = []
for i,ser in enumerate(lista_zakupow):
    raporty.append(f"{ser:35} {lista_cen1[i]:6.2f}zł\n")
print("".join(raporty))
        
        
    