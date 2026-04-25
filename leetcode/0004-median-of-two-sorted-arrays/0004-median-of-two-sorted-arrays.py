class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        self.oneidx, self.twoidx = 0, 0
        self.even = (len1 + len2) % 2 == 0

        def findmed(med):
            av1, av2 = len1 - self.oneidx, len2 - self.twoidx
            half = math.ceil(med/2)

            if med == 1 and av1 != 0 and av2 != 0:
                if self.even:
                    self.even = False
                    if nums1[self.oneidx] <= nums2[self.twoidx]:
                        temp = self.oneidx
                        self.oneidx += 1
                        return (nums1[temp] + findmed(1)) / 2
                    else:
                        temp = self.twoidx
                        self.twoidx += 1
                        return (nums2[temp] + findmed(1)) / 2
                else:
                    return min(nums1[self.oneidx], nums2[self.twoidx])
            if av1 == 0:
                if self.even:
                    return (nums2[self.twoidx + med - 1] + nums2[self.twoidx + med]) / 2
                return nums2[self.twoidx + med - 1]
            elif av2 == 0:
                if self.even:
                    return (nums1[self.oneidx + med - 1] + nums1[self.oneidx + med]) / 2
                return nums1[self.oneidx + med - 1]
            elif av1 >= half and av2 < half:
                idx1 = self.oneidx + med - av2 - 1
                idx2 = len2 - 1
            elif av1 < half and av2 >= half:
                idx1 = len1 - 1
                idx2 = self.twoidx + med - av1 - 1
            elif av1 >= half and av2 >= half:
                idx1 = self.oneidx + half - 1
                idx2 = self.twoidx + med - half - 1
            
            if nums1[idx1] <= nums2[idx2]:
                removed = idx1+1 - self.oneidx
                self.oneidx = idx1 + 1
            else:
                removed = idx2 + 1 - self.twoidx
                self.twoidx = idx2 + 1
            
            return findmed(med - removed)

        return findmed(math.ceil((len1 + len2) / 2) )