class StringHandler:
    
    def getString(self):
        self.text = input()
    
    def printString(self):
        print(self.text.upper())


# объект жасаймыз
obj = StringHandler()

# методтарды шақырамыз
obj.getString()
obj.printString()
