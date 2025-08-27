# Agentic RAG Demo
This repository showcases a step-by-step demo for building an **agentic Retrieval-Augmented Generation (RAG)** system using the Hugging Face ecosystem. The system leverages a multi-source knowledge base and integrates decision-making agents to dynamically retrieve and synthesize information.


## 📚 Dataset Overview

The demo uses the [**CRAG dataset**](https://github.com/facebookresearch/CRAG), which contains questions across five domains. Each question is paired with:

- Five searched web pages in HTML format
- A ground-truth answer

For this demo, 100 questions from three selected domains are used. Each domain's web pages are parsed and combined to form three separate knowledge bases. These are indexed using **FAISS** with the embedding model [`thenlper/gte-small`](https://huggingface.co/thenlper/gte-small).

## 🤖 Agentic RAG Workflow

The system uses **OpenAI's `o3-mini`** model as both the agent and the generative engine. Here's how it works:

1. A question is first passed to the AI agent.
2. The agent decides which domain-specific vector database to query.
3. Retrieved documents are fed back to the agent to generate a response.
4. The agent may decide to query additional sources before finalizing the answer.

This iterative, decision-driven retrieval loop defines the **agentic** nature of the system.

## 🧪 Evaluation

To assess performance, 50 questions are selected for comparison between:
- The agentic RAG system
- A standard one-shot RAG baseline

Evaluation is conducted using **OpenAI's `gpt-4o`** as a judge model, scoring each answer on:
- **Faithfulness**
- **Relevance**
- **Completeness**

Each metric is rated on a scale from 1 to 5. Results show that the agentic RAG system outperforms the baseline by **9–18%** across metrics, demonstrating the strength of agent-driven retrieval.

## ⚙️ Environment Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management. Install dependencies by running

```bash
poetry lock
poetry install
```

Activate the environment by running

```bash
eval $(poetry env activate)
```

Pre-requisite:
- An OpenAI API key
- A Hugging Face account (for model and dataset access)

## 📓 Notebooks

The repository includes 5 Jupyter notebooks that walk through the entire pipeline:

1. Data cleaning
2. Knowledge base construction
3. Evaluation dataset construction
4. Agentic RAG creation
5. Evaluate

Running the notebook in order provides a clear, reproducible path from raw data to final evaluation.

⚠️ Note: RAG performance may vary from time to time due to the stochastic nature of LLMs.