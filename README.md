Assignment 3
Your computer runs (localhost) several HTTP servers on various ports. The server serves the get following requests (you can try it in your browser):

    http://localhost:8080
    Returns the ports of other servers the called server knows about.
    http://localhost:8080/new?port=8081
    Adds the server running on the port 8081 to the list of ports (no checks done).

For testing purposes consider the following implementation (the implementation is greatly simplified, no checks for errors, etc.) of the servers together with a script that runs the servers nodes.zip. The nodes basicaly create a directed graph, thus I will use graph terminology.

Implement the following coroutines:

    async def complete_neighbourhood(start)
    Modifies the nodes so that the neighbours of start form a complete graph.
    async def climb_degree(start)
    We start at node start. In each step we move to the neighbour of highest degree, and in case that degrees are equal among those we choose the neighbour with lowest port number. We continue until local maximum is reached. The number of the port where local maximum is needed is returned.
    async def distance4(start)
    Finds all vertices in distance exactly 4 from start.

Your implementation should use (at least to a degree) cooperative multitasking. For each coroutine, implement one unit test (you need not to cover everything). The unittest should not include networking. Also write one system test where each function is called. The system test should include running the servers and all the networking. Note that the code that creates and runs the servers takes some condition variables. You can use them to synchorize your system test. Finally, write a test that checks that your coroutines execute the requests in parallel instead of synchronously. One of the ways to do this is to fake the networking part of your program so that handling of each request includes some sleep time and then check, if the resulting time is aproximately as expected.
