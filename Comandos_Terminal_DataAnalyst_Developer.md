# Comandos Terminal para Análisis de Datos y Desarrollo de Software
## Guía Práctica para Linux/Ubuntu

**Fecha creada:** Julio 2026  
**Contexto:** Desarrollo en GCF (Neurail, COGI), Python, Git, análisis de datos  
**Objetivo:** Dominar la terminal para flujos cotidianos en Linux

---

## 📋 Índice
1. [Navegación y Archivos](#navegación-y-archivos)
2. [Manipulación de Archivos de Datos](#manipulación-de-archivos-de-datos)
3. [Python y Entornos](#python-y-entornos)
4. [Git y Control de Versiones](#git-y-control-de-versiones)
5. [Búsqueda y Filtrado](#búsqueda-y-filtrado)
6. [Monitoreo del Sistema](#monitoreo-del-sistema)
7. [Scripting Básico](#scripting-básico)
8. [Casos de Uso Reales](#casos-de-uso-reales)

---

## Navegación y Archivos

### Listar archivos con detalles
```bash
ls -lah
```
**Explicación:** `-l` (largo), `-a` (todos, incluyendo ocultos), `-h` (tamaño legible)  
**Contexto:** Ver estructura de un proyecto GCF
```bash
ls -lah ~/projects/neurail_libs/
```

### Cambiar directorio
```bash
cd /ruta/al/proyecto
cd ..          # Subir un nivel
cd -           # Volver al directorio anterior
cd ~           # Ir al home
```
**Contexto real:**
```bash
cd ~/projects/neurail_data_checker
cd ..
cd ~/projects/cogi_wui
```

### Crear directorios
```bash
mkdir nombre_carpeta
mkdir -p ruta/profunda/carpeta   # Crea padres si no existen
```
**Contexto:** Crear estructura de proyecto nuevo
```bash
mkdir -p ~/projects/my_new_project/{data,scripts,output}
```

### Copiar archivos/carpetas
```bash
cp archivo.txt copia_archivo.txt
cp -r carpeta/ copia_carpeta/     # Recursivo (carpetas y contenido)
```
**Contexto:** Backup de datos o replicar estructura
```bash
cp datos_sensor.csv datos_sensor_backup.csv
cp -r ~/projects/neurail_libs ~/projects/neurail_libs_backup
```

### Mover/Renombrar
```bash
mv archivo_viejo.txt archivo_nuevo.txt   # Renombrar
mv archivo.txt ~/proyectos/              # Mover a carpeta
```
**Contexto:**
```bash
mv datos_raw.csv datos_procesados.csv
mv ~/Downloads/sensor_log.json ~/projects/neurail_data_checker/data/
```

### Eliminar archivos
```bash
rm archivo.txt
rm -r carpeta/        # Recursivo (cuidado!)
rm -i archivo.txt     # Pide confirmación (seguro)
```
**Contexto:**
```bash
rm datos_temporales.csv
rm -r ~/projects/proyecto_abandonado/
```

### Ver tamaño de archivos/carpetas
```bash
du -sh carpeta/          # Resumen, tamaño legible
du -sh *                 # Tamaño de todo en directorio actual
ls -lhS                  # Listar ordenado por tamaño (mayor primero)
```
**Contexto:**
```bash
du -sh ~/projects/neurail_libs/
du -sh ~/projects/*      # Ver tamaño de todos los proyectos
```

### Crear archivo vacío / tocar
```bash
touch nuevo_archivo.txt
```

---

## Manipulación de Archivos de Datos

### Ver contenido de archivo
```bash
cat archivo.txt              # Mostrar completo
head -n 10 archivo.txt       # Primeras 10 líneas
tail -n 10 archivo.txt       # Últimas 10 líneas
less archivo.txt             # Navegable (presiona 'q' para salir)
```
**Contexto:** Inspeccionar datos de sensores
```bash
head -n 20 sensor_data.csv          # Ver primeras líneas de CSV
tail -n 5 sensor_log.json           # Ver últimas líneas de JSON
less ~/projects/neurail_data_checker/output/report.txt
```

### Contar líneas
```bash
wc -l archivo.txt
```
**Contexto:**
```bash
wc -l datos_sensor_fbg.csv          # ¿Cuántos registros tengo?
```

### Búsqueda dentro de archivos (grep)
```bash
grep "patrón" archivo.txt           # Buscar líneas que contengan "patrón"
grep -i "patrón" archivo.txt        # Case-insensitive
grep -n "patrón" archivo.txt        # Mostrar número de línea
grep -c "patrón" archivo.txt        # Contar coincidencias
grep -v "patrón" archivo.txt        # Invertir (líneas SIN patrón)
```
**Contexto real:**
```bash
grep "ERROR" sensor_log.json        # Buscar errores en logs
grep -i "FBG" datos_neurail.csv     # Buscar referencias a sensores FBG
grep -n "timeout" /var/log/syslog   # Buscar timeouts en logs del sistema
grep -c "anomaly" report.txt        # Contar anomalías detectadas
```

### Procesar archivos CSV/JSON línea a línea
```bash
cat archivo.csv | head -5    # Ver primeras 5 líneas
```

### Extraer columnas de CSV
```bash
cut -d',' -f1,3 datos.csv    # Extraer columnas 1 y 3 (delimitador coma)
```
**Contexto:**
```bash
cut -d',' -f1,4,5 sensor_readings.csv > timestamp_value.csv
```

### Ordenar
```bash
sort archivo.txt             # Orden alfabético
sort -n archivo.txt          # Orden numérico
sort -r archivo.txt          # Orden inverso
```
**Contexto:**
```bash
sort -n valores_sensor.txt   # Ordenar valores de sensor
```

### Eliminar duplicados
```bash
sort archivo.txt | uniq
sort -u archivo.txt          # Más directo
```

### Contar ocurrencias únicas
```bash
sort archivo.txt | uniq -c   # Contar repeticiones
```
**Contexto:**
```bash
sort sensor_types.txt | uniq -c | sort -rn    # Ver qué sensor aparece más
```

### Pipes (encadenar comandos)
```bash
cat datos.csv | grep "sensor_1" | wc -l       # Contar registros de sensor_1
```
**Contexto:**
```bash
cat neurail_sensor_data.csv | grep "CH0" | grep -c "anomaly"
```

### Sustituir texto (sed)
```bash
sed 's/viejo/nuevo/' archivo.txt              # Reemplazar primera ocurrencia por línea
sed 's/viejo/nuevo/g' archivo.txt             # Reemplazar TODAS (global)
sed -i 's/viejo/nuevo/g' archivo.txt          # Modificar archivo in-place
```
**Contexto:**
```bash
sed 's/sensor_viejo/sensor_nuevo/g' datos.csv > datos_actualizado.csv
sed -i 's/UTC/CET/g' log_timestamps.txt       # Actualizar zona horaria
```

---

## Python y Entornos

### Activar entorno conda
```bash
conda activate dataenv           # Activar tu entorno dataenv
conda activate base              # Volver a base
conda deactivate                 # Desactivar actual
```

### Listar entornos disponibles
```bash
conda env list
```

### Crear entorno nuevo
```bash
conda create -n nombre_env python=3.11
```
**Contexto:**
```bash
conda create -n neurail_dev python=3.11 pandas numpy matplotlib
```

### Instalar paquetes
```bash
pip install paquete              # Instalar en entorno activo
pip install paquete==1.2.3       # Versión específica
pip install -r requirements.txt  # Desde archivo
```

### Listar paquetes instalados
```bash
pip list
pip freeze > requirements.txt    # Guardar dependencias
```

### Ejecutar script Python
```bash
python script.py
python -u script.py              # Unbuffered (output inmediato)
```

### Python interactivo
```bash
python
# o para Jupyter en la terminal
jupyter lab
jupyter notebook
```

### Ejecutar módulo Python directamente
```bash
python -m http.server 8000      # Servidor HTTP simple
python -m json.tool archivo.json # Validar/formatear JSON
```
**Contexto:**
```bash
python -m json.tool sensor_config.json > sensor_config_formatted.json
```

---

## Git y Control de Versiones

### Verificar estado del repositorio
```bash
git status
```

### Ver histórico de commits
```bash
git log --oneline              # Resumen
git log --oneline -10          # Últimos 10
git log --graph --oneline --all # Visualización de ramas
```

### Ver cambios
```bash
git diff                        # Cambios no staged
git diff --staged               # Cambios staged
git diff HEAD~1                 # Comparar con commit anterior
```

### Agregar cambios
```bash
git add archivo.py
git add -A                      # Agregar todos
git add .                       # Agregar todos en directorio actual
```

### Hacer commit
```bash
git commit -m "Mensaje descriptivo"
git commit -m "tipo: descripción"    # Conventional Commits
```
**Contexto (siguiendo tu convenio):**
```bash
git commit -m "feat: add FBG sensor data validation"
git commit -m "fix: correct timestamp parsing in MQTT handler"
git commit -m "docs: update COGI sensor documentation"
```

### Ver commits de un archivo
```bash
git log --oneline archivo.py
git blame archivo.py             # Ver quién cambió cada línea
```

### Crear/cambiar rama
```bash
git branch nombre-rama
git checkout nombre-rama
git checkout -b nombre-rama      # Crear y cambiar en uno
```
**Contexto:**
```bash
git checkout -b feature/neurail-wp3.2
git checkout -b bugfix/mqtt-timeout
```

### Fusionar ramas
```bash
git merge nombre-rama
```

### Pull/Push desde GitLab GCF
```bash
git pull origin main             # Actualizar desde servidor
git push origin nombre-rama      # Enviar rama
```

### Ver remotes configurados
```bash
git remote -v
```

### Descargar repositorio
```bash
git clone git@gitlab.gcf.it:grupo/neurail_libs.git
```

---

## Búsqueda y Filtrado

### Buscar archivos por nombre
```bash
find . -name "*.csv"            # Buscar CSVs en directorio actual
find ~ -name "sensor*.json"     # Buscar JSONs que empiezan con "sensor"
find . -name "*.py" -type f     # Solo archivos (no directorios)
```
**Contexto real:**
```bash
find ~/projects/neurail_data_checker -name "*.csv"
find ~/projects -name "requirements.txt"
find . -name "*.log" -type f | grep -i error
```

### Buscar texto en múltiples archivos
```bash
grep -r "patrón" directorio/
grep -ri "TODO" ~/projects/      # Case-insensitive, recursivo
```
**Contexto:**
```bash
grep -r "MQTT" ~/projects/neurail_libs/
grep -ri "fixme" ~/projects/cogi_wui/
```

### Buscar archivos modificados en las últimas 24 horas
```bash
find . -mtime -1                 # Modified in last 1 day
find . -mmin -60                 # Modified in last 60 minutes
```

### Listar archivos de un tipo
```bash
find . -type f -name "*.csv" -o -type f -name "*.json"
```

---

## Monitoreo del Sistema

### Ver procesos en ejecución
```bash
ps aux                           # Todos los procesos
ps aux | grep python             # Filtrar Python
ps aux | grep "nombre_script"
```

### Monitoreo en tiempo real
```bash
top                              # Interfaz interactiva (presiona 'q' para salir)
htop                             # Versión mejorada de top (si está instalado)
```

### Matar proceso
```bash
kill PID
kill -9 PID                      # Fuerza kill
pkill nombre_proceso             # Kill por nombre
```
**Contexto:**
```bash
pkill python                     # Matar todos los procesos Python
```

### Ver uso de disco
```bash
df -h                            # Espacio disponible
du -sh ~/projects/               # Tamaño de carpeta de proyectos
```

### Ver consumo de memoria
```bash
free -h
```

### Ver logs del sistema
```bash
tail -f /var/log/syslog         # Monitoreo en vivo (Ctrl+C para salir)
journalctl -xe                   # Logs de systemd
```

---

## Scripting Básico

### Crear script bash simple
```bash
#!/bin/bash
echo "Hola desde terminal"
```
**Guardar como `script.sh` y ejecutar:**
```bash
chmod +x script.sh               # Hacer ejecutable
./script.sh                      # Ejecutar
```

### Script con variables
```bash
#!/bin/bash
archivo=$1
echo "Procesando archivo: $archivo"
wc -l $archivo
```
**Guardar como `contar_lineas.sh`:**
```bash
chmod +x contar_lineas.sh
./contar_lineas.sh datos.csv
```

### Script que busca y procesa
```bash
#!/bin/bash
# Buscar todos los CSVs y contar líneas

for archivo in *.csv; do
    echo "$archivo: $(wc -l < $archivo) líneas"
done
```

### Script con condiciones
```bash
#!/bin/bash
if [ -f "$1" ]; then
    echo "Archivo existe: $1"
    head -5 "$1"
else
    echo "Archivo no encontrado"
fi
```

### Variables de entorno
```bash
export PYTHONPATH=/home/miguel/projects/neurail_libs:$PYTHONPATH
export MQTT_BROKER=mqtt.gcf.local
```

---

## Casos de Uso Reales

### 1. Procesar un CSV: contar registros por sensor
```bash
# Archivo: sensor_readings.csv
# Formato: timestamp,sensor_id,value,status

# Contar registros totales
wc -l sensor_readings.csv

# Contar por sensor_id
cut -d',' -f2 sensor_readings.csv | sort | uniq -c

# Extraer solo registros de sensor "FBG_CH0"
grep "FBG_CH0" sensor_readings.csv > fbg_ch0_only.csv

# Contar anomalías por sensor
grep "anomaly" sensor_readings.csv | cut -d',' -f2 | sort | uniq -c
```

### 2. Monitorear ejecución de script Python en tiempo real
```bash
# Ejecutar Python y monitorear logs simultáneamente (en otra terminal)
python neurail_data_checker.py

tail -f output/processing.log    # En otra terminal
```

### 3. Procesamiento batch de múltiples archivos
```bash
#!/bin/bash
# Procesar todos los CSVs en data/ y guardar en processed/

mkdir -p processed/

for csv_file in data/*.csv; do
    filename=$(basename "$csv_file")
    echo "Procesando $filename..."
    
    # Tu comando aquí, ej:
    grep -v "error" "$csv_file" > "processed/$filename"
    echo "✓ $filename completado"
done

echo "Todos los archivos procesados"
```

### 4. Búsqueda de errores en logs
```bash
# Buscar errores MQTT de las últimas 24h
find ~/projects/neurail_libs -name "*.log" -mtime -1 | xargs grep -i "error"

# Contar por tipo de error
grep -i "error" server.log | grep -o "ERROR:.*" | sort | uniq -c | sort -rn
```

### 5. Backup automático de proyecto
```bash
#!/bin/bash
project_name="neurail_libs"
backup_dir="~/backups"
timestamp=$(date +%Y%m%d_%H%M%S)

mkdir -p "$backup_dir"
cp -r ~/projects/$project_name "$backup_dir/${project_name}_${timestamp}"
echo "Backup completado: ${project_name}_${timestamp}"
```

### 6. Limpiar archivos temporales
```bash
#!/bin/bash
# Eliminar archivos .tmp y __pycache__ recursivamente

find ~/projects -name "*.tmp" -delete
find ~/projects -name "__pycache__" -type d -exec rm -r {} +
find ~/projects -name ".DS_Store" -delete

echo "Archivos temporales eliminados"
```

### 7. Generar reporte de proyecto
```bash
#!/bin/bash
# Resumen rápido de un proyecto

project="$1"
echo "=== Reporte de $project ==="
echo "Archivos Python:"
find "$project" -name "*.py" | wc -l
echo "Líneas de código:"
find "$project" -name "*.py" -exec wc -l {} + | tail -1
echo "Archivos CSV:"
find "$project" -name "*.csv" | wc -l
echo "Tamaño total:"
du -sh "$project"
```

**Ejecutar:**
```bash
chmod +x generar_reporte.sh
./generar_reporte.sh ~/projects/neurail_libs
```

---

## 📌 Tips y Atajos Útiles

| Atajo | Función |
|-------|---------|
| `Ctrl + C` | Cancelar comando en ejecución |
| `Ctrl + Z` | Pausar proceso (luego `fg` para reanudar) |
| `Ctrl + L` | Limpiar pantalla (equivalente a `clear`) |
| `Ctrl + R` | Buscar en histórico de comandos |
| `Tab` | Autocompletar nombre de archivo/comando |
| `!!` | Ejecutar último comando |
| `!$` | Último argumento del comando anterior |
| `^viejo^nuevo` | Ejecutar último comando reemplazando texto |

**Ejemplos:**
```bash
cd /ruta/muy/larga/proyecto  # Lentamente
cd !$                         # Mismo path en cd anterior
python script.py arg1 arg2
vim !$                        # Editar arg2 con vim
```

---

## 🎯 Plan de Práctica Recomendado

**Semana 1:** Navegación y archivos básicos  
- `ls`, `cd`, `cp`, `mv`, `rm` 
- Práctica: organizar ~/projects

**Semana 2:** Manipulación de datos  
- `grep`, `cut`, `sort`, `uniq`, pipes
- Práctica: procesar CSVs reales

**Semana 3:** Git y versionado  
- Status, commits, branches
- Práctica: flujo GCF en GitLab

**Semana 4:** Python + scripting  
- Entornos conda, ejecución
- Primer script bash

**Semana 5+:** Integración  
- Combinar todo en workflows reales
- Automatización de tareas cotidianas

---

**Última actualización:** Julio 2026  
**Próxima revisión sugerida:** Cuando domine las 5 semanas iniciales
