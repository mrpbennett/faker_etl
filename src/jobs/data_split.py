import psycopg2

db = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="192.168.5.81",
    port="5432",
)

# GDPR-compliant countries (EU/EEA, Switzerland, UK)
countries_gdpr = "'AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE','IS','LI','NO','CH','GB'"

# Other GDPR-aligned countries (recognized for adequacy) but not part of the EU/EEA
countries_other_compliant = "'CA','JP','KR','NZ','IL'"

# Middle East and EMEA countries (excluding GDPR countries and GDPR-aligned ones)
countries_emea = (
    "'AE','BH','EG','IR','IQ','JO','KW','LB','OM','PS','QA','SA','SY','TR','YE'"
)

# Non-GDPR countries (all other countries excluding GDPR and compliant)
countries_no_gdpr = "'AF','AG','AI','AO','AR','AU','BB','BD','BJ','BM','BN','BO','BR','BT','BW','BZ','CL','CN','CO','CR','CU','DM','DO','DZ','EC','FJ','GD','GH','GT','GY','HK','HN','ID','IN','JM','KE','KH','KN','LA','LK','LR','LY','MA','MG','MM','MO','MR','MU','MX','MY','MZ','NA','NG','NI','NP','OM','PA','PE','PH','PK','RW','SC','SG','SL','SN','SR','SV','TH','TJ','TN','TT','TZ','UA','UG','US','UY','UZ','VE','VN','ZA','ZM','ZW'"
