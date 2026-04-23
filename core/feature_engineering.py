def extract_features(data):
    features = {}

    # Latency check
    features["is_high_latency"] = data.get("latency", 0) > 100

    # Packet loss check
    features["is_packet_loss"] = data.get("packet_loss", 0) > 2

    # Signal strength check
    features["weak_signal"] = data.get("signal_dbm", -70) < -70

    return features