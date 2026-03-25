# 🇪🇹 Amharic DBpedia: LLM-Based RDF Extraction Pipeline

## 📝 Overview
>  Built as part of exploration for DBpedia GSoC (Amharic LLM Pipeline project)
This project presents a prototype pipeline for extracting structured knowledge from unstructured text and converting it into RDF triples aligned with the DBpedia Ontology.

It is designed as part of the GSoC exploration for automating knowledge graph construction in the Amharic DBpedia chapter using Large Language Models (LLMs).

---

## ⚠️ Problem Statement

Wikipedia contains vast amounts of unstructured data, especially in low-resource languages like Amharic. Converting this into Linked Open Data (LOD) remains largely manual or semi-automated.

This project aims to automate:

* Entity extraction
* Relation prediction
* Ontology-aligned RDF generation

using LLMs while ensuring semantic correctness through ontology validation.

---

## 🏗️ Architecture

```text
Text Input (Amharic / English)
        ↓
LLM Extraction (Real / Mock)
        ↓
Structured JSON (Entities + Relations)
        ↓
Entity Normalization
        ↓
Ontology Mapping & Validation
        ↓
RDF Triple Generation (rdflib)
        ↓
FastAPI Backend  ↔  UI Layer
```

---

## ✨ Features

* **Modular Pipeline**
  Separate components for extraction, normalization, mapping, and RDF generation

* **LLM Integration**
  Supports real LLMs with fallback mock system for reliability

* **Ontology-Aware Mapping**
  Aligns predicates with DBpedia ontology (`dbo:` namespace)

* **Class + Relation Prediction**
  Generates both `rdf:type` and relationship triples

* **RDF Output (Turtle)**
  Standardized and reusable knowledge graph format

* **API Support**
  FastAPI backend with interactive Swagger documentation

* **End-to-End Demo**
  UI + API integration for real-time testing

---

## 📂 Project Structure

```text
amharic-dbpediallm-pipeline/
├── pipeline/
│   ├── extractor.py        # LLM / mock extraction
│   ├── normalizer.py       # Entity normalization
│   ├── mapper.py           # Ontology mapping
│   └── rdf_generator.py    # RDF triple creation
├── api.py                  # FastAPI backend
├── main.py                 # Local pipeline testing
├── index.html              # Simple UI demo
├── output.ttl              # Generated RDF output
├── README.md               # Documentation
```

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install rdflib fastapi uvicorn
```

---

### 2. Run Pipeline (Local Test)

```bash
python main.py
```

---

### 3. Run Backend API

```bash
uvicorn api:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### 4. RUN UI

Open `index.html` in your browser
````
##UI DEMO
````
<img width="1440" height="900" alt="ui_demo" src="https://github.com/user-attachments/assets/b1f6d952-af96-4553-bf12-809804a41472" />


---

## 📊 Example

### Input

```text
Addis Ababa is the capital of Ethiopia
```

---

### Output (Turtle RDF)

```ttl
@prefix dbo: <http://dbpedia.org/ontology/> .

<http://example.org/resource/Addis_Ababa> rdf:type dbo:City .
<http://example.org/resource/Ethiopia> rdf:type dbo:Country .

<http://example.org/resource/Addis_Ababa> dbo:capital <http://example.org/resource/Ethiopia> .
<http://example.org/resource/Ethiopia> dbo:location <http://example.org/resource/Africa> .
```

---

## 🔐 LLM Integration

The system supports:

* Real LLM-based extraction (OpenAI / HuggingFace)
* Fallback mock extraction for offline reliability

---

## 🛠️ Future Enhancements

* Amharic-specific NLP model integration
* Ontology validation using official DBpedia schema
* SPARQL endpoint for querying
* Full web deployment
* Human-in-the-loop validation system

---

## 🤝 Contribution

This project is part of the exploration phase for the DBpedia GSoC program.

Contributions, feedback, and suggestions are welcome.

---

## 👤 Author

**Mahek Maurya**

