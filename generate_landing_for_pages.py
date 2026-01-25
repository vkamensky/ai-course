#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для генерации лендинга курса в папку docs/ для GitHub Pages.
Используйте этот скрипт для публикации лендинга в отдельном репозитории.
"""

import shutil
from pathlib import Path

def main():
    """Генерирует лендинг в папку docs/ для GitHub Pages"""
    
    # Определяем пути
    script_dir = Path(__file__).parent
    source_website = script_dir / "website_output"
    docs_dir = script_dir / "docs"
    
    print("🎯 ГЕНЕРАЦИЯ ЛЕНДИНГА ДЛЯ GITHUB PAGES")
    print("="*60)
    print(f"📁 Источник: {source_website}")
    print(f"📁 Финальная папка: {docs_dir}")
    
    if not source_website.exists():
        print(f"\n❌ ОШИБКА: Папка {source_website} не найдена!")
        print("   Убедитесь, что файлы лендинга находятся в website_output/")
        return
    
    # Создаем docs/ если не существует
    docs_dir.mkdir(exist_ok=True)
    
    # Находим все файлы лендинга
    landing_files = list(source_website.glob("ai-productivity-v*.html"))
    
    if not landing_files:
        print(f"\n⚠️  Файлы лендинга не найдены в {source_website}")
        print("   Ожидаются файлы вида: ai-productivity-v*.html")
        return
    
    # Находим последнюю версию (по дате изменения)
    latest = max(landing_files, key=lambda p: p.stat().st_mtime)
    
    print(f"\n📋 Найдено файлов: {len(landing_files)}")
    print(f"📄 Последняя версия: {latest.name}")
    
    # Копируем последнюю версию как index.html
    shutil.copy2(latest, docs_dir / "index.html")
    print(f"\n✅ {latest.name} → index.html (главная страница)")
    
    # Копируем папку assets/ если она существует
    assets_source = source_website / "assets"
    if assets_source.exists() and assets_source.is_dir():
        assets_dest = docs_dir / "assets"
        if assets_dest.exists():
            shutil.rmtree(assets_dest)
        shutil.copytree(assets_source, assets_dest)
        print(f"✅ assets/ → docs/assets/ (изображения)")
    
    # Опционально: копируем все версии для истории
    # Раскомментируйте, если нужны все версии:
    # for file in landing_files:
    #     if file != latest:
    #         shutil.copy2(file, docs_dir / file.name)
    #         print(f"  ✅ {file.name}")
    
    print(f"\n✅ Лендинг готов в {docs_dir}")
    print(f"\n📝 Следующие шаги:")
    print(f"   1. Проверьте сайт локально: откройте {docs_dir}/index.html в браузере")
    print(f"   2. Закоммитьте изменения:")
    print(f"      git add docs/")
    print(f"      git commit -m 'Обновлен лендинг'")
    print(f"      git push")
    print(f"\n🌐 Сайт будет доступен на GitHub Pages через 1-2 минуты после push")
    print(f"   URL: https://vkamensky.github.io/ai-course/")

if __name__ == "__main__":
    main()

