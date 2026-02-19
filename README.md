# 🔧 Conversor Excel a LaTeX - VERSIÓN CORREGIDA

## ✅ Problemas Solucionados

Esta versión corrige los siguientes problemas que tenía la versión anterior:

1. **✓ Saltos de línea correctos**: Los saltos de línea del Excel ahora se convierten correctamente a `\\` en LaTeX
2. **✓ Sin cortes de página**: Uso de `longtable` en lugar de `table` para que las tablas continúen en la siguiente página
3. **✓ Mejor espaciado**: Texto con espaciado adecuado, no amontonado
4. **✓ 106 páginas**: Mayor claridad y legibilidad (vs. 49 páginas anteriores comprimidas)

## 📦 Archivos Incluidos

### Scripts Python
- **`excel_to_latex_fixed.py`** - Script corregido (USAR ESTE)
- `excel_to_latex.py` - Versión original (solo referencia)
- `excel_to_latex_v2.py` - Versión con casos de uso (solo referencia)

### Archivos LaTeX Generados (carpeta `latex_output_fixed/`)
- `requerimientos_funcionales.tex` - 41 requerimientos funcionales
- `requerimientos_no_funcionales.tex` - 13 requerimientos no funcionales
- `todos_los_requerimientos.tex` - Documento principal completo
- `todos_los_requerimientos.pdf` - **PDF FINAL (106 páginas)**
- `ejemplo_mejoras.pdf` - Documento explicativo de las mejoras

## 🚀 Uso del Script Corregido

### Instalación de Dependencias

```bash
# Python y pandas
pip install pandas openpyxl --break-system-packages

# LaTeX (si no lo tienes)
sudo apt-get install texlive-latex-base texlive-latex-extra
```

### Generar Tablas LaTeX

```bash
# Sintaxis básica
python3 excel_to_latex.py <archivo_excel> [directorio_salida]

# Ejemplo con tu archivo
python3 excel_to_latex.py ERS-SGPI.xlsx mi_tesis/requerimientos/

# Usar directorio por defecto (latex_output_fixed/)
python3 excel_to_latex.py ERS-SGPI.xlsx
```

### Compilar a PDF

```bash
cd latex_output_fixed/

# Primera pasada
pdflatex todos_los_requerimientos.tex

# Segunda pasada (para referencias cruzadas)
pdflatex todos_los_requerimientos.tex
```

## 📊 Ejemplo de Salida

### Antes (Problemas) ❌
```latex
\textbf{Criterios de aceptación:} & Los usuarios pueden navegar\\ Los textos tienen significado\\ \\
```
**Problema**: Los `\\` aparecían literalmente en el texto

### Después (Corregido) ✅
```latex
\textbf{Criterios de aceptación:} & Los usuarios pueden navegar entre módulos sin perderse. \\ 
Los textos, botones e iconos tienen significado claro. \\ 
Los procesos principales se completan en menos de 3 pasos. \\
```
**Resultado**: Saltos de línea correctos y legibles

## 🎯 Características Principales

### 1. Uso de `longtable`

```latex
\begin{longtable}{|p{0.28\textwidth}|p{0.67\textwidth}|}
% La tabla puede ocupar múltiples páginas sin cortarse
\end{longtable}
```

**Ventajas:**
- ✅ No se corta en el pie de página
- ✅ Encabezados se repiten en cada página
- ✅ Muestra "Continúa en la siguiente página"
- ✅ Ideal para requerimientos largos

### 2. Procesamiento de Saltos de Línea

El script detecta y convierte:
- `\n` del Excel → `\\` de LaTeX
- `\r\n` del Excel → `\\` de LaTeX
- Múltiples saltos → Espaciado correcto

### 3. Espaciado Mejorado

```latex
\setlength{\LTpre}{1em}           % Espacio antes de tabla
\setlength{\LTpost}{1em}          % Espacio después de tabla
\renewcommand{\arraystretch}{1.3} % Altura de filas
\vspace{0.5cm}                    % Entre tablas
```

## 📋 Formato de Requerimientos

### Requerimientos Funcionales (RF)
Incluye:
- Id del requerimiento
- Nombre
- Descripción
- Datos de entrada/salida
- Pre-condiciones/Post-condiciones
- Proceso y Proceso Alternativo
- Prioridad y Estabilidad
- Fuente del requerimiento
- Requerimientos relacionados

### Requerimientos No Funcionales (RNF)
Incluye:
- Id del requerimiento
- Nombre
- Tipo
- Descripción
- Pre-condiciones/Post-condiciones
- Criterios de aceptación
- Prioridad y Estabilidad

## 🔍 Comparación de Resultados

| Aspecto | Versión Original | Versión Corregida |
|---------|------------------|-------------------|
| Saltos de línea | Mostraba `\\` literal | Procesa correctamente |
| Cortes de página | Se cortaban las tablas | Continúa sin cortes |
| Espaciado | Texto amontonado | Espaciado adecuado |
| Páginas totales | 49 páginas | 106 páginas |
| Legibilidad | Regular | Excelente |
| Tabla usada | `table` | `longtable` |

## 📝 Integración en tu Tesis

### Preámbulo de tu Documento

```latex
\documentclass[12pt]{report}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\usepackage{longtable}
\usepackage{array}

\geometry{margin=2.5cm}

% Configuración para tablas
\setlength{\LTpre}{1em}
\setlength{\LTpost}{1em}
\renewcommand{\arraystretch}{1.3}
```

### Incluir los Requerimientos

```latex
\chapter{Especificación de Requerimientos}

\section{Requerimientos Funcionales}
Los requerimientos funcionales definen las funcionalidades específicas
que debe proporcionar el sistema...

\input{ruta/a/requerimientos_funcionales.tex}

\newpage
\section{Requerimientos No Funcionales}
Los requerimientos no funcionales establecen las restricciones y 
cualidades del sistema...

\input{ruta/a/requerimientos_no_funcionales.tex}
```

## 🎨 Personalización

### Cambiar Ancho de Columnas

En el script `excel_to_latex_fixed.py`, línea ~92:

```python
latex_code.append(r"\begin{longtable}{|p{0.28\textwidth}|p{0.67\textwidth}|}")
#                                        ^^^^              ^^^^
#                                   Columna 1         Columna 2
```

Valores recomendados:
- **0.28 y 0.67**: Balance (actual)
- **0.25 y 0.70**: Más espacio para contenido
- **0.30 y 0.65**: Más espacio para etiquetas

### Agregar Campos Personalizados

Si tu Excel tiene campos adicionales:

```python
# En la función generate_requirement_table_longtable()
# Agregar después de Estabilidad:

if 'Mi_Campo_Nuevo' in row.index and not pd.isna(row.get('Mi_Campo_Nuevo', '')):
    mi_campo = format_text_with_linebreaks(row['Mi_Campo_Nuevo'])
    latex_code.append(r"\textbf{Mi Campo:} & " + mi_campo + r" \\")
    latex_code.append(r"\hline")
```

## 🐛 Solución de Problemas

### Problema: "Underfull \hbox" warnings

**Causa**: LaTeX no puede justificar bien el texto en columnas estrechas

**Solución**: Esto es solo una advertencia, no afecta el PDF. Para reducirlas:
```latex
\usepackage{ragged2e}
% Usar \RaggedRight en columnas
```

### Problema: Tabla muy ancha

**Causa**: Contenido muy largo en alguna celda

**Solución**: Ajustar anchos de columna o usar `\small` en el contenido:
```python
latex_code.append(r"\small " + texto + r" \normalsize \\")
```

### Problema: Caracteres especiales se ven mal

**Causa**: Problemas de codificación

**Solución**: El script ya maneja UTF-8. Si persiste:
```latex
\usepackage[utf8]{inputenc}
```

## 📈 Estadísticas del Procesamiento

```
Archivo procesado: ERS-SGPI.xlsx
├── Requerimientos Funcionales: 41
├── Requerimientos No Funcionales: 13
├── Total de requerimientos: 54
└── Páginas generadas: 106
```

## 💡 Mejores Prácticas

1. **Siempre ejecuta pdflatex dos veces** para que las referencias cruzadas funcionen
2. **Revisa el PDF generado** antes de incluirlo en tu tesis
3. **Guarda una copia del Excel original** antes de hacer cambios
4. **Usa control de versiones** (Git) para el Excel y los .tex generados
5. **Compila regularmente** para detectar problemas temprano

## 🔄 Actualizar después de Cambios en el Excel

```bash
# 1. Edita tu archivo Excel
# 2. Regenera los archivos LaTeX
python3 excel_to_latex.py ERS-SGPI.xlsx latex_output_fixed

# 3. Recompila el PDF
cd latex_output_fixed
pdflatex todos_los_requerimientos.tex
pdflatex todos_los_requerimientos.tex
```

## 📧 Notas Importantes

- ✅ Este script está optimizado para el formato de tu Excel específico
- ✅ Los saltos de línea ahora funcionan correctamente
- ✅ Las tablas no se cortan en los pies de página
- ✅ El espaciado es profesional y legible
- ✅ Compatible con tesis y documentos académicos

## 🎓 Ejemplo Real

Ver el archivo **`ejemplo_mejoras.pdf`** incluido para ver:
- Comparación antes/después
- Explicación de las correcciones
- Ejemplos de uso de longtable
- Guía de integración en tesis

---

**Versión del Script**: 3.0 (Corregida)  
**Última actualización**: Febrero 2026  
**Archivo procesado**: ERS-SGPI.xlsx  
**Resultado**: 106 páginas de requerimientos profesionales