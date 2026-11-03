
import time

from main1 import (
    OPD_QUEUES,
    add_to_opd_queue,
    start_consultation,
    calculate_actual_waiting_time
)

OPD_QUEUES.clear()

department = "Cardiology"

# Register patient
result = add_to_opd_queue(department, "ROUTINE")
ticket_id = result["ticket"]["ticket_id"]

# Simulate waiting for 3 seconds
time.sleep(3)

# Start consultation
start_result = start_consultation(
    department, ticket_id
)

print("START RESULT:", start_result)

# Calculate actual waiting time
wait_result = calculate_actual_waiting_time(
    department, ticket_id
)

print("\nACTUAL WAITING TIME:")
print(wait_result)
