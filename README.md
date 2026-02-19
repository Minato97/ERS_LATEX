🔧 Conversor Excel / Google Drive a LaTeX
Versión 5.0 – Soporte Google Drive + Categoría en RNF

Script profesional para convertir requerimientos (funcionales y no funcionales) desde:

📄 Archivo Excel local (.xlsx)

☁️ Google Drive (archivo compartido)

📊 Google Sheets (exportación automática a Excel)

Genera automáticamente:

requerimientos_funcionales.tex

requerimientos_no_funcionales.tex

Usando longtable para evitar cortes de página y mejorar la presentación académica.

🚀 Novedades de la Versión 5.0
✅ 1. Soporte completo para Google Drive y Google Sheets

Ahora puedes ejecutar el script usando:

python excel_drive_a_latex.py ID_DRIVE

o directamente con el link:

python excel_drive_a_latex.py https://docs.google.com/spreadsheets/d/ID/edit

El script:

Detecta automáticamente si es Google Sheets

Descarga el archivo

Lo convierte a .xlsx

Genera los .tex

✅ 2. Nueva columna "Categoría" en RNF

Si el Excel contiene la columna:

Categoria

Y el requerimiento es No Funcional (RNF), el script agregará automáticamente:

\textbf{Categoría:} & Seguridad \\

Esto solo aplica a la hoja:

Req. No Funcionales
✅ 3. Uso de longtable (sin cortes de página)

Cada requerimiento usa:

\begin{longtable}{|p{0.28\textwidth}|p{0.67\textwidth}|}

Ventajas:

No se cortan en el pie de página

Se repiten encabezados automáticamente

Muestra "Continúa en la siguiente página"

Ideal para tesis largas

📂 Estructura Esperada del Excel
Hoja 1:
Req. Funcionales
Hoja 2:
Req. No Funcionales
📋 Columnas Detectadas Automáticamente

El script incluye los campos si existen:

Id

Nombre

Descripción / Descripcion

Datos de entrada

Datos de Salida

Pre-condiciones

Post Condiciones

Criterios de aceptacion

Proceso

Proceso Alternativo

Prioridad

Estabilidad

Fuente del requerimiento

Requerimientos relacionados

Categoria (solo RNF)

Si una columna no existe o está vacía, simplemente no se imprime.

📦 Instalación
1️⃣ Dependencias Python
pip install pandas openpyxl gdown
2️⃣ LaTeX (si compilas PDF)

Ubuntu/Debian:

sudo apt install texlive-latex-base texlive-latex-extra
▶️ Uso del Script
🔹 Caso 1: Excel local
python excel_drive_a_latex.py ERS_SMMY.xlsx
🔹 Caso 2: Excel local con carpeta de salida
python excel_drive_a_latex.py ERS_SMMY.xlsx latex_output_final
🔹 Caso 3: Google Drive (archivo compartido)
python excel_drive_a_latex.py 1AbCdEfGhIjKlMnOpQrStUvWxYz
🔹 Caso 4: Google Sheets (link completo)
python excel_drive_a_latex.py https://docs.google.com/spreadsheets/d/ID/edit
📄 Archivos Generados

En la carpeta:

latex_output_final/

Se crean:

requerimientos_funcionales.tex

requerimientos_no_funcionales.tex

🧠 Procesamiento Inteligente del Texto

El script:

✔ Escapa caracteres especiales de LaTeX:

&

%

$

_

#

{ }

~

^

\

✔ Convierte saltos de línea del Excel en:
\newline
✔ Limpia líneas vacías
🧩 Integración en tu Tesis

En tu documento principal:

\usepackage{longtable}
\usepackage{array}

\setlength{\LTpre}{1em}
\setlength{\LTpost}{1em}
\renewcommand{\arraystretch}{1.3}

Luego:

\chapter{Especificación de Requerimientos}

\section{Requerimientos Funcionales}
\input{latex_output_final/requerimientos_funcionales.tex}

\newpage

\section{Requerimientos No Funcionales}
\input{latex_output_final/requerimientos_no_funcionales.tex}
📊 Flujo Completo
Excel / Google Sheets
        ↓
Script python
        ↓
Archivos .tex
        ↓
pdflatex
        ↓
PDF listo para tesis
🛠 Personalización de Columnas

Si deseas modificar el ancho de columnas:

En el script:

\begin{longtable}{|p{0.28\textwidth}|p{0.67\textwidth}|}

Puedes cambiar a:

0.25 / 0.70 → Más espacio para contenido

0.30 / 0.65 → Más espacio para etiquetas

⚠️ Errores Comunes
❌ "No se pudo interpretar el archivo"

Revisa:

Que el ID de Drive esté bien copiado

Que el archivo esté compartido públicamente

❌ Underfull \hbox

Solo advertencia visual. No afecta el PDF.

❌ Caracteres raros

Asegúrate de tener:

\usepackage[utf8]{inputenc}
📌 Recomendaciones

Ejecuta pdflatex dos veces

Guarda respaldo del Excel

Usa control de versiones (Git)

No edites manualmente los .tex generados

🎓 Ideal para

Tesis

SRS IEEE 830

Documentación académica

Proyectos de Ingeniería de Software

Entregables formales

🏁 Versión

Script: excel_drive_a_latex.py
Versión: 5.0
Soporte: Excel local + Google Drive + Google Sheets
Salida: Tablas LaTeX con longtable
Compatibilidad: Tesis académicas
