import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import App from "../src/App.jsx";


describe("App", () => {
  it("renders the starter heading and implementation message", () => {
    render(<App />);

    expect(screen.getByRole("heading", { name: "Fee Review Assistant" })).toBeInTheDocument();
    expect(screen.getByRole("status")).toHaveTextContent("Starter application ready");
  });
});

