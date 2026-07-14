#!/usr/bin/env python3
"""TaskLite: a tiny command-line to-do list manager.

Tasks are stored as a JSON list in tasks.json, in the current directory.
"""

import json
import sys
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks():
    """Return the list of tasks, or an empty list if none exist yet."""
    if not TASKS_FILE.exists():
        return []
    with open(TASKS_FILE) as f:
        return json.load(f)


def save_tasks(tasks):
    """Write the given list of tasks back to tasks.json."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(description, priority="normal"):
    """Add a new, not-yet-done task with the given description."""
    tasks = load_tasks()
    tasks.append({"description": description, "priority": priority, "done": False})
    save_tasks(tasks)
    print(f"Added: {description}")


def list_tasks():
    """Print all tasks with a status checkbox and a display number."""
    tasks = load_tasks()
    if not tasks:
        print('No tasks yet. Add one with: tasklite add "buy milk"')
        return
    for i, task in enumerate(tasks):
        status = "x" if task["done"] else " "
        # NOTE: this shows a 1-based number (i + 1) for readability,
        # but done()/remove() below expect a 0-based index. See issue
        # "Task numbers in list don't match the numbers done/remove expect".
        print(f"[{status}] {i + 1}. {task['description']}")


def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked task {index} as done.")
    except IndexError:
        print("No such task.")


def remove_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Removed: {removed['description']}")
    except IndexError:
        print("No such task.")


def sort_by_priority(tasks):
    """Sort tasks so 'high' priority tasks come first, then 'normal', then 'low'.

    TODO(enhancement): not implemented yet. Currently returns tasks
    unsorted. Should also be wired up behind a `list --sort` flag.
    """
    return tasks


def main():
    if len(sys.argv) < 2:
        print("Usage: tasklite <add|list|done|remove> [args]")
        return

    command = sys.argv[1]
    if command == "add":
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "list":
        list_tasks()
    elif command == "done":
        mark_done(int(sys.argv[2]))
    elif command == "remove":
        remove_task(int(sys.argv[2]))
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
