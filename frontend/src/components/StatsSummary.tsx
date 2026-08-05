interface StatItem {
  label: string
  value: number
}

const stats: StatItem[] = [
  { label: 'Ofertas encontradas', value: 0 },
  { label: 'Nuevas oportunidades', value: 0 },
  { label: 'Postulaciones', value: 0 },
]

function StatsSummary() {
  return (
    <section className="jr-stats" aria-label="Resumen de actividad">
      <div className="row g-3">
        {stats.map((stat) => (
          <div key={stat.label} className="col-12 col-md-4">
            <article className="jr-stat-card card border-0 h-100">
              <div className="card-body">
                <p className="jr-stat-card__value mb-1">{stat.value}</p>
                <h2 className="jr-stat-card__label h6 mb-0">{stat.label}</h2>
              </div>
            </article>
          </div>
        ))}
      </div>
    </section>
  )
}

export default StatsSummary
