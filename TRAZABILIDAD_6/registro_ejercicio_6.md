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

- Commits del ejercicio 6: pendientes.
- Publicación de la rama: pendiente.
- Ejecución inicial verde: pendiente.
- Prueba controlada roja: pendiente.
- Corrección y ejecución verde: pendientes.
- Pull request: pendiente.

No se ejecutó OpenTofu localmente, `apply` ni `destroy`. Las comprobaciones de planes y política se realizarán en GitHub Actions, sin publicar los archivos temporales `.tfplan` como artefactos.
