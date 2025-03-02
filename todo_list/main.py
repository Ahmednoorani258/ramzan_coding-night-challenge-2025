import click
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """A simple todo list Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task '{task}' added to the list")

@click.command()
def list():
    """List all tasks in the list"""
    tasks = load_tasks()
    if not tasks:
        click.echo("NO tasks in the list")
        return
    for i, task in enumerate(tasks,1):
        status = "✔" if task["done"] else "✘"
        click.echo(f"{i}. {task['task']} [{status}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Complete a task"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} completed")
    else:
        click.echo("Invalid task number")


@cli.command()
@click.argument("task_number", type=int)
def delete(task_number):
    """Delete a task"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Task {task_number} deleted")
    else:
        click.echo("Invalid task number")   
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
    