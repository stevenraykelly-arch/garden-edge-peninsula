---
description: Architecture and Usage of the Global Contact Form
---

# Contact Form Architecture

The website includes a global contact form "placeholder" section that appears on every page above the footer.

## Component Structure

- **File**: `src/components/ContactForm.astro`
- **Location**: Imported and placed in `src/layouts/Layout.astro` immediately before the `<Footer />`.

## Usage & Customization

The component is designed to host a 3rd party form embed (e.g. HubSpot, Mailchimp, Tally, or a generic HTML form).

### How to insert a real form:

1.  Open `src/components/ContactForm.astro`.
2.  Locate the placeholder `div`:
    ```astro
    {/* Placeholder for Custom Form Code */}
    <div id="contact-form-placeholder" ...>
       ...
    </div>
    ```
3.  **Replace** the entire `div` (or just its contents) with your `<script>` or `<iframe>` code.

### Text Updates

- **Headings**: The text "Request More Information" and "Tell us about your project" are hardcoded in `ContactForm.astro`.
- **Phone Number**: The phone number is also hardcoded in the paragraph text within the same file.
