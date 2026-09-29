import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Hunt from './Hunt.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Hunt />
  </StrictMode>,
)