class Solution {
    public boolean isAnagram(String s, String t) {
        char[] chars1 = s.toCharArray();
        Arrays.sort(chars1);

        char[] chars2 = t.toCharArray();
        Arrays.sort(chars2);

        String sorted1= String.valueOf(chars1);
        String sorted2= String.valueOf(chars2);

        if(sorted1.equals(sorted2)){
            return true;
        }
        return false;

    }


}
