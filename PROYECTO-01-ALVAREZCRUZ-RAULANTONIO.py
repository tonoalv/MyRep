from StoreData import lifestore_products, lifestore_sales, lifestore_searches

print("\n   ***Bienvenido a Life Store***\n")
print("     --Para las necesidades de tu vida--\n")

print("         Para continuar, inicia sesión\n")

nombre = input("          Nombre: ")
usuario = input("         Usuario: ")
contrasena = input("      Contraseña: ")

print("Para verificar tu información, por favor ingresa tus datos nuevamente")

while True:
    verif_usuario = input("          Usuario: ")
    verif_contrasena = input("          Contrseña: ")
    if verif_usuario == usuario and verif_contrasena == contrasena:
        print("  BIENVENIDO, ", nombre,"!")
        break
    else:
        print("El usuario o contraseña ingresados no coinciden. Favor de intentarlo de nuevo")

print("***************************************************")
print("1.- Productos")
print("2. Finanzas")
print("3. Editar información personal")
print("4. Salir")
print("***************************************************")

sales = []
while True:
    menu_op = int(input("Selecciona una opción del menu"))
    if menu_op < 0 or menu_op > 5:
      print("Opcion invalida. Intenta de nuevo.")
    else:
      break


if menu_op == 1:
    print("1.- Los más populares")
    print("2.- Los menos populares")

    while True:
        prod_op = int(input("Selecciona la información que deseas ver"))
        if prod_op == 1:
            print("****PRODUCTOS MÁS POPULARES*****")
            print("1.- Por venta")
            print("2.- Por búsqueda")
            print("3.- Por reseña")
            while True:
                op_prod = int(input("Selecciona la información que deseas ver"))
                
                if op_prod == 1:
                  contador = 0
                  devs = 0
                  ventastotales = []
                  least_sales = []
                  for item in lifestore_products:
                    for venta in lifestore_sales:
                      if item[0] == venta[1]:
                        contador += 1
                        if venta[4] == 1:
                          devs += 1
                    freq = [item[0], item[-2], contador, "Devs: ", devs, "Stock: ", item[-1]]
                    ventastotales.append(freq)
                    contador = 0
                    devs = 0
                    least = []
                    ventastotales.sort(key = lambda x: x[2], reverse = True)



                  print("*****TOP 10 MÁS VENDIDOS****")
                  print(ventastotales[1:11])
                  while True:
                    ver_mas = input("Presiona '+' para ver el top 50 de ventas o presiona 1 para ver la lista completa")
                    if ver_mas == '+':
                      print("******TOP 50*****")
                      print(ventastotales[1:51])
                    if ver_mas == 1:
                      print("****TODAS LAS VENTAS****")
                      print(ventastotales)

                      
                    
                elif op_prod == 2:
                  contador = 0
                  total_searches = []
                  for item in lifestore_products:
                    for search in lifestore_searches:
                      if item[0] == search[1]:
                        contador += 1
                    freq = [item[0], item[-2], contador]
                    total_searches.append(freq)
                    contador = 0
                    total_searches.sort(key = lambda x: x[2], reverse = True)
                  print("******TOP 10*****")
                  print(total_searches[1:11])
                  while True:
                    ver_mas = input("Presiona '+' para ver el top 50 de ventas o presiona 1 para ver la lista completa")
                    if ver_mas == '+':
                      print("******TOP 50*****")
                      print(total_searches[1:51])
                    if ver_mas == 1:
                      print("****TODAS LAS BÚSQUEDAS****")
                      print(total_searches)

                elif op_prod == 3:
                  contador = 0
                  stars = 0
                  devs = 0
                  total_reviews = []
                  for producto in lifestore_products:
                    for review in lifestore_sales:
                      if producto[0] == review[1]:
                        contador += 1
                        stars += review[2]
                        final_s = stars/contador
                        final_stars = round(final_s, 2)
                        if review[4] == 1:
                          devs += 1
                    freq = [producto[0], producto[-2],final_stars, "Devoluciones: ", devs]
                    total_reviews.append(freq)
                    contador = 0
                    stars = 0
                    devs = 0
                    total_reviews.sort(key = lambda x: x[2], reverse = True)
                  print("*****TOP 10 MEJORES ARTÍCULOS****")
                  print(total_reviews[1:11])
                  while True:
                    ver_mas = input("Presiona '+' para ver el top 50 de ventas o presiona 1 para ver la lista completa")
                    if ver_mas == '+':
                      print("******TOP 50*****")
                      print(total_reviews[1:51])
                    if ver_mas == 1:
                      print("****TODAS LAS VENTAS****")
                      print(total_reviews)


                else:
                  print("Opción inválida. Intenta de nuevo")

        elif prod_op == 2:
            print("****LOS PRODUCTOS MENOS POPULARES*****")
            print("1.- Por venta")
            print("2.- Por búsqueda")
            print("3.- Por reseña")
            while True:
                op_prod = int(input("Selecciona la información que deseas ver"))
                
                if op_prod == 1:
                  contador = 0
                  devs = 0
                  ventastotales = []
                  for item in lifestore_products:
                    for venta in lifestore_sales:
                      if item[0] == venta[1]:
                        contador += 1
                        if venta[4] == 1:
                          devs += 1
                    freq = [item[0], item[-2],contador, "Devoluciones: ", devs, "Stock: ", item[-1]]
                    ventastotales.append(freq)
                    contador = 0
                    devs = 0
                    least = []
                    ventastotales.sort(key = lambda x: x[2])

                  print("****LAS MANZANAS PODRIDAS****")
                  print("**** TOP 10 MENOS VENTAS :( ****")
                  print(ventastotales[1:11])
                  while True:
                    ver_mas = input("Presiona '+' para ver el top 50 de ventas o presiona 1 para ver la lista completa")
                    if ver_mas == '+':
                      print("******TOP 50 :( *****")
                      print(ventastotales[1:51])
                    if ver_mas == 1:
                      print("****TODAS LAS NO-VENTAS****")
                      print(ventastotales)

                elif op_prod == 2:
                  contador = 0
                  total_searches = []
                  for item in lifestore_products:
                    for search in lifestore_searches:
                      if item[0] == search[1]:
                        contador += 1
                    freq = [item[0], item[-2], contador]
                    total_searches.append(freq)
                    contador = 0
                    total_searches.sort(key = lambda x: x[2])

                  print("***TOP 10 ABANDONADOS :(***")
                  print(total_searches[1:11])
                  while True:
                    ver_mas = input("Presiona '+' para ver el top 50 de ventas o presiona 1 para ver la lista completa")
                    if ver_mas == '+':
                      print("******TOP 50 MÁS ABANDONADOS*****")
                      print(total_searches[1:51])
                    if ver_mas == 1:
                      print("****TODOS LOS RELEGADOS****")
                      print(total_searches)

                elif op_prod == 3:
                  contador = 0
                  stars = 0
                  devs = 0
                  total_reviews = []
                  for producto in lifestore_products:
                    for review in lifestore_sales:
                      if producto[0] == review[1]:
                        contador += 1
                        stars += review[2]
                        final_s = stars/contador
                        final_stars = round(final_s, 2)
                        if review[4] == 1:
                          devs += 1
                    freq = [producto[0], producto[-2],final_stars, "Devoluciones: ", devs]
                    total_reviews.append(freq)
                    contador = 0
                    stars = 0
                    devs = 0
                    total_reviews.sort(key = lambda x: x[2])
                  print("****LOS 10 MENOS QUERIDOS****")
                  print(total_reviews[1:11])
                  while True:
                    ver_mas = input("Presiona '+' para ver el top 50 de ventas o presiona 1 para ver la lista completa")
                    if ver_mas == '+':
                      print("******TOP 50 PEOR CALIFICADOS*****")
                      print(total_reviews[1:51])
                    if ver_mas == 1:
                      print("****TODAS LAS VENTAS****")
                      print(total_reviews)

          
        else:
            print("Opción invalida. Intenta de nuevo")
                      
elif menu_op == 2:
    print("****FINANZAS****")
    print("1.- Ventas Mensual")
    print("2.- Ingreso Anual")
    print("3.- Devoluciones")
    while True:
      menu_ventas = int(input("Selecciona la opción que deseas ver"))      
      if menu_ventas == 1:
        meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        final = []
        contador = 0
        for mes in meses:
          for sale in lifestore_sales:
            if mes == sale[-2][3:5]:
              contador += 1
          freq = [mes, contador]
          final.append(freq)
          contador = 0
        print("****VENTAS MENSUALES***")
        print(final)
        print("Para los meses con menores ventas: 1")
        print("Para los meses con mayores ventas: 2")
        print("Para ingreso por mes: 3")
        menu_arreglo = int(input("Selecciona una opción del menu"))
        if menu_arreglo == 1:
          final.sort(key = lambda x:x[1])
          print(final[0:4])
          opcionmas = input("Presiona 0 para ver la lista completa")
          if opcionmas == 0:
            print(final)
        if menu_arreglo == 2:
          final.sort(key = lambda x:x[1], reverse = True)
          print(final[0:4])
          opcionmas = input("Presiona 0 para ver toda la lista")
          if opcionmas == 0:
            print(final)
        if menu_arreglo == 3:
          meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
          final = []
          contador = 0
          valor = 0
          for mes in meses:
            for sale in lifestore_sales:
               if mes == sale[-2][3:5]:
                contador += 1
                for producto in lifestore_products:
                  if producto[0] == sale[1]:
                    valor += producto[2]
            freq = [mes, contador, '$',valor]
            final.append(freq)
            contador = 0
            valor = 0
          print("****VENTAS POR MES***")
          print(final)
          opcionmas = int(input("Presiona 0 para ordenar la lista"))
          if opcionmas == 0:
            final.sort(key = lambda x: x[-1], reverse = True)
            print(final)

      if menu_ventas == 2:
        contador = 0
        refunds = 0
        total_refs = []
        totaltotalrefs = []
        ingresototalanual = []
        for producto in lifestore_products:
          for refund in lifestore_sales:
            if producto[0] == refund[1]:
              contador += 1
              if refund[-1] == 1:
                refunds += 1
          freq = [producto[0], producto[2], contador, refunds]
          total_refs.append(freq)
          freq1 = [producto[0], producto[2], contador, producto[2]*contador]
          totaltotalrefs.append(freq1)
          freq2 = [producto[2]*contador]
          ingresototalanual.append(freq2)
          contador = 0
          refunds = 0
          total_refs.sort(key = lambda x: x[0], reverse = True)
        sumatotal = sum(sum(x) for x in ingresototalanual)
        print("INGRESO ANUAL: $",sumatotal)
        print("PROMEDIO MENSUAL: $", (round(sumatotal/12)))
        print("PROMEDIO DIARIO: $", (round(sumatotal/365)))
        opcionmas = input("Para ver detalles presiona '+'")
        if opcionmas == "+":
          print(totaltotalrefs)

      if menu_ventas == 3:
        contador = 0
        refunds = 0
        total_refs = []
        totaltotalrefs = []
        for producto in lifestore_products:
          for refund in lifestore_sales:
            if producto[0] == refund[1]:
              contador += 1
              if refund[-1] == 1:
                refunds += 1
          freq = [producto[0], producto[2], contador, refunds]
          total_refs.append(freq)
          freq1 = [producto[0], producto[2], refunds, producto[2]*refunds]
          totaltotalrefs.append(freq1)
          contador = 0
          refunds = 0
          total_refs.sort(key = lambda x: x[0], reverse = True)
          if freq1[-2] == 0:
            totaltotalrefs.remove(freq1)
        n1 = 0
        for suma in totaltotalrefs:
          n1 += suma[-1]
        
        print("Total en devoluciones: $",n1)
        opcionmas = input("Para más detalles presiona +")
        if opcionmas == "+":
          print(totaltotalrefs)


elif menu_op == 3:
    print("Usuario: ", usuario)
    print(" 1.- Editar")
    print("Contraseña: ", contrasena)
    print("2. Editar")
    print("Nombre: ", nombre)
    print("3. Editar")

    while True:
      nva_info = int(input("Selecciona una opción del menú"))
      if nva_info == 1:
        old_user = input("Escribe tu actual usuario")
        nvo_user = input("Escribe tu nuevo usuario")
        if old_user == usuario:
          nvo_user = usuario
        print("Cambio realizado con éxito")
        break
      if nva_info == 2:
        old_pass = input("Escribe tu contraesña actual")
        new_pass = input("Escribe tu nueva contraseña")
        if old_pass == contrasena:
          new_pass = contrasena
          print("Cambio realizado con éxito")
          break
      if nva_info == 3:
        old_name = input("Escribe tu nombre actual")
        nvo_name = input("Escribe tu nuevo nombre")
        if old_name == nombre:
          nvo_name = nombre
          print("Cambio realizado con éxito")
          break
      else:
        print("Opción no válida. Intenta de nuevo")


elif menu_op == 4:
    print("Gracias por elegir Life Store")
    print("Hasta pronto")
    exit
else:
  print("La opción ingresada no existe. Intenta de nuevo")
