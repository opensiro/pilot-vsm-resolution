import Pilot.Core

namespace Pilot

-- The theorem can be imported and reused outside its defining module.
theorem round_trip {α : Type} (xs : List α) : reverse (reverse xs) = xs :=
  reverse_involutive xs

-- Executable concrete case, separate from the general proof.
example : reverse (reverse [1, 2, 3]) = [1, 2, 3] := by decide

end Pilot
