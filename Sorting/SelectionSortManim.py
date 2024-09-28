
from manim import *
from utils.Common import *
class SelectionSortManim(Scene):
    def construct(self):
        nums=[25,57,48,37,12,92,86,33]
        boxes=initiate_array(self,nums)
        self.SelectionSort(boxes,nums)
    def SelectionSort(self,boxes,nums):
        initial_pointer = create_pointer(boxes[0], color=RED, label="i")
        min_pointer=create_pointer(boxes[0], color=GREEN, label="min")
        # Display the pointers
        self.play(Create(initial_pointer), Create(min_pointer))
        self.wait(1)
        for i in range(0,len(nums)):
            min_index=i
            self.play(initial_pointer.animate.next_to(boxes[i], DOWN))
            self.wait(0.5)
            self.play(min_pointer.animate.next_to(boxes[i], DOWN))
            self.wait(0.5)
            for j in range(i+1,len(nums)):
                self.play(min_pointer.animate.next_to(boxes[j], DOWN))
                self.wait(0.5)
                if(nums[j]<nums[min_index]):
                    min_index=j
            
            self.play(min_pointer.animate.next_to(boxes[min_index], DOWN))
            self.wait(0.5)  
            if(min_index!=i):
                swap_boxes(self,boxes,min_index,i,nums)
                # nums[min_index],nums[i]=nums[i],nums[min_index]
        return nums