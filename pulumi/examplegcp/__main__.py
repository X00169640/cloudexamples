import pulumi
import pulumi_gcp as gcp

example_vpc = gcp.compute.Network("examplevpc",
    auto_create_subnetworks=False
)

example_subnet = gcp.compute.Subnetwork("examplesubnet",
    region = "europe-west2",
    ip_cidr_range="10.0.0.0/24",
    network=example_vpc.id
)

example_server = gcp.compute.Instance("exampleserver",
    machine_type="e2-medium",
    zone="europe-west2-a",
    boot_disk={
        "initializeParams": {
            "image": "debian-cloud/debian-9",
        },
    },
    network_interfaces=[{"subnetwork": example_subnet.id,}]
)