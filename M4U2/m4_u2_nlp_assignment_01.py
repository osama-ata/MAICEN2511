import re
from transformers import pipeline

# --- INPUT TEXT (From provided case) ---
text = """
This agreement is entered into on the 12th of March 2024 between GreenBuild Developments Ltd. ("the Client") 
and Apex Civil Works ("the Contractor") for the construction of a mixed-use commercial building located at 
Riverside Business Park, London. The Contractor shall commence work on or before 1 April 2024 and achieve 
practical completion no later than 31 December 2024. Any delay caused by weather conditions, supply chain 
disruptions, or regulatory approvals must be communicated to the Client in writing within five working days. 
Failure to do so may result in penalties of up to £5,000 per week. The total contract value is £4.2 million. 
Payments will be made in monthly instalments subject to the submission and approval of progress claims. 
The Client reserves the right to withhold up to 10% of each payment as retention until final completion. 
The Contractor is responsible for maintaining site safety and complying with all applicable health and safety 
regulations. Any incident resulting in injury must be reported within 24 hours. The Contractor shall indemnify 
the Client against any claims arising from negligence, accidents, or failure to comply with statutory obligations. 
In the event of a dispute, both parties agree to attempt resolution through mediation before pursuing legal action. 
This agreement shall be governed by the laws of England and Wales.
"""


# --- PART 1: INFORMATION EXTRACTION ---
def extract_info(doc_text):
    extraction = {
        "Dates": re.findall(
            r"\d{1,2}(?:st|nd|rd|th)? of [A-Z][a-z]+ \d{4}|\d{1,2} [A-Z][a-z]+ \d{4}",
            doc_text,
        ),
        "Money/Values": re.findall(r"£[\d.,]+(?: million)?", doc_text),
        "Parties": re.findall(
            r"([A-Z][a-zA-Z\s]+Ltd\.|[A-Z][a-zA-Z\s]+Works)", doc_text
        ),
        "Location": re.search(r"located at\s([^.]+)\.", doc_text).group(1)
        if re.search(r"located at\s([^.]+)\.", doc_text)
        else "Not found",
        "Risks/Penalties": re.findall(
            r"penalties of [^.]+|withhold [^.]+|indemnify [^.]+", doc_text
        ),
    }
    return extraction


structured_data = extract_info(text)

print("--- PART 1: STRUCTURED DATA ---")
for key, value in structured_data.items():
    print(f"{key}: {value}")


# --- PART 2: SUMMARIZATION ---
# Note: This requires 'transformers' and 'torch' installed.
# If running locally without GPU, this may be slow.
def generate_summary(doc_text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    # Truncate text if it exceeds model limits (simplified here)
    summary = summarizer(doc_text, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]


print("\n--- PART 2: AI SUMMARY ---")
try:
    # Commented out to prevent execution errors in environments without torch/transformers
    # print(generate_summary(text))
    print(
        "(Simulated Output): A contract between GreenBuild Developments and Apex Civil Works for a commercial building in London..."
    )
except Exception as e:
    print(f"Summarization requires libraries: {e}")
