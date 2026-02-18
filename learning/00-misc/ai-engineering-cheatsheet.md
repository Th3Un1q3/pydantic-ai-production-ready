# AI Engineering Master Cheat Sheet

## Building, Evaluating, and Scaling Production-Ready Generative AI

### 1. Strategy: The "ROI Gap" & Usefulness

- **The ROI Gap:** 95% of agentic demos fail in production because they lack "Observation in Operation" strategies.
- **Usefulness Thresholds:** Prioritize *"Is it good enough to be useful?"* over *"Is it perfect?"*
- **The Debate Partner Pattern:** Leverage AI to present diverse options/views rather than a single "ground truth," reducing the risk of a single point of failure.
- **Risk Tolerance:** Enterprises favor **Internal Apps** (Knowledge Mgmt) over External Chatbots to mitigate reputational risk.

### 2. The AI Engineering Stack

- **Philosophy:** Prioritize **Model Adaptation** (Prompting, RAG) over Model Training.
- **Application Layer:** UX/UI, Context Construction, Evaluation Pipelines.
- **Model Layer:** Inference Optimization, Fine-tuning (LoRA), Dataset Engineering.
- **Infrastructure Layer:** Orchestration, Vector Stores, Serving, Monitoring.

### 3. Evolutionary Architecture (The 6 Phases)

*Start simple. Add complexity only when the Usefulness Threshold demands it.*

1. **Phase 1: Request/Response** → Direct App-to-Model API call.
2. **Phase 2: Context Enhancement** → RAG (Vector/Doc DBs) + Read-only Search.
3. **Phase 3: Guardrails** → Input (PII, Injection) & Output (Format, Safety) filters.
4. **Phase 4: Routers & Gateways** → Intent-based routing; unified API fallback.
5. **Phase 5: System Caching** → Exact matching or Semantic caching to slash latency.
6. **Phase 6: Agentic Write Actions** → State changes (DB updates, Email) + Human-in-the-loop.

### 4. Prompt Engineering & Context Design

*Adaptation without weight changes via In-Context Learning (ICL).*

- **Anatomy:** `[Task Description] + [Persona] + [Few-Shot Examples] + [Current Input]`
- **Tactics:**
  - **Chain-of-Thought (CoT):** "Think step-by-step" to reduce hallucinations.
  - **Task Decomposition:** Break complex queries into sub-tasks (Sequential or Parallel).
- **Context Efficiency:**
  - **Lost-in-the-Middle:** Critical instructions must be at the **Start** or **End**.
  - **Instructions vs. System Prompts:** In agents, prefer per-request "Instructions" to reduce context bloat.

### 5. RAG Pipeline Engineering

*Moving beyond naive vector search to production-grade grounding.*

- **Ingestion:**
  - **Chunking:** Semantic boundaries (Markdown/Code) > Fixed token counts.
  - **Overlap:** 10–20% to preserve context at boundaries.
- **Advanced Retrieval:**
  - **Hybrid Search:** **Dense** (Vector) + **Sparse** (BM25) via **RRF (Reciprocal Rank Fusion)**.
  - **Query Rewriting:** Convert ambiguous user turns into standalone search queries.
  - **Contextual Retrieval:** Augment chunks with "situating" context (titles/summaries) *before* indexing.
  - **Parent Document:** Retrieve small chunks for matching, but feed the parent doc to the LLM.

### 6. Agentic Logic & Tooling

- **The Loop:** **Plan** (Generate steps) → **Execute** (Call Tools) → **Reflect** (Check outputs) → **Iterate**.
- **Tool Juggling:** Expose only relevant tool subsets (Dynamic listing) to prevent confusion/hallucination.
- **Plan-then-Execute:** Separate the "Reasoning" phase (Plan) from the "Action" phase to prevent Goal Hijacking.
- **Graceful Handling:** Distinguish between **Technical Failures** (Retriable) and **Behavioral Failures** (Requires logic change).

### 7. Pydantic AI Implementation Primitives

*Building context-aware systems with code-first reliability.*

- **RunContext & Deps:** Type-safe injection of live data (DB connections, API keys) into tools and prompts.
- **Dynamic Instructions:** Using `@agent.instructions` to build system prompts that update based on runtime state (User ID, Time).
- **Structured Output Validation:** Ensuring model-generated content conforms to validated Pydantic models (moving errors from Runtime to "Write-time").
- **Instrumentation:** `logfire.instrument_pydantic_ai()` for instant tracing.

### 8. Evaluation Strategies (The Framework)

*The bottleneck of AI Engineering. Define "Good" before you build.*

- **Evaluation Hierarchy (Fail-Fast):**
    1. **Deterministic:** Instant checks (JSON Schema, Regex, PII).
    2. **Span-Based (Behavioral):** Verify *how* a result was reached (Trace analysis).
    3. **LLM-as-a-Judge:** Subjective quality (Tone, Helpfulness) on 1% sample.
- **The RAG Triad:**
  - **Faithfulness:** Supported *only* by context?
  - **Answer Relevance:** Addresses query?
  - **Context Precision:** Relevant chunks ranked top?

### 9. Metrics & Business Alignment

*Bridging technical performance to business value.*

- **Business Metrics:** % Automation, Labor Reduction, User Retention.
- **Model Metrics:** **Pass@k** (Code), **IFEval** (Instructions), **Factual Consistency**.
- **Operational Metrics:**
  - **Goodput:** Requests meeting **SLOs** (e.g., Latency < 2s).
  - **TTFT (Time-to-First-Token):** Prefill/UX responsiveness.
  - **TPOT (Time-Per-Output-Token):** Decoding/Reading speed.
- **Cost Efficiency:** Batch APIs (50% cheaper) for offline tasks (Reporting, Migration).

### 10. Observability & Operational Health

*Turn the "Black Box" into a "Glass Box".*

- **Observability vs. Monitoring:**
  - **Monitoring:** Tracks knowns (Error rates, Latency).
  - **Observability:** Explains *why* (Traces, Spans, Tool Inputs).
- **DORA for AI:** **MTTD** (Detection), **MTTR** (Response), **CFR** (Change Failure Rate).
- **Drift Detection:** Monitor **User Edit Rate** and **Refusal Rate** as proxies for model decay.

### 11. Security: The OWASP Top 10 (2026)

- **ASI01 Goal Hijacking:** Indirect injection alters the objective.
- **ASI02 Tool Misuse:** Legitimate tools used destructively.
- **ASI06 Memory Poisoning:** Malicious data persists in Long-Term Memory.
- **Mitigation:**
  - **Sandboxing:** Run code/tools in isolated environments.
  - **Least Agency:** Grant minimum required permissions.
  - **Human-in-the-Loop:** For high-stakes "Write" actions.

### 12. User-Centric Design & Feedback

- **Implicit Feedback:** Track "Early Termination" (Stop generation) or "Regeneration" (Retry) as negative signals.
- **Manual Fallbacks:** If the Agent fails, expose manual UI controls so the user can finish the task.
- **In-Place Comparison:** Allow users to "Regenerate with Model B" to gather preference data.
- **Latency Masking:** Use streaming (low TTFT) to maintain perceived performance during long reasoning steps.
