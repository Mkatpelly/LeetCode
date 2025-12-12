class AuthenticationManager {

    private final int timeToLive;
    private final Map<String, Integer> tokenExp;

    public AuthenticationManager(int timeToLive) {
        this.timeToLive = timeToLive;
        tokenExp = new HashMap<>();
    }

    public void generate(String tokenId, int currentTime) {
        tokenExp.put(tokenId, currentTime + timeToLive);
    }

    public void renew(String tokenId, int currentTime) {
        Integer exp = tokenExp.get(tokenId);
        // Only renew if token exists and is unexpired
        if (exp != null && exp > currentTime) {
            tokenExp.put(tokenId, currentTime + timeToLive);
        }
    }

    public int countUnexpiredTokens(int currentTime) {
        int count = 0;
        for (Integer exp : tokenExp.values()) {
            if (exp > currentTime) count++;
        }
        return count;
    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager obj = new AuthenticationManager(timeToLive);
 * obj.generate(tokenId,currentTime);
 * obj.renew(tokenId,currentTime);
 * int param_3 = obj.countUnexpiredTokens(currentTime);
 */