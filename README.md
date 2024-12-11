## Executar a api
### Criar ambiente com venv

```
cd api
python -m venv .venv

# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### Instalar dependencias

```
pip install uvicorn fastapi
```

### Executar api

```
uvicorn main:app --reload
```

## Executar o frontend
### Criar ambiente com venv

```
cd frontend
python -m venv .venv

# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### Instalar dependencias

```
pip install streamlit
```

### Executar streamlit

```
streamlit run app.py
```