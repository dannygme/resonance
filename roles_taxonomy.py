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
    ("Biostatistician",
     "Apply statistical methods to biological and clinical research. Clinical trial design, "
     "survival analysis, SAS, R, and regulatory submission support."),

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
    ("QA Engineer",
     "Design and execute test plans for software products. Manual and automated testing, "
     "Selenium, bug tracking, regression testing, and quality assurance processes."),
    ("Embedded Systems Engineer",
     "Program microcontrollers and hardware interfaces. C, C++, RTOS, "
     "firmware development, signal processing, and IoT protocols."),

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
    ("MLOps Engineer",
     "Operationalise ML models in production. Model versioning, feature stores, "
     "Kubeflow, MLflow, monitoring, data drift detection, and retraining pipelines."),

    # --- Cybersecurity ---
    ("Cybersecurity Analyst",
     "Monitor, detect, and respond to security threats. SIEM tools, incident response, "
     "vulnerability management, network security, and security frameworks like NIST."),
    ("Penetration Tester",
     "Conduct authorised attacks on systems to identify vulnerabilities. "
     "Ethical hacking, Metasploit, Burp Suite, red teaming, and security reporting."),
    ("Security Engineer",
     "Build and maintain security controls and infrastructure. Zero-trust architecture, "
     "IAM, secure SDLC, threat modeling, and cloud security."),
    ("Information Security Manager",
     "Oversee an organisation's information security programme. Risk management, "
     "compliance, policy development, team leadership, and incident response planning."),

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
    ("UI Designer",
     "Design pixel-perfect interfaces for web and mobile. Component libraries, "
     "interaction design, Figma, accessibility standards, and developer handoff."),
    ("Growth Product Manager",
     "Drive user acquisition, activation, and retention. Experimentation, "
     "funnel analysis, lifecycle marketing, and growth modelling."),

    # --- Visual & Creative Arts ---
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
    ("Fine Artist",
     "Create original artwork in painting, sculpture, printmaking, or mixed media. "
     "Studio practice, gallery exhibitions, artist statements, and arts funding."),
    ("Concept Artist",
     "Create visual concepts for games, film, and animation. Character design, "
     "environment art, mood boards, and working within creative pipelines."),
    ("Photographer",
     "Capture and edit images for commercial, editorial, or artistic purposes. "
     "Lighting, composition, retouching, client direction, and post-production."),

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
    ("Fashion Buyer",
     "Select and purchase clothing ranges for retail. Trend analysis, supplier negotiation, "
     "OTB management, and working closely with merchandising and design teams."),

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
    ("Interior Decorator",
     "Style residential and commercial spaces with furniture, colour, and accessories. "
     "Client consultation, sourcing, mood boards, and project coordination."),

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
    ("Broadcast Journalist",
     "Report and present news for television, radio, or digital platforms. "
     "Story research, on-camera presenting, interviewing, and deadline management."),
    ("Podcast Producer",
     "Develop, record, and edit podcast content. Guest booking, audio editing, "
     "show structure, distribution, and audience growth strategies."),

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
    ("Music Teacher",
     "Teach instrumental or vocal performance to students of all ages. "
     "Lesson planning, music theory, performance preparation, and curriculum development."),
    ("A&R Manager",
     "Discover and develop musical talent for a record label. Artist scouting, "
     "contract negotiation, creative direction, and project oversight."),

    # --- Gaming ---
    ("Game Designer",
     "Design gameplay mechanics, systems, and player experiences. Level design, "
     "balancing, documentation, prototyping, and collaboration with engineering and art."),
    ("Game Developer",
     "Build game systems and features using Unity or Unreal Engine. C#, C++, "
     "physics systems, multiplayer networking, and performance optimisation."),
    ("Narrative Designer",
     "Craft story, dialogue, and lore for games. World-building, branching narratives, "
     "writing for interactivity, and working with design and art teams."),
    ("Game QA Tester",
     "Test games for bugs, balance issues, and player experience problems. "
     "Test case writing, regression testing, bug reporting, and feature validation."),
    ("3D Artist",
     "Create 3D models, textures, and environments for games, film, or VR. "
     "Maya, Blender, ZBrush, PBR texturing, and optimising assets for real-time engines."),

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
    ("Literary Agent",
     "Represent authors and negotiate publishing deals. Manuscript evaluation, "
     "query letters, contract negotiation, and author career development."),
    ("Book Editor",
     "Develop manuscripts from acquisition through publication. Developmental editing, "
     "copy editing, author relationships, and working with design and marketing teams."),
    ("Translator",
     "Convert written content between languages with accuracy and cultural sensitivity. "
     "Specialisation in legal, medical, literary, or technical translation."),
    ("Interpreter",
     "Provide real-time spoken or signed language interpretation. Conference, legal, "
     "medical, or community settings, and consecutive or simultaneous modes."),
    ("Localization Manager",
     "Oversee the adaptation of products and content for international markets. "
     "Translation management, cultural consulting, workflow tools, and QA processes."),

    # --- Publishing ---
    ("Publishing Manager",
     "Oversee editorial, production, and marketing for a publishing imprint or list. "
     "Acquisitions strategy, author relations, budget management, and market positioning."),
    ("Acquisitions Editor",
     "Identify and sign new books or content for a publisher. Market research, "
     "proposal evaluation, author negotiation, and list building."),

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
    ("School Counselor",
     "Support student wellbeing, academic planning, and social development. "
     "Individual counselling, crisis intervention, college advising, and family liaison."),
    ("Special Education Teacher",
     "Teach students with diverse learning needs. IEP development, differentiated "
     "instruction, assistive technology, and collaboration with families and specialists."),

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
    ("Therapist / Counselor",
     "Provide individual, group, or family therapy. CBT, DBT, trauma-informed care, "
     "case notes, treatment planning, and client progress monitoring."),
    ("Career Coach",
     "Help individuals navigate career transitions and professional development. "
     "Resume coaching, interview preparation, goal setting, and job search strategy."),
    ("Life Coach",
     "Support clients in achieving personal and professional goals. "
     "Goal setting, accountability, mindset work, and motivational interviewing."),

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
    ("Physical Therapist",
     "Evaluate and treat physical impairments through exercise and manual therapy. "
     "Rehabilitation plans, patient education, and outcomes tracking."),
    ("Clinical Research Coordinator",
     "Manage the day-to-day operations of clinical trials. Protocol compliance, "
     "patient recruitment, data collection, IRB submissions, and regulatory reporting."),
    ("Lab Technician",
     "Conduct laboratory tests and experiments in medical, scientific, or industrial settings. "
     "Sample processing, equipment maintenance, data recording, and quality control."),
    ("Physician Assistant",
     "Provide diagnostic and therapeutic services under physician supervision. "
     "Patient assessment, diagnosis, treatment planning, and prescribing."),
    ("Health Informatics Specialist",
     "Manage and analyse healthcare data systems. EHR implementation, data governance, "
     "interoperability standards, and clinical decision support."),

    # --- Beauty & Wellness ---
    ("Esthetician",
     "Provide skincare treatments and beauty services. Facials, waxing, chemical peels, "
     "client consultations, and product recommendations."),
    ("Makeup Artist",
     "Apply makeup for editorial, film, events, and bridal clients. "
     "Colour theory, skin preparation, airbrush technique, and client communication."),
    ("Wellness Coach",
     "Support clients in building healthy habits across nutrition, movement, and mindset. "
     "Goal setting, habit tracking, motivational coaching, and programme design."),
    ("Personal Trainer",
     "Design and deliver personalised fitness programmes. Movement assessment, "
     "strength and conditioning, client motivation, and progress tracking."),

    # --- Sports & Fitness ---
    ("Sports Coach",
     "Develop athlete performance through training, strategy, and mentorship. "
     "Practice planning, performance analysis, team management, and athlete development."),
    ("Athletic Trainer",
     "Prevent, diagnose, and treat athletic injuries. Injury assessment, rehabilitation, "
     "taping and bracing, and working alongside coaching and medical staff."),
    ("Sports Analyst",
     "Analyse player and team performance data to inform coaching decisions. "
     "Video analysis, statistical modelling, scouting reports, and performance metrics."),
    ("Fitness Instructor",
     "Lead group fitness classes and individual training sessions. "
     "Programme design, motivational coaching, safety supervision, and client retention."),
    ("Sports Director",
     "Oversee athletic programmes for clubs, schools, or organisations. "
     "Budget management, staff hiring, facility oversight, and stakeholder relations."),

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
    ("Accountant",
     "Manage financial records, prepare statements, and ensure compliance. "
     "GAAP, tax preparation, auditing, and financial reporting."),
    ("Financial Planner",
     "Help individuals and families plan for financial goals. Retirement planning, "
     "investment advice, tax strategy, insurance, and estate planning."),
    ("DeFi Analyst",
     "Research decentralised finance protocols, tokenomics, liquidity pools, "
     "yield strategies, on-chain analytics, and smart contract risk assessment."),
    ("Actuary",
     "Assess financial risk using mathematics and statistics. Insurance pricing, "
     "pension valuations, regulatory reporting, and probability modelling."),

    # --- Real Estate ---
    ("Real Estate Agent",
     "Assist buyers and sellers in property transactions. Market analysis, "
     "property listings, client negotiation, contract management, and closing."),
    ("Property Manager",
     "Manage residential or commercial properties on behalf of owners. "
     "Tenant relations, maintenance coordination, rent collection, and lease administration."),
    ("Real Estate Appraiser",
     "Determine the market value of properties. Comparative market analysis, "
     "site inspections, appraisal reports, and compliance with valuation standards."),
    ("Real Estate Developer",
     "Identify, finance, and build real estate projects. Site acquisition, "
     "feasibility analysis, contractor management, and investor relations."),

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
    ("Contract Manager",
     "Draft, review, and manage contracts across business relationships. "
     "Risk assessment, negotiation, compliance monitoring, and contract lifecycle management."),

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
    ("Business Analyst",
     "Bridge business needs and technical solutions. Requirements gathering, "
     "process mapping, stakeholder management, and documentation."),
    ("Management Consultant",
     "Advise organisations on strategy, operations, and transformation. "
     "Frameworks, client workshops, slide decks, benchmarking, and implementation support."),

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
    ("SEO Specialist",
     "Improve organic search visibility. Keyword research, on-page optimisation, "
     "link building, technical SEO, and performance tracking."),
    ("Email Marketing Manager",
     "Design and execute email marketing programmes. Segmentation, automation, "
     "A/B testing, deliverability, and lifecycle campaigns."),
    ("Influencer Marketing Manager",
     "Develop and manage influencer partnerships. Creator sourcing, campaign briefs, "
     "contract negotiation, performance tracking, and community building."),

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
    ("HR Business Partner",
     "Align HR strategy with business objectives. Workforce planning, "
     "performance management, employee relations, and organisational development."),
    ("Compensation & Benefits Manager",
     "Design and manage total rewards programmes. Salary benchmarking, "
     "benefits administration, equity planning, and regulatory compliance."),

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
    ("International Development Specialist",
     "Design and implement development programmes in low and middle income countries. "
     "Needs assessment, project management, donor reporting, and community engagement."),

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
    ("Travel Consultant",
     "Plan and book travel experiences for individuals and groups. Itinerary design, "
     "supplier relations, visa advice, and customer service."),
    ("Tourism Manager",
     "Develop and promote tourism products and destinations. Partnership management, "
     "visitor experience, marketing, and stakeholder engagement."),

    # --- Engineering ---
    ("Civil Engineer",
     "Design and oversee construction of infrastructure. Structural analysis, "
     "AutoCAD, project management, site supervision, and regulatory compliance."),
    ("Mechanical Engineer",
     "Design and develop mechanical systems and products. CAD modelling, "
     "thermodynamics, materials science, prototyping, and manufacturing processes."),
    ("Electrical Engineer",
     "Design electrical systems for buildings, products, or infrastructure. "
     "Circuit design, power systems, control systems, and safety standards."),
    ("Structural Engineer",
     "Analyse and design structures to withstand loads and forces. "
     "Calculations, Revit, construction drawings, and site inspections."),
    ("Chemical Engineer",
     "Design processes for manufacturing chemicals, fuels, and materials. "
     "Process simulation, thermodynamics, safety analysis, and plant operations."),
    ("Biomedical Engineer",
     "Develop medical devices, equipment, and software. FDA regulations, "
     "prototyping, clinical testing, and cross-functional collaboration with clinicians."),

    # --- Aviation & Logistics ---
    ("Pilot",
     "Operate commercial, cargo, or private aircraft. Flight planning, "
     "crew resource management, navigation, safety protocols, and regulatory compliance."),
    ("Logistics Coordinator",
     "Coordinate the movement of goods across supply chains. Freight booking, "
     "customs documentation, carrier management, and shipment tracking."),
    ("Supply Chain Analyst",
     "Analyse supply chain data to improve efficiency and reduce costs. "
     "Demand forecasting, inventory modelling, ERP systems, and supplier performance."),
    ("Air Traffic Controller",
     "Direct aircraft movements to ensure safe and efficient air traffic flow. "
     "Radar systems, communication protocols, emergency procedures, and shift work."),

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
    ("Environmental Consultant",
     "Advise organisations on environmental compliance and impact reduction. "
     "EIA reports, regulatory guidance, site assessments, and sustainability planning."),
    ("Renewable Energy Engineer",
     "Design and develop solar, wind, or other renewable energy systems. "
     "Energy modelling, grid integration, project development, and technical sales."),

    # --- Agriculture & Food Science ---
    ("Agricultural Scientist",
     "Research and develop methods to improve crop yield, soil health, and farming practices. "
     "Field trials, data analysis, and working with farming communities and policy bodies."),
    ("Food Technologist",
     "Develop and improve food products for safety, taste, and shelf life. "
     "Product development, sensory analysis, regulatory compliance, and manufacturing."),
    ("Farm Manager",
     "Oversee day-to-day operations of a farm. Crop planning, equipment management, "
     "staff supervision, financial management, and compliance with agricultural regulations."),
    ("Agronomist",
     "Advise farmers on crop production and soil management. Field scouting, "
     "soil testing, fertiliser recommendations, and sustainable farming practices."),

    # --- Library & Information Science ---
    ("Librarian",
     "Manage library collections, assist patrons with research, and deliver information "
     "literacy programmes. Cataloguing, database management, and community outreach."),
    ("Archivist",
     "Preserve and provide access to historical records and documents. "
     "Appraisal, arrangement, description, digitisation, and reference services."),
    ("Information Manager",
     "Oversee the organisation and governance of information assets. "
     "Knowledge management, records management, taxonomy design, and compliance."),
    ("Research Librarian",
     "Support academic or corporate research through expert information services. "
     "Literature searches, citation management, database training, and subject expertise."),

    # --- Sales ---
    ("Sales Development Representative",
     "Generate and qualify pipeline through outbound prospecting. Cold outreach, "
     "objection handling, CRM hygiene, and handoff to account executives."),
    ("Account Executive",
     "Close new business and manage deals through a full sales cycle. "
     "Discovery, demos, negotiation, forecasting, and CRM management."),
    ("Sales Manager",
     "Lead and develop a sales team to hit revenue targets. Pipeline coaching, "
     "quota setting, performance management, and cross-functional alignment."),
    ("Business Development Manager",
     "Identify and develop new revenue opportunities through partnerships and outreach. "
     "Market research, deal structuring, relationship building, and pipeline management."),
    ("Account Manager",
     "Manage and grow existing client relationships. Upselling, contract renewals, "
     "stakeholder management, QBRs, and customer satisfaction."),
    ("Revenue Operations Manager",
     "Align sales, marketing, and customer success around shared revenue goals. "
     "CRM administration, funnel analytics, forecasting, and process optimisation."),
    ("Sales Engineer",
     "Provide technical expertise during the sales process. Product demos, "
     "solution design, RFP responses, and bridging sales and engineering teams."),

    # --- Customer Success & Support ---
    ("Customer Success Manager",
     "Manage post-sale relationships to drive retention and expansion. Onboarding, "
     "QBRs, health scoring, churn prevention, and cross-functional advocacy."),
    ("Customer Support Specialist",
     "Resolve customer issues across chat, email, and phone. Ticketing systems, "
     "product knowledge, escalation handling, and CSAT improvement."),
    ("Technical Support Engineer",
     "Troubleshoot technical issues for customers and provide product expertise. "
     "Debugging, documentation, ticket management, and engineering escalation."),
    ("Customer Experience Manager",
     "Design and improve end-to-end customer journeys. NPS, CSAT, journey mapping, "
     "feedback loops, and cross-functional process improvement."),
    ("Community Manager",
     "Build and manage online communities around a brand or product. "
     "Forum moderation, engagement programmes, user feedback, and community growth."),

    # --- E-commerce & Retail ---
    ("E-commerce Manager",
     "Manage online retail operations. Product listings, conversion optimisation, "
     "platform management (Shopify, Amazon), and performance analytics."),
    ("Retail Manager",
     "Oversee store operations, staff, and sales performance. Inventory management, "
     "visual merchandising, customer service standards, and P&L ownership."),
    ("Category Manager",
     "Manage product categories to maximise sales and margin. Supplier negotiation, "
     "range planning, pricing strategy, and performance analysis."),
    ("Merchandising Manager",
     "Plan and execute product placement and promotional strategy. Planograms, "
     "inventory allocation, seasonal planning, and cross-functional collaboration."),

    # --- Administration & Executive Support ---
    ("Executive Assistant",
     "Support senior executives with scheduling, communications, and operations. "
     "Calendar management, travel coordination, meeting preparation, and stakeholder liaison."),
    ("Office Manager",
     "Oversee day-to-day office operations. Facilities management, vendor coordination, "
     "onboarding support, expense management, and team administration."),
    ("Operations Coordinator",
     "Support operational workflows and cross-functional processes. Scheduling, "
     "documentation, data entry, reporting, and administrative coordination."),
    ("Administrative Assistant",
     "Provide clerical and administrative support. Correspondence, filing, "
     "scheduling, data management, and general office duties."),
    ("Programme Coordinator",
     "Coordinate logistics and administration for organisational programmes. "
     "Scheduling, reporting, stakeholder communication, and documentation management."),
]