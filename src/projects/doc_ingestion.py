from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
import shutil
from pydantic import  HttpUrl


from src.loaders.text_loader import TextLoader
from src.loaders.pdf_loader import PdfLoader
from src.loaders.web_loader import WebLoader
from src.loaders.arxiv_loader import ArxivLoader

router = APIRouter(prefix="/ingestion", tags=["Data Ingestions"])

@router.post("/upload-file")
async def upload_and_process(file: UploadFile = File(...)):
    """
    Uploads a file (PDF or TXT), extracts text
    """

    content = await file.read()
    file_name = file.filename.lower()

    extracted_text = ""

    if file_name.endswith('.txt'):
        loader = TextLoader()
        extracted_text = loader.load(content)
    elif file_name.endswith('.pdf'):
        loader = PdfLoader()
        extracted_text = loader.load(content)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type. Use .pdf, .txt, or .md")
    
    return {
        "source": file.filename,
        "type": "file",
        "extracted_text": extracted_text,
        "total_characters": len(extracted_text)
    }

@router.post("/ingest-url")
async def ingest_from_url(url: HttpUrl):
    """
    Scrapes a website URL, extracts text, and chunks it.
    """
    loader = WebLoader()
    url_str = str(url)

    extracted_text = loader.load(url_str)

    if extracted_text.startswith('Error loading website'):
        raise HTTPException(status_code=400, detail=extracted_text)
    
    return {
        "source": url_str,
        "extracted_text": extracted_text,
        "total_characters": len(extracted_text)
    }

@router.post("/ingest-arxiv")
async def ingest_from_arxiv(query: str):
    loader = ArxivLoader()
    extracted_text = loader.load(query)

    if extracted_text.startswith("Error") or extracted_text == "No papers found for this query.":
        raise HTTPException(status_code=400, detail=extracted_text)

    return {
        "source": query,
        "type": "Arxiv PDF",
        "extracted_text": extracted_text,
        "total_characters": len(extracted_text)
    }