# Tiny Spam Detector

keywords = [
    # Frequent
    "click", "download", "otp", "loan", "verify",
    "free", "offer", "win", "prize", "money",
    "urgent", "limited", "credit", "account", "password",

    # Marketing / urgency words
    "100% more", "100% free", "100% satisfied", "additional income", "be your own boss",
    "best price", "big bucks", "billion", "cash bonus", "cents on the dollar",
    "consolidate debt", "double your cash", "double your income", "earn extra cash",
    "earn money", "eliminate bad credit", "extra cash", "extra income", "expect to earn",
    "fast cash", "financial freedom", "free access", "free consultation", "free gift",
    "free hosting", "free info", "free investment", "free membership", "free money",
    "free preview", "free quote", "free trial", "full refund", "get out of debt",
    "get paid", "giveaway", "guaranteed", "increase sales", "increase traffic",
    "incredible deal", "lower rates", "lowest price", "make money", "million dollars",
    "miracle", "money back", "once in a lifetime", "one time", "pennies a day",
    "potential earnings", "promise", "pure profit", "risk-free", "satisfaction guaranteed",
    "save big money", "save up to", "special promotion",

    # Urgency phrases
    "act now", "apply now", "become a member", "call now", "click below", "click here",
    "get it now", "do it today", "don’t delete", "exclusive deal", "get started now",
    "important information regarding", "information you requested", "instant",
    "limited time", "new customers only", "order now", "please read", "see for yourself",
    "sign up free", "take action", "this won’t last", "urgent", "what are you waiting for?",
    "while supplies last", "will not believe your eyes", "winner", "winning",
    "you are a winner", "you have been selected",

    # Shady / scammy behavior
    "bulk email", "buy direct", "cancel at any time", "check or money order",
    "congratulations", "confidentiality", "cures", "dear friend", "direct email",
    "direct marketing", "hidden charges", "human growth hormone", "internet marketing",
    "lose weight", "mass email", "meet singles", "multi-level marketing", "no catch",
    "no cost", "no credit check", "no fees", "no gimmick", "no hidden costs",
    "no hidden fees", "no interest", "no investment", "no obligation",
    "no purchase necessary", "no questions asked", "no strings attached",
    "not junk", "notspam", "obligation", "passwords", "requires initial investment",
    "social security number", "this isn’t a scam", "this isn’t junk", "this isn’t spam",
    "undisclosed", "unsecured credit", "unsecured debt", "unsolicited", "valium",
    "viagra", "vicodin", "we hate spam", "weight loss", "xanax",

    # Legal / marketing jargon
    "accept credit cards", "ad", "all new", "as seen on", "bargain", "beneficiary",
    "billing", "bonus", "cards accepted", "cash", "certified", "cheap", "claims",
    "clearance", "compare rates", "credit card offers", "deal", "debt", "discount",
    "fantastic", "in accordance with laws", "income", "investment", "join millions",
    "lifetime", "loans", "luxury", "marketing solution", "message contains",
    "mortgage rates", "name brand", "offer", "online marketing", "opt in", "pre-approved",
    "quote", "rates", "refinance", "removal", "reserves the right", "score",
    "search engine", "sent in compliance", "subject to", "terms and conditions",
    "trial", "unlimited", "warranty", "web traffic", "work from home"
]

while(True):
  ch = int(input("Enter choice:\n1-Text\n2-Exit\n"))
  if ch == 2:
    break
  text = input("Enter text: ")
  spam = 0
  found = []
  for keyword in keywords:
    if keyword in text.lower():
      spam += 1
      found.append(keyword)
  words = text.split()
  if(spam / len(words) > 0.1):
    print("Spam Detected.")
    print("Why? ", ", ".join(found))
    print()
  else:
    print("Not Spammy.")
    print()