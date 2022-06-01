class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key
        self.i_k_max = None

    def add_element_by_key(self, key):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key)
                    return self.left
                else:
                    self.left.add_element_by_key(key)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key)
                    return self.right
                else:
                    self.right.add_element_by_key(key)
        else:
            self.key = key
            return self

    def add_element_with_i_k_max(self, key, i_k_max):
        element = self.add_element_by_key(key)

    def delete_element(self, key):
        element = self.find_by_key(key)
        if element is not None:
            if element.right is not None:
                current_element = element.right
                while current_element.left is not None:
                    current_element = current_element.left
                element.key = current_element.key
                if current_element.right is not None and element is not self:
                    current_element.replace(current_element.right)
            else:
                if element.left is not None:
                    element.replace(element.left)
        else:
            print("there is no such element")

    def print_all_elements(self):
        if self.left:
            self.left.print_all_elements()
        print(self.key, " ", self.left, '  ', self.right)
        if self.right:
            self.right.print_all_elements()

    def find_by_key(self, key):
        if self.key:
            if key == self.key:
                return self
            elif key < self.key:
                if self.left is None:
                    return None
                else:
                    return self.left.find_by_key(key)
            elif key > self.key:
                if self.right is None:
                    return None
                else:
                    return self.right.find_by_key(key)
        else:
            return None

    def get_data_of_element(self, key):
        element = self.find_by_key(key)
        return element.key, "  ", element.i_k_max

    def bypass_tree(self):
        pass

    def delete_all_elements_by_type(self, type_of_transistor):
        pass

    def replace(self, obj):
        self.key = obj.key
        if self.right is not None:
            self.right = obj.right
        elif self.left is not None:
            self.left = obj.left
        del obj


if __name__ == '__main__':
    root = Node(20)
    root.add_element_by_key(10)
    root.add_element_by_key(40)
    root.add_element_by_key(30)
    root.add_element_by_key(35)
    root.add_element_by_key(34)
    root.add_element_by_key(33)
    root.add_element_by_key(31)
    root.add_element_by_key(32)
    root.print_all_elements()
    print(root.delete_element(20))
    print("-----------")
    root.print_all_elements()
   # print(root.find_by_key(30).right.key)
