# Website Factory Master 1

**Current Version:** 1.0.0 (Generic Master Template)
**Last Updated:** 2026-01-21

## Overview
This is the **Master Template** for generating local service business websites. It contains:
- **Generic Structure:** `Layout.astro`, `Header.astro`, `Footer.astro` with generic placeholders.
- **Service Examples:** `service-example.astro` structure.
- **Strict Protocols:** `directives/master_design_prompt.md` enforces SEO, Research, and Verification loops.

## How to Use
1.  **Copy this folder** to a new directory (e.g., `my-new-client-site`).
2.  **Open the new folder** in your IDE.
3.  **Update `directives/master_design_prompt.md`**:
    - Fill in the "Business Details" section with the new client's info.
4.  **Install Dependencies**:
    - `npm install`
5.  **Start the Agent**:
    - Instruct the agent to "Read master_design_prompt.md and start the build".
6.  **Follow the Protocol**:
    - The agent will pause for Research, Localhost Verification, and Deployment approval.

## Protocols Enforced
- **Deep Research**: The agent must study competitors and local visuals first.
- **SEO Mandates**: Sitemap and Schema are mandatory.
- **No Auto-Push**: Deployment to Bunny.net requires explicit "DEPLOY" command.
