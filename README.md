# Monte-Carlo-Verification-of-Laplace-s-Rule-of-Succession

This Python script implements a Reverse Monte Carlo simulation to verify Laplace's Rule of Succession. Laplace's Rule provides a way to estimate the probability of a future event given past observations, especially when prior information is limited.

As an example case of the problem, the code demonstrates how to estimate the probability of winning in a raffle (or any binary event) **when the true probability is unknown**. The code:

1. **Simulates possible “raffle machines”** with unknown win probability.
2. **Filters only the machines** that could have produced the observed results (wins and losses).
3. **Predicts the next outcome** by averaging over these plausible machines.

This method shows how Laplace’s Rule of Succession emerges naturally, purely from simulation, without assuming the Beta distribution.

---

## How It Works

1. Input:
   - `w` = number of observed wins
   - `l` = number of observed losses
2. Randomly guess a possible win probability `p`.
3. Simulate the observed sequence of wins/losses using `p`.
4. Accept `p` if it matches the observed results exactly.
5. Simulate one additional “next draw” for this accepted `p`.
6. Repeat until enough accepted worlds are collected.
7. Compute the fraction of next draws that are wins → estimated probability.

---

## Example Usage

```python
w, l = 3, 1
estimate = reverse_monte_carlo(w, l)
print("Estimated probability of next win:", estimate)
