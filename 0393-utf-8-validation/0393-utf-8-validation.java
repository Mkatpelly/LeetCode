class Solution {
    public boolean validUtf8(int[] data) {
        int i = 0;
        while (i < data.length) {
            int byte1 = data[i];
            int numBytes = 0;
            if ((byte1 >> 7) == 0b0) {
                numBytes = 1;
            } else if ((byte1 >> 5) == 0b110) {
                numBytes = 2;
            } else if ((byte1 >> 4) == 0b1110) {
                numBytes = 3;
            } else if ((byte1 >> 3) == 0b11110) {
                numBytes = 4;
            } else {
                return false;
            }
            if (i + numBytes > data.length) {
                return false;
            }
            for (int j = 1; j < numBytes; j++) {
                int byteN = data[i + j];
                if ((byteN >> 6) != 0b10) {
                    return false;
                }
            }
            i += numBytes;
        }
        
        return true;
    }
}