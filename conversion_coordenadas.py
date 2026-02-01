def dd_to_dms(dd):
    #se usa valores enteros para hacer calculos limpios
    dd_abs = abs(dd)
    grados = int(dd_abs)
    minutos = int((dd_abs - grados) * 60)
    segundos = (dd_abs - grados - minutos / 60) * 3600
    return grados, minutos, segundos

def dms_to_dd(grados, minutos, segundos, direccion):
    dd = grados + minutos / 60 + segundos / 3600
    if direccion.upper() in ["S", "W", "O"]:
        dd = dd * -1
    return dd

def main ():
    print ("=" * 52) 
    print ("Bienvenidos a la calculadora de coordenadas")
    print (" conversor de coordenadas")
    print ("=" * 52)
 

def main():
    print("Conversión de coordenadas")
    print("1. Grados decimales a grados, minutos y segundos")
    print("2. Grados, minutos y segundos a grados decimales")
    option = input(">>")

    if option == "1":
        lat_dd = float(input("Ingrese la latitud en grados decimales: "))
        lon_dd = float(input("Ingrese la longitud en grados decimales: "))
        lat_dms = dd_to_dms(lat_dd)
        lat_dir = "N" if lat_dd >= 0 else "S"
        lon_dms = dd_to_dms(lon_dd)
        lon_dir = "E" if lon_dd >= 0 else "W"
        print(f"Latitud: {lat_dms[0]}° {lat_dms[1]}' {lat_dms[2]:.4f}\" {lat_dir}")
        print(f"Longitud: {lon_dms[0]}° {lon_dms[1]}' {lon_dms[2]:.4f}\" {lon_dir}")

    elif option == "2":
        lat_grados = int(input("Ingrese la latitud en grados: "))
        lat_minutos = int(input("Ingrese los minutos de la latitud: "))
        lat_segundos = float(input("Ingrese los segundos de la latitud: "))
        lat_dir = input("Ingrese la dirección de la latitud (N/S): ").upper()
        lon_grados = int(input("Ingrese la longitud en grados: "))
        lon_minutos = int(input("Ingrese los minutos de la longitud: "))
        lon_segundos = float(input("Ingrese los segundos de la longitud: "))
        lon_dir = input("Ingrese la dirección de la longitud (E/W): ").upper()
        lat_dd = dms_to_dd(lat_grados, lat_minutos, lat_segundos, lat_dir)
        lon_dd = dms_to_dd(lon_grados, lon_minutos, lon_segundos, lon_dir)
        print(f"Latitud: {lat_dd:.6f}° {lat_dir}")
        print(f"Longitud: {lon_dd:.6f}° {lon_dir}") 

    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()