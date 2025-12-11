class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();
        String[] components = path.split("/");

        for (String component : components){
            if (component.equals("") || component.equals(".")){
                continue;
            }
            else if (component.equals("..")){
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            }
            else{
                stack.push(component);
            }
        }
        StringBuilder simplifiedPath = new StringBuilder();
        for (String dir : stack) {
            simplifiedPath.append("/").append(dir);
        }
        return simplifiedPath.length() > 0 ? simplifiedPath.toString() : "/";
    }
}