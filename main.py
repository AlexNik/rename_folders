import os
import sys


def clean_name(name: str, patterns: list) -> str:
    """Удаляет заданные подстроки из имени файла или папки."""
    for pattern in patterns:
        name = name.replace(pattern, "")
    return name.strip()


def rename_items(root_dir: str, patterns: list):
    """Проходит по всем файлам и папкам, переименовывает их при необходимости."""
    for current_dir, dirs, files in os.walk(root_dir, topdown=False):
        for name in files + dirs:
            new_name = clean_name(name, patterns)
            if new_name != name:
                old_path = os.path.join(current_dir, name)
                new_path = os.path.join(current_dir, new_name)
                os.rename(old_path, new_path)
                print(f'Renamed: "{old_path}" -> "{new_path}"')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <путь к папке>")
        sys.exit(1)

    target_directory = sys.argv[1]
    substrings_to_remove = ["XXX"]

    if not os.path.isdir(target_directory):
        print("Ошибка: указанная папка не существует.")
        sys.exit(1)

    rename_items(target_directory, substrings_to_remove)
    print("Готово!")