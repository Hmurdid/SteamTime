# SteamTime

## About project: 
This is a small project to get started with public coding.
The program shows how much time a specific user spent in certain games by making requests to official Steam servers through your personal API.

---

## Requirement:

1. Create your SteamAPI:
   - Go to https://steamcommunity.com/dev/apikey and get your API key. You need this to use my project. You may need to verify your account via Steam Guard. **Do not show your API key to anyone. It is a confidentional information.**

2.  Select Steam profile: 
	- Select the Steam profile you want to check
	- Find his profile's URL
	- Copy the valid form of ID. Valid ID is without URL. 
	`Example:` https://steamcommunity.com/profiles/6969696969696969/ —> **6969696969696969**

---

### Windows enjoyers:

#### Manual instalation/run:
 1. Open CMD from a project folder and run this: 
	   -  `python -m venv venv`
	   -  `venv\Scripts\pip.exe install -r requirements.txt`
2. Every time you will run my project, you require to use venv:
	   -  `venv\Scripts\python.exe main.py`
#### Auto:
1. Run `setup.bat`
2. Run `run.bat`

---

### Linux/MacOS enjoyers:

#### Manual instalation:
1. Open console from a project folder and run this:
    - `python3 -m venv venv`
    - `./venv/bin/pip install -r requirements.txt`
2.  After that you can open main.py with:
	- `./main.py`
#### Auto:
1.  `chmod +x setup.sh run.sh`
2.  `./setup.sh`
3.  `./run.sh`