import pandas as pd

# Cargar los datos en un DataFrame
data = pd.read_csv("datos_demograficos.csv")

# 1. Contar el número de personas de cada raza
race_counts = data['race'].value_counts()

# 2. Calcular la edad promedio de los hombres
average_age_men = data[data['sex'] == 'Male']['age'].mean()

# 3. Calcular el porcentaje de personas con un grado de licenciatura
bachelors_percentage = (data['education'] == "Bachelors").mean() * 100

# 4. Calcular el porcentaje de personas con una educación avanzada que ganan más de 50k
advanced_education = data[data['education'].isin(["Bachelors", "Masters", "Doctorate"])]
advanced_education_rich_percentage = (advanced_education['salary'] == ">50K").mean() * 100

# 5. Calcular el porcentaje de personas sin una educación avanzada que ganan más de 50k
no_advanced_education = data[~data['education'].isin(["Bachelors", "Masters", "Doctorate"])]
no_advanced_education_rich_percentage = (no_advanced_education['salary'] == ">50K").mean() * 100

# 6. Encontrar el mínimo número de horas que una persona trabaja por semana
min_hours_per_week = data['hours-per-week'].min()

# 7. Calcular el porcentaje de personas que trabajan el mínimo de horas por semana y tienen un salario de más de 50k
min_hours_per_week_rich_percentage = (data[data['hours-per-week'] == min_hours_per_week]['salary'] == ">50K").mean() * 100

# 8. Encontrar el país con el porcentaje más alto de personas que ganan >50k y calcular ese porcentaje
country_max_percentage = data[data['salary'] == ">50K"]['native-country'].value_counts(normalize=True).idxmax()
max_percentage = data[data['native-country'] == country_max_percentage]['salary'].value_counts(normalize=True)['>50K'] * 100

# 9. Identificar la ocupación más popular de aquellos que ganan >50k en India
top_occupation_india = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]['occupation'].value_counts().idxmax()

# Imprimir los resultados
print("1. Número de personas de cada raza:")
print(race_counts)
print("\n2. Edad promedio de los hombres:", average_age_men)
print("\n3. Porcentaje de personas con un grado de licenciatura:", bachelors_percentage)
print("\n4. Porcentaje de personas con una educación avanzada que ganan más de 50k:", advanced_education_rich_percentage)
print("\n5. Porcentaje de personas sin una educación avanzada que ganan más de 50k:", no_advanced_education_rich_percentage)
print("\n6. Mínimo número de horas que una persona trabaja por semana:", min_hours_per_week)
print("\n7. Porcentaje de personas que trabajan el mínimo de horas por semana y tienen un salario de más de 50k:", min_hours_per_week_rich_percentage)
print("\n8. País con el porcentaje más alto de personas que ganan >50k:", country_max_percentage)
print("   Porcentaje:", max_percentage)
print("\n9. Ocupación más popular de aquellos que ganan >50k en India:", top_occupation_india)
