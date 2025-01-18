from openai import OpenAI
client = OpenAI()

# Retrieve the state of a fine-tune
client.fine_tuning.jobs.retrieve("ftjob-6kCnO9AItVkv40C0Rs1JZsvR")