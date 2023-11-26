from app.core.config import configs
import replicate

async def summarize(temperature, kind):
    response = ""
    prompt = f"Formulate a comical weather synopsis for {kind} temperature {temperature} farhenheit."
    api = replicate.Client(api_token=configs.REPLICATE_API_TOKEN)
    cursor = api.run(
    "meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d",
    input={
        "debug": False,
        "top_k": 50,
        "top_p": 1,
        "prompt": prompt,
        "temperature": 0.75,
        "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
        "max_new_tokens": 500,
        "min_new_tokens": -1
    }
    )

    for output in cursor:
        response += output
    
    return response
