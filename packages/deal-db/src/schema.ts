import { pgTable, serial, text, numeric, timestamp, varchar, integer } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

export const leads = pgTable('leads', {
  id: serial('id').primaryKey(),
  address: varchar('address', { length: 255 }).notNull(),
  city: varchar('city', { length: 100 }).notNull(),
  county: varchar('county', { length: 100 }).notNull(),
  state: varchar('state', { length: 2 }).default('FL'),
  zip: varchar('zip', { length: 10 }),
  arv: numeric('arv', { precision: 12, scale: 2 }),
  repairs: numeric('repairs', { precision: 12, scale: 2 }),
  mao: numeric('mao', { precision: 12, scale: 2 }),
  beds: integer('beds'),
  baths: integer('baths'),
  sqft: integer('sqft'),
  source: varchar('source', { length: 100 }).notNull(),
  status: varchar('status', { length: 50 }).default('new'),
  scrapedAt: timestamp('scraped_at').defaultNow(),
  notes: text('notes')
});

export const leadsRelations = relations(leads, ({ many }) => ({
  // future relations
}));

// Zod schema for validation
export const leadSchema = /* Zod schema here later */;
