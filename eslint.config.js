import js from '@eslint/js';import globals from 'globals';import tseslint from 'typescript-eslint';
export default tseslint.config({ignores:['dist/**','.cache/**','public/**','src/scene/**']},{files:['src/**/*.{ts,tsx}','scripts/*.ts','vite.config.ts'],extends:[js.configs.recommended,...tseslint.configs.recommended],languageOptions:{globals:{...globals.browser,...globals.node}}});
