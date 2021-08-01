import java.io.*;
import java.util.*;
 
public class barns {
 
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine());
        Integer[] cows = new Integer[n];
        StringTokenizer tokenizer = new StringTokenizer(in.readLine());
        for (int j = 0; j < n; j++) {
            cows[j] = Integer.parseInt(tokenizer.nextToken());
        }
        Integer[] stalls = new Integer[n];
        tokenizer = new StringTokenizer(in.readLine());
        for (int j = 0; j < n; j++) {
            stalls[j] = Integer.parseInt(tokenizer.nextToken());
        }
        Arrays.sort(stalls);
        long answer = 1;
        for (int j = 0; j < n; j++) {
            long howManyFit = 0;
            for (int cow : cows) {
                if (cow <= stalls[j]) {
                    howManyFit++;
                }
            }
            howManyFit -= j;
            answer *= howManyFit;
        }
        System.out.println(answer);
    }
}
