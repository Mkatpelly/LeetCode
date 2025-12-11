class Solution {
    private int[] parent;
    private int[] rank;
    private int count = 0;
    
    private int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }
    
    private void union(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX == rootY) return;
        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        } else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
        count--;
    }

    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        List<Integer> res = new ArrayList<>();
        parent = new int[m * n];
        rank = new int[m * n];
        Arrays.fill(parent, -1);
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        
        for (int[] pos : positions) {
            int r = pos[0], c = pos[1], idx = r * n + c;
            if (parent[idx] != -1) {
                res.add(count);
                continue;
            }
            parent[idx] = idx;
            count++;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1], nidx = nr * n + nc;
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || parent[nidx] == -1)
                    continue;
                union(idx, nidx);
            }
            res.add(count);
        }
        return res;
    }
}