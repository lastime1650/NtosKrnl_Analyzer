# sub_006F3DB6

- RVA: `0x006F3DB6`–`0x006F4169` (길이 `947` bytes)
- VA: `0x00000001406F3DB6`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC58C`
- 디코드: `265`개 명령, `947/947` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006F3E05` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x006F3E11` → [XmEvaluateIndexSpecifier](../57/XmEvaluateIndexSpecifier_function_00578928.md) (function, `0x00578928`)
- `0x006F3E40` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F3E4D` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x006F3E8E` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F3E9B` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x006F3EAD` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F3EBA` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x006F3ECC` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F3ED9` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x006F3EEB` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F3EF8` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x006F3F0A` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F3F17` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x006F3F29` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F3F36` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x006F3F99` → [XmGetWordImmediate](../47/XmGetWordImmediate_function_004731DC.md) (function, `0x004731DC`)
- `0x006F3FC4` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F3FD5` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F3FF0` → [XmGetWordImmediate](../47/XmGetWordImmediate_function_004731DC.md) (function, `0x004731DC`)
- `0x006F4028` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F4039` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F4050` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F405E` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F40A7` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F40B8` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x006F40C9` → [XmGetWordImmediate](../47/XmGetWordImmediate_function_004731DC.md) (function, `0x004731DC`)
- `0x006F40D7` → [XmGetWordImmediate](../47/XmGetWordImmediate_function_004731DC.md) (function, `0x004731DC`)
- `0x006F40E4` → [XmGetWordImmediate](../47/XmGetWordImmediate_function_004731DC.md) (function, `0x004731DC`)
- `0x006F40F2` → [XmGetWordImmediate](../47/XmGetWordImmediate_function_004731DC.md) (function, `0x004731DC`)
- `0x006F4100` → [XmGetWordImmediate](../47/XmGetWordImmediate_function_004731DC.md) (function, `0x004731DC`)
- `0x006F4111` → [XmGetWordImmediate](../47/XmGetWordImmediate_function_004731DC.md) (function, `0x004731DC`)
- `0x006F414C` → [x86BiosTranslateAddress](../47/x86BiosTranslateAddress_function_004736C0.md) (function, `0x004736C0`)
- `0x006F4163` → [longjmp](../4F/longjmp_function_004FD5F0.md) (function, `0x004FD5F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **25**
  - `0x006F3DEC` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3DF5` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3DFD` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3E18` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3E20` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3E28` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3E30` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3E38` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3E57` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3E85` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3EA5` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3EC4` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3F02` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3F21` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3F40` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3F87` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3F91` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3FA7` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F3FB0` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F4007` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F4014` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F4048` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F409C` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F4121` → [XmEvaluateAddressSpecifier + 0x100](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)
  - `0x006F4152` → [XmEvaluateAddressSpecifier + 0x9B](../47/XmEvaluateAddressSpecifier_function_00473224.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F3DB6  0F 84 8E 00 00 00               je 0x1406f3e4a
006F3DBC  83 FA 08                        cmp edx, 8
006F3DBF  0F 87 97 00 00 00               ja 0x1406f3e5c
006F3DC5  74 76                           je 0x1406f3e3d
006F3DC7  85 D2                           test edx, edx
006F3DC9  74 6A                           je 0x1406f3e35
006F3DCB  83 EA 01                        sub edx, 1
006F3DCE  74 5D                           je 0x1406f3e2d
006F3DD0  83 EA 01                        sub edx, 1
006F3DD3  74 50                           je 0x1406f3e25
006F3DD5  83 EA 01                        sub edx, 1
006F3DD8  74 43                           je 0x1406f3e1d
006F3DDA  83 EA 01                        sub edx, 1
006F3DDD  74 2D                           je 0x1406f3e0c
006F3DDF  83 EA 01                        sub edx, 1
006F3DE2  74 1E                           je 0x1406f3e02
006F3DE4  83 EA 01                        sub edx, 1
006F3DE7  74 11                           je 0x1406f3dfa
006F3DE9  83 FA 01                        cmp edx, 1
006F3DEC  0F 85 32 F5 D7 FF               jne 0x140473324
006F3DF2  8B 77 34                        mov esi, dword ptr [rdi + 0x34]
006F3DF5  E9 2A F5 D7 FF                  jmp 0x140473324
006F3DFA  8B 77 30                        mov esi, dword ptr [rdi + 0x30]
006F3DFD  E9 22 F5 D7 FF                  jmp 0x140473324
006F3E02  48 8B CF                        mov rcx, rdi
006F3E05  E8 66 9E E7 FF                  call 0x14056dc70
006F3E0A  EB 0A                           jmp 0x1406f3e16
006F3E0C  8B D1                           mov edx, ecx
006F3E0E  48 8B CF                        mov rcx, rdi
006F3E11  E8 12 4B E8 FF                  call 0x140578928
006F3E16  8B F0                           mov esi, eax
006F3E18  E9 07 F5 D7 FF                  jmp 0x140473324
006F3E1D  8B 77 24                        mov esi, dword ptr [rdi + 0x24]
006F3E20  E9 FF F4 D7 FF                  jmp 0x140473324
006F3E25  8B 77 20                        mov esi, dword ptr [rdi + 0x20]
006F3E28  E9 F7 F4 D7 FF                  jmp 0x140473324
006F3E2D  8B 77 1C                        mov esi, dword ptr [rdi + 0x1c]
006F3E30  E9 EF F4 D7 FF                  jmp 0x140473324
006F3E35  8B 77 18                        mov esi, dword ptr [rdi + 0x18]
006F3E38  E9 E7 F4 D7 FF                  jmp 0x140473324
006F3E3D  48 8B CF                        mov rcx, rdi
006F3E40  E8 33 F8 D7 FF                  call 0x140473678
006F3E45  0F BE F0                        movsx esi, al
006F3E48  EB 0A                           jmp 0x1406f3e54
006F3E4A  48 8B CF                        mov rcx, rdi
006F3E4D  E8 1E 9E E7 FF                  call 0x14056dc70
006F3E52  8B F0                           mov esi, eax
006F3E54  03 77 18                        add esi, dword ptr [rdi + 0x18]
006F3E57  E9 C8 F4 D7 FF                  jmp 0x140473324
006F3E5C  83 EA 09                        sub edx, 9
006F3E5F  0F 84 C1 00 00 00               je 0x1406f3f26
006F3E65  83 EA 01                        sub edx, 1
006F3E68  0F 84 99 00 00 00               je 0x1406f3f07
006F3E6E  83 EA 01                        sub edx, 1
006F3E71  74 75                           je 0x1406f3ee8
006F3E73  83 EA 01                        sub edx, 1
006F3E76  74 94                           je 0x1406f3e0c
006F3E78  83 EA 01                        sub edx, 1
006F3E7B  74 4C                           je 0x1406f3ec9
006F3E7D  83 EA 01                        sub edx, 1
006F3E80  74 28                           je 0x1406f3eaa
006F3E82  83 FA 01                        cmp edx, 1
006F3E85  0F 85 99 F4 D7 FF               jne 0x140473324
006F3E8B  48 8B CF                        mov rcx, rdi
006F3E8E  E8 E5 F7 D7 FF                  call 0x140473678
006F3E93  0F BE F0                        movsx esi, al
006F3E96  EB 0A                           jmp 0x1406f3ea2
006F3E98  48 8B CF                        mov rcx, rdi
006F3E9B  E8 D0 9D E7 FF                  call 0x14056dc70
006F3EA0  8B F0                           mov esi, eax
006F3EA2  03 77 34                        add esi, dword ptr [rdi + 0x34]
006F3EA5  E9 7A F4 D7 FF                  jmp 0x140473324
006F3EAA  48 8B CF                        mov rcx, rdi
006F3EAD  E8 C6 F7 D7 FF                  call 0x140473678
006F3EB2  0F BE F0                        movsx esi, al
006F3EB5  EB 0A                           jmp 0x1406f3ec1
006F3EB7  48 8B CF                        mov rcx, rdi
006F3EBA  E8 B1 9D E7 FF                  call 0x14056dc70
006F3EBF  8B F0                           mov esi, eax
006F3EC1  03 77 30                        add esi, dword ptr [rdi + 0x30]
006F3EC4  E9 5B F4 D7 FF                  jmp 0x140473324
006F3EC9  48 8B CF                        mov rcx, rdi
006F3ECC  E8 A7 F7 D7 FF                  call 0x140473678
006F3ED1  0F BE F0                        movsx esi, al
006F3ED4  EB 0A                           jmp 0x1406f3ee0
006F3ED6  48 8B CF                        mov rcx, rdi
006F3ED9  E8 92 9D E7 FF                  call 0x14056dc70
006F3EDE  8B F0                           mov esi, eax
006F3EE0  03 77 2C                        add esi, dword ptr [rdi + 0x2c]
006F3EE3  E9 18 01 00 00                  jmp 0x1406f4000
006F3EE8  48 8B CF                        mov rcx, rdi
006F3EEB  E8 88 F7 D7 FF                  call 0x140473678
006F3EF0  0F BE F0                        movsx esi, al
006F3EF3  EB 0A                           jmp 0x1406f3eff
006F3EF5  48 8B CF                        mov rcx, rdi
006F3EF8  E8 73 9D E7 FF                  call 0x14056dc70
006F3EFD  8B F0                           mov esi, eax
006F3EFF  03 77 24                        add esi, dword ptr [rdi + 0x24]
006F3F02  E9 1D F4 D7 FF                  jmp 0x140473324
006F3F07  48 8B CF                        mov rcx, rdi
006F3F0A  E8 69 F7 D7 FF                  call 0x140473678
006F3F0F  0F BE F0                        movsx esi, al
006F3F12  EB 0A                           jmp 0x1406f3f1e
006F3F14  48 8B CF                        mov rcx, rdi
006F3F17  E8 54 9D E7 FF                  call 0x14056dc70
006F3F1C  8B F0                           mov esi, eax
006F3F1E  03 77 20                        add esi, dword ptr [rdi + 0x20]
006F3F21  E9 FE F3 D7 FF                  jmp 0x140473324
006F3F26  48 8B CF                        mov rcx, rdi
006F3F29  E8 4A F7 D7 FF                  call 0x140473678
006F3F2E  0F BE F0                        movsx esi, al
006F3F31  EB 0A                           jmp 0x1406f3f3d
006F3F33  48 8B CF                        mov rcx, rdi
006F3F36  E8 35 9D E7 FF                  call 0x14056dc70
006F3F3B  8B F0                           mov esi, eax
006F3F3D  03 77 1C                        add esi, dword ptr [rdi + 0x1c]
006F3F40  E9 DF F3 D7 FF                  jmp 0x140473324
006F3F45  0F 84 7B 01 00 00               je 0x1406f40c6
006F3F4B  83 FA 08                        cmp edx, 8
006F3F4E  0F 87 1F 01 00 00               ja 0x1406f4073
006F3F54  0F 84 F3 00 00 00               je 0x1406f404d
006F3F5A  85 D2                           test edx, edx
006F3F5C  0F 84 BD 00 00 00               je 0x1406f401f
006F3F62  83 EA 01                        sub edx, 1
006F3F65  0F 84 AE 00 00 00               je 0x1406f4019
006F3F6B  83 EA 01                        sub edx, 1
006F3F6E  74 4B                           je 0x1406f3fbb
006F3F70  83 EA 01                        sub edx, 1
006F3F73  74 40                           je 0x1406f3fb5
006F3F75  83 EA 01                        sub edx, 1
006F3F78  74 32                           je 0x1406f3fac
006F3F7A  83 EA 01                        sub edx, 1
006F3F7D  74 24                           je 0x1406f3fa3
006F3F7F  83 EA 01                        sub edx, 1
006F3F82  74 12                           je 0x1406f3f96
006F3F84  83 FA 01                        cmp edx, 1
006F3F87  0F 85 97 F3 D7 FF               jne 0x140473324
006F3F8D  0F B7 77 24                     movzx esi, word ptr [rdi + 0x24]
006F3F91  E9 8E F3 D7 FF                  jmp 0x140473324
006F3F96  48 8B CF                        mov rcx, rdi
006F3F99  E8 3E F2 D7 FF                  call 0x1404731dc
006F3F9E  E9 7B 01 00 00                  jmp 0x1406f411e
006F3FA3  0F B7 77 34                     movzx esi, word ptr [rdi + 0x34]
006F3FA7  E9 78 F3 D7 FF                  jmp 0x140473324
006F3FAC  0F B7 77 30                     movzx esi, word ptr [rdi + 0x30]
006F3FB0  E9 6F F3 D7 FF                  jmp 0x140473324
006F3FB5  0F B7 4F 34                     movzx ecx, word ptr [rdi + 0x34]
006F3FB9  EB 11                           jmp 0x1406f3fcc
006F3FBB  0F B7 4F 30                     movzx ecx, word ptr [rdi + 0x30]
006F3FBF  EB 0B                           jmp 0x1406f3fcc
006F3FC1  48 8B CF                        mov rcx, rdi
006F3FC4  E8 AF F6 D7 FF                  call 0x140473678
006F3FC9  0F BE C8                        movsx ecx, al
006F3FCC  66 03 4F 2C                     add cx, word ptr [rdi + 0x2c]
006F3FD0  EB 16                           jmp 0x1406f3fe8
006F3FD2  48 8B CF                        mov rcx, rdi
006F3FD5  E8 9E F6 D7 FF                  call 0x140473678
006F3FDA  0F B7 4F 30                     movzx ecx, word ptr [rdi + 0x30]
006F3FDE  66 03 4F 2C                     add cx, word ptr [rdi + 0x2c]
006F3FE2  0F BE D0                        movsx edx, al
006F3FE5  66 03 CA                        add cx, dx
006F3FE8  0F B7 F1                        movzx esi, cx
006F3FEB  EB 13                           jmp 0x1406f4000
006F3FED  48 8B CF                        mov rcx, rdi
006F3FF0  E8 E7 F1 D7 FF                  call 0x1404731dc
006F3FF5  66 03 47 30                     add ax, word ptr [rdi + 0x30]
006F3FF9  66 03 47 2C                     add ax, word ptr [rdi + 0x2c]
006F3FFD  0F B7 F0                        movzx esi, ax
006F4000  40 38 AF 8C 00 00 00            cmp byte ptr [rdi + 0x8c], bpl
006F4007  0F 85 17 F3 D7 FF               jne 0x140473324
006F400D  C7 47 74 02 00 00 00            mov dword ptr [rdi + 0x74], 2
006F4014  E9 0B F3 D7 FF                  jmp 0x140473324
006F4019  0F B7 4F 34                     movzx ecx, word ptr [rdi + 0x34]
006F401D  EB 11                           jmp 0x1406f4030
006F401F  0F B7 4F 30                     movzx ecx, word ptr [rdi + 0x30]
006F4023  EB 0B                           jmp 0x1406f4030
006F4025  48 8B CF                        mov rcx, rdi
006F4028  E8 4B F6 D7 FF                  call 0x140473678
006F402D  0F BE C8                        movsx ecx, al
006F4030  66 03 4F 24                     add cx, word ptr [rdi + 0x24]
006F4034  EB 0F                           jmp 0x1406f4045
006F4036  48 8B CF                        mov rcx, rdi
006F4039  E8 3A F6 D7 FF                  call 0x140473678
006F403E  0F BE C8                        movsx ecx, al
006F4041  66 03 4F 34                     add cx, word ptr [rdi + 0x34]
006F4045  0F B7 F1                        movzx esi, cx
006F4048  E9 D7 F2 D7 FF                  jmp 0x140473324
006F404D  48 8B CF                        mov rcx, rdi
006F4050  E8 23 F6 D7 FF                  call 0x140473678
006F4055  0F B7 4F 30                     movzx ecx, word ptr [rdi + 0x30]
006F4059  EB 0C                           jmp 0x1406f4067
006F405B  48 8B CF                        mov rcx, rdi
006F405E  E8 15 F6 D7 FF                  call 0x140473678
006F4063  0F B7 4F 34                     movzx ecx, word ptr [rdi + 0x34]
006F4067  66 03 4F 24                     add cx, word ptr [rdi + 0x24]
006F406B  0F BE D0                        movsx edx, al
006F406E  66 03 CA                        add cx, dx
006F4071  EB D2                           jmp 0x1406f4045
006F4073  83 EA 09                        sub edx, 9
006F4076  74 E3                           je 0x1406f405b
006F4078  83 EA 01                        sub edx, 1
006F407B  0F 84 51 FF FF FF               je 0x1406f3fd2
006F4081  83 EA 01                        sub edx, 1
006F4084  74 2F                           je 0x1406f40b5
006F4086  83 EA 01                        sub edx, 1
006F4089  74 19                           je 0x1406f40a4
006F408B  83 EA 01                        sub edx, 1
006F408E  74 A6                           je 0x1406f4036
006F4090  83 EA 01                        sub edx, 1
006F4093  0F 84 28 FF FF FF               je 0x1406f3fc1
006F4099  83 FA 01                        cmp edx, 1
006F409C  0F 85 82 F2 D7 FF               jne 0x140473324
006F40A2  EB 81                           jmp 0x1406f4025
006F40A4  48 8B CF                        mov rcx, rdi
006F40A7  E8 CC F5 D7 FF                  call 0x140473678
006F40AC  0F BE C8                        movsx ecx, al
006F40AF  66 03 4F 30                     add cx, word ptr [rdi + 0x30]
006F40B3  EB 90                           jmp 0x1406f4045
006F40B5  48 8B CF                        mov rcx, rdi
006F40B8  E8 BB F5 D7 FF                  call 0x140473678
006F40BD  0F B7 4F 34                     movzx ecx, word ptr [rdi + 0x34]
006F40C1  E9 18 FF FF FF                  jmp 0x1406f3fde
006F40C6  48 8B CF                        mov rcx, rdi
006F40C9  E8 0E F1 D7 FF                  call 0x1404731dc
006F40CE  66 03 47 30                     add ax, word ptr [rdi + 0x30]
006F40D2  EB 46                           jmp 0x1406f411a
006F40D4  48 8B CF                        mov rcx, rdi
006F40D7  E8 00 F1 D7 FF                  call 0x1404731dc
006F40DC  E9 18 FF FF FF                  jmp 0x1406f3ff9
006F40E1  48 8B CF                        mov rcx, rdi
006F40E4  E8 F3 F0 D7 FF                  call 0x1404731dc
006F40E9  66 03 47 34                     add ax, word ptr [rdi + 0x34]
006F40ED  EB 2F                           jmp 0x1406f411e
006F40EF  48 8B CF                        mov rcx, rdi
006F40F2  E8 E5 F0 D7 FF                  call 0x1404731dc
006F40F7  66 03 47 30                     add ax, word ptr [rdi + 0x30]
006F40FB  EB 21                           jmp 0x1406f411e
006F40FD  48 8B CF                        mov rcx, rdi
006F4100  E8 D7 F0 D7 FF                  call 0x1404731dc
006F4105  66 03 47 34                     add ax, word ptr [rdi + 0x34]
006F4109  E9 EB FE FF FF                  jmp 0x1406f3ff9
006F410E  48 8B CF                        mov rcx, rdi
006F4111  E8 C6 F0 D7 FF                  call 0x1404731dc
006F4116  66 03 47 34                     add ax, word ptr [rdi + 0x34]
006F411A  66 03 47 24                     add ax, word ptr [rdi + 0x24]
006F411E  0F B7 F0                        movzx esi, ax
006F4121  E9 FE F1 D7 FF                  jmp 0x140473324
006F4126  44 8B 47 74                     mov r8d, dword ptr [rdi + 0x74]
006F412A  42 0F B7 54 47 44               movzx edx, word ptr [rdi + r8*2 + 0x44]
006F4130  3B F2                           cmp esi, edx
006F4132  77 23                           ja 0x1406f4157
006F4134  8B 4F 78                        mov ecx, dword ptr [rdi + 0x78]
006F4137  03 CE                           add ecx, esi
006F4139  3B CA                           cmp ecx, edx
006F413B  77 1A                           ja 0x1406f4157
006F413D  89 B7 80 00 00 00               mov dword ptr [rdi + 0x80], esi
006F4143  0F B7 D6                        movzx edx, si
006F4146  42 0F B7 4C 47 38               movzx ecx, word ptr [rdi + r8*2 + 0x38]
006F414C  E8 6F F5 D7 FF                  call 0x1404736c0
006F4151  90                              nop
006F4152  E9 68 F1 D7 FF                  jmp 0x1404732bf
006F4157  48 8D 8F A0 00 00 00            lea rcx, [rdi + 0xa0]
006F415E  BA 0E 00 00 00                  mov edx, 0xe
006F4163  E8 88 94 E0 FF                  call 0x1404fd5f0
006F4168  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F3DB6(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsi;

    if (condition_is_equal) goto loc_006F3E4A;
    if (a2 > 8) goto loc_006F3E5C;
    if (a2 == 8) goto loc_006F3E3D;
    if (a2 == 0) goto loc_006F3E35;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_006F3E2D;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_006F3E25;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_006F3E1D;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_006F3E0C;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_006F3E02;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_006F3DFA;
loc_006F3DFA:
loc_006F3E02:
    result = XmGetLongImmediate(v_rdi, a2, a3, a4);
    goto loc_006F3E16;
loc_006F3E0C:
    result = XmEvaluateIndexSpecifier(v_rdi, (unsigned int)((unsigned int)(v_rdi)), a3, a4);
loc_006F3E16:
loc_006F3E1D:
loc_006F3E25:
loc_006F3E2D:
loc_006F3E35:
loc_006F3E3D:
    result = XmGetCodeByte(v_rdi, (unsigned int)((unsigned int)(v_rdi)), a3, a4);
    goto loc_006F3E54;
loc_006F3E4A:
    result = XmGetLongImmediate(v_rdi, (unsigned int)((unsigned int)(v_rdi)), a3, a4);
loc_006F3E54:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) + (*(unsigned int *)(v_rdi + 24)));
loc_006F3E5C:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (9));
    if (condition_is_equal) goto loc_006F3F26;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_006F3F07;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_006F3EE8;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_006F3E0C;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_006F3EC9;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_006F3EAA;
    result = XmGetCodeByte(v_rdi, a2, a3, a4);
    goto loc_006F3EA2;
loc_006F3EA2:
    v_rsi = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(v_rdi + 52)));
loc_006F3EAA:
    result = XmGetCodeByte(v_rdi, a2, a3, a4);
    goto loc_006F3EC1;
loc_006F3EC1:
    v_rsi = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(v_rdi + 48)));
loc_006F3EC9:
    result = XmGetCodeByte(v_rdi, a2, a3, a4);
    goto loc_006F3EE0;
loc_006F3EE0:
    v_rsi = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(v_rdi + 44)));
    goto loc_006F4000;
loc_006F3EE8:
    result = XmGetCodeByte(v_rdi, a2, a3, a4);
    goto loc_006F3EFF;
loc_006F3EFF:
    v_rsi = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(v_rdi + 36)));
loc_006F3F07:
    result = XmGetCodeByte(v_rdi, a2, a3, a4);
    goto loc_006F3F1E;
loc_006F3F1E:
    v_rsi = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(v_rdi + 32)));
loc_006F3F26:
    result = XmGetCodeByte(v_rdi, a2, a3, a4);
    goto loc_006F3F3D;
loc_006F3F3D:
    v_rsi = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(v_rdi + 28)));
loc_006F4000:
    *(unsigned int *)(v_rdi + 116) = 2;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006F3DB6(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsi;

    if (condition_is_equal) goto loc_006F3E4A;
    if (Arg2 > 8) goto loc_006F3E5C;
    if (Arg2 == 8) goto loc_006F3E3D;
    if (Arg2 == 0) goto loc_006F3E35;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_006F3E2D;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_006F3E25;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_006F3E1D;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_006F3E0C;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_006F3E02;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_006F3DFA;
loc_006F3DFA:
loc_006F3E02:
    result = XmGetLongImmediate(local_rdi, Arg2, a3, a4);
    goto loc_006F3E16;
loc_006F3E0C:
    result = XmEvaluateIndexSpecifier(local_rdi, (uint32_t)((uint32_t)(local_rdi)), a3, a4);
loc_006F3E16:
loc_006F3E1D:
loc_006F3E25:
loc_006F3E2D:
loc_006F3E35:
loc_006F3E3D:
    result = XmGetCodeByte(local_rdi, (uint32_t)((uint32_t)(local_rdi)), a3, a4);
    goto loc_006F3E54;
loc_006F3E4A:
    result = XmGetLongImmediate(local_rdi, (uint32_t)((uint32_t)(local_rdi)), a3, a4);
loc_006F3E54:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) + (*(uint32_t *)(local_rdi + 0x18)));
loc_006F3E5C:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (9));
    if (condition_is_equal) goto loc_006F3F26;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_006F3F07;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_006F3EE8;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_006F3E0C;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_006F3EC9;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_006F3EAA;
    result = XmGetCodeByte(local_rdi, Arg2, a3, a4);
    goto loc_006F3EA2;
loc_006F3EA2:
    local_rsi = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(local_rdi + 0x34)));
loc_006F3EAA:
    result = XmGetCodeByte(local_rdi, Arg2, a3, a4);
    goto loc_006F3EC1;
loc_006F3EC1:
    local_rsi = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(local_rdi + 0x30)));
loc_006F3EC9:
    result = XmGetCodeByte(local_rdi, Arg2, a3, a4);
    goto loc_006F3EE0;
loc_006F3EE0:
    local_rsi = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(local_rdi + 0x2C)));
    goto loc_006F4000;
loc_006F3EE8:
    result = XmGetCodeByte(local_rdi, Arg2, a3, a4);
    goto loc_006F3EFF;
loc_006F3EFF:
    local_rsi = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(local_rdi + 0x24)));
loc_006F3F07:
    result = XmGetCodeByte(local_rdi, Arg2, a3, a4);
    goto loc_006F3F1E;
loc_006F3F1E:
    local_rsi = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(local_rdi + 0x20)));
loc_006F3F26:
    result = XmGetCodeByte(local_rdi, Arg2, a3, a4);
    goto loc_006F3F3D;
loc_006F3F3D:
    local_rsi = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(local_rdi + 0x1C)));
loc_006F4000:
    *(uint32_t *)(local_rdi + 0x74) = 2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F3DB6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
