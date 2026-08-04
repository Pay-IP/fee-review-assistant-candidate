import FeeExplanation from "./components/FeeExplanation.jsx";
import FeeFilters from "./components/FeeFilters.jsx";
import FeeTable from "./components/FeeTable.jsx";


export default function App() {
  // TODO(candidate): add fee, filter, threshold, selection, loading, and error state.
  return (
    <main className="app-shell">
      <header>
        <p className="eyebrow">Engineering interview</p>
        <h1>Fee Review Assistant</h1>
        <p className="intro">
          Review fictional card-network fees and identify records that may need investigation.
        </p>
      </header>

      <p className="starter-message" role="status">
        Starter application ready. Implement the fee-review workflow described in the candidate instructions.
      </p>

      <FeeFilters />
      <FeeTable />
      <FeeExplanation />
    </main>
  );
}

