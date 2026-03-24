from rdflib import Namespace

DBO = Namespace("http://dbpedia.org/ontology/")

def map_predicate(predicate):
    mapping = {
        "capitalOf": DBO.capital,
        "locatedIn": DBO.location
    }
    return mapping.get(predicate, DBO.relatedTo)