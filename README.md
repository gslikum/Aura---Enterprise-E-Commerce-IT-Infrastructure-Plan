# Aura - Enterprise E-Commerce IT Infrastructure Plan

This repository showcases the comprehensive, 90-day Information Systems Project Plan for **Aura**, a premium sleep-wellness e-commerce start-up. Designed from the perspective of the Chief Technology Officer (CTO), this project outlines the strategy for establishing a scalable IT infrastructure to support a rapidly growing business.

---

## 🚀 Business Profile: Aura
Aura is an innovative e-commerce startup specializing in technology-enabled sleep and bedding systems (mattresses, accessories, and wellness sleep tracking).
* **Current Status:** 10 core corporate employees | $5 Million annual revenue
* **2-Year Projections:** 30 core corporate employees | $30 Million annual revenue
* **Facility:** New standalone, two-story corporate headquarters (transitioning from no pre-existing IT infrastructure).
* **Supply Chain Model:** Hybrid dropship and light-inventory model inspired by Wayfair.

---

## 🛠 Tech Stack & Architecture
To support rapid scalability and eliminate warehousing overhead, Aura's technology system is designed as a hybrid cloud and on-premise model:

* **Storefront & Checkout:** Shopify Plus (Fully hosted SaaS, PCI-DSS compliant)
* **ERP & Integration Middleware:** Katana ERP (manages automated order routing to mattress manufacturing partners via APIs)
* **Customer Relationship Management (CRM):** HubSpot CRM (integrates sleep-trial tracking and marketing)
* **Database & Analytics:** Amazon RDS (PostgreSQL transactional database) & Snowflake Data Warehouse (Business Intelligence)
* **Physical Office IT:** Local Area Network (LAN) utilizing a Next-Generation Firewall (NGFW), managed PoE switches, and 5x Wi-Fi 6 wireless access points.
* **On-Site Storage:** Local NAS configured in a RAID-10 array for secure, redundant backups.

---

## 📂 Project Milestones & Deliverables

### 📅 Week 2: Project Plan Inception
* **Core Proposal:** [Aura_Project_Plan_Inception.docx](./Week%202/Aura_Project_Plan_Inception.docx) — Fully formatted academic document (Times New Roman, double-spaced, 1-inch margins) featuring cover page, demographics, and technical systems details.
* **Source File:** [Aura_Project_Plan_Inception.md](./Week%202/Aura_Project_Plan_Inception.md) — Source text in Markdown.
* **Gantt Chart (Excel):** [Part_2_Gantt_Chart.xlsx](./Week%202/Part_2_Gantt_Chart.xlsx) — Interactive project tracker with WBS, durations, predecessors, and a cell-colored visual bar chart.
* **Gantt Chart (XML):** [Part_2_Gantt_Chart.xml](./Week%202/Part_2_Gantt_Chart.xml) — Direct MS Project file for importing into Microsoft Project.

#### Systems Infrastructure Diagram
Below is the system block diagram showing customer interactions, secure administrative pathways, API dropship logic, and local office hardware setup.

```mermaid
graph TD
    subgraph internet ["Public Internet"]
        Customer[Customer Web/Mobile Browser]
    end

    subgraph cloud ["Cloud Infrastructure (Hosted SaaS)"]
        Shopify[Shopify Plus Storefront & Payment Gateway]
        ERP[Katana ERP / Integration Middleware]
        RDS[(Amazon RDS - PostgreSQL Database)]
        HubSpot[HubSpot CRM & Support]
    end

    subgraph partners ["Manufacturing Partners (External)"]
        Supplier[Mattress Manufacturing Facility - API Integrations]
    end

    subgraph office ["Corporate Office (Two-Story Facility)"]
        FW[Next-Gen Firewall / Security Gateway]
        Switch[Managed PoE Switches]
        WAP[Wi-Fi 6 Access Points]
        NAS[(Local NAS Backup)]
        Staff[Staff Laptops & Devices]
    end

    %% Connections
    Customer -->|1. Browses & Purchases| Shopify
    Shopify -->|2. Writes Orders| RDS
    Shopify -->|3. Routes Order| ERP
    ERP -->|4. Dropship Request via API| Supplier
    Shopify -->|5. Syncs Lead Data| HubSpot
    
    FW -->|Secure Admin Access| Shopify
    FW -->|Secure Admin Access| ERP
    FW -->|Secure Admin Access| RDS
    
    FW --- Switch
    Switch --- WAP
    Switch --- NAS
    WAP --- Staff
```

#### 90-Day Implementation Timeline
The IT rollout schedule is represented below using native Markdown Gantt syntax:

```mermaid
gantt
    title Aura IT Infrastructure Implementation
    dateFormat  YYYY-MM-DD
    axisFormat  %m-%d

    section Phase 1: Planning
    Finalize Office Layout & Server Room  :active, t1, 2026-07-15, 5d
    Procure ISP Business Broadband       : t2, after t1, 5d
    Draft Hardware Bill of Materials (BoM) : t3, after t2, 5d

    section Phase 2: Procurement & Cloud
    Order Hardware & Laptops             : t4, after t3, 5d
    Provision Shopify Sandbox & DBs     : t5, after t4, 8d
    Integrate Katana ERP Middleware      : t6, after t5, 7d

    section Phase 3: Physical Setup
    Install Cat6 Ethernet Cabling        : t7, after t4, 10d
    Mount Switches & Access Points       : t8, after t7, 10d
    Configure Firewall & VPN Access      : t9, after t8, 5d

    section Phase 4: System Testing
    End-to-End Order Integration Tests   : t10, after t6, 8d
    Network Performance & Failover Tests : t11, after t9, 4d
    Configure Local NAS Backups          : t12, after t8, 3d

    section Phase 5: Handoff & Go-Live
    Onboard & Train Core Staff           : t13, after t11, 7d
    Beta Storefront Launch               : t14, after t10, 6d
    Project Handoff & Go-Live            : t15, after t14, 2d
```

---

### 📅 Week 4: Business Requirements
*🔓 Unlocks in Week 4*

---

### 📅 Week 6: Infrastructure Design
*🔓 Unlocks in Week 6*

---

### 📅 Week 8: System Implementation
*🔓 Unlocks in Week 8*

---

### 📅 Week 10: Comprehensive Project Plan & Executive Presentation
*🔓 Unlocks in Week 10*
