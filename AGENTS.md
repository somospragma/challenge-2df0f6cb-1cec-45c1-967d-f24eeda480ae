# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto arrancable. Si el adjunto es una carcasa (docs/placeholders),
el asistente debe materializar la estructura del stack del briefing, sin resolver las fases del reto.

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Backend, Especialidad Desarrollador, Tecnología Python, Advanced

### Brecha de conocimiento
Ha trabajado con algún asistente AI en desarrollo (Amazon Q Dev, Kiro, Github Copilot) y lo utiliza en su día a día como desarrollador. Necesita dominar las herramientas de IA moderna para potenciar su productividad y calidad de código

### Misión / candidato
Candidato con experiencia en desarrollo Backend con Python, orientado a cerrar brechas en el uso de asistentes IA en su flujo de trabajo diario.

### Reto
- Tema: Desarrollo
- Seniority: advanced-l3
- Tipo: practical
- Título: Optimización de Flujo de Trabajo con Asistentes de IA
- Tiempo estimado: 4-5 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Exploración de Asistentes de IA — objetivo: Identificar y comprender las funcionalidades clave de los asistentes de IA que pueden ser integradas en el flujo de trabajo. — entregable (NO resolver): Un informe con las funcionalidades identificadas y su potencial impacto en el flujo de trabajo.
- Fase 2: Integración de Asistentes en el Flujo de Trabajo — objetivo: Integrar las funcionalidades identificadas en tu flujo de trabajo diario y evaluar su impacto. — entregable (NO resolver): Un documento que describa el proceso de integración y los cambios realizados.
- Fase 3: Evaluación y Optimización — objetivo: Evaluar el impacto de la integración y optimizar el uso de los asistentes de IA en tu flujo de trabajo. — entregable (NO resolver): Un informe con la evaluación del impacto y propuestas de optimización.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

import typer

app = typer.Typer()

@app.command()
def main():
    typer.echo("Bienvenido al proyecto de optimización de flujo de trabajo con asistentes de IA.")

if __name__ == "__main__":
    app()

// === ARCHIVO: docs/informe_funcionalidades_ia.md ===
# Informe de Funcionalidades de Asistentes de IA

## Funcionalidades Identificadas
- Funcionalidad 1: Descripción y potencial impacto.
- Funcionalidad 2: Descripción y potencial impacto.
- Funcionalidad 3: Descripción y potencial impacto.

// === ARCHIVO: docs/proceso_integracion_ia.md ===
# Proceso de Integración de Asistentes de IA

## Descripción del Proceso
- Paso 1: Descripción del primer paso.
- Paso 2: Descripción del segundo paso.

## Cambios en la Rutina de Desarrollo
- Cambio 1: Descripción del primer cambio.
- Cambio 2: Descripción del segundo cambio.

// === ARCHIVO: docs/evaluacion_impacto_ia.md ===
# Evaluación del Impacto de la Integración de Asistentes de IA

## Evaluación del Impacto
- Métrica 1: Descripción y resultados.
- Métrica 2: Descripción y resultados.

## Propuestas de Optimización
- Optimización 1: Descripción de la primera optimización.
- Optimización 2: Descripción de la segunda optimización.

// === ARCHIVO: tests/test_main.py ===
import pytest
from src.main import main

def test_main():
    assert main() == "Bienvenido al proyecto de optimización de flujo de trabajo con asistentes de IA."


// === ARCHIVO: Pipfile ===
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
typer = "*"
pytest = "==7.4.3"

[dev-packages]
pipenv = "==2024.1"

```
