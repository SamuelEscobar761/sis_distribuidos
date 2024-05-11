JSON_FILE="invalid.json"

while IFS= read -r line
do
  echo "Solicitud: $line"
  echo "$line" | grpcurl -plaintext -d @ localhost:2029 ViajeService/Start
done < <(jq -c '.[]' "$JSON_FILE")
