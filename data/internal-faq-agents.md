# FinServe — Internal FAQ for Customer Service Agents

**Document version:** 2.2  
**Effective date:** 1 January 2025  
**Classification:** INTERNAL — Not for client distribution  
**Approved by:** Head of Client Support, FinServe S.A.

---

## Scenario 1: Client Threatening to Leave (Churn Risk)

**Trigger:** Client states they want to close their account, switch to a competitor, or expresses strong dissatisfaction with FinServe's services.

### Steps to Follow

1. **Listen and acknowledge.** Let the client explain their frustration fully before responding. Use empathetic language: "I understand this is frustrating, and I want to help resolve this."
2. **Identify the root cause.** Ask open-ended questions to understand the real issue — is it pricing, service quality, a specific incident, or a competitor offer?
3. **Check the client's account in CRM.** Review:
   - Client tenure and product history.
   - Total revenue generated (loan interest, fees paid).
   - Any open complaints or recent negative interactions.
   - Payment history (is the client in good standing?).
4. **Offer a resolution within your authority:**
   - Fee waiver: You may waive fees up to **EUR 50** without approval.
   - If the issue is pricing, note the details and escalate to the **Team Lead** for a potential rate review or loyalty offer.
   - If the issue is service quality, apologise, log the incident in the CMS, and explain what corrective steps will be taken.
5. **If the client insists on leaving:** Do not argue. Inform them of the account closure process (written request required, 30-day notice period for credit facilities, settlement of outstanding balance). Log the churn reason in CRM under "Client Retention — Lost."
6. **Escalate if:** The client has a loan balance above **EUR 100,000**, is a client of more than 3 years, or mentions regulatory or legal action. Escalate to **Team Lead** immediately.

**System:** CRM (client history), CMS (log interaction).

---

## Scenario 2: First-Time Late Payment

**Trigger:** A client's payment is overdue for the first time (past the 5-day grace period).

### Steps to Follow

1. **Verify the payment status** in the Core Banking System (CBS). Confirm the payment was not received or is not pending (SEPA transfers can take up to 2 business days).
2. **Check if it is genuinely the first late payment.** Review the client's full payment history in CBS.
3. **Contact the client** by phone (preferred) or email within 1 business day of the grace period expiry.
   - Tone: Friendly and understanding. Assume it is an oversight, not intentional.
   - Script: "Hello [Client Name], this is [Your Name] from FinServe. I'm calling regarding your [product] payment that was due on [date]. We noticed it hasn't been received yet. Is everything alright? I'd like to help you get this sorted."
4. **If the client has a valid reason** (e.g., bank processing delay, temporary cash flow issue):
   - Offer a one-time payment deferral of up to **14 days** (available once per 12-month period, no fee). Process in CBS under "Payment Deferral — First Late."
   - If deferral is not needed, confirm the client will pay within 1–2 business days and note the commitment in CBS.
5. **If the client indicates financial difficulty:**
   - Do NOT discuss restructuring options yourself. Explain that FinServe has options to help and escalate to the **Collections Team** (Credit & Operations) by creating a referral in CBS.
   - Log the conversation in CMS with the tag "Financial Difficulty — Referral."
6. **Confirm the late payment fee.** A EUR 15 late fee has been automatically applied. For a first offence with a good payment history, you may request a fee reversal from the **Team Lead** (your authority does not cover late fee reversals).

**System:** CBS (payment status, deferral processing), CMS (log interaction), CRM (client notes).

---

## Scenario 3: Suspected Fraud

**Trigger:** Client reports unauthorised transactions, or you notice suspicious activity on an account (e.g., sudden large drawdowns, unusual patterns, identity inconsistencies).

### Steps to Follow

1. **Do NOT alert the potentially fraudulent party.** If the caller may not be the genuine account holder, do not reveal account details or confirm balances.
2. **Verify the caller's identity** using standard verification (client number, date of birth, registered email, and security question). If verification fails, politely end the call and log as "Failed Verification — Possible Fraud."
3. **If the genuine client reports fraud:**
   - Express concern and reassure the client: "I'm sorry to hear this. Let me help secure your account immediately."
   - Place a **temporary hold** on the affected product in CBS (you have authority to freeze drawdowns on credit lines and block invoice submissions).
   - Record all details of the suspected fraud (dates, amounts, how the client noticed).
4. **Escalate immediately** to the **Risk & Compliance Analyst** by:
   - Creating a "Fraud Alert" ticket in the CMS with priority **Critical**.
   - Sending an email to fraud@finserve.eu with the client number, description, and actions taken.
   - Calling the Risk & Compliance team directly at ext. 3050 if the suspected loss exceeds **EUR 5,000**.
5. **Inform the client** that the case has been escalated to the specialist fraud team and they will receive an update within **2 business days**. Provide the fraud team's direct email (fraud@finserve.eu) for any additional information.
6. **Do NOT:**
   - Attempt to investigate the fraud yourself.
   - Reverse any transactions without Risk & Compliance approval.
   - Share details of the investigation with anyone outside the fraud handling team.

**System:** CBS (account freeze), CMS (Fraud Alert ticket), Email (fraud@finserve.eu).

---

## Scenario 4: Complaint About an Employee

**Trigger:** Client files a complaint specifically about the behaviour, conduct, or actions of a FinServe employee.

### Steps to Follow

1. **Take the complaint seriously** regardless of the severity. Do not dismiss, minimise, or defend the employee.
2. **Record the details carefully:**
   - Name or description of the employee involved (if known).
   - Date, time, and channel of the interaction (phone, email, portal, in-person).
   - Specific description of the behaviour or action complained about.
   - Any witnesses or evidence (e.g., email thread, call recording reference).
3. **Acknowledge the complaint:** "Thank you for bringing this to our attention. We take complaints about our staff very seriously, and this will be reviewed thoroughly."
4. **Log the complaint in CMS** with the category **"Employee Conduct"** and priority **High**.
5. **Escalate immediately to the Head of Client Support.** Employee conduct complaints are always handled at Level 3 regardless of severity. Do NOT attempt to resolve or mediate yourself.
6. **Inform the client** that the complaint has been escalated to senior management and they will receive a response within **5 business days**.
7. **Do NOT:**
   - Share the complaint with the employee who is the subject of the complaint.
   - Provide the employee's full name, personal details, or schedule to the client.
   - Promise specific disciplinary outcomes.

**System:** CMS (Employee Conduct category), escalation to Head of Client Support.

---

## Scenario 5: Client Requests Data Erasure (GDPR Right to Erasure)

**Trigger:** Client requests that FinServe delete all their personal data, citing GDPR Article 17.

### Steps to Follow

1. **Acknowledge the request** and confirm the client's identity using standard verification.
2. **Check if the client has an active loan or credit facility** in CBS.
   - **If yes (active product):** Explain that FinServe is legally required to retain data for the duration of the contractual relationship and for a statutory period thereafter (5 years for KYC/AML, 10 years for financial records). The erasure request cannot be fully fulfilled while the product is active, but the client's marketing preferences will be updated immediately.
   - **If no (no active product):** Proceed with the erasure request.
3. **For eligible erasure requests:**
   - Log the request in CMS under **"GDPR — Erasure Request"** with priority **High**.
   - Forward the request to the **Data Protection Officer (DPO)** at dpo@finserve.eu within 1 business day.
   - Confirm to the client that the request has been received and will be processed within **30 calendar days**.
4. **What you should communicate to the client:**
   - Certain data may be retained where FinServe has a legal obligation (AML records, tax records). The DPO will provide a detailed response explaining what can and cannot be deleted.
   - The client has the right to lodge a complaint with the national data protection authority if unsatisfied.
5. **Do NOT:**
   - Delete any data yourself. All erasure is handled by the DPO and IT Security.
   - Promise complete deletion without checking for legal retention obligations.

**System:** CMS (GDPR — Erasure Request), Email (dpo@finserve.eu).

---

## Scenario 6: Client Requests Debt Restructuring

**Trigger:** Client contacts support requesting changes to their repayment schedule due to financial difficulty.

### Steps to Follow

1. **Listen with empathy.** Financial difficulty is stressful. Use supportive language: "I understand this is a difficult situation. Let's look at what options are available."
2. **Verify the client's identity and account status** in CBS. Check:
   - Current product and outstanding balance.
   - Payment history (how many payments missed, if any).
   - Whether the account is already in collections (Stage 2 or later).
3. **If the account is current or in Stage 1 (Soft Collection):**
   - Explain the three restructuring options:
     - **Extended term:** Up to 12 additional months.
     - **Interest-only period:** Up to 3 months.
     - **Reduced instalments:** Up to 40% reduction for up to 6 months.
   - Inform the client that a restructuring fee of **EUR 50** applies and that the restructured status will be reported to credit bureaus.
   - Ask the client to submit a written request via email (support@finserve.eu) or through the portal, including:
     - Brief explanation of the financial difficulty.
     - Preferred restructuring option.
     - Any supporting documentation (e.g., termination letter, medical certificate).
4. **If the account is in Stage 2 (Formal Collection) or later:**
   - Inform the client that the case is being handled by the **Collections Team** and provide the direct contact: collections@finserve.eu or +48 22 100 2030.
   - You may help the client draft the restructuring request, but the decision authority lies with the Collections Team.
5. **Processing:**
   - Log the interaction in CMS under **"Restructuring Request."**
   - Create a referral to the **Senior Credit Analyst** (loans up to EUR 100,000) or the **Credit Committee** (loans above EUR 100,000) in CBS.
   - Processing time: **5 business days** from receipt of the complete request.
6. **Follow up:** If the client has not submitted the written request within 5 business days, send a reminder email.

**System:** CBS (account status, referral), CMS (Restructuring Request), Email (support@finserve.eu).

---

## Quick Reference: Escalation Contacts

| Issue | Escalate To | Contact |
|---|---|---|
| Fee waiver > EUR 50 or rate review | Team Lead, Client Support | Internal ext. 2001 |
| Financial difficulty / restructuring | Collections Team, Credit & Operations | collections@finserve.eu / ext. 2030 |
| Suspected fraud | Risk & Compliance Analyst | fraud@finserve.eu / ext. 3050 |
| Employee conduct complaint | Head of Client Support | Internal ext. 2000 |
| GDPR / data erasure request | Data Protection Officer | dpo@finserve.eu / ext. 2050 |
| Regulatory or legal threat | Head of Client Support → COO | Internal ext. 2000 |
| Client with balance > EUR 100,000 threatening churn | Team Lead → Head of Client Support | Internal ext. 2001 → 2000 |
