class InterfaceExample3 {
    public static void main(String args[]) {
        SeparateVolume obj = new SeparateVolume("863��", "����", "��������");
        printState(obj);
        obj.checkOut("�̼���", "20060317");
        printState(obj);
    }
    static void printState(SeparateVolume  obj) {
        if (obj.state == Lendable.STATE_NORMAL) {
            System.out.println("------------------");
            System.out.println("�������: ���Ⱑ��");
            System.out.println("------------------");
        }
        if (obj.state == Lendable.STATE_BORROWED) {
            System.out.println("------------------");
            System.out.println("�������: ������");
            System.out.println("������: " + obj.borrower);
            System.out.println("������: " + obj.checkOutDate);
            System.out.println("------------------");
        }
    }
}
