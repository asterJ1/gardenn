class ConstrExample1 {
    public static void main(String args[]) {
        GoodsStock obj;                        
        obj = new GoodsStock("52135", 200);      // 선언된 생성자를 이용해서 객체를 생성
        System.out.println("상품코드:" + obj.goodsCode);  
        System.out.println("재고수량:" + obj.stockNum);   
        obj.addStock(1000);                               
        System.out.println("상품코드:" + obj.goodsCode);  
        System.out.println("재고수량:" + obj.stockNum);   
    }
}
