class LogSystem(object):

    def __init__(self):
        self.logs = []
        self.idx = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }

    def put(self, id, timestamp):
        self.logs.append((id, timestamp))

    def retrieve(self, start, end, granularity):
        cut = self.idx[granularity]
        start = start[:cut]
        end = end[:cut]

        res = []
        for log_id, ts in self.logs:
            t = ts[:cut]
            if start <= t <= end:
                res.append(log_id)

        return res



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)