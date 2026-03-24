import streamlit as st
import requests
import pandas as pd

# 1. Page Configuration (The "Professional" touch)
st.set_page_config(
    page_title="Amharic DBpedia LLM Pipeline",
    page_icon="🇪🇹",
    layout="wide"
)

# 2. Sidebar for GSoC Project Info (Addresses FAIR principles)
with st.sidebar:
    st.title("📌 Project Overview")
    st.info("""
    **Goal:** Automate Amharic DBpedia extraction using LLMs.
    **Standards:** RDF, Turtle, OWL.
    """)
    st.markdown("---")
    st.subheader("Pipeline Status")
    try:
        # Quick health check to see if backend is up
        health = requests.get("http://127.0.0.1:8000/docs", timeout=2)
        st.success("✅ Backend: Online")
    except:
        st.error("❌ Backend: Offline")
        st.caption("Run 'uvicorn api:app --reload' in your terminal.")

# 3. Main UI Header
st.title("🇪🇹 Amharic DBpedia Knowledge Extraction")
st.markdown("This prototype extracts structured triples from Amharic text and validates them against the official **DBpedia Ontology**.")

# 4. Input Section
input_text = st.text_area(
    "Enter Amharic Text (or English for testing):", 
    value="Addis Ababa is the capital of Ethiopia",
    height=150
)

# 5. Action Button
if st.button("Extract & Validate Triples", type="primary"):
    if not input_text:
        st.warning("Please enter some text first!")
    else:
        with st.spinner("LLM Extracting and Validating against Ontology..."):
            try:
                # API Call to your FastAPI backend
                response = requests.post(
                    "http://127.0.0.1:8000/extract", 
                    json={"text": input_text},
                    timeout=30
                )
                
                if response.status_code == 200:
                    data = response.json()
                    triples = data.get('triples', [])
                    rdf_output = data.get('rdf_output', '')

                    # Layout: Two columns for Results
                    col1, col2 = st.columns([2, 1])

                    with col1:
                        st.subheader("📊 Extracted Knowledge Graph")
                        if triples:
                            # Convert to DataFrame for a clean UI table
                            df = pd.DataFrame(triples)
                            
                            # Highlight the 'status' column to show the Validator worked
                            st.dataframe(
                                df, 
                                use_container_width=True,
                                column_config={
                                    "status": st.column_config.TextColumn("Validation Status", help="Checked against dbpedia_ontology.owl")
                                }
                            )
                        else:
                            st.info("No triples were extracted. Try different text.")

                    with col2:
                        st.subheader("✅ Validation Summary")
                        if triples:
                            # Calculate accuracy for your GSoC Impact report
                            valid_count = len([t for t in triples if "Verified" in str(t.get('status', ''))])
                            accuracy = (valid_count / len(triples)) * 100
                            st.metric("Ontology Alignment", f"{accuracy:.1f}%")
                            st.progress(accuracy / 100)
                        else:
                            st.write("No metrics available.")

                    # RDF Output Section
                    st.markdown("---")
                    st.subheader("📄 Generated RDF (Turtle Format)")
                    st.code(rdf_output, language='turtle')
                    
                    # Download Button for the .ttl file
                    st.download_button(
                        label="Download .ttl File",
                        data=rdf_output,
                        file_name="output.ttl",
                        mime="text/turtle"
                    )

                else:
                    st.error(f"Backend Error: {response.status_code}")
                    st.json(response.json())

            except requests.exceptions.ConnectionError:
                st.error("Connection Error: Is your FastAPI server running on http://127.0.0.1:8000?")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

# Footer
st.markdown("---")
st.caption("Built for DBpedia GSoC 2025 Exploration | Author: Mahek Maurya")