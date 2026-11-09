from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # input is a list of list

        original_color = image[sr][sc]

        if original_color == color:
            return image

        q = deque([(sr, sc)])
        image[sr][sc] = color
        ROWS, COLS = len(image), len(image[0])
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Invariant check: within grid boundaries AND matches original color
                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == original_color:
                    # In-place repaint acts as the 'visited' marker
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image