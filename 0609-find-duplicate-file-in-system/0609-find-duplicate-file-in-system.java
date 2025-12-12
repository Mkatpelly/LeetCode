class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        Map<String, List<String>> contentToFilePaths = new HashMap<>();

        for (String path : paths) {
            String[] parts = path.split(" ");
            String directory = parts[0];

            for (int i = 1; i < parts.length; i++) {
                String[] fileParts = parts[i].split("\\(");
                String fileName = fileParts[0];
                String content = fileParts[1].replace(")", "");

                String fullPath = directory + "/" + fileName;
                contentToFilePaths.putIfAbsent(content, new ArrayList<>());
                contentToFilePaths.get(content).add(fullPath);
            }
        }

        List<List<String>> duplicates = new ArrayList<>();
        for (List<String> filePaths : contentToFilePaths.values()) {
            if (filePaths.size() > 1) {
                duplicates.add(filePaths);
            }
        }

        return duplicates;
    }
}