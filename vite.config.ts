import { mediaPlugin } from './scripts/media-plugin.ts';
import {defineConfig} from 'vite';import react from '@vitejs/plugin-react';export default defineConfig({plugins: [mediaPlugin(), react()]});
