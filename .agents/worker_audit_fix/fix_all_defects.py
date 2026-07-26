import re

path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Fix Block 6
text = text.replace("|Rule 1: Portfolio History|", "|Portfolio History|")
text = text.replace("|Rule 2: Past Purchases|", "|Past Purchases|")
text = text.replace("|Rule 3: Live Bidding Alerts|", "|Live Bidding Alerts|")

# Fix Block 8
text = text.replace("|1. Automated Production & Inventory Requirements|", "|Automated Production & Inventory Requirements|")
text = text.replace("|2. Advance Shipping Notices & Shipping Data|", "|Advance Shipping Notices & Shipping Data|")
text = text.replace("|3. Electronic Payment & EFT Confirmation|", "|Electronic Payment & EFT Confirmation|")

# Fix Diagram 2 Breakdown to include explicit Inputs, Core Processing Mechanisms, Decisioning Logic, Outputs
old_d2_breakdown = """### Explanatory Breakdown of Figure 10.1: Eight Unique Features of E-Commerce Technology

1. **Ubiquity**: Internet technology is available everywhere (at home, work, mobile, in-vehicle)."""

new_d2_breakdown = """### Explanatory Breakdown of Figure 10.1: Eight Unique Features of E-Commerce Technology
- **Inputs**: User interaction logs, standardized TCP/IP network packets, rich multimedia assets, buyer search queries, location tags, and peer social contributions.
- **Core Processing Mechanisms**: Ubiquitous cloud accessibility, cross-border standard data transmission protocols, rich media streaming engines, interactive two-way messaging, and user-generated content aggregation pipelines.
- **Decisioning Logic**: Algorithmic price transparency filtering, dynamic personalization scoring matching buyer profile vectors, search cost optimization models, and dynamic pricing rules.
- **Outputs**: Boundaryless global marketspace access, reduced transaction and search costs for consumers, customized merchant offerings, transparent price comparisons, and peer-to-peer social commerce feeds.

1. **Ubiquity**: Internet technology is available everywhere (at home, work, mobile, in-vehicle)."""

text = text.replace(old_d2_breakdown, new_d2_breakdown)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("fix_all_defects.py completed.")
