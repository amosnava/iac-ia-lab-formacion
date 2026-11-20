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
| 2026-11-20 12:41 +0100 | Publicar el registro del primer resultado verde. | Commit `05696d7`; Actions [44729655004](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44729655004) terminó en `success`; artefacto `evidencia-iac-44729655004-1`. |
| 2026-11-20 12:41 +0100 | Predecir el ensayo con responsable incorrecto. | Los pasos hasta plan de integración deben pasar; el responsable incorrecto solo debe ser rechazado por la política de integración. |
| 2026-11-20 12:42 +0100 | Publicar la prueba controlada con `responsable = "equipo-lab"` en integración. | Commit `fd94583`; Actions [44729729209](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44729729209) terminó en `failure`, con evidencia `evidencia-iac-44729729209-1`. El cambio es una cadena válida, así que el rechazo esperado es la política de integración: `POLÍTICA RECHAZADA: responsable no aprobado para integracion`. |
| 2026-11-20 12:42 +0100 | Restaurar `responsable = "equipo-integracion"` en `escenario-integracion.tfvars`. | Valor aprobado recuperado; se publicó en el commit `25e5511` y la ejecución de corrección fue verde. |
| 2026-11-20 12:45 +0100 | Commit `25e5511` y push de la corrección. | Actions [44730168298](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44730168298) terminó en `success`; ambos planes y ambas políticas volvieron a pasar. Artefacto `evidencia-iac-44730168298-1`. |
| 2026-11-20 12:46 +0100 | Actualizar y publicar el README con la regla por entorno, el resultado del ensayo y la corrección. | Commit `631bedd`; Actions [44730360771](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44730360771) terminó en `success`. El README documenta la ejecución roja y la corrección verde. |
| 2026-11-20 12:47 +0100 | Publicar el cierre de trazabilidad en el commit `041ab93`. | Cambio exclusivo de Markdown; no se repitió Actions porque el código y README ya estaban validados en [44730360771](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44730360771). |
| 2026-11-20 12:48 +0100 | Intentar completar el PR hacia `ejercicio-7-amos-solucion`. | No se pudo crear desde esta sesión: no hay GitHub MCP de escritura ni `gh` instalado. No se hizo merge. El enlace para abrirlo manualmente es [comparar ramas](https://github.com/amosnava/iac-ia-lab-formacion/compare/ejercicio-7-amos-solucion...ejercicio-8-amos-solucion?expand=1). |

Las modificaciones, commits, publicaciones y ejecuciones de Actions se anotarán aquí durante el ejercicio.
