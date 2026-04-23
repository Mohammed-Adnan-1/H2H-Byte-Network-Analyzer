from flask import request, jsonify
from core.normalization import normalize
from core.feature_engineering import extract_features
from core.root_cause_engine import detect_root_cause
from core.qoe_engine import calculate_qoe
from core.recommendation_engine import suggest_fix
from backend.database import insert_log

def register_routes(app):

    @app.route("/analyze", methods=["POST"])
    def analyze():
        raw_data = request.json

        # Step 1: Normalize
        norm = normalize(raw_data)

        # Step 2: Features
        features = extract_features(norm)

        # Step 3: Root cause
        cause = detect_root_cause(features)

        # Step 4: QoE
        qoe = calculate_qoe(norm)

        # Step 5: Recommendation
        fix = suggest_fix(cause)

        #  DEBUG PRINTS (INSIDE FUNCTION)
        print("Received Data:", raw_data)
        print("Normalized:", norm)
        print("Features:", features)
        print("Root Cause:", cause)
        print("QoE:", qoe)
        print("Recommendation:", fix)

        # Step 6: Store
        insert_log(norm, qoe)

        explanation = f"Your WiFi signal is {norm['signal_dbm']} dBm with {norm['packet_loss']}% packet loss, causing {cause}"

        return jsonify({
            "normalized": norm,
            "features": features,
            "root_cause": cause,
            "qoe": qoe,
            "recommendation": fix,
            "explanation": explanation
        })