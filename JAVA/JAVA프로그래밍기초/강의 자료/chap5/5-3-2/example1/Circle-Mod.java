class Circle {
    Circle(double radius) {
         this.radius = radius;
    }
    double getArea() {
         double area;
         area = radius * radius * 3.14;
         return area;
    }
    double radius;
}
