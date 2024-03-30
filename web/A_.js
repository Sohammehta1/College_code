class Node {
    constructor(name) {
        this.name = name;
        this.neighbors = {}; // Key is neighbor name, value is distance
        this.parent = null;
        this.g = 0; // Cost from start to current node
        this.h = 0; // Estimated cost from current node to goal (always 0 in this case)
        this.f = 0; // Total cost (g + h)
    }
}

class PriorityQueue {
    constructor() {
        this.elements = [];
    }

    enqueue(element, priority) {
        this.elements.push({ element, priority });
        this.elements.sort((a, b) => a.priority - b.priority);
    }

    dequeue() {
        return this.elements.shift().element;
    }

    isEmpty() {
        return this.elements.length === 0;
    }
}

function findPath(graph, startNode, goalNode) {
    const openList = new PriorityQueue();
    const closedList = new Set();

    startNode.g = 0;
    openList.enqueue(startNode, startNode.f);

    while (!openList.isEmpty()) {
        const currentNode = openList.dequeue();

        if (currentNode === goalNode) {
            // Found the goal! Backtrack to construct the path
            const path = [];
            let node = currentNode;
            while (node) {
                path.push(node.name);
                node = node.parent;
            }
            return path.reverse();
        }

        closedList.add(currentNode);

        for (const [neighborName, distance] of Object.entries(currentNode.neighbors)) {
            const neighbor = graph[neighborName];

            if (closedList.has(neighbor)) {
                continue;
            }

            const tentativeG = currentNode.g + distance;

            if (openList.elements.some(({ element }) => element === neighbor)) {
                if (tentativeG >= neighbor.g) {
                    continue;
                }
            } else {
                neighbor.g = tentativeG;
                neighbor.parent = currentNode;
                neighbor.f = neighbor.g; // Total cost is just g-score
                openList.enqueue(neighbor, neighbor.f);
            }
        }
    }

    return null; // No path found
}

function main() {
    let numNodes = parseInt(prompt("Enter the number of nodes: "));
    const graph = {};

    const getConnections = (nodeName) => {
        let numConnections = parseInt(prompt(`Enter the number of connections for ${nodeName}: `));
        const node = new Node(nodeName);
        for (let i = 0; i < numConnections; i++) {
            let neighborName = prompt(`Enter a neighbor for ${nodeName}: `);
            let distance = parseFloat(prompt(`Enter the distance to ${neighborName}: `));
            node.neighbors[neighborName] = distance;
        }
        graph[nodeName] = node;
        if (Object.keys(graph).length < numNodes) {
            let nextNodeName = prompt(`Enter node name: `);
            getConnections(nextNodeName);
        } else {
            getStartAndGoalNodes(graph);
        }
    };

    let startNodeName, goalNodeName;

    const getStartAndGoalNodes = (graph) => {
        startNodeName = prompt(`Enter the starting node: `);
        goalNodeName = prompt(`Enter the goal node: `);

        const startNode = graph[startNodeName];
        const goalNode = graph[goalNodeName];

        // Set heuristic to 0 since we don't have an estimate
        for (const node of Object.values(graph)) {
            node.h = 0;
        }

        // Run A* and print path
        const path = findPath(graph, startNode, goalNode);
        if (path) {
            console.log("Path found:", path);
            for (const nodeName of path) {
                const node = graph[nodeName];
                console.log(`${nodeName}: f=${node.f}, g=${node.g}, h=${node.h}`);
            }
        } else {
            console.log("No path found!");
        }
    };

    let firstNodeName = prompt(`Enter node name: `);
    getConnections(firstNodeName);
}

document.addEventListener("DOMContentLoaded", function() {
    main();
});

