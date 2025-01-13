from collections import defaultdict

def build_graph(number_of_junctions):
    conveyor_network = defaultdict(list)
    for _ in range(number_of_junctions):
        connection_data = input().split()
        destination = connection_data[0]
        for source in connection_data[1:]:
            conveyor_network[source].append(destination)
    return conveyor_network

def calculate_shipping_cost(number_of_junctions):
    conveyor_network = build_graph(number_of_junctions)
    
    delivery_sequence = input().split()
    manual_delivery_costs = list(map(int, input().split()))
    allowed_switches = int(input())
    
    junction_switch_count = defaultdict(int)
    active_routes = defaultdict(str)
    
    total_delivery_cost = 0
    
    for package_index, start_point in enumerate(delivery_sequence):
        current_location = start_point
        delivery_route = [current_location]
        
        while current_location in conveyor_network:
            current_location = conveyor_network[current_location][0]
            delivery_route.append(current_location)
            
        requires_manual_delivery = False
        
        for step in range(len(delivery_route)-1):
            current_junction = delivery_route[step]
            next_junction = delivery_route[step+1]
            
            if active_routes[next_junction] != current_junction:
                if junction_switch_count[next_junction] >= allowed_switches:
                    requires_manual_delivery = True
                    break
                    
                active_routes[next_junction] = current_junction
                junction_switch_count[next_junction] += 1
        
        if requires_manual_delivery:
            total_delivery_cost += manual_delivery_costs[package_index]
            
    return total_delivery_cost

number_of_junctions = int(input())
final_cost = calculate_shipping_cost(number_of_junctions)
print(final_cost)
