#!/usr/bin/env python3
"""
Script FINAL para convertir requerimientos desde Excel a tablas LaTeX
Versión 4.0 - Corrige problemas de saltos de línea en celdas y bordes de tabla
"""

import pandas as pd
import sys
import os
import re


def escape_latex(text):
    """Escapa caracteres especiales de LaTeX"""
    if pd.isna(text):
        return ""

    text = str(text)

    # Primero, preservar los saltos de línea reales
    text = text.replace('\r\n', '\n')
    text = text.replace('\r', '\n')

    # Diccionario de reemplazos
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def format_text_with_linebreaks(text):
    """
    Formatea texto procesando correctamente los saltos de línea
    CRÍTICO: Usa \newline en lugar de \\ para evitar que el texto
    se desborde a la columna anterior
    """
    if pd.isna(text) or text == "":
        return ""

    text = str(text).strip()

    # Normalizar saltos de línea
    text = text.replace('\r\n', '\n')
    text = text.replace('\r', '\n')

    # Primero escapar caracteres especiales de LaTeX
    text = escape_latex(text)

    # Dividir en líneas
    lines = text.split('\n')

    # Limpiar líneas vacías
    lines = [line.strip() for line in lines if line.strip()]

    # CAMBIO CRÍTICO: Usar \newline en lugar de \\
    # Esto evita que el contenido se desborde a la columna izquierda
    result = ' \\newline '.join(lines)

    return result


def generate_requirement_table_longtable(row: pd.Series, req_type: str = "RF") -> str:
    """
    Genera una tabla LaTeX usando longtable para requerimientos
    Con bordes correctos y sin desbordamiento de contenido
    """

    latex_code = []

    # ID para referencia
    req_id = escape_latex(str(row['Id'])).lower().replace('.', '-')
    req_name = escape_latex(str(row['Nombre']))

    # Inicio de longtable con especificación correcta de columnas
    # IMPORTANTE: El | al final asegura el borde derecho
    latex_code.append(r"\begin{longtable}{|p{0.28\textwidth}|p{0.67\textwidth}|}")
    latex_code.append(r"\caption{" + req_name + r"} \label{tab:" + req_id + r"} \\")
    latex_code.append(r"\hline")

    # Encabezado que se repite en cada página
    latex_code.append(r"\endfirsthead")
    latex_code.append(r"\multicolumn{2}{c}%")
    latex_code.append(r"{\tablename\ \thetable\ -- \textit{Continuación}} \\")
    latex_code.append(r"\hline")
    latex_code.append(r"\endhead")

    # Pie que aparece al final de cada página excepto la última
    latex_code.append(r"\hline")
    latex_code.append(r"\multicolumn{2}{r}{\textit{Continúa en la siguiente página}} \\")
    latex_code.append(r"\endfoot")

    # Pie final
    latex_code.append(r"\hline")
    latex_code.append(r"\endlastfoot")

    # ID del requerimiento
    latex_code.append(r"\textbf{Id del requerimiento:} & " + escape_latex(str(row['Id'])) + r" \\")
    latex_code.append(r"\hline")

    # Nombre
    latex_code.append(r"\textbf{Nombre:} & " + req_name + r" \\")
    latex_code.append(r"\hline")

    # Tipo (solo para RNF)
    if req_type == "RNF" and 'Tipo' in row.index and not pd.isna(row.get('Tipo', '')):
        tipo = escape_latex(str(row['Tipo']))
        latex_code.append(r"\textbf{Tipo:} & " + tipo + r" \\")
        latex_code.append(r"\hline")

    # Descripción
    desc_col = 'Descripción' if 'Descripción' in row.index else 'Descripcion'
    if desc_col in row.index and not pd.isna(row[desc_col]):
        descripcion = format_text_with_linebreaks(row[desc_col])
        latex_code.append(r"\textbf{Descripción:} & " + descripcion + r" \\")
        latex_code.append(r"\hline")

    # Datos de entrada (solo RF)
    if 'Datos de entrada' in row.index and not pd.isna(row.get('Datos de entrada', '')):
        datos_entrada = format_text_with_linebreaks(row['Datos de entrada'])
        latex_code.append(r"\textbf{Datos de entrada:} & " + datos_entrada + r" \\")
        latex_code.append(r"\hline")

    # Datos de salida (solo RF)
    if 'Datos de Salida' in row.index and not pd.isna(row.get('Datos de Salida', '')):
        datos_salida = format_text_with_linebreaks(row['Datos de Salida'])
        latex_code.append(r"\textbf{Datos de salida:} & " + datos_salida + r" \\")
        latex_code.append(r"\hline")

    # Pre-condiciones
    if 'Pre-condiciones' in row.index and not pd.isna(row.get('Pre-condiciones', '')):
        precondiciones = format_text_with_linebreaks(row['Pre-condiciones'])
        latex_code.append(r"\textbf{Pre-condiciones:} & " + precondiciones + r" \\")
        latex_code.append(r"\hline")

    # Post-condiciones
    if 'Post Condiciones' in row.index and not pd.isna(row.get('Post Condiciones', '')):
        postcondiciones = format_text_with_linebreaks(row['Post Condiciones'])
        latex_code.append(r"\textbf{Post-condiciones:} & " + postcondiciones + r" \\")
        latex_code.append(r"\hline")

    # Criterios de aceptación (solo RNF)
    if 'Criterios de aceptacion' in row.index and not pd.isna(row.get('Criterios de aceptacion', '')):
        criterios = format_text_with_linebreaks(row['Criterios de aceptacion'])
        latex_code.append(r"\textbf{Criterios de aceptación:} & " + criterios + r" \\")
        latex_code.append(r"\hline")

    # Proceso (solo RF)
    if 'Proceso' in row.index and not pd.isna(row.get('Proceso', '')):
        proceso = format_text_with_linebreaks(row['Proceso'])
        latex_code.append(r"\textbf{Proceso:} & " + proceso + r" \\")
        latex_code.append(r"\hline")

    # Proceso Alternativo (solo RF)
    if 'Proceso Alternativo' in row.index and not pd.isna(row.get('Proceso Alternativo', '')):
        proceso_alt = format_text_with_linebreaks(row['Proceso Alternativo'])
        latex_code.append(r"\textbf{Proceso Alternativo:} & " + proceso_alt + r" \\")
        latex_code.append(r"\hline")

    # Prioridad
    if 'Prioridad' in row.index and not pd.isna(row.get('Prioridad', '')):
        prioridad = escape_latex(str(row['Prioridad']))
        latex_code.append(r"\textbf{Prioridad:} & " + prioridad + r" \\")
        latex_code.append(r"\hline")

    # Estabilidad
    if 'Estabilidad' in row.index and not pd.isna(row.get('Estabilidad', '')):
        estabilidad = escape_latex(str(row['Estabilidad']))
        latex_code.append(r"\textbf{Estabilidad:} & " + estabilidad + r" \\")
        latex_code.append(r"\hline")

    # Fuente del requerimiento
    if 'Fuente del requerimiento' in row.index and not pd.isna(row.get('Fuente del requerimiento', '')):
        fuente = escape_latex(str(row['Fuente del requerimiento']))
        latex_code.append(r"\textbf{Fuente del requerimiento:} & " + fuente + r" \\")
        latex_code.append(r"\hline")

    # Requerimientos relacionados
    if 'Requerimientos relacionados' in row.index and not pd.isna(row.get('Requerimientos relacionados', '')):
        req_relacionados = escape_latex(str(row['Requerimientos relacionados']))
        latex_code.append(r"\textbf{Requerimientos relacionados:} & " + req_relacionados + r" \\")
        latex_code.append(r"\hline")

    # Fin de longtable
    latex_code.append(r"\end{longtable}")
    latex_code.append("")  # Línea en blanco
    latex_code.append(r"\vspace{0.5cm}")  # Espacio entre tablas
    latex_code.append("")

    return "\n".join(latex_code)


def generate_all_requirements(excel_file: str, output_dir: str = "."):
    """Genera archivos LaTeX para todos los requerimientos del Excel"""

    os.makedirs(output_dir, exist_ok=True)
    xl_file = pd.ExcelFile(excel_file)

    # Procesar Requerimientos Funcionales
    if 'Req. Funcionales' in xl_file.sheet_names:
        df_rf = pd.read_excel(excel_file, sheet_name='Req. Funcionales')

        with open(os.path.join(output_dir, 'requerimientos_funcionales.tex'), 'w', encoding='utf-8') as f:
            f.write("% Requerimientos Funcionales\n")
            f.write("% Generado automáticamente desde Excel\n\n")

            for idx, row in df_rf.iterrows():
                if pd.notna(row['Id']):
                    f.write(generate_requirement_table_longtable(row, "RF"))
                    f.write("\n")

        print(f"✓ Generados {len(df_rf)} requerimientos funcionales")

    # Procesar Requerimientos No Funcionales
    if 'Req. No Funcionales' in xl_file.sheet_names:
        df_rnf = pd.read_excel(excel_file, sheet_name='Req. No Funcionales')

        with open(os.path.join(output_dir, 'requerimientos_no_funcionales.tex'), 'w', encoding='utf-8') as f:
            f.write("% Requerimientos No Funcionales\n")
            f.write("% Generado automáticamente desde Excel\n\n")

            for idx, row in df_rnf.iterrows():
                if pd.notna(row['Id']):
                    f.write(generate_requirement_table_longtable(row, "RNF"))
                    f.write("\n")

        print(f"✓ Generados {len(df_rnf)} requerimientos no funcionales")

    # Generar archivo principal mejorado
    with open(os.path.join(output_dir, 'todos_los_requerimientos.tex'), 'w', encoding='utf-8') as f:
        f.write(r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\usepackage{longtable}
\usepackage{array}
\usepackage{booktabs}

\geometry{margin=2.5cm}

% Configuración para mejor espaciado en tablas
\setlength{\LTpre}{1em}
\setlength{\LTpost}{1em}
\renewcommand{\arraystretch}{1.3}

\title{Especificación de Requerimientos del Sistema}
\author{}
\date{}

\begin{document}

\maketitle
\tableofcontents
\newpage

\section{Requerimientos Funcionales}

\input{requerimientos_funcionales.tex}

\newpage
\section{Requerimientos No Funcionales}

\input{requerimientos_no_funcionales.tex}

\end{document}
""")

    print(f"\n✓ Archivo principal generado: todos_los_requerimientos.tex")
    print(f"\nPara compilar el documento completo, ejecuta:")
    print(f"  cd {output_dir}")
    print(f"  pdflatex todos_los_requerimientos.tex")
    print(f"  pdflatex todos_los_requerimientos.tex  # Segunda pasada")


def main():
    if len(sys.argv) < 2:
        print("Uso: python excel_to_latex_final.py <archivo_excel> [directorio_salida]")
        print("\nEjemplo:")
        print("  python excel_to_latex_final.py ERS-SGPI.xlsx output/")
        sys.exit(1)

    excel_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "latex_output_final"

    if not os.path.exists(excel_file):
        print(f"Error: No se encuentra el archivo {excel_file}")
        sys.exit(1)

    print(f"Procesando: {excel_file}")
    print(f"Directorio de salida: {output_dir}\n")

    generate_all_requirements(excel_file, output_dir)

    print("\n¡Proceso completado exitosamente!")


if __name__ == "__main__":
    main()
