
#--------------------------------------------------------------
#--------------- EJERCICIO 1 CAJA DE KIOSCO --------------------
#---------------------------------------------------------------

# --- INICIALIZACION Y VALIDACION DEL CLIENTE ----
print(" ================ CAJA DE KIOSCO ================= ")
print("=" * 40)
print("")


nombre = input("Nombre del cliente: ")
#solo letras, validacion con.isalpha()

while not nombre.isalpha():
    print("Error: Su nombre debe contener solo letras y no puede quedar vacio")
    nombre= input("Nombre del cliente: ")

print()

# --- VALIDACIOIN DE CANTIDAD DE PRODUCTOS ---
cantidad = input("Ingrese la cantidad de productos a comprar: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese numeros entero positivo mayor a cero")
    cantidad = input("Ingrese la cantidad de productos a comprar:")

cantidad = int(cantidad)

print()
# --- ACUMULADORES ---
total_sin_descuento = 0
total_con_descuento = 0.0

# --- PROCESAMIENTO DE PRODUCTOS ---
for i in range(1, cantidad + 1):
    # 1. Pedir y validar el precio (ADENTRO DEL FOR)
    precio_str = input(f"Producto {i} - Precio: ")
    while not precio_str.isdigit():
        print("Error: Ingrese un precio numérico entero válido.")
        precio_str = input(f"Producto {i} - Precio: ")
    
    precio = int(precio_str)

#validar si tiene descuento
    descuento = input(f"El producto {i} tiene descuento? (S/N): ")
    while descuento.lower() not in ("s", "n"):
        print("Error: Ingrese unicamente 's' o 'n'. ")
        descuento = input(f"¿El producto {i} tiene descuento (S/N): ")

# suma total
    total_sin_descuento += precio

    if descuento.lower() == "s":
        total_con_descuento += precio * 0.90
    else:
        total_con_descuento += precio

# --- CALCULOS FINALES ---

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad 

# --- SALIDA DE RESULTADOS ---

print("\n --- RESUMEN DE COMPRA ---")
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

print()

print(" ================ ACCESO AL CAMPUS ==================")
print("=" * 40)
# ------------------------------------------------------------
# ------------ EJERCICIO 2 ACCESO AL CAMPUS ------------------
# ------------------------------------------------------------

# ACCESO AL CAMPUS 
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3:

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    print()

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido")
        acceso = True
        break
    else:
        intentos += 1
        print("Usuario o Clave incorrectos")
        print(f"Intentos restantes: {3 - intentos}")

    print()

if not acceso:
    print("Cuenta bloqueada")
else:
    opcion = ""

    while opcion != "4":
        print()
        print("=====================================")
        print("      MENU DEL CAMPUS                ")
        print("======================================")
        print(" 1. Ver estado de inscripcion")
        print(" 2. Cambiar clave")
        print(" 3. Mostrar mensaje motivacional")
        print(" 4. Salir")

        opcion = input("Eliga una opcion: ")

        while not opcion.isdigit():
            print("Error: debe ingresar solo numeros")
            opcion = input("Eliga una opcion: ")

        while int(opcion) < 1 or int(opcion) > 4:
            print("Error: debe ingresar un numero entre el 1 y 4:")
            opcion = input("Eliga una opcion: ")

        if opcion == "1":
            print("Estado de inscripcion: Inscripto")
            input("Presione Enter para volver al menu...")

        elif opcion == "2":
            nueva_clave = input("Ingrese la nueva clave:")

            if len(nueva_clave) < 6:
                print("Error: la clave debe contener minimo 6 caracteres")
            else:
                confirmacion = input("Confirme la nueva clave: ")
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada correctamente")
                else:
                    print("Error: las claves no coinciden")

        elif opcion == "3":
            print("Aveces las cosas no salen como queremos, pero salen como era necesaria vivirlas para poder crecer")
            input("Presione Enter para volver al menu...")

        elif opcion == "4":
            print("Saliendo del campus...")


print()


# ===============================================================
# ============== EJERCICIO 3 — AGENDA DE TURNOS =================
# ================================================================


cupos_lunes = 4
cupos_martes = 3
 
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
 
martes1 = ""
martes2 = ""
martes3 = ""
 
lunes_ocupados = 0
martes_ocupados = 0
 
print("========== AGENDA DE TURNOS ==========")
print("=" * 40)
print("")
 
operador = input("Ingrese su nombre: ")
while not operador.isalpha():
    print("Error: su nombre debe contener solo letras")
    operador = input("Ingrese su nombre: ")
 
opcion = ""
while opcion != "5":
    print("=" * 20)
    print("MENU PRINCIPAL")
    print("=" * 20)
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
 
    opcion = input("Elija una opcion: ")
    while not opcion.isdigit():
        print("Error: debe ingresar solo numeros")
        opcion = input("Elija una opcion: ")
    while int(opcion) < 1 or int(opcion) > 5:                 
        print("Error: debe ingresar un numero entre 1 y 5")
        opcion = input("Elija una opcion: ")
 
    # ---------------- Opcion 1: Reservar turno ----------------
    if opcion == "1":
        dia = input("Elija un dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: ingrese 1 o 2.")
            dia = input("Elija un dia (1=Lunes, 2=Martes): ")
 
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        while not nombre_cliente.isalpha():
            print("Error: su nombre debe contener solo letras")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
 
        if dia == "1":
            existe = False
            if lunes1 == nombre_cliente:
                existe = True
            elif lunes2 == nombre_cliente:
                existe = True
            elif lunes3 == nombre_cliente:
                existe = True
            elif lunes4 == nombre_cliente:
                existe = True
 
            if existe:                                          
                print("Error: ese cliente ya tiene un turno reservado el lunes.")
            elif lunes_ocupados >= cupos_lunes:
                print("No hay turnos disponibles para el lunes.")
            else:
                if lunes1 == "":
                    lunes1 = nombre_cliente
                elif lunes2 == "":
                    lunes2 = nombre_cliente
                elif lunes3 == "":
                    lunes3 = nombre_cliente
                elif lunes4 == "":
                    lunes4 = nombre_cliente
 
                lunes_ocupados += 1
                print(f"Turno reservado para {nombre_cliente} el lunes. ({lunes_ocupados}/{cupos_lunes})")
 
        else:  # dia == "2"
            existe = False
            if martes1 == nombre_cliente:
                existe = True
            elif martes2 == nombre_cliente:
                existe = True
            elif martes3 == nombre_cliente:
                existe = True
 
            if existe:
                print("Error: ese cliente ya tiene un turno reservado el martes.")
            elif martes_ocupados >= cupos_martes:
                print("No hay turnos disponibles para el martes.")
            else:
                if martes1 == "":
                    martes1 = nombre_cliente
                elif martes2 == "":
                    martes2 = nombre_cliente
                elif martes3 == "":
                    martes3 = nombre_cliente
 
                martes_ocupados += 1
                print(f"Turno reservado para {nombre_cliente} el martes. ({martes_ocupados}/{cupos_martes})")
 
    # ---------------- Opcion 2: Cancelar turno ----------------
    elif opcion == "2":
        dia = input("Elija un dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: ingrese 1 o 2.")
            dia = input("Elija un dia (1=Lunes, 2=Martes): ")
 
        nombre_cliente = input("Ingrese el nombre del cliente a cancelar: ")
        while not nombre_cliente.isalpha():
            print("Error: su nombre debe contener solo letras")
            nombre_cliente = input("Ingrese el nombre del cliente a cancelar: ")
 
        if dia == "1":
            if lunes1 == nombre_cliente:
                lunes1 = ""
                lunes_ocupados -= 1
                print(f"Turno de {nombre_cliente} cancelado el lunes.")
            elif lunes2 == nombre_cliente:
                lunes2 = ""
                lunes_ocupados -= 1
                print(f"Turno de {nombre_cliente} cancelado el lunes.")
            elif lunes3 == nombre_cliente:
                lunes3 = ""
                lunes_ocupados -= 1
                print(f"Turno de {nombre_cliente} cancelado el lunes.")
            elif lunes4 == nombre_cliente:
                lunes4 = ""
                lunes_ocupados -= 1
                print(f"Turno de {nombre_cliente} cancelado el lunes.")
            else:
                print("No existe ese paciente en la agenda del lunes.")
 
        else:  # dia == "2"
            if martes1 == nombre_cliente:
                martes1 = ""
                martes_ocupados -= 1
                print(f"Turno de {nombre_cliente} cancelado el martes.")
            elif martes2 == nombre_cliente:
                martes2 = ""
                martes_ocupados -= 1
                print(f"Turno de {nombre_cliente} cancelado el martes.")
            elif martes3 == nombre_cliente:
                martes3 = ""
                martes_ocupados -= 1
                print(f"Turno de {nombre_cliente} cancelado el martes.")
            else:
                print("No existe ese paciente en la agenda del martes.")
 
    # ---------------- Opcion 3: Ver agenda del dia ----------------
    elif opcion == "3":
        dia = input("Elija un dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: ingrese 1 o 2.")
            dia = input("Elija un dia (1=Lunes, 2=Martes): ")
 
        if dia == "1":
            print("Agenda del Lunes:")
            if lunes1 != "":
                print(f"Turno 1: {lunes1}")
            else:
                print("Turno 1: (libre)")
            if lunes2 != "":
                print(f"Turno 2: {lunes2}")
            else:
                print("Turno 2: (libre)")
            if lunes3 != "":
                print(f"Turno 3: {lunes3}")
            else:
                print("Turno 3: (libre)")
            if lunes4 != "":
                print(f"Turno 4: {lunes4}")
            else:
                print("Turno 4: (libre)")
        else:
            print("Agenda del Martes:")
            if martes1 != "":
                print(f"Turno 1: {martes1}")
            else:
                print("Turno 1: (libre)")
            if martes2 != "":
                print(f"Turno 2: {martes2}")
            else:
                print("Turno 2: (libre)")
            if martes3 != "":
                print(f"Turno 3: {martes3}")
            else:
                print("Turno 3: (libre)")
 
    # ---------------- Opcion 4: Resumen general ----------------
    elif opcion == "4":
        total = lunes_ocupados + martes_ocupados
        print("Resumen general de turnos:")
        print(f"Lunes: {lunes_ocupados} ocupados / {cupos_lunes - lunes_ocupados} disponibles")
        print(f"Martes: {martes_ocupados} ocupados / {cupos_martes - martes_ocupados} disponibles")
        print(f"Total de turnos reservados: {total}/{cupos_lunes + cupos_martes}")
 
        if lunes_ocupados > martes_ocupados:                     
            print("Dia con mas turnos: Lunes")
        elif martes_ocupados > lunes_ocupados:
            print("Dia con mas turnos: Martes")
        else:
            print("Empate entre Lunes y Martes")
 
    # ---------------- Opcion 5: Cerrar sistema ----------------
    elif opcion == "5":
        print("Saliendo del sistema...")
 
print("Sistema cerrado. Gracias por utilizar la agenda de turnos.")
print()




# Ejercicio 4 - Escape room a la boveda

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
bloqueado_por_alarma = False
forzar_seguidas = 0

print("========== ESCAPE ROOM A LA BOVEDA ==========")
print("=" * 40)
print("")

nombre_agente = input("Ingrese su nombre: ")

while not nombre_agente.isalpha():
    print("Error: su nombre debe contener solo letras")
    nombre_agente = input("Ingrese su nombre: ")

# ---------- Ciclo principal del juego ----------
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado_por_alarma:

    print("=" * 20)
    print("MENU PRINCIPAL")
    print("=" * 20)
    print(f"Energia: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Elija una opcion: ")
    while not opcion.isdigit() or int(opcion) not in (1, 2, 3):
        print("Error: ingrese una opcion valida (1, 2 o 3).")
        opcion = input("Elija una opcion: ")
    opcion = int(opcion)

    # ---------- Opcion 1: Forzar cerradura ----------
    if opcion == 1:
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2

        if forzar_seguidas == 3:
            # Regla anti-spam: 3ra vez seguida forzando
            print(">> La cerradura se trabo por forzarla demasiadas veces seguidas.")
            alarma = True
            forzar_seguidas = 0
        else:
            if energia < 40:
                print(">> Riesgo de alarma: energia por debajo de 40.")
                riesgo = input("Elija un numero (1-3): ")
                while not riesgo.isdigit() or int(riesgo) not in (1, 2, 3):
                    print("Error: ingrese un numero entre 1 y 3.")
                    riesgo = input("Elija un numero (1-3): ")
                riesgo = int(riesgo)

                if riesgo == 3:
                    print(">> ¡Activaste la alarma!")
                    alarma = True
                else:
                    cerraduras_abiertas += 1
                    print(">> Cerradura forzada con exito.")
            else:
                cerraduras_abiertas += 1
                print(">> Cerradura forzada con exito.")

    # ---------- Opcion 2: Hackear panel ----------
    elif opcion == 2:
        forzar_seguidas = 0
        energia -= 10
        tiempo -= 3

        letras = "ABCDEFGH"
        print(">> Hackeando panel...")
        for paso in range(4):
            codigo_parcial += letras[len(codigo_parcial) % len(letras)]
            print(f"   Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print(">> ¡Codigo completo! Se abrio una cerradura automaticamente.")

    # ---------- Opcion 3: Descansar ----------
    else:
        forzar_seguidas = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1

        if alarma:
            energia -= 10
            print(">> Descansaste, pero la alarma sigue activa (-10 energia extra).")
        else:
            print(">> Descansaste y recuperaste energia.")

    if energia < 0:
        energia = 0
    if tiempo < 0:
        tiempo = 0

    # ---------- Regla de bloqueo por alarma ----------
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado_por_alarma = True

# ---------- Condiciones de fin ----------
print("\n========================================")
if cerraduras_abiertas == 3:
    print(f"VICTORIA - {nombre_agente} abrio la boveda a tiempo.")
elif bloqueado_por_alarma:
    print("DERROTA (bloqueo) - El sistema se bloqueo por la alarma.")
else:
    print("DERROTA - Te quedaste sin energia o sin tiempo.")




#Ejercicio 5 -- "Escape Room: La Arena del Gladiador"
#Simulador de batalla por turnos.

print("========== ESCAPE ROOM A LA BOVEDA ==========")
print("=" * 40)
print("")

# ---------- Configuracion del personaje ----------
print("--- BIENVENIDO A LA ARENA ---")
nombre_jugador = input("Nombre del Gladiador: ")
while nombre_jugador.strip() == "" or not nombre_jugador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_jugador = input("Nombre del Gladiador: ")


vida_jugador = 100          
vida_enemigo = 100        
pociones = 3                 
danio_ataque_pesado = 15     
danio_enemigo = 12           
juego_activo = True          

print("=== INICIO DEL COMBATE ===")

# ---------- Ciclo de combate ----------
while vida_jugador > 0 and vida_enemigo > 0:

    print(f"{nombre_jugador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    opcion = input("Opcion: ")
    while not opcion.isdigit() or int(opcion) not in (1, 2, 3):
        print("Error: Ingrese un numero valido.")
        opcion = input("Opcion: ")
    opcion = int(opcion)

    # ---------- Accion A: Ataque Pesado ----------
    if opcion == 1:
        if vida_enemigo < 20:
            danio_final = danio_ataque_pesado * 1.5   # float -> Golpe Critico
            print(">> ¡Golpe Critico!")
        else:
            danio_final = float(danio_ataque_pesado)

        vida_enemigo -= danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

    # ---------- Accion B: Rafaga Veloz ----------
    elif opcion == 2:
        print(">> ¡Inicias una rafaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # ---------- Accion C: Curar ----------
    else:
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100:
                vida_jugador = 100
            pociones -= 1
            print(">> Usaste una pocion y recuperaste 30 puntos de vida.")
        else:
            print("¡No quedan pociones!")

    # ---------- Turno del enemigo ----------
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

    print("=== NUEVO TURNO ===")

# ---------- Paso 4: Fin del juego ----------
juego_activo = False
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre_jugador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
 
