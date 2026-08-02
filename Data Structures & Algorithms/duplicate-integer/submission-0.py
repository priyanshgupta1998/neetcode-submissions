class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Step 1: Ek empty set banao jo already dekhe elements store karega
        seen = set()
        
        # Step 2: Array ke har element ko ek-ek karke check karo
        for num in nums:
            # Step 3: Agar current element already set mein hai,
            #         iska matlab duplicate mil gaya
            if num in seen:
                return True
            
            # Step 4: Agar nahi hai, to set mein add kar do
            seen.add(num)
        
        # Step 5: Agar pura loop khatam ho gaya aur koi duplicate nahi mila,
        #         to return False
        return False