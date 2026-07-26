import re

target_path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(target_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. FIX MERMAID BLOCK 5: Remove "Click 1:", "Click 2:", etc.
old_block5 = """```mermaid
flowchart TD
    C1[Click 1: User Arrives via Search Portal] --> C2[Click 2: User Selects Apparel Category]
    C2 --> C3[Click 3-5: User Views Specific Item, Size & Color]
    C3 --> C4[Click 6: User Abandons Cart without Purchasing]
    C4 --> Net[Tracking Beacons & Cookies Transmit Profile to Ad Network]
    Net --> RTB[Real-Time Bidding Exchange Auctions User Profile]
    RTB --> Retarget[Ad Retargeting: Product Ads Follow User Across External Websites]
```"""

new_block5 = """```mermaid
flowchart TD
    C1[Initial Arrival: User Arrives via Search Portal] --> C2[Category Selection: User Selects Apparel Category]
    C2 --> C3[Item Inspection: User Views Specific Item, Size & Color]
    C3 --> C4[Cart Abandonment: User Abandons Cart without Purchasing]
    C4 --> Net[Tracking Beacons & Cookies Transmit Profile to Ad Network]
    Net --> RTB[Real-Time Bidding Exchange Auctions User Profile]
    RTB --> Retarget[Ad Retargeting: Product Ads Follow User Across External Websites]
```"""

content = content.replace(old_block5, new_block5)

# 2. FIX MERMAID BLOCK 6: Remove "Rule 1:", "Rule 2:", "Rule 3:" from edge labels
old_block6 = """```mermaid
flowchart LR
    User[Web Visitor / Mobile User] <--> Server[E-Commerce Personalization Engine]

    Server -->|Rule 1: Portfolio History| Ad1[Financial Portal: Recommended Stock Portfolio Assets]
    Server -->|Rule 2: Past Purchases| Ad2[Book Store: Recommended Management Titles]
    Server -->|Rule 3: Live Bidding Alerts| Ad3[Auction Site: Bid Status on Specific Saved Items]
```"""

new_block6 = """```mermaid
flowchart LR
    User[Web Visitor / Mobile User] <--> Server[E-Commerce Personalization Engine]

    Server -->|Portfolio History| Ad1[Financial Portal: Recommended Stock Portfolio Assets]
    Server -->|Past Purchases| Ad2[Book Store: Recommended Management Titles]
    Server -->|Live Bidding Alerts| Ad3[Auction Site: Bid Status on Specific Saved Items]
```"""

content = content.replace(old_block6, new_block6)

# 3. FIX MERMAID BLOCK 7: Remove "1.", "2.", etc. from edge labels
old_block7 = """```mermaid
flowchart TD
    Consumer[Consumer Terminal] -->|1. Requests Web Page| Merchant[Network Merchant Site]
    Merchant -->|2. Relays Page Request| AdServer[Central Ad Server: Google Marketing Platform]
    AdServer <-->|3. Queries Cookie & User Profile| DB[(User Profile Database)]
    AdServer -->|4. Serves Targeted Banner Ad| Consumer
    Consumer <-->|5. Continuous Behavioral Tracking across Partner Sites| Network[Network Member Sites]
```"""

new_block7 = """```mermaid
flowchart TD
    Consumer[Consumer Terminal] -->|Requests Web Page| Merchant[Network Merchant Site]
    Merchant -->|Relays Page Request| AdServer[Central Ad Server: Google Marketing Platform]
    AdServer <-->|Queries Cookie & User Profile| DB[(User Profile Database)]
    AdServer -->|Serves Targeted Banner Ad| Consumer
    Consumer <-->|Continuous Behavioral Tracking across Partner Sites| Network[Network Member Sites]
```"""

content = content.replace(old_block7, new_block7)

# 4. FIX MERMAID BLOCK 8: Remove "1.", "2.", "3." from edge labels
old_block8 = """```mermaid
flowchart LR
    subgraph Supplier Systems
        S_DB[(Supplier Inventory & Order DB)]
    end

    subgraph Purchasing Firm Systems
        F_DB[(Firm Production & POS DB)]
    end

    F_DB -->|1. Automated Production & Inventory Requirements| S_DB
    S_DB -->|2. Advance Shipping Notices & Shipping Data| F_DB
    F_DB -->|3. Electronic Payment & EFT Confirmation| S_DB

    S_DB <-->|Continuous Replenishment Loop| F_DB
```"""

new_block8 = """```mermaid
flowchart LR
    subgraph Supplier Systems
        S_DB[(Supplier Inventory & Order DB)]
    end

    subgraph Purchasing Firm Systems
        F_DB[(Firm Production & POS DB)]
    end

    F_DB -->|Automated Production & Inventory Requirements| S_DB
    S_DB -->|Advance Shipping Notices & Shipping Data| F_DB
    F_DB -->|Electronic Payment & EFT Confirmation| S_DB

    S_DB <-->|Continuous Replenishment Loop| F_DB
```"""

content = content.replace(old_block8, new_block8)

# 5. RESTRUCTURE ALL 12 EXPLANATORY BREAKDOWN SECTIONS WITH UNIFORM INPUTS/PROCESSING/DECISIONING/OUTPUTS AND SEQUENTIAL FIGURE HEADERS (10.0 to 10.11)

# Diagram 1 Breakdown
old_breakdown1 = """### Explanatory Breakdown of Figure 10.0: Car Dashboard System Architecture
- **Inputs & Drivers**: Business challenges drive management decision-making (designing revenue models), organizational strategy (establishing privacy guidelines and safety-compliant interfaces), and technological investment (in-vehicle display hardware, Android Auto, Apple CarPlay, Android Automotive, and proprietary vehicle OS environments).
- **Core Processing Mechanisms**: The **Dashboard Infotainment Information System** ingests vehicle telemetry, GPS positioning, driver preferences, and merchant offerings. It processes these data feeds to serve real-time location-based advertisements, analyze driving behavior, recommend preventive maintenance, and process payments (e.g., automated coffee ordering or toll/gas payments).
- **Outputs & Value Realization**: Outputs include new monetization streams (ad placement fees, transaction commissions), heightened customer intimacy, and brand engagement. Data privacy concerns and safety risks feedback into ongoing managerial and regulatory evaluation."""

new_breakdown1 = """### Explanatory Breakdown of Figure 10.0: Car Dashboard System Architecture
- **Inputs**: Vehicle telemetry sensors, GPS geolocation coordinates, driver preference profiles, ambient noise audio, and sponsor merchant advertising feeds.
- **Core Processing Mechanisms**: The **Dashboard Infotainment Information System** processes data through vehicle operating systems (Android Automotive, Apple CarPlay, vw.OS) and cloud middleware APIs.
- **Decisioning Logic**: Real-time contextual algorithms evaluate driving speed, route proximity, and user privacy constraints to select non-distracting, safety-compliant in-car offers.
- **Outputs**: Rendered dynamic location-based ads, automated maintenance alerts, voice-guided transaction confirmations (gas/coffee payments), and high-margin data monetization streams."""

content = content.replace(old_breakdown1, new_breakdown1)

# Diagram 2 Breakdown
old_breakdown2 = """### Explanatory Breakdown of Figure 10.1: Eight Unique Features of E-Commerce Technology

1. **Ubiquity**: Internet technology is available everywhere (at home, work, mobile, in-vehicle).
   - *Business Impact*: Creates a **marketspace**—a marketplace extended beyond traditional temporal and physical boundaries. Consumers can shop 24/7/365 from any location. Significantly lowers consumer **transaction costs** (the time, effort, and financial costs of participating in a market).
2. **Global Reach**: Technical standards enable cross-border commercial transactions without modification.
   - *Business Impact*: Marketspace potential equals the world’s online population (billions of consumers). Breaks local/regional market limitations faced by traditional media.
3. **Universal Standards**: A single set of global technical standards (Internet/TCP/IP protocols).
   - *Business Impact*: Disparate computing systems communicate effortlessly. Drastically lowers **market entry costs** for merchants and **search costs** for consumers looking for goods.
4. **Richness**: Ability to deliver complex visual, audio, and text marketing messages simultaneously to large audiences.
   - *Business Impact*: Overcomes the traditional tradeoff between reach and richness. Merges the rich sensory experience of physical retail with global digital scale.
5. **Interactivity**: Technology enables dynamic, two-way communication between seller and buyer, as well as peer-to-peer sharing.
   - *Business Impact*: Engages consumers in a active dialogue, matching retail experience while customizing messages to individual preferences.
6. **Information Density**: Drastically increases total amount and quality of information available to all market participants.
   - *Business Impact*: Elevates **price transparency** (consumers knowing exact product prices) and **cost transparency** (consumers discovering actual production costs). Enables merchants to engage in **dynamic pricing** (altering prices based on demand/supply metrics).
7. **Personalization & Customization**: Permits merchants to target marketing messages to specific individuals by adjusting message to person’s name, interests, and past purchases.
   - *Business Impact*: Customizes product features and services to individual buyer preferences.
8. **Social Technology**: Enables user-generated content creation and distribution across social networks.
   - *Business Impact*: Shifts content creation from traditional centralized broadcast networks to decentralized peer-to-peer social communities."""

new_breakdown2 = """### Explanatory Breakdown of Figure 10.1: Eight Unique Features of E-Commerce Technology
- **Inputs**: User interaction logs, standardized TCP/IP network packets, rich multimedia assets, buyer search queries, location tags, and peer social contributions.
- **Core Processing Mechanisms**: Ubiquitous cloud accessibility, cross-border standard data transmission protocols, rich media streaming engines, interactive two-way messaging, and user-generated content aggregation pipelines.
- **Decisioning Logic**: Algorithmic price transparency filtering, dynamic personalization scoring matching buyer profile vectors, search cost optimization models, and dynamic pricing rules.
- **Outputs**: Boundaryless global marketspace access, reduced transaction and search costs for consumers, customized merchant offerings, transparent price comparisons, and peer-to-peer social commerce feeds."""

content = content.replace(old_breakdown2, new_breakdown2)

# Diagram 3 Breakdown
old_breakdown3 = """### Explanatory Breakdown of Figure 10.2: Benefits of Disintermediation
- **Layer 1 (Traditional 3-Tier Distribution)**: A manufacturer produces a sweater at a cost of $10.00. The distributor marks up the product to cover wholesale overhead and profit, selling to the retailer for $15.00. The retailer adds store markup and overhead, setting a final price of $48.50 to the consumer. Intermediary markups account for over 380% of the original production cost.
- **Layer 2 (Single-Tier Removal)**: Bypassing the wholesaler/distributor allows the manufacturer to sell directly to a retail entity for $20.00, reducing the final consumer price to $40.34.
- **Layer 3 (Direct-to-Consumer Disintermediation)**: The manufacturer operates an e-commerce platform, selling directly to the customer for $20.45. The consumer saves $28.05 (a 58% reduction), while the manufacturer retains double its traditional margin ($10.45 profit vs traditional wholesaler margin)."""

new_breakdown3 = """### Explanatory Breakdown of Figure 10.2: Benefits of Disintermediation
- **Inputs**: Manufacturer production cost metrics ($10.00 base cost), wholesaler markup allocations ($15.00), retailer operational markups ($25.00), and final consumer pricing demand ($48.50 vs $20.45).
- **Core Processing Mechanisms**: Direct-to-consumer e-commerce ordering systems, automated warehouse picking, and digital payment processing replacing multi-tier wholesale and retail distributor steps.
- **Decisioning Logic**: Channel cost evaluation logic determining whether intermediary distribution tiers add sufficient value or create price inflation, routing orders directly from factory floor to end buyers.
- **Outputs**: Complete elimination of intermediary overhead layers, 58% price reduction for end consumers ($20.45 direct price), and doubled profit margins retained by original manufacturers ($10.45 direct margin)."""

content = content.replace(old_breakdown3, new_breakdown3)

# Diagram 4 Breakdown
old_breakdown4 = """### Explanatory Breakdown of Figure 10.4: FinTech Underwriting vs. Traditional Banking
- **Inputs & Data Streams**: Traditional banking relies on manual, paper-based application forms, physical tax returns, credit bureau scores, and fixed collateral appraisals. In contrast, FinTech underwriting ingests real-time point-of-sale (POS) and payment gateway transaction streams (e.g., Square, PayPal, Kabbage) tracking live daily cash flows, customer transaction frequency, return rates, and chargeback history.
- **Core Processing Mechanisms & Risk Scoring**: Traditional underwriting relies on human loan officers performing manual credit checks and committee reviews across a multi-week timeline. FinTech machine underwriting employs automated machine-learning algorithms that continuously audit seller performance metrics, dynamic cash-flow volatility, and sales trends to calculate instant risk scores without manual human intervention.
- **Decisioning & Algorithmic Offers**: Traditional bank systems output binary, high-threshold approval or rejection decisions for fixed-term, high-value loans. FinTech platforms generate automated, pre-approved loan offers directly within merchant management dashboards, enabling 1-click acceptance.
- **Outputs & Settlement Models**: Traditional loans require fixed monthly principal and interest payments backed by collateral assets. FinTech capital disbursement occurs within 24 hours ("Next-Day Capital Deposit"), and repayment is automatically settled via a fixed daily percentage deduction from ongoing credit card sales, aligning debt service directly with merchant revenue velocity."""

new_breakdown4 = """### Explanatory Breakdown of Figure 10.3: FinTech Underwriting vs. Traditional Banking
- **Inputs**: Real-time point-of-sale (POS) transaction streams (Square, PayPal), historical cash flow velocity, chargeback rates, return metrics vs traditional paper credit applications and collateral appraisals.
- **Core Processing Mechanisms**: Automated machine-learning credit risk scoring models auditing daily sales volume and cash flow volatility vs manual human loan officer committee reviews.
- **Decisioning Logic**: Automated real-time risk threshold evaluation determining pre-approved loan amounts and dynamic fee structures without requiring fixed physical collateral.
- **Outputs**: 24-hour capital disbursement ("Next-Day Capital Deposit"), 1-click dashboard approval offers, and automated daily percentage deductions from ongoing credit card sales."""

content = content.replace(old_breakdown4, new_breakdown4)

# Diagram 5 Breakdown
old_breakdown5 = """### Explanatory Breakdown of Figure 10.3: Visitor Tracking Architecture
- **Step 1 (Arrival & Referral Log)**: The consumer lands on an e-commerce home page via a search engine link. Web analytics log the entry portal, timestamp (2:30 PM), IP location, operating system, and browser header. Tracking cookies are dropped onto the browser.
- **Step 2 (Category Navigation)**: The user navigates to the women's apparel section, demonstrating category intent.
- **Step 3 (Item Selection)**: The user inspects a specific size 10 pink blouse and adds it to the shopping cart. Data systems record color, size, and pricing preference.
- **Step 4 (Cart Abandonment)**: The user closes the tab prior to checkout. This signal highlights potential usability issues, high shipping fees, or hesitation.
- **Step 5 (Cross-Site Retargeting)**: Ad network beacons (e.g., Google Marketing Platform) broadcast the abandoned pink blouse profile. When the user visits external news or social sites, automated retargeting engines serve dynamic ads featuring that exact pink blouse."""

new_breakdown5 = """### Explanatory Breakdown of Figure 10.4: Visitor Tracking Architecture
- **Inputs**: User entry portal referrer data, timestamp, IP geolocation, browser headers, clicked product attributes (blouse size 10, pink color), and cart status signals.
- **Core Processing Mechanisms**: E-commerce analytics engines, cookie tracking beacons, ad network profile synchronization, and real-time bidding (RTB) exchange auctions.
- **Decisioning Logic**: Abandonment detection rules evaluating uncompleted checkout sessions and retargeting bidding algorithms matching user intent with advertiser product catalogs.
- **Outputs**: Broadcast abandoned cart profiles, dynamic retargeted product display ads rendered across partner web/social properties, and optimized conversion recovery pipelines."""

content = content.replace(old_breakdown5, new_breakdown5)

# Diagram 6 Breakdown
old_breakdown6 = """### Explanatory Breakdown of Figure 10.4: Dynamic Personalization
- **Processing Logic**: When a user authenticates or presents an identified tracking cookie, the web application queries customer databases, transaction histories, and predictive models.
- **Dynamic Content Generation**: Rather than serving generic homepages, the system renders customized modules: financial news outlets display portfolio-aligned market alerts; bookstores present personalized book recommendations based on reading history; auction platforms display real-time status of active user watchlist items."""

new_breakdown6 = """### Explanatory Breakdown of Figure 10.5: Dynamic Personalization
- **Inputs**: Authenticated user credentials, cookie session identifiers, historical purchase records, real-time browsing behavior, active watchlist items, and recommendation model embeddings.
- **Core Processing Mechanisms**: Personalization decision engines querying customer relational databases, market basket analysis models, and live auction bidding state feeds.
- **Decisioning Logic**: Conditional business rule matching (e.g., Portfolio History -> Financial Portal Alerts; Past Purchases -> Recommended Management Titles; Live Bidding -> Watchlist Status Updates).
- **Outputs**: Real-time custom rendered homepages, targeted banner advertisements, personalized product recommendations, and dynamic notification widgets."""

content = content.replace(old_breakdown6, new_breakdown6)

# Diagram 7 Breakdown
old_breakdown7 = """### Explanatory Breakdown of Figure 10.5: Ad Network Architecture
- **Step 1**: A consumer requests a Web page from an publisher site belonging to an ad network.
- **Step 2**: The merchant site server communicates with the network’s central ad server (e.g., Google Marketing Platform).
- **Step 3**: The ad server reads the consumer’s tracking cookie and queries the database for user demographics, search history, and behavioral interests.
- **Step 4**: Based on algorithmic scoring, the ad server selects a behaviorally targeted ad and renders it on the user's screen in milliseconds.
- **Step 5**: As the consumer browses other member sites, tracking cookies log user movements, continuously refining the behavioral database profile."""

new_breakdown7 = """### Explanatory Breakdown of Figure 10.6: Ad Network Architecture
- **Inputs**: Consumer web page requests, merchant site publisher calls, tracking cookie identifiers, user profile database records, and advertiser campaign bids.
- **Core Processing Mechanisms**: Central ad server request handling (Google Marketing Platform), database querying across demographic/behavioral profiles, algorithmic auction scoring, and cross-site tracking.
- **Decisioning Logic**: Real-time ad placement scoring selecting the optimal target ad based on publisher context, user demographic match, and highest advertiser bid price within milliseconds.
- **Outputs**: Targeted banner ads served directly to consumer terminals, continuous cross-site clickstream logging, and updated user behavioral database profiles."""

content = content.replace(old_breakdown7, new_breakdown7)

# Diagram 8 Breakdown
old_breakdown8 = """### Explanatory Breakdown of Figure 10.6: EDI System Integration
- **Processing Flow**: EDI standard formats structure data fields across industry supply chains. Instead of manual purchasing agents issuing POs, the buyer's production management system automatically transmits real-time inventory requirements to the supplier.
- **Automated Fulfillment**: The supplier system receives the EDI transmission, schedules manufacturing/warehouse picking, and responds with automated advance shipping notices.
- **Settlement**: Upon delivery confirmation, electronic funds transfer (EFT) payment signals complete the loop without manual paper intervention."""

new_breakdown8 = """### Explanatory Breakdown of Figure 10.7: EDI System Integration
- **Inputs**: Real-time point-of-sale (POS) store sales, warehouse stock thresholds, automated production schedule requirements, and standardized EDI document formats (ANSI X12 / EDIFACT).
- **Core Processing Mechanisms**: Direct system-to-system computer data transmission between buyer ERP/WMS systems and supplier inventory databases, eliminating manual purchase order creation.
- **Decisioning Logic**: Automated replenishment threshold triggers generating advance shipping notices (ASN) and Electronic Funds Transfer (EFT) payment authorizations based on inventory level rules.
- **Outputs**: Automated inventory replenishment shipments, advance shipping notices, digital invoice reconciliation, and direct EFT bank settlements."""

content = content.replace(old_breakdown8, new_breakdown8)

# Diagram 9 Breakdown
old_breakdown9 = """### Explanatory Breakdown of Figure 10.7: Private Industrial Network Architecture
- **Structure**: Owned and operated by a dominant buyer (e.g., VW Group Supply handling 90% of global Volkswagen purchasing).
- **Functionality**: Goes beyond basic transactional buying to enable deep joint collaborative commerce: sharing product design engineering, joint demand forecasting, inventory visibility, production scheduling, and unstructured project communication."""

new_breakdown9 = """### Explanatory Breakdown of Figure 10.8: Private Industrial Network Architecture
- **Inputs**: Strategic buyer enterprise requirements (e.g., Volkswagen Group), Tier 1 component supplier capacity data, raw material specs, logistics tracking feeds, and dealership inventory reports.
- **Core Processing Mechanisms**: Centralized private exchange extranet platform facilitating collaborative engineering design, joint demand forecasting, shared inventory visibility, and unstructured project communications.
- **Decisioning Logic**: Collaborative supply chain decisioning balancing joint production schedules, supplier allocation quotas, and component engineering changes across long-term partner networks.
- **Outputs**: Synchronized global supply chain schedules, reduced procurement overhead, joint product design revisions, and streamlined multi-tier logistics coordination."""

content = content.replace(old_breakdown9, new_breakdown9)

# Diagram 10 Breakdown
old_breakdown10 = """### Explanatory Breakdown of Figure 10.8: Net Marketplace Structure
- **Hub Services**: Provides digital product catalogs, supplier sourcing, automated RFQ (Request for Quotation) bidding, order consolidation, payment processing, and fulfillment tracking.
- **Classification Dimensions**:
  - **Direct Goods**: Materials directly used in production (e.g., sheet steel for auto bodies).
  - **Indirect Goods**: Maintenance, repair, and operating (MRO) supplies not built into final products (e.g., office supplies, lubricants).
  - **Contractual Purchasing**: Long-term sourcing relationships built on negotiated volume discounts (e.g., Exostar aerospace hub).
  - **Spot Purchasing**: Purchasing goods based on immediate short-term needs, often with volatile dynamic pricing."""

new_breakdown10 = """### Explanatory Breakdown of Figure 10.9: Net Marketplace Structure
- **Inputs**: Buyer Request for Quotations (RFQs), supplier product catalogs, spot market purchasing bids, and contract pricing agreements across direct and indirect goods categories.
- **Core Processing Mechanisms**: Digital e-hub platform services aggregating hundreds of buyers and suppliers, providing centralized product catalogs, automated RFQ matching, order consolidation, and settlement.
- **Decisioning Logic**: Marketplace matching algorithms evaluating contract vs spot purchasing terms, pricing thresholds, supplier ratings, and volume discount brackets.
- **Outputs**: Consolidated purchase orders, competitive RFQ supplier bids, automated payment processing, fulfillment tracking metrics, and market clearing price transparency."""

content = content.replace(old_breakdown10, new_breakdown10)

# Diagram 11 Breakdown
old_breakdown11 = """### Explanatory Breakdown of Figure 10.9: Mobile Payment Systems

| Technology Type | Technical Mechanism & Process | Leading Market Examples |
| :--- | :--- | :--- |
| **Near Field Communication (NFC)** | Short-range wireless radio communication between NFC chips in mobile devices and merchant POS card readers. Exchanging encrypted tokenized credentials when held within inches. | Apple Pay, Google Pay, Samsung Pay |
| **QR Code Payment** | Scanning dynamic 2D barcodes using smartphone camera apps. The merchant display generates a transaction QR code scanned by the buyer, or the buyer app displays a barcode scanned by the merchant laser scanner. | Walmart Pay, Starbucks App, Target, Dunkin' |
| **Peer-to-Peer (P2P)** | Cloud-based software enabling direct transfer of funds between personal bank accounts or linked debit cards using phone numbers or email identifiers. | Venmo, Zelle, Cash App |"""

new_breakdown11 = """### Explanatory Breakdown of Figure 10.10: Mobile Payment Systems
- **Inputs**: User payment credentials (credit/debit cards), contactless NFC radio signals, 2D QR code scans, and mobile app P2P identifiers (phone/email).
- **Core Processing Mechanisms**: Mobile OS hardware secure element tokenization (Apple Pay / Google Pay), optical camera barcode reading algorithms, cloud software P2P bank routing (Venmo / Zelle), and PCI-DSS encrypted payment gateway authorization.
- **Decisioning Logic**: Biometric authentication rules (Face ID / Touch ID), tokenized security validation matching temporary payment tokens against account vaulted credentials, and fraud risk scoring.
- **Outputs**: Instant POS payment authorizations, digital transaction receipts, encrypted token exchanges, and direct bank account fund transfers.

| Technology Type | Technical Mechanism & Process | Leading Market Examples |
| :--- | :--- | :--- |
| **Near Field Communication (NFC)** | Short-range wireless radio communication between NFC chips in mobile devices and merchant POS card readers. Exchanging encrypted tokenized credentials when held within inches. | Apple Pay, Google Pay, Samsung Pay |
| **QR Code Payment** | Scanning dynamic 2D barcodes using smartphone camera apps. The merchant display generates a transaction QR code scanned by the buyer, or the buyer app displays a barcode scanned by the merchant laser scanner. | Walmart Pay, Starbucks App, Target, Dunkin' |
| **Peer-to-Peer (P2P)** | Cloud-based software enabling direct transfer of funds between personal bank accounts or linked debit cards using phone numbers or email identifiers. | Venmo, Zelle, Cash App |"""

content = content.replace(old_breakdown11, new_breakdown11)

# Diagram 12 Breakdown
old_breakdown12 = """### Explanatory Breakdown of Figure 10.10: Presence Architecture
- **Multi-Touchpoint Integration**: Modern buyers interact across diverse channels depending on context and device. A firm must maintain tailored platforms for each presence category.
- **Execution Activities**: Website presence relies on search and display marketing; email presence drives conversion via newsletters and cart recovery alerts; social presence fosters community engagement and brand trust; offline traditional media builds broad brand awareness and drives traffic to digital channels."""

new_breakdown12 = """### Explanatory Breakdown of Figure 10.11: Presence Architecture
- **Inputs**: Target audience demographic profiles, multi-channel customer touchpoint interactions, campaign marketing budgets, and media channel performance metrics.
- **Core Processing Mechanisms**: Multi-channel digital presence coordination across Web platforms (desktop/mobile), email automation systems, social media management tools, and offline media referrals.
- **Decisioning Logic**: Resource allocation logic mapping customer touchpoint intent to channel execution activities (e.g., SEO/SEM for web acquisition, cart recovery automation for email, brand engagement for social, exposure for offline).
- **Outputs**: Integrated multi-platform brand presence, cross-channel traffic conversion, social community engagement, and synchronized customer journey touchpoints."""

content = content.replace(old_breakdown12, new_breakdown12)

# Write back updated content
with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Remediation script executed successfully.")
