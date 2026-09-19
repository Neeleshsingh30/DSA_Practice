# Class Solution():
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         products.sort()
#         result = []
#         prefix = ""
#         for char in searchWord:
#             prefix += char
#             suggestions = []
#             for product in products:
#                 if product.startswith(prefix):
#                     suggestions.append(product)
#                 if len(suggestions) == 3:
#                     break
#             result.append(suggestions)
#         return result

# # example usage
# solution = Solution()
# products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
# searchWord = "mouse"    
# print(solution.suggestedProducts(products, searchWord))





# non overlapping intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals based on the end time
        intervals.sort(key=lambda x: x[1])
        count = 1
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]

        return len(intervals) - count