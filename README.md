# AnalyserBot - Role-Based AI Response Evaluator

This project explores how different AI roles interpret and respond to the same set of machine learning questions. It uses the **Groq API** to simulate responses from multiple professional personas such as **Data Scientist**, **ML Auditor**, and **Tech Reporter**. The system automatically generates prompts, collects responses, and produces comparative summaries for analysis.

---

## Features

- **Role Simulation:** Generates AI responses from different professional perspectives.  
- **Automated Prompting:** Uses structured templates for consistent testing.  
- **Async Execution:** Handles multiple roles efficiently with asyncio.  
- **Data Logging:** Saves responses and summaries as CSV files.  
- **Comparative Evaluation:** Highlights tone and depth variations among roles.

---

## Tech Stack

- **Language:** Python  
- **Model:** `llama-3.3-70b-versatile` (Groq)  
- **Libraries:** `groq`, `python-dotenv`, `pandas`, `asyncio`, `os`

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/role-based-ai-response-evaluator.git
   cd role-based-ai-response-evaluator
   ```

2. **Install dependencies:**
   ```bash
   pip install groq python-dotenv pandas
   ```

3. **Set up environment variables:**  
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

4. **Run the script:**
   ```bash
   python role_based_ai_responses.py
   ```

---

## Output

- **role_based_prompts_results.csv** — Contains detailed responses for each role and query.  
- **role_based_summary.csv** — Summarizes tone and perspective differences across roles.

---

## Use Cases

- Evaluating role-based differences in AI-generated responses  
- Experimenting with prompt engineering and persona control  
- Teaching AI ethics, communication tone, and prompt design  
- Demonstrating Responsible AI evaluation techniques  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
