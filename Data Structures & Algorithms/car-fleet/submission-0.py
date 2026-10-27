class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for car in cars:
            time = (target - car[0])/car[1]    
            if not st or st[-1] < time:
                st.append(time)
            
        return len(st)