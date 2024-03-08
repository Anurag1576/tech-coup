import java.util.Scanner;

public class test5 {

	public static void main(String[] args) {
		int a,b,c;
		Scanner sc= new Scanner(System.in);
		System.out.println("enter value of a:");
		a=sc.nextInt();
		System.out.println("Enter value of b");
		b=sc.nextInt();
		c=a+b;
	    b=c-b;
	    a=c-a;
	    System.out.println("value of a:" +a+ "value of b:" + b);
//	    System.out.println("Value of b:" +b);
		}

}
