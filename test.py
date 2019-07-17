import java.util.Scanner;
import java.lang.Math;
//test AP
class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int a = s.nextInt();
    int n = s.nextInt();
    int d = s.nextInt();
    int t = a + (n-1) * d;
    System.out.print(t);
  }
}
