# 🏥 Healthcare Claims & Risk Adjustment Data Pipeline

This project demonstrates a **production-style healthcare data pipeline** designed to ingest, process, and analyze Medicare claims data for **risk adjustment (RAF scoring)** and analytics.

It simulates real-world data engineering practices using modular components such as ingestion, transformation, orchestration, and data quality validation.

---

## 🚀 Overview

* Ingests healthcare claims data (simulated streaming)
* Processes and transforms data for analytics
* Applies risk adjustment logic (HCC-style flagging)
* Ensures data quality through validation checks
* Demonstrates scalable pipeline architecture

---

## 🧱 Architecture Diagram

```
                ┌──────────────────────┐
                │   Data Source        │
                │ (Claims JSON Data)  │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │   Ingestion Layer    │
                │ (Python Producer)    │
                │ Simulates Pub/Sub    │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │ Processing Layer     │
                │ (Pandas / PySpark)   │
                │ - Deduplication      │
                │ - Risk Flagging      │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │ Data Quality Layer   │
                │ - Null Checks        │
                │ - Value Validation   │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │ Data Modeling Layer  │
                │ (DBT-style SQL)      │
                │ - Aggregations       │
                │ - Analytics Tables   │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │ Data Warehouse       │
                │ (Simulated BigQuery) │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │ Analytics / Output   │
                │ Reporting & Insights │
                └──────────────────────┘
```

---

## 📁 Project Structure

```
healthcare-claims-pipeline/
│
├── data/
│   └── sample_claims.json        # Input dataset
│
├── ingestion/
│   └── producer.py              # Simulated streaming ingestion
│
├── processing/
│   └── transform.py             # Data transformation logic
│
├── utils/
│   └── data_quality.py          # Data validation checks
│
├── dbt_models/
│   ├── staging.sql              # Staging layer
│   └── marts.sql                # Aggregated analytics layer
│
├── airflow/
│   └── dag.py                   # Pipeline orchestration (Airflow)
│
└── README.md
```

---

## ⚙️ Key Features

* ✅ Simulated real-time ingestion pipeline
* ✅ Deduplication of claims data
* ✅ HCC-style high-risk flagging
* ✅ Data quality validation (null checks, constraints)
* ✅ Modular and scalable pipeline design
* ✅ DBT-style transformation layers
* ✅ Airflow orchestration

---

## 📊 Sample Processing Logic

* Identifies high-risk patients using diagnosis codes
* Removes duplicate claim records
* Aggregates claims data at member level
* Produces analytics-ready datasets

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install pandas
```

### 2. Run ingestion (simulated streaming)

```
python ingestion/producer.py
```

### 3. Run transformation

```
python processing/transform.py
```

---

## 📈 Performance (Simulated)

* Designed for ~150K records/day ingestion
* Optimized for scalable batch processing
* Supports partitioned and incremental modeling concepts

---

## 🛠️ Tech Stack

* Python (Pandas)
* SQL
* Apache Airflow (conceptual)
* DBT (conceptual)
* GCP (BigQuery, Pub/Sub – simulated)

---

## 👩‍💻 My Role

* Designed end-to-end data pipeline architecture
* Implemented ingestion, transformation, and validation layers
* Modeled data using warehouse-style transformations
* Applied healthcare domain logic for risk adjustment

---

## ⚠️ Disclaimer

This project is a **lightweight simulation of a production-grade data pipeline**, focusing on architecture, design patterns, and core data engineering concepts rather than full cloud deployment.

---

## 💡 Future Improvements

* Integrate real GCP services (Pub/Sub, BigQuery)
* Add DBT tests and documentation
* Implement streaming using Kafka
* Introduce data observability tools (e.g., Great Expectations)
* Deploy pipeline using Docker and CI/CD

---

## ⭐ If you found this useful

Feel free to star the repo or connect with me!
