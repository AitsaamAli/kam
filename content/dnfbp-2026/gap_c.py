"""Gap series posts 5-6: W-8BEN for Pakistani freelancers; SIM block under Section 114B."""
from gap_common import *

W8 = dict(
    slug=SL["w8"],
    svc=dict(h2="Freelancer Paperwork Done Properly on Both Sides", intro="The W-8BEN settles your status with a US payer. Your Pakistani tax is a separate matter. We help you fill the form correctly and file the Pakistani return that matches the money you receive.",
             hook="Client or platform asking for a W-8BEN?", fee="Freelancer return Rs 5,000 (published fee); W-8BEN guidance alongside a return at a fixed fee confirmed before work starts.", btn="Help with my W-8BEN and return",
             items=["Line-by-line check of your W-8BEN before you sign it",
                    "Your NTN (CNIC) entered correctly as the foreign tax identifying number",
                    "A clear answer on whether you need a treaty claim at all",
                    "Pakistani return and wealth statement matched to your foreign remittances",
                    "ATL status so your bank profit and transactions are taxed at filer rates"],
             risks=["A wrong form or missing details can lead a US payer to withhold 30%",
                    "Signing a treaty claim you do not qualify for is a false certification under penalties of perjury",
                    "Foreign remittances not shown in your wealth statement invite FBR questions"]),
    title="W-8BEN Form for Pakistani Freelancers: How to Fill It (2026)",
    h1="W-8BEN Form for Pakistani Freelancers: What It Is, Who Needs It, and How to Fill Each Line (2026)",
    crumb="W-8BEN for Freelancers",
    description="A plain guide to Form W-8BEN for freelancers in Pakistan: why US clients ask for it, how to fill each line, your NTN as foreign TIN, the treaty part, and Pakistani tax.",
    keywords="w8ben form pakistan, w-8ben form, what is w-8ben, who needs a w-8ben, w8ben form for freelancers, how to fill w-8ben form, w-8ben foreign tax identifying number pakistan",
    category="Freelancers", icon="🌐", read="12 min read",
    banner="The W-8BEN tells a US payer you are not a US person. It does not file anything with the IRS, and it does not change your Pakistani tax.",
    tldr=("Form W-8BEN (Certificate of Foreign Status of Beneficial Owner for United States Tax Withholding and Reporting) is the IRS form a non-US individual gives "
          "to a US payer or platform to show they are not a US person. It is given to the payer, not filed with the IRS. Without a valid form, the IRS instructions say "
          "a withholding agent may have to treat the payment as made to a US person or apply withholding; the standard rate on US-source fixed or determinable income "
          "of a foreign person is 30%. For a freelancer in Pakistan, the key lines are name, country of citizenship, permanent residence address in Pakistan, and the "
          "foreign tax identifying number, which for an individual is the NTN (the CNIC number). Part II (treaty claim) is only for a reduced rate on US-source income. "
          "A form generally stays valid until the last day of the third calendar year after it is signed, unless your circumstances change. Your Pakistani tax on the "
          "same earnings is settled separately, in your FBR return."),
    lead=("Almost every Pakistani freelancer meets the W-8BEN on the first payout from a US client or platform. It looks like a tax return, so people either panic "
          "or click through it carelessly. Both are mistakes. Here is what the form does, line by line, based on the IRS's own instructions, and how it fits with your "
          "FBR obligations."),
    body=f"""
{SERIES("w8")}

<h2 id="what">What the W-8BEN Is</h2>
<p>The full name is "Certificate of Foreign Status of Beneficial Owner for United States Tax Withholding and Reporting (Individuals)". According to the IRS, a foreign person gives it to the withholding agent or payer when requested, to establish that they are not a US person, to claim that they are the beneficial owner of the income, and, where relevant, to claim a reduced rate of withholding under an income tax treaty.</p>
{table(["Point", "Position (IRS instructions)"], [
    ["Who completes it", "A non-US individual (entities use Form W-8BEN-E)"],
    ["Who receives it", "The payer or withholding agent, not the IRS"],
    ["What it proves", "Foreign status and beneficial ownership; optionally a treaty claim"],
    ["Without it", "The payer may have to presume you are a US person or withhold"],
    ["Standard withholding for foreign persons", "30% on US-source fixed or determinable income, unless reduced"],
    ["How long it lasts", "Generally until the last day of the third calendar year after signing, unless circumstances change"],
])}

<h2 id="who">Who Needs a W-8BEN</h2>
<ul>
<li>A Pakistani freelancer paid by a US client or a US-based platform.</li>
<li>A Pakistani investor holding US shares through a broker, for dividend withholding.</li>
<li>Anyone a US payer asks for proof that they are not a US person.</li>
</ul>
<p>You do <strong>not</strong> use a W-8BEN if you are a US citizen or US resident for tax purposes (that is Form W-9), or if you are paid through a company you own (that company uses the W-8BEN-E).</p>

<h2 id="services">Why Most Freelancers Owe No US Tax</h2>
<p>US withholding on a foreign person applies to US-source income. The IRS treats income from personal services as sourced where the services are performed. Work you do while physically in Pakistan is therefore generally foreign-source income for US purposes, even when the client is in the US. That is why, for most freelancers, the W-8BEN simply confirms foreign status and no US tax is withheld. It is also why most freelancers do not need the treaty section at all.</p>
<p>If you travel to the US and work there, or earn US-source income such as US dividends, the position changes and Part II may matter.</p>

<h2 id="lines">How to Fill Each Line</h2>
{table(["Line", "What to enter", "Note for Pakistan"], [
    ["1. Name", "Your name as on your CNIC or passport", "Same spelling as your bank account"],
    ["2. Country of citizenship", "Pakistan", "Dual nationals: country of citizenship relevant to the form; read the instructions"],
    ["3. Permanent residence address", "Your home address in Pakistan", "Not a P.O. box or in-care-of address"],
    ["4. Mailing address", "Only if different", "Leave blank if the same"],
    ["5. US TIN", "SSN or ITIN, if you have one", "Most freelancers leave this blank"],
    ["6a. Foreign tax identifying number", "Your Pakistani tax number", "For an individual, the NTN is the CNIC number"],
    ["6b. FTIN not legally required", "Tick only if your country does not issue one", "Pakistan issues NTNs, so normally not ticked"],
    ["7. Reference number", "Optional, from the payer", "Leave blank unless asked"],
    ["8. Date of birth", "MM-DD-YYYY", "US date order"],
    ["9-10. Treaty claim (Part II)", "Only for a reduced rate on US-source income", "Usually blank for services performed in Pakistan"],
    ["Part III. Certification", "Sign, date, and print your name", "Signed under penalties of perjury"],
])}

<h2 id="treaty">Part II: The Treaty Claim</h2>
<p>The IRS lists an income tax treaty between the United States and Pakistan on its "United States income tax treaties A to Z" page. Part II is used to claim that treaty's reduced rate or exemption on a specific kind of US-source income, such as dividends. You name the country of residence, and for a special rate you cite the treaty article, the rate and the type of income, with the conditions you meet.</p>
<p>Two cautions. First, if your income is not US-source (services performed in Pakistan), there is nothing to reduce, so a treaty claim adds risk without benefit. Second, the IRS instructions say a US TIN or foreign TIN is generally required for treaty claims, and the certification is signed under penalties of perjury. Do not cite an article you have not read. When in doubt, leave Part II blank and ask.</p>

<h2 id="mistakes">Mistakes We See</h2>
<ul>
<li><strong>Writing "N/A" in line 6a</strong> when you have an NTN. Enter the number.</li>
<li><strong>Putting a business address</strong> in line 3. It must be your permanent residence.</li>
<li><strong>Using W-8BEN for your company.</strong> A private limited company or AOP uses W-8BEN-E.</li>
<li><strong>Claiming a treaty rate on service income</strong> earned in Pakistan, often copied from a template online.</li>
<li><strong>Forgetting to update</strong> after you move abroad or become a US resident. The instructions say that after a change in circumstances that makes the form incorrect, you must tell the payer within 30 days and give a new form.</li>
<li><strong>Date order:</strong> 03-07-1995 means 7 March, not 3 July.</li>
</ul>

<h2 id="pakistan">Your Pakistani Tax Is Separate</h2>
<p>The W-8BEN only deals with US withholding. A resident individual in Pakistan is taxed on worldwide income under the Income Tax Ordinance 2001, so your freelance earnings are reported in your FBR return. How freelance and IT export income is taxed, and what records banks issue for foreign remittances, is covered in our <a href="{X["free"]}">tax return guide for freelancers</a>. Remittances that build up in your accounts should match your <a href="{X["ws"]}">wealth statement</a>.</p>
<p>Staying on the Active Taxpayers List also matters for a freelancer who keeps money in Pakistani banks: bank profit is taxed at 20% instead of 40%, and there is no <a href="{B["cash"]}">cash withdrawal tax</a>.</p>

<h2 id="renew">Validity and Renewal</h2>
<p>A W-8BEN generally remains in effect until the last day of the third calendar year following the year it is signed. A form signed on 15 March 2026 is valid until 31 December 2029, unless a change in circumstances makes any information incorrect. Platforms usually remind you to renew; keep a copy of each signed form.</p>
""",
    faqs=[
        ("What is a W-8BEN form?", "An IRS form a non-US individual gives to a US payer to certify foreign status and beneficial ownership, and optionally to claim treaty benefits. It is not filed with the IRS."),
        ("Who needs a W-8BEN in Pakistan?", "A Pakistani individual paid by a US client, platform or broker who asks for proof of non-US status."),
        ("What is my foreign tax identifying number on the W-8BEN?", "For an individual in Pakistan, the NTN, which is the same as the CNIC number."),
        ("Do I need to fill Part II (treaty claim) as a freelancer?", "Usually not. Services performed in Pakistan are generally not US-source income, so there is no US tax to reduce."),
        ("What happens if I do not submit a W-8BEN?", "The payer may have to presume you are a US person or withhold tax; the standard rate on US-source fixed or determinable income of a foreign person is 30%."),
        ("How long is a W-8BEN valid?", "Generally until the last day of the third calendar year after it is signed, unless a change in circumstances makes it incorrect."),
        ("Is the W-8BEN the same as a W-9?", "No. A W-9 is for US persons; a W-8BEN is for non-US individuals."),
        ("Does submitting a W-8BEN affect my Pakistani tax?", "No. Your Pakistani tax on freelance income is settled in your FBR return."),
    ],
    sources=[S_W8, S_W8A, S_TRE, S_ITO],
    related=[(X["free"], "Tax Return for Freelancers"), (X["ws"], "Wealth Statement Guide"), (B["cash"], "Cash Withdrawal Tax")],
    cta_h="Clean Paperwork for Your Foreign Income",
    cta_p="We help with the W-8BEN and file the Pakistani return that matches your remittances.",
    wa_text="Assalam o Alaikum, W-8BEN form aur freelancer return mein madad chahiye.",
)

SIM = dict(
    slug=SL["sim"],
    svc=dict(h2="Get Off the List and Restore Your SIM", intro="Section 114B targets people liable to file who are not on the ATL. The fix is a filed return, followed by a restoration request. We do both and track it to the end.",
             hook="SIM blocked or a notice under Section 114(4)?", fee=FEE_RET + " Notice reply from Rs 5,000.", btn="Restore my SIM",
             items=["A check of whether you were actually liable to file",
                    "Return and wealth statement filed, with the surcharge or ATL-U route if late",
                    "Reply to the Section 114(4) notice",
                    "Restoration request to your Commissioner under Section 114B(3)",
                    "Follow-up until the SIM, electricity or gas connection is restored"],
             risks=["The order can also cut electricity and gas and restrict foreign travel",
                    "Section 114B action does not stop other penalties (Section 114B(5))",
                    "The late filing penalty keeps running until you file"]),
    title="FBR SIM Block for Non-Filers: Section 114B Explained (2026)",
    h1="FBR SIM Block for Non-Filers in 2026: How Section 114B Works, Who Can Be Listed, and How to Get Your SIM Restored",
    crumb="SIM Block (Section 114B)",
    description="Section 114B lets FBR block SIMs and cut power, gas and travel for people liable to file but not on the ATL. Who can be listed, the conditions, and how to get restored.",
    keywords="fbr sim block, fbr sim block list, sim block due to non filer, fbr block sim how to activate, fbr sim block check online, section 114b income tax ordinance, income tax general order sim block",
    category="FBR Compliance", icon="📵", read="11 min read",
    banner="A SIM can be blocked only after a Section 114(4) notice, a missed deadline and no return. Filing is what reverses it.",
    tldr=("Section 114B of the Income Tax Ordinance 2001 (inserted by the Finance Act 2022, expanded by the Finance Act 2024) lets the Board issue an 'income tax "
          "general order' against persons who are not on the Active Taxpayers List but are liable to file a return. The order may disable mobile phones or SIMs, "
          "discontinue electricity and gas connections, and restrict foreign travel for citizens (excluding NICOP holders, minors, students, Hajj and Umrah travellers "
          "and others the Board notifies). No one can be included unless a notice under Section 114(4) was issued, its compliance date has passed, and the return has "
          "still not been filed. The Board or the Commissioner may order restoration once the return is filed or the person is shown not to have been liable. The "
          "action does not prevent any other action under the Ordinance."),
    lead=("Every few months a 'FBR SIM block list' story goes round, and people ask whether their number is next. The answer is in one section of the law, and it "
          "is narrower than the rumours suggest. Here is what Section 114B allows, the three conditions that must be met first, and the way out."),
    body=f"""
{SERIES("sim")}

<h2 id="law">What Section 114B Says</h2>
<p>Section 114B(1) says that, notwithstanding any other law, the Board has the power to issue an income tax general order in respect of persons who are not appearing on the Active Taxpayers List but are liable to file a return under the Ordinance.</p>
<p>Section 114B(2) lists the consequences the order may entail, any or all of them:</p>
{table(["Clause", "Consequence"], [
    ["(a)", "Disabling of mobile phones or mobile phone SIMs"],
    ["(b)", "Discontinuance of electricity connection"],
    ["(c)", "Discontinuance of gas connection"],
    ["(d)", "Restriction on foreign travel for a citizen of Pakistan (added by the Finance Act 2024)"],
])}
<p>The travel restriction excludes persons holding a NICOP, minors, students, persons going abroad for Hajj or Umrah, and other classes the Board notifies.</p>

<h2 id="conditions">Three Conditions Before Anyone Is Listed</h2>
<p>Section 114B(4) says no person shall be included in the general order unless all three conditions are met:</p>
<ol>
<li>A notice under Section 114(4) has been issued, requiring the person to file a return.</li>
<li>The compliance date in that notice has passed.</li>
<li>The person has not filed the return.</li>
</ol>
<p>So the order is not a surprise for someone who is watching their IRIS inbox and the address on their record. The notice comes first. If you have received a Section 114(4) notice, that is the moment to act, not after the SIM stops working.</p>

<h2 id="who">Who Is Liable to File, and So at Risk</h2>
<p>Section 114B reaches only people who are <em>liable</em> to file. Under Section 114(1), that includes every company, every other person whose taxable income exceeds the amount not chargeable to tax, and any person who: was charged to tax in either of the two preceding tax years; owns immovable property of 500 square yards or more, or a flat in the areas the section lists; owns a motor vehicle above 1000 cc; or has obtained an NTN. Under Section 115(3), a widow and an orphan below twenty-five, among others, are not required to file solely because they own such property or a vehicle.</p>
<p>If you were never liable, the restoration ground in Section 114B(3)(b) applies; you still need to show it.</p>

<h2 id="check">How to Know If You Are Exposed</h2>
<ol>
<li><strong>Check your ATL status.</strong> If you appear on the list, the general order cannot cover you. Use the <a href="{X["chk"]}">online or SMS ATL check</a>.</li>
<li><strong>Check your IRIS inbox and post</strong> for a notice under Section 114(4).</li>
<li><strong>Look at your filing history.</strong> If your last return is missing and you have income or assets above the thresholds, file now.</li>
</ol>
<p>We have not found an official FBR online tool that lists blocked SIMs by number, so we do not recommend third-party "SIM block check" sites asking for your CNIC.</p>

<h2 id="restore">How to Get a SIM, Electricity or Gas Restored</h2>
<p>Section 114B(3) lets the Board or the Commissioner who has jurisdiction over you order restoration of mobile phones, SIMs and electricity and gas connections where satisfied that:</p>
<ul>
<li>(a) the return has been filed; or</li>
<li>(b) the person was not liable to file a return under the Ordinance.</li>
</ul>
<p>In practice:</p>
<ol>
<li>File the return and wealth statement for the year in the notice.</li>
<li>If it is late, the surcharge under Section 182A or <a href="{X["atlu"]}">Form ATL-U</a> gets you onto the ATL; the <a href="{X["atlroute"]}">ATL route calculator</a> compares them.</li>
<li>Submit a restoration request to your Commissioner with the acknowledgement of the filed return.</li>
<li>Follow up until the order is withdrawn for your CNIC.</li>
</ol>

<h2 id="penalties">What Else Still Applies</h2>
<p>Section 114B(5) says the action does not preclude any other action under the Ordinance. Filing late still attracts the Section 182 late filing penalty (estimate it with our <a href="{X["pen"]}">late filing penalty calculator</a>), and the Commissioner may still make a best judgement assessment under Section 121 if the notice is ignored.</p>

<h2 id="mistakes">Common Misunderstandings</h2>
<ul>
<li><strong>"All non-filers will be blocked."</strong> Only persons liable to file, after a Section 114(4) notice and a missed deadline.</li>
<li><strong>"Paying a fine unblocks the SIM."</strong> The law ties restoration to a filed return or proof of non-liability.</li>
<li><strong>"Overseas Pakistanis cannot travel."</strong> NICOP holders are excluded from the travel restriction.</li>
<li><strong>"Joining the ATL is enough without the return."</strong> You join the ATL by filing; there is no shortcut.</li>
</ul>
""",
    faqs=[
        ("Can FBR block my SIM for not filing a return?", "Yes, under Section 114B, if you are liable to file, received a Section 114(4) notice, missed its deadline and still have not filed."),
        ("What else can a Section 114B order do?", "Cut electricity and gas connections and, from the Finance Act 2024, restrict foreign travel for citizens (with exclusions such as NICOP holders, minors, students and Hajj or Umrah travellers)."),
        ("How do I get my blocked SIM activated?", "File the return, then ask the Commissioner to order restoration under Section 114B(3); restoration also applies if you show you were not liable to file."),
        ("Is there an official FBR SIM block check online?", "We have not found one. Check your ATL status and your IRIS inbox for a Section 114(4) notice instead."),
        ("Can I be listed without a notice?", "No. Section 114B(4) requires a Section 114(4) notice, its compliance date to have passed, and no return filed."),
        ("Does Section 114B apply to people on the ATL?", "No. It covers persons not appearing on the Active Taxpayers List."),
        ("Does restoration cancel the late filing penalty?", "No. Section 114B(5) says the action does not preclude any other action under the Ordinance."),
        ("Are overseas Pakistanis covered by the travel ban?", "Persons holding a NICOP are excluded from the travel restriction in Section 114B(2)(d)."),
    ],
    sources=[S_ITO, S_ATL, S_IRIS],
    related=[(X["chk"], "Check Your ATL Status"), (X["atlu"], "Form ATL-U Guide"), (X["notice"], "FBR Notice Defence")],
    cta_h="SIM Blocked? File and Restore",
    cta_p="We file the return, reply to the notice and request restoration from your Commissioner.",
    wa_text="Assalam o Alaikum, FBR ne SIM block ki hai / 114(4) notice aya hai. Madad chahiye.",
)
