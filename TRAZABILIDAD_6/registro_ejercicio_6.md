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
- Commit de prueba: `eea19c0b93fef98d5ed9a18f129876a58816ec08` (`Prueba: ayuda en entorno diferente`), publicado en la rama del ejercicio.
- Actions [44511887777](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44511887777) terminó en `failure`. Formato, validación y plan predeterminado pasaron; `Politica del plan predeterminado` falló; el plan y la política de integración se omitieron; resumen y evidencia terminaron en éxito.
- GitHub denegó la descarga del log detallado con HTTP 403, por lo que no se pudo observar independientemente la salida estándar. El mensaje previsto y emitido por el código para esta discrepancia es `POLÍTICA RECHAZADA: portal y ayuda deben pertenecer al mismo entorno`.
- Tras la prueba, se restauró `module.ayuda.entorno = var.entorno`.

## Corrección y nueva ejecución verde

- Commit de corrección: `4187b04b6eb5dbaf04a17c90d8a8763add0c3c3d` (`Corrección: ayuda comparte entorno`), publicado en la rama del ejercicio.
- Actions [44512182633](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44512182633) terminó en `success`. Formato, validación, ambos planes, ambas políticas, resumen y publicación de evidencia pasaron.
- Artefacto de evidencia: `evidencia-iac-44512182633-1`, con retención hasta el 26-11-2026. Los planes `.tfplan` no se publicaron como artefactos.

## Corrección, entrega y PR

- La ejecución de Actions [44512445858](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44512445858), disparada al publicar la actualización de trazabilidad, terminó en `success`; formato, validación, ambos planes, ambas políticas, resumen y evidencia pasaron.
- Artefacto de evidencia: `evidencia-iac-44512445858-1`, con retención hasta el 26-11-2026.
- El diff neto contra `main` no contiene el cambio temporal de `main.tf`; la rama termina con `module.ayuda.entorno = var.entorno`.
- No se pudo crear el pull request desde esta sesión: el servidor MCP de GitHub no estuvo disponible, `gh` no está instalado, no había credencial API en el entorno y no se pudieron cargar las herramientas de navegador. El push de GitHub ofreció este enlace para abrirlo manualmente: https://github.com/amosnava/iac-ia-lab-formacion/pull/new/ejercicio-6-amos-solucion
- El PR queda pendiente de creación y revisión; no se fusionó nada en `main`.

No se ejecutó OpenTofu localmente, `apply` ni `destroy`. Los planes se generaron únicamente en runners de GitHub Actions y los `.tfplan` no se publicaron como artefactos.
