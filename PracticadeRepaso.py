class Pasajero:
    def __init__(self, dni, nombre_completo, edad, peso_equipaje, ruta):
        # Se usan los setters para validar los datos desde la instanciación [cite: 41]
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.peso_equipaje = peso_equipaje
        self.ruta = ruta

    # --- Properties para Atributos Privados ---

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        # Valida exactamente 8 dígitos numéricos [cite: 179, 183]
        if not (isinstance(valor, str) and len(valor) == 8 and valor.isdigit()):
            raise ValueError("DNI inválido: Debe tener exactamente 8 dígitos numéricos.")
        self.__dni = valor

    @property
    def nombre_completo(self):
        return self.__nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, valor):
        # Elimina espacios, aplica formato título y valida longitud mínima [cite: 179, 184, 185]
        formateado = valor.strip().title()
        if len(formateado) < 5:
            raise ValueError("Nombre inválido: Debe tener al menos 5 caracteres.")
        self.__nombre_completo = formateado

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        # Valida que sea entero entre 0 y 120 [cite: 180, 186]
        if not isinstance(valor, int) or not (0 <= valor <= 120):
            raise ValueError("Edad inválida: Debe ser un entero entre 0 y 120.")
        self.__edad = valor

    @property
    def peso_equipaje(self):
        return self.__peso_equipaje

    @peso_equipaje.setter
    def peso_equipaje(self, valor):
        # Valida rango de 0 a 25 kg [cite: 181, 191]
        if not (0 <= valor <= 25):
            raise ValueError("Peso de equipaje inválido: El rango permitido es de 0 a 25 kg.")
        self.__peso_equipaje = float(valor)

    @property
    def ruta(self):
        return self.__ruta

    @ruta.setter
    def ruta(self, valor):
        # Valida rutas permitidas [cite: 182, 192]
        opciones = ["Iquitos-Nauta", "Iquitos-Yurimaguas", "Iquitos-Pucallpa", "Iquitos-Sta. Rosa"]
        if valor not in opciones:
            raise ValueError(f"Ruta no permitida. Opciones válidas: {opciones}")
        self.__ruta = valor

    # --- Properties Calculadas (Solo Lectura) ---

    @property
    def categoria_edad(self):
        # Clasificación según rango de edad [cite: 194]
        if self.edad < 12: return "Niño"
        if self.edad <= 17: return "Adolescente"
        if self.edad <= 59: return "Adulto"
        return "Adulto mayor"

    @property
    def tarifa_base(self):
        # Tarifa según destino [cite: 195]
        tarifas = {
            "Iquitos-Nauta": 25.0,
            "Iquitos-Sta. Rosa": 80.0,
            "Iquitos-Yurimaguas": 120.0,
            "Iquitos-Pucallpa": 180.0
        }
        return tarifas.get(self.ruta, 0.0)

    @property
    def recargo_equipaje(self):
        # S/. 2 por cada kg que exceda los 15 kg [cite: 196, 197]
        exceso = self.peso_equipaje - 15
        return max(0, exceso * 2)

    @property
    def tarifa_total(self):
        # 50% de descuento en tarifa base para Niños y Adultos mayores [cite: 198]
        t_base = self.tarifa_base
        if self.categoria_edad in ["Niño", "Adulto mayor"]:
            t_base *= 0.5
        return t_base + self.recargo_equipaje

    def __str__(self):
        # Boleta legible con desglose de costos [cite: 201]
        return (
            f"\n--- BOLETA DE PASAJE ---"
            f"\nPasajero: {self.nombre_completo} (DNI: {self.dni})"
            f"\nEdad: {self.edad} años ({self.categoria_edad})"
            f"\nRuta: {self.ruta}"
            f"\nEquipaje: {self.peso_equipaje} kg"
            f"\n------------------------"
            f"\nTarifa Base:    S/. {self.tarifa_base:>6.2f}"
            f"\nRecargo Equip.: S/. {self.recargo_equipaje:>6.2f}"
            f"\nTOTAL A PAGAR:  S/. {self.tarifa_total:>6.2f}"
            f"\n------------------------"
        )

# --- Pruebas Obligatorias ---
if __name__ == "__main__":
    try:
        print("1. Registro de pasajero válido:")
        p1 = Pasajero("45678912", "  juan perez  ", 65, 20.0, "Iquitos-Yurimaguas")
        print(p1)

        print("\n2. Registro de pasajero con descuento (Niño):")
        p2 = Pasajero("77889900", "LUCIA RAMIREZ", 8, 10.0, "Iquitos-Nauta")
        print(p2)

        print("\n3. Intento de DNI inválido (Letras):")
        p_error = Pasajero("45678A12", "Error DNI", 30, 5, "Iquitos-Nauta")
    except ValueError as e:
        print(f"CAPTURA DE ERROR: {e}")

    try:
        print("\n4. Intento de Ruta inexistente:")
        p_error2 = Pasajero("12345678", "Ruta Mal", 25, 5, "Iquitos-Lima")
    except ValueError as e:
        print(f"CAPTURA DE ERROR: {e}")