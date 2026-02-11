# Persona: The "Compliance-First AI Engineer"

* **Name:** David Chen
* **Role:** Senior Security Engineer / AI Governance Lead at a highly regulated firm (HealthTech, LegalTech, or GovTech).
* **Background:** Extensive experience in cybersecurity, GDPR/HIPAA compliance, and static analysis. He treats AI models as "untrusted components" by default.
* **Goal:** To deploy AI agents that are not just functional but **rigorously verifiable, auditable, and incapable of executing unauthorized actions**, specifically defending against sophisticated attacks like indirect prompt injection.

## Why David's Interests are Not Widely Covered

Current resources largely focus on *functionality* (making the agent work) rather than *restriction* (stopping it from doing the wrong thing). David needs defensive programming patterns specific to Pydantic AI that go beyond basic validation.

* **Missing Interest 1: "The Semantic Firewall Pattern"**
* **The Gap:** Most tutorials handle validation errors by simply asking the LLM to retry. David needs **deterministic failure modes**. He needs to know how to implement "circuit breakers" that trigger a hard stop or human intervention when a model consistently fails safety checks, rather than looping indefinitely.
* **Specific Question:** "How do I build a Pydantic `AfterValidator` that runs a secondary, lightweight classifier to detect PII or toxicity, and then *deterministically* sanitizes the output or kills the process before it ever leaves the agent scope?"

* **Missing Interest 2: "Audit-Grade Tracing & Replayability"**
* **The Gap:** While observability tools (like Logfire) exist, David needs **immutable audit logs** for legal discovery. He needs to serialize the *entire* state of an agent (including hidden context, tool outputs, and system prompt versions) into a format that can be cryptographically signed and replayed later to prove *why* an agent made a specific decision.
* **Specific Question:** "How can I architect a Pydantic AI agent to produce a 'verifiable execution proof'—a serialized artifact containing every prompt, tool call, and model response hash—that I can store in a WORM (Write Once Read Many) database for compliance audits?"

* **Missing Interest 3: "Defense Against Indirect Prompt Injection"**
* **The Gap:** Many tutorials show how to parse user input. David needs advanced patterns for **sanitizing retrieved content** (like web pages or emails) before it hits the prompt context. He needs to prevent "jailbreaks" embedded in external data from hijacking the agent.
* **Specific Question:** "What is the Pydantic AI pattern for 'sandboxing' retrieved context? How do I use a separate, restricted 'parser agent' to strip dangerous instructions from web content before passing safe, structured data to the main executive agent?"
