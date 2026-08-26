# 1. Define dimensions
logical_width = 2
logical_height = 2
scale = 3  # Each room is a 3x3 block of characters

# 2. Create the blank canvas (a list of lists filled with spaces)
visual_width = logical_width * scale
visual_height = logical_height * scale
canvas = [[" " for _ in range(visual_width)] for _ in range(visual_height)]

# 3. Iterate through the logical grid
for logical_y in range(logical_height):
    for logical_x in range(logical_width):
        
        # Translate logical coordinates to visual starting coordinates
        # This finds the top-left corner of the current room's 3x3 block
        vis_x = logical_x * scale
        vis_y = logical_y * scale
        
        # 4. "Paint" the characters onto the canvas using the visual coordinates
        # Draw the four corners
        canvas[vis_y][vis_x] = "+"                 # Top-Left
        canvas[vis_y][vis_x + 2] = "+"             # Top-Right
        canvas[vis_y + 2][vis_x] = "+"             # Bottom-Left
        canvas[vis_y + 2][vis_x + 2] = "+"         # Bottom-Right
        
        # Draw the center
        canvas[vis_y + 1][vis_x + 1] = "C"

# 5. Render to terminal
for row in canvas:
    # Join the list of characters into a single string and print
    print("".join(row))