import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
import json
import os

root = tk.Tk()
root.title("Toxic Player Tracker")
root.geometry("500x300")


# Load the toxic players dictionary from file if it exists

print("Current directory:", os.path.dirname(os.path.abspath(__file__)))

toxic_players = {}

directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, "toxic_players.json")

try:
    with open("toxic_players.json", "r") as f:
        toxic_players = json.load(f)
except FileNotFoundError:
    toxic_players = {}

def add_toxic_player():
    toxic_name = username_entry.get().strip()
    toxic_note = note_entry.get().strip()
    if toxic_name in toxic_players:
        messagebox.showerror("Error", "Username already exists")
        return
    toxic_players[toxic_name] = toxic_note
    toxic_list.insert("", "end", values=(toxic_name, toxic_note))
    # Save the toxic players dictionary to file
    with open("toxic_players.json", "w") as f:
        json.dump(toxic_players, f)

def search_toxic_players():
    search_entry = search_field.get().strip()
    search_terms = [term.strip() for term in search_entry.split(',')]
    toxic_list.delete(*toxic_list.get_children())
    found = False
    for term in search_terms:
        term = term.strip()
        if term in toxic_players:
            toxic_list.insert("", "end", values=(term, toxic_players[term]))
            found = True
        else:
            messagebox.showwarning("Warning", "Username '{}' not found".format(term))
    if not found:
        messagebox.showwarning("Warning", "No usernames found")

username_label = ttk.Label(root, text="Username:")
username_label.pack()

username_entry = ttk.Entry(root)
username_entry.pack()

note_label = ttk.Label(root, text="Note:")
note_label.pack()

note_entry = ttk.Entry(root)
note_entry.pack()

add_button = ttk.Button(root, text="Add", command=add_toxic_player)
add_button.pack()

search_label = ttk.Label(root, text="Search:")
search_label.pack()

search_field = ttk.Entry(root)
search_field.pack()

search_button = ttk.Button(root, text="Search", command=search_toxic_players)
search_button.pack()

toxic_list = ttk.Treeview(root, columns=("username", "note"), show="headings")
toxic_list.pack()
toxic_list.heading("username", text="Username")
toxic_list.heading("note", text="Note")

if __name__ == "__main__":
    for toxic_name, toxic_note in toxic_players.items():
        toxic_list.insert("", "end", values=(toxic_name, toxic_note))

root.mainloop()
