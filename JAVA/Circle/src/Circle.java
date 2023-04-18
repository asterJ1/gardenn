
public class Circle {
	private double radius;
	static final double PI = 3.141592;//PI라는 이름으로 3.141592로 초기화된 정적 상수
	
	//1. 원의 반지름을 매개 변수로 받는 생성자를 작성하라.
	Circle(double radius) {
		this.radius = radius;
	}
	//2. 매개 변수가 없는 생성자로서 원의 반지름을 0.0으로 설정한다.
	
	//3. 설정자 메소드인 setRadius()를 작성한다.
	void setRadius (double radius) {
		this.radius = radius;
	}
	//4. 접근자 메소드인 getRadius()를 작성한다.
	double getRadius() {
	return radius;	
	}
	//5. double형의 값을 제곱하여 반환하는 square() 메소드를 작성한다. 전용 메소드로 선언하라.
	private double square(double n) {
		return n * n;
	}
	//6. 원의 면적을 계산하는 getArea() 메소드를 작성한다.
	
	//7. 원의 둘레를 계산하는 getPerimeter() 메소드를 작성한다.
	double getPerimeter() {
		return 2 * PI * radius;
	}
	//8. PI값을 반환하는 정적 메소드 getPI() 메소드를 작성한다.
	static double getPI() {
		return PI;
	}
	//9. Circle 클래스 안에 main()을 추가하고 다음과 같이 square() 메소드를 호출하여 보자. 어떤 결과가 발생하가? 또 그 이유는 무엇인가?
	public static void main(String args[]) {
		square(10.0);
		//10. main() 안에서 정적 메소드인 getPI()를 호출하여 보라.
		Circle c1 = new Circle();
		c1.square(10.0);
		getPI();
		//11. Circle 클래스를 테스트하기 위하여 별도의 클래스인 CircleTest 클래스를 작성하라. main() 안에서 Circle 객체를 생성하고 getArea()와 getPerimeter()를 호출하여서 원의 면적과 둘레를 구하라.
		Circle c1 = new Circle(5.0);
		System.out.println("원의 넓이: " + c1.getArea());
		System.out.println("원의 둘레: " + c1.getPerimeter());
		
		Circle.radius = 10.0;
		Circle.square(20.6);
		//12. CircleTest 클래스 안에서 다음과 같이 radius를 참조하여 보라. 어떤 결과가 나오는가? 그 이유는?
		
		//13. 필드 radius의 수식자인 private를 제거하고 12번을 다시 하여 보자. 어떤 결과가 나오는가? 그 이유는?
		
		//14. 필드 radius의 수식자를 public으로 변경하고 12번을 다시 하여 보자. 어떤 결과가 나오는가? 그 이유는?
		
		//15. 전용 메소드인 square()를 다음과 같이 호출하여 보자. 어떤 결과가 나오는가? 그 이유는?
		
		
	}
}
