# ============================================================
# KGMU AI TRIAGE PROTOTYPE
# ============================================================
# Flow:
#
# Patient Input
#       ↓
# Normalize Symptoms
#       ↓
# Extract Context
#       ↓
# Detect Red Flags
#       ↓
# Triage Decision
#       ↓
# EMERGENCY / URGENT / ROUTINE
#       ↓
# Department Routing
#       ↓
# Patient Message
#       ↓
# Final Result
# ============================================================


# ============================================================
# 1. COLLECT PATIENT INFORMATION
# ============================================================

def collect_patient():

    print("\n--- Patient Information ---")

    # --------------------------------------------------------
    # AGE
    # --------------------------------------------------------

    age = input("Enter patient age: ").strip()

    # --------------------------------------------------------
    # SYMPTOMS
    # --------------------------------------------------------

    symptoms = input(
        "Enter your main symptoms: "
    ).strip()

    # --------------------------------------------------------
    # SEVERITY
    # --------------------------------------------------------

    print("\nHow severe are your symptoms?")

    print("1. Mild")
    print("2. Moderate")
    print("3. Severe")

    severity_choice = input(
        "Enter option (1-3): "
    ).strip()

    severity_options = {
        "1": "MILD",
        "2": "MODERATE",
        "3": "SEVERE"
    }

    severity = severity_options.get(
        severity_choice,
        "UNKNOWN"
    )

    # --------------------------------------------------------
    # DURATION
    # --------------------------------------------------------

    print("\nHow long have you had these symptoms?")

    print("1. Less than 24 hours")
    print("2. 1-3 days")
    print("3. 4-7 days")
    print("4. More than 1 week")

    duration_choice = input(
        "Enter option (1-4): "
    ).strip()

    duration_options = {
        "1": "LESS_THAN_24_HOURS",
        "2": "1_TO_3_DAYS",
        "3": "4_TO_7_DAYS",
        "4": "MORE_THAN_1_WEEK"
    }

    duration = duration_options.get(
        duration_choice,
        "UNKNOWN"
    )

    # --------------------------------------------------------
    # FINAL PATIENT OBJECT
    # --------------------------------------------------------

    patient = {

        "age": age,

        "symptoms": symptoms,

        "severity": severity,

        "duration": duration
    }

    return patient

# ============================================================
# 2. NORMALIZE PATIENT LANGUAGE
# ============================================================

def normalize_symptoms(symptoms):

    symptoms = symptoms.lower().strip()

    symptom_aliases = {

        # ----------------------------------------------------
        # Breathing
        # ----------------------------------------------------

        "breathing difficulty": "difficulty breathing",
        "trouble breathing": "difficulty breathing",
        "shortness of breath": "difficulty breathing",
        "breathlessness": "difficulty breathing",
        "breathing problem": "difficulty breathing",

        # ----------------------------------------------------
        # Pain
        # ----------------------------------------------------

        "stomach ache": "stomach pain",
        "tummy pain": "stomach pain",
        "head pain": "headache",
        "belly pain": "abdominal pain",

        # ----------------------------------------------------
        # Urinary
        # ----------------------------------------------------

        "urine problem": "urination problem",
        "problem with urination": "urination problem",
        "urinary problem": "urination problem",

        # ----------------------------------------------------
        # Vision
        # ----------------------------------------------------

        "blur vision": "blurred vision",
        "blurry vision": "blurred vision",

        # ----------------------------------------------------
        # Ear / Throat
        # ----------------------------------------------------

        "earache": "ear pain",
        "throat pain": "sore throat",

        # ----------------------------------------------------
        # Fever
        # ----------------------------------------------------

        "high temperature": "high fever",

        # ----------------------------------------------------
        # Heart
        # ----------------------------------------------------

        "heart pain": "chest pain",

        # ----------------------------------------------------
        # Injury
        # ----------------------------------------------------

        "head trauma": "head injury",
        "brain trauma": "brain injury"
    }

    for phrase, standard in symptom_aliases.items():

        symptoms = symptoms.replace(
            phrase,
            standard
        )

    return symptoms


# ============================================================
# 3. EXTRACT BASIC SYMPTOMS
# ============================================================

# ============================================================
# 3. EXTRACT IDENTIFIED SYMPTOMS
# ============================================================

def extract_symptoms(symptoms):

    symptoms = symptoms.lower().strip()

    known_symptoms = [

        # General symptom
        "pain",

        # Emergency / safety related
        "difficulty breathing",
        "chest pain",
        "severe bleeding",
        "loss of consciousness",
        "major trauma",
        "major injury",

        # General
        "fever",
        "weakness",
        "body pain",

        # Head / neurological
        "headache",
        "seizure",
        "numbness",
        "dizziness",

        # Respiratory
        "cough",
        "asthma",

        # Gastrointestinal
        "stomach pain",
        "abdominal pain",
        "vomiting",
        "diarrhea",

        # Urinary
        "urination problem",
        "blood in urine",

        # Eye
        "eye pain",
        "eye problem",
        "vision problem",
        "blurred vision",

        # ENT
        "ear pain",
        "hearing problem",
        "sore throat",
        "throat problem",
        "nose problem",

        # Skin
        "skin rash",
        "itching",
        "skin infection",
        "skin problem",

        # Orthopedic / trauma
        "bone pain",
        "fracture",
        "joint pain",
        "back pain",
        "shoulder pain",
        "neck pain",
        "leg pain",
        "arm pain",
        "foot pain",
        "ankle pain",
        "knee pain",
        "elbow pain",
        "wrist pain",
        "hip pain",
        "accident",
        "trauma",

        # Other
        "kidney problem",
        "kidney pain",
        "dialysis",
        "pregnancy",
        "pregnant",
        "period problem",
        "menstrual problem",
        "depression",
        "anxiety",
        "panic attack",
        "mental health",
        "surgical problem",
        "lump",
        "hernia",
        "thyroid lump",
        "thyroid swelling",
        "burn injury",
        "reconstructive surgery"
    ]

    detected_symptoms = []

    for symptom in known_symptoms:

        if symptom in symptoms:
            detected_symptoms.append(
                symptom
            )

    # --------------------------------------------------------
    # Remove generic "pain" when a more specific pain location
    # or pain type has already been identified.
    # --------------------------------------------------------

    if "pain" in detected_symptoms:
        specific_pain_symptoms = [
            item for item in detected_symptoms
            if item != "pain" and "pain" in item
        ]

        if specific_pain_symptoms:
            detected_symptoms = [
                item for item in detected_symptoms
                if item != "pain"
            ]

    # --------------------------------------------------------
    # If nothing was identified
    # --------------------------------------------------------

    if not detected_symptoms:

        detected_symptoms.append(
            "unspecified symptom"
        )

    return detected_symptoms
# ============================================================
# 4. DETECT BASIC SEVERITY
# ============================================================
def detect_severity(patient):

    severity = patient.get(
        "severity",
        "UNKNOWN"
    )

    return severity


# ============================================================
# 5. EXTRACT PATIENT CONTEXT
# ============================================================

# def extract_context(patient):

#     symptoms_text = normalize_symptoms(
#         patient["symptoms"]
#     )

#     severity = detect_severity(
#         symptoms_text
#     )

#     context = {

#         "severity": severity,

#         "duration": "UNKNOWN",

#         "age": patient["age"],

#         "associated_symptoms": []
#     }
def extract_context(patient):

    # --------------------------------------------------------
    # NORMALIZE SYMPTOMS
    # --------------------------------------------------------

    symptoms_text = normalize_symptoms(
        patient["symptoms"]
    )

    # --------------------------------------------------------
    # GET PATIENT-PROVIDED SEVERITY
    # --------------------------------------------------------

    severity = detect_severity(
        patient
    )

    # --------------------------------------------------------
    # GET PATIENT-PROVIDED DURATION
    # --------------------------------------------------------

    duration = patient.get(
        "duration",
        "UNKNOWN"
    )

    # --------------------------------------------------------
    # PATIENT CONTEXT
    # --------------------------------------------------------

    context = {

        "severity": severity,

        "duration": duration,

        "age": patient.get(
            "age",
            "UNKNOWN"
        ),

        "associated_symptoms": []
    }

    # --------------------------------------------------------
    # ASSOCIATED SYMPTOMS
    # --------------------------------------------------------

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

            context["associated_symptoms"].append(
                symptom
            )

    return context

    # --------------------------------------------------------
    # Duration detection
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # Associated symptoms
    # --------------------------------------------------------

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

            context["associated_symptoms"].append(
                symptom
            )

    return context


# ============================================================
# 6. DETECT RED FLAGS
# ============================================================

# ============================================================
# 6. DETECT RED FLAGS
# ============================================================

def detect_red_flags(symptoms):

    symptoms = symptoms.lower().strip()

    red_flag_rules = {

        "difficulty breathing":
            "Difficulty breathing",

        "chest pain":
            "Chest pain",

        "severe bleeding":
            "Severe bleeding",

        "loss of consciousness":
            "Loss of consciousness",

        "major trauma":
            "Major trauma",

        "major injury":
            "Major injury",

        "seizure":
            "Seizure"
    }

    detected_red_flags = []

    for keyword, description in red_flag_rules.items():

        if keyword in symptoms:
            detected_red_flags.append(
                description
            )

    return detected_red_flags


# ============================================================
# 7. TRIAGE DECISION ENGINE
# ============================================================

def make_triage_decision(
    symptoms,
    context,
    red_flags
):

    # ========================================================
    # LEVEL 1 — EMERGENCY
    # ========================================================

    if len(red_flags) > 0:

        return "EMERGENCY"


    # ========================================================
    # LEVEL 2 — URGENT
    # ========================================================

    urgent_keywords = [

        "high fever",
        "very high fever",

        "persistent vomiting",

        "severe abdominal pain",

        "fracture",

        "severe pain",

        "blood in urine",

        "severe headache"
    ]

    for keyword in urgent_keywords:

        if keyword in symptoms:

            return "URGENT"


    # ========================================================
    # LEVEL 3 — ROUTINE
    # ========================================================

    return "ROUTINE"


# ============================================================
# 8. COMPLETE TRIAGE FUNCTION
# ============================================================

# def triage_patient(patient):

#     # --------------------------------------------------------
#     # 1. NORMALIZE PATIENT SYMPTOMS
#     # --------------------------------------------------------

#     normalized_symptoms = normalize_symptoms(
#         patient["symptoms"]
#     )

#     # --------------------------------------------------------
#     # 2. EXTRACT IDENTIFIED SYMPTOMS
#     # --------------------------------------------------------

#     symptoms = extract_symptoms(
#         normalized_symptoms
#     )

#     # --------------------------------------------------------
#     # 3. EXTRACT PATIENT CONTEXT
#     # --------------------------------------------------------

#     context = extract_context(
#         patient
#     )
# ============================================================
# 8. GENERATE FOLLOW-UP QUESTION
# ============================================================

def generate_follow_up_question(
    patient,
    context,
    symptoms,
    red_flags
):

    # 1. SAFETY
    if len(red_flags) > 0:

        return (
            "Your symptoms may require immediate attention. "
            "Are you currently experiencing severe difficulty "
            "breathing, loss of consciousness, severe bleeding, "
            "or another rapidly worsening symptom?"
        )

    # 2. UNSPECIFIED SYMPTOM
    if (
        "unspecified symptom" in symptoms
        or len(symptoms) == 0
    ):

        return (
            "What is your main problem right now? "
            "For example: pain, fever, breathing problem, "
            "vomiting, injury, weakness, or another problem."
        )

    # 3. PAIN WITHOUT CLEAR LOCATION
    if "pain" in symptoms:

        pain_locations = [
            "chest",
            "stomach",
            "abdomen",
            "head",
            "back",
            "joint",
            "bone"
        ]

        symptom_text = patient[
            "symptoms"
        ].lower()

        location_found = False

        for location in pain_locations:

            if location in symptom_text:
                location_found = True
                break

        if not location_found:

            return (
                "Where exactly is the pain located? "
                "For example: chest, stomach/abdomen, "
                "head, back, joint, bone, or another area."
            )

    # 4. UNKNOWN SEVERITY
    if context.get("severity") == "UNKNOWN":

        return (
            "How severe are your symptoms right now? "
            "Please choose Mild, Moderate, or Severe."
        )

    # 5. UNKNOWN DURATION
    if context.get("duration") == "UNKNOWN":

        return (
            "How long have you had these symptoms?"
        )

    # 6. NONE
    return None
# ============================================================
# 9. COLLECT FOLLOW-UP RESPONSE
# ============================================================

def collect_follow_up_response(question):

    print("\n")
    print("=" * 50)
    print("          ADDITIONAL INFORMATION")
    print("=" * 50)

    print(question)

    print("=" * 50)

    answer = input(
        "Your answer: "
    ).strip()

    return answer

def triage_patient(patient):

    # --------------------------------------------------------
    # 1. NORMALIZE PATIENT SYMPTOMS
    # --------------------------------------------------------

    normalized_symptoms = normalize_symptoms(
        patient["symptoms"]
    )

    # --------------------------------------------------------
    # 2. EXTRACT IDENTIFIED SYMPTOMS
    # --------------------------------------------------------

    symptoms = extract_symptoms(
        normalized_symptoms
    )

    # --------------------------------------------------------
    # 3. EXTRACT PATIENT CONTEXT
    # --------------------------------------------------------

    context = extract_context(
        patient
    )

    # --------------------------------------------------------
    # 4. CHECK FOR RED FLAGS
    # --------------------------------------------------------

    red_flags = detect_red_flags(
        normalized_symptoms
    )

    # --------------------------------------------------------
    # 5. MAKE TRIAGE DECISION
    # --------------------------------------------------------

    priority = make_triage_decision(
        normalized_symptoms,
        context,
        red_flags
    )

    # --------------------------------------------------------
    # 6. RETURN COMPLETE TRIAGE RESULT
    # --------------------------------------------------------

    return {

        "symptoms": symptoms,

        "context": context,

        "red_flags": red_flags,

        "priority": priority
    }
def update_patient_from_follow_up(patient, answer):

    answer = answer.lower().strip()

    original_symptoms = patient["symptoms"].lower().strip()

    # Pain location follow-up
    pain_locations = {
        "chest": "chest pain",
        "stomach": "stomach pain",
        "abdomen": "abdominal pain",
        "head": "headache",
        "back": "back pain",
        "joint": "joint pain",
        "bone": "bone pain",
        "shoulder": "shoulder pain",
        "neck": "neck pain",
        "leg": "leg pain",
        "arm": "arm pain",
        "foot": "foot pain",
        "ankle": "ankle pain",
        "knee": "knee pain",
        "elbow": "elbow pain",
        "wrist": "wrist pain",
        "hip": "hip pain"
    }

    # If the original complaint was pain,
    # combine the location with pain.
    if "pain" in original_symptoms:

        if answer in pain_locations:

            patient["symptoms"] = pain_locations[answer]

    return patient



def is_unspecified_pain_location(answer):

    answer = answer.lower().strip()

    unspecified_locations = [
        "another area",
        "other area",
        "somewhere else",
        "other",
        "elsewhere"
    ]

    return answer in unspecified_locations

def make_triage_decision(
    symptoms,
    context,
    red_flags
):

    # --------------------------------------------------------
    # 1. RED FLAG CHECK
    # --------------------------------------------------------

    if len(red_flags) > 0:
        return "EMERGENCY"


    # --------------------------------------------------------
    # 2. CHECK WHETHER SYMPTOM INFORMATION IS TOO VAGUE
    # --------------------------------------------------------

    vague_inputs = [
        "pain",
        "problem",
        "issue",
        "not feeling well",
        "feeling sick",
        "unwell"
    ]

    symptoms_lower = symptoms.lower()

    for vague in vague_inputs:

        if symptoms_lower.strip() == vague:
            return "NEEDS_MORE_INFORMATION"


    # --------------------------------------------------------
    # 3. GET PATIENT-PROVIDED SEVERITY
    # --------------------------------------------------------

    severity = context.get(
        "severity",
        "UNKNOWN"
    )


    # --------------------------------------------------------
    # 4. URGENT SYMPTOMS
    # --------------------------------------------------------

    urgent_keywords = [
        "high fever",
        "very high fever",
        "persistent vomiting",
        "blood in urine",
        "fracture"
    ]

    for keyword in urgent_keywords:

        if keyword in symptoms_lower:
            return "URGENT"


    # --------------------------------------------------------
    # 5. SEVERITY-BASED DECISION
    # --------------------------------------------------------

    if severity == "SEVERE":
        return "URGENT"


    # --------------------------------------------------------
    # 6. INSUFFICIENT INFORMATION
    # --------------------------------------------------------

    if severity == "UNKNOWN":
        return "NEEDS_MORE_INFORMATION"


    # --------------------------------------------------------
    # 7. ROUTINE
    # --------------------------------------------------------

    return "ROUTINE"
    # --------------------------------------------------------
    # 6. RETURN COMPLETE TRIAGE RESULT
    # --------------------------------------------------------

    return {

        "symptoms": symptoms,

        "context": context,

        "red_flags": red_flags,

        "priority": priority
    }
# ============================================================
# 9. KGMU DEPARTMENT ROUTER
# ============================================================
# ============================================================
# 7. ROUTE PATIENT TO DEPARTMENT
# ============================================================

def route_department(patient, priority):

    # --------------------------------------------------------
    # 1. NORMALIZE SYMPTOMS
    # --------------------------------------------------------

    symptoms = normalize_symptoms(
        patient["symptoms"]
    ).lower().strip()
    # --------------------------------------------------------
    # EMERGENCY CASES GO TO EMERGENCY PATHWAY
    # --------------------------------------------------------
# --------------------------------------------------------
    # 2. EMERGENCY CASES GO TO EMERGENCY PATHWAY
    # --------------------------------------------------------

    if priority == "EMERGENCY":

        return "Emergency Medicine"

    # --------------------------------------------------------
    # 2. CHECK WHETHER SYMPTOMS ARE TOO VAGUE
    # --------------------------------------------------------

    vague_inputs = [
        "pain",
        "problem",
        "issue",
        "not feeling well",
        "feeling sick",
        "unwell",
        "unspecified symptom"
    ]

    if symptoms in vague_inputs:

        return "NEEDS_MORE_INFORMATION"


    # --------------------------------------------------------
    # 3. DEPARTMENT RULES
    # --------------------------------------------------------

    department_rules = {

        "Emergency Medicine": [
            "difficulty breathing",
            "chest pain",
            "severe bleeding",
            "loss of consciousness",
            "major trauma",
            "major injury",
            "seizure"
        ],

        "Cardiology": [
            "palpitations",
            "heart problem"
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
            "weakness",
            "dizziness"
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
            "blood in urine"
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

        "Psychiatry": [
            "depression",
            "anxiety",
            "panic attack",
            "mental health"
        ],

        "Respiratory Medicine": [
            "cough",
            "asthma",
            "respiratory problem"
        ],

       "Orthopedic Surgery": [
    "bone pain",
    "fracture",
    "joint pain",
    "back pain",
    "shoulder pain",
    "neck pain",
    "leg pain",
    "arm pain",
    "foot pain",
    "ankle pain",
    "knee pain",
    "elbow pain",
    "wrist pain",
    "hip pain"
],

        "Trauma Surgery": [
            "accident",
            "trauma"
        ],

        "General Surgery": [
            "surgical problem",
            "lump",
            "hernia"
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
            "body pain",
            "general illness"
        ]
    }


    # --------------------------------------------------------
    # 4. FIND MATCHING DEPARTMENTS
    # --------------------------------------------------------

    matched_departments = []

    for department, keywords in department_rules.items():

        for keyword in keywords:

            if keyword in symptoms:

                matched_departments.append(
                    department
                )

                break


    # --------------------------------------------------------
    # 5. NO MATCH → ASK FOR MORE INFORMATION
    # --------------------------------------------------------

    if len(matched_departments) == 0:

        return "NEEDS_MORE_INFORMATION"


    # --------------------------------------------------------
    # 6. SINGLE CLEAR MATCH
    # --------------------------------------------------------

    if len(matched_departments) == 1:

        return matched_departments[0]


    # --------------------------------------------------------
    # 7. MULTIPLE POSSIBLE DEPARTMENTS
    # --------------------------------------------------------

    return "NEEDS_MORE_INFORMATION"


        # 

# ============================================================
# 10. GENERATE PATIENT MESSAGE
# ============================================================

# ============================================================
# 8. GENERATE PATIENT MESSAGE
# ============================================================

def generate_message(priority):

    # --------------------------------------------------------
    # EMERGENCY
    # --------------------------------------------------------

    if priority == "EMERGENCY":

        return (
            "Your responses indicate symptoms that require "
            "immediate clinical assessment. Please proceed "
            "to the appropriate emergency service."
        )


    # --------------------------------------------------------
    # URGENT
    # --------------------------------------------------------

    elif priority == "URGENT":

        return (
            "Your symptoms have been classified as URGENT "
            "by this prototype. Prompt clinical assessment "
            "is recommended."
        )


    # --------------------------------------------------------
    # NEEDS MORE INFORMATION
    # --------------------------------------------------------

    elif priority == "NEEDS_MORE_INFORMATION":

        return (
            "We need a little more information to understand "
            "your symptoms and identify the appropriate "
            "care pathway."
        )


    # --------------------------------------------------------
    # ROUTINE
    # --------------------------------------------------------

    else:

        return (
            "Your symptoms have been classified as ROUTINE "
            "by this prototype. Please follow the appropriate "
            "hospital OPD process."
        )
# ============================================================
# 11. DISPLAY RESULT
# ============================================================

def display_result(result):

    print("\n")
    print("=" * 50)
    print("              TRIAGE RESULT")
    print("=" * 50)

    print(
        "Symptoms       :",
        ", ".join(result["symptoms"])
    )

    print(
        "Severity       :",
        result["severity"]
    )

    print(
        "Priority       :",
        result["priority"]
    )

    print(
        "Department     :",
        result["department"]
    )

    print(
        "Red Flags      :",
        ", ".join(result["red_flags"])
        if result["red_flags"]
        else "None detected"
    )

    print("\nMessage:")
    print(result["message"])

    print("=" * 50)

    print(
        "Prototype decision only."
    )

    print(
        "Clinical assessment is required."
    )

    print("=" * 50)


# ============================================================
# 12. MAIN PROGRAM
# ============================================================

def main():

    patient = collect_patient()

    triage_result = triage_patient(
        patient
    )

    priority = triage_result["priority"]
    context = triage_result["context"]
    red_flags = triage_result["red_flags"]
    symptoms = triage_result["symptoms"]

    # FOLLOW-UP QUESTION
    if priority == "NEEDS_MORE_INFORMATION":

        follow_up_question = generate_follow_up_question(
            patient,
            context,
            symptoms,
            red_flags
        )

        if follow_up_question:

            answer = collect_follow_up_response(
                follow_up_question
            )

            # Check if patient did not specify exact pain location
            if is_unspecified_pain_location(answer):

                second_question = (
                    "Please tell me the specific area where "
                    "you are experiencing the pain. "
                    "For example: shoulder, neck, leg, arm, "
                    "foot, or another specific body area."
                )

                answer = collect_follow_up_response(
                    second_question
                )

            patient = update_patient_from_follow_up(
                patient,
                answer
            )
            print(
            "DEBUG - Updated symptoms:",
            patient["symptoms"]
            )

            # Re-run triage with updated patient information
            triage_result = triage_patient(
                patient
            )

            priority = triage_result["priority"]
            context = triage_result["context"]
            red_flags = triage_result["red_flags"]
            symptoms = triage_result["symptoms"]

    # DEPARTMENT ROUTING
    department = route_department(
        patient,
        priority
    )

    # MESSAGE
    message = generate_message(
        priority
    )

    result = {
        "symptoms": symptoms,
        "severity": context["severity"],
        "priority": priority,
        "department": department,
        "red_flags": red_flags,
        "message": message
    }

    display_result(
        result
    )


if __name__ == "__main__":
    main()