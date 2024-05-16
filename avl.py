from bst import BST,Node
from custom_canvas import Custom_Canvas



class AVL (BST):
    """Implements an AVL (Adelson-Velsky and Landis) tree, a self-balancing binary search tree.

    An AVL tree is a BST that maintains a height balance property. This property ensures that
    the height difference between any two subtrees of a node is at most 1. This property allows
    for efficient search, insertion, and deletion operations with a guaranteed logarithmic time complexity
    in the average and worst cases.

    This class inherits from the `BST` class and overrides the `_insert_helper` method to
    perform AVL-specific rebalancing operations after insertion.
    """

    def _rotate_right(self , node : Node):
        """Performs a right rotation on a given node in the AVL tree.

        Args:
        node: The node on which to perform the right rotation.

        Returns:
        The new root node after the rotation.
        """

        temp = node.left.right
        node.left.right = node
        node = node.left
        node.right.left = temp
        self._recalc_height_balance(node.right)
        self._recalc_height_balance(node)
        return node

    def _rotate_left(self , node : Node):
        """Performs a left rotation on a given node in the AVL tree.

        Args:
        node: The node on which to perform the left rotation.

        Returns:
        The new root node after the rotation.
        """

        temp = node.right.left
        node.right.left = node
        node = node.right
        node.left.right = temp
        self._recalc_height_balance(node.left)
        self._recalc_height_balance(node)
        return node

    def _rotate_right_left(self , node : Node):
        """Performs a double rotation: right rotation on the right child followed by a left rotation
        on the current node.

        Args:
        node: The node on which to perform the double rotation.

        Returns:
        The new root node after the double rotation.
        """
        node.right = self._rotate_right(node.right)
        node = self._rotate_left(node)
        return node

    def _rotate_left_right(self):
        """Performs a double rotation: left rotation on the left child followed by a right rotation
        on the current node.

        Args:
        node: The node on which to perform the double rotation.

        Returns:
        The new root node after the double rotation.
        """

        node.left = self._rotate_right(node.left)
        node = self._rotate_left(node)
        return node

    def _insert_helper(self , node : Node , inserted_key : int):
        """Inserts a new key into the AVL tree recursively, performing rebalancing operations as needed.

        Args:
        node: The current node in the recursive search.
        inserted_key: The key to be inserted.

        Returns:
        The updated root node of the AVL tree.

        Raises:
        ValueError: If the key already exists in the AVL tree.
        """

        if node == None : return Node(inserted_key)
        if node.key == inserted_key : raise ValueError ("repeated key")

        if node.key < inserted_key : 
            node.right = self._insert_helper(node.right , inserted_key)

        else : 
            node.left = self._insert_helper(node.left , inserted_key)

        self._recalc_height_balance(node)

        if node.balance < -1:
            if inserted_key > node.right.key : 
                node = self._rotate_left(node)
            else:
                node = self._rotate_right_left(node)
        elif node.balance > 1:
            if inserted_key < node.left.key:
                node = self._rotate_right(node)
            else:
                node = self._rotate_left_right(node)
        return node
    
    def visualize(self , TK_window , canvas:Custom_Canvas):
        """Visualizes the current state of the AVL tree on a Tkinter canvas.

        Args:
        TK_window: The Tkinter window object where the visualization will be displayed.
        canvas: The Custom_Canvas object (likely a subclass of `tkinter.Canvas`) used for
                drawing the tree on the window.
        """

        self._visualize_helper(self.root , TK_window , canvas , canvas.winfo_reqwidth() / 2 , 100 ,  canvas.winfo_reqwidth()  , 0)
 