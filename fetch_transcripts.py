import os

video_urls = [
    "v2I4bX8bH4Q",
    "fS8S7M-4drc",
    "J1MhB8B1foc"
]

output_dir = "research/youtube-transcripts"
os.makedirs(output_dir, exist_ok=True)

print("Memulai proses penarikan transkrip baru...\n")

for video_id in video_urls:
    print(f"Mencari transkrip untuk video: {video_id}...")
    # Menggunakan CLI wrapper untuk langsung mendownload transkrip bersih
    command = f"python -m youtube_transcript_api {video_id} --languages en > {output_dir}/{video_id}.txt"
    exit_code = os.system(command)
    
    if exit_code == 0:
        print(f"✅ Berhasil menyimpan {video_id}.txt\n")
    else:
        print(f"❌ Gagal menarik transkrip {video_id}\n")

print("Proses selesai!")