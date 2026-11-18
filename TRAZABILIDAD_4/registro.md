# Trazabilidad del ejercicio 4

## 2026-11-18 — Inspección inicial y preparación de prerrequisitos

- Se revisó la guía `GUIAS/Guia_Alumnado_Ejercicio_4.docx` y los archivos `main.tf`, `variables.tf`, `outputs.tf`, `escenario-integracion.tfvars`, `.github/workflows/validacion.yml` y `.gitignore`.
- El proyecto define un único recurso ficticio `terraform_data.aplicacion`; no usa proveedores cloud. El workflow de la rama del ejercicio 3 tiene los dos planes y `variables.tf` conserva las validaciones de entorno y nombre.
- La rama inicial era `ejercicio-3-amos-solucion`, limpia en `d73a310`, igual a `origin/ejercicio-3-amos-solucion`. `origin` apunta a `git@github.com:amosnava/iac-ia-lab-formacion.git`.
- La guía espera que los ejercicios 1–3 ya estén en `main`, pero `main` local y remoto estaba en `2237e1e`: no tenía el escenario de integración, el segundo plan ni las validaciones del ejercicio 3.
- Se comprobó que la rama del ejercicio 3 contiene el estado de los ejercicios 2 y 3 y un archivo temporal de Word rastreado (`GUIAS/~$ia_Alumnado_Ejercicio_2.docx`).
- El usuario eligió integrar primero los prerrequisitos en `main` mediante una rama limpia y PR, y usar `ejercicio-4-amos-solucion` como nombre de la futura rama de trabajo del ejercicio 4.

## 2026-11-18 — Preparación de rama limpia de integración

- Se creó `integrar-ejercicio-3` desde `main`.
- Se incorporaron desde `ejercicio-3-amos-solucion` los archivos necesarios para el ejercicio 2 y sus validaciones del ejercicio 3: workflow, variables, configuración principal, archivo `.tfvars` y trazabilidades de los ejercicios 2 y 3.
- Se excluyó `GUIAS/~$ia_Alumnado_Ejercicio_2.docx`, archivo temporal de Word que no es necesario para los ejercicios.
- Se creó este registro para que la trazabilidad solicitada acompañe la integración y pueda continuar con los cambios del ejercicio 4.
- No se ejecutó OpenTofu ni se hizo `apply` o `destroy`.
