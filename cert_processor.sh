# local directories to use
script_dir="$(pwd)"
local_cert_folder="/etc/letsencrypt/live"
local_backup_folder="/Users/Shared/Playground/CodeForLyf/ssl-certificates"

copy_and_convert_certificate() {
    SOURCE_CERT_DIR_PATH=$1
    DEST_CERT_DIR_PATH=$2
    PASSWORD=$3

    cp -RL "${SOURCE_CERT_DIR_PATH}/." "${DEST_CERT_DIR_PATH}/"
    cd "${DEST_CERT_DIR_PATH}"
    openssl pkcs12 -export -out certificate.pfx -inkey privkey.pem -in cert.pem -certfile chain.pem -passout pass:$PASSWORD
}

# Copy the certificates to the backup folder and convert them to pfx as necessary
copy_and_convert_certificate "${local_cert_folder}/admin-server.veniqa.com-0003" "${local_backup_folder}/admin-server.veniqa.com" "YOUR_PASSWORD_HERE"
copy_and_convert_certificate "${local_cert_folder}/shop-server.veniqa.com" "${local_backup_folder}/shop-server.veniqa.com" "YOUR_PASSWORD_HERE"

# Activate python virtual env & run the uploader
cd "$script_dir"
source venv/bin/activate
python cert_uploader.py