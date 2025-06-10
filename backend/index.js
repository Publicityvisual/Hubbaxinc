import express from 'express';
import fetch from 'node-fetch';

const app = express();
app.use(express.json());

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

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Backend running on port ${port}`);
});
