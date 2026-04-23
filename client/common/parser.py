def parse_log(raw_text):
    data = {}
    for line in raw_text.split("\n"):
        if "Signal" in line:
            data["signal"] = int(line.split(":")[1].strip().replace("%", ""))
    return data