# SL_Projects

These projects was developed as part of the Advanced Executive Program in Applied Generative AI. It demonstrates the application of Generative AI and Large Language Models (LLMs) to solve real-world business problems using modern AI frameworks and cloud-native technologies.

• Project: CEP_1_Crafting_an_AI_Powered_HR_Assistant 
	> This project focuses on developing a conversational AI chatbot to improve the operational efficiency of Nestlé’s Human Resources (HR) department.
	>  The chatbot is designed to answer employee queries related to Nestlé’s HR policies by extracting relevant information from official HR documents and presenting accurate, context-aware responses through a user-friendly interface. 
	>  The chatbot follows a RAG architecture: 
			1) HR policy documents are loaded from PDF format.
			2) Text is split into smaller overlapping chunks.
			3) Each chunk is converted into embeddings using OpenAI embeddings.
			4) FAISS stores and retrieves vectors based on semantic similarity.
			5) Relevant document chunks are passed to GPT-3.5 Turbo as context.
			6) The model generates accurate, policy-based responses.
			7) Gradio provides the conversational interface for users.
		
• Project: NEWSGENIE (AN AI-POWERED INFORMATION AND NEWS ASSISTANT)
	> Developed NewsGenie, an AI-powered assistant that provides both real-time news updates and general information through a single conversational interface.
	> Integrated OpenAI GPT for intelligent responses and Tavily API for live news retrieval.
	> Implemented LangGraph-based query routing to intelligently direct user requests to the appropriate processing workflow.
	> Built an interactive Streamlit UI with robust error handling, fallback mechanisms, and secure API integration for a reliable user experience.

• Project: Banking Customer Support AI Agent using Multi-Agent Architecture
	> Developed a Banking Customer Support AI Agent using a multi-agent architecture to automate customer support interactions and service requests.
	> Implemented LLM-powered intent classification to understand customer queries and route them to the appropriate support agent.
	> Enabled automated ticket creation, tracking, and database integration for efficient issue management.
	> Built a Streamlit-based interface with LLMOps logging and evaluation capabilities to monitor performance and improve response quality.

• Python Project : Adventure Game 
	> Developed a text-based Adventure Game in Python where players navigate different paths and make decisions to find a hidden treasure. 
	> Implemented modular functions, conditional logic, and user input handling to create interactive gameplay and multiple outcomes. 
	> Designed branching storylines with win/lose scenarios based on player choices, enhancing engagement and replay ability. 
	> Built a game loop with restart functionality, demonstrating core Python programming concepts such as functions, loops, and control flow.

• Python Project : analyse_cust_order
	> Developed a Customer Orders Analysis System in Python to process and analyze customer purchase data using lists, tuples, dictionaries, and sets.
	> Implemented customer segmentation by calculating spending patterns and classifying customers as high-value, moderate, or low-value buyers.
	> Generated business insights including category-wise revenue, top-spending customers, unique products, and cross-category purchasing behavior.
	> Utilized Python data structures, loops, comprehensions, and set operations to perform efficient data analysis and reporting.




