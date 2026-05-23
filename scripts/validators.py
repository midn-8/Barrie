import json

def load_config():
    with open("config/parameters.json", "r") as f:
        return json.load(f)

def check_barrier_ratio(ceramide, cholesterol, fatty_acids):
    config = load_config()
    ideal = config["ideal_lipid_ratio"]
    
    if (ceramide / cholesterol >= ideal["ceramide"]/ideal["cholesterol"]) and \
       (cholesterol / fatty_acids >= ideal["cholesterol"]/ideal["fatty_acids"]):
        return True, "Optimal"
    return False, "Warning: Ratio deviates from physiological standards"
