# Billing Agent
import datetime

def charge_agents(agents=3):
    today = datetime.date.today()
    cost = agents * 1
    print(f"[Billing Agent] Charging ${cost} for {agents} agents on {today}")
    return {"date": today, "amount": cost}

if __name__ == "__main__":
    billing = charge_agents()
    print(f"[Billing Agent] Billing completed: ${billing['amount']}")
