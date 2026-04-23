def suggest_fix(cause):
    fixes = {
        "Distance from router": "Move closer to the router or use a WiFi extender",
        "Interference / Congestion": "Change WiFi channel or switch to 5GHz band",
        "Network congestion": "Reduce number of connected devices or upgrade bandwidth",
        "Stable": "No action needed, network is stable"
    }
    
    return fixes.get(cause, "Try restarting your router")