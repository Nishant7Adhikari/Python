import random

def weighted_random_selector(candidates):
    """
    candidates = {
        "Alice": 8,
        "Bob": 3,
        "Charlie": 6,
        "David": 1,
        "Eve": 9
    }
    """
    names = list(candidates.keys())
    weights = list(candidates.values())

    selected = random.choices(names, weights=weights, k=1)[0]
    return selected


# ---- INPUT SECTION ----
candidates = {}

n = int(input("Number of candidates: "))

for _ in range(n):
    name = input("Candidate name: ")
    score = float(input("Score (0–10): "))
    candidates[name] = score

# ---- RESULT ----
print("\nSelected candidate:", weighted_random_selector(candidates))