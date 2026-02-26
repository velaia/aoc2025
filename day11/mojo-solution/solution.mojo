def main():
    # Example connections: fill this via input parsing or manual data
    var connections: Dict[String, List[String]] = load_connections(["input"])

    var total = count_valid_paths(connections, "svr")
    print("Total valid paths: " + total.to_string())

fn load_connections(files: List[String]) -> Dict[String, List[String]]:
    var connections: Dict[String, List[String]] = Dict()
    for file in files:
        # Read file content (simplified — replace with proper file I/O)
        var text = read_file(file)  # placeholder
        for line in text.split("\n"):
            if line.contains(":"):
                let parts = line.split(":", 2)
                let source = parts[0].strip()
                let dests = parts[1].strip().split()
                connections[source] = dests
    return connections

fn count_valid_paths(
    connections: Dict[String, List[String]],
    start: String
) -> Int:
    # Cache results of subproblems using a dictionary with key (node, seen_fft, seen_dac)
    var cache: Dict[(String, Bool, Bool), Int] = Dict()

    fn dfs(
        node: String,
        has_fft: Bool,
        has_dac: Bool
    ) -> Int:
        var new_fft = has_fft or (node == "fft")
        var new_dac = has_dac or (node == "dac")
        let key = (node, new_fft, new_dac)

        if cache.contains(key):
            return cache[key]!

        if connections.contains(node) and connections[node]!.len() == 1 and \
           connections[node]![0] == "out":
            let result = (new_fft and new_dac) ? 1 : 0
            cache[key] = result
            return result

        var total: Int = 0
        if connections.contains(node):
            for dest in connections[node]!:
                total += dfs(dest, new_fft, new_dac)

        cache[key] = total
        return total

    return dfs(start, false, false)

# Placeholder function — provide real file I/O in a Mojo environment
fn read_file(path: String) -> String:
    # Replace with actual file reading API
    return ""

