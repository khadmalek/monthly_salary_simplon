import json

def monthly_salary(): 
    """
    Fonction principale pour calculer et afficher les salaires mensuels des employés.

    Cette fonction lit les données des employés à partir d'un fichier JSON ('employes_data.json'),
    calcule leurs salaires mensuels en fonction de leurs heures de contrat, heures travaillées et taux horaire,
    puis affiche ces informations regroupées par filiale avec des statistiques sur les salaires.
    """

    # Lecture des données des employés à partir du fichier JSON
    with open('employes_data.json', 'r') as file_json:
        data_employees = json.load(file_json)

    def calculate_monthly_salary(employee):
        """
        Calcule le salaire mensuel d'un employé en fonction de ses heures travaillées, 
        de ses heures de contrat et de son taux horaire.

        Si l'employé travaille plus que ses heures de contrat, les heures supplémentaires sont
        rémunérées à un taux majoré de 1,5 fois le taux horaire normal.

        Args:
            employee (dict): Dictionnaire contenant les informations d'un employé.
        
        Returns:
            float: Le salaire mensuel calculé pour l'employé.
        """
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
        """
        Calcule les salaires de tous les employés et les regroupe par filiale.

        Cette fonction parcourt les données des employés et utilise la fonction 
        'calculate_monthly_salary' pour calculer le salaire de chaque employé.

        Returns:
            list: Une liste de dictionnaires contenant les informations de chaque employé 
            (nom, poste, salaire, et filiale).
        """
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
                    'filliale': filliale
                })
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


def calculate_statistics(employees):
    """
    Calcule les statistiques des salaires pour l'ensemble des employés.

    Args:
        employees (list): Liste de dictionnaires contenant les informations des employés et leur salaire.
    
    Returns:
        tuple: Contient le salaire moyen, le salaire maximum et le salaire minimum.
    """
    salaries = [employee['salary'] for employee in employees]
    mean_salary = sum(salaries) / len(salaries)
    maximum_salary = max(salaries)
    minimum_salary = min(salaries)
    return mean_salary, maximum_salary, minimum_salary


def group_employees_by_filliale(employees_salaries):
    """
    Regroupe les employés par filiale.

    Args:
        employees_salaries (list): Liste de dictionnaires contenant les informations de chaque employé
        (nom, poste, salaire, filiale).
    
    Returns:
        dict: Un dictionnaire où les clés sont les noms des filiales et les valeurs sont les listes 
        des employés associés à chaque filiale.
    """
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