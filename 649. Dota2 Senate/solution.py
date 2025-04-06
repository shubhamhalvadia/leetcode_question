from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

    # Step 1: Initialize queues with indexes
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

    # Step 2: Simulate the rounds
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

        # Whoever has the smaller index bans the other
            if r < d:
                radiant.append(r + n)  # Radiant gets back in line for the next round
            else:
                dire.append(d + n)     # Dire gets back in line for the next round

    # Step 3: Declare the winner
        return "Radiant" if radiant else "Dire"