# from main1 import (
#     OPD_QUEUES,
#     add_to_opd_queue,
#     start_consultation
# )

# # Reset queues
# OPD_QUEUES.clear()

# department = "Cardiology"

# # Register three patients
# patient_a = add_to_opd_queue(
#     department, "ROUTINE"
# )

# patient_b = add_to_opd_queue(
#     department, "URGENT"
# )

# patient_c = add_to_opd_queue(
#     department, "ROUTINE"
# )

# # Get ticket IDs
# ticket_a = patient_a["ticket"]["ticket_id"]
# ticket_b = patient_b["ticket"]["ticket_id"]
# ticket_c = patient_c["ticket"]["ticket_id"]

# print("\nCONSULTATION TEST")
# print("=" * 45)

# # Try starting the routine patient first
# result_a = start_consultation(
#     department, ticket_a
# )

# print("\nRoutine patient first attempt:")
# print(result_a)

# # Start urgent patient
# result_b = start_consultation(
#     department, ticket_b
# )

# print("\nUrgent patient:")
# print(result_b)

# # Start first routine patient
# result_a = start_consultation(
#     department, ticket_a
# )

# print("\nRoutine patient second attempt:")
# print(result_a)

# # Try starting third patient when both stations are occupied
# result_c = start_consultation(
#     department, ticket_c
# )

# print("\nThird patient:")
# print(result_c)

from main1 import (
    add_to_opd_queue,
    start_consultation,
    complete_consultation
)

department = "Cardiology"

# Add a patient
result = add_to_opd_queue(department, "ROUTINE")
ticket_id = result["ticket"]["ticket_id"]

# Start consultation
start_result = start_consultation(department, ticket_id)
print("START RESULT:", start_result)

# Complete consultation
complete_result = complete_consultation(department, ticket_id)
print("COMPLETE RESULT:", complete_result)
# Try starting another patient after completion
next_patient = add_to_opd_queue(
    department, "ROUTINE"
)

next_ticket = next_patient["ticket"]["ticket_id"]

next_result = start_consultation(
    department, next_ticket
)

print("\nNext patient after completion:")
print(next_result)