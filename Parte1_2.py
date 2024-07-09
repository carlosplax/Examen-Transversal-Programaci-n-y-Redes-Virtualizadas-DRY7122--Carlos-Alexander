def verificar_vlan(numero_vlan):
    if numero_vlan >= 1 and numero_vlan <= 1000:
        print("El número de VLAN", numero_vlan, "corresponde a una VLAN del rango normal.")
    elif numero_vlan >= 1002 and numero_vlan <= 4094:
        print("El número de VLAN", numero_vlan, "corresponde a una VLAN del rango extendido.")
    else:
        print("El número de VLAN", numero_vlan, "no es válido.")

# Solicitar al usuario el número de VLAN
numero_vlan = int(input("Ingrese el número de VLAN: "))

# Verificar la VLAN ingresada
verificar_vlan(numero_vlan)