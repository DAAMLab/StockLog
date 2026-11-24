productos = [
    ("SKU-0001", "Tarima de madera estándar", 120),
    ("SKU-0002", "Caja corrugada", 450),
    ("SKU-0003", "Película stretch industrial reforzada", 35),
    ("SKU-0004", "Etiqueta térmica", 2000),
]

print(f"{'SKU':<10} {'Nombre':<15} {'Cantidad':>8}")
print("-" * 35)


for sku, nombre, cantidad in productos:
    contenido = nombre if len(nombre) <= 15 else nombre[:12]+'...'
    print(f"{sku:<10} {contenido:<15} {cantidad:>8}")