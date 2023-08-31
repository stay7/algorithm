def build_order(project, dependencies):
    graph = {p: set() for p in project}
    order = []
    unbuilt = set(project)
    for dependency, project in dependencies:
        graph[project].add(dependency)

    while unbuilt:
        something_build = False
        for project in list(unbuilt):
            dependencies = graph[project]
            if not unbuilt.intersection(dependencies):
                order.append(project)
                unbuilt.remove(project)
                something_build = True
        if not something_build:
            # raise error
            pass
    return build_order
