function Header() {
  return (
    <header className="rg-header">
      <div className="container rg-header__inner">
        <div className="rg-brand">
          <span className="rg-mark" aria-hidden="true">
            RG
          </span>
          <div className="rg-brand__text">
            <p className="rg-brand__name">RoleGazer</p>
            <p className="rg-brand__tagline">
              Encontrá las oportunidades que mejor encajan con tu perfil
            </p>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header
