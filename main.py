from pipeline.extractor import extract
from pipeline.rdf_generator import generate_rdf

text = "Addis Ababa is the capital of Ethiopia"

data = extract(text)
rdf = generate_rdf(data)


print(rdf)

with open("output.ttl", "w") as f:
    f.write(rdf)

print(" RDF saved to output.ttl")