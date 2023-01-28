import java.util.*;
import java.io.*;

public class shell {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new FileReader("shell.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new BufferedWriter(new FileWriter("shell.out"))));
        int n = Integer.parseInt(br.readLine());
        int peb1[] = { 0, 2, 3 };
        int peb2[] = { 1, 0, 3 };
        int peb3[] = { 1, 2, 0 };
        int score1 = 0;
        int score2 = 0;
        int score3 = 0;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int temp = peb1[a - 1];
            peb1[a - 1] = peb1[b - 1];
            peb1[b - 1] = temp;

            int temp2 = peb2[a - 1];
            peb2[a - 1] = peb2[b - 1];
            peb2[b - 1] = temp2;

            int temp3 = peb3[a - 1];
            peb3[a - 1] = peb3[b - 1];
            peb3[b - 1] = temp3;

            int g = Integer.parseInt(st.nextToken());

            if (peb1[g - 1] == 0) {
                score1++;
            }
            if (peb2[g - 1] == 0) {
                score2++;
            }
            if (peb3[g - 1] == 0) {
                score3++;
            }
        }
        int x = Math.max(score1, score2);
        int ans = Math.max(score3, x);
        System.out.println(ans);
        pw.println(ans);
        pw.close();
    }
}
