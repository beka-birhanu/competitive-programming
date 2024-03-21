class UndergroundSystem:

    def __init__(self):
        # stores startStation,endStation to the time it took
        self.time = defaultdict(lambda : (0,0))

        # stores the person id maped to a start station,startTime
        self.person = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.person or self.person[id]:
            self.person[id] = t,stationName

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # time is the start time that person id = checked in at start station
        time,startStation = self.person[id]

        # prev_time is the prev average time and travel freq is the nyumber of times persons travle from start staion to end station
        prev_time,travel_freq  = self.time[(startStation,stationName)]


        self.time[(startStation,stationName)] = (travel_freq*prev_time+t-time)/ (travel_freq+1), travel_freq+1



    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.time[(startStation,endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)