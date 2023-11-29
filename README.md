```mermaid
flowchart TD
    EnterMasterPW[Enter Password] --> PWValidation{Password correct?}
    PWValidation -->|False| EnterMasterPW
    PWValidation -->|True| MainMenu[Main menu]
    MainMenu -->UserInput{User Input}
    UserInput -->|1| CreatePWManagerEntry[New Password Entry]
    UserInput -->|2| ViewPasswordEntries[View Password Entries]
    UserInput -->|3| Exit[Exit]
    ViewPasswordEntries --> UserInput
    CreatePWManagerEntry --> PWEntry{Website, Name?}
    PWEntry --> PWEntryPasswordType{Select Password Type}
    PWEntryPasswordType -->|1| OnlyLetters[Only Letters]
    PWEntryPasswordType -->|2| LettersNumbers[Letters and Numbers]
    PWEntryPasswordType -->|3| LettersNumbersSpecial[Letters, Numbers, Special Characters]
    OnlyLetters --> PWEntryPasswordLength
    LettersNumbers --> PWEntryPasswordLength
    LettersNumbersSpecial --> PWEntryPasswordLength{Password Length?}
    PWEntryPasswordLength --> CreatePasswordEntry[Create Password Entry]
    CreatePasswordEntry --> UserInput

```

created with https://mermaid.live/edit#pako:eNqVVM9PgzAU_ldeemYH9baDO0xNTGSSbEoi7PCE59YILSklc2H7322hbKCokUPzfnzf18fra2uWyJTYlL1lcpdsUWlY3cQCzHcrNCkfS7MGYdR4EGBZ7qRK1zCZXEMQPmPGU9RcirpLQSKVokTPjq1MH2RZhzvMSjoM5X-ArlRlkD5y4ZOoImtAbqx1i-8SFvtUkroXRaVra0FjugpOqUbz4gBzRagpCH0UuCFlKlH7qA2e_hDIRtdjCpcHeOa065CWzqmMbGxIN9FRgSvz9x9cR3ZxgBHBpsUnYgsbq9wdRWPXIb2WXJMHC8zpfATfgN1eq31B9ZIyc2Dn2m1wSO3Duy4-imz_QNqcXxlZG5yz_p1puueAiyp_tWTnAooUXOwPjauvGsuCEo5ZJ-V1Oh64DMzNbGPSq69X_lhjHkhs9LaFDvf6H7rb_0fS-eK0_my8822ykXFD0JuW79N725veEfxwtpjHclI58tQ8BLUlxUxvKaeYTY2ZonqPWSyOBoeVlsu9SNhUm7vpsaow15VuOG4U5mz6Zu-2xwoUL1KefUq5lspvX5rmwTl-Ag7alTI