class Accumulator {
    int total = 0;
    static int grandTotal = 0;        // ���� �ʵ带 �����ϴ� ����
    void accumulate(int amount) {
        total += amount;
        grandTotal += amount;         // ���� �ʵ忡 amount �Ķ���� ���� ���ϴ� ���Թ�
    }
}
