class Solution(object):
    def angleClock(self, hour, minutes):
        # 1. Calculate positions in degrees relative to 12:00
        minute_angle = minutes * 6
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        # 2. Find the absolute difference
        diff = abs(hour_angle - minute_angle)
        
        # 3. Return the smaller of the two possible angles
        return min(diff, 360 - diff)
