import "./App.css";

function App() {
  return (
    <div className="app-shell">
      <header className="app-header">
        <h1>Plataforma Financiera Modular</h1>
        <p>Proyecto final de Fundamentos de Programación</p>
      </header>

      <main className="app-main">
        <section className="card">
          <h2>Dashboard</h2>
          <p>Vista principal del sistema.</p>
        </section>

        <section className="card">
          <h2>Módulos activos</h2>
          <p>Ingresos, gastos, flujo de caja, reportes y más.</p>
        </section>
      </main>
    </div>
  );
}

export default App;
