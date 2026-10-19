def calcular_precio_con_descuento(precio, porcentaje_descuento):
    """Calcula precio final con descuento e IVA"""

    def aplicar_descuento(p, descuento):
        """Función auxiliar interna"""
        return p * (1 - descuento / 100)

    def aplicar_iva(p):
        """Función auxiliar interna"""
        return p * 1.21

    # Usar las funciones internas
    precio_con_descuento = aplicar_descuento(precio, porcentaje_descuento)
    precio_final = aplicar_iva(precio_con_descuento)

    return precio_final

print(calcular_precio_con_descuento(100, 10))  # 108.9

# print(aplicar_iva(9)) # No reconoce la función fuera del ámbito 