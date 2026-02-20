# 🚀 Conversor Excel a LaTeX para Tesis - Guía Completa

## 📋 Índice

1. [Descripción General](#descripción-general)
2. [Dos Formas de Usar el Script](#dos-formas-de-usar-el-script)
3. [Opción 1: Excel Local](#opción-1-excel-local-excel_to_latexpy)
4. [Opción 2: Excel en Google Drive](#opción-2-excel-en-google-drive-excel_drive_a_latexpy)
5. [Comparación de Métodos](#comparación-de-métodos)
6. [Instalación de Dependencias](#instalación-de-dependencias)
7. [Ejemplos de Uso](#ejemplos-de-uso)
8. [Formato del Excel](#formato-del-excel)
9. [Solución de Problemas](#solución-de-problemas)
10. [Personalización](#personalización)

---

## 🎯 Descripción General

Este proyecto proporciona **dos scripts de Python** que convierten automáticamente requerimientos desde Excel a tablas LaTeX profesionales, perfectamente formateadas para documentos de tesis.

### ✅ Problemas Resueltos

Ambos scripts incluyen todas las correcciones necesarias:

1. ✅ **Saltos de línea correctos**: Usa `\newline` para evitar desbordamiento de texto
2. ✅ **Sin cortes de página**: Implementa `longtable` para continuidad automática
3. ✅ **Bordes completos**: Todas las tablas tienen bordes cerrados correctamente
4. ✅ **Espaciado profesional**: Texto bien espaciado, no amontonado
5. ✅ **Sin desbordamiento**: El contenido permanece en su columna correcta

### 📦 Archivos del Proyecto

```
proyecto/
├── excel_to_latex.py           ← Script para Excel LOCAL
├── excel_drive_a_latex.py      ← Script para Excel en GOOGLE DRIVE
├── README.md                   ← Este archivo
└── ERS-SGPI.xlsx              ← Tu archivo Excel (opcional)
```

---

## 🔀 Dos Formas de Usar el Script

Tienes **dos opciones** para trabajar con tus requerimientos, dependiendo de dónde tengas tu archivo Excel:

| Método | Script | Cuándo Usarlo |
|--------|--------|---------------|
| **Opción 1: Local** | `excel_to_latex.py` | Tienes el Excel descargado en tu computadora |
| **Opción 2: Drive** | `excel_drive_a_latex.py` | Tu Excel está en Google Drive o Google Sheets |

### 🤔 ¿Cuál Debo Elegir?

**Usa `excel_to_latex.py` si:**
- ✅ Ya tienes el archivo Excel descargado
- ✅ Trabajas sin conexión a internet
- ✅ Prefieres simplicidad (menos dependencias)
- ✅ No colaboras con otros en tiempo real

**Usa `excel_drive_a_latex.py` si:**
- ✅ Tu Excel está en Google Drive o Google Sheets
- ✅ Colaboras con otras personas en el documento
- ✅ Quieres la última versión siempre sin descargar manualmente
- ✅ Trabajas desde diferentes computadoras

---

## 📁 Opción 1: Excel Local (`excel_to_latex.py`)

### Características

- ✨ **Simplicidad**: Solo necesita `pandas` y `openpyxl`
- 🚀 **Velocidad**: Procesamiento más rápido (no descarga)
- 📴 **Sin internet**: Funciona offline
- 🔒 **Privacidad**: Todo local, nada en la nube

### Instalación

```bash
# Solo dos dependencias
pip install pandas openpyxl
```

### Uso Básico

```bash
# Sintaxis
python excel_to_latex.py <archivo_excel> [directorio_salida]

# Ejemplo 1: Usar directorio por defecto
python excel_to_latex.py ERS-SGPI.xlsx

# Ejemplo 2: Especificar directorio de salida
python excel_to_latex.py ERS-SGPI.xlsx mi_tesis/capitulo3/

# Ejemplo 3: Con ruta completa (Windows)
python excel_to_latex.py "C:\Users\Usuario\Desktop\ERS-SGPI.xlsx" output/
```

### Salida Esperada

```
Procesando: ERS-SGPI.xlsx
Directorio de salida: latex_output_final

✓ Generados 41 requerimientos funcionales
✓ Generados 13 requerimientos no funcionales

✓ Archivo principal generado: todos_los_requerimientos.tex

Para compilar el documento completo, ejecuta:
  cd latex_output_final
  pdflatex todos_los_requerimientos.tex
  pdflatex todos_los_requerimientos.tex  # Segunda pasada

¡Proceso completado exitosamente!
```

### Ventajas

| Ventaja | Descripción |
|---------|-------------|
| 🚀 Más rápido | No necesita descargar nada |
| 📦 Menos dependencias | Solo pandas y openpyxl |
| 🔒 Más privado | Todo permanece local |
| 📴 Funciona offline | No requiere internet |

### Desventajas

| Desventaja | Descripción |
|------------|-------------|
| 📥 Descarga manual | Debes descargar el Excel cada vez |
| 🔄 Sincronización manual | Si hay cambios, descargar nuevamente |
| 👥 Sin colaboración | No refleja cambios en tiempo real |

---

## ☁️ Opción 2: Excel en Google Drive (`excel_drive_a_latex.py`)

### Características

- 🌐 **Acceso directo**: Lee desde Google Drive/Sheets
- 🔄 **Siempre actualizado**: Obtiene la última versión automáticamente
- 👥 **Colaborativo**: Ideal para equipos
- 📱 **Multiplataforma**: Accede desde cualquier dispositivo

### Instalación

```bash
# Tres dependencias (incluye gdown para Drive)
pip install pandas openpyxl gdown
```

### Uso Básico

#### 📍 Opción A: Con Link Completo de Google Sheets

```bash
python excel_drive_a_latex.py "https://docs.google.com/spreadsheets/d/1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ/edit?usp=sharing"
```

#### 📍 Opción B: Con Link de Google Drive (archivo .xlsx)

```bash
python excel_drive_a_latex.py "https://drive.google.com/file/d/1ABC123xyz/view?usp=sharing"
```

#### 📍 Opción C: Solo con el ID del archivo

```bash
python excel_drive_a_latex.py 1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ
```

#### 📍 Opción D: Excel local (también funciona)

```bash
python excel_drive_a_latex.py ERS-SGPI.xlsx
```

### Obtener el Link/ID

**Desde Google Sheets:**
1. Abre tu Google Sheet
2. Clic en "Compartir" → "Obtener enlace"
3. Asegúrate de que sea "Cualquiera con el enlace puede ver"
4. Copia el link completo o solo el ID (la parte entre `/d/` y `/edit`)

**Desde Google Drive (archivo .xlsx):**
1. Haz clic derecho en el archivo
2. "Obtener enlace"
3. Configurar como "Cualquiera con el enlace"
4. Copiar el link

### 🔗 Ejemplo Real del Proyecto

```bash
# Usar el Excel de ejemplo del proyecto
python excel_drive_a_latex.py "https://docs.google.com/spreadsheets/d/1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ/edit?usp=sharing"
```

### Salida Esperada

```
Descargando archivo desde Google...
Downloading...
From: https://docs.google.com/spreadsheets/d/1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ/export?format=xlsx
To: temp_excel.xlsx
100%|████████████████████████████████████████| 68.2k/68.2k [00:01<00:00, 45.3kB/s]

Procesando: temp_excel.xlsx
Directorio de salida: latex_output_final

✓ Generados 41 requerimientos funcionales
✓ Generados 13 requerimientos no funcionales

Proceso completado exitosamente.
```

### Ventajas

| Ventaja | Descripción |
|---------|-------------|
| 🔄 Siempre actualizado | Descarga automáticamente la última versión |
| 👥 Trabajo colaborativo | Múltiples personas pueden editar |
| 📱 Acceso desde cualquier lugar | No necesitas el archivo localmente |
| 🌐 Integración con Drive | Funciona con toda tu infraestructura de Google |

### Desventajas

| Desventaja | Descripción |
|------------|-------------|
| 📦 Más dependencias | Requiere `gdown` adicional |
| 🌐 Necesita internet | No funciona offline |
| 🔐 Permisos necesarios | El archivo debe ser público o compartido |
| ⏱️ Ligeramente más lento | Tiempo de descarga incluido |

---

## ⚖️ Comparación de Métodos

### Tabla Comparativa Completa

| Característica | `excel_to_latex.py` | `excel_drive_a_latex.py` |
|----------------|---------------------|--------------------------|
| **Dependencias** | pandas, openpyxl | pandas, openpyxl, gdown |
| **Funciona offline** | ✅ Sí | ❌ No |
| **Velocidad** | ⚡ Muy rápida | 🐢 Descarga + procesamiento |
| **Colaboración** | ❌ No | ✅ Sí |
| **Actualización** | 🔄 Manual | ✅ Automática |
| **Complejidad** | 😊 Simple | 🤓 Requiere configuración |
| **Privacidad** | 🔒 Total | ⚠️ Requiere permisos públicos |
| **Soporte Drive** | ❌ No | ✅ Sí |
| **Soporte Sheets** | ❌ No | ✅ Sí |
| **Entrada** | Solo .xlsx local | .xlsx, Drive, Sheets, IDs |

### 🎯 Recomendación por Caso de Uso

#### Caso 1: Tesis Individual
**Recomendación:** `excel_to_latex.py`
- Trabajas solo
- Control total del archivo
- Más simple y rápido

#### Caso 2: Proyecto en Equipo
**Recomendación:** `excel_drive_a_latex.py`
- Varios miembros del equipo
- Actualizaciones frecuentes
- Coordinación necesaria

#### Caso 3: Presentación/Demo
**Recomendación:** `excel_drive_a_latex.py`
- Archivo en Drive compartido
- Acceso desde proyector/otra PC
- Siempre la última versión

#### Caso 4: Sin Internet Confiable
**Recomendación:** `excel_to_latex.py`
- Conexión inestable
- Trabajo en campo
- Prefieren local

---

## 🔧 Instalación de Dependencias

### Para `excel_to_latex.py`

**Windows:**
```bash
pip install pandas openpyxl
```

**Linux/Mac:**
```bash
pip3 install pandas openpyxl
```

**Si hay problemas:**
```bash
python -m pip install pandas openpyxl
# o
py -3 -m pip install pandas openpyxl
```

### Para `excel_drive_a_latex.py`

**Windows:**
```bash
pip install pandas openpyxl gdown
```

**Linux/Mac:**
```bash
pip3 install pandas openpyxl gdown
```

**Verificar instalación:**
```bash
python -c "import pandas, openpyxl, gdown; print('✓ Todo instalado correctamente')"
```

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Proyecto Individual con Excel Local

```bash
# Descarga tu Excel de Drive (una sola vez)
# Colócalo en tu carpeta de proyecto

# Generar tablas LaTeX
python excel_to_latex.py ERS-SGPI.xlsx

# Resultado en: latex_output_final/
```

### Ejemplo 2: Trabajo Colaborativo con Google Sheets

```bash
# Tu equipo edita el Google Sheet
# Tú generas el LaTeX directo desde Drive

python excel_drive_a_latex.py "https://docs.google.com/spreadsheets/d/1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ/edit"

# Siempre obtienes la última versión sin descargar
```

### Ejemplo 3: Actualización Frecuente

```bash
# Día 1: Primera versión
python excel_to_latex.py ERS-SGPI.xlsx tesis/v1/

# Día 5: Tu compañero actualizó el Excel en Drive
python excel_drive_a_latex.py "LINK_DEL_DRIVE" tesis/v2/

# Día 10: Versión final
python excel_drive_a_latex.py "LINK_DEL_DRIVE" tesis/final/
```

### Ejemplo 4: Múltiples Directorios de Salida

```bash
# Para diferentes capítulos de tu tesis

python excel_to_latex.py ERS-SGPI.xlsx tesis/capitulo2/
python excel_to_latex.py ERS-SGPI.xlsx presentacion/
python excel_to_latex.py ERS-SGPI.xlsx documentacion_cliente/
```

### Ejemplo 5: Script Automatizado

**actualizar_requerimientos.sh** (Linux/Mac):
```bash
#!/bin/bash

DRIVE_LINK="https://docs.google.com/spreadsheets/d/1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ/edit"
FECHA=$(date +%Y%m%d)
OUTPUT_DIR="versiones/version_$FECHA"

echo "Generando requerimientos - $FECHA"
python3 excel_drive_a_latex.py "$DRIVE_LINK" "$OUTPUT_DIR"

echo "✓ Requerimientos guardados en: $OUTPUT_DIR"
```

**actualizar_requerimientos.bat** (Windows):
```batch
@echo off
set DRIVE_LINK=https://docs.google.com/spreadsheets/d/1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ/edit
set OUTPUT_DIR=latex_output_final

echo Generando requerimientos...
python excel_drive_a_latex.py "%DRIVE_LINK%" "%OUTPUT_DIR%"

echo Proceso completado!
pause
```

---

## 📊 Formato del Excel

### Estructura Requerida

Tu archivo Excel debe tener **dos hojas** con nombres exactos:

#### 🟦 Hoja 1: "Req. Funcionales"

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| `Id` | Identificador único | RF-1, RF-1.1, RF-1.2 |
| `Nombre` | Nombre del requerimiento | Registrar Usuario |
| `Descripción` | Descripción detallada | Permite al administrador... |
| `Datos de entrada` | Campos de entrada | Nombre, Email, Contraseña |
| `Datos de Salida` | Resultados esperados | Mensaje: "Usuario registrado" |
| `Pre-condiciones` | Condiciones previas | Usuario administrador autenticado |
| `Post Condiciones` | Estado posterior | Usuario creado en base de datos |
| `Proceso` | Flujo principal (numerado) | 1. Ingresar datos 2. Validar... |
| `Proceso Alternativo` | Flujos alternativos | Caso A: Email duplicado... |
| `Prioridad` | Nivel de importancia | Alta, Media, Baja, Crítica |
| `Estabilidad` | Probabilidad de cambio | Alta, Media, Baja |
| `Fuente del requerimiento` | Origen | Entrevista, Documento, etc. |
| `Requerimientos relacionados` | Referencias | RF-1, RF-2, RF-3 |

#### 🟪 Hoja 2: "Req. No Funcionales"

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| `Id` | Identificador único | RNF-1, RNF-2 |
| `Nombre` | Nombre del requerimiento | Seguridad de Datos |
| `Categoria` | Tipo de RNF | Seguridad, Rendimiento, Usabilidad |
| `Descripcion` | Descripción detallada | El sistema debe encriptar... |
| `Pre-condiciones` | Condiciones previas | Sistema en producción |
| `Post Condiciones` | Estado posterior | Datos protegidos |
| `Criterios de aceptacion` | Validación | Cumple con estándar ISO... |
| `Prioridad` | Nivel de importancia | Alta, Media, Baja |
| `Estabilidad` | Probabilidad de cambio | Alta, Media, Baja |

### 📝 Ejemplo de Contenido con Saltos de Línea

En Excel, usa **Alt + Enter** para crear saltos de línea dentro de una celda:

```
Datos de entrada:
Nombre
Apellido
Email
Contraseña
```

Esto se convertirá automáticamente en:
```latex
\textbf{Datos de entrada:} & Nombre \newline 
Apellido \newline 
Email \newline 
Contraseña \\
```

### 🎨 Formato Recomendado

**IDs consistentes:**
- ✅ RF-1, RF-1.1, RF-1.2, RF-2, RF-2.1
- ❌ RF1, RF_1_1, rf-1, Req-1

**Procesos numerados:**
```
1. Usuario ingresa datos
2. Sistema valida formato
3. Sistema guarda en base de datos
4. Sistema muestra confirmación
```

**Procesos alternativos con casos:**
```
Caso A: Email inválido
1. Sistema valida email
2. Muestra error: "Formato inválido"

Caso B: Email duplicado
1. Sistema verifica unicidad
2. Muestra error: "Email ya registrado"
```

---

## 📄 Archivos Generados

Ambos scripts generan los mismos archivos de salida:

```
latex_output_final/
├── requerimientos_funcionales.tex       (41 requerimientos)
├── requerimientos_no_funcionales.tex    (13 requerimientos)
├── todos_los_requerimientos.tex         (Documento principal)
└── todos_los_requerimientos.pdf         (Después de compilar)
```

### Compilar a PDF

```bash
cd latex_output_final

# Primera compilación
pdflatex todos_los_requerimientos.tex

# Segunda compilación (para referencias cruzadas)
pdflatex todos_los_requerimientos.tex
```

**Requisitos para compilar:**
- Windows: [MiKTeX](https://miktex.org/) o [TeX Live](https://www.tug.org/texlive/)
- Mac: [MacTeX](https://www.tug.org/mactex/)
- Linux: `sudo apt-get install texlive-latex-base texlive-latex-extra`
- En línea: [Overleaf](https://www.overleaf.com) (no requiere instalación)

---

## 🐛 Solución de Problemas

### Problema 1: "No module named 'pandas'"

```bash
# Instalar dependencias
pip install pandas openpyxl

# Si no funciona
python -m pip install pandas openpyxl
```

### Problema 2: "No module named 'gdown'" (solo excel_drive_a_latex.py)

```bash
pip install gdown
```

### Problema 3: Error al descargar desde Drive

**Error:** "Access denied" o "Failed to download"

**Solución:**
1. Verifica que el archivo sea público ("Cualquiera con el enlace")
2. Para Google Sheets, usa el link completo con `/edit`
3. Intenta con el ID solo en lugar del link completo

```bash
# Método 1: Link completo
python excel_drive_a_latex.py "https://docs.google.com/spreadsheets/d/1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ/edit"

# Método 2: Solo ID
python excel_drive_a_latex.py 1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ
```

### Problema 4: "No se encuentra el archivo"

**Con excel_to_latex.py:**
```bash
# Verifica que el archivo existe
ls ERS-SGPI.xlsx  # Linux/Mac
dir ERS-SGPI.xlsx # Windows

# Usa ruta absoluta
python excel_to_latex.py "C:\Users\Usuario\Desktop\ERS-SGPI.xlsx"
```

**Con excel_drive_a_latex.py:**
- El archivo se descarga temporalmente como `temp_excel.xlsx`
- Se elimina automáticamente después

### Problema 5: Columnas faltantes en Excel

**Error:** "KeyError: 'Descripción'" o similar

**Solución:**
Verifica que tu Excel tenga exactamente estos nombres de hoja:
- ✅ "Req. Funcionales" (con punto y espacio)
- ✅ "Req. No Funcionales" (con punto y espacio)

Y las columnas correctas en cada hoja (ver sección "Formato del Excel")

### Problema 6: Caracteres especiales en Windows

**Error:** Encoding issues al leer el Excel

**Solución:**
```bash
# Usar Python 3.8 o superior
python --version

# Asegurar UTF-8
set PYTHONIOENCODING=utf-8
python excel_to_latex.py ERS-SGPI.xlsx
```

---

## 🎨 Personalización

### Cambiar Anchos de Columnas

Edita la línea ~92 en cualquiera de los dos scripts:

```python
latex_code.append(r"\begin{longtable}{|p{0.28\textwidth}|p{0.67\textwidth}|}")
#                                        ↑                 ↑
#                                   Etiquetas          Contenido
```

**Opciones:**
- `0.28 y 0.67` - Balance estándar (actual)
- `0.25 y 0.70` - Más espacio para contenido
- `0.30 y 0.65` - Más espacio para etiquetas
- `0.35 y 0.60` - Columnas equilibradas

### Modificar Espaciado entre Tablas

Línea ~235:

```python
latex_code.append(r"\vspace{0.5cm}")  # Cambiar 0.5cm a 1cm, 2cm, etc.
```

### Agregar Nuevos Campos

Si tu Excel tiene columnas adicionales, agrega en la función `generate_requirement_table_longtable()`:

```python
# Después de la sección de Estabilidad (línea ~220):

if 'Campo_Personalizado' in row.index and not pd.isna(row.get('Campo_Personalizado', '')):
    contenido = format_text_with_linebreaks(row['Campo_Personalizado'])
    latex_code.append(r"\textbf{Mi Campo:} & " + contenido + r" \\")
    latex_code.append(r"\hline")
```

### Cambiar Estilo de Tabla

**Bordes dobles:**
```python
latex_code.append(r"\begin{longtable}{||p{0.28\textwidth}||p{0.67\textwidth}||}")
```

**Sin bordes verticales:**
```python
latex_code.append(r"\begin{longtable}{p{0.28\textwidth}p{0.67\textwidth}}")
```

---

## 📚 Integración en tu Tesis

### Estructura Recomendada

```
Mi_Tesis/
├── main.tex
├── capitulos/
│   ├── introduccion.tex
│   ├── marco_teorico.tex
│   └── requerimientos/
│       ├── requerimientos_funcionales.tex    ← Copiar aquí
│       └── requerimientos_no_funcionales.tex ← Copiar aquí
└── referencias.bib
```

### Preámbulo en main.tex

```latex
\documentclass[12pt,oneside]{report}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\usepackage{longtable}
\usepackage{array}

\geometry{margin=2.5cm}

% Configuración de tablas
\setlength{\LTpre}{1em}
\setlength{\LTpost}{1em}
\renewcommand{\arraystretch}{1.3}

\title{Título de tu Tesis}
\author{Tu Nombre}
\date{\today}
```

### Incluir en el Documento

```latex
\chapter{Especificación de Requerimientos}

\section{Requerimientos Funcionales}
Los requerimientos funcionales describen las funcionalidades específicas 
del sistema desarrollado.

\input{capitulos/requerimientos/requerimientos_funcionales}

\newpage
\section{Requerimientos No Funcionales}
Los requerimientos no funcionales establecen las restricciones y 
cualidades del sistema.

\input{capitulos/requerimientos/requerimientos_no_funcionales}
```

---

## 🔄 Flujo de Trabajo Recomendado

### Para Proyectos Individuales

```
1. Crear/editar Excel localmente
   ↓
2. Ejecutar: python excel_to_latex.py ERS-SGPI.xlsx
   ↓
3. Copiar .tex a carpeta de tesis
   ↓
4. Compilar tesis completa
   ↓
5. Revisar y ajustar
```

### Para Proyectos Colaborativos

```
1. Equipo edita Google Sheet
   ↓
2. Tú ejecutas: python excel_drive_a_latex.py "LINK_DRIVE"
   ↓
3. Script descarga última versión automáticamente
   ↓
4. Copiar .tex a carpeta de tesis
   ↓
5. Compilar y revisar
   ↓
6. Repetir cuando haya actualizaciones
```

---

## 📊 Estadísticas del Proyecto

Del archivo de ejemplo procesado:

```
📈 Requerimientos Funcionales:      41
📈 Requerimientos No Funcionales:   13
📈 Total de requerimientos:         54
📈 Páginas generadas (PDF):         65
📈 Tiempo de procesamiento:         ~3 segundos (local)
📈 Tiempo de procesamiento:         ~8 segundos (Drive)
```

---

## 🎯 Resumen de Comandos

### Comandos Rápidos para excel_to_latex.py

```bash
# Instalación
pip install pandas openpyxl

# Uso más común
python excel_to_latex.py ERS-SGPI.xlsx

# Con directorio personalizado
python excel_to_latex.py ERS-SGPI.xlsx output/
```

### Comandos Rápidos para excel_drive_a_latex.py

```bash
# Instalación
pip install pandas openpyxl gdown

# Con link de Google Sheets
python excel_drive_a_latex.py "https://docs.google.com/spreadsheets/d/1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ/edit"

# Con ID solo
python excel_drive_a_latex.py 1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ

# Archivo local (también funciona)
python excel_drive_a_latex.py ERS-SGPI.xlsx
```

---

## 📞 Recursos y Enlaces

### Excel de Ejemplo

🔗 **Archivo de ejemplo en Google Sheets:**
```
https://docs.google.com/spreadsheets/d/1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ/edit?usp=sharing
```

Este es el archivo real usado en el proyecto con 54 requerimientos.

### Documentación

- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
- [Overleaf Documentation](https://www.overleaf.com/learn)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [gdown Documentation](https://github.com/wkentaro/gdown)

### Herramientas Recomendadas

- **Editores LaTeX:**
  - [Overleaf](https://www.overleaf.com) - Editor online
  - [TeXstudio](https://www.texstudio.org) - Editor local
  - [VS Code + LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)

---

## 📋 Checklist Pre-Entrega

Antes de entregar tu tesis, verifica:

- [ ] El Excel tiene todas las columnas necesarias
- [ ] No hay celdas combinadas
- [ ] Los IDs son consistentes (RF-1, RF-1.1, etc.)
- [ ] El script ejecutó sin errores
- [ ] El PDF compiló correctamente (2 pasadas)
- [ ] Las tablas tienen bordes completos
- [ ] Los saltos de línea se ven correctos
- [ ] No hay desbordamiento de texto
- [ ] Las referencias cruzadas funcionan
- [ ] Has hecho backup del Excel

---

## 🎓 Casos de Uso Reales

### Caso 1: Tesis Individual

**Situación:** Estudiante trabajando solo en su tesis
**Solución:** `excel_to_latex.py`
**Por qué:** Simple, rápido, todo local

```bash
python excel_to_latex.py mi_tesis_requerimientos.xlsx tesis/cap3/
```

### Caso 2: Equipo de 3 Personas

**Situación:** Proyecto final de carrera en equipo
**Solución:** `excel_drive_a_latex.py`
**Por qué:** Todos editan el mismo Google Sheet

```bash
# Persona 1 edita Excel en Drive
# Persona 2 genera LaTeX:
python excel_drive_a_latex.py "LINK_DEL_SHEET_COMPARTIDO"
# Persona 3 integra en tesis
```

### Caso 3: Proyecto para Cliente

**Situación:** Documentación que se actualiza frecuentemente
**Solución:** `excel_drive_a_latex.py`
**Por qué:** Cliente edita Drive, tú generas PDF actualizado

```bash
# Script que se ejecuta cada semana
python excel_drive_a_latex.py "LINK_CLIENTE" documentacion/
```

---

## 🚀 Próximos Pasos

1. **Instala las dependencias** según el script que vayas a usar
2. **Prepara tu Excel** con el formato correcto
3. **Ejecuta el script** correspondiente
4. **Revisa los archivos .tex** generados
5. **Compila a PDF** para verificar el resultado
6. **Integra en tu tesis** cuando estés satisfecho

---

## 💡 Consejos Finales

### ✅ Mejores Prácticas

1. **Mantén backup** del Excel original
2. **Usa control de versiones** (Git) para tus archivos
3. **Prueba localmente** antes de la versión final
4. **Compila dos veces** para referencias correctas
5. **Revisa el PDF** antes de incluir en la tesis

### 🎯 Tips de Productividad

- Crea un script `.bat` o `.sh` para automatizar
- Usa aliases en tu terminal:
  ```bash
  alias genreq='python excel_to_latex.py ERS-SGPI.xlsx'
  ```
- Programa actualizaciones periódicas con cron (Linux) o Task Scheduler (Windows)

---

## 📄 Licencia

Este proyecto es de uso libre para fines académicos y de investigación.

**Permitido:**
- ✅ Uso en tesis y proyectos académicos
- ✅ Modificación para tus necesidades
- ✅ Compartir con compañeros

**Agradecemos:**
- 🙏 Compartir mejoras que realices
- 📝 Reportar bugs o sugerencias

---

## 📊 Tabla Resumen Final

| Característica | `excel_to_latex.py` | `excel_drive_a_latex.py` |
|----------------|:-------------------:|:------------------------:|
| **Instalación** | `pip install pandas openpyxl` | `pip install pandas openpyxl gdown` |
| **Uso local** | ✅ Sí | ✅ Sí |
| **Uso con Drive** | ❌ No | ✅ Sí |
| **Uso con Sheets** | ❌ No | ✅ Sí |
| **Requiere internet** | ❌ No | ✅ Sí |
| **Velocidad** | ⚡ Rápido | 🐌 Medio |
| **Colaboración** | ❌ No | ✅ Sí |
| **Complejidad** | 😊 Simple | 🤓 Media |
| **Recomendado para** | Individual | Equipos |

---

**¿Listo para generar tus requerimientos profesionales?** 🚀

Elige tu script y comienza:

```bash
# Opción 1: Local
python excel_to_latex.py ERS-SGPI.xlsx

# Opción 2: Drive
python excel_drive_a_latex.py "https://docs.google.com/spreadsheets/d/1XRlYe4mO8fZclhQlko7KMrVdtVt_Y9SRpF6PlYTEgwQ/edit"
```

---

**Versión:** 5.0 Final  
**Última actualización:** Febrero 2026  
**Scripts incluidos:** 2 (Local + Drive)  
**Formato de salida:** LaTeX profesional con longtable

¡Éxito con tu tesis! 🎓