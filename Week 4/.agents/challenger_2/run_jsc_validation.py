import subprocess
import json
import sys

target_file = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md"

with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

blocks = []
in_b = False
s_line = 0
cur = []

for idx, line in enumerate(lines, 1):
    if line.strip().startswith("```mermaid"):
        in_b = True
        s_line = idx
        cur = []
    elif line.strip() == "```" and in_b:
        in_b = False
        blocks.append({
            "block_num": len(blocks) + 1,
            "start_line": s_line,
            "end_line": idx,
            "lines": [l for _, l in cur],
            "raw": "".join([l for _, l in cur])
        })
        cur = []
    elif in_b:
        cur.append((idx, line))

print(f"Extracted {len(blocks)} blocks for JSC empirical testing.")

js_code = """
var blocks = """ + json.dumps(blocks) + """;

var validDiagramTypes = [
    "graph", "flowchart", "sequenceDiagram", "classDiagram", "stateDiagram",
    "stateDiagram-v2", "erDiagram", "gantt", "pie", "gitGraph", "timeline",
    "mindmap", "quadrantChart", "sankey-beta", "xychart-beta", "block-beta"
];

var validDirections = ["TD", "TB", "BT", "RL", "LR"];

function validateMermaidBlock(block) {
    var logs = [];
    var errors = [];
    var lines = block.lines;
    
    if (lines.length === 0) {
        errors.push("Empty code block");
        return { valid: false, errors: errors };
    }
    
    var firstLine = lines[0].trim();
    var parts = firstLine.split(/\\s+/);
    var dtype = parts[0];
    
    if (validDiagramTypes.indexOf(dtype) === -1) {
        errors.push("Invalid diagram type: " + dtype);
    }
    
    if (dtype === "graph" || dtype === "flowchart") {
        if (parts.length < 2) {
            errors.push("Missing graph direction (e.g. TD, LR)");
        } else if (validDirections.indexOf(parts[1]) === -1) {
            errors.push("Invalid graph direction: " + parts[1]);
        }
    }
    
    var subgraphStack = [];
    var quoteCount = 0;
    
    for (var i = 0; i < lines.length; i++) {
        var rawLine = lines[i];
        var line = rawLine.trim();
        if (!line || line.indexOf("%%") === 0) continue;
        
        // Subgraph tracking
        if (line.indexOf("subgraph") === 0) {
            subgraphStack.push({ lineNum: i + 1, text: line });
        } else if (line === "end" || line.indexOf("end ") === 0) {
            if (subgraphStack.length === 0) {
                errors.push("Unmatched 'end' statement at block line " + (i + 1));
            } else {
                subgraphStack.pop();
            }
        }
        
        // Check bracket pairs
        var sq = 0, pa = 0, cur = 0, inDQuote = false;
        for (var j = 0; j < line.length; j++) {
            var ch = line.charAt(j);
            if (ch === '"') {
                inDQuote = !inDQuote;
            } else if (!inDQuote) {
                if (ch === '[') sq++;
                else if (ch === ']') sq--;
                else if (ch === '(') pa++;
                else if (ch === ')') pa--;
                else if (ch === '{') cur++;
                else if (ch === '}') cur--;
            }
        }
        
        if (inDQuote) {
            errors.push("Unclosed double quote at block line " + (i + 1) + ": " + line);
        }
        if (sq !== 0) {
            errors.push("Unbalanced [] brackets (delta=" + sq + ") at block line " + (i + 1) + ": " + line);
        }
        if (pa !== 0) {
            errors.push("Unbalanced () parens (delta=" + pa + ") at block line " + (i + 1) + ": " + line);
        }
        if (cur !== 0) {
            errors.push("Unbalanced {} braces (delta=" + cur + ") at block line " + (i + 1) + ": " + line);
        }
    }
    
    if (subgraphStack.length > 0) {
        for (var k = 0; k < subgraphStack.length; k++) {
            errors.push("Unclosed subgraph starting at line " + subgraphStack[k].lineNum + ": " + subgraphStack[k].text);
        }
    }
    
    return { valid: errors.length === 0, errors: errors };
}

print("==================================================");
print("EMPIRICAL JS VALIDATION RESULTS VIA JAVASCRIPTCORE");
print("==================================================");

var totalErrors = 0;
for (var b = 0; b < blocks.length; b++) {
    var block = blocks[b];
    var res = validateMermaidBlock(block);
    print("Block " + block.block_num + " (Lines " + block.start_line + "-" + block.end_line + "): " + (res.valid ? "PASS" : "FAIL"));
    if (!res.valid) {
        for (var e = 0; e < res.errors.length; e++) {
            print("  - ERROR: " + res.errors[e]);
            totalErrors++;
        }
    }
}
print("Total JSC Errors: " + totalErrors);
"""

js_file_path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/.agents/challenger_2/run_jsc.js"
with open(js_file_path, "w", encoding="utf-8") as f:
    f.write(js_code)

cmd = ["/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc", js_file_path]
proc = subprocess.run(cmd, capture_output=True, text=True)

print(proc.stdout)
if proc.stderr:
    print("STDERR:", proc.stderr)
