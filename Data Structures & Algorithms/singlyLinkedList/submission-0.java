public class LinkedList {

    // head of the LinkedList
    Node head, tail;
    int length;
    
    // construct a linked list with head and tail pointers
    public LinkedList() {
        head = null;
        tail = head;
        length = 0;
    }

    // return value of node at i-th index, -1 otherwise
    public int get(int index) {

        if (index < 0 || index >= length) { // check bounds
            return -1;
        } else if (index == 0) {    // case 1: return head in O(1)
            return head.val;
        } else if (index == length - 1) { // case 2: return tail in O(1)
            return tail.val;
        }

        /* case 3: iterate through the list; O(n) */

        Node curr = head;
        int count = 0;
        while (curr != null && count < index) {
            curr = curr.next;
            count++;
        }
        return curr.val;
    }

    // inserts a node with val at head of the list
    public void insertHead(int val) {
        Node node = new Node(val, null);

        // if length = 0, ie, inserting for the first time, then head = tail = new node
        if (length == 0) {
            head = node;
            tail = head;
        } else {
            node.next = head;
            head = node;
        }

        length++; // increment size of list
    }

    // inserts a node with val at tail of the list
    public void insertTail(int val) {
        Node node = new Node(val, null);

        // if length = 0, ie, inserting for the first time, then head = tail = new node
        if (length == 0) {
            tail = node;
            head = tail;
        } else {
            tail.next = node;
            tail = node;
        }
        length++;

    }

    // remove node at i-th index; if index out of bounds return false, otherwise true
    public boolean remove(int index) {
        if (index < 0 || index >= length) { // check bounds
            return false;
        }
        
        if (index == 0) {    // case 1: remove from head
            head = head.next;
        } else if (index == length - 1) { // case 2: remove from tail
            Node curr = head;
            while (curr.next != tail) {
                curr = curr.next;
            }
            tail = curr;
        } else { // case 3: remove from middle of list
            Node prev = head;
            int i = 0;
            while (i < index - 1){
                prev = prev.next;
                i++;
            }
            prev.next = prev.next.next; // skip over node at index index i
        }

        length--;
        return true;

    }

    // return all values from head to tail stored as an ArrayList object
    public ArrayList<Integer> getValues() {
        ArrayList<Integer> arr = new ArrayList<>();

        Node curr = head;
        while (curr != null) {
            arr.add(curr.val);
            curr = curr.next;
        }

        return arr;
    }

    // inner class
    private static class Node {
        // instance variables of Node class
        int val;
        Node next;

        // Node constructor
        Node(int val, Node next) {
            this.val = val;
            this.next = next;
        }
    }
}
