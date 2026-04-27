export default function getBudgetObject(inc, Gross_domestic_product, capital) {
  const budget = {
    income: inc,
    gdp: Gross_domestic_product,
    capita: capital,
  };

  return budget;
}
