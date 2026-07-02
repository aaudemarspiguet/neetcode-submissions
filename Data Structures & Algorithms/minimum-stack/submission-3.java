class MinStack {
    ArrayList<Integer> stack;
    ArrayList<Integer> minStack;

    public MinStack() {
        stack = new ArrayList<Integer>();
        minStack = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        stack.add(val);
        if (minStack.isEmpty() || val < minStack.getLast()) {
            minStack.add(val);
        } else {
            minStack.add(minStack.getLast()); // carry min at previous state over to new
        }
    }
    
    public void pop() {
        stack.removeLast();
        minStack.removeLast();
        
    }
    
    public int top() {
        return stack.getLast();
        
    }
    
    public int getMin() {
        return minStack.getLast();
    }
}
