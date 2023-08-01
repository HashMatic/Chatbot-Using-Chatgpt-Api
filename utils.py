import openai

def get_initial_message():
    messages = [
        {"role": "system", "content": "You are a helpful AI Tutor. Who answers brief questions about AI."},
        {"role": "user", "content": "I want to learn AI"},
        {"role": "assistant", "content": "That's awesome, what do you want to know about AI"}
    ]
    return messages

def get_chatgpt_response(messages):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=messages,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None,
        top_p=1.0
    )
    return response.choices[0].text.strip()

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages