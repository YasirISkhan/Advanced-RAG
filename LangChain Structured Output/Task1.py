class BSTIterator():
    def __init__(self, array):
        self.array = array
        self.root = self.array[0]
        self.numbers = []
        self.pointer = None
        for count in range(len(self.array)):
            if self.array[count] == None: 
                pass
            else:
                self.numbers.append(self.array[count])
        self.smallest = min(self.numbers)
        self.pointer = self.smallest - 1

    def hasNext(self):
        if len(self.numbers) > 0:
            if self.numbers[0] > self.pointer:
                return True
            else:
                return False
        else:
            return False

    def next(self):
        
        self.pointer = self.numbers[self.root+]
        self.numbers.remove(self.pointer)
        return self.pointer


bstIterator = BSTIterator([10, 7, 20, None, None, 3, 30])
final_output = [None]
final_output.append(bstIterator.next())
final_output.append(bstIterator.next())
final_output.append(bstIterator.hasNext())
final_output.append(bstIterator.next())
final_output.append(bstIterator.hasNext())
final_output.append(bstIterator.next())
final_output.append(bstIterator.hasNext())
final_output.append(bstIterator.next())
final_output.append(bstIterator.hasNext())
print(final_output)