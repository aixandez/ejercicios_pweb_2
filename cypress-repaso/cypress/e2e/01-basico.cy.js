// Test mínimo que solo verifica que true es igual a true.
// Sirve para confirmar que Cypress está funcionando correctamente.

describe('Mi primer test', () => {
  it('No hace mucho', () => {
    expect(true).to.equal(true)
  })
})