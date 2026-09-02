"""
query.py

This is the script that executes a user query.
Run a single question through the full RAG + LangGraph pipeline and print the result
, including the attempt log (useful for seeing the retrieve -> grade -> reformulate loop in action).

Usage:
    python src/query.py "Why would you use difference-in-differences instead of a simple before/after comparison?"
"""

import sys
from graph import run
from dotenv import load_dotenv

load_dotenv()  # read in environment variables

def main():

    # checking if a question was passed as an argument when calling the script
    if len(sys.argv) < 2:
        print('No question detected. Use script in the following way: ')
        print('python src/query.py "your question here"')
        sys.exit(1)

    question = sys.argv[1]
    print(f"Question: {question}\n")
    print("Running question through RAG pipeline...\n")

    result = run(question)

    # printing the attempt log, including the questions being posed.
    print("=" * 30)
    print("ATTEMPT LOG")
    print("=" * 30)

    for entry in result["attempt_log"]:
        print(f"  Attempt {entry['attempt']}: grade={entry['grade']}")
        print(f"    Question used: {entry['question']}")

    # printing details of final attempt, including preview of the chunks used, as well as the response
    print("\n" + "=" * 30)
    print("RETRIEVED CHUNKS (final attempt)")
    print("=" * 30)

    for i, chunk in enumerate(result["chunks"], 1):
        preview = chunk[:200].replace("\n", " ")
        print(f"  [{i}] {preview}...")

    print("\n" + "=" * 30)
    print("ANSWER")
    print("=" * 30)
    print(result["response"])

if __name__ == "__main__":
    main()