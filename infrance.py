from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch



model_dir = "model\Model_V1.5"
tokenizer_dir ="model\Tokonizer_V1.5" 

def translation(inputs):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
    
    
    tokenized_input = tokenizer.encode_plus(inputs, max_length = 10, truncation = True, padding= True, return_tensors= "pt")
    inputs_ids = tokenized_input["input_ids"]
    attention_mask = tokenized_input["attention_mask"]
    output = model.generate(inputs_ids, attention_mask=attention_mask)
    return tokenizer.decode(output[0], skip_special_tokens=True)


if "__main__":
    print(translation("ياواد اشبك"))