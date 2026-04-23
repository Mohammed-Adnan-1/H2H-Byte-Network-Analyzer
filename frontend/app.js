let chart;

// ✅ SAFE EVENT HANDLING (NO REFRESH, NO PROPAGATION ISSUES)
document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("analyzeBtn");

    btn.addEventListener("click", (e) => {
        e.stopPropagation();   // 🔥 prevents unwanted triggers
        analyzeWiFi();
    });
});


// ✅ MAIN FUNCTION
async function analyzeWiFi() {

    // 🔥 START LOADING
    document.getElementById("loading").style.display = "block";

    const data = {
        latency: 120,
        packet_loss: 3,
        signal_dbm: -75
    };

    try {
        const response = await fetch("https://h2h-byte-network-analyzer.onrender.com/analyze", {
    method: "POST",   // 🔥 VERY IMPORTANT
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
});

        const result = await response.json();

        // ✅ UPDATE UI
        document.getElementById("qoe").innerText = result.qoe;
        document.getElementById("cause").innerText = result.root_cause;
        document.getElementById("fix").innerText = result.recommendation;
        document.getElementById("explanation").innerText = result.explanation;

        // ✅ COLOR CODING QoE
        const qoeElement = document.getElementById("qoe");
        if (result.qoe === "Good") qoeElement.style.color = "#22c55e";
        else if (result.qoe === "Moderate") qoeElement.style.color = "#facc15";
        else qoeElement.style.color = "#ef4444";

        // ✅ CHART
        const ctx = document.getElementById("chart").getContext("2d");

        if (chart) chart.destroy();

        chart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: ["Latency", "Packet Loss", "Signal"],
                datasets: [{
                    label: "WiFi Metrics",
                    data: [data.latency, data.packet_loss, data.signal_dbm],
                    backgroundColor: [
                        "#38bdf8",
                        "#facc15",
                        "#ef4444"
                    ],
                    borderRadius: 10
                }]
            },
            options: {
                plugins: {
                    legend: {
                        labels: {
                            color: "white"
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: { color: "white" }
                    },
                    y: {
                        ticks: { color: "white" }
                    }
                }
            }
        });

    } catch (error) {
        console.error("ERROR:", error);
    }

    // 🔥 ALWAYS STOP LOADING
    document.getElementById("loading").style.display = "none";
}