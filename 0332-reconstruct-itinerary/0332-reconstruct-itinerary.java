class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, PriorityQueue<String>> graph = new HashMap<>();
        for (List<String> ticket : tickets) {
            graph
                .computeIfAbsent(ticket.get(0), k -> new PriorityQueue<>())
                .add(ticket.get(1));
        }

        LinkedList<String> itinerary = new LinkedList<>();
        dfs("JFK", graph, itinerary);
        return itinerary;
    }
    
    private void dfs(String airport, Map<String, PriorityQueue<String>> graph, LinkedList<String> itinerary) {
        PriorityQueue<String> dests = graph.get(airport);
        while (dests != null && !dests.isEmpty()) {
            String next = dests.poll();
            dfs(next, graph, itinerary);
        }
        itinerary.addFirst(airport);  // Add after visiting all descendent airports
    }
}