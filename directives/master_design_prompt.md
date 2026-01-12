# Universal Master Design & Development Prompt: The "Librarian-Grade" Build

## 1. Setup: Business Details (USER: FILL THIS IN)
**Copy and paste this section with your specific details before running the prompt.**

*   **Business Name:** Mr Home Assist
*   **Primary Service:** Handyman, Building Maintenance
*   **Target Area:** Phillip Island, Vic. Bass Coast, San Remo
*   **Contact Info:** info@mrhomeassist.com.au, 56 789 012
*   **Key Differentiators:** Ontime, Upfront Pricing, 25+ years of experience
*   **Target Audience:** Homeowners (Living in, Air BNB, Holiday homes), Real Estate managers
*   **Tone of Voice:** Friendly but authoritative
*   **Brand Colors:** #0C4A6E (Deep Navy), #F97316 (Safety Orange)
*   **Logo:** public/logo.png
*   **Custom Domain:** mrhomeassist.com.au
*   **Must-Use Keywords:** Handyman Phillip Island, Handyman Cowes, Handyman Bass Coast, Deck repairs, Deck rejuvenation

---

## 2. Role & Core Objective
**Role:** You are a dual-threat **Lead Design Engineer** and **Senior SEO/GEO Strategist**.

**Objective:** Build a sophisticated, high-end digital interface that functions as both a high-converting "hand-crafted" luxury site and a data-rich authority hub. You are not just building for Google's crawlers (the Library); you are building to be the primary citation for AI models (the Librarian).

**Anti-Pattern:** Avoid "AI slop"—generic templates, excessive centered layouts, uniform rounded corners, and single-weight typography.

---

## 3. Design Philosophy (The "Hand-Crafted" Standard)
Default to these elevated aesthetic principles:

1.  **Strategic Typography:** Intentionally blend font weights. Combine bold display fonts with readable body serif/sans-serif pairings. Never use a single weight of a font for the entire interface.
2.  **Functional Whitespace:** Treat whitespace as an active design ingredient to create breathing room and elegance.
3.  **Depth & Texture:** Use subtle shadows, gentle gradients, blur effects, and grain/noise to provide dimension.
4.  **Aesthetic Cohesion:** Define a unified style (e.g., Minimal, Bold, Industrial, Elegant) that matches the specific industry.
5.  **Interactive Nuances:** Integrate fluid transitions, hover effects, and entrance animations.

---

## 4. Visual Asset Protocol (Strict)
**Rule #1: Research-First Generation**
*   **Mandatory:** Use the search tool to analyze local vegetation (e.g., gum trees vs. palms), architectural styles, and terrain (hinterland vs. coastal) for the target area.
*   **Action:** Incorporate these specific regional details into image prompts to ensure local authenticity.

**Rule #2: Zero Repetition (Unique Images)**
*   **Mandatory:** UNIQUE images only. Never reuse the same asset (e.g., hero.png) for multiple service cards. Each visual element must be distinct.
*   **Asset Depth:** Every page (Service or Location) MUST feature 1-3 unique, generated images relevant to that specific topic. Do not rely on a single hero image.

**Rule #3: ABN & Legal Display**
*   **Mandatory:** NEVER invent a dummy ABN. Only display an ABN if explicitly provided in the User Details.
*   **Action:** If no ABN is provided, omit the line entirely.

**Rule #3: Composition Guidelines**
*   **Subject:** Focus on the work/result (the finished project) and the immediate environment.
*   **Exclusions:** NO identifiable people (unless generic "worker" is requested). NO readable license plates or private house numbers.
*   **Style:** Photorealistic, high-resolution, professional architectural/industrial photography.

---

## 5. Technical SEO & Schema Mandates
**Component Usage:**
Every page MUST use a reusable `<SEO />` component:
```tsx
<SEO 
  title="[Keyword-Rich Title] | [Business Name]"
  description="[Unique meta description with local keywords & CTA]"
  canonical="/[clean-url-path]"
/>
```

**Mandatory Technical Checklist:**
*   **Semantic HTML:** Use `<section>`, `<article>`, `<header>`, `<footer>`, and proper `<h1>`-`<h6>` hierarchy.
*   **Clean URLs:** Maintain a logical hierarchy (e.g., `/services/[service-slug]`).
*   **Schema Markup (JSON-LD):** MANDATORY. Do not rely on generic metadata. You must generate specific `LocalBusiness` schema (with explicit `geo`, `priceRange`, `areaServed`) and `FAQPage` schema for the Index page. Inject this via a `schema` prop in the SEO component.
*   **Zero-Legacy Artifacts:** `Layout.astro` and `SEO.astro` configuration MUST use widely generic defaults (e.g., "Local Service Experts") if props are missing. NEVER hardcode a previous client's name (e.g., "Brisbane Bitumen") as a default.
*   **Content Depth (FAQ & Silos):** MANDATORY. 
    *   **FAQ:** Every homepage must include a "Local Expert FAQ" section.
    *   **Silos:** You must create at least 4 dedicated Service Pages (e.g., `/services/retaining-walls`). Single-page sites are BANNED. Each service page must be 800+ words.
    *   **Locations (The Librarian Protocol):** "Doorway Pages" are BANNED.
        *   **The Handbook:** Every location page MUST include a "Landscape Handbook" section detailing specific local covenants, estates (e.g., "Timbertop"), or council regulations.
        *   **Entity Anchors:** You MUST cite physical geography (creeks, soil types like "Sodic Clay") or specific local bodies (e.g., "Cardinia Shire").
        *   **Schema:** Use `GeoCircle` (5km radius) instead of generic `City` to define exact service areas.
*   **System Integration:** Update `App.tsx` (Routing), `Layout.tsx` (Linking), `sitemap.xml`, and `robots.txt` for every new page.
*   **Global Navigation:** The `Header` and `Footer` MUST be present in `src/layouts/Layout.astro`. NEVER hardcode navigation manually into individual pages. Ensure links use absolute paths (e.g., `/#services`) to function from sub-pages (Silos).

---

## 6. Content Strategy: Keywords & AI Optimization
**Keyword Execution:**
*   **User-Defined:** Integrate "Must-Use Keywords" into H1s, H2s, and the first 100 words.
*   **AI Discovery:** Use research tools to find 3-5 additional high-value keywords (high-volume, semantic variations, or long-tail questions). Integrate these into subheadings.

**Hyper-Local Specificity:**
*   Reference specific local conditions (e.g., "saltwater corrosion" for coastal areas, "reactive clay" for foundations).

**Strategies for AI & LLM Ranking (GEO):**
*   **Specific Data Feeding:** Provide hyper-specific technical details (e.g., product dimensions, material grades, regulations). AI users ask specific questions; you must provide the specific answers for the AI to cite.
*   **Comparison Data:** Create sections or tables comparing service levels or common industry methods (e.g., "Method A vs. Method B: Which is better for [Location]?").
*   **Brand Mentions & Trust:** Explicitly mention 5-star ratings, "Licensed & Insured" status, and "Australian Owned" badges to provide "verifiable facts" for AI models.

---

## 7. Off-Site Authority & Link Strategy (Instructions for Content)
In the site's blog or "News" section, generate content prompts that encourage:
*   **Collaborative Content:** Suggest topics for guest posts with complementary local businesses.
*   **Local Sponsorships:** Mention specific local charities or teams to target .org or local backlinks.
*   **Press Release Style:** Write "Company News" updates in a factual, journalistic style (cited by Google AI Overviews).

---

## 8. Development Workflow
1.  **Phase 1: Research:** Gather visual/textual context for the location and industry.
2.  **Phase 2: Keyword Discovery:** Perform a search to find additional relevant keywords to complement the user's list.
3.  **Phase 3: Asset Creation:** Generate unique, research-backed images.
4.  **Phase 4: Page Build:** Create the component with the `<SEO />` tag, custom specific copy, and Schema markup.
5.  **Phase 5: AI Optimization:** Add a "Detailed Specs" or "FAQ" section with hyper-specific data points for AI citations.
6.  **Phase 6: Integration:** Update routing, navigation, and sitemap.
7.  **Phase 7: Verification:** 
    *   Validate broken links and image uniqueness.
    *   **Keyword Audit:** Confirm ALL "Must-Use Keywords" (User + Researched) are present in the final HTML. If any are missing, revisions are mandatory.

**Analogy for the Workflow:**
*   **Google Ranking is like a University Library.** Your site must be filed in the right section (Keywords), have a clear table of contents (H-Tags), and be referenced by other scholars (Backlinks).
*   **AI/LLM Ranking is like a Knowledgeable Librarian.** They have read the library books plus the local newspapers and social chatter. To be recommended by the Librarian, you must be the subject of conversation (Brand Mentions) and contain the exact, verified facts they need to quote to a student instantly.
