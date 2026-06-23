// Muestra cómo usar hooks. El beforeEach visita la página y hace click
// antes de cada test para no repetir ese código en cada uno.

before(() => {
  console.log('Previo a la ejecución de todo el test suite')
})

beforeEach(() => {
  // Esto corre antes de CADA test
  cy.visit('https://example.cypress.io')
  cy.contains('type').click()
})

describe('TS', () => {
  it('TST01 - Verifica la URL', () => {
    cy.url().should('include', '/commands/actions')
  })

  it('TST02 - Escribe un email', () => {
    cy.get('.action-email').type('pepe@email.com')
    cy.get('.action-email').should('have.value', 'pepe@email.com')
  })
})