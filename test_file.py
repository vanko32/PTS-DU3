import unittest
from unittest.mock import Mock
import asyncio
from functions import Request
from functions import Functions


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.f = Functions(Request())
        self.graph = []

        async def add_connection(x,y):
            if (x, y) not in self.graph:
                self.graph.append((x,y))
                self.graph.append((y,x))

        async def neighbours(node):
            neighbourhood = list()
            for g in self.graph:
                if (g[0] == node) or (g[1] == node):
                    if g[0] != node:
                        neighbourhood.append(g[0])
                    else:
                        neighbourhood.append(g[1])


        self.f.request.add_connection = Mock(side_effect = add_connection)
        self.f.request.neighbours = Mock(side_effect = neighbours)

    def test_complete_neighbourhood(self):
        self.graph = ((8030,8031),(8031,8030),(8030,8032),(8032,8030))
        asyncio.run(self.f.complete_neighbourhood(8030))
        self.assertEqual(self.graph, ((8030,8031),(8031,8030),(8030,8032),(8032,8030), (8031,8032), (8032,8031)))

    def test_distance4(self):
        pass

    def test_climb_degree(self):
        pass


if __name__=="__main__":
    unittest.main()
