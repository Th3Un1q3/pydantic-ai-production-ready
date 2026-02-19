# OWASP Top 10 for Large Language Model Applications (2025)

**Source:** [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
**Official List:** [https://genai.owasp.org/llm-top-10/](https://genai.owasp.org/llm-top-10/)

The OWASP Top 10 for LLM Applications project aims to educate developers, designers, architects, managers, and organizations about the potential security risks when deploying and managing Large Language Models.

## The Top 10 Entries (2025 Version)

### LLM01: Prompt Injection

Prompt injection vulnerabilities occur when an attacker manipulates the operation of a trusted LLM through crafted inputs. This can cause the LLM to execute unintended actions or bypass security controls. Direct injection overwrites system prompts, while indirect injection manipulates inputs from external sources.

### LLM02: Sensitive Information Disclosure

LLM applications may inadvertently reveal sensitive information, proprietary algorithms, or other confidential details through their output. This can result in unauthorized access to sensitive data, intellectual property theft, and privacy violations.

### LLM03: Supply Chain Vulnerabilities

The LLM supply chain can be compromised, leading to integration of vulnerable components or services. This includes third-party datasets, pre-trained models, and plugins that may contain vulnerabilities or malicious code.

### LLM04: Data and Model Poisoning

Attackers can manipulate the training or fine-tuning data, or the model itself, to introduce vulnerabilities, backdoors, or biases. This compromises the model's integrity and can lead to incorrect or harmful outputs.

### LLM05: Improper Output Handling

Improper output handling occurs when LLM outputs are accepted without scrutiny and passed directly to backend systems. This can lead to XSS, CSRF, SSRF, privilege escalation, or remote code execution on backend systems.

### LLM06: Excessive Agency

Excessive agency grants an LLM-based system the ability to interface with other systems and perform actions in response to unexpected or ambiguous prompts. This can lead to unauthorized actions or unintended consequences in downstream systems.

### LLM07: System Prompt Leakage

System prompt leakage occurs when an LLM reveals its internal system prompts or instructions. This can expose sensitive logic, business rules, or prompt engineering strategies to attackers.

### LLM08: Vector and Embedding Weaknesses

Weaknesses in vector embeddings or the vector database can be exploited to manipulate retrieval mechanisms or bypass security controls. This can lead to information retrieval errors or unauthorized access.

### LLM09: Misinformation

LLMs can generate plausible but false information (hallucinations). If users rely on this information without verification, it can lead to poor decision-making, safety risks, or reputational damage.

### LLM10: Unbounded Consumption

Unbounded consumption refers to the lack of resource limits on LLM interactions. Attackers can exploit this to cause denial-of-service (DoS) or meaningful financial impact by consuming excessive computational resources or API quotas.
