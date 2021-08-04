import java.util.*;
import java.io.*;

public class hoofball {

	public static void main(String[] args) throws Exception {

		Scanner stdin = new Scanner(new File("hoofball.in"));

		
		int n = stdin.nextInt();
		int[] vals = new int[n];
		for (int i=0; i<n; i++)
			vals[i] = stdin.nextInt();
		Arrays.sort(vals);

		
		PrintWriter out = new PrintWriter(new FileWriter("hoofball.out"));
		out.println(solve(vals));
		out.close();
		stdin.close();
	}

	public static int solve(int[] vals) {

		int n = vals.length;

		
		if (n < 3) return 1;

		
		boolean[] right = new boolean[n];
		right[0] = true;

		
		for (int i=1; i<n-1; i++)
			if (vals[i]-vals[i-1] > vals[i+1]-vals[i])
				right[i] = true;

		int ans = 0, i = 0;

		
		while (i < n) {

			
			int rCnt = 0;
			while (right[i]) {
				i++;
				rCnt++;
			}

			
			int lCnt = 0;
			while (i<n && !right[i]) {
				i++;
				lCnt++;
			}

		
			if (rCnt > 1 && lCnt > 1)
				ans += 2;

		
			else
				ans++;
		}

		return ans;
	}
}
