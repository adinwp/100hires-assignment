import os

video_urls = [
    "R2_1j6j74hU",
    "F3zW1j8r0L0",
    "4W4H1xWp1hE"
]

output_dir = "research/youtube-transcripts"
os.makedirs(output_dir, exist_ok=True)

print("Memulai proses penarikan transkrip...\n")

for video_id in video_urls:
    print(f"Mencari transkrip untuk video: {video_id}...")
    # Kita eksekusi library-nya langsung lewat CLI terminal untuk bypass error class
    command = f"python -m youtube_transcript_api {video_id} > {output_dir}/{video_id}.txt"
    exit_code = os.system(command)
    
    if exit_code == 0:
        print(f"✅ Berhasil menyimpan {video_id}.txt\n")
    else:
        print(f"❌ Gagal menarik transkrip {video_id}\n")

print("Proses selesai!")