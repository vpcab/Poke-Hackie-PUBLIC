# Don't change these import settings
import sys
sys.path.append('../players')
from players.gen6player import Gen6Player

# Import the required classes        
from poke_env.environment.move import Move
from poke_env.environment.pokemon import Pokemon
from players.gen6player import Gen6Player
from poke_env.environment.move import Move
from poke_env.environment.pokemon import Pokemon

class MyPokeBot(Gen6Player):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spikes_count = 0  # Initialize a counter for Spikes
        
        
    def choose_move(self, battle):
        # Get the active Pokémon
        # active_pokemon = battle.active_pokemon
        # print("Active Pokemon: ", active_pokemon)
        # print("Available moves:", battle.available_moves)
        # 
        
        if battle.available_moves:
            # Get the active Pokémon
            active_pokemon = battle.active_pokemon
            opponent_pokemon = battle.opponent_active_pokemon
            print("Active Pokemon: ", active_pokemon)
            print("Available moves:", battle.available_moves)
            available_moves = battle.available_moves
        
            # if active_pokemon is None:
                # return self.choose_random_move(battle)
        
            # Check if the active Pokémon is Landorus-Therian
            if active_pokemon.species == "landorustherian":
                print("Landorus-Therian", active_pokemon.type_1, active_pokemon.type_2)

                # Prioritize using Earthquake if it's super effective
                if "earthquake" in available_moves and opponent_pokemon and opponent_pokemon.type_1 in ["Fire", "Electric", "Rock", "Steel", "Poison"]:
                    print("Earthquake")
                    return self.create_order(Move("earthquake", 6))

                # Use Stone Edge if the opponent is weak to Rock-type moves
                if "stoneedge" in available_moves and opponent_pokemon and opponent_pokemon.type_1 in ["Flying", "Bug", "Fire", "Ice"]:
                    print("Stone Edge")
                    return self.create_order(Move("stoneedge", 6))

                # Use U-turn for pivoting
                if "uturn" in available_moves and opponent_pokemon and opponent_pokemon.type_1 not in ["Flying", "Bug", "Fire", "Ice", "Electric", "Rock", "Steel", "Poison"]:
                    print("U-turn")
                    return self.create_order(Move("uturn", 6))

                # Use Knock Off to remove items
                if "knockoff" in available_moves and opponent_pokemon and opponent_pokemon.item is not None:
                    print("Knock Off")
                    return self.create_order(Move("knockoff", 6))
                print("Default move")
                return self.choose_random_move(battle)
        
            
            # Define move logic for Rotom-Wash
            if active_pokemon.species == "rotomwash":
                print("Rotom-Wash", active_pokemon.type_1, active_pokemon.type_2)
                
                # Use Hydro Pump if it's super effective
                if opponent_pokemon and (opponent_pokemon.type_1 in ["Fire", "Ground", "Rock"] or opponent_pokemon.type_2 in ["Fire", "Ground", "Rock"]):
                    print("Hydro Pump")
                    return self.create_order(Move("hydropump", 6))

                # Use Volt Switch if it's super effective
                if opponent_pokemon and (opponent_pokemon.type_1 in ["Water", "Flying"] or opponent_pokemon.type_2 in ["Water", "Flying"]):
                    print("Volt Switch")
                    return self.create_order(Move("voltswitch", 6))

                # Use Will-O-Wisp to burn physical attackers
                if opponent_pokemon and opponent_pokemon.base_stats["atk"] > opponent_pokemon.base_stats["spa"] and opponent_pokemon.status is None:
                    print("Will-O-Wisp")
                    return self.create_order(Move("willowisp", 6))

                # Use Pain Split if Rotom-Wash's HP is low
                if active_pokemon.current_hp_fraction < 0.5:
                    print("Pain Split")
                    return self.create_order(Move("painsplit", 6))
                
                print("Default move")
                return self.choose_random_move(battle)
            
                
                # Define move logic for Ferrothorn
            if active_pokemon.species == "ferrothorn":
                print("Ferrothorn", active_pokemon.type_1, active_pokemon.type_2)
                
                # Use Gyro Ball if it's super effective
                if opponent_pokemon and (opponent_pokemon.type_1 in ["Fairy", "Rock", "Ice"] or opponent_pokemon.type_2 in ["Fairy", "Rock", "Ice"]):
                    print("Gyro Ball")
                    return self.create_order(Move("gyroball", 6))

                # Use Stealth Rock if entry hazards are not set
                if not battle.side_conditions and self.spikes_count < 3:
                    self.spikes_count += 1
                    print(f"Spikes (used {self.spikes_count} times)")
                    return self.create_order(Move("spikes", 6))
   
                # Use Leech Seed to drain HP
                # if opponent_pokemon and (opponent_pokemon.type_1 not in ["Grass"] or opponent_pokemon.type_2 not in ["Grass"]):
                #    print("Leech Seed")
                #    return self.create_order(Move("leechseed", 6))

                # else:
                # # Use Protect to scout or stall
                # print("Protect")
                # return self.create_order(Move("protect", 6))
                print("Default move")
                return self.choose_random_move(battle)
        
        
            # Define move logic for Latios
            if active_pokemon.species == "latios":
                print("Latios", active_pokemon.type_1, active_pokemon.type_2)
                
                # Use Draco Meteor if it's super effective
                if opponent_pokemon and (opponent_pokemon.type_1 in ["Dragon"] or opponent_pokemon.type_2 in ["Dragon"]):
                    print("Draco Meteor")
                    return self.create_order(Move("dracometeor", 6))
                
                # Use Psyshock if it's super effective
                if opponent_pokemon and (opponent_pokemon.type_1 in ["Fighting", "Poison"] or opponent_pokemon.type_2 in ["Fighting", "Poison"]):
                    print("Psyshock")
                    return self.create_order(Move("psyshock", 6))
                
                # Use Defog to remove hazards if they are present
                if battle.side_conditions or battle.opponent_side_conditions:
                    print("Defog")
                    return self.create_order(Move("defog", 6))
                
                # Use Roost to heal if Latios's HP is low
                if active_pokemon.current_hp_fraction < 0.5:
                    print("Roost")
                    return self.create_order(Move("roost", 6))
            
                print("Default move")
                return self.choose_random_move(battle)
        
        
        
            # Define move logic for Heatran
            if active_pokemon.species == "heatran":
                print("Heatran", active_pokemon.type_1, active_pokemon.type_2)
                
                # Use Lava Plume if it's super effective
                if opponent_pokemon and (opponent_pokemon.type_1 in ["Steel", "Grass", "Bug", "Ice"] or opponent_pokemon.type_2 in ["Steel", "Grass", "Bug", "Ice"]):
                    print("Lava Plume")
                    return self.create_order(Move("lavaplume", 6))
            
                # Use Earth Power if it's super effective
                if opponent_pokemon and (opponent_pokemon.type_1 in ["Fire", "Electric", "Rock", "Steel", "Poison"] or opponent_pokemon.type_2 in ["Fire", "Electric", "Rock", "Steel", "Poison"]):
                    print("Earth Power")
                    return self.create_order(Move("earthpower", 6))

                # Use Toxic to poison the opponent
                if opponent_pokemon and (opponent_pokemon.type_1 not in ["Steel", "Poison"] or opponent_pokemon.type_2 not in ["Steel", "Poison"]):
                    print("Toxic")
                    return self.create_order(Move("toxic", 6))
            
                # Use Protect to scout or stall
                print("Protect")
                return self.create_order(Move("protect", 6))
            
            
            # Define move logic for Azumarill
            if active_pokemon.species == "azumarill":
                print("Azumarill", active_pokemon.type_1, active_pokemon.type_2)

                # Use Play Rough if it's super effective
                if "playrough" in available_moves and opponent_pokemon and (opponent_pokemon.type_1 in ["Dragon", "Dark", "Fighting"] or opponent_pokemon.type_2 in ["Dragon", "Dark", "Fighting"]):
                    print("Play Rough")
                    return self.create_order(Move("playrough", 6))

                # Use Waterfall if it's super effective
                if "waterfall" in available_moves and opponent_pokemon and (opponent_pokemon.type_1 in ["Fire", "Ground", "Rock"] or opponent_pokemon.type_2 in ["Fire", "Ground", "Rock"]):
                    print("Waterfall")
                    return self.create_order(Move("waterfall", 6))

                # Use Knock Off to remove items
                if "knockoff" in available_moves and opponent_pokemon and opponent_pokemon.item is not None:
                    print("Knock Off")
                    return self.create_order(Move("knockoff", 6))

                # Use Aqua Jet for priority
                if "aquajet" in available_moves:
                    print("Aqua Jet")
                    return self.create_order(Move("aquajet", 6))

                print("Default move")
                return self.choose_random_move(battle)
        
        
        else:
            print("Default move")
            return self.choose_random_move(battle)
        
        print("Default move")
        return self.choose_random_move(battle)
