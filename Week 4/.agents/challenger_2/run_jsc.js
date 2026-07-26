
var blocks = [{"block_num": 1, "start_line": 35, "end_line": 58, "lines": ["graph LR\n", "    subgraph Strategy_Loop [Strategic Alignment]\n", "        BS[Business Strategy]\n", "        ITS[IT Strategy]\n", "        IT[Information Technology]\n", "        BS <--> ITS\n", "        ITS <--> IT\n", "        IT <--> BS\n", "    end\n", "\n", "    subgraph Infrastructure_Platform [IT Platform]\n", "        SERVICES[IT Services and Infrastructure]\n", "    end\n", "\n", "    subgraph Capabilities [Business Services & Capabilities]\n", "        CAP[Customer Services<br/>Supplier Services<br/>Enterprise Services]\n", "    end\n", "\n", "    BS --> SERVICES\n", "    ITS --> SERVICES\n", "    IT --> SERVICES\n", "    SERVICES --> CAP\n"], "raw": "graph LR\n    subgraph Strategy_Loop [Strategic Alignment]\n        BS[Business Strategy]\n        ITS[IT Strategy]\n        IT[Information Technology]\n        BS <--> ITS\n        ITS <--> IT\n        IT <--> BS\n    end\n\n    subgraph Infrastructure_Platform [IT Platform]\n        SERVICES[IT Services and Infrastructure]\n    end\n\n    subgraph Capabilities [Business Services & Capabilities]\n        CAP[Customer Services<br/>Supplier Services<br/>Enterprise Services]\n    end\n\n    BS --> SERVICES\n    ITS --> SERVICES\n    IT --> SERVICES\n    SERVICES --> CAP\n"}, {"block_num": 2, "start_line": 88, "end_line": 106, "lines": ["timeline\n", "    title Eras in IT Infrastructure Evolution\n", "    1959 : Mainframe / Minicomputer Era\n", "         : IBM Mainframes (1401, 360)\n", "         : DEC Minicomputers (PDP-11, VAX)\n", "    1981 : Personal Computer (PC) Era\n", "         : IBM PC, DOS, Wintel Standard\n", "         : Desktop productivity software\n", "    1983 : Client / Server Era\n", "         : Two-tier & Multitier architectures\n", "         : Desktop clients connected to servers (Novell, Windows)\n", "    1992 : Enterprise Computing Era\n", "         : Enterprise-wide networks, TCP/IP protocol\n", "         : Integrated enterprise applications & Web services\n", "    2000 : Cloud & Mobile Computing Era\n", "         : On-demand shared cloud resources (AWS, IBM, Azure, Google)\n", "         : Smartphones, tablets, SaaS, PaaS, IaaS\n"], "raw": "timeline\n    title Eras in IT Infrastructure Evolution\n    1959 : Mainframe / Minicomputer Era\n         : IBM Mainframes (1401, 360)\n         : DEC Minicomputers (PDP-11, VAX)\n    1981 : Personal Computer (PC) Era\n         : IBM PC, DOS, Wintel Standard\n         : Desktop productivity software\n    1983 : Client / Server Era\n         : Two-tier & Multitier architectures\n         : Desktop clients connected to servers (Novell, Windows)\n    1992 : Enterprise Computing Era\n         : Enterprise-wide networks, TCP/IP protocol\n         : Integrated enterprise applications & Web services\n    2000 : Cloud & Mobile Computing Era\n         : On-demand shared cloud resources (AWS, IBM, Azure, Google)\n         : Smartphones, tablets, SaaS, PaaS, IaaS\n"}, {"block_num": 3, "start_line": 109, "end_line": 116, "lines": ["graph LR\n", "    Client[Client Machine<br/>Desktop / Mobile] <===> Internet((Internet))\n", "    Internet <===> WebServer[Web Server<br/>Handles web page requests]\n", "    WebServer <===> AppServer[Application Server<br/>Handles business logic]\n", "    AppServer <===> Systems[Sales / Production /<br/>Accounting / HR Systems]\n", "    Systems <===> Data[(Corporate Database /<br/>Data Storage)]\n"], "raw": "graph LR\n    Client[Client Machine<br/>Desktop / Mobile] <===> Internet((Internet))\n    Internet <===> WebServer[Web Server<br/>Handles web page requests]\n    WebServer <===> AppServer[Application Server<br/>Handles business logic]\n    AppServer <===> Systems[Sales / Production /<br/>Accounting / HR Systems]\n    Systems <===> Data[(Corporate Database /<br/>Data Storage)]\n"}, {"block_num": 4, "start_line": 162, "end_line": 173, "lines": ["graph TD\n", "    CORE((IT Infrastructure<br/>Ecosystem))\n", "\n", "    CORE --- HW[1. Computer Hardware Platforms<br/>IBM, Oracle Sun, HP, Apple]\n", "    CORE --- OS[2. Operating Systems Platforms<br/>Microsoft Windows, Unix, Linux, MacOS, Chrome, Android, iOS]\n", "    CORE --- APP[3. Enterprise Software Applications<br/>SAP, Oracle, Microsoft, IBM]\n", "    CORE --- DATA[4. Data Management & Storage<br/>IBM DB2, Oracle, SQL Server, Sybase, MySQL, Apache Hadoop]\n", "    CORE --- NET[5. Networking / Telecommunications<br/>Windows Server, Linux, Cisco, AT&T, Verizon]\n", "    CORE --- INT[6. Internet Platforms<br/>Apache, Microsoft IIS, .NET, Unix, Cisco, Java]\n", "    CORE --- CON[7. Consultants & System Integrators<br/>IBM, HP, Accenture]\n"], "raw": "graph TD\n    CORE((IT Infrastructure<br/>Ecosystem))\n\n    CORE --- HW[1. Computer Hardware Platforms<br/>IBM, Oracle Sun, HP, Apple]\n    CORE --- OS[2. Operating Systems Platforms<br/>Microsoft Windows, Unix, Linux, MacOS, Chrome, Android, iOS]\n    CORE --- APP[3. Enterprise Software Applications<br/>SAP, Oracle, Microsoft, IBM]\n    CORE --- DATA[4. Data Management & Storage<br/>IBM DB2, Oracle, SQL Server, Sybase, MySQL, Apache Hadoop]\n    CORE --- NET[5. Networking / Telecommunications<br/>Windows Server, Linux, Cisco, AT&T, Verizon]\n    CORE --- INT[6. Internet Platforms<br/>Apache, Microsoft IIS, .NET, Unix, Cisco, Java]\n    CORE --- CON[7. Consultants & System Integrators<br/>IBM, HP, Accenture]\n"}, {"block_num": 5, "start_line": 241, "end_line": 274, "lines": ["graph TD\n", "    subgraph External_Devices[\"Client Devices & External Hardware\"]\n", "        Servers[\"Servers\"]\n", "        Desktops[\"Desktops\"]\n", "        Laptops[\"Laptops\"]\n", "        iPhone[\"iPhone\"]\n", "        Tablets[\"Tablet Computers\"]\n", "    end\n", "\n", "    subgraph Cloud_Platform[\"Cloud Computing Platform\"]\n", "        subgraph Platform_Services[\"Platform Services\"]\n", "            BS[\"Block Storage\"]\n", "            CN[\"Communication Networks\"]\n", "            IM[\"Identity Management\"]\n", "            CS[\"Content Servers\"]\n", "        end\n", "\n", "        subgraph Application_Services[\"Application Services\"]\n", "            CM[\"Content Management\"]\n", "            ES[\"Enterprise Software\"]\n", "            CE[\"Collaboration Environments\"]\n", "            PM[\"Process Management\"]\n", "        end\n", "\n", "        subgraph Infrastructure_Services[\"Infrastructure Services\"]\n", "            CRM[\"Computing Resource Management\"]\n", "            NM[\"Network Management\"]\n", "            SM[\"Storage Management\"]\n", "        end\n", "    end\n", "\n", "    External_Devices <--> Cloud_Platform\n"], "raw": "graph TD\n    subgraph External_Devices[\"Client Devices & External Hardware\"]\n        Servers[\"Servers\"]\n        Desktops[\"Desktops\"]\n        Laptops[\"Laptops\"]\n        iPhone[\"iPhone\"]\n        Tablets[\"Tablet Computers\"]\n    end\n\n    subgraph Cloud_Platform[\"Cloud Computing Platform\"]\n        subgraph Platform_Services[\"Platform Services\"]\n            BS[\"Block Storage\"]\n            CN[\"Communication Networks\"]\n            IM[\"Identity Management\"]\n            CS[\"Content Servers\"]\n        end\n\n        subgraph Application_Services[\"Application Services\"]\n            CM[\"Content Management\"]\n            ES[\"Enterprise Software\"]\n            CE[\"Collaboration Environments\"]\n            PM[\"Process Management\"]\n        end\n\n        subgraph Infrastructure_Services[\"Infrastructure Services\"]\n            CRM[\"Computing Resource Management\"]\n            NM[\"Network Management\"]\n            SM[\"Storage Management\"]\n        end\n    end\n\n    External_Devices <--> Cloud_Platform\n"}, {"block_num": 6, "start_line": 277, "end_line": 289, "lines": ["graph TD\n", "    AWS((\"Amazon Web Services\"))\n", "    AWS --- Comp[\"Computing\"]\n", "    AWS --- Net[\"Networking\"]\n", "    AWS --- CD[\"Content delivery\"]\n", "    AWS --- DS[\"Data storage\"]\n", "    AWS --- DB[\"Database\"]\n", "    AWS --- Dep[\"Deployment\"]\n", "    AWS --- Mgmt[\"Management\"]\n", "    AWS --- AS[\"Application services\"]\n", "    AWS --- Ana[\"Analytics\"]\n"], "raw": "graph TD\n    AWS((\"Amazon Web Services\"))\n    AWS --- Comp[\"Computing\"]\n    AWS --- Net[\"Networking\"]\n    AWS --- CD[\"Content delivery\"]\n    AWS --- DS[\"Data storage\"]\n    AWS --- DB[\"Database\"]\n    AWS --- Dep[\"Deployment\"]\n    AWS --- Mgmt[\"Management\"]\n    AWS --- AS[\"Application services\"]\n    AWS --- Ana[\"Analytics\"]\n"}, {"block_num": 7, "start_line": 337, "end_line": 362, "lines": ["flowchart LR\n", "    subgraph External_Partners [\"External Systems & Devices\"]\n", "        SW[\"Southwest Airlines Systems\"]\n", "        TO[\"Tour Operator's Systems\"]\n", "        TR[\"Travel Reservation System\"]\n", "        WW[\"Wireless WebSite\"]\n", "        FP[\"Future Business Partners' Systems\"]\n", "    end\n", "\n", "    WS[\"Web Services<br/>(Intermediate Layer)\"]\n", "\n", "    subgraph Dollar_Systems [\"Dollar Rent A Car Systems\"]\n", "        SVR[\"Server\"]\n", "        LRS[\"Legacy Reservation System\"]\n", "    end\n", "\n", "    SW <--> WS\n", "    TO <--> WS\n", "    TR <--> WS\n", "    WW <--> WS\n", "    FP <-.-> WS\n", "\n", "    WS <--> SVR\n", "    SVR <--> LRS\n"], "raw": "flowchart LR\n    subgraph External_Partners [\"External Systems & Devices\"]\n        SW[\"Southwest Airlines Systems\"]\n        TO[\"Tour Operator's Systems\"]\n        TR[\"Travel Reservation System\"]\n        WW[\"Wireless WebSite\"]\n        FP[\"Future Business Partners' Systems\"]\n    end\n\n    WS[\"Web Services<br/>(Intermediate Layer)\"]\n\n    subgraph Dollar_Systems [\"Dollar Rent A Car Systems\"]\n        SVR[\"Server\"]\n        LRS[\"Legacy Reservation System\"]\n    end\n\n    SW <--> WS\n    TO <--> WS\n    TR <--> WS\n    WW <--> WS\n    FP <-.-> WS\n\n    WS <--> SVR\n    SVR <--> LRS\n"}, {"block_num": 8, "start_line": 407, "end_line": 438, "lines": ["flowchart TD\n", "    subgraph Center_Hub [Center Hub]\n", "        HUB((\"Your Firm's<br/>IT Services and<br/>Infrastructure\"))\n", "    end\n", "\n", "    subgraph Internal_Factors [Internal Factors]\n", "        F2[\"2. Your Firm's<br/>Business Strategy\"]\n", "        F3[\"3. Your Firm's<br/>IT Strategy, Infrastructure,<br/>and Cost\"]\n", "        F4[\"4. Information<br/>Technology\"]\n", "    end\n", "\n", "    subgraph External_Market_Factors [External Market Factors]\n", "        F1[\"1. Market Demand for Your Firm's<br/>Customer Services, Supplier Services,<br/>and Enterprise Services\"]\n", "        F6[\"6. Competitor Firms'<br/>IT Infrastructure Investments\"]\n", "        F5[\"5. Competitor Firms'<br/>IT Services\"]\n", "    end\n", "\n", "    F1 --> HUB\n", "    F2 --> HUB\n", "    F3 --> HUB\n", "    F4 --> HUB\n", "    F5 --> HUB\n", "    F6 --> HUB\n", "\n", "    F1 -.- F2\n", "    F2 -.- F3\n", "    F3 -.- F4\n", "    F4 -.- F5\n", "    F5 -.- F6\n", "    F6 -.- F1\n"], "raw": "flowchart TD\n    subgraph Center_Hub [Center Hub]\n        HUB((\"Your Firm's<br/>IT Services and<br/>Infrastructure\"))\n    end\n\n    subgraph Internal_Factors [Internal Factors]\n        F2[\"2. Your Firm's<br/>Business Strategy\"]\n        F3[\"3. Your Firm's<br/>IT Strategy, Infrastructure,<br/>and Cost\"]\n        F4[\"4. Information<br/>Technology\"]\n    end\n\n    subgraph External_Market_Factors [External Market Factors]\n        F1[\"1. Market Demand for Your Firm's<br/>Customer Services, Supplier Services,<br/>and Enterprise Services\"]\n        F6[\"6. Competitor Firms'<br/>IT Infrastructure Investments\"]\n        F5[\"5. Competitor Firms'<br/>IT Services\"]\n    end\n\n    F1 --> HUB\n    F2 --> HUB\n    F3 --> HUB\n    F4 --> HUB\n    F5 --> HUB\n    F6 --> HUB\n\n    F1 -.- F2\n    F2 -.- F3\n    F3 -.- F4\n    F4 -.- F5\n    F5 -.- F6\n    F6 -.- F1\n"}, {"block_num": 9, "start_line": 451, "end_line": 490, "lines": ["graph TD\n", "    subgraph Business_Challenges [Business Challenges]\n", "        BC1[\"\u2022 Outdated IT infrastructure\"]\n", "        BC2[\"\u2022 Highly competitive industry\"]\n", "    end\n", "\n", "    subgraph Management [Management]\n", "        M1[\"\u2022 Monitor service level and costs\"]\n", "        M2[\"\u2022 Make IT infrastructure investments\"]\n", "    end\n", "\n", "    subgraph Organization [Organization]\n", "        O1[\"\u2022 Create new services and business processes\"]\n", "    end\n", "\n", "    subgraph Technology [Technology]\n", "        T1[\"\u2022 Dynamic Rebooking system\"]\n", "        T2[\"\u2022 Cloud-based customer-facing applications\"]\n", "        T3[\"\u2022 IBM Cloud computing services\"]\n", "    end\n", "\n", "    subgraph Information_System [Information System]\n", "        IS_TITLE[\"Customer-Facing Systems\"]\n", "        IS1[\"\u2022 Provide online reservation rebooking\"]\n", "        IS2[\"\u2022 Provide online customer services at website, mobile phone, kiosks\"]\n", "    end\n", "\n", "    subgraph Business_Solutions [Business Solutions]\n", "        BS1[\"\u2022 Improve customer service\"]\n", "        BS2[\"\u2022 Increase revenue\"]\n", "    end\n", "\n", "    BC1 --> Management\n", "    BC2 --> Management\n", "    Management --> Information_System\n", "    Organization --> Information_System\n", "    Technology --> Information_System\n", "    Information_System --> Business_Solutions\n"], "raw": "graph TD\n    subgraph Business_Challenges [Business Challenges]\n        BC1[\"\u2022 Outdated IT infrastructure\"]\n        BC2[\"\u2022 Highly competitive industry\"]\n    end\n\n    subgraph Management [Management]\n        M1[\"\u2022 Monitor service level and costs\"]\n        M2[\"\u2022 Make IT infrastructure investments\"]\n    end\n\n    subgraph Organization [Organization]\n        O1[\"\u2022 Create new services and business processes\"]\n    end\n\n    subgraph Technology [Technology]\n        T1[\"\u2022 Dynamic Rebooking system\"]\n        T2[\"\u2022 Cloud-based customer-facing applications\"]\n        T3[\"\u2022 IBM Cloud computing services\"]\n    end\n\n    subgraph Information_System [Information System]\n        IS_TITLE[\"Customer-Facing Systems\"]\n        IS1[\"\u2022 Provide online reservation rebooking\"]\n        IS2[\"\u2022 Provide online customer services at website, mobile phone, kiosks\"]\n    end\n\n    subgraph Business_Solutions [Business Solutions]\n        BS1[\"\u2022 Improve customer service\"]\n        BS2[\"\u2022 Increase revenue\"]\n    end\n\n    BC1 --> Management\n    BC2 --> Management\n    Management --> Information_System\n    Organization --> Information_System\n    Technology --> Information_System\n    Information_System --> Business_Solutions\n"}];

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
    var parts = firstLine.split(/\s+/);
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
