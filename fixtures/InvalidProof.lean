import Pilot.Core

namespace Pilot

-- Intentionally false: this MUST NOT compile. Not a normal library target.
example : reverse [1, 2] = [1, 2] := by
  rfl

end Pilot
