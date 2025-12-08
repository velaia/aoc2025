from dataclasses import dataclass
import math
from pathlib import Path
from functools import reduce


@dataclass
class Node:
    point: list[int]

    def __init__(self, coords):
        coords = coords.split(",")
        self.x = int(coords[0])
        self.y = int(coords[1])
        self.z = int(coords[2])
        self.point = [self.x, self.y, self.z]

    def get_distance(self, point2) -> float:
        return math.dist(self.point, point2.point)


def is_already_connected(connection, circuits):
    for circuit in circuits:
        if connection[0] in circuit and connection[1] in circuit:
            return True
    return False


def connects_circuits(connection, circuits:list) -> bool:
    # connection can only connect two circuits, not have both nodes in one (due to prev test)
    connected_circuits = []

    for node in connection:
        for i, circuit in enumerate(circuits):
            if node in circuit:
                connected_circuits.append(i)
    
    # unify connected circuits and return True
    if len(connected_circuits) == 2:
        cir1 = circuits[connected_circuits[0]]
        cir2 = circuits[connected_circuits[1]]
        cir1.extend(cir2)

        circuits.remove(cir2)
        return True

    return False

    

def update_circuits(connection, circuits:list):
    new_circuit = True

    if connects_circuits(connection, circuits):
        pass # update circuits in function
    else:
        for circuit in circuits:
            if connection[0] in circuit:
                circuit.append(connection[1])
                new_circuit = False
            elif connection[1] in circuit:
                circuit.append(connection[0])
                new_circuit = False

        if new_circuit:
            circuits.append(connection)


def calculate_clusters(path: str, max_connections: int = 10) -> int:
    solution = 0
    points: list[Node] = []
    distances: list[tuple[float, tuple]] = []

    with Path(path).open() as file:
        for line in file.readlines():
            points.append(Node(line.strip()))

    for i, point1 in enumerate(points):
        for j, point2 in enumerate(points[i + 1 :]):
            distances.append((point1.get_distance(point2), [i, j + i + 1], (point1.point, point2.point)))

    distances = list(reversed(sorted(distances, key=lambda x: x[0])))

    connections_made = 0
    circuits = []

    while connections_made < max_connections:
        connection = distances.pop()
        connections_made += 1
        if not is_already_connected(connection[1], circuits):
            update_circuits(connection[1], circuits)

    circuit_sizes = [len(circuit) for circuit in circuits]
    circuit_sizes = sorted(circuit_sizes, reverse=True)
    solution = reduce(lambda x, y: x*y, circuit_sizes[:3])

    return solution

def calculate_last_connection(path: str) -> int:
    solution = 0
    points: list[Node] = []
    distances: list[tuple[float, tuple]] = []

    with Path(path).open() as file:
        for line in file.readlines():
            points.append(Node(line.strip()))

    for i, point1 in enumerate(points):
        for j, point2 in enumerate(points[i + 1 :]):
            distances.append((point1.get_distance(point2), [i, j + i + 1], (point1.point, point2.point)))

    distances = list(reversed(sorted(distances, key=lambda x: x[0])))

    connections_made = 0
    circuits = []
    connection = None
    counter = 0

    while True:
        counter += 1
        connection = distances.pop()
        connections_made += 1
        if not is_already_connected(connection[1], circuits):
            update_circuits(connection[1], circuits)
        print(connection)
        if counter > 5 and len(circuits) == 1 and len(circuits[0]) == len(points):
            break
    
    print(f"last connection: {connection}")

    # circuit_sizes = [len(circuit) for circuit in circuits]
    # circuit_sizes = sorted(circuit_sizes, reverse=True)
    # solution = reduce(lambda x, y: x*y, circuit_sizes[:3])

    return connection[2][0][0] * connection[2][1][0]


if __name__ == "__main__":
    dir = "day8"

    # part 1
    # for path in [("sample", 10), ("input", 1000)]:
    #     solution = calculate_clusters("day8/" + path[0], path[1])
    #     print(f"{path}, solution: {solution}")
    #     if path == "sample":
    #         assert 40 == solution
    
    # part 2
    for path in [("sample", 10), ("input", 1000)]:
        solution = calculate_last_connection("day8/" + path[0])
        print(f"{path}, solution: {solution}")
        if path[0] == "sample":
            assert 25272 == solution
