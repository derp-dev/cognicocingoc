import openai
"""
The OPENAI_API_BASE environment variable is used in the OpenAI Python library to specify the base URL for making API requests. By default, the OpenAI Python library uses the official OpenAI API endpoint, so you usually don't need to set the OPENAI_API_BASE variable
If you are working with a custom deployment or a different API endpoint, you can set the OPENAI_API_BASE environment variable to specify the base URL for API requests.
"""
# Set the custom API base URL
openai.api_base = "https://custom-api.example.com/v1"

# Now make API requests as usual
response = openai.Completion.create(...)

"""
```import openai

# Set the custom API base URL
openai.api_base = "https://custom-api.example.com/v1"

# Now make API requests as usual
response = openai.Completion.create(...)
```
once i have run this, I can use the rest of the openai lib and it will inference "https://custom-api.example.com/v1" for all the methods of the lib?
"""