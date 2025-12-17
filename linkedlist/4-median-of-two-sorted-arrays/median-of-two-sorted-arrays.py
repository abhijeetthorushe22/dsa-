
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_length = m + n
        half_length = total_length // 2
        
        # Binary search on the smaller array
        left, right = 0, m
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half_length - partition1
            
            # Find left and right boundaries of partitions
            max_left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            min_right1 = nums1[partition1] if partition1 < m else float('inf')
            
            max_left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            min_right2 = nums2[partition2] if partition2 < n else float('inf')
            
            # Check if the partitions are valid
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Odd total length
                if total_length % 2:
                    return min(min_right1, min_right2)
                # Even total length
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1 > min_right2:
                # Move left in nums1
                right = partition1 - 1
            else:
                # Move right in nums1
                left = partition1 + 1

        