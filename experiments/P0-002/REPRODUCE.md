# Reproduce P0.1 on dev-alpha or another Linux x86_64 host

Source commit `1f232ebfc915bb7a45db20ac12381cc2099f7136`. Requires Git, curl, tar, zstd and Python 3.10+, and several GB temporary space. Do not unpack Lean into this VM's nearly full root filesystem.

```sh
mkdir -p /dev/shm/vsm-res-lean-20261023
curl -fL --retry 2 https://github.com/leanprover/lean4/releases/download/v4.35.0/lean-4.35.0-linux.tar.zst -o /dev/shm/vsm-res-lean-20261023/lean-4.35.0-linux.tar.zst
echo '7289597a44543246c9227b8cae501767e095ce17f6d448b95fc4a8dc97268f6d  /dev/shm/vsm-res-lean-20261023/lean-4.35.0-linux.tar.zst' | sha256sum --check
tar -I zstd -xf /dev/shm/vsm-res-lean-20261023/lean-4.35.0-linux.tar.zst -C /dev/shm/vsm-res-lean-20261023
git clone https://github.com/opensiro/pilot-vsm-resolution.git /dev/shm/vsm-res-p01-replay
cd /dev/shm/vsm-res-p01-replay
git checkout --detach 1f232ebfc915bb7a45db20ac12381cc2099f7136
export PATH=/dev/shm/vsm-res-lean-20261023/lean-4.35.0-linux/bin:$PATH
python3 -m unittest discover -s scripts -p 'test_*.py' -v
lake clean
python3 scripts/run_pilot.py --output experiments/local-dev-alpha-replay-unique
```

Use a new output path every run: the runner refuses overwrites. Archive the receipt and logs with host metadata; `/dev/shm` can vanish on reboot. This runbook does not configure GitHub Actions or a persistent service.
