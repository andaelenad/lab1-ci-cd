import json
import sys
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent / "tasks.json"


def load():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1


def add(description):
    tasks = load()
    task = {
        "id": next_id(tasks),
        "description": description,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save(tasks)
    print(f"[OK] Adaugat: {description}")


def list_tasks():
    tasks = load()
    if not tasks:
        print("Nu exista cursuri.")
        return
    print(f"{'ID':>3}  {'Stare':<13}  {'Descriere':<40}  {'Creat'}")
    print("-" * 70)
    for t in tasks:
        stare = "finalizat" if t["done"] else "in asteptare"
        print(f"{t['id']:>3}  {stare:<13}  {t['description']:<40}  {t['created_at']}")


def update(task_id, new_desc):
    tasks = load()
    for t in tasks:
        if t["id"] == task_id:
            old_desc = t["description"]
            t["description"] = new_desc
            save(tasks)
            print(f"[OK] Curs #{task_id} actualizat:")
            print(f"      inainte: {old_desc}")
            print(f"      dupa:    {new_desc}")
            return
    print(f"[EROARE] Cursul #{task_id} nu exista.")


def done(task_id):
    tasks = load()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save(tasks)
            print(f"[OK] Cursul #{task_id} marcat ca finalizat.")
            return
    print(f"[EROARE] Cursul #{task_id} nu exista.")


def delete(task_id):
    tasks = load()
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            save(tasks)
            print(f"[OK] Cursul #{task_id} sters: \"{t['description']}\"")
            return
    print(f"[EROARE] Cursul #{task_id} nu exista.")


def usage():
    print("Utilizare:")
    print("  python todo.py add <descriere>         # adauga curs")
    print("  python todo.py list                     # listeaza cursuri")
    print("  python todo.py update <id> <descriere>  # modifica descriere")
    print("  python todo.py done <id>                # marcheaza finalizat")
    print("  python todo.py delete <id>              # sterge curs")


def main():
    if len(sys.argv) < 2:
        usage()
        return

    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) >= 3:
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "update" and len(sys.argv) >= 4:
        update(int(sys.argv[2]), " ".join(sys.argv[3:]))
    elif cmd == "done" and len(sys.argv) == 3:
        done(int(sys.argv[2]))
    elif cmd == "delete" and len(sys.argv) == 3:
        delete(int(sys.argv[2]))
    else:
        usage()


if __name__ == "__main__":
    main()
