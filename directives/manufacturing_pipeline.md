# DIR: Manufacturing-Pipeline (v1.7 - Librarian Edition)

## 1. PURPOSE
Autonomous "Factory" for high-end trade sites using Astro (Static HTML) for maximum performance and minimum resource usage.
- Brain: Gemini 1.5 Pro (Research & UI)
- Eyes: Nano Banana Pro (NBP)
    *   **Hero:** 1x Global Hero.
3.  **Brand Identity (Logo):**
    *   **Check:** If USER provided a logo path, copy to `public/images/logo.png` and update `Header.astro` to use `<img>` tag.
    *   **Fallback (Standard Build):** If NO logo is provided, do NOT generate one. Use the standard **Text + SVG Icon** layout in `Header.astro`.
- Hands: Python/Git/Coolify (Deployment)
- Standard: [Master Design Prompt](file:///c:/Users/srkel/Downloads/Website-builder-antigravity-at-scale/directives/master_design_prompt.md)

## 2. INPUTS
- `TRADE`: Business type (e.g., "High-End Roofer")
- `LOC`: Target City, State
- `BRAND`: (Auto-gen if null)
- `DETAILS`: Specific business details provided in Section 1 of the Master Prompt.

## 3. LAYER 3 TOOLS (Execution Manifest)
- `execution/research_market.py` -> API search (Tavily/Exa) for keywords and local context.
- `execution/generate_hero_nbp.py` -> Call NBP API; save to `public/images/hero.jpg`.
- `execution/unified_deploy.py` -> Astro build -> Git push -> Coolify.

## 4. WORKFLOW (Layer 2 Orchestration)

### Phase 1: Research & Context
1. **Search Grounding**: Use the `search` tool to analyze the specific subject matter and location (vegetation, architecture, terrain).
2. **Competitor Audit (NEW)**:
    - Identify Top 3 Competitors in the target area.
    - Extract their **Services Offered** (to find gaps or must-haves).
    - Analyze their **Keywords** (to find ranking opportunities).
3. **Context Gathering**: Understand the "Librarian" context - what verifiable facts does the AI need?

### Phase 2: Keyword & Entity Discovery
1.  **Search:** "[Industry] regulations [Target Suburb]", "[Physical Entity] types [Target Suburb]" (e.g., Soil/Water/Rock), "[Target Suburb] local planning codes".
2.  **Identify Entities:** List specific creeks, parks, council names, and estates to anchor the content.
3.  **Keyword Expansion:** Find 3-5 high-volume keywords + 3 local long-tail questions.
3. **Data Store**: Save brief to `.tmp/market_data.json`.

### Phase 3: Asset Creation
1.  **Prompt Engineering:** Write photorealistic, research-backed prompts for unique images.
2.  **Production:** Generate unique assets to `public/images/`.


### Phase 4: Page Build & Component Assembly
1. **Structure**: Use `src/layouts/Layout.astro` and `src/pages/index.astro`.
2. **Design Standards**: Apply "Hand-Crafted" typography, whitespace, and texture.
3. **SEO Mandate**: Implement `<SEO />` and semantic HTML5.

### Phase 5: AI Optimization (GEO)
1. **Data Feeding**: Add hyper-specific technical specs and comparison tables.
2. **Trust Signals**: Embed verification badges (Licensed, Insured, etc.).

### Phase 6: Integration & Polish
1. **Routing**: Ensure all links and routing are functional.
2. **Sitemap**: Update `sitemap.xml`.

### Phase 7: Verification & Deployment
1.  **Keyword Audit**: Explicitly check that all User Provided and Researched keywords are present in the H1, H2, or body.
2.  **Build**: Run `npm run build` to verify the static output.
3.  **Infrastructure**: Deploy using the factory's automated scripts to Coolify.

### Phase 8: Post-Manufacturing Audit (MANDATORY)
1.  **Run Audit**: Execute `python execution/factory_audit.py` to verify strict compliance.
    - **Silo Check**: Ensures >3 service pages exist (No Single-Page Sites).
    - **Asset Check**: Verifies 5+ unique assets exist (No Repetition).
    - **H1 Check**: Verifies H1 tags contain "[Service] + [Location]".
    - **Schema Check**: Confirms JSON-LD implementation.
    - **Sitemap Check**: Confirms `sitemap()` integration is active.
    - **Trust Check**: Confirms presence of "Licensed/Insured" signals.
2.  **Hard Stop**: If Audit Fails, DO NOT hand over to client. Rectify immediately.

## 5. COOLIFY DEPLOYMENT PROTOCOL
*   **Standard:** Deploy to staging (e.g., `[project].coolify.app`).
*   **Custom Domain (When Requested):**
    1.  **Identify:** Check `master_design_prompt.md` or User Request for the domain name.
    2.  **Config:** Update Coolify Service -> Settings -> Domains.
    3.  **DNS:** Provide the USER with the necessary A Records / CNAME pointing to the Coolify IP.
    4.  **Verify:** Ensure SSL generation succeeds.

## 6. SELF-ANNEALING LOOPS
- **Performance Fail**: If Lighthouse score < 95, optimize images -> Regenerate.
- **Copy Fail**: If tone is generic, apply "Editorial Voice" -> Regenerate.

## 7. DELIVERABLES
- **LIVE_URL**: [Coolify Endpoint]
- **GIT_REPO**: [GitHub URL]
- **STATUS**: Success
