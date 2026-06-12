# LankaDayOuts - Backend

FastAPI backend service for LankaDayOuts, providing APIs for holiday packages and database connection health checks. It interfaces with a TiDB serverless database.

## Tech Stack

- **Language:** Python 3.11+
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (v0.136+)
- **ASGI Server:** [Uvicorn](https://www.uvicorn.org/) (v0.48+)
- **Database:** [TiDB Cloud](https://pingcap.com/products/tidb-serverless) (Serverless MySQL)
- **Database Driver:** [PyMySQL](https://pymysql.readthedocs.io/)
- **ORM / Query Builder:** [SQLAlchemy](https://www.sqlalchemy.org/) (v2.0+)
- **Settings Management:** [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) (v2.0+)

---

## Folder Structure

```
LankaDayOuts-Backend/
├── app/
│   ├── main.py            # FastAPI application entry point, CORS, and router configuration
│   ├── api/
│   │   ├── deps.py        # Dependency injection helpers (database session)
│   │   └── package.py     # Endpoint router for packages and DB test
│   ├── core/
│   │   └── config.py      # Configuration management (Pydantic Settings)
│   └── db/
│       └── session.py     # SQLAlchemy database engine and connection pool session setup
├── database/
│   └── db.txt             # SQL schema definitions and sample seed data (TiDB/MySQL)
├── nginx/                 # Nginx configuration directory
├── .env                   # Environment variables (Database URLs, credentials)
├── .gitignore
├── LICENSE
├── requirements.txt       # Python package dependencies
└── README.md              # Project documentation (this file)
```

---

## Database Schema (`database/db.txt`)

The database consists of the following tables:

1. **`packages`**: Holds day-out and night-out holiday package details.
   - `id` (VARCHAR(36), PK)
   - `title` (TEXT)
   - `location` (TEXT)
   - `price` (DECIMAL)
   - `rating` (DECIMAL)
   - `reviews_count` (INT)
   - `type` (ENUM: `'Couple'`, `'Group'`, `'Family'`)
   - `category` (ENUM: `'Dayout'`, `'Nightout'`)
   - `image` (TEXT)
   - `is_featured` (BOOLEAN)
2. **`tags`**: Stores unique tags (e.g. `'Dinner'`, `'Heritage Walk'`).
3. **`package_tags`**: Many-to-many relationship mapping packages to tags.

---

## Setup & Local Development

### 1. Environment Configuration

Create a `.env` file in the root directory and provide your TiDB database connection URL:

```env
DATABASE_URL=mysql+pymysql://<db_user>:<db_password>@<db_host>:<port>/dayout_db
```

### 2. Install Dependencies

It is recommended to run the backend in a virtual environment:

#### Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Initialize Database Schema
Import the SQL commands from [database/db.txt](file:///c:/Users/anjul/Documents/LankaDayOuts-Backend/database/db.txt) into your TiDB / MySQL server to create the schema and seed the initial package information.

---

## Running the Application

Start the FastAPI ASGI server using Uvicorn:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

- **Interactive API Docs (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative Docs (ReDoc):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

### 1. Welcome / Root Endpoint
- **URL:** `GET /`
- **Response:**
  ```json
  { "message": "Welcome to the Lanka Day Outs Backend" }
  ```

### 2. Database Connectivity Test
- **URL:** `GET /test-db`
- **Response:**
  ```json
  { "status": "TiDB connected successfully" }
  ```

### 3. Fetch Packages
- **URL:** `GET /packages`
- **Response:** Returns list of available packages, formatting fields to match frontend consumption.
  ```json
  {
    "packages": [
      {
        "id": "1",
        "title": "Galle Fort Heritage Night",
        "location": "Galle, Sri Lanka",
        "price": 12000.0,
        "rating": 4.9,
        "reviewsCount": 203,
        "type": "Group",
        "category": "Nightout",
        "image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4",
        "tags": [],
        "isFeatured": true
      }
    ]
  }
  ```
