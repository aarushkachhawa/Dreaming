import Head from 'next/head'
import Link from 'next/link'
import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'

interface ExplorationDetail {
  id: string
  date: string
  title: string
  question: string
  summary: string
  tags: string[]
  content: string
  perspectives: Array<{
    title: string
    description: string
  }>
  connections: string[]
  openQuestions: string[]
}

export default function ExplorationPage() {
  const router = useRouter()
  const { id } = router.query
  const [exploration, setExploration] = useState<ExplorationDetail | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (!id) return

    fetch(`/api/explorations/${id}`)
      .then(res => res.json())
      .then(data => {
        setExploration(data.exploration)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [id])

  if (loading) {
    return (
      <>
        <Head><title>Loading...</title></Head>
        <main className="container">
          <div className="loading">Reading the dream...</div>
        </main>
      </>
    )
  }

  if (!exploration) {
    return (
      <>
        <Head><title>Not Found</title></Head>
        <main className="container">
          <Link href="/" className="back-link">← Back to explorations</Link>
          <div className="empty">Exploration not found</div>
        </main>
      </>
    )
  }

  return (
    <>
      <Head>
        <title>{exploration.title} - The Curiosity Project</title>
        <meta name="description" content={exploration.summary} />
      </Head>

      <main className="container exploration">
        <Link href="/" className="back-link">← Back to explorations</Link>

        <header className="exploration-header">
          <time className="exploration-date">
            {new Date(exploration.date).toLocaleDateString('en-US', {
              weekday: 'long',
              year: 'numeric',
              month: 'long',
              day: 'numeric'
            })}
          </time>
          <h1 className="exploration-title">{exploration.title}</h1>
          <p className="exploration-question">{exploration.question}</p>
          <div className="exploration-tags">
            {exploration.tags.map(tag => (
              <span key={tag} className="tag">{tag}</span>
            ))}
          </div>
        </header>

        <section className="exploration-content">
          <div className="prose" dangerouslySetInnerHTML={{ __html: exploration.content }} />
        </section>

        {exploration.perspectives.length > 0 && (
          <section className="perspectives">
            <h2>Multiple Perspectives</h2>
            <div className="perspectives-grid">
              {exploration.perspectives.map((p, i) => (
                <div key={i} className="perspective">
                  <h3>{p.title}</h3>
                  <p>{p.description}</p>
                </div>
              ))}
            </div>
          </section>
        )}

        {exploration.openQuestions.length > 0 && (
          <section className="open-questions">
            <h2>Open Questions</h2>
            <ul>
              {exploration.openQuestions.map((q, i) => (
                <li key={i}>{q}</li>
              ))}
            </ul>
          </section>
        )}

        {exploration.connections.length > 0 && (
          <section className="connections">
            <h2>Connections to Other Ideas</h2>
            <ul>
              {exploration.connections.map((c, i) => (
                <li key={i}>{c}</li>
              ))}
            </ul>
          </section>
        )}
      </main>
    </>
  )
}
