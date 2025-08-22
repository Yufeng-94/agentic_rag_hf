sports_cfg = {
        "name": "sports_retriever",
        "description": "Using semantic similarity, retrieves documents from the sports knowledge base that have the closest embeddings to the input query. Covers topics like player statistics, match results, team histories, and sports records.",
        "inputs": {
            "query": {
                "type": "string",
                "description": "The sports-related query to perform. Use the affirmative form rather than a question."
            }
        },
        "output_type": "string"
    }
finance_cfg = {
        "name": "finance_retriever",
        "description": "Using semantic similarity, retrieves documents from the finance knowledge base that have the closest embeddings to the input query. Covers topics like earnings reports, market trends, stock performance, and economic indicators.",
        "inputs": {
            "query": {
                "type": "string",
                "description": "The finance-related query to perform. Use the affirmative form rather than a question."
            }
        },
        "output_type": "string"
    }
movie_cfg = {
        "name": "movie_retriever",
        "description": "Using semantic similarity, retrieves documents from the movie knowledge base that have the closest embeddings to the input query. Covers topics like film synopses, box office data, cast information, and critical reception.",
        "inputs": {
            "query": {
                "type": "string",
                "description": "The movie-related query to perform. Use the affirmative form rather than a question."
            }
        },
        "output_type": "string"
    }
unified_cfg = {
        "name": "unified_retriever",
        "description": "Using semantic similarity, retrieves documents from the sports, finance, and movie knowledge base that have the closest embeddings to the input query",
        "inputs": {
            "query": {
                "type": "string",
                "description": "The query to perform. Use the affirmative form rather than a question."
            }
        },
        "output_type": "string"
    }