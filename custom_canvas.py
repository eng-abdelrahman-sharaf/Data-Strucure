import tkinter as tk

class Custom_Canvas(tk.Canvas):
  """Custom canvas class for drawing circles and lines."""

  def draw_number(self, number: float, x: float, y: float, radius: float = 20) -> None:
    """Draws a circle with a number label at the specified position.

    Args:
      number: The number to display.
      x: The x-coordinate of the center.
      y: The y-coordinate of the center.
      radius: The radius of the circle (default: 20).
    """
    
    points = ((x - radius, y - radius), (x + radius, y + radius))
    self.create_oval(points, outline="black", fill="white")
    self.create_text(x, y, text=str(number), fill="black", font="Arial 18")  # Use Arial font

  def join_2_numbers(self, x1: float, y1: float, x2: float, y2: float, width=4, fill="black") -> None:
    """Draws a line connecting two points.

    Args:
      x1, y1: Coordinates of the first point.
      x2, y2: Coordinates of the second point.
      width: Width of the line (default: 4).
      fill: Color of the line (default: black).
    """

    line_id = self.create_line(x1, y1, x2, y2, width=width, fill=fill)
    self.tag_lower(line_id)
