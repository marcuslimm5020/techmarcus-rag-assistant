
from src.rag_pipeline import ask_question


TEST_CASES = [
    {
        "question": "What should I do if my product is faulty?",
        "expected_keywords": ["support", "product"],
        "should_answer": True,
    },
    {
        "question": "How long do approved refunds normally take?",
        "expected_keywords": ["5", "10", "business days"],
        "should_answer": True,
    },
    {
        "question": "What should I do if my laptop overheats?",
        "expected_keywords": ["overheat", "support"],
        "should_answer": True,
    },
    {
        "question": "Does TechMarcus sell pet food?",
        "expected_keywords": [],
        "should_answer": False,
    },
]


def run_evaluation():
    passed = 0

    for index, test in enumerate(TEST_CASES, start=1):
        print("\n" + "=" * 60)
        print(f"TEST {index}: {test['question']}")

        result = ask_question(test["question"])
        answer = result["answer"]
        answer_lower = answer.lower()

        print(f"\nAnswer: {answer}")

        if test["should_answer"]:
            keyword_matches = [
                keyword
                for keyword in test["expected_keywords"]
                if keyword.lower() in answer_lower
            ]

            passed_test = len(keyword_matches) >= 2

            print(f"Expected keywords: {test['expected_keywords']}")
            print(f"Matched keywords: {keyword_matches}")
        else:
            refusal_phrases = [
                "couldn't find",
                "could not find",
                "don't have",
                "do not have",
                "not mentioned",
                "not available",
                "knowledge base",
            ]

            passed_test = any(
                phrase in answer_lower
                for phrase in refusal_phrases
            )

            print("Expected: Assistant acknowledges missing information")

        print(f"Result: {'PASS' if passed_test else 'FAIL'}")

        if passed_test:
            passed += 1

    total = len(TEST_CASES)
    print("\n" + "=" * 60)
    print(f"Evaluation: {passed}/{total} tests passed")
    print(f"Pass rate: {passed / total:.0%}")


if __name__ == "__main__":
    run_evaluation()
