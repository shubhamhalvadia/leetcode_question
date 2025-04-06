def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = gain[0]
        for i in range(1,len(gain)):
            gain[i] += gain[i-1]
            if gain[i] > max_altitude:
                max_altitude = gain[i]
        print(gain)
        if max_altitude > 0: return max_altitude
        else: return 0