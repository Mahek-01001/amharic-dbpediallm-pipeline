from fastapi import FastAPI
from pydantic import BaseModel
from pipeline.extractor import extract
from pipeline.rdf_generator import generate_rdf

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/extract")
def extract_api(input: TextInput):
    data = extract(input.text)
    rdf = generate_rdf(data)
    return {"rdf": rdf}