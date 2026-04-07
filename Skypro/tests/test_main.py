from src.processing import filter_by_state, sort_by_date
transactions = [
    {"id": 1, "state": "EXECUTED", "date": "2026-03-10T12:00:00"},
    {"id": 2, "state": "PENDING", "date": "2026-03-11T08:30:00"},
    {"id": 3, "state": "EXECUTED", "date": "2026-03-09T18:45:00"},
]

executed = filter_by_state(transactions)
sorted_executed = sort_by_date(executed)

print(sorted_executed)