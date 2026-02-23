import tkinter as tk
from tkinter import ttk
import json
import os

SAVE_FILE = "checklist_data.json"

# ---------- LIST DATA ----------
DEFAULT_LISTS = {
    "Duomension City East Opponents": [
    {"number": 1, "npc": "Layla", "card": "Ruan Mei's Creation", "level": 2, "checked": False},
    {"number": 2, "npc": "Dovebrook Kid", "card": "Furbo Journalist", "level": 4, "checked": False},
    {"number": 3, "npc": "Meowton", "card": "Senior Staff: Team Leader", "level": 5, "checked": False},
    {"number": 4, "npc": "Issik", "card": "Dreamjolt Troupe's Mr. Domescreen", "level": 5, "checked": False},
    {"number": 5, "npc": "Taro", "card": "Senior Staff: Team Leader", "level": 6, "checked": False},
    {"number": 6, "npc": "Terrance", "card": "Castorice", "level": 9, "checked": False},
    {"number": 7, "npc": "MD-78-8", "card": "Firefly", "level": 9, "checked": False},
    {"number": 8, "npc": "Gogo", "card": "Trailblazemon", "level": 3, "checked": False},
    {"number": 9, "npc": "Typha", "card": "Dreamjolt Troupe's Mr. Domescreen", "level": 6, "checked": False},
    {"number": 10, "npc": "Down-Bad Jones", "card": "Automaton Beetle", "level": 6, "checked": False},
    {"number": 11, "npc": "@Eating_Solo", "card": "Senior Staff: Team Leader", "level": 5, "checked": False},
    {"number": 12, "npc": "Aceme", "card": "Grunt: Security Personnel", "level": 6, "checked": False},
    {"number": 13, "npc": "Cosmic Scalping King", "card": "Aventurine", "level": 9, "checked": False},
    {"number": 14, "npc": "Mech Matchmaker", "card": "Grunt: Trashcan", "level": 4, "checked": False},
],
    "Duomension City West Opponents": [
    {"number": 1, "npc": "Dades", "card": "Robin", "level": 9, "checked": False},
    {"number": 2, "npc": "Quackaloo", "card": "Trailblazemon", "level": 3, "checked": False},
    {"number": 3, "npc": "Longtail", "card": "Skott", "level": 7, "checked": False},
    {"number": 4, "npc": "Nikka", "card": "Automaton Beetle", "level": 3, "checked": False},
    {"number": 5, "npc": "Willyn", "card": "Grunt: Security Personnel", "level": 5, "checked": False},
    {"number": 6, "npc": "Narna", "card": "Grunt: Security Personnel", "level": 6, "checked": False},
    {"number": 7, "npc": "@HungryMeowComment", "card": "Trashcan", "level": 5, "checked": False},
    {"number": 8, "npc": "Detective Croc", "card": "Sparxicle", "level": 1, "checked": False},
    {"number": 9, "npc": "Love❤︎Sparxicle", "card": "Sparxie", "level": 8, "checked": False},
    {"number": 10, "npc": "Jinix", "card": "Yao Guang", "level": 9, "checked": False},
    {"number": 11, "npc": "Kraken", "card": "Chimera", "level": 2, "checked": False},
    {"number": 12, "npc": "Charing", "card": "Trailblazemon", "level": 2, "checked": False},
],
    "Dovebrook District Opponents": [
    {"number": 1, "npc": "@Lone_Freerider", "card": "Dreamjolt Troupe's Mr. Domescreen", "level": 4, "checked": False},
    {"number": 2, "npc": "Master Moon", "card": "Sparxie", "level": 9, "checked": False},
    {"number": 3, "npc": "Toxicape", "card": "Dromas", "level": 2, "checked": False},
    {"number": 4, "npc": "Umbralle", "card": "Grunt: Security Personnel", "level": 5, "checked": False},
    {"number": 5, "npc": "Saliman", "card": "Grunt: Security Personnel", "level": 5, "checked": False},
    {"number": 6, "npc": "Hymes", "card": "Senior Staff: Team Leader", "level": 5, "checked": False},
    {"number": 7, "npc": "Gus", "card": "Grunt: Security Personnel", "level": 4, "checked": False},
    {"number": 8, "npc": "Furblix", "card": "Furbo Journalist", "level": 4, "checked": False},
],
    "Graphia Academy Opponents": [
    {"number": 1, "npc": "AAA Delivery, Contact Me", "card": "Trashcan", "level": 6, "checked": False},
    {"number": 2, "npc": "Anoine", "card": "Dromas", "level": 3, "checked": False},
    {"number": 3, "npc": "Mr. Tyker", "card": "Dreamjolt Troupe's Mr. Domescreen", "level": 6, "checked": False},
    {"number": 4, "npc": "Radiant ☆ Boy", "card": "Acheron", "level": 9, "checked": False},
    {"number": 5, "npc": "Angela", "card": "Dreamjolt Troupe's Mr. Domescreen", "level": 5, "checked": False},
    {"number": 6, "npc": "Dollie", "card": "Senior Staff: Team Leader", "level": 5, "checked": False},
    {"number": 7, "npc": "Scarlett", "card": "Ruan Mei's Creation", "level": 2, "checked": False},
    {"number": 8, "npc": "☆ Magical ☆ Middleager ☆", "card": "Trailblazemon", "level": 3, "checked": False},
    {"number": 9, "npc": "Dana", "card": "Acheron", "level": 9, "checked": False},
    {"number": 10, "npc": "Donny", "card": "Aventurine", "level": 9, "checked": False},
    {"number": 11, "npc": "Exam God", "card": "Furbo Journalist", "level": 4, "checked": False},
    {"number": 12, "npc": "Fortune Cat", "card": "Furbo Journalist", "level": 5, "checked": False},
    {"number": 13, "npc": "Reddy", "card": "Dreamjolt Troupe's Mr. Domescreen", "level": 5, "checked": False},
    {"number": 14, "npc": "Mr. Joerjo", "card": "Sparkxie", "level": 9, "checked": False},
    {"number": 15, "npc": "Whitepaper", "card": "Chimera", "level": 2, "checked": False},
    {"number": 16, "npc": "Seadrake", "card": "Trashcan", "level": 4, "checked": False},
],
    "World's End Tavern Opponents": [
    {"number": 1, "npc": "Zhongshan", "card": "Furbo Journalist", "level": 6, "checked": False},
    {"number": 2, "npc": "@Chad", "card": "Furbo Journalist", "level": 6, "checked": False},
    {"number": 3, "npc": "Heartain", "card": "Trashcan", "level": 6, "checked": False},
    {"number": 4, "npc": "Singafar", "card": "Trashcan", "level": 5, "checked": False},
    {"number": 5, "npc": "Aco", "card": "Ruan Mei's Creation", "level": 2, "checked": False},
    {"number": 6, "npc": "Hop-Know-Not", "card": "Trailblazemon", "level": 3, "checked": False},
],
}
# ------------------------------------


def load_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return DEFAULT_LISTS


def save_data():
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def toggle_visibility(tab_name):
    show_completed[tab_name] = not show_completed[tab_name]
    refresh_tab(tab_name)


def refresh_tab(tab_name):
    frame = content_frames[tab_name]

    for widget in frame.winfo_children():
        widget.destroy()

    # Header
    header = tk.Frame(frame)
    header.pack(fill="x")

    tk.Label(header, text="No.", width=5, anchor="w").grid(row=0, column=0)
    tk.Label(header, text="NPC", width=25, anchor="w").grid(row=0, column=1)
    tk.Label(header, text="Card", width=30, anchor="w").grid(row=0, column=2)
    tk.Label(header, text="Level", width=8, anchor="w").grid(row=0, column=3)
    tk.Label(header, text="Done", width=8, anchor="w").grid(row=0, column=4)

    for i, item in enumerate(data[tab_name]):
        if not show_completed[tab_name] and item["checked"]:
            continue

        row = tk.Frame(frame)
        row.pack(fill="x", pady=2)

        tk.Label(row, text=item["number"], width=5, anchor="w").grid(row=0, column=0)
        tk.Label(row, text=item["npc"], width=25, anchor="w").grid(row=0, column=1)
        tk.Label(row, text=item["card"], width=30, anchor="w").grid(row=0, column=2)
        tk.Label(row, text=item["level"], width=8, anchor="w").grid(row=0, column=3)

        var = tk.BooleanVar(value=item["checked"])

        def make_callback(index=i, variable=var):
            def callback():
                data[tab_name][index]["checked"] = variable.get()
                save_data()
            return callback

        chk = tk.Checkbutton(row, variable=var, command=make_callback())
        chk.grid(row=0, column=4)


# ---------- MAIN APP ----------
root = tk.Tk()
root.title("NPC Card Checklist")
root.geometry("900x550")

data = load_data()
show_completed = {name: True for name in data}

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

content_frames = {}

for list_name in data:
    tab_frame = tk.Frame(notebook)
    notebook.add(tab_frame, text=list_name)

    # Toggle button
    btn = tk.Button(
        tab_frame,
        text="Show/Hide Completed",
        command=lambda name=list_name: toggle_visibility(name),
    )
    btn.pack(pady=5)

    # Scrollable area setup
    canvas = tk.Canvas(tab_frame)
    scrollbar = ttk.Scrollbar(tab_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e, canvas=canvas: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    content_frames[list_name] = scrollable_frame

    refresh_tab(list_name)


root.mainloop()
