# Trazabilidad del ejercicio 5

## 2026-11-18 — Inspección y punto de partida

- Se revisaron las guías `GUIAS/Guia_Alumnado_Ejercicio_5.docx` y `Guia_Ejercicio_5_IaC_IA_Modalidad_Local_BRR.docx`, junto con `main.tf`, `variables.tf`, `outputs.tf`, `README.md`, `escenario-integracion.tfvars` y `.github/workflows/validacion.yml`.
- El árbol de trabajo estaba limpio en `ejercicio-4-amos-solucion`. Esa rama tenía el commit local `a3ee579` con los cambios del workflow del ejercicio 4, un commit por delante de `origin/main` (`c91516b`); no existía una rama remota `ejercicio-4-amos-solucion`.
- El usuario indicó que los cambios del ejercicio 5 se publicarán primero en una rama propia y que posteriormente se sincronizarán con `main`. Se eligió el nombre `ejercicio-5-arquitectura-amos-solucion`.
- No existían `modulo_ficha/` ni `TRAZABILIDAD_5/`. `escenario-integracion.tfvars` contiene `portal-interno` e `integracion`.

## 2026-11-18 — Implementación local del ejercicio 5

- Se creó `ejercicio-5-arquitectura-amos-solucion` desde el estado local de `ejercicio-4-amos-solucion`, conservando los cambios previos del ejercicio 4 sin publicarlos.
- Se creó `modulo_ficha/` con `main.tf`, `variables.tf` y `outputs.tf`: un recurso ficticio parametrizado, dos entradas obligatorias validadas y una salida `resumen`.
- En el `main.tf` raíz, se reemplazó el recurso único por las instancias `portal` y `ayuda` del mismo módulo.
- En el `outputs.tf` raíz, se consolidaron los resúmenes de ambas instancias.
- En `.github/workflows/validacion.yml`, se añadió `-recursive` al chequeo de formato para incluir el módulo y se conservaron los demás pasos y evidencias del ejercicio 4.
- En `README.md`, se añadió `Arquitectura ficticia` para explicar reutilización, entradas, escenarios, evidencias y límites.
- Se dejó la configuración en su estado final correcto. El ensayo temporal sin `nombre` requiere una ejecución posterior controlada y no se dejó en los archivos.
- No se modificaron las variables de raíz ni `escenario-integracion.tfvars`; no se añadieron proveedores cloud ni credenciales.
- No se ejecutó OpenTofu, no se hizo `apply` o `destroy`, y no se hizo commit ni push.

## 2026-11-18 — Primer commit y validación verde

- Se confirmó `Ejercicio 5: módulo local reutilizable` (`c45e91501084dcf5d42f3dc40dddfc08cd8ab36c`) con los tres archivos del módulo, `main.tf`, `outputs.tf`, el workflow y este registro; `README.md` quedó para un commit posterior como indica la guía.
- Se publicó `ejercicio-5-arquitectura-amos-solucion` en `origin`.
- La ejecución de Actions [44296306544](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44296306544) terminó en `success`. El job confirma `success` para formato, validación, ambos planes, resumen y artefacto.
- Se publicó el artefacto `evidencia-iac-44296306544-1` (expira el 25-11-2026).
- La API permitió consultar estados y artefacto, pero negó la descarga del log detallado con `403 Must have admin rights`; no se registran como observados los detalles internos de las salidas de plan.

## 2026-11-18 — Ensayo controlado: falta nombre en ayuda

- Se quitó temporalmente `nombre = "portal-ayuda"` de la llamada raíz `module.ayuda`, manteniendo su `source` y `entorno`.
- Se espera que `Validar` falle por el argumento obligatorio `nombre` ausente; los dos pasos de plan deberían omitirse, mientras que resumen y publicación de evidencia se intentan por `always()`.
- Este fallo es deliberado y no debe permanecer en la solución final. La ejecución remota y su log se registrarán después de publicar el commit de prueba.
