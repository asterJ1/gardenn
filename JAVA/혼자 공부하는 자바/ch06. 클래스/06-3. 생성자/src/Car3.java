
public class Car3 {
	String company = "Hyundae";
	String model;
	String color;
	int maxSpeed;
	
	Car3() {
	}
	
	Car3(String model) {
		this(model, "silver", 250);
	}
	
	Car3(String model, String color) {
		this(model, color, 250);
	}
	
	Car3(String model, String color, int maxSpeed) {
		this.model = model;
		this.color = color;
		this.maxSpeed = maxSpeed;
	}
}
