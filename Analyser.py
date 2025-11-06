import os
import asyncio
import pandas as pd
from dotenv import load_dotenv
from groq import Groq

#  ENV SETUP 
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

#  ROLES + TASK 
ROLES = [
    "Data Scientist",
    "ML Auditor",
    "Tech Reporter"
]

# All roles will answer the same queries
QUERIES = [
    "Explain how overfitting affects a machine learning model.",
    "Describe how to evaluate a classification model effectively.",
    "Summarize the importance of data ethics in AI systems."
]

#  ROLE PROMPT TEMPLATE 
PROMPT_TEMPLATE = """
You are a {role}. Respond to the following question in your professional tone.

Question: {query}

Guidelines:
- Use your role’s expertise, vocabulary, and perspective.
- Keep the response under 120 words.
"""

#  RUN ROLE-BASED TESTS 
async def run_role_tests():
    results = []

    for query in QUERIES:
        print(f"\n=== Running Query: {query} ===")
        for role in ROLES:
            full_prompt = PROMPT_TEMPLATE.format(role=role, query=query)

            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": full_prompt}],
                temperature=0.7,
            )

            response = completion.choices[0].message.content.strip()
            print(f"\n[{role}] Response:\n{response}\n")

            results.append({
                "Query": query,
                "Role": role,
                "Response": response
            })

    # Save results
    df = pd.DataFrame(results)
    df.to_csv("role_based_prompts_results.csv", index=False)
    print("\nResults saved to role_based_prompts_results.csv")

    # Generate comparison summary
    summary = []
    for query in QUERIES:
        subset = df[df["Query"] == query]
        summary.append({
            "Query": query,
            "Observation": "Compare tone, depth, and critique differences among roles."
        })

    summary_df = pd.DataFrame(summary)
    summary_df.to_csv("role_based_summary.csv", index=False)
    print("Summary file saved to role_based_summary.csv")


#  ENTRY POINT 
if __name__ == "__main__":
    asyncio.run(run_role_tests())
