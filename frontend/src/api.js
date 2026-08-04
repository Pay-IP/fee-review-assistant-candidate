const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";


async function request(path) {
  const response = await fetch(`${API_BASE_URL}${path}`);
  if (!response.ok) {
    throw new Error(`API request failed with status ${response.status}`);
  }
  return response.json();
}


export async function fetchFees(filters = {}) {
  // TODO(candidate): encode supported filters and call request("/fees?..." ).
  void filters;
  throw new Error("Fee loading has not been implemented");
}


export async function fetchFeeExplanation(feeId, threshold) {
  // TODO(candidate): request the deterministic explanation for the selected fee.
  void feeId;
  void threshold;
  throw new Error("Explanation loading has not been implemented");
}

export { request };

