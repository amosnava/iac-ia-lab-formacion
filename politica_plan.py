import json
import sys


DIRECCIONES_ESPERADAS = {
    'module.fichas["portal"].terraform_data.ficha',
    'module.fichas["ayuda"].terraform_data.ficha',
}
ENTORNOS_PERMITIDOS = {"desarrollo", "pruebas", "integracion"}
CAMPOS_PERMITIDOS = {"nombre", "entorno", "etiquetas"}
ETIQUETAS_PERMITIDAS = {"proyecto", "entorno", "responsable"}
RESPONSABLE_POR_ENTORNO = {
    "desarrollo": "equipo-lab",
    "pruebas": "equipo-lab",
    "integracion": "equipo-integracion",
}


def rechazar(motivo):
    print(f"POLÍTICA RECHAZADA: {motivo}")
    raise SystemExit(1)


def contiene_true(valor):
    if valor is True:
        return True
    if isinstance(valor, dict):
        return any(contiene_true(elemento) for elemento in valor.values())
    if isinstance(valor, list):
        return any(contiene_true(elemento) for elemento in valor)
    return False


def esta_marcado(metadatos, campo):
    if metadatos is True:
        return True
    if not isinstance(metadatos, dict):
        return False
    entradas = metadatos.get("input", {})
    if entradas is True:
        return True
    if isinstance(entradas, dict):
        return contiene_true(entradas.get(campo, {}))
    return contiene_true(entradas)


try:
    plan = json.load(sys.stdin)
except (json.JSONDecodeError, UnicodeDecodeError):
    rechazar("la entrada estándar no contiene JSON válido")
except OSError:
    rechazar("no se pudo leer el JSON de la entrada estándar")

if not isinstance(plan, dict):
    rechazar("el documento JSON raíz debe ser un objeto")
if "resource_changes" not in plan:
    rechazar("falta resource_changes")

cambios = plan["resource_changes"]
if not isinstance(cambios, list):
    rechazar("resource_changes debe ser una lista")
if len(cambios) != 2:
    rechazar("se esperan exactamente las fichas portal y ayuda")

por_direccion = {}
for recurso in cambios:
    if not isinstance(recurso, dict):
        rechazar("cada elemento de resource_changes debe ser un objeto")

    direccion = recurso.get("address")
    if not isinstance(direccion, str):
        rechazar("la dirección del recurso debe ser una cadena")
    if direccion not in DIRECCIONES_ESPERADAS:
        rechazar(f"dirección de recurso no permitida: {direccion}")
    if direccion in por_direccion:
        rechazar(f"dirección duplicada: {direccion}")
    if recurso.get("mode") != "managed":
        rechazar(f"{direccion}: el recurso debe ser managed")
    if recurso.get("type") != "terraform_data":
        rechazar(f"{direccion}: el tipo debe ser terraform_data")

    cambio = recurso.get("change")
    if not isinstance(cambio, dict):
        rechazar(f"{direccion}: falta el objeto change")
    if cambio.get("actions") != ["create"]:
        rechazar(f"{direccion}: la única acción permitida es create")

    after = cambio.get("after")
    if not isinstance(after, dict):
        rechazar(f"{direccion}: falta change.after")
    entradas = after.get("input")
    if not isinstance(entradas, dict):
        rechazar(f"{direccion}: change.after.input debe ser un objeto")

    campos_extra = set(entradas) - CAMPOS_PERMITIDOS
    if campos_extra:
        rechazar(f"{direccion}: input contiene campos no permitidos")
    campos_faltantes = CAMPOS_PERMITIDOS - set(entradas)
    if campos_faltantes:
        rechazar(f"{direccion}: input no contiene todos los campos requeridos")

    desconocidos = cambio.get("after_unknown", {})
    sensibles = cambio.get("after_sensitive", {})
    if not isinstance(desconocidos, dict) and desconocidos is not True:
        rechazar(f"{direccion}: after_unknown tiene una estructura inválida")
    if not isinstance(sensibles, dict) and sensibles is not True:
        rechazar(f"{direccion}: after_sensitive tiene una estructura inválida")

    valores = {}
    for campo in ("nombre", "entorno", "etiquetas"):
        if esta_marcado(desconocidos, campo):
            rechazar(f"{direccion}: el valor {campo} es desconocido")
        if esta_marcado(sensibles, campo):
            rechazar(f"{direccion}: el valor {campo} está marcado como sensible")
        valores[campo] = entradas[campo]

    for campo in ("nombre", "entorno"):
        if not isinstance(valores[campo], str):
            rechazar(f"{direccion}: el valor {campo} debe ser una cadena conocida")

    etiquetas = valores["etiquetas"]
    if not isinstance(etiquetas, dict):
        rechazar(f"{direccion}: etiquetas debe ser un objeto")
    if set(etiquetas) != ETIQUETAS_PERMITIDAS:
        rechazar(f"{direccion}: etiquetas debe contener proyecto, entorno y responsable")
    for campo in ETIQUETAS_PERMITIDAS:
        if not isinstance(etiquetas[campo], str):
            rechazar(f"{direccion}: la etiqueta {campo} debe ser una cadena conocida")

    if not valores["nombre"].startswith("portal-"):
        rechazar(f"{direccion}: el nombre debe comenzar por portal-")
    if direccion == 'module.fichas["ayuda"].terraform_data.ficha':
        if valores["nombre"] != "portal-ayuda":
            rechazar("la ficha de ayuda debe llamarse portal-ayuda")
    if valores["entorno"] not in ENTORNOS_PERMITIDOS:
        rechazar(f"{direccion}: entorno no permitido: {valores['entorno']}")
    if etiquetas["proyecto"] != "nexo-portal":
        rechazar(f"{direccion}: proyecto debe ser nexo-portal")
    if etiquetas["entorno"] != valores["entorno"]:
        rechazar(f"{direccion}: la etiqueta entorno debe coincidir con el entorno de la ficha")
    responsable_esperado = RESPONSABLE_POR_ENTORNO[valores["entorno"]]
    if etiquetas["responsable"] != responsable_esperado:
        rechazar(f"responsable no aprobado para {valores['entorno']}")

    por_direccion[direccion] = valores

if set(por_direccion) != DIRECCIONES_ESPERADAS:
    rechazar("las direcciones no coinciden con las dos fichas esperadas")

entorno_portal = por_direccion['module.fichas["portal"].terraform_data.ficha']["entorno"]
entorno_ayuda = por_direccion['module.fichas["ayuda"].terraform_data.ficha']["entorno"]
if entorno_portal != entorno_ayuda:
    rechazar("portal y ayuda deben pertenecer al mismo entorno")

print("POLÍTICA APROBADA: dos fichas con etiquetas y responsable ficticios correctos")
