import json
import sys
from datetime import datetime
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    if not TASKS_FILE.exists():
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add(description):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1 if not tasks else max(t["id"] for t in tasks) + 1,
        "description": description,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: {description}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for t in tasks:
        status = "x" if t["done"] else " "
        print(f"[{status}] {t['id']:>3}. {t['description']}")


def delete(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task {task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"Deleted task {task_id}.")


def done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return
    print(f"Task {task_id} not found.")


def usage():
    print("Usage:")
    print("  python todo.py add <description>")
    print("  python todo.py list")
    print("  python todo.py delete <id>")
    print("  python todo.py done <id>")


def main():
    if len(sys.argv) < 2:
        usage()
        return

    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) >= 3:
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "delete" and len(sys.argv) == 3:
        delete(int(sys.argv[2]))
    elif cmd == "done" and len(sys.argv) == 3:
        done(int(sys.argv[2]))
    else:
        usage()


if __name__ == "__main__":
    main()
