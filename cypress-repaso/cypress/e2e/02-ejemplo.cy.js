// Entra a la página de ejemplos de Cypress, hace click en un link,
// escribe un email en un campo y verifica que se escribió bien.

describe('Mi primer test', () => {
  it('Gets, types and asserts', () => {
    // Entra a la página
    cy.visit('https://example.cypress.io')
    // Encuentra el elemento con texto "type" y hace click
    cy.contains('type').click()
    // Verifica que la URL cambió correctamente
    cy.url().should('include', '/commands/actions')
    // Escribe en el campo de email
    cy.get('.action-email').type('fake@email.com')
    // Verifica que el campo tiene el valor escrito
    cy.get('.action-email').should('have.value', 'fake@email.com')
  })
})