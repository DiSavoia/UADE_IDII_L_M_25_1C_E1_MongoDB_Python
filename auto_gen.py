from faker import Faker
import random
from datetime import datetime, timedelta

def generar_productos(n):
    fake = Faker()
    tipos = ['miel', 'harina', 'leche', 'queso', 'huevos', 'verduras']
    calidades = ['pura', '000', 'orgánica', 'premium', 'estándar']

    productos = []
    for _ in range(n):
        producto = {
            "tipo": random.choice(tipos),
            "cantidad": str(random.randint(1, 100)),
            "calidad": random.choice(calidades),
            "precio_final": random.randint(1000, 10000),
            "peso": str(random.randint(1, 200)),
            "fecha_ingreso": fake.date_this_year().isoformat()
        }
        productos.append(producto)

    return productos

def generar_animales(n):
    tipos = ['caballo', 'cerdo', 'perro', 'abeja', 'oveja', 'gallina', 'conejo']
    generos = ['macho', 'hembra']

    animales = []
    for _ in range(n):
        animal = {
            "tipo": random.choice(tipos),
            "peso": random.randint(1, 350),
            "edad": random.randint(1, 25),
            "genero": random.choice(generos)
        }
        animales.append(animal)

    return animales

def generar_cultivos(n):
    fake = Faker()
    tipos = ["Albahaca","Papa","Soja","Tomate","Maiz","Trigo","Algodon"]
    estado = ["En transcurso", "Finalizado"]
    salud = ["Saludable","Plagado"]
 
    cultivos = []
    for _ in range(n):
        cultivo = {
            "tipo": random.choice(tipos),
            "fecha_plantacion": fake.date_this_year().isoformat(),
            "fecha_ultimo_riego": fake.date_this_year().isoformat(),
            "estado_riego": random.choice(estado),
            "fecha_estimada_recoleccion":  fake.date_this_year().isoformat(),
            "estado_salud": random.choice(salud),
            "produccion_estimada": random.randint(1,1000),
            "produccion_acumulada": random.randint(1,1000),
            "precio": random.randint(1000,5000),
           
        }
        cultivos.append(cultivo)
 
    return cultivos

def generar_fecha_aleatoria(fecha_inicio, fecha_fin):
    delta = fecha_fin - fecha_inicio
    dia_aleatorio = random.randint(0, delta.days)
    fecha_aleatoria = fecha_inicio + timedelta(days=dia_aleatorio)
    return fecha_aleatoria

def generar_maquinarias(n):  
    fake = Faker()
    nombres=['Tractor agrícola','Cosechadora de granos','Sembradora neumática','Rastra de discos',
             'Pulverizadora autopropulsada','Enfardadora automática']
    marca = ["John Deere", "Case IH",    "New Holland",    "Massey Ferguson",   "Claas","Challenger"]
    tipo= ['Cosechadoras','Tractores', 'Sembradoras' ,'Rastras', 'Pulverizadoras','Enfardadoras']
   
    fecha_inicio = datetime(2010, 1, 1)
    fecha_fin = datetime(2025, 12, 31)

    productos = []    
    for _ in range(n):      
        producto = {          
                    "Nombre": random.choice(nombres),          
                    "Marca": random.choice(marca),          
                    "Tipo": random.choice(tipo),          
                    "Antiguedad": random.randint(1, 50),      
                    "Fecha Ultima Reparación": generar_fecha_aleatoria(fecha_inicio, fecha_fin),  
                    "Fecha Ultima Revisión": generar_fecha_aleatoria(fecha_inicio, fecha_fin),  
                    "Mantenimiento": fake.boolean(),
                    "Precio": random.randint(12000,90000),
                    "Capacidad de Combustible":random.randint(300,600)
                    }
        productos.append(producto)  
    return productos