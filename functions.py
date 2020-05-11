import asyncio
import requests

class Request:
    async def neighbours(node, HOST='localhost'):
        try:
            return requests.get(f'http://{HOST}:{node}')
        except:
            return []

    async def add_connection(x, y, HOST='localhost'):
        neighbours = await Request.neighbours(x)
        connection = False

        for n in neighbours:
            if (n == y):
                connection = True
                break

        if (connection == False):
            r = requests.get(f'http://{HOST}:{x}/new?port={y}')
            r = requests.get(f'http://{HOST}:{y}/new?port={x}')
        else:
            print("Connection exists")

class Functions:
    def __init__(self, request):
        self.request = request

    async def complete_neighbourhood(self, start):
        neighbours = await self.request.neighbours(start)

        async def make_connections(node):
            for n in neighbours:
                if (n != node):
                    await self.request.add_connection(n,node)

        await asyncio.gather(*[asyncio.create_task(make_connections(node)) for node in neighbours])



    async def climb_degree(self, start):
        neighbours = self.request.neighbours(start)
        p = start
        control = start

        async def node_information(node, set, HOST='localhost'):
            neighbours = await self.request.neighbours(node)
            number_of_neighbours = len(neighbours)
            set.append((number_of_neighbours, node))

        while (1):
            length = len(neighbours)
            set = set()
            functions = list()
            for n in neighbours:
                functions.append(asyncio.create_task(node_information(n, set)))
            await asyncio.gather(functions)

            for port in set:
                if (port[0] > length):
                    length = port[0]
                    p = port[1]
                elif (port[0] == length):
                    if (port[1] < p):
                        p = port[1]

            if (control == p):
                break
            else:
                control = p
                neighbours = self.request.neighbours(p)

        return p



    async def distance4(self, start):
        visited = []
        queue = []
        path = []

        visited.append(start)
        queue.append(start)
        count = 0
        path.append(count)

        async def help_function(r, visited, queue, path, count):
            for neighbour in r:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    path.append(count)

        while queue:
            s = queue.pop(0)
            r = self.request.neighbours(s)
            count = count + 1
            functions = list()
            functions.append(asyncio.create_task(help_function(r, visited, queue, path, count)))
            await asyncio.gather(functions)

        vertices_4 = []
        for i in path:
            if (path[i] == 4):
                vertices_4.append(visited[i])

        return vertices_4
