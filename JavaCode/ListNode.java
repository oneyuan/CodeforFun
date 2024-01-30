import java.util.Objects;
import java.util.function.Predicate;

public class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }

    ListNode(int x, ListNode node) {
        val = x;
        next = node;
    }

    public static ListNode createList(int... values) {
        ListNode head = new ListNode(values[0]);
        ListNode prev = head;
        for (int i = 1; i < values.length; i++) {
            prev.next = new ListNode(values[i]);
            prev = prev.next;
        }
        return head;
    }

    public ListNode filter(Predicate<ListNode> f) {

        ListNode node = this;
        while (node != null && !f.test(node)) {
            node = node.next;
        }
        return node;
    }

    @Override
    public String toString() {

        return val + "->" + next;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        ListNode listNode = (ListNode) o;
        return val == listNode.val &&
                Objects.equals(next, listNode.next);
    }

    @Override
    public int hashCode() {
        return Objects.hash(val, next);
    }
}
