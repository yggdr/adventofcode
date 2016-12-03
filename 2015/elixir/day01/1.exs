defmodule Main do
  def main do
    case File.read "../../input/day01/input" do
      {:ok, content} -> content
                        |> String.graphemes
                        |> Enum.map(fn x -> case x do "(" -> 1; ")" -> -1 end end)
                        |> Enum.reduce(fn x, acc -> x + acc end)
                        |> IO.puts
      {:error, reason} -> IO.puts "Something went wrong: #{reason}"
    end
  end

  # "Inspired" by Rob-bie. Don't like that you still have to go through the entire
  # list
  def second do
    case File.read "../../input/day01/input" do
      {:ok, content} -> content
                        |> String.graphemes
                        |> Enum.map(fn x -> case x do "(" -> 1; ")" -> -1 end end)
                        |> Enum.reduce({0, 0}, fn x, acc ->
                             case acc do
                               {n, -1} -> n
                               {n, p} -> case x do
                                 1 -> {n+1, p+1}
                                 -1 -> {n+1, p-1}
                               end
                               n -> n
                             end
                           end)
                        |> IO.puts
      {:error, reason} -> IO.puts "Something went wrong: #{reason}"
    end
  end
end

Main.main
Main.second
