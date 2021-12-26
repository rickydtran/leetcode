class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create datastore/dictionary to store difference pair
        # and index
        ds = {}
        # Loop through passed list
        for i in range(len(nums)):
            # Compute the differential pair from target
            dp = target - nums[i]
            # Lookup in datastore if diff pair was stored
            lu = ds.get(dp)
            # If value is None, then no diff pair from target
            # was stored, so we insert the value and index to table
            if lu == None:
                ds[nums[i]] = i
            # If we find the value in our map then we return that
            # found value and current index in list
            else:
                return [lu, i]
                