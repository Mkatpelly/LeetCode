class FileSystem {

    class Node {
        boolean isFile;
        Map<String, Node> children = new HashMap<>();
        StringBuilder content = new StringBuilder();
    }
    
    private Node root;
    
    public FileSystem() {
        root = new Node();
    }
    
    public List<String> ls(String path) {
        Node curr = root;
        List<String> res = new ArrayList<>();
        if (!path.equals("/")) {
            String[] parts = path.split("/");
            for (int i = 1; i < parts.length; i++) {
                curr = curr.children.get(parts[i]);
            }
            if (curr.isFile) {
                res.add(parts[parts.length-1]);
                return res;
            }
        }
        res.addAll(curr.children.keySet());
        Collections.sort(res);
        return res;
    }
    
    public void mkdir(String path) {
        Node curr = root;
        String[] parts = path.split("/");
        for (int i = 1; i < parts.length; i++) {
            curr.children.putIfAbsent(parts[i], new Node());
            curr = curr.children.get(parts[i]);
        }
    }
    
    public void addContentToFile(String filePath, String content) {
        Node curr = root;
        String[] parts = filePath.split("/");
        for (int i = 1; i < parts.length; i++) {
            curr.children.putIfAbsent(parts[i], new Node());
            curr = curr.children.get(parts[i]);
        }
        curr.isFile = true;
        curr.content.append(content);
    }
    
    public String readContentFromFile(String filePath) {
        Node curr = root;
        String[] parts = filePath.split("/");
        for (int i = 1; i < parts.length; i++) {
            curr = curr.children.get(parts[i]);
        }
        return curr.content.toString();
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * List<String> param_1 = obj.ls(path);
 * obj.mkdir(path);
 * obj.addContentToFile(filePath,content);
 * String param_4 = obj.readContentFromFile(filePath);
 */