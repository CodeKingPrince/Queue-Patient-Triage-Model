# ============================================================
# KGMU AI TRIAGE PROTOTYPE
# Step 2.3
#
# Purpose:
# - Collect patient symptoms
# - Normalize common symptom expressions
# - Detect basic severity language
# - Assign triage priority
# - Route to a KGMU department
# - Generate a safe prototype message
#
# IMPORTANT:
# This is a hackathon prototype.
# It is NOT a medical diagnosis system.
# ============================================================


# ============================================================
# 1. PATIENT INFORMATION
# ============================================================

def collect_patient():

    print("\n--- Patient Information ---")

    age = input("Enter patient age: ")
    symptoms = input("Enter symptoms: ")

    patient = {
        "age": age,
        "symptoms": symptoms
    }

    return patient


# ============================================================
# 2. NORMALIZE PATIENT LANGUAGE
# ============================================================

def normalize_symptoms(symptoms):

    symptoms = symptoms.lower().strip()

    symptom_aliases = {

        # Breathing
        "breathing difficulty": "difficulty breathing",
        "trouble breathing": "difficulty breathing",
        "shortness of breath": "difficulty breathing",
        "breathlessness": "difficulty breathing",

        # Pain
        "stomach ache": "stomach pain",
        "tummy pain": "stomach pain",
        "head pain": "headache",

        # Urinary
        "urine problem": "urination problem",
        "problem with urination": "urination problem",

        # Vision
        "blur vision": "blurred vision",
        "blurry vision": "blurred vision",

        # Ear / throat
        "earache": "ear pain",
        "throat pain": "sore throat"
    }

    for phrase, standard in symptom_aliases.items():

        symptoms = symptoms.replace(
            phrase,
            standard
        )

    return symptoms


# ============================================================
# 3. DETECT BASIC SEVERITY LANGUAGE
# ============================================================

def detect_severity(symptoms):

    symptoms = symptoms.lower()

    if "severe" in symptoms or "extreme" in symptoms:
        return "SEVERE"

    elif "very high" in symptoms:
        return "VERY HIGH"

    elif "high" in symptoms:
        return "HIGH"

    elif "moderate" in symptoms:
        return "MODERATE"

    elif "mild" in symptoms or "slight" in symptoms:
        return "MILD"

    else:
        return "UNKNOWN"


def extract_context(patient):

    symptoms_text = normalize_symptoms(patient["symptoms"]).lower()

    severity = detect_severity(symptoms_text)

    context = {
        "severity": severity,
        "duration": "UNKNOWN",
        "age": patient["age"],
        "associated_symptoms": []
    }

    # Duration detection
    duration_keywords = [
        "today",
        "yesterday",
        "2 days",
        "3 days",
        "4 days",
        "5 days",
        "one week",
        "1 week",
        "two weeks",
        "2 weeks"
    ]

    for duration in duration_keywords:
        if duration in symptoms_text:
            context["duration"] = duration
            break

    # Associated symptoms
    possible_associated_symptoms = [
        "chest pain",
        "difficulty breathing",
        "vomiting",
        "diarrhea",
        "headache",
        "weakness",
        "dizziness",
        "cough",
        "abdominal pain"
    ]

    for symptom in possible_associated_symptoms:
        if symptom in symptoms_text:
            context["associated_symptoms"].append(symptom)

    return context
# ============================================================
# 4. TRIAGE ENGINE
# ============================================================

# def triage_patient(patient):

#     symptoms = normalize_symptoms(
#         patient["symptoms"]
#     )

#     severity = detect_severity(symptoms)

#     # --------------------------------------------------------
#     # EMERGENCY RULES
#     # These rules have the highest priority.
#     # --------------------------------------------------------

#     emergency_keywords = [

#         "chest pain",
#         "difficulty breathing",
#         "severe bleeding",
#         "loss of consciousness",
#         "major trauma",
#         "major injury"
#     ]

#     for keyword in emergency_keywords:

#         if keyword in symptoms:
#             return "EMERGENCY"


#     # --------------------------------------------------------
#     # URGENT RULES
#     # --------------------------------------------------------

#     urgent_keywords = [

#         "high fever",
#         "very high fever",
#         "persistent vomiting",
#         "severe abdominal pain"
#     ]

#     for keyword in urgent_keywords:

#         if keyword in symptoms:
#             return "URGENT"


    # # --------------------------------------------------------
    # # ROUTINE
    # # --------------------------------------------------------

    # return "ROUTINE"
def triage_patient(patient):

    # Normalize input
    normalized_symptoms = normalize_symptoms(
        patient["symptoms"]
    )

    # Extract symptoms
    symptoms = extract_symptoms(
        normalized_symptoms
    )

    # Extract context
    context = extract_context(
        patient
    )

    # Detect emergency red flags
    red_flags = detect_red_flags(
        symptoms
    )

    # Make final triage decision
    priority = make_triage_decision(
        symptoms,
        context,
        red_flags
    )

    return {
        "symptoms": symptoms,
        "context": context,
        "red_flags": red_flags,
        "priority": priority
    }

# ============================================================
# 5. KGMU DEPARTMENT ROUTER
# ============================================================

def route_department(patient):

    symptoms = normalize_symptoms(
        patient["symptoms"]
    )


    # --------------------------------------------------------
    # KGMU CLINICAL DEPARTMENT RULES
    # --------------------------------------------------------

    department_rules = {

        "Emergency Medicine": [

            "difficulty breathing",
            "chest pain",
            "severe bleeding",
            "loss of consciousness",
            "major trauma",
            "major injury"
        ],


        "Cardiology": [

            "chest pain",
            "palpitations",
            "heart problem",
            "heart pain"
        ],


        "Dermatology, Venereology & Leprosy": [

            "skin rash",
            "itching",
            "skin infection",
            "skin problem"
        ],


        "Ophthalmology": [

            "eye pain",
            "eye problem",
            "vision problem",
            "blurred vision"
        ],


        "Otorhinolaryngology & Head Neck Surgery": [

            "ear pain",
            "hearing problem",
            "sore throat",
            "throat problem",
            "nose problem"
        ],


        "Neurology": [

            "headache",
            "seizure",
            "numbness",
            "weakness"
        ],


        "Neuro Surgery": [

            "head injury",
            "brain injury"
        ],


        "Medical Gastroenterology": [

            "stomach pain",
            "abdominal pain",
            "vomiting",
            "diarrhea",
            "digestive problem"
        ],


        "Urology": [

            "urination problem",
            "blood in urine",
            "urinary problem"
        ],


        "Nephrology": [

            "kidney problem",
            "kidney pain",
            "dialysis"
        ],


        "Obstetrics & Gynecology": [

            "pregnancy",
            "pregnant",
            "period problem",
            "menstrual problem"
        ],


        "Pediatrics": [

            "child",
            "baby",
            "infant"
        ],


        "Psychiatry": [

            "depression",
            "anxiety",
            "panic attack",
            "mental health"
        ],


        "Geriatric Mental Health": [

            "elderly mental health",
            "old age mental health"
        ],


        "Respiratory Medicine": [

            "cough",
            "asthma",
            "breathing problem",
            "respiratory problem"
        ],


        "Pulmonary & Critical Care Medicine": [

            "severe respiratory problem",
            "critical breathing problem"
        ],


        "Orthopedic Surgery": [

            "bone pain",
            "fracture",
            "joint pain",
            "back pain"
        ],


        "Paediatric Orthopaedics": [

            "child bone problem",
            "child fracture",
            "child joint problem"
        ],


        "Trauma Surgery": [

            "accident",
            "major injury",
            "trauma"
        ],


        "General Surgery": [

            "surgical problem",
            "lump",
            "hernia"
        ],


        "Surgical Gastroenterology": [

            "gastro surgery problem",
            "surgical stomach problem"
        ],


        "Endocrine Surgery": [

            "thyroid lump",
            "thyroid swelling"
        ],


        "Plastic & Reconstructive Surgery": [

            "reconstructive surgery",
            "burn injury"
        ],


        "Medicine": [

            "fever",
            "weakness",
            "body pain",
            "general illness"
        ]
    }


    # --------------------------------------------------------
    # MATCH SYMPTOMS TO DEPARTMENT
    # --------------------------------------------------------

    for department, keywords in department_rules.items():

        for keyword in keywords:

            if keyword in symptoms:

                return department


    # --------------------------------------------------------
    # DEFAULT
    # --------------------------------------------------------

    return "Medicine"


# ============================================================
# 6. GENERATE PATIENT MESSAGE
# ============================================================

def generate_message(priority):

    if priority == "EMERGENCY":

        return (
            "High-priority symptoms detected. "
            "Immediate clinical assessment is recommended."
        )


    elif priority == "URGENT":

        return (
            "Your symptoms have been classified as urgent "
            "for this prototype. Prompt clinical assessment "
            "is recommended."
        )


    else:

        return (
            "Your symptoms have been classified as routine "
            "for this prototype. Please follow the appropriate "
            "hospital process."
        )


# ============================================================
# 7. DISPLAY RESULT
# ============================================================

def display_result(result):

    print("\n==============================")
    print("       TRIAGE RESULT")
    print("==============================")

    print("Symptoms   :", result["symptoms"])
    print("Severity   :", result["severity"])
    print("Priority   :", result["priority"])
    print("Department :", result["department"])

    print("\nMessage:")
    print(result["message"])

    print("==============================")

    print("Prototype decision only.")
    print("Clinical assessment is required.")


# ============================================================
# 8. MAIN PROGRAM
# ============================================================

def main():

    # --------------------------------------------------------
    # 1. COLLECT PATIENT INFORMATION
    # --------------------------------------------------------

    patient = collect_patient()


    # --------------------------------------------------------
    # 2. RUN TRIAGE ENGINE
    # --------------------------------------------------------

    triage_result = triage_patient(
        patient
    )


    # --------------------------------------------------------
    # 3. GET TRIAGE INFORMATION
    # --------------------------------------------------------

    priority = triage_result["priority"]

    context = triage_result["context"]

    red_flags = triage_result["red_flags"]

    symptoms = triage_result["symptoms"]


    # --------------------------------------------------------
    # 4. ROUTE TO DEPARTMENT
    # --------------------------------------------------------

    department = route_department(
        patient
    )


    # --------------------------------------------------------
    # 5. GENERATE PATIENT MESSAGE
    # --------------------------------------------------------

    message = generate_message(
        priority
    )


    # --------------------------------------------------------
    # 6. CREATE FINAL RESULT
    # --------------------------------------------------------

    result = {

        "symptoms": symptoms,

        "severity": context["severity"],

        "priority": priority,

        "department": department,

        "red_flags": red_flags,

        "message": message
    }


    # --------------------------------------------------------
    # 7. DISPLAY RESULT
    # --------------------------------------------------------

    display_result(
        result
    )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()


# ============================================================
# 9. PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()
    # /
    # python .
    # \Phase1\main1.py
    # python .\Phase1\main1.py