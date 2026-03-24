import os
from rdflib import Graph, Namespace, RDF, OWL

class OntologyValidator:
    def __init__(self, ontology_path="data/dbpedia_ontology.owl"):
        self.valid_properties = set()
        
        if not os.path.exists(ontology_path) or os.path.getsize(ontology_path) < 100:
            print("❌ Error: Ontology file is missing or invalid. Using fallback properties.")
            self.valid_properties = {"capital", "population", "leader", "location"}
            return

        try:
            print(f"⏳ Loading DBpedia Ontology from {ontology_path}...")
            g = Graph()
            # This might take 10-20 seconds the first time
            g.parse(ontology_path, format="xml")
            
            # Extract all property names into a fast-search Set
            for s in g.subjects(RDF.type, OWL.ObjectProperty):
                self.valid_properties.add(str(s).split('/')[-1])
            for s in g.subjects(RDF.type, OWL.DatatypeProperty):
                self.valid_properties.add(str(s).split('/')[-1])
                
            print(f"✅ Success! Loaded {len(self.valid_properties)} valid DBpedia properties.")
        except Exception as e:
            print(f"⚠️ Parsing failed: {e}. Check if the file is valid XML.")
            self.valid_properties = {"capital", "population"}

    def validate_triple(self, subject, predicate, obj):
        # Clean the predicate (e.g., 'dbo:capital' -> 'capital')
        clean_p = predicate.split(':')[-1].split('/')[-1]
        
        if clean_p in self.valid_properties:
            return True, "Verified ✅"
        else:
            return False, f"Invalid ❌ ('{clean_p}' not in DBO)"