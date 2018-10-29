import java.util.*;

public class Solution{

     public static void main(String []args){
         Scanner sc = new Scanner(System.in);
         
         int cases = Integer.parseInt(sc.nextLine());
        int anagram;
             boolean found;
        int count1[] = new int [26];
                 int count2[] = new int [26];
         for (int x = 1; x <= cases; x ++) {
             int length = Integer.parseInt(sc.nextLine());
             
             
             String input1 = sc.nextLine();
             String input2 = sc.nextLine();

             
             anagram = 0;
             for (int y = 1; y <= length; y ++) {
                 found = true;
                 
                 
                 for (int z = 0; z + y - 1 < length; z ++) {
                    String temp = input1.substring(z, z + y);
                    String temp2 = "";
                    int tempLength = temp.length();
                    Arrays.fill(count1, 0);
                    for (int a = 0 ; a < tempLength; a++) {
                        count1[((int)(temp.charAt(a))) - 65] ++;
                    }
                    for (int a = 0; a + tempLength <= length; a ++) {
                        Arrays.fill(count2, 0);

                        temp2 = input2.substring( a, a + tempLength);
                        for (int b = 0; b < tempLength; b++) {
                            count2[((int)(input2.charAt(b + a))) - 65] ++;
                        
                        }
                        for (int b = 0; b < 26; b ++) {
                            if (count1[b] != count2[b]) {
                                found = false;
                                break;
                            }
                        }
                        if (found) {

                            break;
                        } else {
                            if (a + tempLength < length)
                            found = true;
                            
                        }
                    }
                    if (found) {
                        anagram ++;
                    } else {
                        found = true;
                    }
                 }
             }
             System.out.println ("Case #" + x + ": " + anagram);
         }
     }
}