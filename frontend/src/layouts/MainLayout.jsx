import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";
import "../App.css";

function MainLayout() {
  return (
    <div className="app-layout">
      <Sidebar />
      <div className="app-content">
        <Topbar />
        <main className="page-content">
          <h1>Dashboard</h1>
          <p>Bienvenida a la plataforma financiera modular.</p>
        </main>
      </div>
    </div>
  );
}

export default MainLayout;