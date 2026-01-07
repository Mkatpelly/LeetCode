#include <bits/stdc++.h>
using namespace std;

class MyCalendarTwo {
    vector<pair<int,int>> booked;
    vector<pair<int,int>> overlaps;

    static bool intersect(int s1, int e1, int s2, int e2) {
        return max(s1, s2) < min(e1, e2); // non-empty intersection for half-open intervals
    }

public:
    MyCalendarTwo() {}

    bool book(int start, int end) {
        // If new event overlaps any double-booked interval => triple booking
        for (auto &[s, e] : overlaps) {
            if (intersect(start, end, s, e)) return false;
        }

        // Record new double-booked intervals created with existing bookings
        for (auto &[s, e] : booked) {
            if (intersect(start, end, s, e)) {
                overlaps.push_back({max(start, s), min(end, e)});
            }
        }

        booked.push_back({start, end});
        return true;
    }
};
