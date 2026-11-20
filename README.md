# Laboratorio de IaC e IA · empieza por aquí

Este repositorio contiene **un único proyecto ficticio**, `portal-demo`. Vas a trabajar en **una copia propia** del repositorio durante todos los ejercicios. Cada ejercicio amplía lo que hiciste en el anterior. Al principio solo existe el código necesario para el ejercicio 1; los demás archivos aparecerán cuando tú los crees.

## Tu primer paso

1. Descarga y abre la [Guía del ejercicio 1 (Word)](GUIAS/Guia_Alumnado_Ejercicio_1.docx?raw=1). Léela desde el principio: incluye los botones para crear tu copia y comprobarla.
2. En esta página pulsa **Use this template → Create a new repository**. En **Owner** elige tu usuario, deja **Include all branches** desmarcado y crea un repositorio público con otro nombre. **Hazlo una sola vez.**
3. Comprueba que la URL de tu copia empieza por `https://github.com/TU_USUARIO/`. A partir de aquí, todos tus cambios irán a esa copia.
4. Abre **Actions** en tu copia. Si aparece **Validacion IaC → Commit inicial → comprobar** en verde, el laboratorio ya ejecutó OpenTofu en GitHub. La guía explica qué hacer si no aparece.
5. Continúa la guía del ejercicio 1: abre **tu copia** en `github.dev`, cambia `variables.tf`, confirma y publica el cambio, y consulta la nueva ejecución de Actions.

**No necesitas instalar GitHub Actions, OpenTofu, Git ni VS Code en tu equipo para la ruta de navegador.** GitHub Actions es una pestaña de GitHub; el workflow instala OpenTofu en un ejecutor temporal. `github.dev` es el editor web. Abre ChatGPT o Copilot Chat en **otra pestaña** para preguntar, predecir y revisar. Usa solo datos ficticios.

## Las cinco guías

| Orden | Guía Word | Qué harás en la misma copia |
| --- | --- | --- |
| 1 | [Puesta en marcha, IA y primer plan](GUIAS/Guia_Alumnado_Ejercicio_1.docx?raw=1) | Crear la copia, comprender tres archivos, cambiar un entorno y leer el resultado. |
| 2 | [Dos escenarios](GUIAS/Guia_Alumnado_Ejercicio_2.docx?raw=1) | Parametrizar la configuración y comparar dos planes. |
| 3 | [Revisión y gobierno](GUIAS/Guia_Alumnado_Ejercicio_3.docx?raw=1) | Crear una rama, añadir validaciones y revisar un pull request. |
| 4 | [Automatización y evidencias](GUIAS/Guia_Alumnado_Ejercicio_4.docx?raw=1) | Mejorar el workflow y diagnosticar un fallo real de la práctica. |
| 5 | [Módulo reutilizable](GUIAS/Guia_Alumnado_Ejercicio_5.docx?raw=1) | Crear un módulo local y usarlo para dos fichas ficticias. |

**El ejercicio 2 empieza donde dejaste el 1**; no crees otra copia. Sigue el mismo principio para los siguientes. Las guías están en `GUIAS/` para poder descargarlas; el código que editarás está en la raíz y en `.github/workflows/`.

## Qué son los archivos iniciales

| Archivo | Función |
| --- | --- |
| `variables.tf` | Declara el entorno, inicialmente `desarrollo`. |
| `main.tf` | Describe una ficha ficticia con `terraform_data`. |
| `outputs.tf` | Define el resumen del plan. |
| `.github/workflows/validacion.yml` | Instala OpenTofu y ejecuta las comprobaciones en GitHub Actions. |

El workflow calcula un plan, **no ejecuta `tofu apply`** y no crea una web ni infraestructura comercial. Si tu equipo permite VS Code local, puedes usarlo con **esa misma copia**: el código y la comprobación en Actions son los mismos. La ruta principal, explicada paso a paso en los Word, funciona desde el navegador.

## Arquitectura ficticia

- **Necesidad:** representar un portal principal y una ficha de ayuda con la misma estructura.
- **Reutilización:** ambas fichas utilizan el módulo local `modulo_ficha`, que define el recurso ficticio una sola vez.
- **Entradas:** cada instancia recibe `nombre` y `entorno`; el módulo valida el prefijo `portal-` y los entornos permitidos.
- **Escenarios:** los mismos archivos generan un plan predeterminado y otro de integración mediante `escenario-integracion.tfvars`.
- **Evidencias:** GitHub Actions comprueba formato recursivo, valida la configuración, genera los dos planes y publica un resumen y un artefacto de texto.
- **Límites:** no se ejecuta `apply`; no se crean portales, servidores ni redes, y no se miden costes ni observabilidad de infraestructura real.
- **Gobernanza:** antes de aprobar un cambio, se revisan el diff, los planes y las evidencias del pipeline.

## Política del laboratorio

`politica_plan.py` lee el JSON de cada plan y aprueba únicamente las dos altas ficticias esperadas: `module.fichas["portal"].terraform_data.ficha` y `module.fichas["ayuda"].terraform_data.ficha`. Comprueba sus nombres, que ambas usen el mismo entorno permitido y que no haya otras operaciones. El workflow ejecuta la política después de cada plan y muestra ambos resultados en el resumen de Actions.

`tofu validate` comprueba la estructura y coherencia de la configuración; la política aplica además reglas de negocio al resultado previsto, como exigir que portal y ayuda compartan entorno. Por eso una configuración puede validar y generar un plan, pero ser rechazada por la política.

Este control solo cubre las reglas didácticas del laboratorio. No sustituye una revisión humana, aprobaciones independientes, controles de permisos, análisis de costes o seguridad, ni demuestra que un despliegue real sea seguro. Los planes se inspeccionan en el runner; no se ejecuta `apply` ni se crean recursos cloud.

## Responsables y etiquetas ficticias

El ejercicio 8 añade la variable raíz `responsable`: su valor predeterminado es `equipo-lab`, y `escenario-integracion.tfvars` selecciona `equipo-integracion`. La raíz pasa ese dato a cada instancia del módulo, que lo incorpora junto con `proyecto = "nexo-portal"` y el entorno en el mapa `etiquetas` de `terraform_data.ficha.input`.

La política comprueba que las fichas tengan exactamente las entradas y etiquetas esperadas, que las etiquetas coincidan con el entorno y que el equipo esté aprobado para ese entorno: `equipo-lab` para desarrollo y pruebas, y `equipo-integracion` para integración. Un responsable incorrecto puede superar formato, validación y plan, pero debe ser rechazado por la política del plan correspondiente. En la repetición guiada por la skill, `equipo-lab` en integración fue rechazado ([prueba roja](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44736724334)); al restaurar `equipo-integracion`, se lanzó la [ejecución de corrección](https://github.com/amosnava/iac-ia-lab-formacion/actions/runs/44736830900).

Estas etiquetas son datos ficticios de `terraform_data`, no etiquetas nativas de recursos cloud. El workflow solo inspecciona planes; no ejecuta `apply` ni crea infraestructura real.

## Catálogo de fichas

El local `catalogo` de `main.tf` contiene las claves `portal` y `ayuda`. Una única llamada al módulo usa `for_each` para crear una instancia por clave; `each.value` entrega el nombre (`portal-demo` o `portal-ayuda`, y `portal-interno` para portal en integración). La expresión `for` de `outputs.tf` reúne las salidas `resumen` en un mapa conservando las claves.

La prueba temporal con la clave `informes` fue válida para el formato, la validación y el plan, pero la política la rechazó porque solo autoriza las fichas `portal` y `ayuda`. Retirar esa entrada restaura el catálogo aprobado. Esto no es un despliegue ni un servicio real de autoservicio: solo se planifican fichas ficticias con `terraform_data`, sin `apply` ni infraestructura cloud.
