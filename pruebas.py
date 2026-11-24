productos = [
    ("SKU-0001", "Tarima de madera estándar", 120),
    ("SKU-0002", "Caja corrugada", 450),
    ("SKU-0003", "Película stretch industrial reforzada", 35),
    ("SKU-0004", "Etiqueta térmica", 2000),
]


def recortar_nombre(nombre, largo=15):
    """Devuelve el nombre tal cual si cabe; si no, lo recorta y agrega '...'."""
    if len(nombre) <= largo:
        return nombre
    return nombre[:largo - 2] + '...'


def imprimir_tabla(productos):
    print(f"{'SKU':<10} {'Nombre':<15} {'Cantidad':>8}")
    print("-" * 35)
    for sku, nombre, cantidad in productos:
        print(f"{sku:<10} {recortar_nombre(nombre):<15} {cantidad:>8}")


# Este bloque solo se ejecuta si corres "python pruebas.py" directamente,
# NO cuando otro archivo hace "import pruebas" (como el archivo de pruebas).
if __name__ == "__main__":
    imprimir_tabla(productos)
