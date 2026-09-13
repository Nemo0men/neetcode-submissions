// import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        //sort arrays
        char[] arrayS;
        arrayS = s.toCharArray();
        Arrays.sort(arrayS);
        char[] arrayT;
        arrayT = t.toCharArray();
        Arrays.sort(arrayT);

        System.out.println(arrayS);
        System.out.println(arrayT);
    
        //compare arrays
        return Arrays.equals(arrayS, arrayT);

    }
}
