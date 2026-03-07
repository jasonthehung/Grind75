class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        start_color = image[sr][sc]

        if start_color == color:
            return image

        rows, cols = len(image), len(image[0])
        neighbors = [(sr, sc)]

        while neighbors:
            r, c = neighbors.pop()

            if image[r][c] == start_color:
                image[r][c] = color

                for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        neighbors.append((nr, nc))

        return image
