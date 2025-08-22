from smolagents.tools import Tool
from langchain.vectorstores import VectorStore


class RetrieverTool(Tool):
    name = "retriever"
    description = "Using semantic similarity, retrieves some documents from the knowledge base that have the closest embeddings to the input query."
    inputs =  {
        "query": {
            "type": "string", 
            "description": "The query to perform. This should be semantically close to your target documents. Use the affirmative form rather than a question."
        }
    }

    output_type = "string"

    def __init__(self,  vectordb: VectorStore, cfg: dict, **kwargs):
        super().__init__(**kwargs)
        self.description = cfg['description']
        self.name = cfg['name']
        self.inputs = cfg['inputs']
        self.output_type = cfg['output_type']
        self.vectordb = vectordb

    def forward(self, query: str) -> str:
        assert isinstance(query, str)

        docs = self.vectordb.similarity_search(
            query,
            k=7,
        )

        return "\nRetrieved Documents:\n" + "".join(
            [f"===== Document {str(i)} =====\n" + doc.page_content for i, doc in enumerate(docs)]
        )