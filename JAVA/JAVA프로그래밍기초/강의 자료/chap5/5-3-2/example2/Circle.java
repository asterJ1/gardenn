class Circle {
    private  double radius;
    Circle(double radius) {
         this.radius = radius;
    }
    double getArea() {
         double area;
         area = radius * radius * 3.14;
         return area;
    }
   double getRadius(){
	return radius;
   }
   void  setRadius(double radius){
          this.radius = radius;
   }
  
}
