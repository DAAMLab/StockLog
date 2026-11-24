# pytest busca automáticamente archivos que empiecen con "test_"
# y dentro de ellos, funciones que empiecen con "test_".

from pruebas import recortar_nombre, imprimir_tabla


def test_nombre_corto_no_se_modifica():
    assert recortar_nombre("Caja corrugada") == "Caja corrugada"


def test_nombre_de_exactamente_15_no_se_recorta():
    nombre = "A" * 15
    assert recortar_nombre(nombre) == nombre


def test_nombre_largo_se_recorta_con_puntos():
    assert recortar_nombre("Tarima de madera estándar") == "Tarima de ma..."


def test_nombre_recortado_mide_15():
    resultado = recortar_nombre("Película stretch industrial reforzada")
    assert len(resultado) == 15


def test_largo_personalizado():
    assert recortar_nombre("Etiqueta térmica", largo=8) == "Etiqu..."


def test_tabla_imprime_todos_los_productos(capsys):
    # capsys es una herramienta de pytest que "atrapa" lo que se imprime
    productos = [("SKU-1", "Caja", 5), ("SKU-2", "Tarima", 10)]
    imprimir_tabla(productos)
    salida = capsys.readouterr().out
    assert "SKU-1" in salida
    assert "SKU-2" in salida
