from manim import *

class QuickSortManim(Scene):
    def construct(self):
        nums = [25, 57, 48, 37, 12, 92, 86, 33]
        boxes = self.create_boxes(nums)

        # Animate the creation of the array
        self.play(*[Create(box) for box in boxes])
        self.wait(1)
        self.quicksort(boxes, nums, 0, len(nums)-1)

    def partition(self, boxes, nums, left, right):
        i = left
        j = right


        left_pointer = self.create_pointer(boxes[i], color=GREEN, label="i")
        right_pointer = self.create_pointer(boxes[j], color=BLUE, label="j")

        # Display the pointers
        self.play(Create(left_pointer), Create(right_pointer))
        self.wait(1)

        pivot = nums[left]

        # set pivot box to red
        pivot_box = boxes[left].copy().set_color(RED)
        self.play(pivot_box.animate.shift(UP * 2))
        self.wait(1)

        while i < j:
            while i < right and nums[i] <= pivot:
                i += 1
                if i <= right:
                    self.play(left_pointer.animate.next_to(boxes[i], DOWN))
                self.wait(0.5)
                
            while j > left and nums[j] > pivot:
                j -= 1
                if j >= left:
                    self.play(right_pointer.animate.next_to(boxes[j], DOWN))
                self.wait(0.5)
                
            if i < j:
                self.swap_boxes(boxes, i, j, nums)
                self.wait(0.5)

        # Swap pivot with nums[j]
        self.swap_boxes(boxes, left, j, nums)
        self.wait(1)

        # Clear pointers and pivot
        self.play(FadeOut(left_pointer), FadeOut(right_pointer), FadeOut(pivot_box))
        self.wait(1)

        return j

    def quicksort(self, boxes, nums, left, right):
        if left < right:
            pivot_pos = self.partition(boxes, nums, left, right)
            self.quicksort(boxes, nums, left, pivot_pos - 1)
            self.quicksort(boxes, nums, pivot_pos + 1, right)

    def create_boxes(self, array):
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

    def create_pointer(self, box, color, label):
        pointer = Arrow(start=UP, end=DOWN, color=color).next_to(box, DOWN)
        text = Text(label, color=color).next_to(pointer, DOWN)
        pointer.add(text)
        return pointer

    def swap_boxes(self, boxes, i, j, nums):
        box1 = boxes[i]
        box2 = boxes[j]

        # Animate the swap
        self.play(box1.animate.move_to(box2.get_center()), box2.animate.move_to(box1.get_center()))

        # Swap the numbers in the array and boxes
        nums[i], nums[j] = nums[j], nums[i]
        boxes[i], boxes[j] = boxes[j], boxes[i]  
