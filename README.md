# Tender Compass

Tender Compass is a reusable, source-bound procurement evaluation contract. A buyer freezes a brief, numbered mandatory clauses, and ordered scoring criteria before bids arrive. Each bidder supplies a public HTTPS proposal; the contract fetches that proposal itself and freezes a neutral factual snapshot before validators see it.

The first gate is responsiveness, not taste. Validators must agree on the exact missing mandatory clauses and the entire criterion-score vector, as well as one of `RESPONSIVE`, `RESPONSIVE_WITH_GAPS`, `NON_RESPONSIVE`, or `UNVERIFIABLE`. A deterministic backstop prevents a proposal with mandatory gaps from being recorded as fully responsive.

The contract does not select a winner, transfer funds, or pretend that procurement is purely automatic. It supplies a transparent comparison primitive that marketplaces, grant programs, DAOs, and public buyers can compose into their own governed process.

Lifecycle: `open_tender` → `evaluate_bid` (repeatable per bid) → `close_tender`. Structured views expose the frozen rubric, fetched proposal record, clause-level gaps, ordered scores, and rationale.

## StudioNet deployment

`0x5356195f0E4E5320CbBfa7251e4B83b7de288682`  
Deployment transaction: `0xa525d34ba0e764d2d66ed39583325bea14b089e3c6b3143a398579c87f022c0d`
