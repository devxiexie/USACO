import java.util.*;
import java.io.*;

public class swap {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("swap.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new BufferedWriter(new FileWriter("swap.out"))));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int a1 = Integer.parseInt(st.nextToken());
        int a2 = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int b1 = Integer.parseInt(st.nextToken());
        int b2 = Integer.parseInt(st.nextToken());
        
        int line[] = new int[n];
        for (int i = 0; i < n; i++) {
            line[i] = i + 1;
        }

        for (int i = 0; i < k; i++) {
            int t1=a1; 
            int t2=a2;
            while(a1<a2){
                int tempswap = line[a1-1];
                line[a1-1] = line[a2-1];
                line[a2-1] = tempswap;
                a1++;
                a2--;
            }
            a1=t1;
            a2=t2;
            t1=b1;
            t2=b2;
            while(b1<b2){
                int tempswap = line[b1-1];
                line[b1-1] = line[b2-1];
                line[b2-1] = tempswap;
                b1++;
                b2--;
            }
            b1=t1;
            b2=t2;
        }
        
        

        for(int i=0;i<n;i++){
            pw.println(line[i]);
        }
        pw.close();

    }
}
