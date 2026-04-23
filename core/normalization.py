def normalize(data):
    return {
        "signal_dbm": data.get("signal_dbm", -70),
        "latency": data.get("latency", 0),
        "packet_loss": data.get("packet_loss", 0),
        "throughput": data.get("throughput", 0)
    }