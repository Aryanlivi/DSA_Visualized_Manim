from manim import *
from utils.Common import initiate_array,create_boxes,create_pointer,swap_boxes
class QuickSortManim(Scene):
    def construct(self):
        nums=[25,57,48,37,12,92,86,33]
        boxes=initiate_array(self,nums)
        self.quicksort(boxes, nums, 0, len(nums)-1)

    def partition(self, boxes, nums, left, right):
        i = left
        j = right


        left_pointer = create_pointer(boxes[i], color=GREEN, label="i")
        right_pointer = create_pointer(boxes[j], color=BLUE, label="j")

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
                swap_boxes(self,boxes, i, j, nums)
                self.wait(0.5)

        # Swap pivot with nums[j]
        swap_boxes(self,boxes, left, j, nums)
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

    

    

