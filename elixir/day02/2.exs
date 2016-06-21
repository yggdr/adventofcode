defmodule Wrapping do
  def how_much_paper? do
    Enum.reduce(measures(&area/3), fn x, acc -> x+acc end)
  end

  defp measures func do
    for measure <- File.read!("../../input/day02/input") |> String.split("\n") do
      case String.split(measure, "x") do
        [x, y, z] -> func.(x, y, z)
        _ -> 0
      end
    end
  end

  defp conv x, y, z do
    [String.to_integer(x), String.to_integer(y), String.to_integer(z)]
  end

  defp area x, y, z do
    [x, y, z] = conv x, y, z
    xy = x*y
    xz = x*z
    yz = y*z
    2*xz+2*xy+2*yz + (min(xz, xy) |> min(yz))
  end

  defp len x, y, z do
    [x, y, z] = conv(x, y, z) |> Enum.sort
    2*(x+y) + x*y*z
  end

  def how_much_ribbon? do
    Enum.reduce(measures(&len/3), fn x, acc -> x+acc end)
  end
end

IO.puts Wrapping.how_much_paper?
IO.puts Wrapping.how_much_ribbon?
