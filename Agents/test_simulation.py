# 3-Day Simulation of the Autonomous Game Company
from game_generator import generate_game
from marketing_agent import post_ads
from billing_agent import charge_agents

def run_simulation(days=3):
    for day in range(1, days+1):
        print(f"\n--- Simulation Day {day} ---")
        game = generate_game()
        metrics = post_ads(game)
        billing = charge_agents()
        print(f"Summary: Game={game['title']}, CTR={metrics['CTR']}, Amount Charged=${billing['amount']}")

if __name__ == "__main__":
    run_simulation()
