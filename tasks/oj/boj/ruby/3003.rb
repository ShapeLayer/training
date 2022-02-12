king, queen, rook, bishop, knight, pawn = gets.split
puts '%d %d %d %d %d %d' % [1 - king.to_i, 1 - queen.to_i, 2 - rook.to_i, 2 - bishop.to_i, 2 - knight.to_i, 8 - pawn.to_i]