import json
import sys


DIRECCIONES_ESPERADAS = {
    "module.portal.terraform_data.ficha",
    "module.ayuda.terraform_data.ficha",
}
ENTORNOS_PERMITIDOS = {"desarrollo", "pruebas", "integracion"}
CAMPOS_PERMITIDOS = {"nombre", "entorno"}


def rechazar(motivo):
    print(f"POLÍTICA RECHAZADA: {motivo}")
    raise SystemExit(1)


def esta_marcado(metadatos, campo):
    nodo = metadatos
    for clave in ("input", campo):
        if nodo is True:
            return True
        if not isinstance(nodo, dict):
            return False
        nodo = nodo.get(clave)
    return nodo is True


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
    rechazar("debe haber exactamente dos cambios")

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

    desconocidos = cambio.get("after_unknown", {})
    sensibles = cambio.get("after_sensitive", {})
    if not isinstance(desconocidos, dict) and desconocidos is not True:
        rechazar(f"{direccion}: after_unknown tiene una estructura inválida")
    if not isinstance(sensibles, dict) and sensibles is not True:
        rechazar(f"{direccion}: after_sensitive tiene una estructura inválida")

    valores = {}
    for campo in ("nombre", "entorno"):
        if esta_marcado(desconocidos, campo):
            rechazar(f"{direccion}: el valor {campo} es desconocido")
        if esta_marcado(sensibles, campo):
            rechazar(f"{direccion}: el valor {campo} está marcado como sensible")
        if campo not in entradas:
            rechazar(f"{direccion}: falta el valor {campo}")
        if not isinstance(entradas[campo], str):
            rechazar(f"{direccion}: el valor {campo} debe ser una cadena conocida")
        valores[campo] = entradas[campo]

    if not valores["nombre"].startswith("portal-"):
        rechazar(f"{direccion}: el nombre debe comenzar por portal-")
    if direccion == "module.ayuda.terraform_data.ficha":
        if valores["nombre"] != "portal-ayuda":
            rechazar("la ficha de ayuda debe llamarse portal-ayuda")
    if valores["entorno"] not in ENTORNOS_PERMITIDOS:
        rechazar(f"{direccion}: entorno no permitido: {valores['entorno']}")

    por_direccion[direccion] = valores

if set(por_direccion) != DIRECCIONES_ESPERADAS:
    rechazar("las direcciones no coinciden con las dos fichas esperadas")

entorno_portal = por_direccion["module.portal.terraform_data.ficha"]["entorno"]
entorno_ayuda = por_direccion["module.ayuda.terraform_data.ficha"]["entorno"]
if entorno_portal != entorno_ayuda:
    rechazar("portal y ayuda deben pertenecer al mismo entorno")

print("POLÍTICA APROBADA: dos fichas ficticias, mismo entorno y sin operaciones reales")
