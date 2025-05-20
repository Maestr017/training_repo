import json
import os

TASKS_FILE = "tasks.json"


# Загрузка задач из файла JSON
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


# Сохраняет задачи в файл JSON
def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)


# Отображение меню приложения
def display_menu():
    print("\nМеню:")
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    print("5. Выход")


# Отображает список задач
def show_tasks(tasks):
    if not tasks:
        print("\nНет задач!")
    else:
        print("\nСписок задач:")
        for idx, task in enumerate(tasks, 1):
            status = "✓" if task.get("completed", False) else " "
            print(f"{idx}. [{status}] {task['title']}")


# Добавляет новую задачу
def add_task(tasks):
    title = input("\nВведите название задачи: ").strip()
    if not title:
        print("Название задачи не может быть пустым!")
        return

    new_task = {
        "title": title,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"\nЗадача '{title}' добавлена!")


# Отмечает задачу как выполненную
def mark_completed(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("\nВведите номер задачи для отметки: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            save_tasks(tasks)
            print(f"Задача '{tasks[task_num - 1]['title']}' отмечена как выполненная!")
        else:
            print("Неверный номер задачи!")
    except ValueError:
        print("Пожалуйста, введите число!")


# Удаляет задачу
def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("\nВведите номер задачи для удаления: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Задача '{deleted_task['title']}' удалена!")
        else:
            print("Неверный номер задачи!")
    except ValueError:
        print("Пожалуйста, введите число!")


# Основная функция приложения
def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("\nВыберите действие (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nДо свидания!")
            break
        else:
            print("\nНеверный ввод. Пожалуйста, выберите от 1 до 5.")


if __name__ == "__main__":
    main()