class Solution {
    public boolean isNumber(String s) {
        String numberPattern = "^[+-]?(\\d+(\\.\\d*)?|\\.\\d+)([eE][+-]?\\d+)?$";
        return s.matches(numberPattern);
    }
}