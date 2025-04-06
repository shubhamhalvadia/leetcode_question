def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for asteroid in asteroids:

            if asteroid>0:
                stack.append(asteroid)
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(asteroid):
                    stack.pop()
                    
                if stack and abs(asteroid)<stack[-1]:
                    continue
                if stack and abs(asteroid)==stack[-1]:
                    stack.pop()
                    continue
                if stack and stack[-1]<0 and asteroid<0:
                    stack.append(asteroid)
                if not(stack):
                    stack.append(asteroid)    
        return stack