#t95 vs maus
#eleccion de municion (apcr, he, heat)
#posibilidad de critico
#posibilidad de one-shot
#eleccion de zona de impacto (torreta, escotilla, transmision, chasis)

import random

# Tipos de munición disponibles
MUNICIONES = {
    "APCR": {"penetracion": 310, "daño": 750, "critico": 0.2},
    "HEAT": {"penetracion": 330, "daño": 700, "critico": 0.25},
    "HE": {"penetracion": 80, "daño": 950, "critico": 0.5},
}

# Puntos de impacto
PUNTOS_IMPACTO = {
    "transmision": {"mod_blindaje": 0.7, "critico": 0.15, "one_shot": False},
    "torreta": {"mod_blindaje": 1.0, "critico": 0.2, "one_shot": False},
    "escotilla": {"mod_blindaje": 0.5, "critico": 0.3, "one_shot": False},
    "chasis": {"mod_blindaje": 0.8, "critico": 0.1, "one_shot": True},
}

# Clase del tanque
class Tanque:
    def __init__(self, nombre, blindaje_base, puntos_vida):
        self.nombre = nombre
        self.blindaje_base = blindaje_base
        self.puntos_vida = puntos_vida

    def recibir_disparo(self, tipo_municion, punto_objetivo):
        municion = MUNICIONES[tipo_municion.upper()]
        impacto = PUNTOS_IMPACTO[punto_objetivo]

        blindaje_efectivo = self.blindaje_base * impacto["mod_blindaje"]
        penetracion = municion["penetracion"]
        daño = 0

        print(f"\n{self.nombre} recibe disparo en {punto_objetivo.replace('_', ' ')} (Blindaje efectivo: {blindaje_efectivo:.0f})")

        if penetracion > blindaje_efectivo:
            daño = municion["daño"]

            # Crítico
            if random.random() < (municion["critico"] + impacto["critico"]):
                daño *= 2
                print("💥 ¡Daño crítico!")

            # One-shot (explosión de munición)
            if impacto["one_shot"] and random.random() < 0.1:
                print("💣 ¡Impacto en compartimento de munición! Tanque destruido instantáneamente.")
                self.puntos_vida = 0
                return True
        else:
            print("🛡️ ¡El disparo rebotó! No hizo daño.")
            return False

        self.puntos_vida -= daño
        print(f"💥 {self.nombre} recibió {daño} de daño. Vida restante: {self.puntos_vida}")
        return self.puntos_vida <= 0

# Elegir munición
def elegir_municion(nombre_tanque):
    while True:
        print(f"\n🔫 {nombre_tanque} - Tipos de munición disponibles:")
        for tipo, stats in MUNICIONES.items():
            print(f" {tipo}: Penetración={stats['penetracion']} | Daño={stats['daño']} | Crítico={int(stats['critico']*100)}%")
        eleccion = input("Elige munición (APCR / HEAT / HE): ").upper()
        if eleccion in MUNICIONES:
            return eleccion
        print("❌ Tipo inválido.")

# Elegir punto de impacto
def elegir_punto_impacto():
    while True:
        print("\n🎯 Puntos disponibles para disparar:")
        for punto in PUNTOS_IMPACTO:
            print(f" {punto.replace('_', ' ')}")
        eleccion = input("Elige el punto donde disparar: ").lower().replace(" ", "_")
        if eleccion in PUNTOS_IMPACTO:
            return eleccion
        print("❌ Punto inválido.")

# Inicializar tanques
t95 = Tanque("T95", blindaje_base=305, puntos_vida=2000)
maus = Tanque("Maus", blindaje_base=240, puntos_vida=3000)

# Combate por turnos
turno = 1
while t95.puntos_vida > 0 and maus.puntos_vida > 0:
    print(f"\n===== TURNO {turno} =====")

    # T95 dispara
    print("\n👉 Turno del T95")
    municion_t95 = elegir_municion("T95")
    punto_t95 = elegir_punto_impacto()
    if maus.recibir_disparo(municion_t95, punto_t95):
        print("\n✅ ¡El Maus ha sido destruido! Gana el T95.")
        break

    # Maus dispara
    print("\n👉 Turno del Maus")
    municion_maus = elegir_municion("Maus")
    punto_maus = elegir_punto_impacto()
    if t95.recibir_disparo(municion_maus, punto_maus):
        print("\n✅ ¡El T95 ha sido destruido! Gana el Maus.")
        break

    turno += 1
