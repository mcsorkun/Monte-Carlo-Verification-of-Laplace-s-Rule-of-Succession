
import numpy as np
from tqdm.notebook import tqdm

def reverse_monte_carlo(w, l, n_accept=10000):
    accepted = 0
    next_wins = 0

    with tqdm(total=n_accept, desc="Simulating accepted trials") as pbar:
        while accepted < n_accept:
            # Step 1: sample p uniformly
            p = np.random.rand()
            # print("p:",p)
            # Step 2: simulate observed data
            draws = np.random.rand(w + l) < p
            # print(draws)

            if draws.sum() == w:
                accepted += 1
                pbar.update(1) # Update the progress bar when a trial is accepted
                # print("Accepted")
                # Step 3: simulate next draw
                next_draw = np.random.rand()
                # print("Next draw:",next_draw)
                if next_draw < p:
                    next_wins += 1

    return next_wins / accepted

# example
w, l = 3, 1
estimate = reverse_monte_carlo(w, l)
theoretical = (w + 1) / (w + l + 2)

print("Reverse MC:", estimate)
print("Theoretical:", theoretical)
