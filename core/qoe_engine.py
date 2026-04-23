def calculate_qoe(data):
    score = 100

    # Reduce score based on latency
    score -= data.get("latency", 0) * 0.2

    # Reduce score based on packet loss
    score -= data.get("packet_loss", 0) * 5

    # Weak signal penalty
    if data.get("signal_dbm", -70) < -70:
        score -= 20

    # Clamp score between 0 and 100
    score = max(0, min(100, score))

    # Convert to category
    if score > 80:
        return "Good"
    elif score > 50:
        return "Moderate"
    else:
        return "Poor"