import heapq
import math
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class GraphEdge:
    """Directed edge with weight."""
    target: str
    weight: float

def dijkstra(graph: Dict[str, List[Tuple[str, float]]], 
             source: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
    """
    Production implementation of Dijkstra's single-source shortest path.
    
    Time Complexity: O((V+E) log V)
    Correctness: Guaranteed for w(e) ≥ 0 (Cormen et al. 2009)
    """
    # Phase 1: Initialize data structures
    distances = {node: math.inf for node in graph}
    distances[source] = 0.0
    predecessors = {node: None for node in graph}
    pq: List[Tuple[float, str]] = [(0.0, source)]
    
    # Phase 2: Greedy relaxation loop
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        # Prune obsolete entries
        if current_dist > distances[current]:
            continue
            
        # Relax outgoing edges
        for neighbor, weight in graph.get(current, []):
            new_dist = distances[current] + weight
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                predecessors[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distances, predecessors
