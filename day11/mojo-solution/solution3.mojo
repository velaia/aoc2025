import File
import Strings
import Array
import Dict

# Load connection mappings from files (high-performance version)
def load_connections(files: Array[str]) -> Dict[str, Array[str]]:
    var connections: Dict[str, Array[str]] = Dict()

    for file in files:
        if not File.exists(file):
            print("Warning: \(file) does not exist")
            continue

        let contents = File.read(file)
        let lines = Strings.split(contents, "\n")

        for line in lines:
            let line = Strings.strip(line)
            if Strings.empty(line) or not Strings.contains(line, ":"):
                continue

            let parts = Strings.split(line, ":", max_splits=1)
            let source = Strings.strip(parts[0])
            let dest_str = Strings.strip(parts[1])
            let destinations = Array(Strings.split(dest_str, " "))

            connections[source] = destinations

    return connections

# Recursive path counting using arrays and static typing
def follow(source: str, connections: Dict[str, Array[str]]) -> Int:
    if connections.get(source) == Array("out"):
        return 1

    var num_paths: Int = 0
    for dest in connections.get(source, Array()):
        num_paths += follow(dest, connections)
    return num_paths

# Main entry point
def main() -> None:
    let files: Array[str] = Array(["sample", "input"])
    let connections = load_connections(files)

    for file in files:
        let num_paths = follow("you", connections)
        # Uncomment to print results
        # print("\(file)=, \(num_paths)=")

main()

