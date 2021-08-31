class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        if self.head is None and self.tail is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head,None)
        self.head = node
        self.tail = self.head.next

    def insert_at_end(self, data):
        if self.head is None and self.tail is None:
            self.head = Node(data,None,None)
            self.tail = self.head

            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None,itr)
        self.tail = itr.next

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next,itr.prev)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        self.tail = None

        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self,data_after, data_to_insert):
    	if self.head is None:
    		return

    	count = 0
    	itr = self.head
    	while itr:
    		if itr.data == data_after:
    			self.insert_at(count+1,data_to_insert)
    			break
    		itr = itr.next
    		count+=1

    def remove_by_value(self, data):
    	if self.head is None and self.tail is None:
    		return

    	count = 0
    	itr = self.head

    	while itr:
    		if itr.data == data:
    			self.remove_at(count)
    		itr = itr.next
    		count+=1

    def print_forward(self):
        if self.head is None and self.tail is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.tail is None and self.head is None:
            print("Linked list is empty")
            return

        itr = self.tail
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(llstr)




if __name__ == '__main__':
    ll = DLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()

