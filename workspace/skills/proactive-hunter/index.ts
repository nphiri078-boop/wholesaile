import fs from 'fs';
import { parse } from 'json5';
import { LeadSchema } from '../../packages/deal-db/src/schema.js';

const counties = JSON.parse(fs.readFileSync('../../workspace/config/florida-counties.json', 'utf8')).top10.map(c => c.name);

console.log('Proactive Hunter TS stub ready. Counties:', counties.length);

// TODO: loop counties, scrape, parse, save
// await import('browser_agent');
// for (const county of counties) { ... }
