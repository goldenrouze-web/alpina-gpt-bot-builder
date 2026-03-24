# Alpina GPT Bot Builder

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-0.104.0-green)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/openai-GPT-orange)](https://platform.openai.com/)

**Alpina GPT Bot Builder** — это готовый шаблон проекта для создания собственного GPT-бота с использованием OpenAI API, FastAPI и Docker. Проект включает поддержку CI/CD через GitHub Actions, удобную структуру кода и возможность быстрого деплоя.

---

## 🗂 Структура проекта

```text
alpina-gpt-bot-builder/
├── alpinabot/               # Исходный код бота
│   ├── __init__.py
│   └── main.py              # Основной файл с FastAPI и OpenAI
│
├── .github/workflows/       # GitHub Actions
│   ├── ci.yml               # Проверка кода (flake8, pytest)
│   └── docker.yml           # Сборка Docker
│
├── Dockerfile               # Docker образ для бота
├── docker-compose.yml       # Запуск контейнера локально
├── requirements.txt         # Python зависимости
├── .env.example             # Пример файла с переменными окружения
├── .dockerignore            # Файлы, исключаемые из Docker
└── README.md
