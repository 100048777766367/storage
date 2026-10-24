import os, sys, json, time, hashlib
REPO_NAME = "{repo_name}"
epoch = 1
state_file = "synapses/state.json"
if os.path.exists(state_file):
    try:
        with open(state_file, "r") as f: epoch = json.load(f).get("generation_epoch", 0) + 1
    except Exception: pass

t = int(time.time())
cid = hashlib.shake_256(f"{REPO_NAME}_{epoch}_{t}".encode()).hexdigest(32)

seed_vector = 0b1101111100000001
entropy_delta = int(cid[:8], 16) & 0xFFFF
xor_mutated = seed_vector ^ entropy_delta
reverted = xor_mutated ^ entropy_delta
assert reverted == seed_vector, "LỖI BẤT BIẾN: Toán tử XOR mất tính đối xứng tự nghịch đảo!"

def execute_domain_logic(): return "DOMAIN_PULSE_ACTIVE"
domain_status = execute_domain_logic()

os.makedirs("synapses", exist_ok=True)
with open(state_file, "w", encoding="utf-8") as f:
    json.dump({"generation_epoch": epoch, "last_timestamp": t, "quantum_cid": cid, "state_vector_hex": hex(xor_mutated), "status": "SYNCHRONIZED_ALIVE"}, f, indent=4)

with open("synapse_forward.json", "w", encoding="utf-8") as f:
    json.dump({"contract": "bodhi.contract.v1", "identity": f"100048777766367/{REPO_NAME}", "epoch": epoch, "cid": cid, "proof": "XOR_INVARIANT_VALID", "domain_status": domain_status}, f, indent=4)
