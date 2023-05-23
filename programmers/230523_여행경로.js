function solution(tickets) {
  var answer = [];

  let len = tickets.length;
  let visited = Array.from({ length: len }, () => false);

  tickets.sort();

  function dfs(loc, path, depth) {
    if (depth === len && !answer.length) return (answer = path);

    for (let i = 0; i < len; i++) {
      if (tickets[i][0] === loc && !visited[i]) {
        visited[i] = true;
        dfs(tickets[i][1], [...path, tickets[i][1]], depth + 1);
        visited[i] = false;
      }
    }
  }

  dfs("ICN", ["ICN"], 0);

  return answer;
}
