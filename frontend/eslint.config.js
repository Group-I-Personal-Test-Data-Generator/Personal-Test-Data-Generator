import path from "path";
import { fileURLToPath } from "url";
import js from "@eslint/js";
import { FlatCompat } from "@eslint/eslintrc";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Create compat helper for migrating old-style configs
const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: js.configs.recommended
});

export default [
  js.configs.recommended, // built-in recommended ESLint rules
  ...compat.config({
    rules: {
      "no-console": "warn",
      "eqeqeq": "error",
      "curly": "error",
      "no-unused-vars": ["warn", { args: "none" }]
    },
    env: {
      browser: true,
      node: true,
      es2021: true
    },
    parserOptions: {
      ecmaVersion: "latest",
      sourceType: "module"
    }
  })
];
