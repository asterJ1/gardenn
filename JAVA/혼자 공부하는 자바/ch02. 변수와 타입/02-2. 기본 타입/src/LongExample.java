
public class LongExample {
	public static void main(String[] args) {
		long var1 = 10;
		long var2 = 20L;
		//long var3 = 1000000000000; <- long 타입 변수에 정수 리터럴을 저장할 때, 컴파일러에게 long 타입임을 알려주지 않으면 컴파일 에러가 발생.
		long var4 = 1000000000000L;
		
		System.out.println(var1);
		System.out.println(var2);
		System.out.println(var4);
	}
}
