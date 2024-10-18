import json

# Fonction principale pour calculer et afficher les salaires mensuels des employés.
def monthly_salary(): 
    # Cette fonction lit les données des employés à partir d'un fichier JSON ('employes_data.json')
    with open('employes_data.json', 'r') as file_json:
        data_employees = json.load(file_json)

    # calcule les salaires en fonction des heures de contrat, des heures travaillées et du taux horaire
    def calculate_monthly_salary(employee):
        
        contract_hours = employee['contract_hours']
        weekly_hours_worked = employee['weekly_hours_worked']
        hourly_rate = employee['hourly_rate']

        if weekly_hours_worked > contract_hours:
            overtime_hours = weekly_hours_worked - contract_hours
            overtime_rate = hourly_rate * 1.5
            salary = contract_hours * hourly_rate + overtime_hours * overtime_rate
        else:
            salary = weekly_hours_worked * hourly_rate
        return salary 

    def salary_employees():
    #    Calcule les salaires de tous les employés et les regroupe par filiale
        employees_salaries = []
        for filliale, employees in data_employees.items():
            for employee in employees:
                name = employee['name']
                job = employee['job']
                salary = calculate_monthly_salary(employee)
                employees_salaries.append({
                    'name': name,
                    'job': job,
                    'salary': salary,
                    'filliale': filliale  # Ajouter la filiale pour chaque employé
                })
        # retourne la liste des employés avec leur nom, poste, salaire et filiale.
        return employees_salaries
    
    employees_salaries = salary_employees()

    # Grouper les employés par filiale
    filliales = group_employees_by_filliale(employees_salaries)

    # Afficher les employés par filiale sous forme de tableau
    for filliale, employees in filliales.items():
        print(f"\nTableau des employés pour la filiale: {filliale}")
        print(f"{'Nom':<20} | {'Poste':<20} | {'Salaire':<20}")
        print("-" * 60)
        for employee in employees:
            print(f"{employee['name']:<20} | {employee['job']:<20} | {employee['salary']:<20.2f}")

    # Calculer et afficher les statistiques des salaires
    mean_salary, max_salary, min_salary = calculate_statistics(employees_salaries)

    print("\nStatistiques des salaires globales :")
    print(f"Salaire moyen: {mean_salary:.2f}")
    print(f"Salaire maximum: {max_salary:.2f}")
    print(f"Salaire minimum: {min_salary:.2f}")

# Calcule les statistiques des salaires pour l'ensemble des employés
def calculate_statistics(employees):
    salaries = [employee['salary'] for employee in employees]
    mean_salary = sum(salaries) / len(salaries)
    maximum_salary = max(salaries)
    minimum_salary = min(salaries)
    return mean_salary, maximum_salary, minimum_salary

# Calcule les statistiques des salaires par filliales
def group_employees_by_filliale(employees_salaries):
    filliales = {}
    for employee in employees_salaries:
        filliale = employee['filliale']
        if filliale in filliales:
            filliales[filliale].append(employee)
        else:
            filliales[filliale] = [employee]
    return filliales

# Appeler la fonction principale
monthly_salary()