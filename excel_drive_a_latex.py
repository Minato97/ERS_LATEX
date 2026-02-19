#!/usr/bin/env python3
"""
Script FINAL para convertir requerimientos desde Excel a tablas LaTeX
Versión 5.0 - Soporta Google Drive y Categoría en RNF
"""

import pandas as pd
import sys
import os
import re
import gdown


# ==========================================================
# SOPORTE GOOGLE DRIVE / GOOGLE SHEETS
# ==========================================================

def extract_drive_id(input_value: str):

    match_sheets = re.search(r"spreadsheets/d/([a-zA-Z0-9_-]+)", input_value)
    if match_sheets:
        return match_sheets.group(1), True

    match_drive = re.search(r"/d/([a-zA-Z0-9_-]+)", input_value)
    if match_drive:
        return match_drive.group(1), False

    if len(input_value) > 20 and " " not in input_value and not input_value.endswith(".xlsx"):
        return input_value, False

    return None, None


def download_from_drive(file_id: str, is_sheets: bool):

    if is_sheets:
        url = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=xlsx"
    else:
        url = f"https://drive.google.com/uc?id={file_id}"

    output_name = "temp_excel.xlsx"
    print("Descargando archivo desde Google...")
    gdown.download(url, output_name, quiet=False)

    return output_name


# ==========================================================
# FUNCIONES ORIGINALES (NO SE MODIFICAN)
# ==========================================================

def escape_latex(text):
    if pd.isna(text):
        return ""

    text = str(text)
    text = text.replace('\r\n', '\n')
    text = text.replace('\r', '\n')

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

    if pd.isna(text) or text == "":
        return ""

    text = str(text).strip()
    text = text.replace('\r\n', '\n')
    text = text.replace('\r', '\n')

    text = escape_latex(text)

    lines = text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]

    return ' \\newline '.join(lines)


def generate_requirement_table_longtable(row: pd.Series, req_type: str = "RF") -> str:

    latex_code = []

    req_id = escape_latex(str(row['Id'])).lower().replace('.', '-')
    req_name = escape_latex(str(row['Nombre']))

    latex_code.append(r"\begin{longtable}{|p{0.28\textwidth}|p{0.67\textwidth}|}")
    latex_code.append(r"\caption{" + req_name + r"} \label{tab:" + req_id + r"} \\")
    latex_code.append(r"\hline")

    latex_code.append(r"\endfirsthead")
    latex_code.append(r"\multicolumn{2}{c}%")
    latex_code.append(r"{\tablename\ \thetable\ -- \textit{Continuación}} \\")
    latex_code.append(r"\hline")
    latex_code.append(r"\endhead")

    latex_code.append(r"\hline")
    latex_code.append(r"\multicolumn{2}{r}{\textit{Continúa en la siguiente página}} \\")
    latex_code.append(r"\endfoot")

    latex_code.append(r"\hline")
    latex_code.append(r"\endlastfoot")

    latex_code.append(r"\textbf{Id del requerimiento:} & " + escape_latex(str(row['Id'])) + r" \\")
    latex_code.append(r"\hline")

    latex_code.append(r"\textbf{Nombre:} & " + req_name + r" \\")
    latex_code.append(r"\hline")

    # 👉 NUEVO: Mostrar Categoría en RNF si existe
    if req_type == "RNF" and 'Categoria' in row.index and not pd.isna(row.get('Categoria', '')):
        categoria = escape_latex(str(row['Categoria']))
        latex_code.append(r"\textbf{Categoría:} & " + categoria + r" \\")
        latex_code.append(r"\hline")

    desc_col = 'Descripción' if 'Descripción' in row.index else 'Descripcion'
    if desc_col in row.index and not pd.isna(row[desc_col]):
        descripcion = format_text_with_linebreaks(row[desc_col])
        latex_code.append(r"\textbf{Descripción:} & " + descripcion + r" \\")
        latex_code.append(r"\hline")

    if 'Datos de entrada' in row.index and not pd.isna(row.get('Datos de entrada', '')):
        datos_entrada = format_text_with_linebreaks(row['Datos de entrada'])
        latex_code.append(r"\textbf{Datos de entrada:} & " + datos_entrada + r" \\")
        latex_code.append(r"\hline")

    if 'Datos de Salida' in row.index and not pd.isna(row.get('Datos de Salida', '')):
        datos_salida = format_text_with_linebreaks(row['Datos de Salida'])
        latex_code.append(r"\textbf{Datos de salida:} & " + datos_salida + r" \\")
        latex_code.append(r"\hline")

    if 'Pre-condiciones' in row.index and not pd.isna(row.get('Pre-condiciones', '')):
        precondiciones = format_text_with_linebreaks(row['Pre-condiciones'])
        latex_code.append(r"\textbf{Pre-condiciones:} & " + precondiciones + r" \\")
        latex_code.append(r"\hline")

    if 'Post Condiciones' in row.index and not pd.isna(row.get('Post Condiciones', '')):
        postcondiciones = format_text_with_linebreaks(row['Post Condiciones'])
        latex_code.append(r"\textbf{Post-condiciones:} & " + postcondiciones + r" \\")
        latex_code.append(r"\hline")

    if 'Criterios de aceptacion' in row.index and not pd.isna(row.get('Criterios de aceptacion', '')):
        criterios = format_text_with_linebreaks(row['Criterios de aceptacion'])
        latex_code.append(r"\textbf{Criterios de aceptación:} & " + criterios + r" \\")
        latex_code.append(r"\hline")

    if 'Proceso' in row.index and not pd.isna(row.get('Proceso', '')):
        proceso = format_text_with_linebreaks(row['Proceso'])
        latex_code.append(r"\textbf{Proceso:} & " + proceso + r" \\")
        latex_code.append(r"\hline")

    if 'Proceso Alternativo' in row.index and not pd.isna(row.get('Proceso Alternativo', '')):
        proceso_alt = format_text_with_linebreaks(row['Proceso Alternativo'])
        latex_code.append(r"\textbf{Proceso Alternativo:} & " + proceso_alt + r" \\")
        latex_code.append(r"\hline")

    if 'Prioridad' in row.index and not pd.isna(row.get('Prioridad', '')):
        prioridad = escape_latex(str(row['Prioridad']))
        latex_code.append(r"\textbf{Prioridad:} & " + prioridad + r" \\")
        latex_code.append(r"\hline")

    if 'Estabilidad' in row.index and not pd.isna(row.get('Estabilidad', '')):
        estabilidad = escape_latex(str(row['Estabilidad']))
        latex_code.append(r"\textbf{Estabilidad:} & " + estabilidad + r" \\")
        latex_code.append(r"\hline")

    if 'Fuente del requerimiento' in row.index and not pd.isna(row.get('Fuente del requerimiento', '')):
        fuente = escape_latex(str(row['Fuente del requerimiento']))
        latex_code.append(r"\textbf{Fuente del requerimiento:} & " + fuente + r" \\")
        latex_code.append(r"\hline")

    if 'Requerimientos relacionados' in row.index and not pd.isna(row.get('Requerimientos relacionados', '')):
        req_relacionados = escape_latex(str(row['Requerimientos relacionados']))
        latex_code.append(r"\textbf{Requerimientos relacionados:} & " + req_relacionados + r" \\")
        latex_code.append(r"\hline")

    latex_code.append(r"\end{longtable}")
    latex_code.append("")
    latex_code.append(r"\vspace{0.5cm}")
    latex_code.append("")

    return "\n".join(latex_code)


# ==========================================================
# GENERACIÓN PRINCIPAL
# ==========================================================

def generate_all_requirements(excel_file: str, output_dir: str = "."):

    os.makedirs(output_dir, exist_ok=True)
    xl_file = pd.ExcelFile(excel_file)

    # FUNCIONALES
    if 'Req. Funcionales' in xl_file.sheet_names:
        df_rf = pd.read_excel(excel_file, sheet_name='Req. Funcionales')

        with open(os.path.join(output_dir, 'requerimientos_funcionales.tex'), 'w', encoding='utf-8') as f:
            for idx, row in df_rf.iterrows():
                if pd.notna(row['Id']):
                    f.write(generate_requirement_table_longtable(row, "RF"))

    # NO FUNCIONALES
    if 'Req. No Funcionales' in xl_file.sheet_names:
        df_rnf = pd.read_excel(excel_file, sheet_name='Req. No Funcionales')

        with open(os.path.join(output_dir, 'requerimientos_no_funcionales.tex'), 'w', encoding='utf-8') as f:
            for idx, row in df_rnf.iterrows():
                if pd.notna(row['Id']):
                    f.write(generate_requirement_table_longtable(row, "RNF"))


def main():

    if len(sys.argv) < 2:
        print("Uso: python excel_drive_a_latex.py <archivo.xlsx | ID_DRIVE | LINK_DRIVE>")
        sys.exit(1)

    input_value = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "latex_output_final"

    # Archivo local
    if input_value.endswith(".xlsx") and os.path.exists(input_value):
        excel_file = input_value
    else:
        drive_id, is_sheets = extract_drive_id(input_value)

        if not drive_id:
            print("Error: No se pudo interpretar el archivo de entrada.")
            sys.exit(1)

        excel_file = download_from_drive(drive_id, is_sheets)

    generate_all_requirements(excel_file, output_dir)
    print("Proceso completado exitosamente.")


if __name__ == "__main__":
    main()