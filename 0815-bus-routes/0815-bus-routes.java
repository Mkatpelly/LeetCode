class Solution {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) return 0;

        // Map each stop to the list of routes that include it
        Map<Integer, List<Integer>> stopToRoutes = new HashMap<>();
        for (int i = 0; i < routes.length; i++) {
            for (int stop : routes[i]) {
                stopToRoutes.computeIfAbsent(stop, k -> new ArrayList<>()).add(i);
            }
        }

        // BFS: queue stores the route index, and we track the number of buses taken
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visitedRoutes = new HashSet<>();
        Set<Integer> visitedStops = new HashSet<>();

        // Start from all routes that contain the source stop
        for (int routeIndex : stopToRoutes.getOrDefault(source, new ArrayList<>())) {
            queue.offer(routeIndex);
            visitedRoutes.add(routeIndex);
        }

        int buses = 1;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int routeIndex = queue.poll();
                // Check if the current route contains the target stop
                for (int stop : routes[routeIndex]) {
                    if (stop == target) return buses;
                    // Add all routes that share this stop and haven't been visited
                    for (int nextRoute : stopToRoutes.getOrDefault(stop, new ArrayList<>())) {
                        if (!visitedRoutes.contains(nextRoute)) {
                            visitedRoutes.add(nextRoute);
                            queue.offer(nextRoute);
                        }
                    }
                }
            }
            buses++;
        }

        return -1;
    }
}