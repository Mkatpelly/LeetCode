class Solution {
    public String findContestMatch(int n) {
        List<String> teams = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            teams.add(String.valueOf(i));
        }

        while (teams.size() > 1) {
            List<String> newTeams = new ArrayList<>();
            int i = 0;
            int j = teams.size() - 1;
            while (i < j) {
                newTeams.add("(" + teams.get(i) + "," + teams.get(j) + ")");
                i++;
                j--;
            }
            teams = newTeams;
        }

        return teams.get(0);
    }
}