class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            for i in range(ceil(len(image)/2)):
                row[i], row[len(row)-i-1] = abs(row[len(row)-i-1] - 1), abs(row[i] - 1)
        return image
        
                