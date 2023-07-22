import openai
import config
openai.api_key = config.api_key

def analyze_text(text):
    #default bot prompt
    prompt = 'Detect the political bias in the given text and provide a brief summary(<50 words). Rate the magnitude of bias on a scale of 0-10, where 0 is unbiased, and 10 is extremely biased. A neutral/centrist input should receive a score between 0 and 3. Here is the text to analyze: ' + text + 'Respond in the following format: Political Direction (Left/Right/Neutral): , Magnitude of Bias: (integer from 1-10) , Summary: (recap of article).  Political Direction:'
    
    #use fine-tuned gpt-3 model, temp = 0 for stable results
    response = openai.Completion.create(
        #engine="text-davinci-003",
        model = "davinci:ft-personal-2023-07-19-01-36-09",
        prompt=prompt,
        max_tokens=100,
        temperature=0,
        n=1,
        stop=None,
    )
    
    #retrieve response, return
    generated_text = 'Political Direction: ' + response.choices[0].text.strip()
    
    return generated_text