"""Top-up for directorate pages."""
EXTRA = {
"dnfbp-registration-karachi-sindh": ("""
<h2 id="jewellers-khi">Karachi Jewellers and Bullion Traders</h2>
<p>Karachi's gold trade includes both retail jewellers and bullion traders dealing in larger quantities. Both are dealers in precious metals and stones under FBR's definition once they engage in a cash transaction of Rs 2 million or more with a customer. For bullion traders, single cash trades above the threshold are routine, so a CTR process must work every day, not occasionally: identify the counterparty, record the trade in the cash register, file the CTR on goAML and note its reference. Retail jewellers should pay special attention during the wedding season, when cash bridal purchases most often cross the line.</p>
""", [
    ("Do Karachi bullion traders need DNFBP registration?",
     "Yes, once they engage in a cash transaction of Rs 2 million or more with a customer, which for bullion traders is common."),
    ("Can a Karachi business choose to deal with the Lahore or Islamabad directorate instead?",
     "No. Supervision follows the jurisdiction table in S.R.O. 1497(I)/2026, based on your tax office and where you carry on business."),
]),
"dnfbp-registration-islamabad-rawalpindi": ("""
<h2 id="rawalpindi-markets">Rawalpindi's Jewellers and Property Dealers</h2>
<p>Rawalpindi's jewellery markets and property offices fall under Additional Director-II (DNFBPs), Islamabad, through RTO Rawalpindi. A jeweller here follows the same Rs 2 million cash rule as anywhere else, and property dealers working in Rawalpindi's housing schemes identify both buyer and seller in every deal. Because many customers move between the twin cities, a business should keep its CDD file with the customer's actual address, not only the city where the sale took place.</p>
""", [
    ("Do Rawalpindi jewellers report to the Islamabad DNFBP directorate?",
     "Yes. Businesses within RTO Rawalpindi's territory are supervised by Additional Director-II (DNFBPs), Islamabad."),
    ("Which directorate covers an Islamabad business owned by a Lahore resident?",
     "Supervision follows the tax office and place of business first; residence is used only for DNFBPs not otherwise covered."),
]),
"dnfbp-registration-peshawar-kp": ("""
<h2 id="peshawar-gold">Peshawar's Gold Market</h2>
<p>Gold traders in Peshawar deal with retail customers, wholesale buyers and people selling old gold. Each cash transaction of Rs 2 million or more with a customer makes the business a DNFBP and needs a CTR. Keep a customer file even for regular trade buyers: a familiar face is not due diligence, and FMU's red flags include payments from third parties and deliveries to people who are neither buyer nor payer.</p>
""", [
    ("Do regular trade buyers need CDD each time?",
     "Keep a full customer file and update it when anything changes; check each large cash transaction against the threshold and red flags."),
    ("Does the KP directorate inspect businesses outside Peshawar?",
     "Its jurisdiction covers all DNFBPs within the territorial limits of RTO Peshawar and RTO Abbottabad, wherever they are located in those areas."),
]),
"dnfbp-registration-quetta-balochistan": ("""
<h2 id="quetta-property">Property Dealing in Quetta</h2>
<p>Property dealers in Quetta identify both buyer and seller, record how each payment is made, and file a CTR for cash of Rs 2 million or more. Where land is sold by several family members, each seller is a customer. Where a buyer pays through someone else, identify the payer and record why. These steps take minutes per deal and are what an inspector from the Quetta directorate will look for first.</p>
""", [
    ("What will the Quetta directorate look for in a property dealer's files?",
     "Typically CDD for both buyer and seller, payment records, CTRs for cash of Rs 2 million or more, and screening records."),
    ("Is there a separate FBR form for Balochistan businesses?",
     "No. DNFBP registration uses the same online IRIS process nationwide; only the supervising directorate differs."),
    ("Who is the compliance officer in a Quetta family business with no employees?",
     "If it is a sole proprietorship without employees, the owner is deemed the compliance officer under FBR Condition No. 3 (2022)."),
]),
}
