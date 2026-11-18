# Trazabilidad del ejercicio 3

## 2026-11-17 — Inspección y preparación

- Se inspeccionaron `main.tf`, `variables.tf`, `outputs.tf`, `escenario-integracion.tfvars`, `.github/workflows/validacion.yml` y `.gitignore`, junto con la rama, el estado y `origin`.
- El punto de partida esperado estaba en `main`, pero la rama `main` local no contenía el ejercicio 2: usaba `entorno = "desarrollo"` y solo tenía un plan. `ejercicio-2-amos-solucion` sí contenía el ejercicio 2 completo y estaba limpio.
- Tras consultar la discrepancia, el usuario eligió basar el ejercicio 3 en `ejercicio-2-amos-solucion` y usar la rama `ejercicio-3-amos-solucion`.
- Se creó `ejercicio-3-amos-solucion` desde el commit del ejercicio 2.

## 2026-11-17 — Reglas de validación

- En `variables.tf`, se añadió una validación para limitar `entorno` a `desarrollo`, `pruebas` o `integracion`.
- En `variables.tf`, se añadió una validación para exigir que `nombre_aplicacion` comience por `portal-`.
- Se conservaron los valores predeterminados y el archivo `escenario-integracion.tfvars`.
- No se modificaron otros archivos del proyecto, no se ejecutó OpenTofu, no se hizo commit ni push.
