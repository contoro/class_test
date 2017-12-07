dub_pa_a = {"name" : "dub-pa-5050-a", "ip" : "10.60.255.5", "location" : "DUB", "vendor" : "Palo Alto", "Model" : "PA 5050" }
dub_pa_b = {"name" : "dub-pa-5050-b", "ip" : "10.60.255.6", "location" : "DUB", "vendor" : "Palo Alto", "Model" : "PA 5050" }
ven_core_a = {"name" : "ven-core-a", "ip" : "10.30.255.253", "location" : "VEN", "vendor" : "Cisco", "Model" : "Nexus 9504" }
ven_pa3050_a = {"name" : "ven-pa-3050-a", "ip" : "10.30.255.5", "location" : "VEN", "vendor" : "Palo Alto", "Model" : "PA 3050" }
wlt_sdwan_a = {"name" : "wlt-wan-veg2000a", "ip" : "172.30.89.210", "location" : "WLT", "vendor" : "Viptela", "Model" : "vEdge 2000" }
wlt_idf_4s = {"name" : "wlt-idf-4s", "ip" : "10.89.255.11", "location" : "WLT", "vendor" : "Cisco", "Model" : "Catalyst 4510" }


device_list = [
    dub_pa_a, dub_pa_b, ven_core_a, ven_pa3050_a, wlt_idf_4s, wlt_sdwan_a ]
#
# print([d["name"] for d in device_list if "vendor" in d])

for i in device_list:
    if "vendor" == "Cisco":
        print(i ["ip"])

# for i in device_list:
#     if device_list
#         print(i)
#     if dict.get('name'):
#         print
#
# for k, v in dub_pa_b.items():
#     if dub_pa_b.items():
#         print(v)

