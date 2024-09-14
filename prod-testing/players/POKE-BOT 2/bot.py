# Don't change these import settings
import sys
sys.path.append('../players')
from players.gen6player import Gen6Player

# Import the required classes        
from poke_env.environment.move import Move
from poke_env.environment.pokemon import Pokemon

class MyPokeBot(Gen6Player):

    def choose_move(self, battle):
        # Get the active Pokémon
        active_pokemon = battle.active_pokemon
        print("Active Pokemon:", active_pokemon)
        
        
        # TODO: First pokemon to go in battle
        
        if active_pokemon != None:

            # Check if the active Pokémon is Landorus-Therian
            if active_pokemon.species == "landorustherian":
                # Print the available moves
                print("Available moves:", battle.available_moves)
                
                # Use Knock Off to remove items
                if "knockoff" in battle.available_moves and battle.opponent_active_pokemon and battle.opponent_active_pokemon.item != None:
                    print("Removing opponent's item with Knock Off")
                    return self.create_order(Move("knockoff", 6))
                
                # Prioritize using Earthquake if it's super effective
                elif "earthquake" in battle.available_moves and battle.opponent_active_pokemon and (battle.opponent_active_pokemon.type_1 in ["Fire", "Electric", "Rock", "Steel", "Poison"] or battle.opponent_active_pokemon.type_2 in ["Fire", "Electric", "Rock", "Steel", "Poison"]):
                    print("Opponent's active Pokémon is weak to Ground-type moves")
                    return self.create_order(Move("earthquake", 6),)
                
                # # Use Stone Edge if the opponent is weak to Rock-type moves
                elif "stoneedge" in battle.available_moves and battle.opponent_active_pokemon and (battle.opponent_active_pokemon.type_1 in ["Flying", "Bug", "Fire", "Ice"] or battle.opponent_active_pokemon.type_2 in ["Flying", "Bug", "Fire", "Ice"]):
                    print("Opponent's active Pokémon is weak to Rock-type moves")
                    return self.create_order(Move("stoneedge", 6))
                
                # # Use U-turn for pivoting
                elif "uturn" in battle.available_moves and battle.opponent_active_pokemon and (battle.opponent_active_pokemon.type_1 not in ["Flying", "Bug", "Fire", "Ice", "Electric", "Rock", "Steel", "Poison"] or battle.opponent_active_pokemon.type_2 not in ["Flying", "Bug", "Fire", "Ice", "Electric", "Rock", "Steel", "Poison"]):
                    print("Pivoting with U-turn")
                    return self.create_order(Move("uturn", 6))
                
                
             
  
        
        # Default move 
        return self.choose_random_move(battle)
