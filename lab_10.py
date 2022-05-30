class Node:
    def __init__(self, type_of_transistor, mark, i_k_max, u_k_max):
        self.right = None
        self.left = None
        self.type_of_transistor = type_of_transistor
        self.mark = mark
        self.i_k_max = i_k_max
        self.u_k_max = u_k_max

    def add_element(self, type_of_transistor, mark, i_k_max, u_k_max):
        if self.i_k_max:
            if i_k_max < self.i_k_max:
                if self.left is None:
                    self.left = Node(type_of_transistor, mark, i_k_max, u_k_max)
                    print("creating Node Left", self.i_k_max)
                else:
                    self.left.add_element(type_of_transistor, mark, i_k_max, u_k_max)
            elif i_k_max > self.i_k_max:
                if self.right is None:
                    self.right = Node(type_of_transistor, mark, i_k_max, u_k_max)
                    print("creating Node Right", self.i_k_max)
                else:
                    self.right.add_element(type_of_transistor, mark, i_k_max, u_k_max)
        else:
            self.i_k_max = i_k_max
            self.u_k_max = u_k_max
            self.mark = mark
            self.type_of_transistor = type_of_transistor

    def delete_element(self, type_of_transistor, mark, i_k_max, u_k_max):
        if self.i_k_max:
            if i_k_max > self.i_k_max:
                if self.right is None:
                    print("There is no such element")
                else:
                    print("reference right")
                    self.right.delete_element(type_of_transistor, mark, i_k_max, u_k_max)
            elif i_k_max < self.i_k_max:
                if self.left is None:
                    print("There is no such element")
                else:
                    print("reference left")
                    self.left.delete_element(type_of_transistor, mark, i_k_max, u_k_max)
            elif self.i_k_max == i_k_max and self.u_k_max == u_k_max and self.mark == mark \
                    and self.type_of_transistor == type_of_transistor:
                if self.right:
                    self.right = self.left
                    del self
                elif self.left:
                    self.left = self.right

    def print_all_elements(self):
        if self.left:
            self.left.print_all_elements()
        print(self.i_k_max, "  ", self.left, "  ", self.right),
        if self.right:
            self.right.print_all_elements()

    def find_by_key(self, key):
        pass

    def get_data_of_element(self):
        pass

    def bypass_tree(self):
        pass

    def delete_all_elements_by_type(self, type_of_transistor):
        pass


if __name__ == '__main__':
    root = Node("p-n-p", "ka-12", 20, 28)
    root.add_element("p-n-p", "kra-12", 54, 280)
    root.add_element("p-n-p", "kra-12", 44, 280)
    root.add_element("p-n-p", "kra-12", 14, 280)
    root.add_element("p-n-p", "kra-12", 104, 280)
    root.print_all_elements()
    root.delete_element("p-n-p", "kra-12", 44, 280)
    print("-------------")
    root.print_all_elements()
