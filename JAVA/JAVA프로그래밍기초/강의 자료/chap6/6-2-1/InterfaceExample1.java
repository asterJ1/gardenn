class InterfaceExample1 {
    public static void main(String args[]) {
        SeparateVolume obj1 = new SeparateVolume("863��774��", "����", 
                                                 "��������");
        AppCDInfo obj2 = new AppCDInfo("2005-7001", "Redhat Fedora");
        obj1.checkOut("�迵��", "20060315");     
        obj2.checkOut("�����", "20060317");     
        obj1.checkIn();     
        obj2.checkIn();     
    }
}
