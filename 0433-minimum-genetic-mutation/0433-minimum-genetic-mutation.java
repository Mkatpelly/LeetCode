class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {
        Set<String> geneBank = new HashSet<>(Arrays.asList(bank));
        if (!geneBank.contains(endGene)) return -1;
        char[] genes = {'A', 'C', 'G', 'T'};
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        
        queue.offer(startGene);
        visited.add(startGene);
        int mutations = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String current = queue.poll();
                if (current.equals(endGene)) return mutations;

                char[] geneArray = current.toCharArray();
                for (int j = 0; j < geneArray.length; j++) {
                    char originalChar = geneArray[j];

                    for (char g : genes) {
                        if (g == originalChar) continue;
                        geneArray[j] = g;
                        String newGene = new String(geneArray);

                        if (geneBank.contains(newGene) && !visited.contains(newGene)) {
                            queue.offer(newGene);
                            visited.add(newGene);
                        }
                    }
                    geneArray[j] = originalChar;
                    }
            }
            mutations++;
        }
        return -1;
    }
}