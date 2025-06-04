# Multi-Agent AI System with Memory and Dashboard

This project is a multi-agent AI system designed to serve as a personal assistant for managing business ecosystems. It features:

- Multiple AI agents with memory capabilities
- Integration with various tools for marketing, website design, ad creation, and more
- A dashboard frontend for monitoring and interacting with agents
- Built using Python for backend agents and React for the frontend dashboard
- Uses MCP framework for agent communication and tool integration

## Setup Instructions

### Backend Setup

1. Install Python 3.8 or higher.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install required Python packages:
   ```bash
   pip install openai mcp-sdk fastapi uvicorn
   ```
4. Run the backend server:
   ```bash
   uvicorn backend.main:app --reload
   ```

### Frontend Setup

1. Install Node.js (version 14 or higher).
2. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Start the frontend development server:
   ```bash
   npm start
   ```

## Project Structure

- `backend/` - Python backend with AI agents and MCP server
- `frontend/` - React dashboard frontend
- `README.md` - This file with setup and usage instructions

## Next Steps

- Implement core AI agents with memory
- Develop dashboard UI components
- Integrate backend and frontend via API
