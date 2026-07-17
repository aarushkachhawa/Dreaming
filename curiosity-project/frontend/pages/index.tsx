import Head from 'next/head'
import Link from 'next/link'
import { useEffect, useState } from 'react'

interface Exploration {
  id: string
  date: string
  title: string
  question: string
  summary: string
  tags: string[]
}

export default function Home() {
  const [explorations, setExplorations] = useState<Exploration[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/explorations')
      .then(res => res.json())
      .then(data => {
        setExplorations(data.explorations || [])
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  return (
    <>
      <Head>
        <title>The Curiosity Project</title>
        <meta name="description" content="Nightly explorations of interesting ideas" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>

      <main className="container">
        <header className="header">
          <h1>The Curiosity Project</h1>
          <p className="subtitle">Explorations generated each night while dreaming</p>
        </header>

        <section className="explorations">
          {loading ? (
            <div className="loading">Awakening curiosities...</div>
          ) : explorations.length === 0 ? (
            <div className="empty">
              <p>The first exploration is being generated...</p>
            </div>
          ) : (
            <div className="grid">
              {explorations.map((exploration) => (
                <Link href={`/exploration/${exploration.id}`} key={exploration.id}>
                  <article className="card">
                    <div className="card-date">{new Date(exploration.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}</div>
                    <h2 className="card-title">{exploration.title}</h2>
                    <p className="card-question">{exploration.question}</p>
                    <p className="card-summary">{exploration.summary}</p>
                    <div className="card-tags">
                      {exploration.tags.map(tag => (
                        <span key={tag} className="tag">{tag}</span>
                      ))}
                    </div>
                  </article>
                </Link>
              ))}
            </div>
          )}
        </section>
      </main>
    </>
  )
}
