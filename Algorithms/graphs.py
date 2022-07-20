from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(person):
    return person[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    print(search_queue)
    while True:
        person = search_queue.popleft()
        print(search_queue)
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return False
            else:
                search_queue += graph[person]
                searched.append(person)


search('you')
