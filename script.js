document.addEventListener("DOMContentLoaded", () => {
    const loader = document.querySelector('.loader');
    if(loader) {
        let dots = 0;
        setInterval(() => {
            dots = (dots + 1) % 4;
            loader.textContent = ".".repeat(dots);
        }, 500);
    }
});

function toggleMute() {
    const video = document.getElementById('pitchVideo');
    const btn = document.getElementById('muteToggle');
    if (!video) return;
    video.muted = !video.muted;
    btn.innerHTML = video.muted ? '🔇 Tap to unmute' : '🔊 Sound on';
    btn.style.background = video.muted ? 'rgba(0,0,0,0.6)' : 'rgba(99,102,241,0.7)';
}
