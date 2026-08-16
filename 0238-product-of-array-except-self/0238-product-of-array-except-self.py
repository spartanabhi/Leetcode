class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:

        n = len(arr)
        total_product = 1
        zero_count = 0

        # Step 1: Calculate the total product and count zeros
        for num in arr:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        result = []

        # Step 2: Build the result array based on zero count
        for num in arr:
            if zero_count > 1:
                # Case 1: More than one zero means everything becomes 0
                result.append(0)
            elif zero_count == 1:
                # Case 2: Exactly one zero
                if num == 0:
                    result.append(total_product)  # The zero position gets the product of the rest
                else:
                    result.append(0)              # Every other position is multiplied by 0
            else:
                # Case 3: No zeros at all (Standard division allowed approach)
                result.append(total_product // num)

        return result



            