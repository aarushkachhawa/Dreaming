import type { NextApiRequest, NextApiResponse } from 'next'
import fs from 'fs'
import path from 'path'

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const { id } = req.query
    const explorationPath = path.join(
      process.cwd(),
      '..',
      'explorations',
      `${id}.json`
    )

    if (!fs.existsSync(explorationPath)) {
      return res.status(404).json({ error: 'Exploration not found' })
    }

    const content = fs.readFileSync(explorationPath, 'utf-8')
    const exploration = JSON.parse(content)

    res.status(200).json({ exploration })
  } catch (error) {
    res.status(500).json({ error: 'Failed to load exploration' })
  }
}
