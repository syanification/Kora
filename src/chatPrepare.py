import json

# Input file in prompt-completion format
input_file = "../data/trainingData_prepared.jsonl"
output_file = "../data/trainingData_chat_prepared.jsonl"

# Convert to chat format
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        example = json.loads(line.strip())
        chat_format = {
            "messages": [
                {"role": "user", "content": example["prompt"]},
                {"role": "assistant", "content": example["completion"].strip()}
            ]
        }
        outfile.write(json.dumps(chat_format) + "\n")

print(f"Chat-formatted data saved to {output_file}")