import { FlatCompat } from '@eslint/eslintrc';
const compat = new FlatCompat({ baseDirectory: __dirname });

export default [
  // Extend recommended ESLint rules
  ...compat.config({
    extends: ['eslint:recommended'],

    // Define your custom rules here
    rules: {
      // Example rules you might have used before
      'no-console': 'warn',           // Warn on console.log
      'eqeqeq': 'error',              // Require === and !==
      'curly': 'error',               // Require curly braces for blocks
      'no-unused-vars': ['warn', { args: 'none' }], // Warn on unused vars
      // Add any other rules your team wants
    },

    env: {
      browser: true,
      node: true,
      es2021: true
    },

    parserOptions: {
      ecmaVersion: 13,
      sourceType: 'module'
    }
  }),
];
