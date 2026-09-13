class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        heights.append(0)
        max_area = 0

        for i, h in enumerate(heights):

            while st and heights[st[-1]] > h:
                index = st.pop()

                width = i if not st else i - st[-1] - 1
                max_area = max(max_area, heights[index] * width)
            st.append(i)
        return max_area