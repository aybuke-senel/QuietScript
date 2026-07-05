import ollama


def ask_agent(system_prompt, user_input):
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
    )

    return response["message"]["content"]