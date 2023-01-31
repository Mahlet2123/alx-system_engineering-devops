#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\w+|\+?\d+)\]\s+\[to:(\+?\d+)\]\s+\[flags:(\-?\d+\:\-?\d+\:\-?\d+\:\-?\d+\:\-?\d+)/).join(',')
