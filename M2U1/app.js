// FIDIC Notice Generator - Main Application Logic

// Notice Templates
const noticeTemplates = {
    "1.9": {
        title: "Sub-Clause 1.9: Delayed Drawings or Instructions",
        subject: "NOTICE PURSUANT TO SUB-CLAUSE 1.9 [DELAYED DRAWINGS OR INSTRUCTIONS]",
        template: (data) => `
Dear ${data.recipientName},

RE: ${data.contractRef}
    ${data.subject}

We hereby give notice pursuant to Sub-Clause 1.9 [Delayed Drawings or Instructions] of the Conditions of Contract.

Event Date: ${data.formattedDate}

Description of Event:
${data.eventDescription}

We hereby notify you that the delayed provision of drawings and/or instructions as described above has caused, and/or is likely to cause, delay to the Works and/or additional Cost to the Contractor.

${data.additionalDetails ? `Additional Details:\n${data.additionalDetails}\n\n` : ''}We request that the necessary drawings and/or instructions be provided immediately to minimize further delay and additional costs.

We reserve our rights under the Contract to claim for extension of time and/or additional payment in accordance with the relevant provisions of the Conditions of Contract.

This notice is given without prejudice to any other rights or remedies available to the Contractor under the Contract or at law.

Yours faithfully,

[Contractor's Representative]
[Position/Title]
[Date]
`
    },
    "4.2": {
        title: "Sub-Clause 4.2: Performance Security",
        subject: "NOTICE PURSUANT TO SUB-CLAUSE 4.2 [PERFORMANCE SECURITY]",
        template: (data) => `
Dear ${data.recipientName},

RE: ${data.contractRef}
    ${data.subject}

We hereby give notice pursuant to Sub-Clause 4.2 [Performance Security] of the Conditions of Contract.

Event Date: ${data.formattedDate}

Description of Event:
${data.eventDescription}

We wish to bring to your attention the matters described above which relate to the Performance Security required under the Contract.

${data.additionalDetails ? `Additional Details:\n${data.additionalDetails}\n\n` : ''}We request your immediate attention to this matter and confirmation of the appropriate actions to be taken in accordance with the Contract provisions.

We reserve all our rights under the Contract and at law in relation to this matter.

This notice is given without prejudice to any other rights or remedies available to the Contractor under the Contract or at law.

Yours faithfully,

[Contractor's Representative]
[Position/Title]
[Date]
`
    },
    "8.3": {
        title: "Sub-Clause 8.3: Programme",
        subject: "NOTICE PURSUANT TO SUB-CLAUSE 8.3 [PROGRAMME]",
        template: (data) => `
Dear ${data.recipientName},

RE: ${data.contractRef}
    ${data.subject}

We hereby give notice pursuant to Sub-Clause 8.3 [Programme] of the Conditions of Contract.

Event Date: ${data.formattedDate}

Description of Event:
${data.eventDescription}

We wish to inform you of the matters described above which affect, or are likely to affect, the progress of the Works as shown in the current programme.

${data.additionalDetails ? `Additional Details:\n${data.additionalDetails}\n\n` : ''}We are reviewing the impact of this event on the programme and will submit a revised programme showing any necessary modifications to the sequence, methods, and timing of the Works.

We reserve our rights under the Contract to claim for extension of time and/or additional payment in accordance with the relevant provisions of the Conditions of Contract.

This notice is given without prejudice to any other rights or remedies available to the Contractor under the Contract or at law.

Yours faithfully,

[Contractor's Representative]
[Position/Title]
[Date]
`
    },
    "20.1": {
        title: "Sub-Clause 20.1: Contractor's Claims",
        subject: "NOTICE OF CLAIM PURSUANT TO SUB-CLAUSE 20.1 [CONTRACTOR'S CLAIMS]",
        template: (data) => `
Dear ${data.recipientName},

RE: ${data.contractRef}
    ${data.subject}

We hereby give notice of claim pursuant to Sub-Clause 20.1 [Contractor's Claims] of the Conditions of Contract.

Event or Circumstance Date: ${data.formattedDate}

Description of Event or Circumstance:
${data.eventDescription}

We consider that we are entitled to an extension of the Time for Completion and/or additional payment under the Contract as a result of the event or circumstance described above.

${data.additionalDetails ? `Additional Details:\n${data.additionalDetails}\n\n` : ''}This notice is given within 28 days after we became aware, or should have become aware, of the event or circumstance giving rise to the claim.

We will submit a fully detailed claim with supporting particulars within 42 days of becoming aware of the event or circumstance, or within such other period as may be agreed with the Engineer.

We are keeping contemporary records as required under Sub-Clause 20.1 and will provide such further information as the Engineer may reasonably require.

This notice is given without prejudice to any other rights or remedies available to the Contractor under the Contract or at law.

Yours faithfully,

[Contractor's Representative]
[Position/Title]
[Date]
`
    }
};

// DOM Elements
const clauseSelector = document.getElementById('clauseSelector');
const recipientName = document.getElementById('recipientName');
const contractRef = document.getElementById('contractRef');
const eventDate = document.getElementById('eventDate');
const eventDescription = document.getElementById('eventDescription');
const additionalDetails = document.getElementById('additionalDetails');
const generateBtn = document.getElementById('generateBtn');
const copyBtn = document.getElementById('copyBtn');
const downloadPdfBtn = document.getElementById('downloadPdfBtn');
const previewArea = document.getElementById('previewArea');
const actionButtons = document.getElementById('actionButtons');
const successAlert = document.getElementById('successAlert');
const successMessage = document.getElementById('successMessage');
const noticeForm = document.getElementById('noticeForm');

let generatedNotice = '';

// Format date to readable format
function formatDate(dateString) {
    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}

// Generate Notice
function generateNotice() {
    // Validate form
    if (!noticeForm.checkValidity()) {
        noticeForm.reportValidity();
        return;
    }

    const selectedClause = clauseSelector.value;

    if (!selectedClause) {
        showAlert('Please select a FIDIC clause.', 'danger');
        return;
    }

    const template = noticeTemplates[selectedClause];

    const data = {
        recipientName: recipientName.value.trim(),
        contractRef: contractRef.value.trim(),
        formattedDate: formatDate(eventDate.value),
        eventDescription: eventDescription.value.trim(),
        additionalDetails: additionalDetails.value.trim(),
        subject: template.subject
    };

    // Generate the notice
    generatedNotice = template.template(data);

    // Display in preview area
    previewArea.innerHTML = `<div class="letter-content">${generatedNotice.replace(/\n/g, '<br>')}</div>`;
    previewArea.classList.add('has-content');

    // Show action buttons
    actionButtons.style.display = 'block';

    // Scroll to preview
    previewArea.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    showAlert('Notice generated successfully!', 'success');
}

// Copy to Clipboard
async function copyToClipboard() {
    try {
        await navigator.clipboard.writeText(generatedNotice);
        showAlert('Notice copied to clipboard!', 'success');

        // Visual feedback on button
        const originalText = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="bi bi-check2"></i> Copied!';
        setTimeout(() => {
            copyBtn.innerHTML = originalText;
        }, 2000);
    } catch (err) {
        console.error('Failed to copy:', err);
        showAlert('Failed to copy to clipboard. Please try again.', 'danger');
    }
}

// Download as PDF
function downloadPDF() {
    try {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();

        // Set font
        doc.setFont("times", "normal");
        doc.setFontSize(12);

        // Add content
        const lines = doc.splitTextToSize(generatedNotice, 170);

        let y = 20;
        const lineHeight = 7;
        const pageHeight = doc.internal.pageSize.height;
        const margin = 20;

        lines.forEach(line => {
            if (y + lineHeight > pageHeight - margin) {
                doc.addPage();
                y = margin;
            }
            doc.text(line, 20, y);
            y += lineHeight;
        });

        // Generate filename
        const clauseValue = clauseSelector.value;
        const date = new Date().toISOString().split('T')[0];
        const filename = `FIDIC_Notice_${clauseValue}_${date}.pdf`;

        doc.save(filename);
        showAlert('PDF downloaded successfully!', 'success');
    } catch (err) {
        console.error('Failed to generate PDF:', err);
        showAlert('Failed to generate PDF. Please try again.', 'danger');
    }
}

// Show Alert
function showAlert(message, type = 'success') {
    successMessage.textContent = message;
    successAlert.className = `alert alert-${type} alert-dismissible fade show mt-3`;
    successAlert.style.display = 'block';

    // Auto-hide after 5 seconds
    setTimeout(() => {
        successAlert.style.display = 'none';
    }, 5000);
}

// Reset Form Handler
noticeForm.addEventListener('reset', function () {
    previewArea.innerHTML = `
        <p class="text-muted text-center">
            <i class="bi bi-info-circle"></i> 
            Fill in the form and click "Generate Notice" to see your letter here.
        </p>
    `;
    previewArea.classList.remove('has-content');
    actionButtons.style.display = 'none';
    generatedNotice = '';
});

// Event Listeners
generateBtn.addEventListener('click', generateNotice);
copyBtn.addEventListener('click', copyToClipboard);
downloadPdfBtn.addEventListener('click', downloadPDF);

// Real-time preview update on clause selection (optional enhancement)
clauseSelector.addEventListener('change', function () {
    if (this.value && previewArea.classList.contains('has-content')) {
        // Regenerate if already generated
        generateNotice();
    }
});

// Set default date to today
eventDate.valueAsDate = new Date();

// Initialize Bootstrap tooltips if needed
const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
});
