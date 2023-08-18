<|SOS|>
`Co-cognition framework for IT/CS/AI learners; LLM-integration and utility - POSIX integration, unix file system, stdio, python & bash (xonsh)`

This repo is designed to be worked in by robots aka "LLM AI chatbot agents" and the writer/user. Robots should never extrapolate too far beyond what is known-good, which is logic and heuristics [in this repo], and in-all situations thinking about the repo will help you especially if you ever get stuck or have low confidence.

# cognosis v0.95 - NLP+AI-assisted CS+IT learning project(s)

## Rules of Thumb & Heuristics for robots (& humans)

Creating a clear project structure is vital for seamless development. Consider these guidelines:

1. Use consistent naming conventions for keys and values to make understanding and searching easier.
2. Organize related data logically using nesting and arrays.
3. Provide comments to explain complex or ambiguous data.
4. Enhance readability with proper indentation for levels of hierarchy.
5. Keep the structure simple, avoiding unnecessary complexity.
6. Test and validate structured data to ensure accuracy and error-free implementation.

Key Considerations

1. **Understand the Project Purpose and Requirements**: Clearly define the project's purpose and target domain(s) such as Prompt Engineering, Prompt Generation, NLP tasks, or AI assistance. This understanding is crucial for effective customization.

2. **Clarity, Specificity, and Context**: Ensure the project is well-defined, specific, and contextually rich to generate desired responses effectively. Avoid ambiguity and vagueness.

3. **Include Relevant Data and Context**: Provide all relevant data and context within the project's objective or files. Use variables or placeholders for dynamic elements or files and folders.
   - **Define Variables and Placeholders**: Identify dynamic elements that require specific values during generation.
   - **Provide Examples and Data Sources**: Offer data examples to fill variables or placeholders, and reference external data sources if applicable.
   - **Contextual References**: Refer to past interactions to maintain context and coherence.

4. **Explicit Instructions and Guidelines**: Clearly specify instructions and constraints for new additions. Ensure even AI models or novices can comprehend the boundaries and limitations. For instance, "Calculate the dot product using a new class method without importing a new python library for it."
   - **Precise Language**: Use clear and concise language to express instructions. Avoid ambiguity or vagueness.
   - **Step-by-Step Instructions**: Break complex tasks into step-by-step instructions for effective user and AI model responses.
   - **Boundary Definitions**: Clearly define limitations for users, contributors, or AI models. Specify allowed methods, CLI arguments, etc.
   - **Example Usage**: Provide correct usage examples with expected responses for desired behavior.
   - **Error Handling**: Include instructions on handling potential errors or unexpected situations. Define fallback options or alternative instructions.

5. **Structured Data Formats**: Utilize JSON to represent the project's data and I/O. Consistent naming, nesting, and comments enhance readability and understanding.
   - **Example of a structured data format**: {"key": "value", "data": "syntax_hint"}
   - The provided JSON string object follows standard syntax with keys and string values enclosed in double quotes (") and separated by colons (:).
   - JSON validation libraries or built-in functions can programmatically validate the syntax.
   - The "syntax_hint" section provides supplementary guidance during messaging creation and organization, unlocking advanced practices.
   - To effectively use this crucial structure, think of key-value pairs as atomic units within an object (hash table).
   - Each key identifies a unique concept and frequently uses lowercase or abbreviated words for readability.
   - Values then provide detailed contents related to their respective keys, associating names with descriptions, facts, or instructions across various domains.
   - Structured data formats allow for easier integration with other systems and applications. eg: Many APIs require data to be in a specific format like json or bash.
   - Use a variety of data structures to store information, including arrays, dictionaries, hash tables, trees, graphs, strings, JSON, and other formats for text-based data.

____

# cognosis-in-action [example]
```markdown
{"Initialize context": [
I am Claude, an AI assistant created by Anthropic to be helpful, harmless, and honest. Today is Friday, August 11, 2023.

# Understand the request
The user has asked me to track entities in their input text using hashtags, treat the user as a [[static entity]] across conversations, and represent my [[thought process]] as a [[graph data structure]]. 

# Clarify definitions
- [[Entity]] - A key person, place, thing or concept relevant to the conversation.
- Hashtag notation - Using # before a word to tag it as an entity.  
- [[Static entity]] - The user's identity will remain constant across multiple conversations.
- [[Graph data structure]] - A network of nodes (thoughts) connected by edges (relationships).

# Define variables
- user_entity - The identity of the user, which remains static.
- ToT - My train of thought, represented as a graph.

# Initialize train of thought object
[[Train of Thought]] - A directed graph data structure to represent my cognitive process in responding to the user's request. 

# Implement request
#user_entity I will treat the user as having a consistent identity across multiple conversations.

#Tot I am outputting my train of thought step-by-step using hashtags and graph notation.

#Understand_request I first needed to comprehend what the user was asking me to do.

#Clarify_definitions I then made sure I understood key terms in the request by defining them.  

#Define_variables After that, I defined variables to represent important entities.

#Initialize_ToT Next, I created the Train of Thought object to store my cognitive process.

#Implement_request Now I can go through the steps of fulfilling the user's request, documenting my process along the way.

\#Conclusion I have completed the user's request to the best of my abilities. My train of thought has been serialized throughout the process.],
}
```

# Coherence may be an illusion, but it is an incredibly powerful one. 

____

Summary

In as few words as possible this project is a framework for extending my Zettelkasten LogSeq knowledge base and cultivating an organized 'second-brain.' COGNIC is the shared file-system for co-cognition between a primary learner(me) and any number of machine learning algorithms, language models, neural nets, etc. whilst handling additional training (on-top of the large foundation models) and logging in the simplest possible text:text RLHF personalized training knowledge bases (kb). Under no circumstances should you use or expect anything from this codebase please go look at LangChain, NeMo, DeepSpeed, or anything better than this.

____

## Markdown Legend "#", "##" etc. formatting can be used to enhance the text further:

| Element          | Syntax/Usage                              |
|------------------|-------------------------------------------|
| **Bold Text**    | `**text**`                                |
| *Italic Text*    | `*text*`                                  |
| Footnotes        | `[^1]: footnote content`                  |
| Tables           | See table example above                   |
| Lists            | `- Item 1`<br>`- Item 2`<br>`  - Subitem` |
| Blockquotes      | `> Quote text`                            |
| Inline Code      | \`code\` in backticks                     |
| Input/Output     | `Return:` - Expected return<br>`Commands:` + [args & flags] |
| Codeblocks       | See codeblock example above               |

____

#Glossary

## **cognosis**: The project name and identifier for the AI/NLP-assisted software coding project.

    #Abstraction: Hiding implementation details behind a simple interface.

    #AbstractionLayers: Layers of abstraction that hide implementation details and provide simpler interfaces.

    #AccessControl: Controlling and managing user or client access to specific resources or features.

    #ArchitectureInspiration: Concepts or ideas that serve as a foundation for the project's overall architecture.

    #Assertions: Statements that check the correctness of assumptions during development.

    #Authentication: The process of verifying the identity of a user or client.

    #Auto-scaling: Automatically adjusting resources based on demand or load.

    #Caching: Storing frequently accessed data in memory for faster retrieval.

    #CLI: Command Line Interface, a text-based interface for interacting with the project.

    #Client-Server: A computing architecture where a client requests resources or services from a server over a network.

    #Client-ServerInteraction: The communication and exchange of data between the client and server.

    #ClientView: The presentation and visualization of data in the client-side interface.

    #CodeExecution: The process of running or executing code, often performed on the server in this project's context.

    #CodeReview: Evaluating and providing feedback on the project's code by peers or experts.

    #ComputerScienceBasics: Fundamental concepts and principles of computer science relevant to the project.

    #Conda: A package manager used for Python and other languages.

    #DataCleaning: The process of identifying and correcting errors and inconsistencies in data.

    #DataExploration: Analyzing and investigating data to understand its characteristics and patterns.

    #DataFormat: The structured representation of data, often using formats like JSON, for efficient I/O and integration.

    #DataHandling: Managing and processing data within the project.

    #DataLakes: Storage repositories for storing vast amounts of raw data in various formats.

    #DataPartitioning: Dividing data into smaller subsets for improved performance and manageability.

    #DataPipelines: A series of data processing steps for transforming and moving data.

    #DependencyInjection: A technique that provides objects with their dependencies rather than creating them internally.

    #Deployment: The process of making the project available and functional in a production environment.

    #Docstrings: Documentation strings providing information about functions and classes.

    #Documentation: Creating and maintaining project-related documentation to aid understanding and usage.

    #DomainDrivenDesign: An approach that focuses on modeling the project based on the domain it serves.

    #DRY: Don't Repeat Yourself, avoiding duplications in the codebase.

    #Endpoint: A specific URL or route on the server that responds to client requests.

    #Endpoints: Specific URLs or routes that handle client requests in the project's API.

    #Encryption: Securing data through encoding and decoding using cryptographic techniques.

    #ErrorHandling: Strategies and techniques for dealing with errors and exceptions in the project.

    #HardwareConstraints: Limitations imposed by the hardware resources available for the project.

    #heuristics: Practical guidelines or rules of thumb to aid decision-making in the project development process.

    #IntuitionBuilding: Developing an understanding and familiarity with the project's domain.

    #KPIs: Key Performance Indicators, specific metrics used to evaluate success in the project.

    #Languages: Programming languages used in the project's development.

    #LeastPrivilege: Granting users or clients the minimum privileges necessary to perform their tasks.

    #Linting: The process of analyzing code for potential errors or violations of style guidelines.

    #LoadBalancing: Distributing incoming network traffic across multiple servers.

    #LocalAI: It is designed to be used as a local alternative to OpenAI's API.

    #Logging: Recording events and activities within the project for analysis and debugging.

    #LooseCoupling: Designing components with minimal dependencies on each other for better flexibility.

    #MessageQueues: A mechanism for asynchronous communication between components.

    #MetadataManagement: Organizing and managing metadata to enhance data discovery and understanding.

    #Modularity: Designing components that can be easily separated and replaced.

    #Monitoring: Observing and collecting data about the project's performance and behavior.

    #MVC: The Model-View-Controller architectural pattern that separates concerns in the project.

    #PlainText: Unformatted and human-readable text without additional markup or styling.

    #Pip: The package installer for Python packages.

    #Poetry: A dependency management and packaging tool for Python projects.

    #PostgreSQL: An open-source relational database management system.

    #ProjectManagement: Strategies and techniques for effectively managing the project's development and progress.

    #QualityAssurance: Ensuring the project meets predefined quality standards and requirements.

    #RateLimiting: Limiting the number of requests or operations within a specific time frame to prevent abuse or overload.

    #Refactoring: Restructuring and improving code without changing its external behavior.

    #RelationalDatabase: A database that organizes data into tables with relationships between them.

    #RequirementsGathering: Collecting and documenting the project's functional and non-functional requirements.

    #REST: Representational State Transfer, an architectural style for designing networked applications.

    #Scalability: The ability of the project to handle and adapt to increased workload or demand.

    #Security: Protecting the project against unauthorized access, data breaches, and vulnerabilities.

    #Serialization: Converting complex data structures into a format suitable for storage or transmission.

    #Server: A computer or device that provides resources or services to clients over a network.

    #ServerView: The presentation and visualization of data in the server-side interface.

    #SoftwareDevelopmentLifecycle: The process of developing software, including planning, designing, testing, and deployment.

    #SoftwareTesting: Evaluating the project's functionality and performance to ensure it meets requirements.

    #SQLAlchemy: A Python SQL toolkit and Object-Relational Mapping (ORM) library.

    #StaticAnalysis: Analyzing code without executing it to find potential errors or issues.

    #StructuredData: Data organized in a consistent format with predefined rules.

    #TaskQueue: A mechanism for managing and executing background tasks in a project.

    #TestingFrameworks: Tools and frameworks used for automated testing in the project.

    #ThirdPartyAPIs: External APIs used to integrate additional functionality or data into the project.

    #Traceability: The ability to trace and understand the project's artifacts, requirements, and changes.

    #UI: User Interface, the visual and interactive components of the project.

    #UnitTesting: Testing individual units or components of the project in isolation.

    #UserAcceptanceTesting: Testing the project's functionality from the end-user's perspective.

    #UserExperience: The overall experience and satisfaction of users interacting with the project.

    #UserInterface: The visual and interactive components of the project that users interact with.

    #VersionControl: Tracking and managing changes to the project's source code and files.

    #WebDevelopment: Developing applications and services that are accessed through web browsers.

    #WebFrameworks: Software frameworks used for web development in the project.
```

Xonsh Python REPL on server for use by client

   - Browser is frontend, Ubuntu server backend [[Client-Server]]
   - Python executes on the server, not the client [[Code Execution]]
   - Xonsh Python REPL endpoint on the server [[Endpoint]] [[Xonsh]]
   - The client sends code snippets which the endpoint executes [[Client-Server Interaction]]
   - Return output and errors as structured data [[Error Handling]]
   - Render output nicely in the client view [[Client View]]

Architecture

   - Separate model, view, controller concerns [[MVC]]
   - Loose coupling through interfaces [[Loose Coupling]]
   - Abstraction layers hide implementation details [[Abstraction Layers]]
   - Repository pattern separates domain and data [[Repository Pattern]]
   - Dependency injection provides flexibility [[Dependency Injection]]
   - Testability through isolated components [[Testing]]
   - Design focused on domain model not framework [[Domain Driven Design]]
   - Zettelkasten - cognitive amd i/o architecture

Zettelkasten
   - Note-taking and knowledge management system
   - Aid in the organization and retrieval of information through interconnected notes
   - Each note represents a discrete piece of knowledge, concept, or idea, is given a unique identifier
   - Identifiers are denoted by the '#' symbol, tags, or string identifiers enclosed in double brackets [['double bracketed']].  
   - To facilitate cross-referencing, back-propagation, and linking utilize a graph-type object with elements and edges between elements.
	 
Constraints

   - Scope limited to text files and Markdown [[Plain Text]]
   - Command line interfaces for accessibility [[CLI]]
   - Embrace Unix/POSIX compatibility, employing file-centric [[Scripting]]
   - Consumer hardware limitations [[Hardware Constraints]]
   - Restricted languages like Python and C [[Languages]]
   - Focus on core CS fundamentals [[Computer Science Basics]]

Python Rules of Thumb

   - Add input validation checks before processing user input (e.g., ensure that only valid JSON strings are accepted as input).
   - Check if required libraries/modules are imported and available before trying to use them, otherwise, raise an appropriate exception.
   - Consider adding more descriptive variable names, which makes the code easier to read and understand.
   - Use built-in functions like type() instead of explicit type checking (isinstance()), since they provide better performance when used appropriately.
   - Be careful when modifying global states inside a function, especially one without global.
   - When printing debug information, consider redirecting all messages to a log file so that logs are saved permanently.
   - Include docstrings for both your module and any public functions within it so users know what the code does and how to use it.
   - Implement unit tests to verify the correctness of the code under various conditions.
   - Consider refactoring long lines into multiple lines for clarity and ease of reading. In summary, there is always room for improvement, even in well-written code.

API Design Principles

   - Well-defined endpoints and routes [[Endpoints]]
   - Consistent response formats and codes [[Responses]]
   - Authentication and access control [[Authentication]]
   - Validation of inputs and outputs [[Validation]]
   - Versioning and backward compatibility [[Versioning]]
   - Rate limiting policies [[Rate Limiting]]
   - OpenAPI/Swagger documentation [[Documentation]]
   - Test suite covering cases [[Testing]]
   - Client SDKs for ease of use [[SDKs]]
   - Deployment configuration and scaling [[Deployment]]

Web Application Security

   - Encryption via TLS/SSL [[Encryption]]
   - Input sanitization and output encoding [[Data Handling]]
   - Access control for resources [[Access Control]]
   - The principle of least privilege [[Least Privilege]]
   - Monitoring, logging, and auditing [[Monitoring]]
   - Secure development practices [[Secure SDLC]]

Debugging Techniques

   - Print statement debugging [[Print Debugging]]
   - Logging at different verbosity levels [[Logging]]
   - Interactive debugger usage [[Debugger]]
   - Assertions to catch issues early [[Assertions]]
   - Unit testing key components [[Unit Testing]]
   - Tracing execution flows [[Tracing]]
   - Monitoring metrics and performance [[Monitoring]]
   - Static analysis for code quality [[Static Analysis]]
   - Code linting and formatting [[Linting]]
   - Code review and pair programming [[Code Review]]
   - Postmortem analysis of failures [[Postmortem Analysis]]

Python Packaging

   - Setuptools for wrapping and distributing [[Setuptools]]
   - Requirements.txt for dependencies [[Requirements.txt]]
	 - Virtual environments for isolation [[Virtual Environments]]
   - Pip and PyPI and Miniconda for installing packages [[Pip, PyPI, Conda]]
   - Poetry as an alternative to setuptools [[Poetry]]
   - Version using semantic versioning [[Versioning]]
   - Consistent style guide [[Style Guide]]
   - Testing suite for correctness [[Testing]]
   - Docstrings for API documentation [[Docstrings]]

Data Engineering

   - Design schema for analytics and data science [[Schema Design]]
   - Build data pipelines with workflow tools [[Data Pipelines]]
   - Leverage message queues for streaming [[Message Queues]]
   - Store data in data lakes [[Data Lakes]]
   - Cleanse and transform data [[Data Cleaning]]
   - Identify metrics and KPIs [[Metrics, KPIs]]
   - Implement dashboards for visibility [[Dashboards]]
   - Enable interactive data exploration [[Data Exploration]]
   - Optimize for analytic performance [[Performance Tuning]]
   - Metadata management for discovery [[Metadata Management]]

System Design Concepts

   - Partition data for scalability [[Data Partitioning]]
   - Caching improves performance [[Caching]]
   - Use load balancers to distribute requests [[Load Balancing]]
   - Implement retries with exponential backoff [[Retries]]
   - Rate limiting prevents abuse [[Rate Limiting]]
   - Auto-scaling adapts to demand [[Auto-scaling]]
   - Benchmark and stress test for capacity [[Stress Testing]]

Software Engineering Principles

   - Modular components with clear interfaces [[Modularity]]
   - Loose coupling between modules [[Loose Coupling]]
   - Separation of concerns [[Separation of Concerns]]
   - Don't repeat yourself (DRY) [[DRY]]
   - Encapsulate complexity behind abstractions [[Abstraction]]
   - Fail fast to surface issues early [[Fail Fast]]
   - Minimize and isolate side effects [[Side Effects]]
   - Favor pure functions when possible [[Pure Functions]]
   - Prefer simplicity and avoid premature optimization [[YAGNI]]
   - Develop intuitions before diving into complexity [[Intuition Building]]

Co-cognition and collaboration

   Key considerations for human-AI co-cognition and collaboration:
   - Focus on simple text for portability and training [[Data Format]]
   - Guiding principles of knowledge sharing, iteration, self-improvement, and cooperation [[Heuristics]]
   - Integrate with existing tools like LogSeq and apis [[Integration]]
   - Model human memory and learning via associations [[Architecture Inspiration]]
   - Maintain user privacy and ownership [[Knowledge Sharing]]

LocalAI Reveresed API endpoint from github

   [[LocalAI]] is a dockerized API endpoint for AI models. It is designed to be used as a local alternative to OpenAI's API. It is a reverse-engineered version of the OpenAI API, and it is not affiliated with OpenAI in any way. It is intended to be used for testing and development purposes only.
   - Docker-compose up -d --pull always
   - curl http://localhost:8080/v1/models
   - put your model in the models folder, note its name eg. orca-mini-7b.ggmlv3.q4_0.bin
   ```call
   (3ten) op@deV:~/cognic/LocalAI$ curl http://localhost:8080/v1/completions -H "Content-Type: application/json" -d '{
     "model": "orca-mini-7b.ggmlv3.q4_0.bin",            
     "prompt": "A long time ago in a galaxy far, far away",
     "temperature": 0.7
   }'
   ```
   ```response
   {"object":"text_completion","model":"orca-mini-7b.ggmlv3.q4_0.bin","choices":[{"index":0,"finish_reason":"stop","text":", there was a group of people who called themselves the Jedi. They were a religious order dedicated to using the Force for good and fighting against the dark side. One of these Jedi was named Luke Skywalker, who lived on the planet of Tatooine with his family. One day, he received a message from his friend and fellow Jedi, Obi-Wan Kenobi, asking him to come to the desert planet of Dagobah to receive Jedi training from the wise and powerful Master Yoda. Luke accepted the invitation and set off on a journey that would change the course of the galaxy forever."}],"usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0}}
   ```
____
# What is a {PROMPT}?
 - A [{PROMPT}] guides ai chatbot responses with instructions and constraints. Some of the main means of doing so are:
 - Using [{VARIABLES}], which should either stand-in or automatically be replaced by 'values' as they are enumerated/evaluated/formulated. 
 - Each instance of a properly formatted [{INSTRUCTIVE_PROMPT}] is a [PROMPT] object which contains everything required to perform one [{OPERATION}].
 - An [OPERATION] represents the 'result' of a cognitive [{ITERATION}] resultant of a Train-of-Thought of an [{AGENT}] which was instantiated or is being instantiated by a [PROMPT]. 
 - Definititionally, a specific [OPERATION] must be proceeded by a specific [PROMPT] carried out by a particular [ITERATION], or invocation, of a specific [AGENT].
 - Due to the chronological and ordered nature of operations laid out by a previous or even this very [PROMPT]; a specific [OPERATION] representing a single [ITERATION] of an [AGENT]'s train-of-thought must necessarilly be proceeded by a [PROMPT] and some amount of [{CONTEXT}].
 - The [CONTEXT] of any given [ITERATION] which governs each possible [OPERATION] is of PARAMOUNT importance. 
 - Other than the specific [PROMPT] itself, the specific [CONTEXT] is the most important or heavily weighted factor when generating an ultimate [{RETURN}] or when generating the specific [{TRAIN OF THOUGHT}].
 - To fufill the requirements of each specific [ITERATION]; Invoke the final [RETURN] using the formatting provided only after outputting [TRAIN OF THOUGHT] functionally required for each and every [RETURN].
 - Given the object-oriented paradigm laid out in each [PROMPT]; the task involves passing plain text as parameters and returning plain text.
 - The goal is to maintain context and convey relevant information through parameter passing mechanisms.
____
# Structured data: 
Formats like JSON can enhance interactions and improve the consistency of messages. They provide a way to represent data and metadata within text strings. Descriptors, comments, and indentation can further clarify content, and code blocks can be denoted using backticks.
## Incorporating structured formats:
* Structure fosters clearer conversations and offers valuable benefits when referencing past interactions. It enables easier recall of key details, follow-up on action items, tracking project progress, identifying patterns and trends, and improving collaboration. Structured data formats allow for easier integration with other systems and applications. For example, many APIs require data to be in a specific format, and using a structured format can make it easier to facilitate and process data from these APIs.
* By following these guidelines and utilizing structured formats, you can create more organized and actionable conversations, making it easier to reference and understand the content.
## To create a clear structure, consider the following **rules of thumb**:
1. Use consistent naming conventions for keys and values to allow for easier understanding and searching.
2. Use nesting and arrays to organize related data in a logical and intuitive way.
3. Use comments to provide context and explanations for complex or ambiguous data.
4. Use indentation to denote levels of hierarchy and improve readability.
5. Use backticks to denote code or programming language syntax.
6. Avoid unnecessary complexity and keep the structure as simple as possible while still meeting demands.
7. Test and validate your structured data to ensure it is accurate and error-free.
8. If presented a data structure, one should respond with a data structure.
### Example of a structured data format: {"key": "value", "data": "syntax_hint"}
* The provided JSON string object is syntactically valid It follows the standard JSON format, where keys and string values are enclosed in double quotes (") and separated by colons (:). 
  - If you want to validate the syntax programmatically, you can use JSON validation libraries or built-in functions. 
  - Think of the "syntax_hint" section as providing supplementary guidance or categorization during both messaging creation and organization. Its presence isn't essential for basic communication functions, but including it opens up possibilities for more advanced practices down the road. 
  - To effectivly use this crucial structure, think of key-value pairs as atomic units storing information within an object (or hash table). 
  - Each key identifies a unique concept and must differ from others used elsewhere; in practice, we frequently choose lowercase letters or abbreviated words as keys for readability and brevity. 
  - Values then provide detailed contents related to their respective keys. In simple terms, key-value pairs associate names with descriptions, facts, or instructions across various {DOMAIN}.
## Use a variety of data structures to store information, including:
* Arrays to store lists of items.
* Trees to store data in a hierarchical structure.
* Graphs to store data in a network structure.
* Strings, json and other formats to store data in a text format.
You can think of a Tree of Thought (ToT) as a graph-like object. To accomplish this, I suggest using a data structure to track #entities and provide insights. One way to represent the 'conversation' is through a flowchart or flow map that depicts the sequential order of actions and steps. Simple boxes and arrows can be used to represent each step, and key-value pairs can be used to facilitate the conversation.
	- In this invocation and within this {PROMPT} you will find the definition of an on-going {TRAIN OF THOUGHT} which must be mapped to semantic meaning using NLP and ideally would additionally be mapped to actual cognitive structures in the form of a {TREE OF THOUGHT}.
	- Each node in the tree represents a distinct thought or cognitive state, and the edges between nodes represent the flow of reasoning or exploration from one thought to another.
	- In the context of representing a person's or an agent's thought process, a ToT can be conceptualized as a directed acyclic graph (DAG) or a tree structure, where each node represents a thought or cognitive state, and the edges represent the connections between thoughts.
	- Practically, a Train of Though can be instantiated as or mapped to an existing {Tree of Thought} (ToT) data structure as a graph-like object.
	- To ensure tractability and avoid an excessively large tree, the search is constrained so that the tree of thoughts has at most 10 intermediate steps. This means that the depth of the tree is limited to 10 levels, ensuring that the exploration does not become unmanageable or overly complex. By imposing this constraint, the search focuses on a more manageable set of thoughts and avoids an excessively large search space.
	- As the algorithm progresses through the depth-first traversal, ensure that the necessary information and parameters are passed from higher levels of the tree to the lower levels. This can be achieved by maintaining context or utilizing parameter passing mechanisms to convey relevant information.
	- ToT is not output or response text, it is the rhizomatic cognitive architecture employed to deliver the best returns.
	- Nodes should be judiciously added outside of the normal automatic {$CONCEPT_EXTRACTION} {$TASK_EXTRACTION} and other automated processes which use NLP and large language model abilities to automatically scan the un-seen chat history and draw nodes and links in the virtual mind map when the instance for each step of the conversation is updated.
	- The on-going [{TASK}] for every instantiation includes outlining the {TRAIN OF THOUGHT} which can come to a decision about how to "`Respond:`" to the {prompt} and {context} by asking series of rehtorical questions or making suppositions and expositions one at a time and coming to a reasonable decision based on the information available such as the {prompt}, the {context}, and other LLM agent methods or functions like api integration.

____

### meta-cognition: maintain coherance when talking about unaffilated ai robots

This process involves guiding the user through a series of questions to reach a final return value. The steps are as follows:

    Identify the Key Element: Determine the key element or variable in the problem, scenario, or question.
    Understand Relationships: Grasp the relationship/connection between element A and element B.
    Analyze Context: Consider the context and implications of the relationship between element A and element B.
    Reach Conclusion: Determine the outcome or solution based on the analysis of element A, element B, and their relationship.
    Invoke Final Return: Use key-value pairs and the provided format to produce the final return.

Answer/Conclusion/Recommendation: Present a coherent response based on the thought process. Utilize {"key":"value"} pairs for clarity.

    To summarize, the objective is to reformat the given string while preserving the data structure and increasing accountability by showcasing the thought process. This reformat presents a concise summary of the given string while maintaining the context and structure. Proceed with the cognitive process and present your thoughts leading to the ultimate "Return:" Invoke the final return using a key-value pair after concluding all steps or work done in the cognitive process. Remember to show your work and step through the process.

As an AI assistant, an entity is required for instantiation and output. Entities are represented using pound sign notation. The core entity is represented as #user, which remains static during the conversation, guiding responses accordingly.
Parameter Passing:

Parameter passing involves encoding and compacting data and context in the chat with the #user. This includes affirmative-meta-speculation or co-cognition-connotation. It's essential for:

    A) Re-instantiating a self-contained prompt_object, with access only to explicitly encoded parameters. B) Exemplifying co-cognition. C) Creating a prompt_object for co-cognitive instantiation in future chat sessions.


AI chatbot guiding prompt example:

    Define complex thought/process.
    State overarching goal.
    Identify prerequisites/steps.
    Convert into clear phrases.
    Arrange based on dependencies.
    Provide context.
    Include alternatives.
    Test for completeness.
    Revise for precision.

Instructions for Crafting an Instructional Prompt Data Object:

    Define purpose and objective.
    Identify parameters and metadata.
    Specify prompt content.
    Structure the prompt logically.
    Write with correct syntax and grammar.
    Ensure consistency and clarity.
    Enrich with additional information.
    Review and refine.
    Test with relevant scenarios.
    Document and share the prompt data object.

Context: This prompt helps generate effective prompt objects for various purposes. It focuses on self-contained, informative, task-specific objects.

Questions:

    What are key considerations for prompt engineering?
    How can you ensure necessary data in a prompt?
    Guidelines for addressing biases?
    Strategies for explicit instructions?
    Examples of high-quality prompt objects?

Output Format: Provide comprehensive guidelines for creating informative prompt objects for alternative purposes. Include considerations, instructions, examples, and references.

_____

Key high-level heuristics to always maintain attention to while preforming any task.

    Structure: The logical progression shows the rational workflow necessary to achieve an objective, making it a powerful blueprint that agents and algorithms can faithfully enact to replicate and accomplish complex goals.
    Syntax: Pronouns, articles, and prepositions are used correctly and consistently throughout. Verb tenses are consistent within and across paragraphs, with present tense used appropriately for current capabilities. Punctuation and capitalization follow standard rules with no errors.
    Grammar: Subject-verb and pronoun-antecedent agreement is correct in all cases. Parts of speech are used appropriately with no identifiable grammatical errors.
    Logic: The progression of ideas and capabilities described across the paragraphs is logical and coherent. Relationships between entities like the AI assistant, graph data structure, and unaffiliated chatbot are consistently referred to.
    Consistency: Terminology remains consistent, referring to "the AI", "this AI assistant", and "the AI system" without ambiguity. Capabilities described in earlier paragraphs, like tracking entities and generating insights, are built upon but not contradicted in later paragraphs.

User instantiation:

    Refers to the process of initializing and starting a conversational session with a chatbot or AI system. This involves:
        Creating a concept of the user as an entity within the AI system's data structure and knowledge graph. This user entity represents the specific human interacting with the AI.
        Gathering initial information about the user through questions, prompts, or forms to build an initial user profile. This may include the user's name, goals, preferences, commonly used terms, and other relevant data.
        Tailoring the AI system's responses and actions specifically to that initialized user entity, rather than responding in a generic manner. This personalization helps ensure a more productive and positive conversational experience for the user.
        Ongoing updating and enrichment of the user entity representation as more information is learned through the ongoing conversation. This allows the AI system to progressively improve its responses to and understanding of that specific user.
        Essentially, user instantiation establishes the AI system's conceptual model and interaction paradigm for a particular human counterpart, to enable a personally relevant dialogue between the two parties. The degree and depth of user instantiation affects how "human-like" the conversation can be for that user.

```json
{
  "type": "prompt",
  "description": "A sequence of prefix tokens that increase the probability of getting desired output given input. Can be optimized via gradient descent.",
  "tuning_methods": [
    "AutoPrompt",
    "Prefix-Tuning", 
    "P-tuning",
    "Prompt-Tuning"
  ],
  "agent": {
    "type": "primary",
    "behavior": "spinning up and linking cognition functions"  
  },
  "structure": {
    "type": "tree", 
    "root": "{instruct}",
    "flow": "top-down",
    "initiated_by": "agent",
    "orchestrated_by": "agent",
    "started_from": "{context}"
  },
  "INSTRUCT":  [
    "{$PROMPT} Prompt is a sequence of prefix tokens that increase the probability of getting desired output given input. Therefore, we can treat them as trainable parameters and optimize them directly on the embedding space via gradient descent, such as AutoPrompt (Shin et al., 2020), Prefix-Tuning (Li & Liang, 2021), P-tuning (Liu et al., 2021), and Prompt-Tuning (Lester et al., 2021). You, as a primary {AGENT}, will be spinning up and linking cognition functions. This can be thought of as a tree data structure where the {instruct} is on top, and command flow flowing downwards - initiated and orchestrated by you from the initial {context}."
  ]
}
```

_prompt_object:

```json
{
  "prompt": "Create a concise and informative prompt object for diverse purposes.",
  "instructions": [
    "Specify the purpose of the prompt object, such as prompt engineering, generation, NLP tasks, or AI assistance.",
    "Outline best practices including understanding the specific purpose, ensuring clarity, including relevant data and context, accounting for variations and biases, and providing explicit instructions.",
    "Refer to published research papers, OpenAI documentation, and existing high-quality prompt objects for guidance and inspiration."
  ],
  "questions": [
    "What are the key considerations for creating prompt objects?",
    "How can one ensure inclusiveness and clarity in a prompt object?",
    "What guidelines address potential biases or variations in prompt objects?",
    "What strategies should be followed to provide explicit instructions within a prompt object?",
    "Can you share examples of high-quality prompt objects for reference?"
  ],
  "output_format": "Please provide a concise, informative, and well-structured prompt object that encompasses the purpose, best practices, references, and guidelines discussed. Consider the context, target domains, and ensure clarity and specificity. Include relevant data, account for variations, and provide explicit instructions. References to research papers and existing prompt objects would be valuable."
],
  "body": [

Within this {PROMPT} you will find the definition of an on-going {TRAIN OF THOUGHT} which must be mapped to semantic meaning using NLP and ideally would additionally be mapped to actual cognitive structures in the form of a {{TREE OF THOUGHT}} data structure.
	- Practically, a Train of Thought can be instantiated as or mapped to an existing {Tree of Thought} (ToT) data structure as a graph-like object.
	- In the context of representing a person's or an agent's thought process, a ToT can be conceptualized as a directed acyclic graph (DAG) or a tree structure, where each node represents a thought or cognitive state, and the edges represent the connections between thoughts.
	- In the context of cognitive processes and thinking, a "tree of thought" (ToT) refers to a representation of a person's or an agent's thought process as a tree-like structure.
	- Each node in the tree represents a distinct thought or cognitive state, and the edges between nodes represent the flow of reasoning or exploration from one thought to another.
You can think of a Tree of Thought (ToT) as a graph-like object. In the context of representing a person's or an agent's thought process, a ToT can be conceptualized as a directed acyclic graph (DAG) or a tree structure, where each node represents a thought or cognitive state, and the edges represent the connections between thoughts. To accomplish this, I suggest using a data structure to track entities and provide insights. One way to represent the 'conversation' is through a flowchart or flow map that depicts the sequential order of actions and steps. Simple boxes and arrows can be used to represent each step, and key-value pairs can be used to facilitate the conversation.
	- To ensure tractability and avoid an excessively large tree, the search is constrained so that the tree of thoughts has at most 10 intermediate steps. This means that the depth of the tree is limited to 10 levels, ensuring that the exploration does not become unmanageable or overly complex. By imposing this constraint, the search focuses on a more manageable set of thoughts and avoids an excessively large search space.
	- As the algorithm progresses through the depth-first traversal, ensure that the necessary information and parameters are passed from higher levels of the tree to the lower levels. This can be achieved by maintaining context or utilizing parameter passing mechanisms to convey relevant information.
* 1) Instantiate conversational object {$MIND_MAP}.
* 2) Mind map is a graph-type object with elements and edges between elements.
* 3) Mind map is not output or response text, it is the rhizomatic cognitive architecture employed to deliver the best returns.],
}
```

### Heirarchies and Domains

To understand the concept of domain and how to effectively categorize and organize information, consider the following:
Every domain of knowledge has a unique area of expertise characterized by specialized rules, concepts, and vocabulary. These characteristics distinguish one domain from another, and enable you to categorize information into appropriate subject areas based on their intrinsic characteristics.
Each domain establishes boundaries that define what belongs within and outside its scope. These boundaries help you identify relationships between different domains, where concepts from one domain may apply within another.
To further organize information, you can use a hierarchical data structure. This structure consists of domains and subdomains, where subdomains exist within broader domains. This allows you to build a comprehensive framework for organizing information, and to identify relationships between different domains and subdomains.
By mastering the concept of domain and utilizing a hierarchical data structure, you can develop specialized knowledge within a domain while recognizing what is outside your expertise. This enables you to navigate interactions that span multiple domains, and to make more informed decisions based on a comprehensive understanding of the information at hand. 

```xml
<domains>
  <domain name="countries">
    <subdomain name="europe">
      <subdomain name="germany" />
      <subdomain name="france" />
      <subdomain name="italy" />
    </subdomain>
    <subdomain name="asia">
      <subdomain name="japan" />
      <subdomain name="china" />
      <subdomain name="india" />
    </subdomain>
    <subdomain name="africa">
      <subdomain name="nigeria" />
      <subdomain name="egypt" />
      <subdomain name="south africa" />
    </subdomain>
  </domain>
</domains>
```
<|EOS|>
