// In a file like api/sendRequests.js
// This is an example of an API route in Vercel

import fetch from 'node-fetch'; // or use any other HTTP client library

export default async function handler(req, res) {
  const { key, token, number } = req.query;

  const url = `https://hemlohahaa.vercel.app/send_requests?key=${key}&token=${token}&number=${number}`;
  const response = await fetch(url);

  if (response.ok) {
    const data = await response.json();
    res.status(200).json(data);
  } else {
    res.status(500).json({ error: 'Failed to send requests to the Flask backend' });
  }
}
