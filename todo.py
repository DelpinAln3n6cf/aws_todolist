import tkinter as tk
from tkinter import messagebox
import requests

# Fonctions pour interagir avec le backend
API_ENDPOINT = "https://goeaoalsjj.execute-api.eu-west-1.amazonaws.com/delphine_dev"

def get_tasks():
    response = requests.get(f"{API_ENDPOINT}/delphine_tasks")
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Erreur", "Impossible de récupérer les tâches")
        return []

def add_task(task):
    response = requests.post(f"{API_ENDPOINT}/delphine_tasks", json={"task": task})
    if response.status_code == 201:
        return True
    else:
        messagebox.showerror("Erreur", "Impossible d'ajouter la tâche")
        return False

def delete_task(task_id):
    response = requests.delete(f"{API_ENDPOINT}/delphine_tasks/{task_id}")
    if response.status_code == 204:
        return True
    else:
        messagebox.showerror("Erreur", "Impossible de supprimer la tâche")
        return False

# Interface graphique
    
def refresh_task_list():
    response = requests.get('https://goeaoalsjj.execute-api.eu-west-1.amazonaws.com/delphine_dev/delphine_tasks')
    if response.status_code == 200:
        tasks = response.json()  # Désérialisation de la réponse JSON
        for task in tasks:
            # Supposons que 'tasks' est une liste de dictionnaires
            task_text = f"{task['taskId']}: {task['task']}"
            print(task_text)
    else:
        print(f"Erreur: {response.status_code}")


# def refresh_task_list():
#     for widget in frame_tasks.winfo_children():
#         widget.destroy()
#     for task in get_tasks():
#         task_text = f"{task['id']}: {task['task']}"
#         lbl = tk.Label(frame_tasks, text=task_text, wraplength=200)
#         lbl.pack()

def add_task_button_click():
    task = entry_task.get()
    if task:
        added = add_task(task)
        if added:
            entry_task.delete(0, tk.END)
            refresh_task_list()

def delete_task_button_click():
    task_id = entry_delete_task.get()
    if task_id:
        deleted = delete_task(task_id)
        if deleted:
            entry_delete_task.delete(0, tk.END)
            refresh_task_list()

app = tk.Tk()
app.title("ToDo List")

# Ajout de tâche
frame_add_task = tk.Frame(app)
frame_add_task.pack()
entry_task = tk.Entry(frame_add_task, width=25)
entry_task.pack(side=tk.LEFT)
btn_add_task = tk.Button(frame_add_task, text="Ajouter tâche", command=add_task_button_click)
btn_add_task.pack(side=tk.LEFT)

# Suppression de tâche
frame_delete_task = tk.Frame(app)
frame_delete_task.pack()
entry_delete_task = tk.Entry(frame_delete_task, width=25)
entry_delete_task.pack(side=tk.LEFT)
btn_delete_task = tk.Button(frame_delete_task, text="Supprimer tâche", command=delete_task_button_click)
btn_delete_task.pack(side=tk.LEFT)

# Liste des tâches
frame_tasks = tk.Frame(app)
frame_tasks.pack()

refresh_task_list()

app.mainloop()
