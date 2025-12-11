class Solution {
    public String nearestPalindromic(String n) {
        long num = Long.parseLong(n);
        int len = n.length();
        List<Long> candidates = new ArrayList<>();

        // Edge cases: 10...01 and 9...9
        candidates.add((long)Math.pow(10, len - 1) - 1); // e.g., 999
        candidates.add((long)Math.pow(10, len) + 1);     // e.g., 1001

        // Middle palindromes
        long prefix = Long.parseLong(n.substring(0, (len + 1) / 2));
        for (long i = -1; i <= 1; i++) {
            StringBuilder sb = new StringBuilder();
            String pre = String.valueOf(prefix + i);
            sb.append(pre);
            // If length is odd, drop the last char for the mirror
            String mirror = (len % 2 == 0) ? pre : pre.substring(0, pre.length() - 1);
            sb.append(new StringBuilder(mirror).reverse());
            candidates.add(Long.parseLong(sb.toString()));
        }

        long minDiff = Long.MAX_VALUE, res = -1;
        for (long cand : candidates) {
            if (cand == num) continue;
            long diff = Math.abs(cand - num);
            if (diff < minDiff || (diff == minDiff && cand < res)) {
                minDiff = diff;
                res = cand;
            }
        }
        return String.valueOf(res);
    }
}