function Header() {
  return (
    <header className="jr-header">
      <div className="container jr-header__inner">
        <div className="jr-brand">
          <span className="jr-mark" aria-hidden="true">
            JR
          </span>
          <div className="jr-brand__text">
            <p className="jr-brand__name">JobRadar</p>
            <p className="jr-brand__tagline">
              Encontrá las oportunidades que mejor encajan con tu perfil
            </p>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header
