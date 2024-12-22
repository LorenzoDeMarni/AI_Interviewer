from openai import AsyncOpenAI
import asyncio

async def test_api_key():
    client = AsyncOpenAI(api_key="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")  # Replace with your key
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Say hello"},
                {"role": "user", "content": "Hello!"},
            ]
        )
        print("API Key is valid. Response:", response)
    except Exception as e:
        print("Error with API Key:", str(e))

asyncio.run(test_api_key())
