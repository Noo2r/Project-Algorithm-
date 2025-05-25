class Node {
  constructor(char, freq, left = null, right = null) {
    this.char = char;
    this.freq = freq;
    this.left = left;
    this.right = right;
  }
}

function buildHuffmanTree(freqMap) {
  const nodes = Object.entries(freqMap).map(([char, freq]) => new Node(char, freq));
  while (nodes.length > 1) {
    nodes.sort((a, b) => a.freq - b.freq);
    const left = nodes.shift();
    const right = nodes.shift();
    nodes.push(new Node(null, left.freq + right.freq, left, right));
  }
  return nodes[0];
}

function generateCodes(node, prefix = "", map = {}) {
  if (!node.left && !node.right) {
    map[node.char] = prefix;
  }
  if (node.left) generateCodes(node.left, prefix + "0", map);
  if (node.right) generateCodes(node.right, prefix + "1", map);
  return map;
}

function convertToD3Tree(node) {
  if (!node) return null;
  const obj = {
    name: node.char ? `${node.char} (${node.freq})` : `${node.freq}`,
    children: []
  };
  if (node.left) obj.children.push(convertToD3Tree(node.left));
  if (node.right) obj.children.push(convertToD3Tree(node.right));
  return obj;
}

function renderTreeGraph(node) {
  d3.select("#tree-container").html("");

  const treeData = convertToD3Tree(node);
  const width = 1200;
  const height = 500;
  const dx = 50;
  const dy = 100;

  const root = d3.hierarchy(treeData);
  const treeLayout = d3.tree().nodeSize([dx, dy]);
  treeLayout(root);

  const svg = d3.select("#tree-container")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("font", "14px sans-serif");

  const g = svg.append("g")
    .attr("transform", `translate(${width * 0.35}, 100)`);

  g.append("g")
    .selectAll("path")
    .data(root.links())
    .join("path")
    .attr("fill", "none")
    .attr("stroke", "#007bff")
    .attr("stroke-width", 2)
    .attr("d", d3.linkVertical()
      .x(d => d.x)
      .y(d => d.y)
    );

  const nodeG = g.append("g")
    .selectAll("g")
    .data(root.descendants())
    .join("g")
    .attr("transform", d => `translate(${d.x},${d.y})`);

  nodeG.append("circle")
    .attr("r", 20)
    .attr("fill", d => d.children ? "#007bff" : "#28a745")
    .attr("stroke", "#fff")
    .attr("stroke-width", 2);

  nodeG.append("text")
    .attr("dy", "0.31em")
    .attr("y", d => d.children ? -30 : 30)
    .attr("text-anchor", "middle")
    .style("font-weight", "bold")
    .text(d => d.data.name)
    .clone(true).lower()
    .attr("stroke", "white");
}

let huffmanTree = null;
let codeMap = null;

function compress() {
  const text = document.getElementById("inputText").value;
  if (!text) return;

  const freq = {};
  for (let char of text) {
    freq[char] = (freq[char] || 0) + 1;
  }

  huffmanTree = buildHuffmanTree(freq);
  codeMap = generateCodes(huffmanTree);

  const encoded = text.split('').map(c => codeMap[c]).join('');

  document.getElementById("frequencies").innerText =
    Object.entries(freq).map(([c, f]) => `${c}: ${f}`).join('\n');

  document.getElementById("codes").innerText =
    Object.entries(codeMap).map(([c, code]) => `${c}: ${code}`).join('\n');

  document.getElementById("encoded").innerText = encoded;
  document.getElementById("decoded").innerText = "";

  renderTreeGraph(huffmanTree);
}

function decompress() {
  const encoded = document.getElementById("encodedInput").value.trim();
  if (!encoded || !huffmanTree) {
    document.getElementById("decoded").innerText = "⚠️ Please enter binary input and make sure you ran compression first.";
    return;
  }

  let result = "";
  let node = huffmanTree;
  for (let bit of encoded) {
    node = bit === '0' ? node.left : node.right;
    if (node.char !== null) {
      result += node.char;
      node = huffmanTree;
    }
  }

  document.getElementById("decoded").innerText = result;
}
