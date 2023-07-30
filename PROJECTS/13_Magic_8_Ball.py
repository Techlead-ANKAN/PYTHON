#  Magic 8 Ball

import wolframalpha

app_id = "LYJ39T-78KE2TJ9WX"
the_client = wolframalpha.Client(app_id)
question = input("Ask Magic 8 Ball:  ")
print("\n")
print("----------Magic 8 Ball is thinking!!!----------\n")
response = the_client.query(question)
answer = next(response.results).text
print(f"Magic 8 Ball says: {answer}.")