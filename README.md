# 🧠 Retail Data Intelligence Platform  

An end-to-end **ETL + API + Analytics** project that extracts, transforms, and visualizes retail sales data.  
This platform demonstrates how data engineering and analytics come together to power business insights.

---

## 📘 Overview

The **Retail Data Intelligence Platform** is designed to automate the data flow for retail sales.  
It performs:
- Data extraction from raw files or APIs  
- Data transformation and enrichment using Python & Pandas  
- Loading into a relational database (MySQL / AlloyDB)  
- Exposing APIs via FastAPI for external access  
- Visualizing analytics in Streamlit dashboards  

It’s a fully functional **mini data engineering system**, simulating how real-world retail platforms process and visualize data.

---

## 🧱 System Architecture

+-----------------+
| Data Sources | ← CSV / API / Mock Generator
+-----------------+
|
▼
+-----------------+
| Extract Layer | ← Python ETL Script
+-----------------+
|
▼
+-----------------+
| Transform Layer | ← Pandas Cleaning + Enrichment
+-----------------+
|
▼
+-----------------+
| Load Layer | ← MySQL / AlloyDB
+-----------------+
|
▼
+-----------------+
| API Layer | ← FastAPI (for KPIs & insights)
+-----------------+
|
▼
+-----------------+
| Visualization | ← Streamlit Dashboard
+-----------------+

---

## ⚙️ Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| **Language** | Python 3 |
| **ETL** | Pandas, SQLAlchemy, Talend (optional) |
| **Backend (API)** | FastAPI |
| **Frontend / Dashboard** | Streamlit |
| **Database** | MySQL / AlloyDB |
| **Cloud** | AWS (S3, EC2, Lambda) |
| **Testing & Logging** | unittest, logging, mock |

---

## 🧩 Features

✅ Automated ETL pipeline (Extract → Transform → Load)  
✅ Configurable data sources (CSV / API / Database)  
✅ Real-time metrics API with FastAPI  
✅ Interactive analytics dashboard (Streamlit)  
✅ Integrated logging and error handling  
✅ Cloud-ready structure (deploy to AWS easily)  
✅ Modular codebase with separate layers for ETL, API, and UI  

---

## 📊 Example KPIs

The dashboard provides insights like:

- 💰 **Total Revenue by City / Category**  
- 🛍️ **Top Products by Sales Volume**  
- 💳 **Payment Methods Breakdown**  
- 🕒 **Revenue Trends Over Time**  
- 📦 **Customer & Order Analytics**

