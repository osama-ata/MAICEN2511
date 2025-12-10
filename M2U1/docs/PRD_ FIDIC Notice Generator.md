# **Product Requirements Document (PRD): FIDIC Notice Generator**

## **Executive Summary**

The **FIDIC Notice Generator** is a web-based utility designed for construction engineers and contract administrators. It solves the business problem of incorrect or delayed contractual notices by automating the drafting process. By standardizing the format, we avoid the "Garbage In, Garbage Out" (GIGO) scenario where poor manual drafting leads to rejected claims.

## **Problem Statement**

Site engineers often struggle to recall the specific sub-clauses required for formal notices (e.g., *Sub-Clause 1.9* vs *8.3*). Drafting these from scratch is prone to human error and tone inconsistencies. This tool ensures that if the input data is correct, the output is legally sound.

## **User Flow (The Logic)**

The application will function based on a linear **Input $\\rightarrow$ Process $\\rightarrow$ Output** model:

1. **Input:** The user selects a specific FIDIC Clause from a dropdown menu and fills in variable fields (Dates, Descriptions, References).  
2. **Process:** The system uses conditional logic to select the correct template and inserts the user's variables into the text string.

3. **Output:** The system generates a formatted letter available for "One-Click Copy" or "Download as PDF."

## **Functional Requirements**

### **A. The Input Interface**

* **Clause Selector:** A dropdown menu containing:  
  * *Sub-Clause 1.9:* Delayed Drawings or Instructions.  
  * *Sub-Clause 4.2:* Performance Security.  
  * *Sub-Clause 8.3:* Programme.  
  * *Sub-Clause 20.1:* Contractor’s Claims.  
* **Variable Fields:**  
  * *Recipient Name/Title* (Text Input)  
  * *Contract Reference Number* (Text Input)  
  * *Event Date* (Date Picker)  
  * *Brief Description of Event* (Text Area)

### **B. The Processing Logic (Algorithm)**

The app must map the "Clause Selector" value to a specific text template.

* *Example Logic:*  
  * **IF** Selection \== "Clause 1.9"  
  * **THEN** Load Template: *"Pursuant to Sub-Clause 1.9 \[Delayed Drawings or Instructions\], we hereby give notice that..."*  
  * **AND** Replace {Date} with User Input.

### **C. The Output**

* A "Preview" pane that updates in real-time as the user types.  
* A "Copy to Clipboard" button.  
* **Constraint:** The text must remain professional and neutral (No slang, purely contractual).

## **UI/UX "Vibe"**

Since the goal is "Vibe Coding"8, the aesthetic should match the target user's environment:

* **Style:** Minimalist, high-contrast, professional.  
* **Color Palette:** "Blueprint Blue" (\#005696), White, and Dark Grey.  
* **Platform:** Web Application (SaaS model style)9.

* **Responsiveness:** Must work on mobile (for engineers on site) and desktop.

## **Success Metrics**

* The user can generate a compliant Sub-Clause 1.9 notice in under 60 seconds.  
* The generated text requires zero editing before sending.
