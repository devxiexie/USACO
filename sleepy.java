import java.util.*;
import java.io.*;

public class sleepy {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new FileReader("sleepy.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new BufferedWriter(new FileWriter("sleepy.out"))));
        int n = Integer.parseInt(br.readLine());
        System.out.println(n);
        

        int ans = n - 1;

        String line=br.readLine();
       
        String[] splited = line.split(" ");
        
        int[] list = new int[n];
        for(int i=0;i<n;i++){
            list[i]=Integer.parseInt(splited[i]);
            System.out.println(list[i]);
        }



        for (int i = n - 2; i > -1; i--) {
            if (list[i] < list[i + 1]) {
                ans = i;
            } 
            else {
                break;
            }
        }
        System.out.println(ans);
        pw.println(ans);
        pw.close();
    }
}
