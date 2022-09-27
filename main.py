from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

list_mahasiswa = {
    18220035: {"nama": "Widhy"}
}
class mahasiswa(BaseModel):
    nama: str

@app.post("/mahasiswa/{NIM}")
async def tambah_mhs(NIM: int, mhs: mahasiswa):
    if NIM in list_mahasiswa:
        return{"message": "NIM sudah terpakai"}
    list_mahasiswa[NIM] = {"nama": mhs.nama}
    return {"message": "Mahasiswa berhasil ditambahkan"}

@app.get("/mahasiswa/")
async def lihat_mhs():
    return list_mahasiswa

@app.get("/cek_nim/{nim}")
async def cek_nim(nim: int = Path(None, description="NIM harus angka")):
    if nim in list_mahasiswa:
        return list_mahasiswa[nim]
    return {"message": "NIM tersebut tidak ditemukan di dalam database"}

@app.get("/cek_nama")
async def cek_nama(nama: str = Path(None, description="Nama harus huruf")):
    for nim in list_mahasiswa:
        if list_mahasiswa[nim]["nama"] == nama:
            return list_mahasiswa[nim]
    return {"message": "Nama tersebut tidak ditemukan di dalam database"}