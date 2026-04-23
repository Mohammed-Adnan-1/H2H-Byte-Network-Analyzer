def detect_root_cause(features):
    # Weak signal → distance issue
    if features.get("weak_signal"):
        return "Distance from router"

    # Packet loss → interference
    if features.get("is_packet_loss"):
        return "Interference / Congestion"

    # High latency → congestion
    if features.get("is_high_latency"):
        return "Network congestion"

    return "Stable"