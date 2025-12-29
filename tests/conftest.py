import pytest

@pytest.fixture(autouse=True)
def mock_api(mocker):
    def fake_get(url):
        nip = url.split("/nip/")[1].split("?")[0]
        response = mocker.Mock()
        if nip == "1234567890":
            response.status_code = 200
            response.json.return_value = {
                "result": {"subject": None}
            }
        elif nip == "7342867148":
            response.status_code = 200
            response.json.return_value = {
                "result": {"subject": {"statusVat": "Czynny"}}
            }
        elif nip == "9571014371":
            response.status_code = 200
            response.json.return_value = {
                "result": {"subject": {"statusVat": "Niezarejestrowany"}}
            }
        return response

    mocker.patch("src.company_account.get", side_effect=fake_get)
    mocker.patch.dict("os.environ", {"BANK_APP_MF_URL": "https://wl-api.mf.gov.pl/"})
