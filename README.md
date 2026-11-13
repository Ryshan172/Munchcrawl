# MunchCrawl 

MunchCrawl is a search engine for cravings. 
Connecting you to the dishes your heart (stomach) desires


## Backend 

### Set-up and Running  

Create and activate virtual environment

```
cd backend 

python3 -m venv code_env

source code_env/bin/activate
```

Install required packages in environment

```
pip install -r requirements.txt
```


**Run API**

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be accessible locally at http://localhost:8000/docs#/


TODO: 
- Add docker container 


## Frontend 

C#.NET Blazor (For fun)

.NET is installed in WSL and there's an empty Blazor app in [frontend/](frontend/). 

**installed**
- **.NET SDK 10.0.404**, the current LTS version. I used Microsoft's official `dotnet-install.sh` script because apt needs your sudo password. It installed into `~/.dotnet`, so nothing system-wide changed.
- **Lines in `~/.bashrc`** that set `DOTNET_ROOT` and add .NET to your `PATH`. Open a new terminal or run `source ~/.bashrc` before `dotnet` will work.
- `libicu`, which .NET needs, was already on your system.

**To run it**
```bash
source ~/.bashrc
cd frontend
dotnet watch
```
Then open http://localhost:5150 in your Windows browser. `dotnet watch` reloads the page as you edit.

**For VS Code:** install the **C# Dev Kit** extension inside the WSL window (it appears as "Install in WSL"). That gives you IntelliSense and debugging for `.razor` and `.cs` files.

