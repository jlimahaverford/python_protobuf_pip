from python_protobuf_pip import game_pb2

game = game_pb2.Game()
game.player_one_id = 0
game.player_one_character = game_pb2.CAPTAIN_FALCON
game.player_two_id = 1
game.player_two_character = game_pb2.DONKEY_KONG
game.player_one_wins = True
print(game)
