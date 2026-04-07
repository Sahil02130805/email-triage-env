TASKS = [
    {
        "name": "easy",
        "input": {
            "email_id": "1",
            "subject": "Wrong charge",
            "body": "I was charged twice",
            "customer_tier": "standard",
            "history": None
        },
        "expected": {
            "category": "billing",
            "priority": "medium"
        }
    },
    {
        "name": "medium",
        "input": {
            "email_id": "2",
            "subject": "App crash",
            "body": "App crashes when uploading",
            "customer_tier": "premium",
            "history": "previous issue"
        },
        "expected": {
            "category": "technical",
            "priority": "high"
        }
    },
    {
        "name": "hard",
        "input": {
            "email_id": "3",
            "subject": "Refund now",
            "body": "Give refund or I complain",
            "customer_tier": "enterprise",
            "history": "multiple complaints"
        },
        "expected": {
            "category": "refund",
            "priority": "high",
            "escalate": True
        }
    }
]