#  LLM-based RDF Extraction Pipeline for Amharic DBpedia

##  Overview

This project demonstrates a prototype pipeline for extracting structured knowledge from unstructured text and converting it into RDF triples aligned with DBpedia ontology.

The system simulates how Large Language Models (LLMs) can be used to automate knowledge graph construction for the Amharic DBpedia chapter.

---

##  Problem Statement

Wikipedia contains vast amounts of unstructured text, which is difficult to use in structured applications like search, analytics, and NLP tasks.

DBpedia aims to convert this data into structured knowledge graphs. This project focuses on automating that process using LLMs.

---

##  Proposed Solution

We designed a modular pipeline that:

1. Extracts entities and relationships from text (LLM / simulated)
2. Normalizes entity names
3. Maps relationships to DBpedia ontology
4. Generates RDF triples in Turtle (.ttl) format
5. Exposes results via API and UI

---

##  Architecture

```
Text Input
   ↓
LLM Extraction (Mock / Real)
   ↓
Structured JSON
   ↓
Normalization
   ↓
Ontology Mapping
   ↓
RDF Triple Generation
   ↓
API (FastAPI) → UI (HTML)
```

---

##  Features

*  Modular pipeline architecture
*  LLM-based extraction (with fallback support)
*  RDF triple generation using rdflib
*  DBpedia ontology mapping (`dbo:` prefix)
*  REST API using FastAPI
*  Simple UI for demonstration
*  Confidence-based filtering
*  Multi-relation support
*  Class (rdf:type) prediction using entity extraction

---

##  Project Structure

```
amharic-dbpediallm-pipeline/
├── api.py
├── main.py
├── index.html
├── README.md
├── output.ttl
├── pipeline/
│   ├── extractor.py
│   ├── normalizer.py
│   ├── mapper.py
│   └── rdf_generator.py
```

---

##  Example

### Input:

```
Addis Ababa is the capital of Ethiopia
```

### Output (RDF):

```ttl
@prefix dbo: <http://dbpedia.org/ontology/> .

<http://example.org/resource/Addis_Ababa> dbo:capital <http://example.org/resource/Ethiopia> .
<http://example.org/resource/Ethiopia> dbo:location <http://example.org/resource/Africa> .
```

---

##  How to Run

### 1. Install dependencies


pip install rdflib fastapi uvicorn


### 2. Run pipeline


python main.py


### 3. Run API


uvicorn api:app --reload


### 4. Open API docs


http://127.0.0.1:8000/docs


### 5. Open UI

Open `index.html` in browser

---

##  LLM Integration

The system supports:

* Real LLM integration (OpenAI)
* Fallback mock extraction (for reliability)

---

##  Future Enhancements

* Integrate real Amharic NLP models
* Improve ontology alignment with DBpedia
* Add SPARQL endpoint support
* Deploy as a web service
* Fine-tune LLM for relation extraction

---

##  Contribution

This is a prototype built as part of exploration for DBpedia GSoC project.

Feedback and suggestions are welcome!

---

##  Author

Mayank Maurya
