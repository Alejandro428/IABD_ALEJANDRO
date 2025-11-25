# Tarea-1-La-Primera-Inspeccion-Proyecto-Analisis-Academico-
// Solución ejercicios //
/* 
    1 : Indicadores_Finales
    2 : Lineas
    3 : Objetivos
    4 : Procesos

        ******PREGUNTA 1******
        ¿Cuál es el separador de columnas (coma , o punto y coma ;)?

        1: (Indicadores_Finales) El primer fichero Indicadores Finales utiliza como separador el ;
        2: (Lineas) El segundo fichero Lineas utiliza como separador la ,
        3: (Objetivos) El tercer fichero Objetivos utiliza la , como separador
        4: (Procesos) El cuarto fichero Procesos utiliza la , como separador

        ******PREGUNTA 2******
        ¿La primera fila contiene los nombres de las columnas (encabezados)? ¿Son claros?

        1: (Indicadores_Finales) La primera columna tiene correctamente la cabecera "Curso", "Identificador", "Indicador"
        2: (Lineas) Si, la primera fila contiene los nombres de las columnas y quedan claros: "Línea", "DescripciónLinea"
        3: (Objetivos) Los nombres de la primera fila quedan claros, aunque ObjetivoPAA no queda muy claro si no sabes que es PAA
        4: (Procesos) Si, son claros: "Proceso", "Descripción"

        ******PREGUNTA 3******
        Inspecciona visualmente las primeras 20-30 filas. ¿Ves valores que te parezcan extraños o que faltan (celdas vacías, "N/A", "s/d")?

        1: (Indicadores_Finales) Los datos parecen correctos, pero algunas celdas están vacías, además, hay algunos valores que parecen claves primarias o tipos que se podrían agrupar de alguna manera. Ejemplo: Columna Identificador con repetidos, Cod_SQ tiene repetidos y Cod_PAA, además de tener repetidos, contiene celdas vacías 
        2: (Lineas) Los valores son correctos, y no hay celdas vacías
        3: (Objetivos) Los valores parecen correctos, no hay celdas vacías, pero se repiten valores linea
        4: (Procesos) Los valores son correctos, lo veo todo normal

        ******PREGUNTA 4******
        ¿Los formatos son consistentes? Por ejemplo, ¿las fechas están siempre como DD/MM/AAAA o a veces cambian?

        1: (Indicadores_Finales) El formato de la fecha siempre es año/día Ej:2022/24, aunque el identificador varía entre valores, a veces tiene 3, otras 5 letras, pero insisto en que se repiten
        2: (Lineas) No hay fechas ni formatos raros, simplemente son ids incrementales
        y descripciones
        3: (Objetivos) Si, los formatos son consistentes
        4: (Procesos) Los formatos parecen correctos, son todos como deberían

        ******PREGUNTA 5******
        Identifica las "claves" o "IDs" que podrían servir para relacionar unos ficheros con otros (ej: id_alumno en el fichero de calificaciones.csv y también en alumnos.csv).

        1: (Indicadores_Finales) La clave en este caso será el identificador (clave única), Cod_SQ (relación con Objetivos y Línea) y Cod_PAA (relación con Procesos)
        2: (Lineas) El id es línea (clave única)
        3: (Objetivos) La clave debería de ser ObjetivoPAA (clave_única), aunque podría ser que línea (clave ajena de Lineas) pueda ser una clave ajena
        4: (Procesos) La clave primaria es "Proceso" (clave única)


*/


# Tarea-2-La-Primera-Inspeccion-Proyecto-Analisis-Academico-
// Solución ejercicios //
/* 
    1 : ALUMNOS
    2 : CALIFICACIONES
    3 : CURSOS
    4 : GRUPOS
    5 : HORAS
    6 : MODULOS

	******PREGUNTA 1******
        ¿Cuál es el separador de columnas (coma , o punto y coma ;)?

        1: (ALUMNOS) El primer fichero ALUMNOS utiliza como separador la coma (,)
        2: (CALIFICACIONES) El segundo fichero CALIFICACIONES utiliza como separador la coma (,)
        3: (CURSOS) El tercer fichero CURSOS utiliza como separador la coma (,)
        4: (GRUPOS) El cuarto fichero GRUPOS utiliza como separador la coma (,)
	5: (HORAS) El quinto fichero HORAS utiliza como separador la coma (,)
        6: (MODULOS) El sexto fichero MODULOS utiliza como separador la coma (,)

	******PREGUNTA 2******
        ¿La primera fila contiene los nombres de las columnas (encabezados)? ¿Son claros?

        1: (ALUMNOS) La primera columna de ALUMNOS tiene correctamente los nombres de las columnas en los encabezados (anyo), (fecha_exportacion), (NIA), (fecha_nac), entre otros. Los nombres quedan claros.

        2: (CALIFICACIONES) La primera columna de CALIFICACIONES tiene correctamente los nombres de las columnas en los encabezados (anyo), (fecha_exportacion), (evaluacion), (alumno), entre otros. Los nombres quedan claros.

        3: (CURSOS) La primera columna de CURSOS tiene correctamente los nombres de las columnas en los encabezados (anyo), (fecha_exportacion), (ensenanza), (codigo), entre otros. Los nombres quedan claros.

        4: (GRUPOS) La primera columna de GRUPOS tiene correctamente los nombres de las columnas en los encabezados (anyo), (fecha_exportacion), (codigo), (nombre), entre otros. Los nombres quedan claros.

        5: (HORAS) La primera columna de HORAS tiene correctamente los nombres de las columnas en los encabezados (codigo), (nombre_cas), (ciclo), (horas), entre otros. Los nombres quedan claros.

        6: (MODULOS) La primera columna de MODULOS tiene correctamente los nombres de las columnas en los encabezados (anyo), (fecha_exportacion), (ensenanza), (curso), entre otros. Los nombres quedan claros.

	******PREGUNTA 3******
        Inspecciona visualmente las primeras 20-30 filas. ¿Ves valores que te parezcan extraños o que faltan (celdas vacías, "N/A", "s/d")?

        1: (ALUMNOS) Los datos parecen correctos, pero algunas celdas están vacías, por ejemplo en municipio_nac hay celdas vacias, en municipio_nac_ext también hay celdas vacías, en provincia_nac también, el ampa tiene algunas vacías, entre otros.

        2: (CALIFICACIONES) Los datos parecen correctos, pero algunas celdas están vacías, por ejemplo en bloque_contenido todas las celdas están vacias, en observaciones hay algunas celdas vacías, y en contenido por norma general hay números, pero a veces pone CV0000, entre otros números.

        3: (CURSOS) Los datos parecen correctos. La columna padre tiene algunas celdas vacías 
        
        4: (GRUPOS) Los valores parecen correctos, solo hay celdas vacías en la columna aula.

        5: (HORAS) Los valores son correctos, pero la columna de código a veces pone número, y otras pone CV0000, TU01CF, entre otros.

        6: (MODULOS) Los valores son correctos, pero la columna de código a veces pone número, y otras pone CV0000, TU01CF, entre otros.

	******PREGUNTA 4******
        ¿Los formatos son consistentes? Por ejemplo, ¿las fechas están siempre como DD/MM/AAAA o a veces cambian?

        1: (ALUMNOS) El formato de la fecha siempre es (fechas formato dd/mm/YYYY HH:MM), lo demás parece correcto

        2: (CALIFICACIONES) El formato de la fecha siempre es (fechas formato dd/mm/YYYY HH:MM), y en contenidos parece que se usan diferentes formatos en la celda, por norma general hay números, pero a veces pone CV0000, entre otros números.

        3: (CURSOS) El campo abreviatura a veces si que tiene una abreviatura correcta (Ej: DAW) pero otras veces se identifica por números (Ej: 20). En nombre_val a veces si se identifica por el nombre del grado, pero otra se pone solo PRIMER, SEGON

        4: (GRUPOS) Los formatos parecen correctos.

        5: (HORAS) Los valores son correctos, pero la columna de código a veces pone número, y otras pone CV0000, TU01CF, entre otros.

        6: (MODULOS) Los valores son correctos, pero la columna de código a veces pone número, y otras pone CV0000, TU01CF, entre otros.

	******PREGUNTA 5******

        Identifica las "claves" o "IDs" que podrían servir para relacionar unos ficheros con otros (ej: id_alumno en el fichero de calificaciones.csv y también en alumnos.csv).

        1: (ALUMNOS) La clave en este caso será NIA en Alumnos

        2: (CALIFICACIONES) La clave en este caso será alumno, que será clave ajena de Alumnos, también el contenido, que es clave ajena de Módulos, que es el código de cada módulo

        3: (CURSOS) La clave debería de ser el código, y también el nombre_cas donde se agrupan varias cosas (cursos, tipo de grado, año, etc), en nombre_val ocurre lo mismo, y posiblemente el padre podría llegar a ser útil como clave, aunque optativa.

        4: (GRUPOS) La clave primaria es codigo, que representa el código del grupo.

        5: (HORAS) La clave es codigo, es clave ajena de módulos. 

        6: (MODULOS) La clave primaria es codigo, que representa el código del módulo. 


*/

# Tarea-2-Arquitectura-de-Data-Lakehouse-
// Solución de ejercicios //

```

\Capa_Bronce
│
├── \Evaluaciones
│   └── \2024_2025
│       ├── \1ºTrimestre
│       │   ├── alumnos.csv
│       │   ├── calificaciones.csv
│       │   ├── cursos.csv
│       │   ├── grupos.csv
│       │   └── modulos.csv
│       │
│       ├── \2ºTrimestre
│       │   ├── alumnos.csv
│       │   ├── calificaciones.csv
│       │   ├── cursos.csv
│       │   ├── grupos.csv
│       │   └── modulos.csv
│       │
│       └── \3ºTrimestre
│           ├── alumnos.csv
│           ├── calificaciones.csv
│           ├── cursos.csv
│           ├── grupos.csv
│           └── modulos.csv
│
└── \Indicadores
    └── \2024_2025
        └── indicadores.csv


\Capa_Plata
│
├── \Evaluaciones
│   └── \2024_2025
│       ├── \1ºTrimestre
│       │   ├── alumnos_limpios.csv
│       │   ├── calificaciones_limpias.csv
│       │   ├── cursos_limpios.csv
│       │   ├── grupos_limpios.csv
│       │   └── modulos_limpios.csv
│       │
│       ├── \2ºTrimestre
│       │   ├── alumnos_limpios.csv
│       │   ├── calificaciones_limpias.csv
│       │   ├── cursos_limpios.csv
│       │   ├── grupos_limpios.csv
│       │   └── modulos_limpios.csv
│       │
│       └── \3ºTrimestre
│           ├── alumnos_limpios.csv
│           ├── calificaciones_limpias.csv
│           ├── cursos_limpios.csv
│           ├── grupos_limpios.csv
│           └── modulos_limpios.csv
│
└── \Indicadores
    └── \2024_2025
        └── indicadores_limpios.csv


\Capa_Oro
│
├── \Datasets_PowerBI
│   └── datos.txt
│
└── \Power_BI\

```
