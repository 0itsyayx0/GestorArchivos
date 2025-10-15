# GestorArchivos

# GestorArchivos - API (Autenticación y Autorización)

## Resumen
API en Flask con:
- registro/login con JWT (access + refresh)
- autorización por roles (ej: `admin`, `editor`, `user`)
- endpoints protegidos por roles
- pruebas con pytest
- archivos de almacenamiento JSON simples (users.json, data.json)

## Requisitos
- Python 3.10+
- Instalar dependencias:
```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
