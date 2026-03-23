ROLES: list[tuple[str, str]] = [
    ("Data Scientist",
     "Build predictive models and machine learning pipelines. Work with Python, "
     "SQL, pandas, scikit-learn, statistical analysis, A/B testing, and data storytelling."),
    ("Data Analyst",
     "Transform raw data into actionable insights using SQL, Excel, Tableau, or Power BI. "
     "Produce dashboards, reports, and support business decision-making."),
    ("Machine Learning Engineer",
     "Design, train, and deploy ML models at scale. MLOps, model serving, feature engineering, "
     "PyTorch, TensorFlow, Kubernetes, and CI/CD pipelines."),
    ("Analytics Engineer",
     "Bridge data engineering and analytics. Build dbt models, maintain data warehouses "
     "like BigQuery or Snowflake, and ensure data quality and documentation."),
    ("Business Intelligence Developer",
     "Develop BI reports and dashboards. Work with Tableau, Power BI, Looker, "
     "data modeling, and stakeholder communication."),
    ("Quantitative Analyst",
     "Apply mathematical and statistical models to financial data. Risk modeling, "
     "derivatives pricing, Python, R, stochastic processes, and financial mathematics."),
    ("Research Scientist",
     "Conduct original research, publish findings, design experiments, "
     "statistical analysis, literature review, academic writing, and peer collaboration."),
    ("Backend Engineer",
     "Build and maintain server-side APIs and services. Python, Node.js, Go, "
     "REST, GraphQL, PostgreSQL, Redis, microservices, and system design."),
    ("Frontend Engineer",
     "Build responsive user interfaces using React, Vue, or Angular. "
     "TypeScript, CSS, accessibility, performance optimisation, and design systems."),
    ("Full-Stack Engineer",
     "Develop both client and server sides of web applications. "
     "React, Node.js, databases, cloud deployment, and API integration."),
    ("Mobile Engineer",
     "Build iOS and Android applications using Swift, Kotlin, or React Native. "
     "UX, offline-first design, push notifications, and App Store deployment."),
    ("DevOps Engineer",
     "Manage CI/CD pipelines, infrastructure-as-code, Kubernetes, Terraform, "
     "AWS/GCP/Azure, monitoring, and site reliability."),
    ("Platform Engineer",
     "Build internal developer platforms, tooling, and infrastructure abstraction layers. "
     "Kubernetes, Helm, Terraform, and developer experience."),
    ("Site Reliability Engineer",
     "Ensure system reliability, uptime, and performance. Incident response, "
     "SLOs, observability, Prometheus, Grafana, and on-call rotations."),
    ("Embedded Systems Engineer",
     "Program microcontrollers and hardware interfaces. C, C++, RTOS, "
     "firmware development, signal processing, and IoT protocols."),
    ("Blockchain Developer",
     "Write smart contracts in Solidity, develop on Ethereum or Solana, "
     "DeFi protocols, Web3.js, ethers.js, and decentralised application architecture."),
    ("Smart Contract Auditor",
     "Review and audit Solidity smart contracts for security vulnerabilities. "
     "Reentrancy, overflow, gas optimisation, formal verification, and DeFi protocol review."),
    ("AI Engineer",
     "Integrate large language models into products. Prompt engineering, "
     "RAG pipelines, LangChain, vector databases, fine-tuning, and API orchestration."),
    ("NLP Engineer",
     "Build natural language processing systems. Named entity recognition, "
     "text classification, transformers, BERT, semantic search, and text generation."),
    ("Computer Vision Engineer",
     "Develop image and video recognition systems. CNNs, YOLO, OpenCV, "
     "PyTorch, segmentation, object detection, and medical imaging."),
    ("MLOps Engineer",
     "Operationalise ML models in production. Model versioning, feature stores, "
     "Kubeflow, MLflow, monitoring, data drift detection, and retraining pipelines."),
    ("Product Manager",
     "Define product vision, roadmap, and requirements. User research, "
     "stakeholder alignment, OKRs, agile ceremonies, and data-driven prioritisation."),
    ("Product Designer",
     "Design user interfaces and experiences. Figma, user research, "
     "wireframing, prototyping, usability testing, and design systems."),
    ("UX Researcher",
     "Conduct user research to inform product decisions. Interviews, "
     "surveys, usability testing, affinity mapping, and insight synthesis."),
    ("Growth Product Manager",
     "Drive user acquisition, activation, and retention. Experimentation, "
     "funnel analysis, lifecycle marketing, and growth modelling."),
    ("Academic Researcher",
     "Conduct peer-reviewed research, write grant proposals, publish in journals, "
     "supervise students, and teach at university level."),
    ("Policy Analyst",
     "Analyse government or organisational policy. Stakeholder consultation, "
     "evidence synthesis, report writing, and recommendations to decision-makers."),
    ("Social Scientist",
     "Conduct qualitative and quantitative social research. Survey design, "
     "interviews, statistical analysis, SPSS, R, and academic publishing."),
    ("Education Researcher",
     "Study teaching and learning outcomes. Curriculum design, assessment, "
     "qualitative methods, and educational policy implications."),
    ("Curriculum Designer",
     "Develop educational content and learning pathways. Instructional design, "
     "LMS platforms, learning objectives, and assessment frameworks."),
    ("Instructional Designer",
     "Create training materials and e-learning content. Articulate Storyline, "
     "adult learning theory, SCORM, and blended learning approaches."),
    ("Investment Analyst",
     "Evaluate investment opportunities, build financial models, "
     "conduct due diligence, and produce equity research reports."),
    ("Financial Analyst",
     "Financial planning, forecasting, variance analysis, Excel modelling, "
     "and management reporting to support business decisions."),
    ("Risk Analyst",
     "Identify and quantify financial or operational risk. Credit risk, "
     "market risk, VaR, stress testing, and regulatory compliance."),
    ("DeFi Analyst",
     "Research decentralised finance protocols, tokenomics, liquidity pools, "
     "yield strategies, on-chain analytics, and smart contract risk assessment."),
    ("Crypto Compliance Officer",
     "Ensure regulatory compliance for digital asset businesses. KYC, AML, "
     "FATF guidance, travel rule, and blockchain transaction monitoring."),
    ("Operations Manager",
     "Optimise business processes, manage teams, track KPIs, "
     "vendor management, and cross-functional project coordination."),
    ("Strategy Consultant",
     "Solve complex business problems. Structured problem-solving, "
     "market analysis, financial modelling, slide decks, and client management."),
    ("Project Manager",
     "Plan and deliver projects on time and budget. Agile, Scrum, "
     "stakeholder communication, risk management, and resource planning."),
    ("Programme Manager",
     "Oversee a portfolio of related projects. Dependencies, governance, "
     "reporting to senior leadership, and strategic alignment."),
    ("Content Strategist",
     "Plan and execute content marketing. SEO, editorial calendars, "
     "audience research, copywriting, and content performance analysis."),
    ("Digital Marketing Manager",
     "Run paid and organic digital campaigns. Google Ads, Meta, "
     "email marketing, attribution, and marketing analytics."),
    ("Brand Strategist",
     "Define and evolve brand identity. Market positioning, "
     "consumer insights, campaign development, and brand guidelines."),
    ("Technical Writer",
     "Produce developer documentation, API references, user guides, "
     "and release notes. Markdown, Docs-as-Code, and developer empathy."),
    ("People Operations Manager",
     "Run HR operations, HRIS, compensation benchmarking, "
     "onboarding, and employee lifecycle management."),
    ("Talent Acquisition Specialist",
     "Source and recruit candidates. Sourcing strategies, "
     "ATS management, interviews, and employer branding."),
    ("Learning & Development Manager",
     "Design and deliver employee training programs. "
     "Needs analysis, facilitation, leadership development, and LMS management."),
    ("Security Engineer",
     "Build and maintain security controls. Penetration testing, "
     "vulnerability management, SIEM, zero-trust, and secure SDLC."),
    ("Web3 Security Researcher",
     "Identify vulnerabilities in blockchain protocols and smart contracts. "
     "Fuzzing, formal verification, bug bounties, and security advisories."),
    ("ESL / EFL Teacher",
     "Teach English as a second or foreign language. Lesson planning, "
     "curriculum design, exam preparation (IELTS, TOEFL, Cambridge), and student assessment."),
    ("Language Programme Coordinator",
     "Manage language training programmes. Scheduling, teacher supervision, "
     "curriculum oversight, student progress tracking, and stakeholder reporting."),
    ("Corporate Trainer",
     "Deliver professional skills training. Facilitation, needs analysis, "
     "workshop design, and post-training evaluation."),
    ("Communications Manager",
     "Manage internal and external communications. Press releases, "
     "stakeholder messaging, crisis communication, and media relations."),
]