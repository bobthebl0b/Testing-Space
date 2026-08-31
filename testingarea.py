import random
def play_session(num_rounds):
    """Plays a single session of coin flips and returns the win rate"""
    wins = 0
    for _ in range(num_rounds):#kkk
        # Automated guess
        guess = random.choice(['heads', 'tails'])
        flip = random.choice(['heads', 'tails'])
        
        if guess == flip:
            wins += 1
            
    return (wins / num_rounds) * 100

def run_simulation(num_sessions=5, rounds_per_session=10):
    """Runs multiple sessions and calculates the average win rate"""
    print(f"--- Starting Simulation: {num_sessions} sessions of {rounds_per_session} rounds each ---\n")
    
    total_win_rate = 0
    
    for i in range(1, num_sessions + 1):
        win_rate = play_session(rounds_per_session)
        total_win_rate += win_rate
        print(f"Session {i}: Win Rate = {win_rate:.1f}%")
        
    average_win_rate = total_win_rate / num_sessions
    
    print("\n" + "=" * 40)
    print(f"SIMULATION COMPLETE")
    print(f"Average Win Rate: {average_win_rate:.1f}%")
    print("=" * 40)

if __name__ == "__main__":
    run_simulation(num_sessions=5, rounds_per_session=10)