import math

class AnimationModel:
    def __init__(self, radius=180):
        self.radius = radius

    def get_triangle_radius(self, theta):
        alpha = (theta - math.pi / 2) % (2 * math.pi / 3) - math.pi / 3
        return self.radius * math.cos(math.pi / 3) / math.cos(alpha)

    def get_points(self, morph_ratio, num_points=360):
        points = []
        for i in range(num_points):
            theta = (2 * math.pi * i) / num_points
            r_circle = self.radius
            r_triangle = self.get_triangle_radius(theta)
            r = r_circle + (r_triangle - r_circle) * morph_ratio
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            points.append((x, y))
        return points

