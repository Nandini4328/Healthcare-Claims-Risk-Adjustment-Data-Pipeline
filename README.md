# 🏥 Healthcare Claims & Risk Adjustment Data Pipeline

A **production-style healthcare data pipeline (simulated locally)** designed to ingest, process, and transform Medicare claims data for **risk adjustment (RAF scoring)** and analytics.

This project demonstrates real-world data engineering practices including ingestion, transformation, data quality validation, and analytical modeling.

---

## 🚀 Overview

* Processes healthcare claims data (simulated streaming + batch)
* Applies risk adjustment logic (HCC-style flagging)
* Implements data quality checks and deduplication
* Produces analytics-ready datasets for reporting
* Follows scalable, cloud-native architecture principles

---

## 🚨 Problem Statement

Healthcare organizations process large volumes of claims data daily, which must be transformed into accurate datasets for **risk adjustment and regulatory reporting**.

Raw data challenges include:

* Duplicate records across ingestion sources
* Inconsistent schemas and formats
* Missing validation and data quality checks
* Poor query performance for analytics

---

## 💡 Solution Approach

This project implements a **layered data pipeline architecture**:

* **Ingestion Layer** → Simulates streaming ingestion (Pub/Sub style)
* **Processing Layer** → Deduplication, transformation, enrichment
* **Data Quality Layer** → Validation and schema checks
* **Modeling Layer** → DBT-style transformations
* **Serving Layer** → Analytics-ready datasets

The design emphasizes modularity, scalability, and maintainability.

---

## 🧱 System Architecture

### 🔹 End-to-End Pipeline

```id="arch_full"
                    ┌──────────────────────────────┐
                    │   Healthcare Data Source     │
                    │  (Claims / Encounter Data)   │
                    └─────────────┬────────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────────┐
                    │     Ingestion Layer          │
                    │  Python Producer (Simulated) │
                    │  → Mimics Pub/Sub Streaming  │
                    └─────────────┬────────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────────┐
                    │    Processing Layer          │
                    │  (Pandas / PySpark Logic)    │
                    │  - Deduplication             │
                    │  - HCC Risk Flagging         │
                    │  - Data Transformation       │
                    └─────────────┬────────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────────┐
                    │    Data Quality Layer        │
                    │  - Null Checks               │
                    │  - Schema Validation         │
                    │  - Business Rules            │
                    └─────────────┬────────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────────┐
                    │   Data Modeling Layer        │
                    │     (DBT-style SQL)         │
                    │  - Staging Models           │
                    │  - Mart / Aggregations      │
                    └─────────────┬────────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────────┐
                    │     Data Warehouse           │
                    │   (Simulated BigQuery)       │
                    │  Partitioned / Analytical    │
                    └─────────────┬────────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────────┐
                    │   Analytics & Reporting      │
                    │  RAF Scoring / Insights      │
                    └──────────────────────────────┘
```

---

### ☁️ Production Architecture (GCP Mapping)

```id="arch_gcp"
Pub/Sub → Cloud Composer (Airflow) → Dataflow / Spark
      → DBT → BigQuery → BI / Reporting
```

---

## 📁 Project Structure

```id="proj_struct"
healthcare-claims-pipeline/
│
├── data/
│   └── sample_claims.json
│
├── ingestion/
│   └── producer.py
│
├── processing/
│   └── transform.py
│
├── utils/
│   └── data_quality.py
│
├── dbt_models/
│   ├── staging.sql
│   └── marts.sql
│
├── airflow/
│   └── dag.py
│
└── README.md
```

---

## ⚙️ Key Features

* ✅ Simulated real-time ingestion pipeline
* ✅ Deduplication using unique claim identifiers
* ✅ HCC-style high-risk patient flagging
* ✅ Data quality validation (null checks, constraints)
* ✅ Modular and scalable architecture
* ✅ DBT-style transformation layers
* ✅ Airflow-based orchestration

---

## ⚙️ Engineering Decisions

### 🔹 Modular Design

Each layer (ingestion → processing → modeling) is decoupled for scalability and maintainability.

### 🔹 Idempotent Processing

Deduplication ensures safe reprocessing without duplicate records.

### 🔹 Data Quality First

Validation is applied before downstream transformations to prevent bad data propagation.

### 🔹 Domain-Specific Logic

Implements healthcare-specific risk logic (HCC-style flags).

---

## 📊 Sample Data Processing

* Removes duplicate claims
* Flags high-risk diagnosis codes
* Aggregates claims at member level
* Prepares analytics-ready datasets

---

## ▶️ How to Run

### 1. Install dependencies

```id="run1"
pip install pandas
```

### 2. Run ingestion (simulated streaming)

```id="run2"
python ingestion/producer.py
```

### 3. Run transformation

```id="run3"
python processing/transform.py
```

---

## 📈 Performance (Simulated Scenario)

* Designed for **~150K records/day ingestion**
* Optimized for scalable processing patterns
* Supports partitioned and incremental modeling concepts
* Reduces downstream query latency through structured transformations

---

## 🔧 Technology Stack

| Layer         | Technology                  |
| ------------- | --------------------------- |
| Ingestion     | Python (Pub/Sub simulation) |
| Processing    | Pandas / PySpark            |
| Orchestration | Apache Airflow              |
| Data Modeling | DBT-style SQL               |
| Storage       | Simulated BigQuery          |
| Data Quality  | Custom validation           |

---

## 👩‍💻 My Role

* Designed end-to-end data pipeline architecture
* Implemented ingestion, transformation, and validation layers
* Built modular pipeline components
* Applied healthcare domain logic for risk adjustment
* Optimized structure for scalability and maintainability

---

## ⚠️ Disclaimer

This project is a **lightweight simulation of a production-grade pipeline**, focusing on architecture, design patterns, and core data engineering concepts rather than full cloud deployment.

---

## 💡 Future Improvements

* Integrate real GCP services (Pub/Sub, BigQuery)
* Add DBT tests and documentation
* Implement streaming with Kafka
* Add data observability (Great Expectations)
* Containerize with Docker and CI/CD pipelines

---

## ⭐ If you found this useful

Feel free to ⭐ the repo or connect with me!
