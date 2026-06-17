class Solution {

    public String encode(List<String> strs) {
        String str = "";
        for (String s : strs) {
            str = str + s.length() + "#" + s;
        }
        return str;
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<String>();

        int delim_index = 0; // 0

        while (delim_index < str.length()) {
            // dynamically read size of word
            int word_pos = 1 + delim_index; // 
            while (str.charAt(word_pos) != '#') {
                word_pos++;
            }

            int word_length = Integer.parseInt(str.substring(delim_index, word_pos));
            strs.add(str.substring(word_pos + 1, 1 + word_pos + word_length));
            delim_index = 1 + word_pos + word_length;
        }
        
        return strs;
    }

    // 2we3say1:3yes10!@#$%^&*()
    // we, say, :, yes, !@#$%^&*()
}
