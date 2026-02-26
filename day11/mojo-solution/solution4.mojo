import File
import Strings
import Array
import Dict

# Load connections from files
def load_connections(files: Array[String]) -> Dict[String, Array[String]]:
    var connections: Dict[String, Array[String]] = Dict()

    for file in files:
        if not File.exists(file):
            print("Warning: \(file) does not exist")
            continue

        let contents: String = File.read(file)
        let lines: Array[String] = Strings.split(contents, "\n")

        for line in lines:
            let line = Strings.strip(line)
            if Strings.empty(line) or not Strings.contains(line, ":"):
                continue

            let parts: Array[String] = Strings.split(line, ":", max_splits=1)
            let source: String = Strings.strip(parts[0])
            let dest_str: String = Strings.strip(parts[1])
            let destinations: Array[String] = Array(Strings.split(dest_str, " "))

            connections[source] = destinations

    return connections

# Recursively count paths to "out"
def follow(source: String, connections: Dict[String, Array[String]]) -> Int:
    if connections.get(source) == Array("out"):
        return 1

    var num_paths: Int = 0
    for dest in connections.get(source, Array()):
        num_paths += follow(dest, connections)
    return num_paths

# Main entry point
def main() -> None:
    let files: Array[String] = Array(["sample", "input"])
    let connections = load_connections(files)

    for file in files:
        let num_paths = follow("you", connections)
        # print("\(file)=, \(num_paths)=")

main()

