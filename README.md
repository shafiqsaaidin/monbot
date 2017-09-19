# monbot
A telegram bot use to monitor and screenshot windows desktop

## Requirement
Before this bot can be use, please make sure you have this following requirement:
- Python 3 download [here](https://www.python.org/downloads/)
- Pyautogui
- Telepot

## Installation
#### Linux
- pip3 install pyautogui
- pip3 install telepot

#### Windows 
- pip install pyautogui
- pip install telepot

## Usage
#### Setup bot Token
You have to setup a bot and get the bot api from bot Father
- Read [this](https://core.telegram.org/bots#6-botfather) before you can start
#### Setup an Admin id
You have to set a variable adminId in tokens.py to be equal your chat_id or multiple chat_id (if more people will use your bot). For example:
- `adminId = [443355]`
- `adminId = [443355, -55667788, 99884433]`

#### Run the code
`python mon.py`

#### Capture desktop image
use this command in your bot to screenshot desktop image `/capture` Example

![Imgur](https://i.imgur.com/RAUHEJb.png)
