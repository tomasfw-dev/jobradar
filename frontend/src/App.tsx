import EmptyState from './components/EmptyState'
import Header from './components/Header'
import SearchForm from './components/SearchForm'
import StatsSummary from './components/StatsSummary'
import './App.css'

function App() {
  return (
    <div className="rg-app">
      <Header />

      <main className="rg-main">
        <div className="container">
          <section className="rg-intro" aria-labelledby="intro-title">
            <h1 id="intro-title" className="rg-intro__title">
              Tu próxima oportunidad, en un solo lugar
            </h1>
            <p className="rg-intro__description">
              RoleGazer recopila y analiza ofertas laborales de distintas
              fuentes para que encuentres roles tecnológicos alineados con tu
              perfil, sin recorrer múltiples sitios.
            </p>
          </section>

          <SearchForm />
          <StatsSummary />
          <EmptyState />
        </div>
      </main>
    </div>
  )
}

export default App
