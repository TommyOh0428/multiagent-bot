# import openai

# class DevOpsAgent:

#     @staticmethod
#     def get_devops_response(input_text: str):
#         devops_response = openai.Completion.create(
#             model="gpt-4o",
#             prompt=input_text,
#             max_tokens=150,
#         )
#         return devops_response.choices[0].text.strip()