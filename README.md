# 🔋 Battery RAG System with Memory

A sophisticated Retrieval-Augmented Generation (RAG) system for battery engineering calculations and analysis, featuring conversation memory and semantic search capabilities.

## 🌟 Features

- **📊 Data Processing**: Loads and processes battery specifications from CSV files
- **🧠 Vector Embeddings**: Uses SentenceTransformers for semantic search
- **💾 Vector Database**: ChromaDB for efficient similarity search
- **🗣️ Conversation Memory**: Maintains context across multiple interactions
- **⚡ Real-time Calculations**: Performs battery pack calculations (series/parallel configurations)
- **🔍 Smart Retrieval**: Finds relevant battery data based on query semantics
- **📈 Comparative Analysis**: Compares batteries across multiple parameters

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas sentence-transformers chromadb langchain langchain-community
```

### Basic Usage
1. Open `rag_system.ipynb` in Jupyter
2. Run all 16 small cells in sequence to initialize the system
3. Use `rag_chain.invoke("your query")` or `battery_chat()` for interaction

## 📁 Project Structure

```
battery_rag_system/
├── rag_system.ipynb           # Streamlined RAG with LangChain (16 small cells)
├── battery_data_10000_rows.csv # Battery specifications dataset (10K records)
└── README.md                  # Complete documentation
```

## 🔧 System Architecture

### 1. Modular Cell Structure (16 Small Cells)
- Separate imports, data loading, embeddings, vector store setup
- Individual functions for retrieval, parsing, calculations
- LangChain components and chain construction

### 2. Data Ingestion & Processing
- Loads battery specifications from CSV
- Converts to structured document format
- Handles data validation and cleaning

### 3. Vectorization & Storage
- Creates semantic embeddings using `all-MiniLM-L6-v2` model
- Stores in ChromaDB with batch processing (handles 10K+ records)
- Optimizes for fast similarity search

### 4. LangChain RAG Pipeline
- **RunnableParallel**: Combines context retrieval and query processing
- **RunnableLambda**: Custom response generation logic
- **PromptTemplate**: Structured battery engineering prompts
- **Memory Integration**: Conversation tracking with LangChain memory

### 5. Memory System
- **Conversation Buffer**: Maintains chat history using LangChain memory
- **Query History**: Tracks all user interactions with timestamps
- **Context Integration**: Uses previous conversations to enhance responses

### 6. Retrieval & Generation
- Embeds user queries for semantic matching
- Retrieves top-k most relevant battery records
- Generates contextual responses with calculation capabilities

## 🔗 LangChain Integration

### Chain Structure
```python
rag_chain = (
    RunnableParallel({
        "context": lambda x: memory.get_context(),
        "query": RunnablePassthrough(),
        "battery_data": lambda x: format_docs(retrieve_documents(x))
    })
    | RunnableLambda(lambda x: generate_response(x["query"], retrieve_documents(x["query"])))
)
```

### Usage Examples
```python
# Direct chain usage
result = rag_chain.invoke("Calculate 2S3P configuration")

# Interactive chat
battery_chat()  # Starts interactive session
```

## 💬 Prompt Engineering

### Main Prompt Template
```
You are a battery engineering expert assistant with access to a comprehensive battery database.

{conversation_context}

Current Query: {query}

Relevant Battery Data:
{retrieved_battery_data}

Instructions:
- Answer based on the provided battery data and previous conversation context
- For calculations, show step-by-step work
- If data is insufficient, clearly state limitations
- Consider previous interactions to provide contextual responses
- For configurations like 2S3P: 2S = 2 cells in series, 3P = 3 cells in parallel

Response:
```

### Key Prompt Features
- **Context Awareness**: Includes previous conversation history
- **Domain Expertise**: Assumes battery engineering knowledge
- **Calculation Focus**: Emphasizes step-by-step mathematical work
- **Configuration Understanding**: Handles series/parallel notation (2S3P format)
- **Data Grounding**: Requires responses based on retrieved data

## 🧮 Calculation Capabilities

### Supported Configurations
- **Series (S)**: Voltages add, capacity remains same
- **Parallel (P)**: Capacities add, voltage remains same
- **Combined (2S3P)**: 2 in series, 3 in parallel

### Example Calculations
```
2S3P Configuration:
- Pack Voltage = Cell Voltage × 2 (series)
- Pack Capacity = Cell Capacity × 3 (parallel)
- Pack Energy = Pack Voltage × Pack Capacity
- Total Cells = 2 × 3 = 6 cells
```

## 🎯 Query Examples

### Battery Pack Calculations
```
"Calculate total energy for 4P configuration with high-density lithium batteries"
"What's the voltage and capacity of a 2S3P pack using NMC cells?"
```

### Comparative Analysis
```
"Compare the top 3 batteries by energy density"
"Which battery type is better for electric vehicles - NMC or LiFePO4?"
```

### Memory-Based Queries
```
"What was the voltage of the battery we discussed earlier?"
"Based on our previous conversation, which configuration do you recommend?"
```

## 🧠 Memory System Details

### Components
1. **ConversationBufferMemory**: LangChain's built-in memory for chat history
2. **Custom Query History**: Tracks interactions with metadata
3. **Context Builder**: Integrates recent conversations into prompts

### Memory Features
- Stores last 3 interactions in context
- Includes timestamps for all queries
- Maintains calculation history
- Enables follow-up questions

## 📊 Data Format

### Expected CSV Structure
```csv
Battery_ID,Type,Voltage,Capacity,Energy_Density,Weight,Chemistry,Anode,Separator
BAT-001,Cylindrical,3.7,2.5,250,45,NMC,Graphite,PE
```

### Document Format (Internal)
```
Battery ID: BAT-001
Type: Cylindrical
Voltage: 3.7 V
Capacity: 2.5 Ah
Energy Density: 250 Wh/kg
```

## 🚀 Advanced Usage

### Custom Query Function
```python
result = battery_rag_query("Your query here", top_k=5)
print(result['response'])
print(f"Retrieved {len(result['retrieved_docs'])} documents")
```

### Interactive Chat
```python
chat_with_battery_expert()  # Starts interactive session
```

### Memory Inspection
```python
print(f"Total interactions: {len(memory.query_history)}")
print(memory.get_context())  # Shows recent conversation context
```

## 🔄 Comparison with YouTube Chatbot

### Similarities
- **Memory Integration**: Both use LangChain memory components
- **RAG Architecture**: Similar retrieval-augmentation pattern
- **Interactive Chat**: Both support conversational interfaces
- **Document Processing**: Handle unstructured data conversion

### Key Differences
- **Domain Specific**: Battery engineering vs. video content
- **Calculation Focus**: Mathematical computations vs. content summarization
- **Structured Data**: CSV processing vs. transcript parsing
- **Technical Precision**: Engineering calculations vs. general Q&A

## 🛠️ Configuration Options

### Embedding Model
- Default: `all-MiniLM-L6-v2`
- Alternative: `all-MiniLM-L12-v2` (better quality, slower)

### Vector Database
- ChromaDB with in-memory storage
- Batch size: 1000 documents (adjustable)

### Memory Settings
- Buffer size: Last 3 interactions
- History: All interactions with timestamps

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues
1. **ChromaDB Batch Size Error**: Reduce batch_size in the code
2. **Memory Overflow**: Clear memory with `memory.query_history.clear()`
3. **Embedding Errors**: Ensure sentence-transformers is properly installed

### Performance Tips
- Use smaller embedding models for faster processing
- Adjust top_k parameter based on your needs
- Clear memory periodically for long sessions

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review the example notebooks