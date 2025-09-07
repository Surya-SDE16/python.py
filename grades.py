from typing import List

def average_score(scores: List[int]) -> float:
    """
    Calculate the average of a list of scores.
    """
    return sum(scores) / len(scores)


def pass_fail(score: int) -> str:
    """
    Determine if a single score is pass or fail.
    Pass is 60 or above, fail otherwise.
    """
    if score >= 60:
        return "pass"
    else:
        return "fail"


def analyze_scores(scores: List[int]) -> None:
    """
    Print each score with its pass/fail status.
    """
    for score in scores:
        print(f"Score {score} → {pass_fail(score)}")


# Main Guard Code
if __name__ == "__main__":
    scores = [95, 82, 67, 54, 100, 73]

    print("All scores:", scores)
    print("Class average:", average_score(scores))

    print()    

    analyze_scores(scores)
