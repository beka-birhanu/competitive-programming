# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

public class MyLinkedList 
{
    int capacity;
    int size;
    int[] values;

    public MyLinkedList() 
    {
        this.capacity = 1;
        this.size = 0;
        this.values = new int[capacity];
    }

    public void Resize(bool increase = true, int index = -1)
    {
        if(increase) this.capacity *= 2;
        else this.capacity = this.size + 1;

        int[] newArr = new int[this.capacity];

        for(int i = 0; i < this.size; i++)
        {
            if(i >= index && index != -1) newArr[i + 1] = values[i];
            else newArr[i] = values[i];
        }

        this.values = newArr;
    }

    public void Swap(int index)
    {
        for(int i = this.size; i >= index; i--) this.values[i + 1] = this.values[i];
    }

    public void DeSwap(int index)
    {
        for(int i = index; i < this.size - 1; i++) this.values[i] = this.values[i + 1];

        this.values[this.size - 1] = 0;
    }
    
    public int Get(int index) 
    {
        if(index < 0 || index > size - 1) return -1;
        else return values[index];
    }
    
    public void AddAtHead(int val) 
    {
        if(this.size + 1 == this.capacity) Resize(true, 0);
        else Swap(0);

        this.values[0] = val;
        this.size++;
    }
    
    public void AddAtTail(int val) 
    {
        if(this.size + 1 == this.capacity) Resize();

        this.values[this.size] = val;
        this.size++;
    }
    
    public void AddAtIndex(int index, int val) 
    {
        if(index > this.size) return;

        if(this.size + 1 == this.capacity) Resize(true, index);
        else Swap(index);

        this.values[index] = val;
        this.size++;
    }
    
    public void DeleteAtIndex(int index) 
    {
        if(index > this.size - 1) return;

        DeSwap(index);
        this.size--;

        if(this.size == capacity / 2) Resize(false);
    }
}