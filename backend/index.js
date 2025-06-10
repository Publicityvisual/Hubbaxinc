import express from 'express';
import fetch from 'node-fetch';
import path from 'path';
import { fileURLToPath } from 'url';

const app = express();
app.use(express.json());

const __dirname = path.dirname(fileURLToPath(import.meta.url));
app.use(express.static(path.join(__dirname, '../frontend')));

const AI_URL = process.env.AI_URL || 'http://ai:8000/generate';

app.post('/api/generate', async (req, res) => {
  const prompt = req.body.prompt || '';
  try {
    const response = await fetch(AI_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    });
    const data = await response.json();
    res.json(data);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to generate content' });
  }
});

app.post('/api/generate-html', async (req, res) => {
  const description = req.body.description || '';
  const prompt = `Genera un fragmento HTML basado en: ${description}`;
  try {
    const response = await fetch(AI_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    });
    const data = await response.json();
    res.json({ generated: Array.isArray(data) ? data[0] : data });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to generate HTML' });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Backend running on port ${port}`);
});
