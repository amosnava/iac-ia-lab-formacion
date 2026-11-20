# Trazabilidad del ejercicio 8 con skill

## Punto de partida

- Repositorio: `amosnava/iac-ia-lab-formacion`; `origin` apunta a la copia personal.
- El PR [#5](https://github.com/amosnava/iac-ia-lab-formacion/pull/5) del ejercicio 8 ya se fusionó en `main` con el commit `525938b`; Actions [44731490528](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44731490528) pasó.
- Para repetir el ejercicio desde su punto de partida anterior, se creó `ejercicio-8-amos-solucion-con-skill` desde `origin/ejercicio-7-amos-solucion`, commit `c7ee93ae8f51f6492813b7c9b005f28a8e86b804`, no desde `main`, que ya incluye el ejercicio 8.
- La rama del ejercicio 7 tenía dos commits locales de personalización fuera del remoto; se excluyeron. El árbol estaba limpio al crear la nueva rama.
- El usuario solicita usar una skill de proyecto y guardar la trazabilidad en esta carpeta.

## Registro de operaciones

| Fecha/hora | Acción | Resultado |
| --- | --- | --- |
| 2026-11-20 13:26 +0100 | Revisar rama actual, estado, `origin`, PR #5, ejecución de `main` y existencia de skills previas. | Confirmado el merge del ejercicio 8, la ejecución verde y que no existía una skill de proyecto ni una carpeta `TRAZABILIDAD_8_SKILL`. |
| 2026-11-20 13:27 +0100 | Crear `ejercicio-8-amos-solucion-con-skill` desde `origin/ejercicio-7-amos-solucion`. | Rama nueva en `c7ee93a`; se mantiene separado el trabajo local previo. |
| 2026-11-20 13:27 +0100 | Revisar los archivos base con la skill recién creada. | El workflow existente ejecuta init, formato, validate, dos planes y dos políticas; no incluye apply. `.gitignore` excluye planes y protege los `.tfvars` salvo `escenario-integracion.tfvars`. |
| 2026-11-20 13:28 +0100 | Crear `.github/skills/iac-opentofu-laboratorio/SKILL.md` y leerlo para ejecutar su procedimiento en esta rama. | La skill cubre inspección de la base, propagación raíz→módulo→plan, política recursiva, prueba negativa, Actions y trazabilidad. |
| 2026-11-20 13:29 +0100 | Commit `c062c0c` y push de la skill y el registro inicial. | Se publicó `ejercicio-8-amos-solucion-con-skill`; Actions [44736502260](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44736502260) pasó con el código base del ejercicio 7. |
| 2026-11-20 13:30 +0100 | Reaplicar los cambios del ejercicio 8 siguiendo la skill. | Cambios en `variables.tf`, `escenario-integracion.tfvars`, `main.tf`, `modulo_ficha/variables.tf`, `modulo_ficha/main.tf`, `politica_plan.py` y `README.md`. Valores previstos: `pruebas/equipo-lab` e `integracion/equipo-integracion`. |
| 2026-11-20 13:30 +0100 | Revisar el diff y herramientas locales. | `git diff --check` pasó; `.github/workflows/validacion.yml` y `.gitignore` no cambiaron. OpenTofu no está instalado y Python no está disponible como intérprete; no se instaló software. La comprobación de planes se hará en Actions. |

Las siguientes filas registrarán los commits, ejecuciones, prueba controlada, corrección y resultado final.
