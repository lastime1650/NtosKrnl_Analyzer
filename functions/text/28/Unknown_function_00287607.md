# sub_00287607

- RVA: `0x00287607`–`0x00287A3A` (길이 `1,075` bytes)
- VA: `0x0000000140287607`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00066D00`
- 디코드: `246`개 명령, `1,075/1,075` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00287618` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002876FB` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x00287784` → [MiAcquirePageListLock](../27/MiAcquirePageListLock_function_0027C450.md) (function, `0x0027C450`)
- `0x002877B0` → [MiReplaceStandbyLookaside](../33/MiReplaceStandbyLookaside_function_003397D0.md) (function, `0x003397D0`)
- `0x0028780C` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x00287851` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00287621` → RVA `0x00E30088` (`.data`; read)
- `0x0028769F` → RVA `0x00E35C00` (`.data`; read)
- `0x002876BA` → RVA `0x00E3CBE6` (`.data`; read)
- `0x002876C3` → RVA `0x00E3D240` (`.data`; read)
- `0x00287971` → RVA `0x00E3014C` (`.data`; read)
- `0x002879FF` → RVA `0x00FC6B06` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **24**
  - `0x00287657` → [sub_00287A62](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x00287671` → [sub_00287E84 + 0x133](Unknown_function_00287E84.md) (`tail-transfer`)
  - `0x002876B4` → [sub_00287A62 + 0x1C7](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x002876D7` → [sub_00287E04 + 0x1B](Unknown_function_00287E04.md) (`tail-transfer`)
  - `0x002876E6` → [sub_00287A62 + 0xA6](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x002876F2` → [sub_00287A62 + 0x1CF](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x00287743` → [sub_00287E84](Unknown_function_00287E84.md) (`tail-transfer`)
  - `0x00287755` → [sub_00287E04](Unknown_function_00287E04.md) (`tail-transfer`)
  - `0x002877B8` → [sub_00287A62 + 0x1FF](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x00287814` → [sub_00287E84 + 0x1EC](Unknown_function_00287E84.md) (`tail-transfer`)
  - `0x00287859` → [sub_00287E84 + 0x21C](Unknown_function_00287E84.md) (`tail-transfer`)
  - `0x0028786E` → [sub_00287E84 + 0xDA](Unknown_function_00287E84.md) (`tail-transfer`)
  - `0x0028788B` → [sub_00287A62 + 0x8C](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x002878BD` → [sub_00287A62 + 0x15D](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x002878FE` → [sub_00287A62 + 0x14A](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x00287937` → [sub_00287A62 + 0x18E](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x00287940` → [sub_00287A62 + 0x345](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x00287950` → [sub_00287A62 + 0x3A](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x00287978` → [sub_00287E84 + 0x36](Unknown_function_00287E84.md) (`tail-transfer`)
  - `0x00287991` → [sub_00287E04 + 0xD](Unknown_function_00287E04.md) (`tail-transfer`)
  - `0x0028799C` → [sub_00287E04 + 0xD](Unknown_function_00287E04.md) (`tail-transfer`)
  - `0x00287A0A` → [sub_00287E84 + 0xF0](Unknown_function_00287E84.md) (`tail-transfer`)
  - `0x00287A1E` → [sub_00287A62 + 0xA](Unknown_function_00287A62.md) (`tail-transfer`)
  - `0x00287A28` → [sub_00287A62 + 0x21C](Unknown_function_00287A62.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00287607  4C 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], r15
0028760F  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00287614  44 8D 42 68                     lea r8d, [rdx + 0x68]
00287618  E8 23 F6 43 00                  call 0x1406c6c40
0028761D  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00287621  48 8B 0D 60 8A BA 00            mov rcx, qword ptr [rip + 0xba8a60]
00287628  48 C1 E8 2B                     shr rax, 0x2b
0028762C  25 FF 03 00 00                  and eax, 0x3ff
00287631  4C 8B 14 C1                     mov r10, qword ptr [rcx + rax*8]
00287635  0F B6 4F 22                     movzx ecx, byte ptr [rdi + 0x22]
00287639  8B C1                           mov eax, ecx
0028763B  4C 89 54 24 40                  mov qword ptr [rsp + 0x40], r10
00287640  83 E0 07                        and eax, 7
00287643  4D 8B BC C2 E0 1B 00 00         mov r15, qword ptr [r10 + rax*8 + 0x1be0]
0028764B  45 8B 47 0C                     mov r8d, dword ptr [r15 + 0xc]
0028764F  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
00287654  F6 C3 01                        test bl, 1
00287657  0F 85 05 04 00 00               jne 0x140287a62
0028765D  F6 C3 02                        test bl, 2
00287660  B8 C0 00 00 00                  mov eax, 0xc0
00287665  41 8B DC                        mov ebx, r12d
00287668  0F 45 D8                        cmovne ebx, eax
0028766B  80 E1 07                        and cl, 7
0028766E  80 F9 05                        cmp cl, 5
00287671  0F 84 40 09 00 00               je 0x140287fb7
00287677  49 BD 00 00 00 00 00 DE FF FF   movabs r13, 0xffffde0000000000
00287681  49 8B C5                        mov rax, r13
00287684  48 8B F7                        mov rsi, rdi
00287687  83 CB 10                        or ebx, 0x10
0028768A  48 2B F0                        sub rsi, rax
0028768D  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00287697  48 C1 FE 04                     sar rsi, 4
0028769B  48 0F AF F0                     imul rsi, rax
0028769F  48 8B 05 5A E5 BA 00            mov rax, qword ptr [rip + 0xbae55a]
002876A6  48 3B F0                        cmp rsi, rax
002876A9  72 0F                           jb 0x1402876ba
002876AB  48 05 00 08 00 00               add rax, 0x800
002876B1  48 3B F0                        cmp rsi, rax
002876B4  0F 82 6F 05 00 00               jb 0x140287c29
002876BA  44 38 25 25 55 BB 00            cmp byte ptr [rip + 0xbb5525], r12b
002876C1  74 1A                           je 0x1402876dd
002876C3  48 8B 05 76 5B BB 00            mov rax, qword ptr [rip + 0xbb5b76]
002876CA  48 8B CE                        mov rcx, rsi
002876CD  48 C1 E9 09                     shr rcx, 9
002876D1  0F B6 14 48                     movzx edx, byte ptr [rax + rcx*2]
002876D5  85 D2                           test edx, edx
002876D7  0F 85 42 07 00 00               jne 0x140287e1f
002876DD  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
002876E2  41 83 F8 02                     cmp r8d, 2
002876E6  0F 85 1C 04 00 00               jne 0x140287b08
002876EC  48 0F BA 67 28 35               bt qword ptr [rdi + 0x28], 0x35
002876F2  0F 82 39 05 00 00               jb 0x140287c31
002876F8  48 8B CF                        mov rcx, rdi
002876FB  E8 F0 AF 09 00                  call 0x1403226f0
00287700  83 CB 01                        or ebx, 1
00287703  44 8B E0                        mov r12d, eax
00287706  F6 C3 02                        test bl, 2
00287709  75 23                           jne 0x14028772e
0028770B  41 83 FE 09                     cmp r14d, 9
0028770F  75 20                           jne 0x140287731
00287711  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00287714  C1 E8 18                        shr eax, 0x18
00287717  A8 08                           test al, 8
00287719  74 16                           je 0x140287731
0028771B  4D 6B FC 58                     imul r15, r12, 0x58
0028771F  83 CB 04                        or ebx, 4
00287722  49 81 C7 C0 0C 00 00            add r15, 0xcc0
00287729  4D 03 FA                        add r15, r10
0028772C  EB 1B                           jmp 0x140287749
0028772E  83 E3 EE                        and ebx, 0xffffffee
00287731  4D 6B FC 58                     imul r15, r12, 0x58
00287735  49 81 C7 C0 0C 00 00            add r15, 0xcc0
0028773C  4D 03 FA                        add r15, r10
0028773F  41 83 FE 09                     cmp r14d, 9
00287743  0F 8C 3B 07 00 00               jl 0x140287e84
00287749  F6 C3 01                        test bl, 1
0028774C  74 15                           je 0x140287763
0028774E  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00287752  48 85 C0                        test rax, rax
00287755  0F 89 A9 06 00 00               jns 0x140287e04
0028775B  F0 49 FF 8A 40 1C 00 00         lock dec qword ptr [r10 + 0x1c40]
00287763  84 DB                           test bl, bl
00287765  78 22                           js 0x140287789
00287767  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0028776C  0F BA EB 08                     bts ebx, 8
00287770  41 B9 01 00 00 00               mov r9d, 1
00287776  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0028777B  45 8B C6                        mov r8d, r14d
0028777E  48 8B D7                        mov rdx, rdi
00287781  49 8B CF                        mov rcx, r15
00287784  E8 C7 4C FF FF                  call 0x14027c450
00287789  F6 C3 08                        test bl, 8
0028778C  75 27                           jne 0x1402877b5
0028778E  45 33 C9                        xor r9d, r9d
00287791  F6 C3 40                        test bl, 0x40
00287794  75 07                           jne 0x14028779d
00287796  44 38 4C 24 50                  cmp byte ptr [rsp + 0x50], r9b
0028779B  74 06                           je 0x1402877a3
0028779D  41 B9 01 00 00 00               mov r9d, 1
002877A3  45 8B C6                        mov r8d, r14d
002877A6  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
002877AD  48 8B CE                        mov rcx, rsi
002877B0  E8 1B 20 0B 00                  call 0x1403397d0
002877B5  F6 C3 04                        test bl, 4
002877B8  0F 85 A3 04 00 00               jne 0x140287c61
002877BE  4C 8B 17                        mov r10, qword ptr [rdi]
002877C1  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
002877CB  4C 8B 5F 18                     mov r11, qword ptr [rdi + 0x18]
002877CF  4C 23 D0                        and r10, rax
002877D2  4C 23 D8                        and r11, rax
002877D5  48 B9 FF FF FF FF 3F 00 00 00   movabs rcx, 0x3fffffffff
002877DF  4C 3B D1                        cmp r10, rcx
002877E2  74 40                           je 0x140287824
002877E4  48 8B 05 15 E4 BA 00            mov rax, qword ptr [rip + 0xbae415]
002877EB  4C 3B D0                        cmp r10, rax
002877EE  72 0B                           jb 0x1402877fb
002877F0  48 05 00 08 00 00               add rax, 0x800
002877F6  4C 3B D0                        cmp r10, rax
002877F9  72 29                           jb 0x140287824
002877FB  4F 8D 34 52                     lea r14, [r10 + r10*2]
002877FF  49 C1 E6 04                     shl r14, 4
00287803  49 8B C5                        mov rax, r13
00287806  4C 03 F0                        add r14, rax
00287809  49 8B CE                        mov rcx, r14
0028780C  E8 DF AE 09 00                  call 0x1403226f0
00287811  44 3B E0                        cmp r12d, eax
00287814  0F 85 56 08 00 00               jne 0x140288070
0028781A  48 B9 FF FF FF FF 3F 00 00 00   movabs rcx, 0x3fffffffff
00287824  4C 3B D9                        cmp r11, rcx
00287827  74 36                           je 0x14028785f
00287829  48 8B 05 D0 E3 BA 00            mov rax, qword ptr [rip + 0xbae3d0]
00287830  4C 3B D8                        cmp r11, rax
00287833  72 0B                           jb 0x140287840
00287835  48 05 00 08 00 00               add rax, 0x800
0028783B  4C 3B D8                        cmp r11, rax
0028783E  72 1F                           jb 0x14028785f
00287840  4F 8D 34 5B                     lea r14, [r11 + r11*2]
00287844  49 C1 E6 04                     shl r14, 4
00287848  49 8B C5                        mov rax, r13
0028784B  4C 03 F0                        add r14, rax
0028784E  49 8B CE                        mov rcx, r14
00287851  E8 9A AE 09 00                  call 0x1403226f0
00287856  44 3B E0                        cmp r12d, eax
00287859  0F 85 41 08 00 00               jne 0x1402880a0
0028785F  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00287864  0F B6 80 E4 3E 00 00            movzx eax, byte ptr [rax + 0x3ee4]
0028786B  44 3B E0                        cmp r12d, eax
0028786E  0F 82 EA 06 00 00               jb 0x140287f5e
00287874  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
0028787E  49 BC 00 00 00 00 00 FF FF FF   movabs r12, 0xffffff0000000000
00287888  4C 3B D0                        cmp r10, rax
0028788B  0F 84 5D 02 00 00               je 0x140287aee
00287891  4F 8D 0C 52                     lea r9, [r10 + r10*2]
00287895  49 C1 E1 04                     shl r9, 4
00287899  49 8B C5                        mov rax, r13
0028789C  4C 03 C8                        add r9, rax
0028789F  49 8B 51 18                     mov rdx, qword ptr [r9 + 0x18]
002878A3  48 8B CA                        mov rcx, rdx
002878A6  48 8B C2                        mov rax, rdx
002878A9  49 23 CC                        and rcx, r12
002878AC  49 0B CB                        or rcx, r11
002878AF  F0 49 0F B1 49 18               lock cmpxchg qword ptr [r9 + 0x18], rcx
002878B5  83 7C 24 30 02                  cmp dword ptr [rsp + 0x30], 2
002878BA  4C 8B C0                        mov r8, rax
002878BD  0F 85 FC 02 00 00               jne 0x140287bbf
002878C3  48 3B D0                        cmp rdx, rax
002878C6  74 22                           je 0x1402878ea
002878C8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
002878D0  49 8B C8                        mov rcx, r8
002878D3  4D 23 C4                        and r8, r12
002878D6  4D 0B C3                        or r8, r11
002878D9  48 8B C1                        mov rax, rcx
002878DC  F0 4D 0F B1 41 18               lock cmpxchg qword ptr [r9 + 0x18], r8
002878E2  4C 8B C0                        mov r8, rax
002878E5  48 3B C8                        cmp rcx, rax
002878E8  75 E6                           jne 0x1402878d0
002878EA  44 8B F3                        mov r14d, ebx
002878ED  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
002878F7  41 C1 EE 02                     shr r14d, 2
002878FB  4C 3B D8                        cmp r11, rax
002878FE  0F 84 A8 02 00 00               je 0x140287bac
00287904  4B 8D 0C 5B                     lea rcx, [r11 + r11*2]
00287908  48 C1 E1 04                     shl rcx, 4
0028790C  49 8B C5                        mov rax, r13
0028790F  48 03 C8                        add rcx, rax
00287912  48 8B 01                        mov rax, qword ptr [rcx]
00287915  49 23 C4                        and rax, r12
00287918  49 0B C2                        or rax, r10
0028791B  48 89 01                        mov qword ptr [rcx], rax
0028791E  41 83 E6 01                     and r14d, 1
00287922  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
00287926  F6 C3 10                        test bl, 0x10
00287929  74 04                           je 0x14028792f
0028792B  F0 49 FF 0F                     lock dec qword ptr [r15]
0028792F  44 8B 6C 24 34                  mov r13d, dword ptr [rsp + 0x34]
00287934  83 FA 02                        cmp edx, 2
00287937  0F 84 B3 02 00 00               je 0x140287bf0
0028793D  F6 C3 08                        test bl, 8
00287940  0F 85 61 04 00 00               jne 0x140287da7
00287946  48 C7 07 00 00 00 00            mov qword ptr [rdi], 0
0028794D  F6 C3 02                        test bl, 2
00287950  0F 85 46 01 00 00               jne 0x140287a9c
00287956  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0028795A  49 BE 00 00 00 00 00 00 20 00   movabs r14, 0x20000000000000
00287964  49 23 C4                        and rax, r12
00287967  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
0028796B  4C 85 77 28                     test qword ptr [rdi + 0x28], r14
0028796F  75 0D                           jne 0x14028797e
00287971  83 3D D4 87 BA 00 01            cmp dword ptr [rip + 0xba87d4], 1
00287978  0F 84 3C 05 00 00               je 0x140287eba
0028797E  C7 47 24 00 00 00 00            mov dword ptr [rdi + 0x24], 0
00287985  84 DB                           test bl, bl
00287987  0F 88 8D 00 00 00               js 0x140287a1a
0028798D  0F BA E3 08                     bt ebx, 8
00287991  0F 83 7A 04 00 00               jae 0x140287e11
00287997  80 7C 24 50 00                  cmp byte ptr [rsp + 0x50], 0
0028799C  0F 84 6F 04 00 00               je 0x140287e11
002879A2  80 7C 24 68 00                  cmp byte ptr [rsp + 0x68], 0
002879A7  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
002879B1  74 0A                           je 0x1402879bd
002879B3  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
002879B8  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
002879BD  80 BC 24 80 00 00 00 00         cmp byte ptr [rsp + 0x80], 0
002879C5  74 0A                           je 0x1402879d1
002879C7  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
002879CC  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
002879D1  80 BC 24 98 00 00 00 00         cmp byte ptr [rsp + 0x98], 0
002879D9  74 0D                           je 0x1402879e8
002879DB  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
002879E3  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
002879E8  80 BC 24 B0 00 00 00 00         cmp byte ptr [rsp + 0xb0], 0
002879F0  74 0D                           je 0x1402879ff
002879F2  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
002879FA  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
002879FF  F6 05 00 F1 D3 00 01            test byte ptr [rip + 0xd3f100], 1
00287A06  49 8D 4F 20                     lea rcx, [r15 + 0x20]
00287A0A  0F 85 64 05 00 00               jne 0x140287f74
00287A10  F0 81 21 FF FF FF BF            lock and dword ptr [rcx], 0xbfffffff
00287A17  F0 FF 09                        lock dec dword ptr [rcx]
00287A1A  41 83 FD 09                     cmp r13d, 9
00287A1E  74 4C                           je 0x140287a6c
00287A20  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00287A25  F6 C3 01                        test bl, 1
00287A28  0F 85 50 02 00 00               jne 0x140287c7e
00287A2E  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00287A32  4C 8B BC 24 10 01 00 00         mov r15, qword ptr [rsp + 0x110]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00287607(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, __int64 a8, __int64 a9, unsigned __int8 a10, __int64 a11, __int64 a12, unsigned __int8 a13, __int64 a14, __int64 a15, unsigned __int8 a16, __int64 a17, __int64 a18, unsigned __int8 a19, __int64 a20, __int64 a21, unsigned __int8 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p40;

    v_stack_p110 = v_r15;
    result = memset(a10, a2, a2 + 104, a4);
    result = (*(unsigned __int64 *)(v_rdi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_p40 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12225120) + result * 8);
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rdi + 34)))) & (7));
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12225120) + result * 8) + result * 8 + 7136) + 12)));
    v_rbx = (unsigned int)((unsigned int)(v_r12));
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) { v_rbx = 192; }
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rdi + 34)) & (7));
    v_rbx = (unsigned int)((v_rbx) | (16));
    v_rsi = (v_rdi) - (v_r13);
    v_rsi = (v_rsi) >> (4);
    v_rsi = (v_rsi) * (v_r13);
    if (v_rsi < (*(unsigned __int64 *)(v_rip + 12248410))) goto loc_002876BA;
    result = (*(unsigned __int64 *)(v_rip + 12248410)) + (0x800ULL);
loc_002876BA:
    if ((*(unsigned __int8 *)(v_rip + 12277029)) == ((unsigned __int8)(v_r12))) goto loc_002876DD;
    a1 = (v_rsi) >> (9);
loc_002876DD:
    v_stack_p34 = (unsigned int)(v_r14);
    result = MiGetPfnPriority(v_rdi, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12278646) + a1 * 2), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12225120) + result * 8) + result * 8 + 7136) + 12)), a4);
    v_rbx = (unsigned int)((v_rbx) | (1));
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_0028772E;
    if (((unsigned int)(v_r14)) != 9) goto loc_00287731;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_00287731;
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12225120) + result * 8) + result * 8 + 7136)) * ((unsigned int)((unsigned int)(result)));
    v_rbx = (unsigned int)((v_rbx) | (4));
    v_r15 = (v_r15) + (0xCC0ULL);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12225120) + result * 8));
    goto loc_00287749;
loc_0028772E:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFEEULL));
loc_00287731:
    v_r15 = (v_r15) * ((unsigned int)((unsigned int)(result)));
    v_r15 = (v_r15) + (0xCC0ULL);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12225120) + result * 8));
loc_00287749:
    if ((((unsigned __int8)(v_rbx)) & (1)) == 0) goto loc_00287763;
loc_00287763:
    result = *(unsigned __int64 *)(v_rdi + 40);
    if (!(sign_flag)) {
        result = a10;
        a4 = 1;
        v_stack_p20 = result;
        a3 = (unsigned int)(v_r14);
        a2 = v_rdi;
        a1 = v_r15;
        result = MiAcquirePageListLock(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) goto loc_002877B5;
    a4 = 0;
    if ((((unsigned __int8)(v_rbx)) & (64)) != 0) goto loc_0028779D;
    if (a10 != 0) {
        a4 = 1;
    }
    result = MiReplaceStandbyLookaside(v_rsi, -1, (unsigned int)((unsigned int)(v_r14)), a4);
loc_002877B5:
    v_r10 = (*(unsigned __int64 *)(v_rdi)) & (result);
    v_r11 = (*(unsigned __int64 *)(v_rdi + 24)) & (result);
    if (v_r10 == v_rsi) goto loc_00287824;
    if (v_r10 < (*(unsigned __int64 *)(v_rip + 12248085))) goto loc_002877FB;
    result = (*(unsigned __int64 *)(v_rip + 12248085)) + (0x800ULL);
    if (v_r10 < result) goto loc_00287824;
loc_002877FB:
    v_r14 = (v_r10 + v_r10 * 2) << (4);
    v_r14 = (v_r14) + (v_r13);
    result = MiGetPfnPriority(v_r14, -1, (unsigned int)((unsigned int)(v_r14)), a4);
loc_00287824:
    if (v_r11 == v_r14) goto loc_0028785F;
    if (v_r11 < (*(unsigned __int64 *)(v_rip + 12248016))) goto loc_00287840;
    result = (*(unsigned __int64 *)(v_rip + 12248016)) + (0x800ULL);
    if (v_r11 < result) goto loc_0028785F;
loc_00287840:
    v_r14 = (v_r11 + v_r11 * 2) << (4);
    v_r14 = (v_r14) + (v_r13);
    result = MiGetPfnPriority(v_r14, -1, (unsigned int)((unsigned int)(v_r14)), a4);
loc_0028785F:
    a4 = (v_r10 + v_r10 * 2) << (4);
    a4 = (a4) + (v_r13);
    a1 = (*(unsigned __int64 *)(a4 + 24)) & ((unsigned int)((unsigned int)(result)));
    a1 = (a1) | (v_r11);
    if ((*(unsigned __int64 *)(a4 + 24)) == (*(unsigned __int64 *)(a4 + 24))) goto loc_002878EA;
loc_002878D0:
    a3 = (*(unsigned __int64 *)(a4 + 24)) & ((unsigned int)((unsigned int)(result)));
    a3 = (a3) | (v_r11);
    if ((*(unsigned __int64 *)(a4 + 24)) != (*(unsigned __int64 *)(a4 + 24))) goto loc_002878D0;
loc_002878EA:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (2));
    a1 = (v_r11 + v_r11 * 2) << (4);
    a1 = (a1) + (v_r13);
    result = (*(unsigned __int64 *)(a1)) & ((unsigned int)((unsigned int)(result)));
    result = (result) | (v_r10);
    *(unsigned __int64 *)(a1) = result;
    v_r14 = (unsigned int)((v_r14) & (1));
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) {
    }
    *(unsigned __int64 *)(v_rdi) = 0;
    result = (*(unsigned __int64 *)(v_rdi + 24)) & ((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(v_rdi + 24) = result;
    if (((*(unsigned __int64 *)(v_rdi + 40)) & (v_r14)) != 0) goto loc_0028797E;
loc_0028797E:
    *(unsigned int *)(v_rdi + 36) = 0;
    if (sign_flag) goto loc_00287A1A;
    if (a13 != 0) {
        result = a12;
    }
    if (a16 != 0) {
        result = a15;
    }
    if (a19 != 0) {
        result = a18;
    }
    if (a22 != 0) {
        result = a21;
    }
loc_00287A1A:
    return (unsigned int)(a7);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00287607(int64_t Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint32_t Arg6, uint32_t Arg7, void *Arg8, uint64_t Arg9, uint8_t Arg10, uint64_t Arg11, void *Arg12, uint8_t Arg13, uint64_t Arg14, void *Arg15, uint8_t Arg16, uint64_t Arg17, void *Arg18, uint8_t Arg19, uint64_t Arg20, void *Arg21, uint8_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, uint64_t Arg33, int64_t Arg34)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg12 = (uint8_t *)Arg12;
    uint8_t *arg15 = (uint8_t *)Arg15;
    uint8_t *arg18 = (uint8_t *)Arg18;
    uint8_t *arg21 = (uint8_t *)Arg21;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    uint64_t v_stack_p110;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint64_t v_stack_p40;

    v_stack_p110 = local_r15;
    result = memset(Arg10, Arg2, Arg2 + 104, Arg4);
    result = (*(uint64_t *)(local_rdi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_p40 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBA8A60) + result * 8);
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(local_rdi + 0x22)))) & (7));
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA8A60) + result * 8) + result * 8 + 0x1BE0) + 0xC)));
    local_rbx = (uint32_t)((uint32_t)(local_r12));
    if ((((uint8_t)(local_rbx)) & (2)) != 0) { local_rbx = 192; }
    Arg1 = (uint8_t)((*(uint8_t *)(local_rdi + 0x22)) & (7));
    local_rbx = (uint32_t)((local_rbx) | (16));
    local_rsi = (local_rdi) - (local_r13);
    local_rsi = (local_rsi) >> (4);
    local_rsi = (local_rsi) * (local_r13);
    if (local_rsi < (*(uint64_t *)(v_rip + 0xBAE55A))) goto loc_002876BA;
    result = (*(uint64_t *)(v_rip + 0xBAE55A)) + (0x800ULL);
loc_002876BA:
    if ((*(uint8_t *)(v_rip + 0xBB5525)) == ((uint8_t)(local_r12))) goto loc_002876DD;
    Arg1 = (local_rsi) >> (9);
loc_002876DD:
    v_stack_p34 = (uint32_t)(local_r14);
    result = MiGetPfnPriority(local_rdi, *(uint8_t *)(*(uint64_t *)(v_rip + 0xBB5B76) + Arg1 * 2), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA8A60) + result * 8) + result * 8 + 0x1BE0) + 0xC)), Arg4);
    local_rbx = (uint32_t)((local_rbx) | (1));
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_0028772E;
    if (((uint32_t)(local_r14)) != 9) goto loc_00287731;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_00287731;
    local_r15 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA8A60) + result * 8) + result * 8 + 0x1BE0)) * ((uint32_t)((uint32_t)(result)));
    local_rbx = (uint32_t)((local_rbx) | (4));
    local_r15 = (local_r15) + (0xCC0ULL);
    local_r15 = (local_r15) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA8A60) + result * 8));
    goto loc_00287749;
loc_0028772E:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFEEULL));
loc_00287731:
    local_r15 = (local_r15) * ((uint32_t)((uint32_t)(result)));
    local_r15 = (local_r15) + (0xCC0ULL);
    local_r15 = (local_r15) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA8A60) + result * 8));
loc_00287749:
    if ((((uint8_t)(local_rbx)) & (1)) == 0) goto loc_00287763;
loc_00287763:
    result = *(uint64_t *)(local_rdi + 0x28);
    if (!(sign_flag)) {
        result = Arg10;
        Arg4 = 1;
        v_stack_p20 = result;
        Arg3 = (uint32_t)(local_r14);
        Arg2 = local_rdi;
        Arg1 = local_r15;
        result = MiAcquirePageListLock(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)(local_rbx)) & (8)) != 0) goto loc_002877B5;
    Arg4 = 0;
    if ((((uint8_t)(local_rbx)) & (64)) != 0) goto loc_0028779D;
    if (Arg10 != 0) {
        Arg4 = 1;
    }
    result = MiReplaceStandbyLookaside(local_rsi, -1, (uint32_t)((uint32_t)(local_r14)), Arg4);
loc_002877B5:
    local_r10 = (*(uint64_t *)(local_rdi)) & (result);
    local_r11 = (*(uint64_t *)(local_rdi + 0x18)) & (result);
    if (local_r10 == local_rsi) goto loc_00287824;
    if (local_r10 < (*(uint64_t *)(v_rip + 0xBAE415))) goto loc_002877FB;
    result = (*(uint64_t *)(v_rip + 0xBAE415)) + (0x800ULL);
    if (local_r10 < result) goto loc_00287824;
loc_002877FB:
    local_r14 = (local_r10 + local_r10 * 2) << (4);
    local_r14 = (local_r14) + (local_r13);
    result = MiGetPfnPriority(local_r14, -1, (uint32_t)((uint32_t)(local_r14)), Arg4);
loc_00287824:
    if (local_r11 == local_r14) goto loc_0028785F;
    if (local_r11 < (*(uint64_t *)(v_rip + 0xBAE3D0))) goto loc_00287840;
    result = (*(uint64_t *)(v_rip + 0xBAE3D0)) + (0x800ULL);
    if (local_r11 < result) goto loc_0028785F;
loc_00287840:
    local_r14 = (local_r11 + local_r11 * 2) << (4);
    local_r14 = (local_r14) + (local_r13);
    result = MiGetPfnPriority(local_r14, -1, (uint32_t)((uint32_t)(local_r14)), Arg4);
loc_0028785F:
    Arg4 = (local_r10 + local_r10 * 2) << (4);
    Arg4 = (Arg4) + (local_r13);
    Arg1 = (*(uint64_t *)(Arg4 + 0x18)) & ((uint32_t)((uint32_t)(result)));
    Arg1 = (Arg1) | (local_r11);
    if ((*(uint64_t *)(Arg4 + 0x18)) == (*(uint64_t *)(Arg4 + 0x18))) goto loc_002878EA;
loc_002878D0:
    Arg3 = (*(uint64_t *)(Arg4 + 0x18)) & ((uint32_t)((uint32_t)(result)));
    Arg3 = (Arg3) | (local_r11);
    if ((*(uint64_t *)(Arg4 + 0x18)) != (*(uint64_t *)(Arg4 + 0x18))) goto loc_002878D0;
loc_002878EA:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (2));
    Arg1 = (local_r11 + local_r11 * 2) << (4);
    Arg1 = (Arg1) + (local_r13);
    result = (*(uint64_t *)(Arg1)) & ((uint32_t)((uint32_t)(result)));
    result = (result) | (local_r10);
    *(uint64_t *)(Arg1) = result;
    local_r14 = (uint32_t)((local_r14) & (1));
    if ((((uint8_t)(local_rbx)) & (16)) != 0) {
    }
    *(uint64_t *)(local_rdi) = 0;
    result = (*(uint64_t *)(local_rdi + 0x18)) & ((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(local_rdi + 0x18) = result;
    if (((*(uint64_t *)(local_rdi + 0x28)) & (local_r14)) != 0) goto loc_0028797E;
loc_0028797E:
    *(uint32_t *)(local_rdi + 0x24) = 0;
    if (sign_flag) goto loc_00287A1A;
    if (Arg13 != 0) {
        result = Arg12;
    }
    if (Arg16 != 0) {
        result = Arg15;
    }
    if (Arg19 != 0) {
        result = Arg18;
    }
    if (Arg22 != 0) {
        result = Arg21;
    }
loc_00287A1A:
    return (uint32_t)(Arg7);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x68` | `32` | `R` |
| `Arg8` | `+ 0x3EE4` | `8` | `R` |
| `Arg12` | `+ 0x18` | `64` | `R/W` |
| `Arg15` | `+ 0x18` | `64` | `R/W` |
| `Arg18` | `+ 0x18` | `64` | `R/W` |
| `Arg21` | `+ 0x18` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00287607&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
