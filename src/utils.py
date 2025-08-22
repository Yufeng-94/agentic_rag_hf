from dotenv import load_dotenv, find_dotenv

def get_openai_api_key():
    # Load API key to env variable
    _ = load_dotenv(
        find_dotenv("./llm.env")
    )
