from manim import *

def initiate_array(scene,array):
        boxes = create_boxes(array)

        # Animate the creation of the array
        scene.play(*[Create(box) for box in boxes])
        scene.wait(1)
        return boxes
def create_boxes(array):
        boxes = []
        total_boxes = len(array)

        # Dynamically calculate the spacing and starting position
        spacing = 1.5  
        max_width = config.frame_width - 2  
        # Adjust start position for visibility
        start_x = -(min(total_boxes * spacing, max_width) / 2) + spacing / 2  

        for i, num in enumerate(array):
            box = Square(side_length=1.5).move_to(ORIGIN + RIGHT * (start_x + i * spacing))
            text = Text(str(num)).move_to(box.get_center())
            box.add(text)
            boxes.append(box)
        return boxes

def create_pointer(box, color, label):
        pointer = Arrow(start=UP, end=DOWN, color=color).next_to(box, DOWN)
        text = Text(label, color=color).next_to(pointer, DOWN)
        pointer.add(text)
        return pointer

def swap_boxes(scene,boxes, i, j, nums):
        box1 = boxes[i]
        box2 = boxes[j]

        # Animate the swap
        scene.play(box1.animate.move_to(box2.get_center()), box2.animate.move_to(box1.get_center()))

        # Swap the numbers in the array and boxes
        nums[i], nums[j] = nums[j], nums[i]
        boxes[i], boxes[j] = boxes[j], boxes[i]  
