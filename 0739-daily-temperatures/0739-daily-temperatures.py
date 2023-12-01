# method1: hash table (beat 5% time & 95% space)
# time: O(n^2) if temperatures are strictly increasing
# space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp2id = {} # number: index
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)-1,-1,-1):
            minId = 10**6
            currTemp = temperatures[i]
            
            tempToRemove = []
            for prevTemp, prevId in temp2id.items():
                # keep updating the smallest id with higher temp than the current one
                if currTemp < prevTemp:
                    minId = min(minId, prevId)
                else:
                    tempToRemove.append(prevTemp)
            
            # remove the temp smaller than the current one
            for temp in tempToRemove:
                temp2id.pop(temp)
            
            if minId != 10**6:
                answer[i] = minId - i
            
            temp2id[currTemp] = i
                
        return answer


# method2: stack (beat)
# time: O(n)
# space: O(n)

# reverse

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)-1,-1,-1):
            while tempStack and temperatures[i] >= temperatures[tempStack[-1]]:
                tempStack.pop(-1)
            if tempStack:
                answer[i] = tempStack[-1] - i
            tempStack.append(i)

        return answer

# forward

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        answer = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while tempStack and temperatures[tempStack[-1]] < temp:
                prevId = tempStack.pop(-1)
                answer[prevId] = i - prevId
            tempStack.append(i)
        return answer