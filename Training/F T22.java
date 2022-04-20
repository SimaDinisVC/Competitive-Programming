import java.util.*;
class MyClass {
    public static void main(String[ ] args) {
        Scanner scanThis = new Scanner(System.in);
        System.out.print("");
        int N = Integer.parseInt(scanThis.nextLine());
        String Ni[] = (scanThis.nextLine()).split(" ");
        System.out.print("");
        int M = Integer.parseInt(scanThis.nextLine());
        String Mi[] = (scanThis.nextLine()).split(" ");
        int pares = 0;
        for (String m : Mi) {
            int m1 = Integer.parseInt(m);
            for (String n : Ni){
                int n1 = Integer.parseInt(n);
                if ((m1+n1)%2 == 0){
                    pares += 1;
                }
        System.out.print(pares + " " + ((M*N)-pares));
            }
        }
    }
}