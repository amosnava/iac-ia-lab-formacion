# Trazabilidad del ejercicio 2

## 2026-11-17 — Inspección inicial

- Se revisaron `variables.tf`, `main.tf`, `outputs.tf`, `.github/workflows/validacion.yml` y `.gitignore`, además de la guía del ejercicio 2.
- La guía espera la rama `main` y `entorno` con valor por defecto `pruebas`; el repositorio estaba en `ejercicio-1-amos-solucion` y el valor encontrado era `prueba`.
- `git status` estaba limpio. `origin` era `git@github.com:amosnava/iac-ia-lab-formacion.git` (fetch/push).
- Se creó esta carpeta de trazabilidad vacía; no se modificaron archivos del proyecto durante esa inspección.

## 2026-11-17 — Parte A

- Se volvió a comprobar el contenido de `variables.tf`, `main.tf` y el estado del repositorio; seguían sin cambios locales.
- Se consultó al usuario por la diferencia entre el valor real `prueba` y el valor indicado `pruebas`. El usuario indicó corregirlo a `pruebas`.
- En `variables.tf`, se ajustó el valor predeterminado de `entorno` a `pruebas` y se añadió la variable `nombre_aplicacion` con valor predeterminado `portal-demo`.
- En `main.tf`, el nombre literal se sustituyó por `var.nombre_aplicacion`.
- No se modificaron otros archivos del proyecto, no se ejecutó OpenTofu, no se hizo commit ni push.

## 2026-11-17 — Comprobación previa a publicar

- La rama inicial era `ejercicio-1-amos-solucion`; como `demo-ejercicio-2-local` no existía localmente, se creó y se cambió a ella. Los cambios locales se conservaron.
- Se confirmó que `git diff --check` termina sin errores.
- Los únicos archivos modificados del proyecto son `variables.tf` y `main.tf`; no había archivos preparados para commit. `TRAZABILIDAD_2/` permanece sin preparar.
- `origin` sigue apuntando a `git@github.com:amosnava/iac-ia-lab-formacion.git`, no al repositorio indicado `mpvicenteselae/iac-ia-laboratorio-demo-mario`.
- No se prepararon archivos ni se hizo commit o push porque la comprobación del remoto no coincide con lo solicitado.

## 2026-11-17 — Preparación para commit

- Se confirmó la rama `demo-ejercicio-2-local`, el remoto `git@github.com:amosnava/iac-ia-lab-formacion.git` y que `git diff --check` no detecta errores.
- Antes de preparar cambios no había archivos en el índice; los únicos archivos modificados del proyecto eran `variables.tf` y `main.tf`.
- Se prepararon exclusivamente `variables.tf` y `main.tf`. La carpeta `TRAZABILIDAD_2/` no se preparó.
- No se hizo commit ni push; queda pendiente la autorización del usuario.

## 2026-11-17 — Revisión previa repetida

- Se verificó de nuevo que la rama activa es `demo-ejercicio-2-local` y que `origin` apunta a `git@github.com:amosnava/iac-ia-lab-formacion.git`.
- `git diff --check` y `git diff --cached --check` no detectaron errores.
- El índice ya contenía únicamente `main.tf` y `variables.tf`; no se prepararon archivos adicionales.
- No se hizo commit ni push.

## 2026-11-17 — Cambio a rama de entrega

- La rama solicitada `ejercicio-2-amos-solucion` no existía localmente; se creó desde `demo-ejercicio-2-local` y se cambió a ella, conservando los cambios preparados.
- Se confirmó `origin` como `git@github.com:amosnava/iac-ia-lab-formacion.git`.
- `git diff --check` y `git diff --cached --check` no detectaron errores.
- El índice contiene exclusivamente `main.tf` y `variables.tf`; `TRAZABILIDAD_2/` permanece sin preparar.
- No se hizo commit ni push.
