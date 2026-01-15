import os
import re
from pathlib import Path

def clean_filename(filename):
    """Очищает имя файла, заменяя # на подчёркивание"""
    # Просто заменяем # на _
    cleaned = filename.replace('#', '_')
    # Удаляем другие странные символы кроме букв, цифр, точек, дефисов и подчёркиваний
    cleaned = re.sub(r'[^a-zA-Z0-9._-]', '', cleaned)
    return cleaned

def rename_files_recursive(directory_path):
    """Переименовывает все файлы, удаляя странные символы"""
    path = Path(directory_path)
    
    if not path.exists():
        print(f"❌ Папка не найдена: {directory_path}")
        return
    
    renamed_count = 0
    
    for file in path.rglob("*"):
        if file.is_file():
            old_name = file.name
            new_name = clean_filename(old_name)
            
            print(f"Проверяю: {old_name}")
            print(f"  → Будет: {new_name}")
            
            if old_name != new_name:
                new_path = file.parent / new_name
                try:
                    file.rename(new_path)
                    print(f"✅ Переименовано!")
                    renamed_count += 1
                except Exception as e:
                    print(f"❌ Ошибка: {e}")
            print()
    
    print(f"✓ Всего переименовано: {renamed_count}")

folder_path = r"D:\validation.zip\validation\gt"
rename_files_recursive(folder_path)
