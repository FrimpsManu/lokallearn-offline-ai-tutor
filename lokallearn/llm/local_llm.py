from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


def load_llm_model():
    model_name = "microsoft/phi-2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

def get_llm_response(pipeline, prompt):
    result = pipeline(prompt, max_new_tokens=60)[0]["generated_text"]
    return result
