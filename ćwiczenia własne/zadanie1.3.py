lista_zakupow=[("roquefort"), ("stilton"), ("brie"),("gouda"), ("edam"), ("parmezan"), ("mozarella"),(" czechosłowacki ser z owczego mleka")]
lista_cen1=[12.50, 11.24, 9.30, 8.55, 11.00,16.50, 14.00, 122.32]
lista_zakupow=[]
lista_zakupow.append("roquefort - 2kg")
lista_zakupow.append("parmezan - 3.5kg")
lista_zakupow.append("mozarella - 1.3kg")
lista_zakupow.append("  czechosłowacki ser z owczego mleka - 2.2kg")
lista_zakupow.append("stilton - 1kg")
lista_zakupow.append("brie - 1 kg")
lista_zakupow.append("gouda - 1 kg")
lista_zakupow.append("edam- 1kg")
lista_zakupow.append("listek miętowy- 0.2 kg")
print(lista_zakupow)
lista_cen1=[]
lista_cen2=[20]
lista_cen1.extend(lista_cen2)
suma_zakupow = sum(lista_cen1)
print(f"Całkowity koszt zakupow: {suma_zakupow} zł")