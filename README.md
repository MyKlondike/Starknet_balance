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
FeedBacK : Ваш отзыв очень важен 👉 [Telegram](https://t.me/MyKlondike) <br>
Вы можете поделиться своим мнением и предложениями в 🐸
[Chat](https://t.me/Klondike_Talks) <br>

🍩 (EVM): 0xe93081718a75818Be2eB1E1336c8c2AC930e44e0:

___
##ENG

This script is designed to check the balance of STARKNET wallets.

## Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Settings](#settings)
4. [Functions](#functions)
5. [Feedback](#feedback)

## Requirements
- Python 3.10+

## Installation

### The script uses the starknet_py library to interact with the STARKNET blockchain.

Using `starknet.py` requires the dependencies `ecdsa`, `fastecdsa` and `sympy`. Depending on your operating system, there are different installation steps required.

###Linux

```bash
sudo apt install -y libgmp3-dev
pip install starknet-py
```

###MacOS

The instructions assume you have Homebrew installed.

**Hint:** If you are having problems installing `starknet.py` due to `fastecdsa` on recent versions of MacOS, consider installing `cmake` version >=3.22.4.

```bash
brew install cmake
```

This is necessary to build the `crypto-cpp-py` dependency if it has not been updated to support the latest versions of MacOS.

#### For Intel processors

```bash
brew install gmp
pip install starknet-py
```

#### For Apple Silicon processors

```bash
brew install gmp
CFLAGS=-I`brew --prefix gmp`/include LDFLAGS=-L`brew --prefix gmp`/lib pip install starknet-py
```

###Windows

You can install `starknet.py` on Windows in two ways:

1. Install MinGW.
The easiest way to install MinGW is through chocolatey.
Add MinGW to your PATH environment variable (for example, C:\ProgramData\chocolatey\lib\mingw\tools\install\mingw64\bin).
2. Use a Linux virtual machine

### Install dependencies using the command:
    ```bash
    pip install -r requirements.txt
    ```

## Settings
In the `private_keys.txt` file, specify the private keys of the wallets you want to check.

All parameters and settings can be changed in the `settings.py` file.

### Wallet type
TYPE WALLET MODE
Specify the type of wallet used to check your balance.

### CAIRO version
CAIRO VERSION CONTROL
CAIRO version management. Specify 0 or 1 depending on the version.

### List of tokens
TOKENS LIST
List of tokens and their corresponding contract addresses on the Starknet network. Change or add tokens as you wish.

## Functions
- The script checks the balance of STARKNET wallets and writes the results to a CSV file (`res.csv`).
- The results contain the wallet address and balance for each token from the STARKNET_TOKENS list.

## Feedback
FeedBacK: Your feedback is very important 👉 [Telegram](https://t.me/MyKlondike) <br>
You can share your opinions and suggestions on 🐸
[Chat](https://t.me/Klondike_Talks) <br>

🍩 (EVM): 0xe93081718a75818Be2eB1E1336c8c2AC930e44e0:
```
