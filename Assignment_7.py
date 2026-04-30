from typing import List, Dict, Set
from functools import reduce
from pprint import pprint
import time
import sys

# ---------- FUNCTIONS ----------

def total_time_per_user(logs: List[Dict]) -> Dict[str, float]:
    return reduce(
        lambda acc, log: (
            acc.update({log["user"]: acc.get(log["user"], 0) + log["duration"]}) or acc
        ),
        logs,
        {}
    )


def most_active_users(logs: List[Dict], k: int) -> List[str]:
    totals = total_time_per_user(logs)

    return [
        user for user, _ in
        sorted(totals.items(), key=lambda x: x[1], reverse=True)[:k]
    ]


def unique_actions(logs: List[Dict]) -> Set[str]:
    return {log["action"] for log in logs}


# ---------- MAIN ----------

if __name__ == "__main__":

    logs: List[Dict] = [
        {"user": "CSB24030", "action": "YouTube", "duration": 2.5},
        {"user": "CSB24031", "action": "Instagram", "duration": 1.0},
        {"user": "CSB24030", "action": "WhatsApp", "duration": 0.5},
        {"user": "CSB24032", "action": "YouTube", "duration": 3.0},
        {"user": "CSB24031", "action": "Netflix", "duration": 2.0},
        {"user": "CSB24030", "action": "Chrome", "duration": 1.5},
    ]

    # ---- Large Data ----
    for i in range(100000):
        logs.append({
            "user": f"CSB24{str(30 + (i % 50)).zfill(3)}",
            "action": f"App{i % 10}",
            "duration": float(i % 5 + 1)
        })

    # ---------- TOTAL TIME ----------
    start_total = time.perf_counter()
    totals = total_time_per_user(logs)
    end_total = time.perf_counter()

    print("\n=== Total Time Per User (Sorted) ===")
    pprint(dict(sorted(totals.items())))

    print(f"\nExecution Time (total_time_per_user): {end_total - start_total:.6f} sec")


    # ---------- TOP K USERS ----------
    k = 5
    start_topk = time.perf_counter()
    top_users = most_active_users(logs, k)
    end_topk = time.perf_counter()

    print(f"\n=== Top {k} Active Users ===")
    print(top_users)

    print(f"Execution Time (most_active_users): {end_topk - start_topk:.6f} sec")


    # ---------- UNIQUE ACTIONS ----------
    start_set = time.perf_counter()
    actions = unique_actions(logs)
    end_set = time.perf_counter()

    print("\n=== Unique Actions (Sorted) ===")
    print(sorted(actions))

    print(f"Execution Time (unique_actions): {end_set - start_set:.6f} sec")


    # ---------- COMPLEXITY ----------
    n = len(logs)
    unique_users = len(totals)

    print("\n=== Complexity Analysis ===")
    print(f"Time Complexity (Top K Users): O(N log N), N = {n}")
    print("Reason: Sorting dominates")

    print(f"\nSpace Complexity: O(U), U = {unique_users} unique users")

    memory_usage = sys.getsizeof(logs) + sys.getsizeof(totals) + sys.getsizeof(actions)
    print(f"\nApprox Memory Used: {memory_usage} bytes")