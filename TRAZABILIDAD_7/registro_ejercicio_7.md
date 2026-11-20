# Trazabilidad del ejercicio 7

## Punto de control

- Repositorio personal: `amosnava/iac-ia-lab-formacion`; `origin` usa `git@github.com:amosnava/iac-ia-lab-formacion.git`.
- La rama del ejercicio 6 estaba limpia en `6e8f0b049cb9921ee353ef82f250077b3ef6a9ea`.
- La ejecución verde anterior fue [Actions 44513471238](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44513471238), sobre ese commit. Formato, validación, los dos planes y las dos políticas pasaron.
- La guía denomina la rama `catalogo-ejercicio-7`; por petición del usuario se creó `ejercicio-7-amos-solucion` desde la rama del ejercicio 6.
- No había entradas en `git stash list`; no se modificó ningún stash.

## Implementación inicial

- En `main.tf`, se sustituyeron las dos llamadas al módulo por el local `catalogo` con claves `portal` y `ayuda`, y una única llamada a `module "fichas"` con `for_each`.
- En `outputs.tf`, `resumen` se construye con una expresión `for` que conserva las claves de `module.fichas`.
- En `politica_plan.py`, se actualizaron las dos direcciones permitidas y la identificación de ayuda. Se mantuvieron las reglas existentes y el rechazo de recuento ahora informa `se esperan exactamente las fichas portal y ayuda`.
- No se modificó `modulo_ficha/` ni el workflow.
- Primera ejecución verde, prueba temporal de `informes`, corrección y README: pendientes.

## Publicaciones y ejecuciones

- Commit verde inicial: pendiente.
- Prueba roja de tercera ficha: pendiente.
- Corrección y nueva ejecución verde: pendientes.
- README y comprobación final: pendientes.
- Pull request: pendiente.

No ejecutar OpenTofu localmente, `apply` ni `destroy`. Los planes y las políticas se comprobarán en GitHub Actions; los `.tfplan` son temporales y no deben publicarse como artefactos.
