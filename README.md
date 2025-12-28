# DeepSeekbot
## 📋 Требования

- ОС:
  - Linux (Ubuntu 20.04+)
  - macOS (Intel / Apple Silicon)
  - Windows 10/11 (через WSL2)
- Минимум **8 GB RAM**
- (Опционально) GPU для ускорения инференса

---

## 🔧 Установка Ollama

### Linux / macOS
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Проверка установки:
```bash
ollama --version
```

---

### Windows (через WSL2)

1. Установите **WSL2**  
   https://learn.microsoft.com/windows/wsl/install

2. Запустите Ubuntu в WSL и выполните:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## Загрузка модели DeepSeek

### Рекомендуемая модель
```bash
ollama pull deepseek-r1
```

### Облегчённая версия (для слабых машин)
```bash
ollama pull deepseek-r1:7b
```

### Проверка работы модели
```bash
ollama run deepseek-r1
```

## Лицензия

Использование модели DeepSeek регулируется лицензией разработчика модели

