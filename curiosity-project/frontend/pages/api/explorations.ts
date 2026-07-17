import type { NextApiRequest, NextApiResponse } from 'next'
import fs from 'fs'
import path from 'path'

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const dataPath = path.join(process.cwd(), '..', 'data', 'metadata')
    let explorations = []

    if (fs.existsSync(dataPath)) {
      const files = fs.readdirSync(dataPath).filter(f => f.endsWith('.json'))
      explorations = files
        .map(file => {
          const filePath = path.join(dataPath, file)
          const content = fs.readFileSync(filePath, 'utf-8')
          return JSON.parse(content)
        })
        .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())
    }

    res.status(200).json({ explorations })
  } catch (error) {
    res.status(500).json({ error: 'Failed to load explorations' })
  }
}
