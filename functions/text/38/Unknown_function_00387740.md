# sub_00387740

- RVA: `0x00387740`–`0x00387BC2` (길이 `1,154` bytes)
- VA: `0x0000000140387740`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007FD90`
- 디코드: `303`개 명령, `1,154/1,154` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003877ED` → [FsRtlAddEntry](FsRtlAddEntry_function_00387BE0.md) (function, `0x00387BE0`)
- `0x003878DC` → [FsRtlAddEntry](FsRtlAddEntry_function_00387BE0.md) (function, `0x00387BE0`)
- `0x00387952` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0038796E` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0038797E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x003879A3` → [ExFreeToPagedLookasideList](ExFreeToPagedLookasideList_function_00387D30.md) (function, `0x00387D30`)
- `0x003879D4` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x00387AA2` → [ExFreeToNPagedLookasideList](ExFreeToNPagedLookasideList_function_0038D9D0.md) (function, `0x0038D9D0`)
- `0x00387ADB` → [FsRtlAddEntry](FsRtlAddEntry_function_00387BE0.md) (function, `0x00387BE0`)
- `0x00387B4F` → [FsRtlAddEntry](FsRtlAddEntry_function_00387BE0.md) (function, `0x00387BE0`)
- `0x00387B85` → [FsRtlAddEntry](FsRtlAddEntry_function_00387BE0.md) (function, `0x00387BE0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0038799C` → RVA `0x00E11E00` (`.data`; read)
- `0x00387A9B` → RVA `0x00E11D80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00387952` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`.text` → `POOLCODE`)
  - `0x0038797E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **29**
  - `0x0038775F` → [sub_003875A6 + 0x17A](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387773` → [sub_003875A6 + 0x106](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x003877AF` → [sub_003875A6 + 0x106](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x003877BC` → [sub_003875A6 + 0xE6](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x003877C6` → [sub_003875A6 + 0xE6](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x003877DB` → [sub_003875A6 + 0x119](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x0038782A` → [sub_003875A6 + 0x16D](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387831` → [sub_003875A6 + 0x9A](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x0038790E` → [sub_003875A6 + 0x178](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387922` → [sub_003875A6 + 0x17A](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387989` → [sub_003875A6 + 0x12C](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x003879AE` → [sub_003875A6 + 0x12C](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x003879B7` → [sub_003875A6 + 0x101](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x003879C2` → [sub_003875A6 + 0x108](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x003879EB` → [sub_003875A6 + 0x111](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387A15` → [sub_003875A6 + 0x111](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387A28` → [sub_003875A6 + 0x178](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387A96` → [sub_003875A6 + 0x178](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387AAD` → [sub_003875A6 + 0x12C](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387AB4` → [sub_003875A6 + 0xD2](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387AF9` → [sub_003875A6 + 0x178](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387B17` → [sub_006E4E52](../6E/Unknown_function_006E4E52.md) (`tail-transfer`)
  - `0x00387B20` → [sub_006E4E52 + 0x7](../6E/Unknown_function_006E4E52.md) (`tail-transfer`)
  - `0x00387B30` → [sub_003875A6 + 0xC4](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387B40` → [sub_006E4E52 + 0x15](../6E/Unknown_function_006E4E52.md) (`tail-transfer`)
  - `0x00387B6B` → [sub_003875A6 + 0x178](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387BAC` → [sub_003875A6 + 0x178](Unknown_function_003875A6.md) (`tail-transfer`)
  - `0x00387BB5` → [sub_006E4E52 + 0x1D](../6E/Unknown_function_006E4E52.md) (`tail-transfer`)
  - `0x00387BBD` → [sub_006E4E52 + 0x3F](../6E/Unknown_function_006E4E52.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00387740  4C 8D 34 F5 00 00 00 00         lea r14, [rsi*8]
00387748  42 8D 2C 2B                     lea ebp, [rbx + r13]
0038774C  8D 55 FF                        lea edx, [rbp - 1]
0038774F  47 39 64 33 04                  cmp dword ptr [r11 + r14 + 4], r12d
00387754  0F 84 35 01 00 00               je 0x14038788f
0038775A  B8 01 00 00 C0                  mov eax, 0xc0000001
0038775F  EB BF                           jmp 0x140387720
00387761  44 8B DE                        mov r11d, esi
00387764  41 8D 77 FF                     lea esi, [r15 - 1]
00387768  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00387770  44 3B DE                        cmp r11d, esi
00387773  0F 8F 33 FF FF FF               jg 0x1403876ac
00387779  42 8D 04 1E                     lea eax, [rsi + r11]
0038777D  99                              cdq
0038777E  2B C2                           sub eax, edx
00387780  D1 F8                           sar eax, 1
00387782  44 8B C8                        mov r9d, eax
00387785  74 0A                           je 0x140387791
00387787  49 63 D1                        movsxd rdx, r9d
0038778A  41 3B 6C D2 F8                  cmp ebp, dword ptr [r10 + rdx*8 - 8]
0038778F  72 13                           jb 0x1403877a4
00387791  49 63 C1                        movsxd rax, r9d
00387794  41 8B 14 C2                     mov edx, dword ptr [r10 + rax*8]
00387798  FF CA                           dec edx
0038779A  3B EA                           cmp ebp, edx
0038779C  76 0B                           jbe 0x1403877a9
0038779E  45 8D 59 01                     lea r11d, [r9 + 1]
003877A2  EB CC                           jmp 0x140387770
003877A4  8D 70 FF                        lea esi, [rax - 1]
003877A7  EB C7                           jmp 0x140387770
003877A9  41 8D 41 FF                     lea eax, [r9 - 1]
003877AD  3B C8                           cmp ecx, eax
003877AF  0F 85 F7 FE FF FF               jne 0x1403876ac
003877B5  33 ED                           xor ebp, ebp
003877B7  8B CD                           mov ecx, ebp
003877B9  45 85 C9                        test r9d, r9d
003877BC  0F 84 CA FE FF FF               je 0x14038768c
003877C2  41 8B 0C C2                     mov ecx, dword ptr [r10 + rax*8]
003877C6  E9 C1 FE FF FF                  jmp 0x14038768c
003877CB  45 85 FF                        test r15d, r15d
003877CE  74 11                           je 0x1403877e1
003877D0  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003877D4  41 8D 4F FF                     lea ecx, [r15 - 1]
003877D8  39 1C C8                        cmp dword ptr [rax + rcx*8], ebx
003877DB  0F 84 DE FE FF FF               je 0x1403876bf
003877E1  41 B8 02 00 00 00               mov r8d, 2
003877E7  41 8B D7                        mov edx, r15d
003877EA  48 8B CF                        mov rcx, rdi
003877ED  E8 EE 03 00 00                  call 0x140387be0
003877F2  84 C0                           test al, al
003877F4  0F 84 23 01 00 00               je 0x14038791d
003877FA  41 8B C7                        mov eax, r15d
003877FD  48 8D 0C C5 00 00 00 00         lea rcx, [rax*8]
00387805  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387809  44 89 64 08 04                  mov dword ptr [rax + rcx + 4], r12d
0038780E  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387812  89 1C 01                        mov dword ptr [rcx + rax], ebx
00387815  41 8D 47 01                     lea eax, [r15 + 1]
00387819  48 8D 14 C5 00 00 00 00         lea rdx, [rax*8]
00387821  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387825  44 89 74 10 04                  mov dword ptr [rax + rdx + 4], r14d
0038782A  E9 E4 FE FF FF                  jmp 0x140387713
0038782F  8B D6                           mov edx, esi
00387831  E9 0A FE FF FF                  jmp 0x140387640
00387836  4C 8B 5F 10                     mov r11, qword ptr [rdi + 0x10]
0038783A  41 FF CF                        dec r15d
0038783D  4D 8B C3                        mov r8, r11
00387840  43 39 1C FB                     cmp dword ptr [r11 + r15*8], ebx
00387844  0F 86 92 01 00 00               jbe 0x1403879dc
0038784A  44 8B 54 24 60                  mov r10d, dword ptr [rsp + 0x60]
0038784F  44 8B CE                        mov r9d, esi
00387852  45 3B CA                        cmp r9d, r10d
00387855  0F 8F 7F 01 00 00               jg 0x1403879da
0038785B  43 8D 04 0A                     lea eax, [r10 + r9]
0038785F  99                              cdq
00387860  2B C2                           sub eax, edx
00387862  D1 F8                           sar eax, 1
00387864  8B F0                           mov esi, eax
00387866  74 0A                           je 0x140387872
00387868  48 63 C6                        movsxd rax, esi
0038786B  41 3B 5C C3 F8                  cmp ebx, dword ptr [r11 + rax*8 - 8]
00387870  72 17                           jb 0x140387889
00387872  48 63 C6                        movsxd rax, esi
00387875  41 8B 0C C3                     mov ecx, dword ptr [r11 + rax*8]
00387879  FF C9                           dec ecx
0038787B  3B D9                           cmp ebx, ecx
0038787D  0F 86 BD FE FF FF               jbe 0x140387740
00387883  44 8D 4E 01                     lea r9d, [rsi + 1]
00387887  EB C9                           jmp 0x140387852
00387889  44 8D 56 FF                     lea r10d, [rsi - 1]
0038788D  EB C3                           jmp 0x140387852
0038788F  44 8D 4E FF                     lea r9d, [rsi - 1]
00387893  85 F6                           test esi, esi
00387895  74 0A                           je 0x1403878a1
00387897  43 39 1C CB                     cmp dword ptr [r11 + r9*8], ebx
0038789B  0F 87 B9 FE FF FF               ja 0x14038775a
003878A1  47 8B 04 33                     mov r8d, dword ptr [r11 + r14]
003878A5  41 FF C8                        dec r8d
003878A8  41 3B D0                        cmp edx, r8d
003878AB  0F 87 A9 FE FF FF               ja 0x14038775a
003878B1  45 33 D2                        xor r10d, r10d
003878B4  85 F6                           test esi, esi
003878B6  0F 84 0B 01 00 00               je 0x1403879c7
003878BC  43 8B 0C CB                     mov ecx, dword ptr [r11 + r9*8]
003878C0  3B CB                           cmp ecx, ebx
003878C2  0F 83 69 01 00 00               jae 0x140387a31
003878C8  41 3B D0                        cmp edx, r8d
003878CB  0F 83 60 01 00 00               jae 0x140387a31
003878D1  41 B8 02 00 00 00               mov r8d, 2
003878D7  8B D6                           mov edx, esi
003878D9  48 8B CF                        mov rcx, rdi
003878DC  E8 FF 02 00 00                  call 0x140387be0
003878E1  84 C0                           test al, al
003878E3  74 38                           je 0x14038791d
003878E5  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003878E9  8D 4E 01                        lea ecx, [rsi + 1]
003878EC  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
003878F1  46 89 64 30 04                  mov dword ptr [rax + r14 + 4], r12d
003878F6  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003878FA  41 89 1C 06                     mov dword ptr [r14 + rax], ebx
003878FE  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387902  44 89 7C C8 04                  mov dword ptr [rax + rcx*8 + 4], r15d
00387907  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0038790B  89 2C C8                        mov dword ptr [rax + rcx*8], ebp
0038790E  E9 0B FE FF FF                  jmp 0x14038771e
00387913  F6 47 0A 01                     test byte ptr [rdi + 0xa], 1
00387917  0F 85 B2 00 00 00               jne 0x1403879cf
0038791D  B8 9A 00 00 C0                  mov eax, 0xc000009a
00387922  E9 F9 FD FF FF                  jmp 0x140387720
00387927  81 FA 00 08 00 00               cmp edx, 0x800
0038792D  8D 82 00 08 00 00               lea eax, [rdx + 0x800]
00387933  8D 0C 12                        lea ecx, [rdx + rdx]
00387936  0F 43 C8                        cmovae ecx, eax
00387939  8B C1                           mov eax, ecx
0038793B  48 C1 E0 03                     shl rax, 3
0038793F  8B E9                           mov ebp, ecx
00387941  49 3B C4                        cmp rax, r12
00387944  77 CD                           ja 0x140387913
00387946  0F B7 4F 08                     movzx ecx, word ptr [rdi + 8]
0038794A  41 B8 46 53 69 6D               mov r8d, 0x6d695346
00387950  8B D0                           mov edx, eax
00387952  E8 B9 A6 7F 00                  call 0x140b82010
00387957  48 8B F0                        mov rsi, rax
0038795A  48 85 C0                        test rax, rax
0038795D  74 B4                           je 0x140387913
0038795F  44 8B 47 04                     mov r8d, dword ptr [rdi + 4]
00387963  48 8B C8                        mov rcx, rax
00387966  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
0038796A  49 C1 E0 03                     shl r8, 3
0038796E  E8 CD EE 33 00                  call 0x1406c6840
00387973  83 3F 0F                        cmp dword ptr [rdi], 0xf
00387976  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0038797A  74 12                           je 0x14038798e
0038797C  33 D2                           xor edx, edx
0038797E  E8 ED AE 7F 00                  call 0x140b82870
00387983  48 89 77 10                     mov qword ptr [rdi + 0x10], rsi
00387987  89 2F                           mov dword ptr [rdi], ebp
00387989  E9 44 FD FF FF                  jmp 0x1403876d2
0038798E  66 83 7F 08 01                  cmp word ptr [rdi + 8], 1
00387993  48 8B D1                        mov rdx, rcx
00387996  0F 85 FF 00 00 00               jne 0x140387a9b
0038799C  48 8D 0D 5D A4 A8 00            lea rcx, [rip + 0xa8a45d]
003879A3  E8 88 03 00 00                  call 0x140387d30
003879A8  48 89 77 10                     mov qword ptr [rdi + 0x10], rsi
003879AC  89 2F                           mov dword ptr [rdi], ebp
003879AE  E9 1F FD FF FF                  jmp 0x1403876d2
003879B3  41 8B 04 C2                     mov eax, dword ptr [r10 + rax*8]
003879B7  E9 EB FC FF FF                  jmp 0x1403876a7
003879BC  41 BC FF FF FF FF               mov r12d, 0xffffffff
003879C2  E9 E7 FC FF FF                  jmp 0x1403876ae
003879C7  41 8B CA                        mov ecx, r10d
003879CA  E9 F1 FE FF FF                  jmp 0x1403878c0
003879CF  B9 9A 00 00 C0                  mov ecx, 0xc000009a
003879D4  E8 77 F0 F6 FF                  call 0x1402f6a50
003879D9  CC                              int3
003879DA  33 F6                           xor esi, esi
003879DC  44 8B 7C 24 68                  mov r15d, dword ptr [rsp + 0x68]
003879E1  41 8D 47 FF                     lea eax, [r15 - 1]
003879E5  41 8B 14 C0                     mov edx, dword ptr [r8 + rax*8]
003879E9  3B D3                           cmp edx, ebx
003879EB  0F 85 C6 FC FF FF               jne 0x1403876b7
003879F1  41 8D 4F FF                     lea ecx, [r15 - 1]
003879F5  45 8B 4C C8 04                  mov r9d, dword ptr [r8 + rcx*8 + 4]
003879FA  45 3B CC                        cmp r9d, r12d
003879FD  74 13                           je 0x140387a12
003879FF  85 C9                           test ecx, ecx
00387A01  74 2A                           je 0x140387a2d
00387A03  41 8D 47 FE                     lea eax, [r15 - 2]
00387A07  41 8B 04 C0                     mov eax, dword ptr [r8 + rax*8]
00387A0B  41 8B F1                        mov esi, r9d
00387A0E  2B F0                           sub esi, eax
00387A10  03 F2                           add esi, edx
00387A12  41 3B F6                        cmp esi, r14d
00387A15  0F 85 9C FC FF FF               jne 0x1403876b7
00387A1B  8B 47 04                        mov eax, dword ptr [rdi + 4]
00387A1E  42 8D 0C 2A                     lea ecx, [rdx + r13]
00387A22  FF C8                           dec eax
00387A24  41 89 0C C0                     mov dword ptr [r8 + rax*8], ecx
00387A28  E9 F1 FC FF FF                  jmp 0x14038771e
00387A2D  8B C6                           mov eax, esi
00387A2F  EB DA                           jmp 0x140387a0b
00387A31  4A 8D 04 CD 00 00 00 00         lea rax, [r9*8]
00387A39  85 F6                           test esi, esi
00387A3B  0F 85 F4 00 00 00               jne 0x140387b35
00387A41  41 8B CA                        mov ecx, r10d
00387A44  3B CB                           cmp ecx, ebx
00387A46  74 71                           je 0x140387ab9
00387A48  85 F6                           test esi, esi
00387A4A  0F 85 AE 00 00 00               jne 0x140387afe
00387A50  41 8B CA                        mov ecx, r10d
00387A53  4D 8D 14 03                     lea r10, [r11 + rax]
00387A57  3B CB                           cmp ecx, ebx
00387A59  0F 83 52 01 00 00               jae 0x140387bb1
00387A5F  41 3B D0                        cmp edx, r8d
00387A62  0F 85 49 01 00 00               jne 0x140387bb1
00387A68  8D 6E 01                        lea ebp, [rsi + 1]
00387A6B  3B 74 24 60                     cmp esi, dword ptr [rsp + 0x60]
00387A6F  0F 82 FB 00 00 00               jb 0x140387b70
00387A75  41 8B CC                        mov ecx, r12d
00387A78  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00387A7D  43 8D 04 2F                     lea eax, [r15 + r13]
00387A81  3B C8                           cmp ecx, eax
00387A83  0F 85 F1 00 00 00               jne 0x140387b7a
00387A89  43 89 1C 33                     mov dword ptr [r11 + r14], ebx
00387A8D  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387A91  44 89 7C E8 04                  mov dword ptr [rax + rbp*8 + 4], r15d
00387A96  E9 83 FC FF FF                  jmp 0x14038771e
00387A9B  48 8D 0D DE A2 A8 00            lea rcx, [rip + 0xa8a2de]
00387AA2  E8 29 5F 00 00                  call 0x14038d9d0
00387AA7  48 89 77 10                     mov qword ptr [rdi + 0x10], rsi
00387AAB  89 2F                           mov dword ptr [rdi], ebp
00387AAD  E9 20 FC FF FF                  jmp 0x1403876d2
00387AB2  8B C6                           mov eax, esi
00387AB4  E9 BF FB FF FF                  jmp 0x140387678
00387AB9  41 3B D0                        cmp edx, r8d
00387ABC  73 8A                           jae 0x140387a48
00387ABE  49 8D 14 03                     lea rdx, [r11 + rax]
00387AC2  85 F6                           test esi, esi
00387AC4  75 45                           jne 0x140387b0b
00387AC6  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00387ACB  45 3B D7                        cmp r10d, r15d
00387ACE  74 6E                           je 0x140387b3e
00387AD0  41 B8 01 00 00 00               mov r8d, 1
00387AD6  8B D6                           mov edx, esi
00387AD8  48 8B CF                        mov rcx, rdi
00387ADB  E8 00 01 00 00                  call 0x140387be0
00387AE0  84 C0                           test al, al
00387AE2  0F 84 35 FE FF FF               je 0x14038791d
00387AE8  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387AEC  46 89 7C 30 04                  mov dword ptr [rax + r14 + 4], r15d
00387AF1  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387AF5  41 89 2C 06                     mov dword ptr [r14 + rax], ebp
00387AF9  E9 20 FC FF FF                  jmp 0x14038771e
00387AFE  41 8B 0C 03                     mov ecx, dword ptr [r11 + rax]
00387B02  4D 8D 14 03                     lea r10, [r11 + rax]
00387B06  E9 4C FF FF FF                  jmp 0x140387a57
00387B0B  44 8B 42 04                     mov r8d, dword ptr [rdx + 4]
00387B0F  45 3B C4                        cmp r8d, r12d
00387B12  74 B2                           je 0x140387ac6
00387B14  45 85 C9                        test r9d, r9d
00387B17  0F 85 35 D3 35 00               jne 0x1406e4e52
00387B1D  41 8B C2                        mov eax, r10d
00387B20  E9 34 D3 35 00                  jmp 0x1406e4e59
00387B25  8D 41 01                        lea eax, [rcx + 1]
00387B28  41 8B DB                        mov ebx, r11d
00387B2B  85 C0                           test eax, eax
00387B2D  0F 44 DE                        cmove ebx, esi
00387B30  E9 35 FB FF FF                  jmp 0x14038766a
00387B35  41 8B 0C 03                     mov ecx, dword ptr [r11 + rax]
00387B39  E9 06 FF FF FF                  jmp 0x140387a44
00387B3E  85 F6                           test esi, esi
00387B40  0F 85 21 D3 35 00               jne 0x1406e4e67
00387B46  33 D2                           xor edx, edx
00387B48  44 8D 46 01                     lea r8d, [rsi + 1]
00387B4C  48 8B CF                        mov rcx, rdi
00387B4F  E8 8C 00 00 00                  call 0x140387be0
00387B54  84 C0                           test al, al
00387B56  0F 84 C1 FD FF FF               je 0x14038791d
00387B5C  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387B60  44 89 78 04                     mov dword ptr [rax + 4], r15d
00387B64  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387B68  44 89 28                        mov dword ptr [rax], r13d
00387B6B  E9 AE FB FF FF                  jmp 0x14038771e
00387B70  41 8B 4C EB 04                  mov ecx, dword ptr [r11 + rbp*8 + 4]
00387B75  E9 FE FE FF FF                  jmp 0x140387a78
00387B7A  41 B8 01 00 00 00               mov r8d, 1
00387B80  8B D6                           mov edx, esi
00387B82  48 8B CF                        mov rcx, rdi
00387B85  E8 56 00 00 00                  call 0x140387be0
00387B8A  84 C0                           test al, al
00387B8C  0F 84 8B FD FF FF               je 0x14038791d
00387B92  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387B96  46 89 64 30 04                  mov dword ptr [rax + r14 + 4], r12d
00387B9B  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387B9F  41 89 1C 06                     mov dword ptr [r14 + rax], ebx
00387BA3  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387BA7  44 89 7C E8 04                  mov dword ptr [rax + rbp*8 + 4], r15d
00387BAC  E9 6D FB FF FF                  jmp 0x14038771e
00387BB1  33 ED                           xor ebp, ebp
00387BB3  85 F6                           test esi, esi
00387BB5  0F 85 B4 D2 35 00               jne 0x1406e4e6f
00387BBB  8B D5                           mov edx, ebp
00387BBD  E9 CF D2 35 00                  jmp 0x1406e4e91
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00387740(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, unsigned int a12, __int64 a13, __int64 a14)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbp;
    unsigned int v_stack_p60;
    unsigned int v_stack_p68;

    if ((*(unsigned int *)(v_r11 + v_rsi * 8 * 1 + 4)) == ((unsigned int)(v_r12))) goto loc_0038788F;
loc_0038775A:
loc_0038788F:
    if ((unsigned int)(v_rsi) == 0) goto loc_003878A1;
    if ((*(unsigned int *)(v_r11 + v_rsi - 1 * 8)) > ((unsigned int)(v_rbx))) goto loc_0038775A;
loc_003878A1:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r11 + v_rsi * 8 * 1))) - 1);
    if (((unsigned int)(v_rbx + v_r13 * 1 - 1)) > ((unsigned int)(a3))) goto loc_0038775A;
    v_r10 = 0;
    if ((unsigned int)(v_rsi) == 0) goto loc_003879C7;
loc_003878C0:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + v_rsi - 1 * 8)))) >= ((unsigned int)(v_rbx))) goto loc_00387A31;
    if (((unsigned int)(v_rbx + v_r13 * 1 - 1)) >= ((unsigned int)(a3))) goto loc_00387A31;
    result = FsRtlAddEntry(v_rdi, (unsigned int)((unsigned int)(v_rsi)), 2, v_rsi - 1);
    if ((unsigned __int8)(result) == 0) goto loc_0038791D;
    *(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16) + v_rsi * 8 * 1 + 4) = (unsigned int)(v_r12);
    *(unsigned int *)(v_rsi * 8 + *(unsigned __int64 *)(v_rdi + 16) * 1) = (unsigned int)(v_rbx);
    *(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16) + v_rsi + 1 * 8 + 4) = (unsigned int)(a14);
    *(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16) + v_rsi + 1 * 8) = (unsigned int)(v_rbx + v_r13 * 1);
loc_0038791D:
loc_003879C7:
    goto loc_003878C0;
loc_00387A31:
    if ((unsigned int)(v_rsi) != 0) goto loc_00387B35;
loc_00387A44:
    if (0 == ((unsigned int)(v_rbx))) goto loc_00387AB9;
loc_00387A48:
    if ((unsigned int)(v_rsi) != 0) goto loc_00387AFE;
loc_00387A57:
    if (0 >= ((unsigned int)(v_rbx))) goto loc_00387BB1;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) != 2) goto loc_00387BB1;
    if (((unsigned int)(v_rsi)) < a12) goto loc_00387B70;
loc_00387A78:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r12)))) != ((unsigned int)(a14 + v_r13 * 1))) goto loc_00387B7A;
    *(unsigned int *)(v_r11 + v_rsi * 8 * 1) = (unsigned int)(v_rbx);
    *(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16) + v_rsi + 1 * 8 + 4) = (unsigned int)(a14);
loc_00387AB9:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) >= 2) goto loc_00387A48;
    if ((unsigned int)(v_rsi) != 0) goto loc_00387B0B;
loc_00387AC6:
    if (((unsigned int)(v_r11 + v_rsi - 1 * 8 * 1)) == ((unsigned int)(a14))) goto loc_00387B3E;
    result = FsRtlAddEntry(v_rdi, (unsigned int)((unsigned int)(v_rsi)), 1, v_rsi - 1);
    if ((unsigned __int8)(result) == 0) goto loc_0038791D;
    *(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16) + v_rsi * 8 * 1 + 4) = (unsigned int)(a14);
    *(unsigned int *)(v_rsi * 8 + *(unsigned __int64 *)(v_rdi + 16) * 1) = (unsigned int)(v_rsi + 1);
loc_00387AFE:
    goto loc_00387A57;
loc_00387B0B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_rsi)) + 4)))) == ((unsigned int)(v_r12))) goto loc_00387AC6;
loc_00387B35:
    goto loc_00387A44;
loc_00387B3E:
    a2 = 0;
    result = FsRtlAddEntry(v_rdi, a2, v_rsi + 1, v_rsi - 1);
    if ((unsigned __int8)(result) == 0) goto loc_0038791D;
    *(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16) + 4) = (unsigned int)(a14);
    *(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16)) = (unsigned int)(v_r13);
loc_00387B70:
    goto loc_00387A78;
loc_00387B7A:
    result = FsRtlAddEntry(v_rdi, (unsigned int)((unsigned int)(v_rsi)), 1, v_rsi - 1);
    if ((unsigned __int8)(result) == 0) goto loc_0038791D;
    *(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16) + v_rsi * 8 * 1 + 4) = (unsigned int)(v_r12);
    *(unsigned int *)(v_rsi * 8 + *(unsigned __int64 *)(v_rdi + 16) * 1) = (unsigned int)(v_rbx);
    *(unsigned int *)(*(unsigned __int64 *)(v_rdi + 16) + v_rsi + 1 * 8 + 4) = (unsigned int)(a14);
loc_00387BB1:
    v_rbp = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00387740(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint32_t Arg12, uint64_t Arg13, void *Arg14)
{
    uint8_t *arg14 = (uint8_t *)Arg14;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbp;
    uint32_t v_stack_p60;
    uint32_t v_stack_p68;

    if ((*(uint32_t *)(local_r11 + local_rsi * 8 * 1 + 0x4)) == ((uint32_t)(local_r12))) goto loc_0038788F;
loc_0038775A:
loc_0038788F:
    if ((uint32_t)(local_rsi) == 0) goto loc_003878A1;
    if ((*(uint32_t *)(local_r11 + local_rsi - 0x1 * 8)) > ((uint32_t)(local_rbx))) goto loc_0038775A;
loc_003878A1:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r11 + local_rsi * 8 * 1))) - 1);
    if (((uint32_t)(local_rbx + local_r13 * 1 - 1)) > ((uint32_t)(Arg3))) goto loc_0038775A;
    local_r10 = 0;
    if ((uint32_t)(local_rsi) == 0) goto loc_003879C7;
loc_003878C0:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + local_rsi - 0x1 * 8)))) >= ((uint32_t)(local_rbx))) goto loc_00387A31;
    if (((uint32_t)(local_rbx + local_r13 * 1 - 1)) >= ((uint32_t)(Arg3))) goto loc_00387A31;
    result = FsRtlAddEntry(local_rdi, (uint32_t)((uint32_t)(local_rsi)), 2, local_rsi - 1);
    if ((uint8_t)(result) == 0) goto loc_0038791D;
    *(uint32_t *)(*(uint64_t *)(local_rdi + 0x10) + local_rsi * 8 * 1 + 0x4) = (uint32_t)(local_r12);
    *(uint32_t *)(local_rsi * 8 + *(uint64_t *)(local_rdi + 0x10) * 1) = (uint32_t)(local_rbx);
    *(uint32_t *)(*(uint64_t *)(local_rdi + 0x10) + local_rsi + 0x1 * 8 + 0x4) = (uint32_t)(Arg14);
    *(uint32_t *)(*(uint64_t *)(local_rdi + 0x10) + local_rsi + 0x1 * 8) = (uint32_t)(local_rbx + local_r13 * 1);
loc_0038791D:
loc_003879C7:
    goto loc_003878C0;
loc_00387A31:
    if ((uint32_t)(local_rsi) != 0) goto loc_00387B35;
loc_00387A44:
    if (0 == ((uint32_t)(local_rbx))) goto loc_00387AB9;
loc_00387A48:
    if ((uint32_t)(local_rsi) != 0) goto loc_00387AFE;
loc_00387A57:
    if (0 >= ((uint32_t)(local_rbx))) goto loc_00387BB1;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) != 2) goto loc_00387BB1;
    if (((uint32_t)(local_rsi)) < Arg12) goto loc_00387B70;
loc_00387A78:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r12)))) != ((uint32_t)(Arg14 + local_r13 * 1))) goto loc_00387B7A;
    *(uint32_t *)(local_r11 + local_rsi * 8 * 1) = (uint32_t)(local_rbx);
    *(uint32_t *)(*(uint64_t *)(local_rdi + 0x10) + local_rsi + 0x1 * 8 + 0x4) = (uint32_t)(Arg14);
loc_00387AB9:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) >= 2) goto loc_00387A48;
    if ((uint32_t)(local_rsi) != 0) goto loc_00387B0B;
loc_00387AC6:
    if (((uint32_t)(local_r11 + local_rsi - 1 * 8 * 1)) == ((uint32_t)(Arg14))) goto loc_00387B3E;
    result = FsRtlAddEntry(local_rdi, (uint32_t)((uint32_t)(local_rsi)), 1, local_rsi - 1);
    if ((uint8_t)(result) == 0) goto loc_0038791D;
    *(uint32_t *)(*(uint64_t *)(local_rdi + 0x10) + local_rsi * 8 * 1 + 0x4) = (uint32_t)(Arg14);
    *(uint32_t *)(local_rsi * 8 + *(uint64_t *)(local_rdi + 0x10) * 1) = (uint32_t)(local_rsi + 1);
loc_00387AFE:
    goto loc_00387A57;
loc_00387B0B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_rsi)) + 0x4)))) == ((uint32_t)(local_r12))) goto loc_00387AC6;
loc_00387B35:
    goto loc_00387A44;
loc_00387B3E:
    Arg2 = 0;
    result = FsRtlAddEntry(local_rdi, Arg2, local_rsi + 1, local_rsi - 1);
    if ((uint8_t)(result) == 0) goto loc_0038791D;
    *(uint32_t *)(*(uint64_t *)(local_rdi + 0x10) + 0x4) = (uint32_t)(Arg14);
    *(uint32_t *)(*(uint64_t *)(local_rdi + 0x10)) = (uint32_t)(local_r13);
loc_00387B70:
    goto loc_00387A78;
loc_00387B7A:
    result = FsRtlAddEntry(local_rdi, (uint32_t)((uint32_t)(local_rsi)), 1, local_rsi - 1);
    if ((uint8_t)(result) == 0) goto loc_0038791D;
    *(uint32_t *)(*(uint64_t *)(local_rdi + 0x10) + local_rsi * 8 * 1 + 0x4) = (uint32_t)(local_r12);
    *(uint32_t *)(local_rsi * 8 + *(uint64_t *)(local_rdi + 0x10) * 1) = (uint32_t)(local_rbx);
    *(uint32_t *)(*(uint64_t *)(local_rdi + 0x10) + local_rsi + 0x1 * 8 + 0x4) = (uint32_t)(Arg14);
loc_00387BB1:
    local_rbp = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg14` | `+ 0x0 + r13*1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00387740&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
