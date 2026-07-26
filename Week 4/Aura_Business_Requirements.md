# Week 4 Assignment - Business Requirements: Aura

---

## Cover Page (SWS Format)

**CIS599: Information Systems Capstone**

**Business Requirements Document: Aura**

**Prepared for:** [Insert Professor's Name]  
**Prepared by:** Gerrell  
**Date:** July 26, 2026  
**Course Title:** Information Systems Capstone (CIS599)  
**Institution:** Strayer University  

---

## 1. Project Overview

Aura is a rapidly growing Business-to-Consumer (B2C) e-commerce start-up specializing in technology-enabled sleep and bedding products, including customizable mattresses, ergonomic pillows, and wellness sleep-tracking accessories. Funded by a venture capital group, the company currently operates with 10 core corporate employees, generating $5 million in annual revenue. Over a two-year horizon, Aura is projected to expand its workforce to 30 corporate employees and scale annual revenue to $30 million.

To support this rapid expansion, Aura is relocating its corporate headquarters to a new, standalone, two-story facility. Currently, this physical building contains no pre-existing Information Technology (IT) hardware, network cabling, or security infrastructure. Furthermore, as customer order volume scales, Aura requires a robust IT infrastructure capable of handling high-volume online transactions without incurring massive warehousing overhead.

### Business Problems Solved
This project addresses three fundamental operational and technical challenges:
1. **Absence of Office IT Infrastructure:** The newly acquired two-story building lacks local area networking (LAN), wireless coverage, physical security gateways, and data backup systems necessary for staff operations.
2. **Scalability and Warehousing Overhead:** Maintaining physical inventory for large mattresses requires immense capital and logistics management. This project implements an automated, high-margin dropshipping model inspired by Wayfair, where custom mattress orders placed online are automatically routed via Application Programming Interfaces (APIs) to manufacturing partners who build and fulfill orders directly to consumers.
3. **Data Security and Regulatory Compliance:** Handling customer payment details, personal data, and customer service records requires strict compliance with Payment Card Industry Data Security Standards (PCI-DSS) and privacy regulations like the California Consumer Privacy Act (CCPA).

### Major Project Goals
The project encompasses five core strategic goals:
* **Goal 1:** Engineer and deploy a secure, high-speed physical network (Next-Gen Firewall, PoE switches, Wi-Fi 6 WAPs, RAID-10 NAS) within the new two-story corporate headquarters by Day 60.
* **Goal 2:** Establish a fully integrated, automated cloud e-commerce pipeline (Shopify Plus storefront connected to Katana ERP middleware) by Day 35.
* **Goal 3:** Achieve automated order-routing integrations with manufacturing partner API endpoints, eliminating manual order processing by Day 75.
* **Goal 4:** Ensure 99.99% storefront uptime, sub-2-second page load speeds, and strict PCI-DSS compliance prior to public launch.
* **Goal 5:** Successfully onboard all corporate employees on new collaboration, CRM, and secure remote access tools by Day 90.

### IT’s Role in the Project
The Information Technology department, led by the Chief Technology Officer (CTO), serves as the primary architect and execution layer for this initiative. IT is responsible for selecting, procuring, engineering, furnishing, installing, testing, and maintaining all software applications, cloud database environments, network hardware, and security protocols. Additionally, IT leads change control management, vendor API integrations, vendor SLA enforcement, and end-user cybersecurity training.

---

## 2. Functional Business Requirements (Scope) and Scope Control

Defining functional business requirements establishes the boundary of what the information systems infrastructure must execute to satisfy operational goals.

### Functional Scope Matrix

| Area | Scope | Incorporation Strategies |
| :--- | :--- | :--- |
| **Applications** | Implementation of Shopify Plus (storefront/checkout), Katana ERP (order routing middleware), HubSpot CRM (customer support & 100-night sleep trial tracking), and Amazon RDS PostgreSQL (database). | Deploy SaaS platforms via cloud subscription models; configure single sign-on (SSO) and role-based access control (RBAC) across all applications. |
| **Sites** | Inclusion of the standalone two-story corporate office and primary AWS cloud hosting regions. | Install Cat6 structured cabling on both floors of the physical office; establish a Site-to-Site IPSec VPN connecting the office firewall to AWS cloud environments. |
| **Process Re-engineering** | Transition from manual order entry to 100% automated dropship dispatch. | Configure Katana ERP to capture Shopify order webhooks, transform order JSON payloads into supplier production formats, and transmit orders instantly via REST APIs. |
| **Customization** | Custom middleware API connectors for real-time inventory webhooks from mattress manufacturers. | Develop modular Python-based API wrapper scripts hosted on AWS Lambda to translate inventory feeds between supplier systems and Katana ERP. |
| **Interfaces** | Integration of Shopify REST API, Katana ERP API, HubSpot Webhooks, and PCI-compliant Payment Gateway APIs. | Utilize secure RESTful web services with OAuth 2.0 authentication and TLS 1.3 encryption for all data exchanges between systems. |
| **Architecture** | Hybrid cloud (SaaS/IaaS) and on-premise physical network architecture. | Host core business applications in cloud environments for maximum uptime; maintain local physical switches, access points, and NAS backups at headquarters. |
| **Conversion** | Migration of existing customer profiles, order histories, and active product catalog data ($5M baseline). | Perform data cleansing, construct CSV/JSON data transformation scripts, and execute trial data loads into Amazon RDS PostgreSQL during sandbox testing. |
| **Testing** | End-to-end unit testing, API payload integration testing, network failover testing, and User Acceptance Testing (UAT). | Execute automated postman API tests, conduct simulated ISP link failovers, run security penetration scans, and perform UAT with 5 core business users. |
| **Funding** | Project budget strictly capped at $150,000 capital and operational expenditure. | Enforce cost tracking per phase in MS Project; require CTO approval for all hardware purchase orders and software subscription tier changes. |
| **Training** | Comprehensive staff onboarding for HubSpot CRM, Google Workspace, Slack, and secure remote VPN access. | Conduct mandatory hands-on workshops during Phase 5 (Days 76–82) and distribute interactive user manuals and video guides. |
| **Education** | Mandatory employee cybersecurity, data privacy, and phishing awareness education. | Partner with a third-party security platform (e.g., KnowBe4) to deliver automated security modules and simulated phishing tests prior to go-live. |

### Scope Control Process
Scope creep represents a major risk to the 90-day timeline and $150,000 budget cap. To control changes:
1. **Change Request Submission:** Any proposed change to functional scope must be submitted via a formal Change Request (CR) form detailing the operational justification.
2. **CTO & Technical Assessment:** The IT department evaluates the proposed change against cost, schedule, security, and architectural impacts.
3. **Change Advisory Board (CAB) Review:** The executive team (CEO, CTO, and Venture Partner representative) reviews all CRs impacting project timelines by more than 3 days or costs by more than $2,500.
4. **Approval & Sign-off:** Approved changes are logged in the master MS Project plan, and revised baseline schedules are distributed to team leads. Unapproved changes are deferred to post-launch maintenance sprints.

---

## 3. Non-functional Business Requirements (Governance, Risk, Compliance)

Non-functional requirements specify the operational quality, security, and governance standards the infrastructure must sustain.

### Governance
1. **IT Steering Committee & Policy Enforcement:** Establish an IT Steering Committee that meets bi-weekly to align project milestones with business growth goals and audit compliance.
2. **Role-Based Access Control (RBAC):** Implement strict least-privilege access across all cloud systems (Shopify, ERP, AWS RDS) using Okta SSO and mandatory Multi-Factor Authentication (MFA).
3. **Asset Lifecycle & Version Control:** Maintain a centralized inventory of all corporate laptops, network appliances, and software licenses, ensuring routine security patching.

### Risk
1. **High Availability & Storefront Uptime:** The cloud e-commerce platform must maintain a minimum uptime SLA of 99.99% (less than 52 minutes of unscheduled downtime per year).
2. **Automated Multi-Zone Database Replication:** Amazon RDS PostgreSQL must be deployed in a Multi-AZ (Availability Zone) configuration to ensure instant automatic failover if a primary cloud data center fails.
3. **Redundant Data Backups:** Daily automated cloud snapshots must be retained for 30 days. On-site corporate assets must back up nightly to a local RAID-10 NAS device, with encrypted offsite mirror copies stored in AWS S3.

### Compliance
1. **PCI-DSS Compliance:** All credit card processing must be offloaded to Level 1 PCI-compliant payment gateways (Shopify Payments / Stripe), ensuring credit card numbers are never stored on Aura's local servers.
2. **Data Privacy (CCPA/GDPR):** System architecture must support customer data privacy rights, including opt-out management, data anonymization, and automated "right-to-be-forgotten" data deletion requests.
3. **Vendor Security Standards:** All external SaaS providers and manufacturing partners must maintain active SOC 2 Type II compliance certifications.

### Other Performance & Scalability Requirements
* **Response Time SLA:** Web storefront page load time must not exceed 2.0 seconds under normal load, and API inventory sync latency must remain under 5.0 seconds.
* **Peak Load Handling:** The infrastructure must dynamically scale to support 5x normal traffic volume during promotional sales without performance degradation.

---

## 4. Technical Requirements for Integration of E-commerce Components

To seamlessly connect customers, corporate staff, and manufacturing partners, five critical technical integration requirements must be satisfied:

1. **RESTful Middleware API Integration (Shopify to Katana ERP):** High-throughput, bi-directional RESTful APIs must connect Shopify Plus with Katana ERP. When an order is completed, a JSON webhook payload containing order line items, customer address, and SKU details must be transmitted to Katana within 2 seconds.
2. **Secure Site-to-Site IPSec VPN Tunnel:** A hardware-based IPSec VPN tunnel must be configured on the office Next-Gen Firewall (NGFW), establishing an encrypted bridge between the physical two-story building LAN and the private AWS VPC hosting Amazon RDS.
3. **Manufacturing Partner Automated Dropship Endpoints:** Katana ERP must transform order payloads into standardized XML/JSON formats accepted by supplier fulfillment endpoints. Automated ACK (Acknowledgement) and tracking number feeds must be ingested from suppliers and updated back to Shopify.
4. **Single Sign-On (SSO) & Multi-Factor Authentication (MFA):** All internal enterprise applications (Google Workspace, HubSpot, Slack, Katana, AWS Console) must integrate with Okta SSO, enforcing TOTP-based MFA for all 10 corporate staff members.
5. **Centralized Data Warehouse Pipeline:** An automated ETL (Extract, Transform, Load) pipeline must extract daily transactional records from Shopify, Katana ERP, and HubSpot into Snowflake, enabling real-time executive dashboard reporting.

---

## 5. Potential Risks, Constraints, and Assumptions

### Risk Management Matrix

| Risk # | Identified Risk | Impact & Severity | Preventative / Mitigating Strategies |
| :---: | :--- | :---: | :--- |
| **Risk #1** | **Manufacturing Partner API Downtime:** External supplier APIs experience outages or payload format changes, blocking dropship dispatch. | **High** | Implement an asynchronous queueing system in Katana ERP with automated retry logic, exponential backoff, and instant IT alert notifications. |
| **Risk #2** | **Hardware Procurement Delays:** Supply chain bottlenecks delay arrival of office firewalls, PoE switches, or WAPs. | **High** | Pre-order core networking hardware during Days 16–20 (Phase 2) from primary and secondary vendors with guaranteed lead times. |
| **Risk #3** | **Security Breach / Data Leak:** Unauthorized access to customer personal data or corporate endpoints. | **Critical** | Enforce NGFW intrusion prevention (IPS), endpoint protection (EDR) on all laptops, network segmentation, mandatory MFA, and AES-256 encryption. |
| **Risk #4** | **Office Cabling Installation Delays:** Structural issues in the two-story building delay Cat6 wiring placement. | **Medium** | Contract licensed structured cabling technicians in Phase 1 (Days 1–15) to perform site surveys before cable pulling begins in Phase 3. |
| **Risk #5** | **Scope Creep & Budget Overrun:** Additional feature requests exceed the $150,000 budget cap or 90-day window. | **High** | Enforce strict Change Advisory Board (CAB) approval protocols for any scope modifications affecting cost or schedule. |

### Project Constraints
* **Budget Constraint:** Total capital and operational expenditure is strictly capped at **$150,000**.
* **Schedule Constraint:** All IT systems and office networking must be operational within a non-negotiable **90-day window**.
* **Physical Facility Constraint:** Cable runs and access point placements are bounded by the architectural layout of the new two-story standalone building.

### Project Assumptions
* **Assumption 1:** High-speed commercial business fiber internet (minimum 1 Gbps symmetric connection) is available for installation at the new building site.
* **Assumption 2:** Manufacturing partners maintain stable RESTful or SOAP API interfaces for dropship order processing.
* **Assumption 3:** Venture capital funding of $5 million remains secured and accessible throughout the 90-day implementation period.

---

## 6. Sources (SWS Format)

1. McKinsey & Company. (2020). *Retail Operations 2020: The Next Horizon*. McKinsey Publications. Provides insights into modern omni-channel retail operations, automated fulfillment strategies, and digital supply chain integration.
2. ValueWalk. (2020). *Top 10 Largest Ecommerce Companies in the US in 2020*. ValueWalk Business Analysis. Used to guide the business model selection and dropshipping operational architecture modeled after major e-commerce leaders.
3. Laudon, K. C., & Laudon, J. P. (2020). *Management Information Systems: Managing the Digital Firm* (16th ed.). Pearson. Foundational text outlining information systems design, network security, risk management, and systems integration principles.
