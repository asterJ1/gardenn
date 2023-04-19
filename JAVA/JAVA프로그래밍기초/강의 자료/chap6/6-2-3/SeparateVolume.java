class SeparateVolume implements Lendable  {
    String requestNo;      // û����ȣ
    String bookTitle;      // ����
    String writer;         // ����
    String borrower;       // ������
    String checkOutDate;   // ������
    byte state;            // �������
    SeparateVolume(String requestNo, String bookTitle, String writer) {
        this.requestNo = requestNo;
        this.bookTitle = bookTitle;
        this.writer = writer;
    }
    public void checkOut(String borrower, String date) {
        if (state != STATE_NORMAL)
            return;
        this.borrower = borrower;
        this.checkOutDate = date;
        this.state = STATE_BORROWED;
        System.out.println("*" + bookTitle + " ��(��) ����Ǿ����ϴ�.");
        System.out.println("������:" + borrower);
        System.out.println("������:" + date + "\n");    
    }
    public void checkIn() {
        this.borrower = null;
        this.checkOutDate = null;
        this.state = STATE_NORMAL;
        System.out.println("*" + bookTitle + " ��(��) �ݳ��Ǿ����ϴ�.\n");
    }
}
