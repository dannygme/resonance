ROLES: list[tuple[str, str]] = [

    # --- Data & Analytics ---
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

    # --- Software Engineering ---
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
    ("Blockchain Developer",
     "Write smart contracts in Solidity, develop on Ethereum or Solana, "
     "DeFi protocols, Web3.js, ethers.js, and decentralised application architecture."),

    # --- AI / LLM ---
    ("AI Engineer",
     "Integrate large language models into products. Prompt engineering, "
     "RAG pipelines, LangChain, vector databases, fine-tuning, and API orchestration."),
    ("NLP Engineer",
     "Build natural language processing systems. Named entity recognition, "
     "text classification, transformers, BERT, semantic search, and text generation."),
    ("Computer Vision Engineer",
     "Develop image and video recognition systems. CNNs, YOLO, OpenCV, "
     "PyTorch, segmentation, object detection, and medical imaging."),

    # --- Product & Design ---
    ("Product Manager",
     "Define product vision, roadmap, and requirements. User research, "
     "stakeholder alignment, OKRs, agile ceremonies, and data-driven prioritisation."),
    ("Product Designer",
     "Design user interfaces and experiences. Figma, user research, "
     "wireframing, prototyping, usability testing, and design systems."),
    ("UX Researcher",
     "Conduct user research to inform product decisions. Interviews, "
     "surveys, usability testing, affinity mapping, and insight synthesis."),
    ("UX Writer",
     "Write interface copy, onboarding flows, error messages, and microcopy. "
     "Collaborate with designers and product managers to shape voice and tone."),
    ("Graphic Designer",
     "Create visual assets for print and digital. Brand identity, typography, "
     "layout, illustration, Adobe Creative Suite, and visual storytelling."),
    ("Visual Designer",
     "Design marketing and product visuals. Motion graphics, brand consistency, "
     "Figma, After Effects, and cross-channel visual communication."),
    ("Brand Designer",
     "Develop and maintain brand identity systems. Logo design, style guides, "
     "color theory, typography, and ensuring visual consistency across touchpoints."),
    ("Illustrator",
     "Create original illustrations for editorial, branding, publishing, and digital media. "
     "Digital and traditional techniques, character design, and concept art."),
    ("Motion Designer",
     "Produce animated graphics and video content. After Effects, Cinema 4D, "
     "storyboarding, kinetic typography, and motion for web and social media."),
    ("Art Director",
     "Lead visual direction for campaigns, shoots, and publications. "
     "Concept development, team direction, client collaboration, and brand alignment."),
    ("Creative Director",
     "Set the creative vision for a brand or agency. Lead design and copy teams, "
     "pitch concepts to clients, and oversee quality across all creative output."),
    ("UI Designer",
     "Design pixel-perfect interfaces for web and mobile. Component libraries, "
     "interaction design, Figma, accessibility standards, and developer handoff."),

    # --- Fashion & Apparel ---
    ("Fashion Designer",
     "Design clothing and accessories from concept to production. Trend research, "
     "sketching, pattern making, fabric selection, and garment construction."),
    ("Textile Designer",
     "Design fabrics, prints, and surface patterns for fashion and interiors. "
     "Color forecasting, repeat patterns, and working with mills and manufacturers."),
    ("Fashion Stylist",
     "Curate looks for editorial shoots, campaigns, celebrities, and retail. "
     "Wardrobe building, trend awareness, and collaboration with photographers and brands."),
    ("Apparel Merchandiser",
     "Plan and manage product assortments for retail. Buying, inventory analysis, "
     "trend forecasting, and working with design and sales teams."),

    # --- Architecture & Interior Design ---
    ("Architect",
     "Design buildings and spaces from concept through construction. AutoCAD, Revit, "
     "building codes, client consultation, and project management."),
    ("Interior Designer",
     "Design functional and aesthetic interior spaces. Space planning, material selection, "
     "client consultation, 3D rendering, and coordination with contractors."),
    ("Landscape Architect",
     "Design outdoor environments including parks, campuses, and urban spaces. "
     "Site analysis, planting design, sustainability, and construction documentation."),
    ("Urban Planner",
     "Plan land use, transportation, and community development. Zoning, policy analysis, "
     "community engagement, GIS mapping, and government collaboration."),

    # --- Film, Media & Production ---
    ("Film Director",
     "Lead the creative vision of film and video productions. Script interpretation, "
     "working with actors, cinematography direction, and post-production oversight."),
    ("Cinematographer",
     "Capture visual storytelling through camera and lighting. Shot composition, "
     "lens selection, lighting design, and collaboration with directors."),
    ("Video Editor",
     "Assemble raw footage into polished video content. Premiere Pro, DaVinci Resolve, "
     "pacing, color grading, sound design, and storytelling through editing."),
    ("Producer",
     "Manage the logistics and finances of film, TV, or digital productions. "
     "Budgeting, scheduling, crew coordination, and stakeholder management."),
    ("Screenwriter",
     "Write scripts for film, television, and digital media. Story structure, "
     "dialogue, character development, and adapting source material."),
    ("Photographer",
     "Capture and edit images for commercial, editorial, or artistic purposes. "
     "Lighting, composition, retouching, and client direction."),

    # --- Music & Audio ---
    ("Music Producer",
     "Oversee the creation and recording of music. Arrangement, mixing, working with artists, "
     "DAWs like Ableton or Logic Pro, and sound design."),
    ("Audio Engineer",
     "Record, mix, and master audio for music, film, and broadcast. "
     "Pro Tools, signal flow, acoustic treatment, and live sound."),
    ("Composer",
     "Write original music for film, TV, games, and concert performance. "
     "Orchestration, notation software, sync licensing, and working to brief."),

    # --- Writing & Journalism ---
    ("Journalist",
     "Research and write news stories for print, digital, or broadcast. "
     "Source development, fact-checking, interviewing, and deadline management."),
    ("Copywriter",
     "Write persuasive content for advertising, marketing, and brand campaigns. "
     "Headlines, taglines, long-form copy, and collaboration with creative teams."),
    ("Content Strategist",
     "Plan and execute content marketing. SEO, editorial calendars, "
     "audience research, copywriting, and content performance analysis."),
    ("Technical Writer",
     "Produce developer documentation, API references, user guides, and release notes. "
     "Markdown, docs-as-code, and developer empathy."),
    ("Editor",
     "Review and refine written content for clarity, accuracy, and style. "
     "Structural editing, copy editing, proofreading, and working with writers."),
    ("Grant Writer",
     "Research funding opportunities and write compelling grant proposals for nonprofits, "
     "research institutions, and arts organisations. Budget narratives and reporting."),

    # --- Education & Training ---
    ("Teacher",
     "Deliver curriculum and support student learning in K-12 or higher education. "
     "Lesson planning, classroom management, assessment, and parent communication."),
    ("Curriculum Designer",
     "Develop educational content and learning pathways. Instructional design, "
     "LMS platforms, learning objectives, and assessment frameworks."),
    ("Corporate Trainer",
     "Deliver professional skills training. Facilitation, needs analysis, "
     "workshop design, and post-training evaluation."),
    ("ESL / EFL Teacher",
     "Teach English as a second or foreign language. Lesson planning, "
     "curriculum design, exam preparation (IELTS, TOEFL, Cambridge), and student assessment."),
    ("Academic Researcher",
     "Conduct peer-reviewed research, write grant proposals, publish in journals, "
     "supervise students, and teach at university level."),
    ("Education Researcher",
     "Study teaching and learning outcomes. Curriculum design, assessment, "
     "qualitative methods, and educational policy implications."),

    # --- Social Sciences & Research ---
    ("Social Scientist",
     "Conduct qualitative and quantitative social research. Survey design, "
     "interviews, statistical analysis, SPSS, R, and academic publishing."),
    ("Policy Analyst",
     "Analyse government or organisational policy. Stakeholder consultation, "
     "evidence synthesis, report writing, and recommendations to decision-makers."),
    ("Sociologist",
     "Study social behaviour, institutions, and inequality. Ethnography, survey research, "
     "critical theory, and publishing findings for academic or public audiences."),
    ("Anthropologist",
     "Research human cultures, societies, and behaviour. Fieldwork, ethnography, "
     "cultural analysis, and applying findings to design, health, or policy contexts."),
    ("Psychologist",
     "Assess and support mental health and behaviour. Clinical, counselling, or research "
     "settings, evidence-based interventions, and case management."),

    # --- Healthcare & Wellness ---
    ("Registered Nurse",
     "Provide patient care in clinical settings. Assessments, medication administration, "
     "care planning, patient education, and interdisciplinary collaboration."),
    ("Public Health Specialist",
     "Design and evaluate community health programmes. Epidemiology, health communication, "
     "policy advocacy, and programme management."),
    ("Nutritionist / Dietitian",
     "Provide evidence-based nutrition guidance for individuals and communities. "
     "Meal planning, clinical assessment, and health coaching."),
    ("Occupational Therapist",
     "Help individuals develop or regain skills for daily living and work. "
     "Assessment, adaptive equipment, and rehabilitation planning."),

    # --- Finance & Fintech ---
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
    ("Accountant",
     "Manage financial records, prepare statements, and ensure compliance. "
     "GAAP, tax preparation, auditing, and financial reporting."),

    # --- Operations & Strategy ---
    ("Operations Manager",
     "Optimise business processes, manage teams, track KPIs, "
     "vendor management, and cross-functional project coordination."),
    ("Strategy Consultant",
     "Solve complex business problems. Structured problem-solving, "
     "market analysis, financial modelling, slide decks, and client management."),
    ("Project Manager",
     "Plan and deliver projects on time and budget. Agile, Scrum, "
     "stakeholder communication, risk management, and resource planning."),
    ("Supply Chain Manager",
     "Oversee procurement, logistics, inventory, and supplier relationships. "
     "ERP systems, demand forecasting, and end-to-end supply chain optimisation."),
    ("Event Manager",
     "Plan and execute corporate, cultural, and social events. Venue sourcing, "
     "vendor management, budgeting, logistics, and on-site coordination."),

    # --- Marketing & Communications ---
    ("Digital Marketing Manager",
     "Run paid and organic digital campaigns. Google Ads, Meta, "
     "email marketing, attribution, and marketing analytics."),
    ("Brand Strategist",
     "Define and evolve brand identity. Market positioning, "
     "consumer insights, campaign development, and brand guidelines."),
    ("Social Media Manager",
     "Manage brand presence across social platforms. Content creation, "
     "community management, analytics, and influencer partnerships."),
    ("Public Relations Manager",
     "Manage media relations, press coverage, and brand reputation. "
     "Press releases, crisis communication, journalist relationships, and events."),
    ("Communications Manager",
     "Manage internal and external communications. Press releases, "
     "stakeholder messaging, crisis communication, and media relations."),

    # --- People & Talent ---
    ("People Operations Manager",
     "Run HR operations, HRIS, compensation benchmarking, "
     "onboarding, and employee lifecycle management."),
    ("Talent Acquisition Specialist",
     "Source and recruit candidates. Sourcing strategies, "
     "ATS management, interviews, and employer branding."),
    ("Learning & Development Manager",
     "Design and deliver employee training programs. "
     "Needs analysis, facilitation, leadership development, and LMS management."),
    ("Diversity & Inclusion Manager",
     "Develop and implement DEI strategies. Data analysis, employee resource groups, "
     "policy development, training, and culture change initiatives."),

    # --- Nonprofit & Social Impact ---
    ("Nonprofit Programme Manager",
     "Design and manage community programmes. Grant reporting, stakeholder engagement, "
     "budget oversight, impact measurement, and team coordination."),
    ("Community Organiser",
     "Build grassroots movements and coalitions. Outreach, advocacy, event coordination, "
     "volunteer management, and campaign strategy."),
    ("Fundraising Manager",
     "Develop and execute fundraising strategies for nonprofits. Major gifts, "
     "events, online campaigns, donor stewardship, and CRM management."),
    ("Social Worker",
     "Support individuals and families facing social, economic, or health challenges. "
     "Case management, advocacy, crisis intervention, and community resources."),

    # --- Hospitality & Culinary ---
    ("Chef / Head Chef",
     "Lead kitchen operations, develop menus, and manage culinary teams. "
     "Food costing, supplier relationships, quality control, and kitchen culture."),
    ("Hotel Manager",
     "Oversee daily operations of a hotel or hospitality property. "
     "Guest experience, staff management, revenue optimisation, and brand standards."),
    ("Food & Beverage Manager",
     "Manage restaurant or catering operations. Menu development, staff scheduling, "
     "cost control, vendor relations, and guest satisfaction."),
    ("Sommelier",
     "Curate wine programmes and advise guests on pairings. Wine knowledge, "
     "cellar management, staff training, and supplier relationships."),

    # --- Legal ---
    ("Lawyer / Attorney",
     "Provide legal advice and representation. Contract drafting, litigation, "
     "legal research, client counselling, and regulatory compliance."),
    ("Paralegal",
     "Support attorneys with legal research, document preparation, case management, "
     "and client communication. Strong attention to detail and legal writing."),
    ("Compliance Officer",
     "Ensure organisational adherence to laws and regulations. Policy development, "
     "risk assessment, audits, and regulatory reporting."),

    # --- Environment & Sustainability ---
    ("Environmental Scientist",
     "Study environmental conditions and develop solutions to pollution and climate issues. "
     "Field sampling, data analysis, regulatory compliance, and reporting."),
    ("Sustainability Manager",
     "Develop and implement sustainability strategies. Carbon accounting, "
     "ESG reporting, supply chain sustainability, and stakeholder engagement."),
    ("Conservation Biologist",
     "Research and protect biodiversity and ecosystems. Fieldwork, species monitoring, "
     "habitat restoration, and conservation policy advocacy."),
]