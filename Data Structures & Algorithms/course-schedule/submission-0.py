class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        int numcourses
        and a list prereq

        we must take course b to take course a

        -> [a, b]

        node b points node a 
        key[b].append[a] <- the courses are dependent of course a
        element in the graph key[i] empty set for all courses that need to be taken before
        graph = defaultdict(set())
        in_degree = {c[1] : 0 for c in numcourses}
        

        bfs:
        q will start with elements with no indeg
        visited = set()
        res = 0
        while q:
            res += 1
            c = q.popleft() # class with no prereq
            for courses in graph[c]:
                if indegree[courses] == 0:
                    q.append(course)

        return True if res == numcourses else False
        '''

        graph = defaultdict(set) 
        in_deg = [0] * numCourses

        for a, b in prerequisites:
            graph[a].add(b)
            in_deg[b] += 1

        q = deque()
        for i in range(numCourses):
            if in_deg[i] == 0:
                q.append(i)

        res = 0
        while q:
            c = q.popleft()
            res += 1
            for course in graph[c]:
                in_deg[course] -= 1
                if in_deg[course] == 0:
                    q.append(course)
        
        return res == numCourses


            


