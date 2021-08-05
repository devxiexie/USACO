import java.util.*;
import java.io.*;

public class race {

    public static int solve(int num, int x) {
        int l = 0;
        int r = 0;
        int timeused = 0;
        for (int curr = 1;; curr++) {
            l += curr;
            timeused++;
            if (l + r >= num) {
                return timeused;
            }
            if (curr >= x) {
                r += curr;
                timeused++;
                if (l + r >= num) {
                    return timeused;
                }

            }

        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new FileReader("race.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new BufferedWriter(new FileWriter("race.out"))));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int end[] = new int[n];
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());
            end[i] = x;

        }
        for(int i = 0; i < n; i++){
            System.out.println(solve(k,end[i]));
            pw.println(solve(k,end[i]));
        
        }
        pw.close();
    }
}
