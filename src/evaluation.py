import json
from smolagents import LiteLLMModel

def evaluate_rag_response(
        prompt: str, 
        judge_llm: LiteLLMModel,
        eval_name: str,
    ) -> dict:

    messages = [
        {"role": "system", "content": "You are a fair evaluator language model."},
        {"role": "user", "content": prompt},
    ]

    response = judge_llm.generate(messages)
    response_dict = json.loads(
        response.content.strip(' ').strip('`').strip('json\n')
    )
    response_dict = {f"{eval_name}_{k}": v for k, v in response_dict.items()}

    return response_dict