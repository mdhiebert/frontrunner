#include <queue>
#include <limits>
#include <cmath>
#include <iostream>

// represents a single pixel
class Node {
  public:
    int idx;     // index in the flattened grid
    float cost;  // cost of traversing this pixel

    Node(int i, float c) : idx(i),cost(c) {}
};

// the top of the priority queue is the greatest element by default,
// but we want the smallest, so flip the sign
bool operator<(const Node &n1, const Node &n2) {
  return n1.cost > n2.cost;
}

bool operator==(const Node &n1, const Node &n2) {
  return n1.idx == n2.idx;
}

// See for various grid heuristics:
// http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html#S7
// L_\inf norm (diagonal distance)
float linf_norm(int i0, int j0, int i1, int j1) {
  return std::max(std::abs(i0 - i1), std::abs(j0 - j1));
}

// L_1 norm (manhattan distance)
float l1_norm(int i0, int j0, int i1, int j1) {
  return std::abs(i0 - i1) + std::abs(j0 - j1);
}

// "Smooth" out path by discouraging turns whenever possible in 4-neighbor model (custom heuristic)
float limit_turns(int i0, int j0, int i1, int j1, float direction) {
  // 2.0 = forward, -2.0 = back, 1.0 = right, -1.0 = left
  float regular = l1_norm(i0, j0, i1, j1);
  //std::cout <<direction << "(start" << i0 << ", " <<j0<< ")"<< "(candidate"<<i1<<", "<<j1<<") | "<<"\n";
  if (direction == 2.0) {
    if (i0 == i1){
      return regular;
    }
    else {
      return 5*regular;
    }
  }
  else if (direction == -2.0) {
    if (i0 == i1){
      return regular;
    }
    else {
      
      return 5*regular;
    }
  }

  else if (direction == 1.0) {
    if (j0 == j1){
      return regular;
    }
    
    else {
      
      return 5*regular;
    }
  }

  else if (direction == -1.0) {
    if (j0 == j1){
      return regular;
    }
    
    else {
      return 5*regular;
    }
  }
  else{
    return regular;
  }
  
}

// weights:        flattened h x w grid of costs
// h, w:           height and width of grid
// start, goal:    index of start/goal in flattened grid
// diag_ok:        if true, allows diagonal moves (8-conn.)
// paths (output): for each node, stores previous node in path
extern "C" bool astar(
      const float* weights, const int h, const int w,
      const int start, const int goal, bool diag_ok,
      int* paths) {

  const float INF = std::numeric_limits<float>::infinity();

  Node start_node(start, 0.);
  Node goal_node(goal, 0.);

  float* costs = new float[h * w];
  for (int i = 0; i < h * w; ++i)
    costs[i] = INF;
  costs[start] = 0.;

  std::priority_queue<Node> nodes_to_visit;
  nodes_to_visit.push(start_node);
  Node cur = nodes_to_visit.top();

  int* nbrs = new int[8];

  int* directions = new int[8];
  
  bool first_node = true;
  bool second_node = false;
  bool solution_found = false;
  while (!nodes_to_visit.empty()) {
    // .top() doesn't actually remove the node
    

    if (cur == goal_node) {
      solution_found = true;
      break;
    }

    nodes_to_visit.pop();

    int row = cur.idx / w;
    int col = cur.idx % w;
    
    // check bounds and find up to eight neighbors: top to bottom, left to right
    nbrs[0] = (diag_ok && row > 0 && col > 0)          ? cur.idx - w - 1   : -1;
    nbrs[1] = (row > 0)                                ? cur.idx - w       : -1;
    nbrs[2] = (diag_ok && row > 0 && col + 1 < w)      ? cur.idx - w + 1   : -1;
    nbrs[3] = (col > 0)                                ? cur.idx - 1       : -1;
    nbrs[4] = (col + 1 < w)                            ? cur.idx + 1       : -1;
    nbrs[5] = (diag_ok && row + 1 < h && col > 0)      ? cur.idx + w - 1   : -1;
    nbrs[6] = (row + 1 < h)                            ? cur.idx + w       : -1;
    nbrs[7] = (diag_ok && row + 1 < h && col + 1 < w ) ? cur.idx + w + 1   : -1;

    float heuristic_cost;
    for (int i = 0; i < 8; ++i) {
      if (nbrs[i] >= 0) {
        // the sum of the cost so far and the cost of this move
        float new_cost = costs[cur.idx] + weights[nbrs[i]];
        if (new_cost < costs[nbrs[i]]) {
          // estimate the cost to the goal based on legal moves
          if (diag_ok) {
            heuristic_cost = linf_norm(nbrs[i] / w, nbrs[i] % w,
                                       goal    / w, goal    % w);
          }
          else {
            
            heuristic_cost = limit_turns(nbrs[i] / w, nbrs[i] % w,
                                       goal    / w, goal    % w,
                                       directions[i]);

            //std::cout <<heuristic_cost << "(" <<nbrs[i] /w << ")"<< ",";
          }
          // else {
          //   heuristic_cost = l1_norm(nbrs[i] / w, nbrs[i] % w,
          //                            goal    / w, goal    % w);
          // }

          // paths with lower expected cost are explored first
          float priority = new_cost + heuristic_cost;


          if ((i == 1) && (second_node == true)) {
            //std::cout << "forward bias!!!!!" << "\n";
            priority = priority/3;
            
            second_node = false;
            
          }
          if ((i == 1) && (first_node == true)) {
            //std::cout << "forward bias!!!!!" << "\n";
            priority = priority/3;
            
            first_node = false;
            second_node = true;
            
          }

          
          
          nodes_to_visit.push(Node(nbrs[i], priority));

          costs[nbrs[i]] = new_cost;
          paths[nbrs[i]] = cur.idx;
        }
      }
    }

    directions[1] = 1.0;
    directions[3] = 2.0;
    directions[4] = -2.0;
    directions[6] = -1.0;
    cur = nodes_to_visit.top();
  }

  delete[] costs;
  delete[] nbrs;

  return solution_found;
}
