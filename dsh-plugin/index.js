import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { BUNDLED_SKILL_RANK } from "@deepseek-ai/dsh-skill";

// Bundled `tkinter-desktop` skill provider for DeepSeek Harness.
//
// This is the embedded-provider pattern used by the official
// `@deepseek-ai/dsh-skill-badge` plugin: the SKILL.md body lives in assets/,
// and the skill is registered on ctx.skills via registerProvider().
// resourceBase points at the skill repository root so the model can resolve
// the references/, scripts/, examples/ paths the SKILL.md body cites.
//
// NOTE: this is a LOCAL / in-repo plugin, NOT a distributable self-contained
// npm package. resourceBase resolves to the parent skill repo via a relative
// path; after `npm publish` the package installs under a profile's
// node_modules and that path no longer points at the skill repo, so resource
// resolution breaks. Do not publish to npm in its current form.

const PROVIDER_NAME = "tkinter-desktop";

// assets/SKILL.md holds a copy of the skill body (kept in sync with SKILL.md).
const SKILL_BODY_URL = new URL("../assets/SKILL.md", import.meta.url);

// The skill root is the parent of this dsh-plugin/ directory, so the body's
// relative references (references/..., scripts/..., examples/...) resolve.
const RESOURCE_BASE = {
  kind: "directory",
  path: fileURLToPath(new URL("../../", import.meta.url)),
};

const CANDIDATE = {
  name: "tkinter-desktop",
  description:
    "Tkinter/ttk native desktop application development skill: full lifecycle from need discovery, MVC architecture, .ui interface design (pygubu Builder), coding, threading & async, SQLite data layer, quality gates to PyInstaller packaging into a native Windows EXE (no browser, no local HTTP server). Use when the user mentions Tkinter, ttk, native desktop GUI, Python built-in GUI, .ui-based tkinter apps, or wants a desktop program that does not depend on a browser.",
  invocation: { modelInvocable: true, userInvocable: true },
  provider: PROVIDER_NAME,
  source: "bundled",
  resourceBase: RESOURCE_BASE,
  rank: BUNDLED_SKILL_RANK,
  locator: SKILL_BODY_URL,
};

const provider = {
  name: PROVIDER_NAME,
  list: () => Promise.resolve([CANDIDATE]),
  async get(_candidate) {
    return {
      name: CANDIDATE.name,
      description: CANDIDATE.description,
      invocation: CANDIDATE.invocation,
      provider: CANDIDATE.provider,
      source: CANDIDATE.source,
      resourceBase: RESOURCE_BASE,
      content: await readFile(SKILL_BODY_URL, "utf8"),
    };
  },
};

/** Cordis plugin name. */
export const name = "tkinter-desktop";
/** Service required by the bundled provider. */
export const inject = ["skills"];

/** Register the bundled `tkinter-desktop` provider on ctx.skills. */
export function apply(ctx) {
  ctx.skills.registerProvider(() => provider);
}
