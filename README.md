# GenAI Q&A Pipeline (In Progress)

This project demonstrates a **GenAI-powered Question & Answer pipeline** built on AWS services, designed to simulate production-ready LLMOps workflows. It showcases **Amazon Bedrock** API workflows (mocked for AWS Free Tier) for LLM inference, **Amazon S3** for context retrieval, and **pre-deployment validation tests** to ensure robust model deployments.

---

## Features
- **GenAI Q&A**: Answers user queries using simulated **Amazon Bedrock** foundation model calls.
- **Context Retrieval**: Fetches domain-specific knowledge from text documents stored in **Amazon S3**.
- **LLMOps Simulation**: Implements pre-deployment validation checks (response latency, response length, and endpoint health).
- **Future Deployment Roadmap**:
  - Deploying pipeline on **Amazon SageMaker endpoints**.
  - Integrating CI/CD workflows for automated deployment.
  - Adding vector database for Retrieval-Augmented Generation (RAG).

---

## Architecture
1. **User Query** → CLI or simple web interface
2. **Document Retrieval** → Context pulled from S3 bucket
3. **Model Inference** → Amazon Bedrock API (mocked for free tier)
4. **Validation Tests** → Pytest-based pre-deployment checks
5. **Future CI/CD & RAG** → Documented for production scale

---

## Tech Stack
- **Language:** Python
- **AWS Services:** Amazon S3, Amazon Bedrock (mocked), SageMaker (planned)
- **Testing & Automation:** Pytest, GitHub Actions (planned for CI/CD)
- **Vector Database (planned):** FAISS or Pinecone

---

## Repository Structure
- genai-qa-pipeline/
- ├── src/  
- │   ├── __init__.py              # Package initializer  
- │   ├── main.py                  # CLI entry point for Q&A pipeline  
- │   ├── s3_client.py             # Handles S3 document retrieval (simulated or real)  
- │   ├── bedrock_client.py        # Simulated Bedrock client using Hugging Face QA pipeline  
- │   ├── validator.py             # Latency and output validation functions  
- │   ├── config.py                # Constants and configuration (e.g., bucket names, flags)  
- │   ├── logger.py                # Logging helper functions  
- │   ├── model_interface.py       # Model inference interface (future Bedrock integration)  
- │
- ├── tests/  
- │   ├── test_placeholder.py              # Initial placeholder test file  
- │   ├── test_latency.py                  # Pytest for latency validation  
- │   ├── test_main_flow.py                # End-to-end pipeline flow test  
- │   ├── test_s3_client.py                # Unit tests for S3 client functions  
- │   ├── test_bedrock_fallback.py         # Tests Bedrock fallback behavior when pipeline fails  
- │   ├── test_bedrock_insufficient_context.py  # Tests handling of insufficient context in QA model
- │   ├── test_cli_json.py                  # Tests JSON outputs  
- │
- ├── requirements.txt            # Dependencies list  
- ├── README.md                   # Project documentation

---  

## JSON Output Mode
Both `run` and `health` commands support `--json` for machine-readable output.

```bash
python -m src.main run --query "What is cloud computing?" --json
python -m src.main health --json

---

## Upcoming Features
- Hugging Face QA pipeline integrated to simulate Amazon Bedrock responses
- Real S3 context fetching (next step)

---
