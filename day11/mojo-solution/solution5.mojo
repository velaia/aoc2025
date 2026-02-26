# Load connections from a list of files
def load_connections(files: List[String]) -> Dict[String, List[String]]:
    var connections: Dict[String, List[String]] = Dict()

    for file in files:
        # Try opening the file
        var f = open(file, "r")
        if f.handle == 0:  # file didn't open
            print("Warning: " + file + " does not exist")
            continue

        # Read entire file as a string
        let contents = f.read()  # reads whole file
        f.close()

        # Split into lines
        let lines = Strings.split(contents, "\n")
        for line in lines:
            let stripped = Strings.strip(line)
            if stripped == "" or not Strings.contains(stripped, ":"):
                continue

            let parts = Strings.split(stripped, ":", max_splits=1)
            let source = Strings.strip(parts[0])
            let dest_str = Strings.strip(parts[1])
            let destinations = List(Strings.split(dest_str, " "))

            connections[source] = destinations

    return connections

# Recursively count paths from source to "out"
def follow(source: String, connections: Dict[String, List[String]]) -> Int:
    if connections.get(source) == List("out"):
        return 1

    var count: Int = 0
    for dest in connections.get(source, List()):
        count += follow(dest, connections)
    return count

# Main entry
def main() -> None:
    let files = List(["sample", "input"])
    let connections = load_connections(files)

    for file in files:
        let num_paths = follow("you", connections)
        # print(file + ": " + num_paths.to_string())

main()

