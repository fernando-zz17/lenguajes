
import pandas as pd # pyright: ignore[reportMissingModuleSource]
dias = ['lunes','martes','miércoles','jueves','viernes','sabado','domingo']
import os
import json
df = pd.read_csv(r"C:\Users\54296\Desktop\tp2\actividad_2.csv")

print (df.head())

df['timestamp'] = pd.to_datetime(df['timestamp'])

df['dia_semana'] = df ['timestamp'].dt.day_name(locale='es_ES').str.lower()

print(df)


contar_dias = {dia: 0 for dia in dias}

for dia in df ['dia_semana']:
    if dia in contar_dias:
        contar_dias[dia]+=1
        
print("entrenamiento por dias", contar_dias)

dia_max_entrenamiento = max (contar_dias, key=contar_dias.get)

print("dia con mas entrenamientos",dia_max_entrenamiento )




primer_entrenamiento = df ['timestamp'].min()
ultimo_entrenamiento = df ['timestamp'].max()


dias_pasados = (primer_entrenamiento -ultimo_entrenamiento ).days

print (primer_entrenamiento, "primer entreno")
print(ultimo_entrenamiento, "ultimo entreno")
print(dias_pasados, "dias pasados")




conteo_campeones = {}
    
    
for campeon in df ['campeon']:
    if campeon not in conteo_campeones:
        conteo_campeones[campeon]=1
    else:
        conteo_campeones[campeon]+=1

campeon_mas= max(conteo_campeones, key=conteo_campeones.get)
print("entrenamiento por campeones",conteo_campeones)
print("campeon que mas entrenoes", campeon_mas,"con",conteo_campeones[campeon_mas])


conteo = df.groupby('dia_semana').size()

# Calcular promedio general
promedio = conteo.mean()

print("Entrenamientos por día:\n", conteo)
print("\nPromedio de entrenamientos por día:", promedio)



fines_semana = df[df['dia_semana'].isin(['sábado', 'domingo'])]

# Contar cuántas veces entrena cada campeón en fines de semana
conteo_finde = fines_semana['campeon'].value_counts()

# Obtener el campeón que más entrena
campeon_mas_finde = conteo_finde.idxmax()
cantidad = conteo_finde.max()

print("Entrenamientos en fines de semana:\n", conteo_finde)
print("\nEl campeón que más entrena en fines de semana es:", campeon_mas_finde)
print("Cantidad de entrenamientos:", cantidad)

os.makedirs("salida", exist_ok=True)
conteo_campeones = df['campeon'].value_counts().reset_index()
conteo_campeones.columns = ['campeon', 'cantidad']


ruta_salida = os.path.join("salida", "entrenamientos_por_campeon.csv")
conteo_campeones.to_csv(ruta_salida, index=False, encoding='utf-8-sig')

print("Archivo generado en:", ruta_salida)
print(conteo_campeones)


total_registros = len(df)

# Crear estructura de datos para el JSON
resultado = {"total_registros": total_registros, "dias": {}}

# Recorrer los días de la semana
for dia, grupo in df.groupby('dia_semana'):
    conteo_campeones = grupo['campeon'].value_counts().to_dict()
    resultado["dias"][dia] = conteo_campeones

# Crear carpeta "salida" si no existe
os.makedirs("salida", exist_ok=True)

# Guardar como JSON dentro de la carpeta salida
ruta_json = os.path.join("salida", "entrenamientos_por_dia.json")
with open(ruta_json, "w", encoding="utf-8") as archivo:
    json.dump(resultado, archivo, indent=4, ensure_ascii=False)

print("Archivo JSON generado en:", ruta_json)