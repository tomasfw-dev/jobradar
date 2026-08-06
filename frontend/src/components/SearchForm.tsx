import { useState, type FormEvent } from 'react'
import type {
  Modality,
  SearchFilters,
  SelectOption,
  Seniority,
} from '../types/search'

const modalityOptions: SelectOption<Modality>[] = [
  { value: 'all', label: 'Todas' },
  { value: 'remote', label: 'Remoto' },
  { value: 'hybrid', label: 'Híbrido' },
  { value: 'onsite', label: 'Presencial' },
]

const seniorityOptions: SelectOption<Seniority>[] = [
  { value: 'all', label: 'Todos' },
  { value: 'trainee', label: 'Trainee' },
  { value: 'junior', label: 'Junior' },
  { value: 'semi-senior', label: 'Semi Senior' },
  { value: 'senior', label: 'Senior' },
]

const initialFilters: SearchFilters = {
  query: '',
  location: '',
  modality: 'all',
  seniority: 'all',
}

function SearchForm() {
  const [filters, setFilters] = useState<SearchFilters>(initialFilters)

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
  }

  return (
    <form className="rg-search-form card border-0 shadow-sm" onSubmit={handleSubmit}>
      <div className="card-body p-4">
        <div className="row g-3">
          <div className="col-12 col-lg-6">
            <label htmlFor="query" className="form-label">
              Puesto o tecnología
            </label>
            <input
              id="query"
              name="query"
              type="text"
              className="form-control"
              placeholder="Ej: Node.js, Python, Backend Developer"
              value={filters.query}
              onChange={(event) =>
                setFilters((current) => ({
                  ...current,
                  query: event.target.value,
                }))
              }
            />
          </div>

          <div className="col-12 col-lg-6">
            <label htmlFor="location" className="form-label">
              Ubicación
            </label>
            <input
              id="location"
              name="location"
              type="text"
              className="form-control"
              placeholder="Ej: Argentina, Buenos Aires, Remoto"
              value={filters.location}
              onChange={(event) =>
                setFilters((current) => ({
                  ...current,
                  location: event.target.value,
                }))
              }
            />
          </div>

          <div className="col-12 col-md-6 col-lg-4">
            <label htmlFor="modality" className="form-label">
              Modalidad
            </label>
            <select
              id="modality"
              name="modality"
              className="form-select"
              value={filters.modality}
              onChange={(event) =>
                setFilters((current) => ({
                  ...current,
                  modality: event.target.value as Modality,
                }))
              }
            >
              {modalityOptions.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </div>

          <div className="col-12 col-md-6 col-lg-4">
            <label htmlFor="seniority" className="form-label">
              Seniority
            </label>
            <select
              id="seniority"
              name="seniority"
              className="form-select"
              value={filters.seniority}
              onChange={(event) =>
                setFilters((current) => ({
                  ...current,
                  seniority: event.target.value as Seniority,
                }))
              }
            >
              {seniorityOptions.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </div>

          <div className="col-12 col-lg-4 d-flex align-items-end">
            <button type="submit" className="btn rg-btn-primary w-100">
              Buscar ofertas
            </button>
          </div>
        </div>
      </div>
    </form>
  )
}

export default SearchForm
