from custom_canvas import Custom_Canvas

class Node:
  """Represents a node in a binary tree."""

  def __init__(self, key: int) -> None:
    """Initializes a new node.

    Args:
      key: The key value associated with the node.
    """

    self.key: int = key
    self.height: int = 1
    self.balance: int = 0
    self.left: Node = None
    self.right: Node = None

  @staticmethod
  def height(node):
    """Returns the height of a node, or 0 if the node is None.

    Args:
      node: The node for which to calculate the height.

    Returns:
      The height of the node.
    """

    if node:
      return node.height
    return 0

class BST:
    """Represents a Binary Search Tree (BST)."""

    def __init__(self) -> None:
        """Initializes an empty BST."""

        self.root = None

    def _recalc_height_balance(self, node : Node):
        """Recalculates the height and balance factor of a node.

        Args:
        node: The node for which to update height and balance.
        """

        node.height = max(Node.height(node.left), Node.height(node.right)) + 1
        node.balance = Node.height(node.left) - Node.height(node.right)

    def insert(self, key: int):
        """Inserts a new key into the BST.

        Args:
        key: The key to be inserted.

        Raises:
        ValueError: If the key already exists in the BST.
        """

        self.root = self._insert_helper(self.root, key)
        
    def _insert_helper(self , node : Node , inserted_key : int):
        """Inserts a key recursively into the BST.

        Args:
            node: The current node in the recursive search.
            inserted_key: The key to be inserted.

        Returns:
            The updated root node of the BST.
        """

        if node == None : return Node(inserted_key)
        if node.key == inserted_key : raise ValueError (f"Duplicated Key {node.key}")

        if node.key < inserted_key : 
            node.right = self._insert_helper(node.right , inserted_key)

        else : 
            node.left = self._insert_helper(node.left , inserted_key)

        self._recalc_height_balance(node)

        return node

    def visualize(self , TK_window , canvas:Custom_Canvas):
        """Visualizes the BST on a Tkinter canvas.

        Args:
            TK_window: The Tkinter window object.
            canvas: The Custom_Canvas object for drawing the tree.
        """

        self._visualize_helper(self.root , TK_window , canvas , 100 , 100 ,  canvas.winfo_reqwidth()  , 0)

    def _visualize_helper(self , node : Node , Tk_window ,  canvas:Custom_Canvas, x, y, width , level):
        """Helper function for visualizing the BST recursively.

        Args:
            node: The current node in the BST.
            Tk_window: The Tkinter window object.
            canvas: The Custom_Canvas object for drawing the tree.
            x: X-coordinate of the current node's position.
            y: Y-coordinate of the current node's position.
            width: Width of the subtree rooted at the current node.
            level: Depth level of the current node in the tree.
        """

        shift_x = (width / 4)  

        if(not node) : return

        canvas.draw_number(node.key , x , y , 20)

        if node.left:
            self._visualize_helper(node.left , Tk_window , canvas, x-shift_x , y + 50 , width / 2, level+1 )
            canvas.join_2_numbers(x , y , x-shift_x , y + 50)
        
        if node.right:
            self._visualize_helper(node.right, Tk_window ,canvas, x+shift_x , y + 50, width / 2 , level+1 )
            canvas.join_2_numbers(x , y , x+shift_x , y + 50)

    def _visualize_insertion(self , key : int , TK_window , canvas : Custom_Canvas):
        """Visualizes the insertion of a single key into the BST.

        Args:
            key: The key to be inserted.
            TK_window: The Tkinter window object.
            canvas: The Custom_Canvas object for drawing the tree.
        """
        
        self.insert(key)
        self.visualize(TK_window , canvas)
    
    def visualize_insertions(self, iterable , TK_window , canvas:Custom_Canvas , delay = 1000):
        """Visualizes the insertion of multiple keys from an iterable in an animated way.

        Args:
            iterable: The iterable containing keys to be inserted (e.g., list, tuple).
            TK_window: The Tkinter window object.
            canvas: The Custom_Canvas object for drawing the tree.
            delay: The delay (in milliseconds) between visualizing each insertion (default 1000).
        """

        for i , key in enumerate(iterable):
            TK_window.after(delay * (i+1) , self._visualize_insertion , key , TK_window , canvas)