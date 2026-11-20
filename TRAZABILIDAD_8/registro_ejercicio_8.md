# Trazabilidad del ejercicio 8

## Punto de partida

- Repositorio personal: `amosnava/iac-ia-lab-formacion`.
- `origin`: `git@github.com:amosnava/iac-ia-lab-formacion.git`.
- La guía denomina la rama `taller-final-ejercicio-8`; por petición del usuario, la rama de trabajo es `ejercicio-8-amos-solucion`.
- La rama se creó desde `origin/ejercicio-7-amos-solucion`, commit `c7ee93ae8f51f6492813b7c9b005f28a8e86b804`, para continuar el ejercicio 7 sin incorporar dos commits locales de personalización que solo añadían y eliminaban `.github/agents/github agent.agent.md`.
- La última ejecución verde del ejercicio 7 fue [Actions 44710704874](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44710704874), en `main`, commit `2fb4c0e83e8b07380a0f113affadac3dae6f6207`.
- El árbol de trabajo estaba limpio al crear la rama. No se modificaron los commits locales de personalización.

## Objetivo y límites

Añadir el responsable ficticio por escenario, propagarlo de la raíz al módulo, guardar las etiquetas en cada `terraform_data.ficha` y ampliar la política para aprobar únicamente el responsable permitido para cada entorno. La integración correcta usa `equipo-integracion`; el escenario predeterminado usa `equipo-lab`.

La validación de los planes se ejecutará en el workflow existente de GitHub Actions. No se añaden proveedores cloud ni se ejecutan `tofu apply` o `destroy`; `terraform_data` y sus etiquetas son datos ficticios.

## Registro de cambios y comprobaciones

| Fecha/hora | Acción | Resultado |
| --- | --- | --- |
| 2026-11-20 12:36 +0100 | Revisar la guía, el remoto, el estado del repositorio y la ejecución del ejercicio 7. | Confirmado el repositorio personal, `origin`, el commit verde y que la rama local del ejercicio 7 tenía dos commits de personalización fuera del remoto. |
| 2026-11-20 12:37 +0100 | Crear `ejercicio-8-amos-solucion` desde `origin/ejercicio-7-amos-solucion`. | Rama creada desde `c7ee93a`; los commits locales de personalización no se incluyeron. |
| 2026-11-20 12:37 +0100 | Añadir `responsable` en la raíz y el módulo, las etiquetas ficticias, las validaciones de política y la documentación inicial. | Cambios implementados; pendientes las verificaciones en el workflow y la prueba controlada. |
| 2026-11-20 12:38 +0100 | Comprobar herramientas y diff local. | `git diff --check` pasó y el workflow no cambió. OpenTofu no está instalado; Python no está disponible como intérprete en este equipo. No se instaló software; la validación del plan y de la política se realizará en GitHub Actions. |
| 2026-11-20 12:39 +0100 | Commit `b778fcc` y push de la implementación inicial a `ejercicio-8-amos-solucion`. | Rama publicada en el repositorio personal; el commit disparó el workflow existente. |
| 2026-11-20 12:40 +0100 | Revisar Actions [44729556613](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44729556613). | Ejecución `success`: inicializar, formato, validar, ambos planes y ambas políticas pasaron. Se produjo el artefacto `evidencia-iac-44729556613-1`. |
| 2026-11-20 12:40 +0100 | Revisar el caso de marcas anidadas en la política. | La búsqueda recursiva trata diccionarios/listas con valores `false` como no marcados y detecta cualquier `true`; el plan inicial aceptado confirma que las marcas `false` del plan real no provocaron un rechazo. |
| 2026-11-20 12:41 +0100 | Preparar el ensayo controlado cambiando solo el responsable de integración a `equipo-lab`. | Predicción: formato, validación, plan y política predeterminada pasarán; el plan de integración pasará y su política fallará con `POLÍTICA RECHAZADA: responsable no aprobado para integracion`. Resultado pendiente de Actions. |

Las modificaciones, commits, publicaciones y ejecuciones de Actions se anotarán aquí durante el ejercicio.
