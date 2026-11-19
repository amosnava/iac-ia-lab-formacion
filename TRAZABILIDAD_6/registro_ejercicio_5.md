# Registro de cambios para el ejercicio 6

## 2026-11-19 — Política sobre los planes

- Se confirmó la rama `ejercicio-6-amos-solucion`, creada desde `main` en `f81ea6b`.
- El árbol estaba limpio al iniciar esta intervención, salvo el archivo `politica_plan.py` sin seguimiento creado en el paso anterior.
- No había entradas en `git stash list`. Se intentó preservar el estado con `git stash push`, que informó `No local changes to save`; no se creó ni alteró ningún stash.
- Se modificó `.github/workflows/validacion.yml`: se desactivó `tofu_wrapper`, se guardaron los planes en `plan-predeterminado.tfplan` y `plan-integracion.tfplan`, se añadió una llamada a `politica_plan.py` tras cada plan y se incorporaron ambos resultados al resumen.
- Se comprobó que `.gitignore` excluye `*.tfplan`; no se modificó.
- No se modificaron `main.tf`, el módulo, las guías ni `politica_plan.py`.
- No se ejecutó OpenTofu ni GitHub Actions. No se hicieron commits, push ni pull request; la integración queda pendiente de una ejecución real publicada.
