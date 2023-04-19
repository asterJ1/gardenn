class Numbers {
    int num[];
    Numbers(int num[]) {              // 생성자
        this.num = num;
    }
    int getTotal() {                  // 배열의 합계를 구하는 메서드
        int total = 0;
        for (int cnt = 0; cnt < num.length; cnt++) 
            total += num[cnt];
        return total;
    }
}
