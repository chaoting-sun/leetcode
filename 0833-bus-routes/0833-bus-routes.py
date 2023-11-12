class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # base case
        if source == target:
            return 0

        stop2bus = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stop2bus[stop].append(bus)

        nBus = 0
        queue = deque([source]) # for stop
        visitedBus = set() # for bus

        while queue:
            nBus += 1
            size = len(queue)

            for i in range(size):
                stopFrom = queue.popleft()
                
                for bus in stop2bus[stopFrom]:
                    # we will check every stops a bus can arrive
                    # so we ignore the bus that has been taken
                    if bus in visitedBus:
                        continue
                    # try to take this bus
                    visitedBus.add(bus)
                    # check all the stops the bus goes to
                    for stopTo in routes[bus]:
                        if stopTo == target:
                            return nBus
                        queue.append(stopTo)        
        return -1