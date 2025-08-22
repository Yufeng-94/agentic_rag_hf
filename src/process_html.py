from typing import List
import pandas as pd
from trafilatura import extract, extract_metadata
from langchain.schema import Document

import json
import logging

def html_to_document(html_content: str, interaction_id: str) -> Document:
    """Convert HTML content to a LangChain Document."""
    # Extract text from HTML content
    text = extract(html_content)
    
    # Extract metadata from HTML content
    extracted_metadata = extract_metadata(html_content)

    # Fetch metadata fields
    metadata = {
        "source":extracted_metadata.url,
        "title":extracted_metadata.title,
        "description":extracted_metadata.description,
        "interaction_id": interaction_id,
    }

    # Create and return a LangChain Document
    if text: # if text is not None
        return Document(
            page_content=text,
            metadata=metadata
        )
    
    logging.warning(f"No text extracted from HTML content. interaction_id: {interaction_id}")
    return None

def record_to_document_list(record: dict) -> List[Document]:
    """Convert a record of CRAG sample to a list of LangChain Documents."""
    documents = []
    interaction_id = record['interaction_id']

    for page in record['search_results']:
        doc = html_to_document(
            html_content=page['page_result'],
            interaction_id=interaction_id,
        )
        if doc: # if doc is not None
            documents.append(doc)

    return documents

def remove_duplicate_pages(documents: List[Document]) -> List[Document]:
    """Remove duplicate pages from a list of LangChain Documents."""
    seen_urls = set()
    unique_documents = []
    
    for doc in documents:
        url = doc.metadata.get("source")
        if url and url not in seen_urls:
            seen_urls.add(url)
            unique_documents.append(doc)

        else:
            logging.warning(f"Duplicate or missing URL found: {url}")
    
    return unique_documents

def record_sanity_check(record: dict, metadata_fields: pd.Series) -> None:
    if record['domain'] != metadata_fields['domain']:
        raise ValueError(f"Domain mismatch: {record['domain']} != {metadata_fields['domain']}")
    if record['question_type'] != metadata_fields['question_type']:
        raise ValueError(f"Question type mismatch: {record['question_type']} != {metadata_fields['question_type']}")
    if record['static_or_dynamic'] != metadata_fields['static_or_dynamic']:
        raise ValueError(f"Static or dynamic mismatch: {record['static_or_dynamic']} != {metadata_fields['static_or_dynamic']}")
    
def save_documents_as_jsonl(documents: List[Document], output_path: str) -> None:
    """Save a list of LangChain Documents to a JSONL file."""
    docs_as_dicts = [{"page_content": doc.page_content, "metadata": doc.metadata}\
                      for doc in documents]
    
    with open(output_path, "w", encoding="utf-8") as f:
        for doc_dict in docs_as_dicts:
            f.write(json.dumps(doc_dict, ensure_ascii=False) + "\n")
            

def load_documents_from_jsonl(input_path: str) -> List[Document]:
    """Load a list of LangChain Documents from a JSONL file."""
    documents = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            doc = json.loads(line)
            documents.append(
                Document(page_content=doc["page_content"], metadata=doc["metadata"])
                )
    return documents
 