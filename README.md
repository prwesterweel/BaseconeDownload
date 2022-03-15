# BaseconeDownload
A tool to download Basecone invoices in batch
Deze tool download tot 500 invoices, daarboven moet je even wat aanpassen.

Log in op secure.basecone.com en haal de volgende Cookies uit je browser;

cookies = {
    'SelectedTenant': 'VALUE',
    'LoggedInUserId': 'VALUE',
    'CurrentCulture': 'nl-NL',
    'SelectedCompanyId': 'VALUE',
    'WebPortalSessionId': 'VALUE',
    '.ASPXAUTH': 'VALUE',
    'intercom-session-jc1nhv3o': 'VALUE',
    '.AspNet.Cookies': 'VALUE',
    'SessionExpiryTime': 'VALUE',
}

Voer die in in het cookies oject in het python document.

maak een pdf folder aan,

klaar. Je hebt zojuist €50 bespaard.