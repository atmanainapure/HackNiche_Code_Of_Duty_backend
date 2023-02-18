
import requests
import json

# This is the prompt that will be used to query OpenAI's API
prompt = "Output 5 questions in the web development domain to test if a person is knowledgeable in web development domain or not. Keep the questions technical. The question difficulty level should be 2 easy 2 medium and 1 hard. Label the easy, medium and hard questions accordingly."

# This is the OpenAI API endpoint
url = "https://api.openai.com/v1/engines/davinci/completions"

# This is the header for the request
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
}

# This is the data that will be sent in the request
data = {
    "prompt": prompt,
    "max_tokens": 863,
    "temperature": 0.7,
    "top_p": 0.9
}

# This is the request that will be sent to the OpenAI API
response = requests.post(url, headers=headers, data=json.dumps(data))

# This is the response from the OpenAI API
response_data = response.json()

print(response_data)
print("=========================================")
# This is the completion that is returned
completion = response_data['choices'][0]['text']

# Finally, print the completion
print(completion)





