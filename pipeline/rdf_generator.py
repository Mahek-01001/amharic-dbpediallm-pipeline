from rdflib import Graph, URIRef, Namespace, RDF
from pipeline.normalizer import normalize
from pipeline.mapper import map_predicate

EX = Namespace("http://example.org/resource/")
DBO = Namespace("http://dbpedia.org/ontology/")

def generate_rdf(data):
    g = Graph()

    g.bind("dbo", DBO)

    # 🔥 ADD THIS BLOCK (CLASS PREDICTION)
    if "entities" in data:
        for ent in data["entities"]:
            subject = URIRef(EX[normalize(ent["name"])])
            obj = URIRef(DBO[normalize(ent["type"])])
            g.add((subject, RDF.type, obj))

    # Existing relation logic
    for rel in data["relations"]:
        if rel.get("confidence", 1) < 0.7:
            continue

        s = URIRef(EX[normalize(rel["subject"])])
        p = map_predicate(rel["predicate"])
        o = URIRef(EX[normalize(rel["object"])])

        g.add((s, p, o))

    return g.serialize(format="turtle")