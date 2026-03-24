🇪🇹 Amharic DBpedia: LLM-Based RDF Extraction Pipeline
📝 Overview
This project demonstrates a prototype pipeline for extracting structured knowledge from unstructured Amharic text and converting it into RDF triples aligned with the DBpedia Ontology. It addresses the GSoC 2025 goal of automating knowledge graph construction for the Amharic DBpedia chapter using Large Language Models (LLMs).

⚠️ Problem Statement
Wikipedia contains vast amounts of unstructured text, specifically in low-resource languages like Amharic. Converting this into Linked Open Data (LOD) is currently a manual or semi-automated process. This project focuses on using LLMs to automate extraction while maintaining high semantic accuracy via ontology verification.

---

Architecture
The pipeline is designed as a modular neuro-symbolic system:

Plaintext
       Text Input (Amharic)
               ↓
    LLM Extraction (Real/Mock) → [Identifies S-P-O Candidates]
               ↓
     Entity Normalization      → [Maps to DBpedia URIs]
               ↓
    ONTOLOGY VALIDATION LAYER  → [Checks candidates against dbpedia.owl]
               ↓
     RDF Triple Generation    → [Serialization via rdflib]
               ↓
    FastAPI Backend (Port 8000) ↔ Streamlit UI (Port 8501)
✨ Features
Modular Pipeline: Decoupled extraction, mapping, and validation logic.

Ontology-Aware: Real-time validation against official DBpedia Object/Datatype properties.

LLM Integration: Supports high-fidelity relation prediction with mock fallback for reliability.

Interactive Dashboard: Streamlit UI for visualization and knowledge graph metrics.

FAIR Principles: Reproducible setup with standardized RDF output (Turtle format).

API Documentation: Auto-generated Swagger docs via FastAPI.

📂 Project Structure
Plaintext
amharic-dbpediallm-pipeline/
├── data/
│   └── dbpedia_ontology.owl   # Official DBpedia Schema
├── pipeline/
│   ├── extractor.py           # LLM logic
│   ├── validator.py           # NEW: Ontology Check Logic
│   ├── mapper.py              # URI Mapping
│   └── rdf_generator.py       # Turtle serialization
├── api.py                     # FastAPI Backend
├── demo.py                    # Streamlit Frontend
├── requirements.txt           # Dependency list
└── README.md                  # Project documentation
🚀 How to Run

1. Setup Environment
Bash
pip install rdflib fastapi uvicorn streamlit pandas requests


2. Download Ontology Data
Create the data folder and pull the latest DBpedia schema:

Bash
mkdir -p data
curl -L -o data/dbpedia_ontology.owl https://databus.dbpedia.org/ontologies/dbpedia.org/ontology/2022.10.13-080000/ontology_type=orig.owl


3. Launch the System
You need two terminal sessions:

Terminal 1 (Backend): uvicorn api:app --reload

Terminal 2 (Frontend): streamlit run demo.py

📊 Example Output
Input: Addis Ababa is the capital of Ethiopia

Validated RDF (Turtle):

Code snippet
@prefix dbo: <http://dbpedia.org/ontology/> .
@prefix dbr: <http://dbpedia.org/resource/> .

dbr:Addis_Ababa dbo:capital dbr:Ethiopia .
dbr:Ethiopia dbo:location dbr:Africa .


🛠️ Future Enhancements

Integrate fine-tuned Amharic NLP models (e.g., AfroLM).

Implement a SPARQL endpoint for direct querying.

Add Human-in-the-Loop (HITL) verification features in the UI.

Deploy the knowledge graph using Virtuoso.

🤝 Contribution & Author
This is a prototype built for the DBpedia GSoC 2025 exploration phase.
Author: Mahek Maurya (Mahek-01001)