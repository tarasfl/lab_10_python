class Node:
    elements = []

    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key
        # values
        self.i_k_max = None
        self.type_of_transistor = None
        self.u_k_max = None

    def add_element_by_key(self, key):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key)
                    return self.left
                else:
                    return self.left.add_element_by_key(key)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key)
                    return self.right
                else:
                    return self.right.add_element_by_key(key)
        else:
            self.key = key
            return self

    def add_element_with_i_k_max(self, key, i_k_max):
        element = self.add_element_by_key(key)
        element.i_k_max = i_k_max

    def delete_element(self, key):
        element = self.find_by_key(key)  # element to delete
        parrent = self.find_parent(key)  # parent of the element to delete

        if element and parrent is not None:
            # change with the least element from right
            if element.right is not None:
                new_element = element.right.find_most_left()

                if parrent.left is element:
                    parrent.left = new_element
                else:
                    parrent.right = new_element

                new_element.left = element.left
                new_element.right = element.right
                element.left = None
                element.right = None

                if new_element.right is not None:
                    new_parrent = element.find_parent(new_element.key)
                    if new_parrent is not None:
                        new_parrent.left = new_element.right
                    else:
                        print("Error: cannot find a parrent node for", element.key)

                new_element.right = element.right
                element.right = None
                del element
            elif element.left is not None:
                new_element = element.left
                if parrent.left == element:
                    parrent.left = new_element
                else:
                    parrent.right = new_element

                element.left = None
                del element
            else:
                if parrent.left == element:
                    parrent.left = None
                else:
                    parrent.right = None
                del element

        elif parrent is None:
            if element.right is not None:
                new_element = element.right.find_most_left()
                new_parrent = self.find_parent(new_element.key)  # node in which change reference

                element.key = new_element.key
                if new_element.right is not None:
                    if new_parrent is not None:
                        new_parrent.left = new_element.right
                new_element.key = None
                new_element.left = None
                new_element.right = None
                del new_element

    def print_all_elements(self):
        print(self.key)
        if self.left:
            self.left.print_all_elements()

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

    def find_parent(self, key):
        if self.key:
            if key == self.key:
                return None
            elif key < self.key and self.left is not None:
                if key == self.left.key:
                    return self
                else:
                    return self.left.find_parent(key)
            elif key > self.key and self.right is not None:
                if key == self.right.key:
                    return self
                else:
                    return self.right.find_parent(key)
        else:
            return None

    def find_most_left(self):
        if self.left is None:
            return self
        else:
            return self.left.find_most_left()

    def get_data_of_element(self, key):
        element = self.find_by_key(key)
        return element.key, "  ", element.i_k_max

    def traversal(self):
        print(self.key)
        if self.left:
            self.left.traversal()
        if self.right:
            self.right.traversal()

    def bottom_to_top_traversal(self):
        if self.left:
            self.left.traversal()
        if self.right:
            self.right.traversal()
        print(self.key)

    def delete_all_elements_by_type(self, type_of_transistor, root):
        if self.left:
            self.left.delete_all_elements_by_type(type_of_transistor, root)
        if self.right:
            self.right.delete_all_elements_by_type(type_of_transistor, root)

        if self.type_of_transistor == type_of_transistor:
            root.delete_element(self.key)

    def print_elements_by_params(self, i_k_max, u_k_max):
        if self.i_k_max == i_k_max and self.u_k_max == u_k_max:
            print(self.key)
        if self.left:
            self.left.print_elements_by_params(i_k_max, u_k_max)

        if self.right:
            self.right.print_elements_by_params(i_k_max, u_k_max)

    def destroy(self, root):
        if self.left:
            self.left.destroy(root)
            root.delete_element(self.left.key)

        if self.right:
            self.right.destroy(root)
            root.delete_element(self.right.key)


if __name__ == '__main__':
    root = Node(20)
    root.add_element_with_i_k_max(10, 8)
    el8 = root.add_element_by_key(8)
    el9 = root.add_element_by_key(9)
    el9.i_k_max = 10
    el8.i_k_max = 10
    el9.u_k_max = 10
    el8.u_k_max = 10
    el9.type_of_transistor = "p-n-p"
    el8.type_of_transistor = "p-n-p"
    root.add_element_by_key(7)
    root.add_element_by_key(40)
    root.add_element_by_key(30)
    root.add_element_by_key(35)
    root.add_element_by_key(34)
    root.add_element_by_key(33)
    root.add_element_by_key(31)
    root.add_element_by_key(32)
    root.delete_all_elements_by_type("p-n-p", root)
    root.traversal()
