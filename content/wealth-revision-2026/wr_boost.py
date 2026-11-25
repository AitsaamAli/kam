"""Second pass (owner, 24 Nov 2026: boost SEO/AEO/GEO): one extra section and two FAQs per guide, aimed at real Google
suggestions (gl=pk) such as "how many months bank statement for canada visa", "schengen visa bank statement requirement pakistan",
"uk visa bank statement translation", "gift from father is exempt under which section", "loan from friend taxable",
"cash in hand limit as per income tax", "revised wealth statement fbr", "wealth reconciliation statement fbr".
Facts: the same official texts as wr_common.py, checked 24 November 2026. No amount, month count or stamp rule that those texts
do not state is given."""
from wr_common import *

BOOST = {
"visa": (f"""
<h2 id="uk-questions">UK Applicants: Months, Translations and Old Statements</h2>
<p>Pakistani applicants searching for UK visa bank statement rules usually ask three things. On the period, the GOV.UK supporting documents guide does not set a number of months; it asks for financial documents that clearly show access to the funds and “detail the origin of the funds held”. On age, the same guide lists “bank statements or letters issued more than 1 year before the date of application” among documents not to use. On language, a document not in English or Welsh “must be accompanied by a full translation that can be independently verified by the Home Office”, with the translator's confirmation of accuracy, the date, the translator's full name, signature and contact details. FBR's IRIS acknowledgements and wealth statements are produced in English, so they normally need no translation; an Urdu sale deed or gift deed does.</p>
<p>The wealth statement's job in that file is the “origin” part. A one-page summary of the corrected figures, with the IRIS acknowledgement, lets the officer trace a balance back to a recorded source in a minute.</p>
""", [
    ("How many months of bank statements does the UK want?",
     "The GOV.UK supporting documents guide does not set a number of months. It asks for statements that show access to the funds and their origin, and says not to use statements issued more than a year before the application."),
    ("Do FBR documents need translation for a UK visa?",
     "Documents not in English or Welsh need a full, verifiable translation. IRIS acknowledgements and wealth statements are in English; Urdu deeds need translating."),
]),
"schengen": (f"""
<h2 id="amount">How Much Balance, and for How Many Months?</h2>
<p>“How much bank statement for Schengen visa from Pakistan” is one of the most searched visa questions in the country, and the honest answer is that the EU rules do not give one figure. Article 6(4) of the Schengen Borders Code makes the amount depend on the length and purpose of the stay and on average budget board and lodging prices in the state you visit, multiplied by the days, and each Member State notifies its own reference amount. Neither Article 14 of the Visa Code nor Article 6 of the Borders Code fixes how many months of statements to submit; that comes from the checklist of the consulate or visa centre you apply through. Use that checklist for the format and period, and use the wealth statement to show that the money in those months is lawfully yours.</p>
""", [
    ("How much bank balance is required for a Schengen visa from Pakistan?",
     "There is no single EU figure. Under Borders Code Article 6(4) it depends on the length and purpose of the stay and the reference amount the Member State you visit has notified."),
    ("How many months of bank statements for a Schengen visa?",
     "The Visa Code and Borders Code articles we checked do not fix a number of months. Follow the checklist of the consulate or visa centre handling your application."),
]),
"canada": (f"""
<h2 id="how-much">How Much Money Does Canada Expect?</h2>
<p>Pakistani searches for a Canada visit visa often ask how much bank statement is needed. IRCC's eligibility page does not give a figure. It says you must “have enough money for your stay” and that “the amount of money you will need depends on how long you will stay and if you will stay in a hotel, or with friends or relatives”. So a two-week stay with a son in Toronto needs less than a month in hotels. What IRCC does fix is the evidence: at least six months of account details including balances, proof the account is yours, and an employer letter dated within three months. The wealth statement then has one task, to make the source of any large balance in those six months a matter of record.</p>
""", [
    ("How much bank balance is needed for a Canada visit visa from Pakistan?",
     "IRCC gives no fixed figure. Its eligibility page says the amount depends on how long you stay and whether you stay in a hotel or with friends or relatives."),
    ("Is a six-month bank statement compulsory for Canada?",
     "IRCC's visitor visa page asks for at least six months of account details, including balances, as part of the bank account statement it lists."),
]),
"sponsor": (f"""
<h2 id="sponsor-checklist">Sponsor's Own Checklist Before the Student Applies</h2>
<ul>
<li><strong>Income:</strong> the sponsor's return shows the income that is meant to pay the fees, for the years the officer will look at.</li>
<li><strong>Accounts:</strong> every account holding the promised funds is in the sponsor's wealth statement at its 30 June balance.</li>
<li><strong>Sources:</strong> any large addition, a property sale, a business withdrawal, a gift from the sponsor's own parent, is recorded in the reconciliation of that year.</li>
<li><strong>Payments:</strong> tuition and deposits already paid appear in total expenditure under section 116(1)(d).</li>
<li><strong>Transfers:</strong> money moved to an adult child is shown as an asset transferred under section 116(1)(c), and the child shows it as a gift from a relative.</li>
<li><strong>Dependents:</strong> a dependent spouse's and minor children's assets are included under section 116(1)(b).</li>
</ul>
<p>Each item either agrees with the sponsor's bank papers or calls for a revision under section 116(3) before the student's application goes in.</p>
""", [
    ("Can my uncle sponsor my studies and use his wealth statement?",
     "Any sponsor's papers must show the funds and their source. An uncle is a relative under section 85(5), so his gift to you is not your income under section 39(1)(la); his own statement should show it leaving."),
    ("Does the sponsor need to be on the Active Taxpayers List?",
     "The official visa pages we checked do not say so. What matters there is that the sponsor's income and assets are documented; FBR rules on the ATL apply separately."),
]),
"refused": (f"""
<h2 id="source-of-wealth">What a “Source of Wealth” Explanation Looks Like</h2>
<p>Many refusals and follow-up requests come down to one phrase: the source of the funds. In Pakistan the documented answer is built from four records, and a revision should leave all four agreeing:</p>
{table(["Record", "What it proves", "Where it comes from"], [
    ["Return of income", "What you earned and paid tax on, year by year", "IRIS, section 114"],
    ["Wealth statement", "What you and your dependents owned on 30 June", "IRIS, section 116(1)-(2)"],
    ["Wealth reconciliation", "How net assets moved: income, gifts, sales, expenses", "Section 116(1)(e)"],
    ["Bank and property papers", "That the figures in the three FBR records are real", "Your bank, the registry, the society"],
])}
<p>An explanation that cites all four, for example “Rs 1,800,000 received from my mother by bank transfer on 12 May 2026, recorded as a gift in my TY2026 reconciliation, IRIS acknowledgement attached”, is far stronger than a letter that only asserts the money is yours. The UK guide's wording, bank statements that “detail the origin of the funds held”, describes exactly this.</p>
""", [
    ("What is a source of funds letter for a visa?",
     "A short note explaining where a balance came from. From Pakistan it is strongest when it cites the bank record and the FBR record of the same money: the return, the wealth statement and its reconciliation."),
    ("Can I reapply immediately after revising my wealth statement?",
     "The FBR revision takes effect when filed. When you reapply is a visa question; check the embassy's guidance. Attach the revised acknowledgement and an explanation of the change."),
]),
"cash": (f"""
<h2 id="limit">Is There a Limit on Cash in Hand?</h2>
<p>“Cash in hand limit as per income tax” is a common search, and much of what comes up is from other countries. In Pakistan, sections 111 and 116 of the Income Tax Ordinance, the provisions on unexplained assets and on the wealth statement, set no rupee ceiling on the cash an individual may hold. They do something more practical: section 116 requires the cash to be declared, and section 111 asks whether its nature and source are explained. Rs 200,000 of cash from salary withdrawn last week needs no explanation beyond the bank record. Rs 3,000,000 at home, growing every year while bank balances stay flat, needs one that most filers cannot give.</p>
<p>Withdrawals themselves are a separate matter: tax on cash withdrawals by persons off the Active Taxpayers List is covered in our {a("/blogs/cash-withdrawal-tax-non-filer-pakistan-2026", "cash withdrawal guide")}.</p>
""", [
    ("Is there a legal limit on cash in hand for individuals in Pakistan?",
     "Sections 111 and 116 of the Income Tax Ordinance set no rupee limit. Cash must be declared in the wealth statement, and money whose source is not adequately explained can be taxed under section 111."),
    ("Should business cash be shown as personal cash in hand?",
     "No. Cash belonging to a sole proprietor's business sits within business capital; only genuinely personal cash goes on the personal line."),
]),
"gift": (f"""
<h2 id="wedding">Wedding Gifts, Salami and Jahez</h2>
<p>Searches for a “gift from father to daughter on wedding day” show how often this comes up. The rule is the same as for any gift: under section 39(1)(la), property or money received as a gift is not income if it comes from a relative as defined in section 85(5). A father, mother, brother, grandparent, uncle or cousin is a relative; so are the same people on the spouse's side once married. Gold, cash or a car given by the bride's family is therefore not the bride's income, but it is her asset, and it belongs in the wealth statement of whoever owns it at 30 June. Cash gifts from many guests are the harder case: guests who are not relatives fall outside the exclusion, and section 39(3) is strict about gifts not received through a bank. Recording large wedding gifts promptly, and depositing cash ones, keeps the next year's statement simple. Our guide to {a("/blogs/getting-married-wealth-statement-merge-separate-pakistan", "wealth statements after marriage")} covers whose statement the assets go in.</p>
""", [
    ("Gift from father is exempt under which section?",
     "Section 39(1)(la) of the Income Tax Ordinance excludes gifts from a relative as defined in section 85(5), which includes a father, from income from other sources."),
    ("Is a loan from a friend taxable in Pakistan?",
     "Not if it is a genuine loan received through a bank or digital channel from a person holding an NTN and recorded as a liability. Otherwise section 39(3) treats it as income from other sources."),
]),
"prop": (f"""
<h2 id="files">Plot Files, Instalments and Possession</h2>
<p>Many Pakistani property holdings are not finished plots but files in a housing scheme or society, paid in instalments over years. In the wealth statement the asset is what you have paid so far, not the full price you will pay: a file costing Rs 9,600,000 over four years with Rs 4,800,000 paid by 30 June is shown at Rs 4,800,000, rising each year as instalments are paid. Instalments are paid from income, so they also show in the reconciliation as an investment rather than an expense. When possession is handed over, the file becomes a plot or house at its full cost. The two errors to avoid are showing the full price from the first instalment, which overstates assets, and leaving a file out because it is “not a property yet”, which leaves the instalments unexplained.</p>
""", [
    ("How should a plot file on instalments be shown in the wealth statement?",
     "At the amount actually paid by 30 June, increasing each year as instalments are paid, until possession, when it becomes the full cost of the property."),
    ("My property's FBR value is higher than my price. Which is used for 236K?",
     "Section 236K is charged on fair market value, so the FBR value applies to the buyer's advance tax. Your wealth statement still shows what you actually paid."),
]),
"foreign": (f"""
<h2 id="conversion">Converting Foreign Assets to Rupees</h2>
<p>A wealth statement is in rupees, so every foreign asset needs a conversion, and the choice of rate is where many statements become inconsistent year to year. Two principles keep it defensible. First, record an asset bought abroad at its cost converted on the date you paid for it, and keep that figure; do not revalue it every year with the exchange rate, or the reconciliation will show “gains” and “losses” that are only currency movements. Second, for cash and bank balances abroad, use a consistent, documented rate for 30 June and note the source of the rate. Section 116A(1)(a) itself asks for foreign assets and liabilities “as on the last day of the tax year”, which is the date your balances should reflect. Whatever method you use, use it every year and say so in the reasons note when you revise.</p>
<p>The section 116A thresholds are in US dollars, USD 10,000 of foreign income or USD 100,000 of foreign assets, so the same care with conversion decides whether that separate statement is due at all.</p>
""", [
    ("Which exchange rate should I use for foreign assets in my wealth statement?",
     "Use cost converted at the date of purchase for assets bought abroad, and a consistent documented rate at 30 June for foreign balances. Apply the same method every year."),
    ("Do I have to declare a foreign account with a small balance?",
     "Yes, in the wealth statement of a resident, whatever the balance. The separate section 116A statement depends on the USD 10,000 income or USD 100,000 asset thresholds."),
]),
"bank": (f"""
<h2 id="certificate">How to Get the Right Balance: The Bank Certificate</h2>
<p>The figure that settles a bank balance is the bank's own certificate of balance for 30 June. Ask your bank for one that states the account title, number and the balance as on 30 June of the year you are revising. For a term deposit or savings certificate account, ask for the principal and any profit accrued and credited up to that date. Keep the certificates with the revision: they are the documents that make the correction bona fide under the proviso to section 116(3), and they answer any later question from FBR in one page.</p>
<p>The same certificates help with withholding tax. The bank's annual withholding tax certificate shows tax deducted on profit, which you claim in the return; if an account was missing from the statement, its profit and tax were probably missing from the return too.</p>
""", [
    ("How do I get my bank balance as on 30 June?",
     "Ask your bank for a certificate of balance as on 30 June of that year, stating the account title and number."),
    ("Do I need to revise my return if I add a missing bank account?",
     "If the account earned profit that the return left out, yes: the profit and the tax deducted on it belong in the return, revised under section 114(6) and its conditions."),
]),
}
