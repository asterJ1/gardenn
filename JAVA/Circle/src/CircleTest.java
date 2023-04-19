
public class CircleTest {
	//11. Circle 클래스를 테스트하기 위하여 별도의 클래스인 CircleTest 클래스를 작성하라. main() 안에서 Circle 객체를 생성하고 getArea()와 getPerimeter()를 호출하여서 원의 면적과 둘레를 구하라.
	public static void main(String[] args) {
		Circle c1 = new Circle(5.0);
		System.out.println("원의 넓이: " + c1.getArea());
		System.out.println("원의 둘레: " + c1.getPerimeter());
		//12. CircleTest 클래스 안에서 다음과 같이 radius를 참조하여 보라. 어떤 결과가 나오는가? 그 이유는?
		//c1.radius = 10.0;
		//12.answer: class Circle에서 radius를 private으로 작성하였기 때문.
		//13. 필드 radius의 수식자인 private를 제거하고 12번을 다시 하여 보자. 어떤 결과가 나오는가? 그 이유는?
		//13.answer: private를 제거한 후에는 외부 클래스에서 접근할 수 있으므로 오류가 발생하지 않음.
		//14. 필드 radius의 수식자를 public으로 변경하고 12번을 다시 하여 보자. 어떤 결과가 나오는가? 그 이유는?
		//14.answer: 수식자가 public으로 변경됨으로써 프로그램 내의 모든 함수들에게 공개되므로 오류가 발생하지 않음.		
		//15. 전용 메소드인 square()를 다음과 같이 호출하여 보자. 어떤 결과가 나오는가? 그 이유는?
		Circle c2 = new Circle(5.0);//객체 생성, 생성자 호출 시 반지름을 5.0으로 설
		//c2.square(20.6);//메소드 호출
		//15.answer: square() 메소드는 전용 메소드로 작성되었기 때문에, Circle 클래스 내의 메소드들에게만 공개됨. 그러므로 외부 클래스인 CircleTest 클래스에서는 오류가 발생함.
	}
	
}
