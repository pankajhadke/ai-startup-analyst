# app/risk_assessment.py

def detect_risks(startup_metrics, benchmark):
    """Flags potential risk indicators based on a benchmark."""
    risks = []
    
    if benchmark:
        if startup_metrics["churn_rate"] > benchmark["avg_churn_rate"] * 1.2:
            risks.append("High churn rate compared to sector average.")
        
        if startup_metrics["market_size"] < benchmark["avg_market_size"] * 0.5:
            risks.append("Market size is significantly smaller than sector average.")
    
    # You could add more complex rules or use an AI model here
    if startup_metrics["churn_rate"] > 0.2:
        risks.append("Churn rate exceeds 20%.")
    
    return risks
