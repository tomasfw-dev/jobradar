function EmptyState() {
  return (
    <section className="rg-empty" aria-labelledby="empty-title">
      <div className="rg-empty__panel">
        <h2 id="empty-title" className="h4 mb-2">
          Todavía no realizaste ninguna búsqueda
        </h2>
        <p className="mb-0">
          Completá los filtros y presioná &quot;Buscar ofertas&quot;. Los
          resultados aparecerán aquí cuando ejecutes una búsqueda.
        </p>
      </div>
    </section>
  )
}

export default EmptyState
