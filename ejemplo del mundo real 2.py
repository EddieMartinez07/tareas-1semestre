class Hotel:
    def __init__(self, nombre):
        # Inicialización de la clase Hotel con un nombre y una lista de habitaciones
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, numero, tipo, precio):
        # Método para agregar una habitación al hotel
        habitacion = Habitacion(numero, tipo, precio)
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        # Método para mostrar las habitaciones disponibles en el hotel
        print(f"\nHabitaciones disponibles en {self.nombre}:")
        for habitacion in self.habitaciones:
            if not habitacion.reservada:
                print(habitacion)

    def realizar_reserva(self, numero_habitacion, cliente, noches):
        # Método para realizar una reserva en una habitación específica
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion and not habitacion.reservada:
                habitacion.reservar(cliente, noches)
                print(f"\nReserva realizada con éxito:\n{habitacion}")
                return
        print("\nLo sentimos, la habitación no está disponible para reserva.")


class Habitacion:
    def __init__(self, numero, tipo, precio):
        # Inicialización de la clase Habitacion con número, tipo, precio, etc.
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False
        self.cliente = None
        self.noches = 0

    def reservar(self, cliente, noches):
        # Método para reservar la habitación con un cliente y número de noches
        self.reservada = True
        self.cliente = cliente
        self.noches = noches

    def __str__(self):
        # Método especial para representar la habitación como una cadena
        estado_reserva = "Reservada" if self.reservada else "Disponible"
        return f"Habitación {self.numero} ({self.tipo}) - Precio: ${self.precio}/noche - Estado: {estado_reserva}"


# Ejemplo de uso del sistema de reservas
hotel_ejemplo = Hotel("Ejemplo Hotel")
hotel_ejemplo.agregar_habitacion(101, "Doble", 150)
hotel_ejemplo.agregar_habitacion(102, "Individual", 100)
hotel_ejemplo.agregar_habitacion(103, "Suite", 200)

hotel_ejemplo.mostrar_habitaciones_disponibles()

hotel_ejemplo.realizar_reserva(102, "John Doe", 3)
hotel_ejemplo.realizar_reserva(101, "Jane Doe", 2)

hotel_ejemplo.mostrar_habitaciones_disponibles()
