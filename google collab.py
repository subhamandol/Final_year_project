
#Cell 2 code
def Llama_Chat(system_role, user_msg):
    prompt = f"{system_role}\nUser: {user_msg}\nAI:"
    outputs = pipeline(
        prompt,
        max_new_tokens=180,
        num_return_sequences=1,
        return_full_text=False
    )
    # Extract the generated response text
    reply = outputs[0]["generated_text"]
    return reply.strip()

system_role = "provide only final answer and strictly within 120 words, not more than 120 words"
user_msg = input("Enter your question: ")

num_responses = 10
dataset = []

for i in range(num_responses):
    response = Llama_Chat(system_role, user_msg)
    output_data = {
        "instruction": system_role,
        "input": user_msg,
        "output": response
    }
    dataset.append(output_data)
    print(output_data)
    print(f"Generated response {i+1}/{num_responses}")

# Step 7: Save all responses to a JSON file
with open("dataset.json", "w") as outfile:
    json.dump(dataset, outfile, indent=4)

print("All responses saved to output_dataset.json")