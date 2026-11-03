from main1 import (
    OPD_QUEUES,
    add_to_opd_queue,
    estimate_wait_time
)

# Start with empty queues
OPD_QUEUES.clear()

# Patient 1: ROUTINE
routine_1 = add_to_opd_queue(
    "Dermatology",
    "ROUTINE"
)

# Patient 2: URGENT
urgent_1 = add_to_opd_queue(
    "Dermatology",
    "URGENT"
)

# Patient 3: ROUTINE
routine_2 = add_to_opd_queue(
    "Dermatology",
    "ROUTINE"
)

# Estimate the wait for the last routine patient
result = estimate_wait_time(
    "Dermatology",
    routine_2["ticket"]["ticket_id"]
)

print("\nWAIT-TIME TEST")
print("=" * 40)
print("Available:", result["available"])

if result["available"]:
    print("Department:", result["department"])
    print("Queue position:", result["queue_position"])
    print("Patients ahead:", result["patients_ahead"])
    print(
        "Estimated waiting time:",
        result["estimated_wait_minutes"],
        "minutes"
    )
    print("Estimate type:", result["estimate_type"])
else:
    print("Reason:", result["reason"])