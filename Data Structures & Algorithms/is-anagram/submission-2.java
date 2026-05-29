class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }

        Map<Character, Integer> map1 = new HashMap<Character, Integer>();
        Map<Character, Integer> map2 = new HashMap<Character, Integer>();

        for (int i = 0; i < s.length(); i++) {

            char char_s = s.charAt(i);
            char char_t = t.charAt(i);
            
            if (!map1.containsKey(char_s))
                map1.put(char_s, 1);
            else
                map1.put(char_s, map1.get(char_s) + 1);

            if (!map2.containsKey(char_t))
                map2.put(char_t, 1);
            else
                map2.put(char_t, map2.get(char_t) + 1);
        }

        return map1.equals(map2);
    }
}
