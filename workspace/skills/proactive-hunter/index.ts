import fs from 'fs/promises';
import path from 'path';
import { z } from 'zod';
import { spawn } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(spawn);

const LeadSchema = z.object({
  address: z.string(),
  city: z.string(),
  county: z.string(),
  state: z.string().default('FL'),
  zip: z.string().optional(),
  arv: z.number().optional(),
  repairs: z.number().optional(),
  mao: z.number().optional(),
  beds: z.number().optional(),
  baths: z.number().optional(),
  sqft: z.number().optional(),
  source: z.string().min(1),
  status: z.string().default('new'),
  notes: z.string().optional()
});

const repoRoot = path.resolve(__dirname, '../../../..');
const configPath = path.join(repoRoot, 'workspace/config/florida-counties.json');
const dealsDir = path.join(repoRoot, 'workspace/deals');

async function main(budget = 800) {
  const config = JSON.parse(await fs.readFile(configPath, 'utf8'));
  const counties = config.top10.slice(0, budget > 2000 ? undefined : 10).map(c => c.name);
  let totalLeads = 0;

  for (const county of counties) {
    console.log(`🦅 Hunting ${county}...`);
    // Camofox scrape XLeads/BatchData
    const scrapeCmd = `bunx camofox-browser 'New session, go to xleads.com search "${county} FL distressed motivated seller preforeclosure", scrape listings addresses prices owners phones beds baths sq ft arv, end task'`;
    const { stdout } = await execAsync(scrapeCmd, { shell: true, cwd: repoRoot });
    
    // Parse scraped text (simple regex for demo)
    const leadsRaw = parseScraped(stdout.toString());
    const validLeads = leadsRaw.map(raw => {
      try { return LeadSchema.parse(raw); } catch { return null; }
    }).filter(Boolean);

    if (validLeads.length) {
      const file = path.join(dealsDir, `${county}-${Date.now()}.md`);
      await fs.mkdir(dealsDir, { recursive: true });
      await fs.writeFile(file, markdownTable(validLeads));
      totalLeads += validLeads.length;
      // Sim DB insert (future drizzle)
      console.log(`Saved ${validLeads.length} leads to ${file}`);
      // Telegram
      await telegramNotify(`New ${county} leads: ${validLeads.length}`);
    }
  }
  console.log(`✅ Hunt complete: ${totalLeads} leads`);
}

function parseScraped(text) { /* regex parse addresses etc */ return []; }
function markdownTable(leads) { /* table */ return '| Address | ... |'; }
async function telegramNotify(msg) { /* curl */ }

main(process.argv[2] ? parseInt(process.argv[2]) : 800);
