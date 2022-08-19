## Pertanyaan

> Kalian diminta untuk membuat sebuah backend services untuk menerima sebuah data kecepatan, latitude dan longitude dalam sebuah body json. Dan kalian juga diharapkan untuk menyimpan data tersebut beserta dengan timestampnya.

### Expected Body
```json
{
    "kecepatan": 90,
    "latitude": 6.2088,
    "longitude": 106.8456
}
```

### Expected data yang disimpan dalam database mongodb
* ID transaksi
* kecepatan
* latitude
* longitude
* timestamp

## Jawab
1. Untuk script json disimpan di file ```bodyJson.py```
2. Expected body menggunakan Postman
![postman](https://user-images.githubusercontent.com/107297270/185641387-2f7e52e4-ff88-4800-85ed-9b5ad7c041fc.png)
3. Untuk script menyimpan data ke mongodb disimpan di file ```db_location.py```
4. Tampilan di web ```mongodb```
![mongodb](https://user-images.githubusercontent.com/107297270/185641089-a23603af-40ee-482e-af7d-ea1b1983225d.png)
