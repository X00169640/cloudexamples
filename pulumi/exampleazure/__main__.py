import pulumi
import pulumi_azure_native as azure_native
from pulumi_azure import compute, network

example_rg = azure_native.resources.ResourceGroup("example_rg",
    resource_group_name="example_rg"
)

example_vnet = azure_native.network.VirtualNetwork("example_vnet",
    resource_group_name=example_rg.name,
    virtual_network_name="example_vnet",
    address_space=azure_native.network.AddressSpaceArgs(
        address_prefixes=["10.0.0.0/16"],
    )
)

example_subnet = azure_native.network.Subnet("example_subnet",
    virtual_network_name=example_vnet.name,
    resource_group_name=example_rg.name,
    subnet_name="example_subnet",
    address_prefix="10.0.0.0/24")

example_nic = network.NetworkInterface("example_nic",
    name = "example_nic",
    resource_group_name=example_rg.name,
    # opts=pulumi.ResourceOptions(depends_on=[web_subnet]),
    ip_configurations=[{
        "name": "exampleconfiguration",
        "subnet_id": example_subnet.id,
        "privateIpAddressAllocation": "Dynamic"
    }])

example_server = compute.VirtualMachine("example-server",
    location=example_rg.location,
    resource_group_name=example_rg.name,
    network_interface_ids=[example_nic.id],
    vm_size="Standard_DS1_v2",
    delete_os_disk_on_termination=True,
    delete_data_disks_on_termination=True,
    storage_image_reference={
        "publisher": "Canonical",
        "offer": "UbuntuServer",
        "sku": "18.04-LTS",
        "version": "latest",
    },
    storage_os_disk={
        "name": "web-disk",
        "caching": "ReadWrite",
        "create_option": "FromImage",
        "managedDiskType": "Standard_LRS",
    },
    os_profile={
        "computer_name": "hostname",
        "admin_username": "testadmin",
        "admin_password": "Password1234!",
    },
    os_profile_linux_config={
        "disable_password_authentication": False,
    })




