# Enterprise ETL Pipeline & Data Warehouse Synchronizer

A resilient, automated Data Engineering pipeline designed to extract business data from multiple disparate third-party APIs (Stripe and Salesforce), transform and clean the data to fit internal schemas, and load it securely into a centralized PostgreSQL Data Warehouse. 

The system handles rate limiting, pagination, incremental loads, and robust error logging.

---

## 🛠️ Tech Stack

* **Language:** Python 3.11+
* **Data Processing:** Pandas, Polars
* **Orchestration:** Apache Airflow
* **Database/Storage:** SQLAlchemy, PostgreSQL
* **Networking/APIs:** Requests, Tenacity (Retry logic), Pydantic (Data validation)

---

## 📂 Project Structure & Team Assignments

```text
zaalima_etl/
│
├── .env                  # Assigned to: Kamlesh (Local secret API keys - NEVER push to GitHub)
├── .gitignore            # Assigned to: Mohsin Ali (Tells Git which files to ignore)
├── requirements.txt      # Assigned to: Mohsin Ali (Python library dependencies)
├── main.py               # Assigned to: Mohsin Ali (Central entry point script)
│
├── extract/              # Assigned to: Raghuvarshan (Data Extraction)
│   ├── __init__.py       
│   └── models.py         # Assigned to: Raghuvarshan (Pydantic data models for validation)
│
├── transform/            # Assigned to: Hanna Farook (Data Transformation)
│   └── __init__.py       
│
├── load/                 # Assigned to: Sidram (Database & Loading)
│   └── __init__.py       
│
└── dags/                 # Assigned to: Kamlesh (Orchestration)
    └── __init__.py
