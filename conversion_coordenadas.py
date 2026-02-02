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
        print("\n--- DATOS DE LATITUD ---")
        lat_g = int(input("Grados: "))
        lat_m = int(input("Minutos: "))
        lat_s = float(input("Segundos: "))
        lat_d = input("Dirección (N/S): ")

        print("\n--- DATOS DE LONGITUD ---")
        lon_g = int(input("Grados: "))
        lon_m = int(input("Minutos: "))
        lon_s = float(input("Segundos: "))
        lon_d = input("Dirección (E/W): ")

        lat_final = dms_to_dd(lat_g, lat_m, lat_s, lat_d)
        lon_final = dms_to_dd(lon_g, lon_m, lon_s, lon_d)

        print(f"\n✅ RESULTADO DECIMAL:")
        print(f" Latitud:  {lat_final:.6f}°")
        print(f" Longitud: {lon_final:.6f}°")

    else:
        print("\n Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

   
    