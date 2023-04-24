
public class FloatDoubleExample {
	public static void main(String[] args) {
		//float var1 = 3.14; <- 실수 리터럴을 float 타입 변수에 저장하면 컴파일 에러 발셍 => 해결을 위해서는 리터럴 뒤에 f / F를 붙여 컴파일러로 하여금 float 타입임을 알 수 있게 해야 함.
		float var2 = 3.14f;
		double var3 = 3.14;
		
		float var4 = 0.1234567890123456789f;
		double var5 = 0.1234567890123456789;
		
		System.out.println("var2: " + var2);
		System.out.println("var3: " + var3);
		System.out.println("var4: " + var4);
		System.out.println("var5: " + var5);
		
		double var6 = 3e6;
		float var7 = 3e6F;
		double var8 = 2e-3;
		System.out.println("var6: " + var6);
		System.out.println("var7: " + var7);
		System.out.println("var8: " + var8);
	}
}
