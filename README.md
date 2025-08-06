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
- │   ├── main.py            # CLI entry point
- │   ├── s3_client.py       # Handles S3 document retrieval (placeholder)
- │   ├── bedrock_client.py  # Simulated Bedrock client using Hugging Face
- │   ├── validator.py       # Latency and output validation functions
- │   └── config.py          # Constants for bucket and file names
- ├── tests/
- │   ├── test_latency.py    # Pytest for latency validation
- ├── requirements.txt       # Dependencies
- └── README.md              # Project documentation


## Upcoming Features
- Hugging Face QA pipeline integrated to simulate Amazon Bedrock responses
- Real S3 context fetching (next step)
