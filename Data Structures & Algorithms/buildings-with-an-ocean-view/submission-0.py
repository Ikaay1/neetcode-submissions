class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        
        we aren't guaranteed a sorted heights

        if heights == [], return []?? -> []


        computing a max_array at a given index from behind
        input = [1,3,2,4,2,5,1]
        
        max_heights at first = [1,1,1,1,1,1,1]

        max_heights at first = [5,5,5,5,5,5,1]



        """

        # if not heights:
        #     return []

        max_heights = [heights[-1]] * len(heights)

        for height_index in range(len(max_heights)-2, -1, -1):

            cur_height = heights[height_index]
            max_heights[height_index] = max(cur_height, max_heights[height_index+1])
        
        ocean_view_buildings = []
        for height_index in range(len(heights)-1): 

            if heights[height_index] > max_heights[height_index+1]:
                ocean_view_buildings.append(height_index)
        
        ocean_view_buildings.append(len(heights)-1)

        return ocean_view_buildings