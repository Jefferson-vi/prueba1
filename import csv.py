import csv
def leer_datos_csv(archivo_csv):
  """
  Función para leer datos de un archivo CSV y almacenarlos en una lista de diccionarios.

  Parámetros:
    archivo_csv (str): Ruta del archivo CSV a leer.

  Devuelve:
    list: Lista de diccionarios donde cada diccionario representa una fila del archivo CSV.
  """
  datos = []
  with open(archivo_csv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for fila in reader:
      datos.append(fila)
  return datos
archivo_csv = "data_csv.csv"  
datos = leer_datos_csv(archivo_csv)
misiones_diplomaticas = []
presupuestos = []

for fila in datos:
  mision_diplomatica = fila["miciones diplomaticas"]
  presupuesto = fila["Presupuesto Asignado"]

  misiones_diplomaticas.append(mision_diplomatica)
  presupuestos.append(presupuesto)
print("Misiones Diplomáticas:")

for mision in misiones_diplomaticas:
  print(mision)

print("\nPresupuestos Asignados:")
for presupuesto in presupuestos:
  print(presupuesto)