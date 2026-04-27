export default function getBudgetObject(inc, prod, cap) {
  const budget = {
    income: inc,
    gdp: prod,
    capita: cap,
  };

  return budget;
}
