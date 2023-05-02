//it don't work
import java.io.*;
import java.util.*;

public class whereami {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("whereami.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new BufferedWriter(new FileWriter("whereami.out"))));
        StringBuilder stringBuilder = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        char[] buffer = new char[n];
        while (br.read(buffer) != -1) {
            stringBuilder.append(new String(buffer));
            buffer = new char[n];
        }
        String line = stringBuilder.toString();
        br.close();

        System.out.println(line);

        char[] act = new char[line.length()];

        for (int i = 0; i < line.length(); i++) {
            act[i] = line.charAt(i);
        }
        char a[] = Arrays.copyOfRange(act, 0, 2);
        System.out.println(a);
        for (int guess = 1; guess <= n; guess++) {
            boolean good = true;
            for (int i = 0; i + guess <= n; i++) {
                for (int j = 0; j < i; j++) {
                    char c[] = Arrays.copyOfRange(act, i, guess+1);
                    char b[] = Arrays.copyOfRange(act, j, guess+1);
                    if (c == b) {
                        good = false;
                    }
                }
            }
            if (good) {
                System.out.println(guess);
                break;
            }
        }

    }
}
