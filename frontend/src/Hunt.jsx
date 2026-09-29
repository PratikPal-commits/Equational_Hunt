import { useState } from "react"; 
import Plot from "react-plotly.js";
import "mathlive";
function normalizeEquation(value) {
  const superscripts = {
    "⁰": "0",
    "¹": "1",
    "²": "2",
    "³": "3",
    "⁴": "4",
    "⁵": "5",
    "⁶": "6",
    "⁷": "7",
    "⁸": "8",
    "⁹": "9",
  }

  return value.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹]/g, char => {
    return `^${superscripts[char]}`
  })
}
function Hunt(){
  const[equation, setEquation] = useState("")
  const[result, setResult] = useState(null)
  const[graphData, setGraphData] = useState(null)

  async function analyzeEquations() {
    const response =  await fetch(
      `http://127.0.0.1:8000/analyze?equation=${encodeURIComponent(equation)}`
    )
    const data = await response.json()
    setResult(data)

    
  }
  async function graphAnalysis(){
    const response = await fetch(
      `http://127.0.0.1:8000/graph?equation=${encodeURIComponent(equation)}`
    )
    const graph = await response.json()
    setGraphData(graph)
  }
  async function handleAnalyze(){
    await analyzeEquations()
    await graphAnalysis()
  }

  return(
    <div className="app">
      <header className="header">
        <h1>Equational Hunt</h1>
      </header>
      <main className="workspace">

  
  <section className="equation-section">

    <math-field
      onInput={(event) => {
        const latex = event.target.getValue("latex")
        setEquation(normalizeEquation(latex))
      }}
      onKeyDown={(event) => {
        if (event.key === "Enter") {
          handleAnalyze()
        }
      }}
    ></math-field>

    <button onClick={handleAnalyze}>
      Analyze an Equation
    </button>

  </section>


  {graphData && (
    <section className="graph-section">

      <div style={{ width: "100%", maxWidth: "800px" }}>
        <h2>Graph</h2>

        <Plot
          data={[
            {
              x: graphData.x,
              y: graphData.y,
              type: "scatter",
              mode: "lines",
            }
          ]}
          layout={{
            autosize: true,
            title: {
              text: "Graph of the Equation"
            },
            xaxis: {
              title: {
                text: "x-axis"
              }
            },
            yaxis: {
              title: {
                text: "y-axis"
              }
            }
          }}
          config={{
            responsive: true,
            scrollZoom: true
          }}
        />

      </div>

    </section>
  )}


  
  {result && (
    <section className="analysis-section">

      <h3>Results</h3>

      <p>
        Equation: {result.equation}
      </p>

      <p>
        Roots: {result.roots.join(", ")}
      </p>

      <p>
        Derivative: {result.derivative}
      </p>

    </section>
  )}

</main>
    </div>
  )

}

export default Hunt