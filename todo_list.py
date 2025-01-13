# Liste des tâches
tasks = []

# Fonction pour afficher les tâches
def list_tasks():
    print("\n--- Liste des tâches ---")
    if not tasks:
        print("Aucune tâche à afficher.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["completed"] else "✖"
            print(f"{i}. {task['task']} [{status}]")
    print()

# Fonction pour ajouter une tâche
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Tâche ajoutée : {task}")

# Fonction pour marquer une tâche comme terminée
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"Tâche terminée : {tasks[index]['task']}")
    else:
        print("Indice invalide.")

# Fonction pour supprimer une tâche
def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Tâche supprimée : {removed_task['task']}")
    else:
        print("Indice invalide.")

# Menu principal
while True:
    print("\n--- Menu ---")
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Supprimer une tâche")
    print("5. Quitter")
    choice = input("Choisissez une option : ")

    if choice == "1":
        list_tasks()
    elif choice == "2":
        task = input("Entrez une nouvelle tâche : ")
        add_task(task)
    elif choice == "3":
        list_tasks()
        index = int(input("Entrez le numéro de la tâche à terminer : ")) - 1
        complete_task(index)
    elif choice == "4":
        list_tasks()
        index = int(input("Entrez le numéro de la tâche à supprimer : ")) - 1
        delete_task(index)
    elif choice == "5":
        print("À bientôt !")
        break
    else:
        print("Option invalide. Réessayez.")
