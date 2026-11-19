# Trazabilidad del ejercicio 6

## Punto de partida

- Rama de trabajo: `ejercicio-6-amos-solucion`, creada desde `main` en `f81ea6b`.
- `origin` apunta a `git@github.com:amosnava/iac-ia-lab-formacion.git`.
- La guía indica crear la rama desde el ejercicio 5 o desde `main` si ya se fusionó; se usó `main`, donde consta el merge del ejercicio 5.
- No había entradas en `git stash list`. Se intentó `git stash push -m "respaldo-antes-ejercicio-6-amos-solucion"` con el árbol limpio; Git respondió `No local changes to save`. No se creó ni alteró ningún stash.

## Implementación local

- Se creó `politica_plan.py` en la raíz. Lee JSON de stdin y comprueba las direcciones, tipos, acciones, nombres y entornos requeridos, además de valores ausentes, desconocidos o sensibles.
- Se modificó `.github/workflows/validacion.yml`: `tofu_wrapper: false`, planes guardados como `plan-predeterminado.tfplan` y `plan-integracion.tfplan`, un paso de política tras cada plan y dos filas nuevas en el resumen.
- Se verificó que cada nombre de `-out` coincide con su `-plan` y que `.gitignore` excluye `*.tfplan`.
- Se añadió en `README.md` la sección `Política del laboratorio`, explicando la regla, la diferencia entre `validate` y la política y sus límites.
- El archivo solicitado en el paso anterior, `TRAZABILIDAD_6/registro_ejercicio_5.md`, se conserva sin cambios.

## Publicaciones y ejecuciones

- Commit inicial: `dbb26254ab5de368239fcd55f6aeaa2a23dd4059` (`Ejercicio 6: política sobre el plan`), publicado en `origin/ejercicio-6-amos-solucion`.
- La ejecución inicial de Actions [44511608851](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44511608851) terminó en `success`. Formato, validación, los dos planes, las dos políticas, resumen y publicación de evidencia pasaron.
- Artefacto de evidencia: `evidencia-iac-44511608851-1`, con retención hasta el 26-11-2026. Los planes `.tfplan` no se publicaron como artefactos.

## Ensayo controlado de entornos distintos

- Se cambió únicamente `module.ayuda.entorno` de `var.entorno` a `"desarrollo"`; `module.portal` conserva `var.entorno` (`"pruebas"` por defecto).
- Predicción: formato, `tofu validate` y el plan predeterminado pasan; la política predeterminada rechaza el plan con `POLÍTICA RECHAZADA: portal y ayuda deben pertenecer al mismo entorno`. Al fallar ese paso, plan y política de integración se omiten; resumen y evidencia se ejecutan por `always()`.
- Commit y ejecución roja: pendientes de publicación y comprobación.

## Corrección, entrega y PR

- Corrección y ejecución verde: pendientes.
- Pull request: pendiente.

No se ejecutó OpenTofu localmente, `apply` ni `destroy`. Las comprobaciones de planes y política se realizarán en GitHub Actions, sin publicar los archivos temporales `.tfplan` como artefactos.
