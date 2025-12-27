class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()

        # Min-heap of free rooms (store room numbers)
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)

        # Min-heap of busy rooms: (end_time, room_number)
        busy_rooms = []

        # Count how many meetings each room hosted
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free all rooms that have finished by 'start'
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                # Use the lowest-numbered free room
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
                count[room] += 1
            else:
                # No free rooms → delay meeting
                end_time, room = heapq.heappop(busy_rooms)
                new_end = end_time + duration
                heapq.heappush(busy_rooms, (new_end, room))
                count[room] += 1

        # Return room with max count (tie → smallest index)
        return count.index(max(count))
