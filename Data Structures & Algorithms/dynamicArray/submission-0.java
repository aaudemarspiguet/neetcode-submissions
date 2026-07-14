class DynamicArray {
    int[] arr;
    int size;

    public DynamicArray(int capacity) {
        arr = new int[capacity];
        size = 0;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (size == arr.length) {
            this.resize();
        }
        arr[size] = n;
        size++;
    }

    public int popback() {
        int element = arr[size - 1];
        arr[size - 1] = 0;
        size--;

        return element;
    }

    private void resize() {
        int[] new_arr = new int[2 * arr.length];
        for (int i = 0; i < new_arr.length; i++){
            if (i < arr.length) {
                new_arr[i] = arr[i];
            } else {
                new_arr[i] = 0; // fill zero for rest
            }
        }

        arr = new_arr; // point to new array
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return arr.length;
    }
}
