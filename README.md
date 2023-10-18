# Starknet_balance

Этот скрипт предназначен для проверки баланса кошельков STARKNET. 

## Оглавление
1. [Требования](#требования)
2. [Установка](#установка)
3. [Настройка](#настройка)
4. [Функции](#функции)
5. [Обратная связь](#обратная-связь)

## Требования
- Python 3.10+

## Установка

### Скрипт использует библиотеку starknet_py для взаимодействия с блокчейном STARKNET.

Для использования `starknet.py` требуются зависимости `ecdsa`, `fastecdsa` и `sympy`. В зависимости от операционной системы необходимо выполнить разные шаги установки.

### Linux

```bash
sudo apt install -y libgmp3-dev
pip install starknet-py
```

### MacOS

Инструкции предполагают, что у вас установлен Homebrew.

**Подсказка:** Если у вас возникают проблемы с установкой `starknet.py` в связи с `fastecdsa` на последних версиях MacOS, рассмотрите установку `cmake` версии >=3.22.4.

```bash
brew install cmake
```

Это необходимо для построения зависимости `crypto-cpp-py`, если она не была обновлена для поддержки новейших версий MacOS.

#### Для процессоров Intel

```bash
brew install gmp
pip install starknet-py
```

#### Для процессоров Apple Silicon

```bash
brew install gmp
CFLAGS=-I`brew --prefix gmp`/include LDFLAGS=-L`brew --prefix gmp`/lib pip install starknet-py
```

### Windows

Можно установить `starknet.py` на Windows двумя способами:

1. Установите MinGW.
Легче всего установить MinGW через chocolatey.
Добавте MinGW в переменную среды PATH (например, C:\ProgramData\chocolatey\lib\mingw\tools\install\mingw64\bin).
2. Используйте виртуальную машину Linux

### Выполните установку зависимостей с помощью команды:
   ```bash
   pip install -r requirements.txt
   ```

## Настройка
В файле `private_keys.txt` укажите приватные ключи кошельков, которые вы хотите проверить.

Все параметры и настройки можно изменять в файле `settings.py`.

### Тип кошелька
TYPE WALLET MODE
Укажите тип кошелька, используемого для проверки баланса.

### Версия CAIRO
CAIRO VERSION CONTROL
Управление версией CAIRO. Укажите 0 или 1 в зависимости от версии.

### Список токенов
TOKENS LIST
Перечень токенов и их соответствующих адресов контрактов на сети Starknet. Измените или добавьте токены по вашему усмотрению.

## Функции
- Скрипт проверяет баланс кошельков STARKNET и записывает результаты в файл CSV (`res.csv`).
- Результаты содержат адрес кошелька и баланс для каждого токена из списка STARKNET_TOKENS.

## Обратная связь
Ваш отзыв очень важен. Вы можете поделиться своим мнением и предложениями в
[Chat](https://t.me/Klondike_Talks) <br>

[Telegram](https://t.me/MyKlondike) <br>

🍩 (EVM): 0xe93081718a75818Be2eB1E1336c8c2AC930e44e0:
```python
"             FeedBacK : https://t.me/MyKlondike  \n", )
"             Чат 🐸:  https://t.me/Klondike_Talks  \n", )
"         🍩: 0xe93081718a75818Be2eB1E1336c8c2AC930e44e0  ", )
```
