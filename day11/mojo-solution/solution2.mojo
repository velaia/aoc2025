import File
import Strings
import List
import Dict

# Function to load connection mappings from a list of files
def load_connections(files: List[str]) -> Dict[str, List[str]]:
    var connections: Dict[str, List[str]] = Dict()
    
    for file in files:
        if not File.exists(file):
            print("Warning: (file) does not exist")
            continue

        let contents = File.read(file)
        for line in Strings.split(contents, "\n"):
            let line = Strings.strip(line)
            if Strings.empty(line) or not Strings.contains(line, ":"):
                continue

            let parts = Strings.split(line, ":", max_splits=1)
            let source = Strings.strip(parts[0])
            let dest_str = Strings.strip(parts[1])
            let destinations = Strings.split(dest_str, " ")

            connections[source] = destinations
    return connections

# Recursive function to count paths from source to "out"
def follow(source: str, connections: Dict[str, List[str]]) -> Int:
    if connections.get(source) == ["out"]:
        return 1

    var num_paths: Int = 0
    for dest in connections.get(source, []):
        num_paths += follow(dest, connections)
    return num_paths

# Main entry point
def main() -> None:
    let files: List[str] = ["sample", "input"]
    let connections = load_connections(files)

    for file in files:
        let num_paths = follow("you", connections)
        # Uncomment to print results
        # print("\(file)=, \(num_paths)=")

main()

