# Input:
# - The URL you want to query, e.g. https://analysiscenter.veracode.com/api/5.0/getapplist.do
# - The HTTP method, e.g. GET
# - Your API credentials VERACODE_ID and VERACODE_KEY which you can generate (and revoke) from the UI
#   Below values don't work any longer (that would be too easy, right?) and are included to allow tracing the HMAC operations.

VERACODE_ID=<api_id>
VERACODE_KEY=<api_secret>

NONCE="$(cat /dev/random | xxd -p | head -c 32)"
# NONCE=43a096639916c4f3925a44200cc2eeeb
TS="$(($(date +%s%N)/1000))"
# TS=1528471895699
URLPATH=/api/5.0/getapplist.do
METHOD=GET

encryptedNonce=$(echo "$NONCE" | xxd -r -p | openssl dgst -sha256 -mac HMAC -macopt hexkey:$VERACODE_KEY | cut -d ' ' -f 2)
# encryptedNonce=fdadd4b99d0e80e2ff62c8462e649df50b7d8454bc44184385ad2d249eb0d3a2

encryptedTimestamp=$(echo -n "$TS" | openssl dgst -sha256 -mac HMAC -macopt hexkey:$encryptedNonce | cut -d ' ' -f 2)
# encryptedTimestamp=cf2289384942ad95b591c15053dc2e91c16ec555722c4886329e697337240c98

signingKey=$(echo -n "vcode_request_version_1" | openssl dgst -sha256 -mac HMAC -macopt hexkey:$encryptedTimestamp | cut -d ' ' -f 2)
# signingKey=72163d368a280f9b5fc467baa1c181c391378e88b5bee0906569142d7d9d9e2f

DATA="id=$VERACODE_ID&host=analysiscenter.veracode.com&url=$URLPATH&method=$METHOD"
signature=$(echo -n "$DATA" | openssl dgst -sha256 -mac HMAC -macopt hexkey:$signingKey | cut -d ' ' -f 2)
VERACODE_AUTH_HEADER="VERACODE-HMAC-SHA-256 id=$VERACODE_ID,ts=$TS,nonce=$NONCE,sig=$signature"
# VERACODE_AUTH_HEADER=VERACODE-HMAC-SHA-256 id=684a28d91070e4ce68b2131e43c2d79b,ts=1528471895699,nonce=43a096...3c72e2

curl -X $METHOD -H "Authorization: $VERACODE_AUTH_HEADER" "https://api.veracode.com/api/authn/v2/users/self"