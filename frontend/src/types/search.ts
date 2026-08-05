export type Modality = 'all' | 'remote' | 'hybrid' | 'onsite'
export type Seniority = 'all' | 'trainee' | 'junior' | 'semi-senior' | 'senior'

export interface SearchFilters {
  query: string
  location: string
  modality: Modality
  seniority: Seniority
}

export interface SelectOption<T extends string> {
  value: T
  label: string
}
