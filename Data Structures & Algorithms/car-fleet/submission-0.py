class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i],speed[i]) for i in range(len(position))], reverse = True)
        st = []
        for pos,sp in cars:
            time = (target - pos) / sp

            if not st or time > st[-1]:
                st.append(time)
        return len(st)
            
