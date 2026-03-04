virus_treatment = {
    "influenza": {
        "symptoms": ["fever", "cough", "sore throat", "headache"],
        "treatment": ["rest", "hydration", "antiviral medication"]
    },
    "common cold": {
        "symptoms": ["runnynose", "cough", "shivering", "feather dropping", "running temprature" "headache"],
        "treatment": ["rest", "antibiotics", "increase temperature but not above 28 degree"]
    },
    "Coccidiosis": {
        "symptoms": ["fever", "cough", "shortness of breath", "high mortality", "brownish watery stool"],
        "treatment": [ "hydration", "antiviral medication", "spacing"]
    },
    "pox": {
        "symptoms": ["swollen around eyes", "nose running", "shivering and feather droppings"],
        "treatment": ["antipox medications", "antibiotics"]
    },
    "cholera and fever": {
        "symptoms": ["continous stool", "cough", "shivering and feather dropping in birds and weakness in other"],
        "treatment": ["increase hygiene", "cholera and fever medicatioons"]
    },
    "marek,gumboro,e-coli": {
        "symptoms": ["difficulty defecating", "lost appetite", "twisted neck"],
        "treatment": ["vaccinate against marek,gumboro,e-coli", "maintain proper hygiene", "antibiotics"]
    },

    }

def get_virus_treatment(symptoms):
    for virus, info in virus_treatment.items():
        if all(symptom in info["symptoms"] for symptom in symptoms):
            return virus, info["treatment"]
    return None, None
def main():
    print("Enter your symptoms (seperated by commas):")
    symptoms = [symptoms.strip() for symptom in input().split(",")]
    virus, treatment = get_virus_treatment(symptoms)
    if virus:
        print(f"possible virus: {virus}")
        print(f"recommended treatment:")
        for item in treatment:
            print(f"- {item}")
    else:
        print("new virus alert!!!!.")

    
    
            
