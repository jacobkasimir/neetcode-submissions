class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        cars = sorted(zip(position, speed), reverse=True)
        for pos, spd in cars:
            time = (target - pos) / spd
            if not times:
                times.append(time)
            elif times and times[-1] < time:
                times.append(time)
            
        return len(times)