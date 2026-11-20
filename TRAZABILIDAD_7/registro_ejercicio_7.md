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
- Los resultados de la ejecución verde inicial y de la prueba temporal de `informes` se documentan a continuación.

## Publicaciones y ejecuciones

- Commit inicial: `d07ad5eeeb2ce32040c1349082f021dad4554b63` (`Ejercicio 7: catalogo de fichas reutilizable`), publicado en `origin/ejercicio-7-amos-solucion`.
- Actions [44708522723](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44708522723) terminó en `success`. Formato, validación, los dos planes y las dos políticas pasaron.
- Artefacto: `evidencia-iac-44708522723-1`, con retención hasta el 27-11-2026.

## Ensayo controlado: tercera ficha

- Se añadió temporalmente `informes = "portal-informes"` al catálogo de `main.tf`.
- Commit de prueba: `64620ad7bebb09e973497a091b478fa2e8f96cd9` (`Prueba: tercera ficha sin aprobar`), publicado en la rama del ejercicio.
- Actions [44708845840](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44708845840) terminó en `failure`. Formato, validación y plan predeterminado pasaron; la política predeterminada falló; ambos pasos de integración se omitieron; resumen y evidencia terminaron en éxito.
- Artefacto: `evidencia-iac-44708845840-1`, con retención hasta el 27-11-2026.
- El rechazo se produce porque la política permite exactamente las dos direcciones del catálogo `portal` y `ayuda`; el mensaje implementado es `POLÍTICA RECHAZADA: se esperan exactamente las fichas portal y ayuda`.
- Revisión asistida por IA contrastada con el plan: `for_each` incorpora la clave del mapa a cada dirección, y añadir `informes` crea una tercera instancia; la expresión `for` de la salida solo reorganiza resultados, no amplía lo que autoriza la política.
- Tras la ejecución roja, se retiró la línea `informes`; queda pendiente publicar la corrección.

## Incidencias de formato y corrección

- El commit de corrección `0bc9bb77047318e29250239351e35697109a5a09` restauró las dos claves, pero Actions [44709199191](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44709199191) falló primero en `Comprobar formato`; validación, planes y políticas quedaron omitidos. Resumen y evidencia sí terminaron.
- El primer intento de corregir el formato no fue suficiente: Actions [44709437910](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44709437910) también falló en `Comprobar formato`. OpenTofu no está instalado localmente y no se instaló software.
- La revisión posterior identificó que `main.tf` conservaba el espaciado alineado para la clave larga `informes` después de retirarla. Se vuelve a alinear el mapa de dos entradas y se restaura en `outputs.tf` el formato de la salida que ya estaba presente en la base.
- Commit de corrección final: `ffa159a92588fa653e094e81352c92b04f12b84d` (`Correccion: alinear mapa de dos fichas`), publicado en la rama.
- Actions [44709636310](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44709636310) terminó en `success`: formato, validación, ambos planes y ambas políticas pasaron.
- Artefacto: `evidencia-iac-44709636310-1`, con retención hasta el 27-11-2026.

## README y PR

- Se añadió la sección `Catálogo de fichas` al README y se actualizaron las direcciones citadas en `Política del laboratorio`.
- Commit documental: `ff4d1c7704462eed51d3e217f74913eb0e68bb4d` (`Ejercicio 7: documentar catalogo de fichas`), publicado en la rama.
- Actions [44709884322](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44709884322) terminó en `success`: formato, validación, ambos planes, ambas políticas, resumen y evidencia pasaron.
- Artefacto: `evidencia-iac-44709884322-1`, con retención hasta el 27-11-2026.
- Diff neto revisado contra `main`: `main.tf`, `outputs.tf`, `politica_plan.py`, `README.md` y este registro. La prueba temporal no cambia el estado final del catálogo.
- El PR está pendiente: no hay herramienta GitHub con permisos de escritura disponible en esta sesión. El enlace para abrirlo manualmente es https://github.com/amosnava/iac-ia-lab-formacion/pull/new/ejercicio-7-amos-solucion .

No ejecutar OpenTofu localmente, `apply` ni `destroy`. Los planes y las políticas se comprobarán en GitHub Actions; los `.tfplan` son temporales y no deben publicarse como artefactos.
