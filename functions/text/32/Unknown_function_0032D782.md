# sub_0032D782

- RVA: `0x0032D782`–`0x0032DCE6` (길이 `1,380` bytes)
- VA: `0x000000014032D782`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076228`
- 디코드: `313`개 명령, `1,380/1,380` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0032D862` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x0032D9A5` → [MiGetProtoPteAddress](MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x0032D9D2` → [MiVadExtentCommitted](MiVadExtentCommitted_function_0032E930.md) (function, `0x0032E930`)
- `0x0032DAC7` → [MiCheckVadSequential](MiCheckVadSequential_function_0032EBE0.md) (function, `0x0032EBE0`)
- `0x0032DB0D` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x0032DBAD` → [MiIsStoreProcess](../2B/MiIsStoreProcess_function_002B62E0.md) (function, `0x002B62E0`)
- `0x0032DBE1` → [MiLockVadCore](../29/MiLockVadCore_function_00297170.md) (function, `0x00297170`)
- `0x0032DBEE` → [MiLocateLockedVadEvent](../2A/MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x0032DC17` → [MiUnlockVadCore](../43/MiUnlockVadCore_function_004311C0.md) (function, `0x004311C0`)
- `0x0032DC5A` → [MiResolveSharedZeroFault](MiResolveSharedZeroFault_function_0032EF20.md) (function, `0x0032EF20`)
- `0x0032DC85` → [MiResolvePrivateZeroFault](MiResolvePrivateZeroFault_function_0032F760.md) (function, `0x0032F760`)
- `0x0032DCBD` → [MiIsVadLargePrivate](MiIsVadLargePrivate_function_0032F720.md) (function, `0x0032F720`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0032D81A` → RVA `0x00E2DB78` (`.data`; read)
- `0x0032D845` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0032D852` → RVA `0x00F0DE58` (`.data`; read)
- `0x0032D9E8` → RVA `0x00FC6B06` (`ALMOSTRO`; reference)
- `0x0032DB20` → RVA `0x00E2DB70` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **20**
  - `0x0032D7CF` → [sub_0032DDAC + 0x28](Unknown_function_0032DDAC.md) (`tail-transfer`)
  - `0x0032D7E5` → [sub_0032DDAC](Unknown_function_0032DDAC.md) (`tail-transfer`)
  - `0x0032D814` → [sub_0032DE99 + 0x43](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032D94D` → [sub_0032DE99 + 0xDA](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032D95A` → [sub_0032DE99 + 0xE8](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032D966` → [sub_0032DE99 + 0xFF](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032D98B` → [sub_0032DE99 + 0x11B](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032D9B0` → [sub_0032DE99 + 0x132](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032D9FD` → [sub_0032DE99 + 0x20](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032DA1A` → [sub_0032DD35](Unknown_function_0032DD35.md) (`tail-transfer`)
  - `0x0032DA2E` → [sub_0032DD4A](Unknown_function_0032DD4A.md) (`tail-transfer`)
  - `0x0032DA83` → [sub_0032DD4A + 0x42](Unknown_function_0032DD4A.md) (`tail-transfer`)
  - `0x0032DB54` → [sub_0032DE99 + 0x59](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032DBA4` → [sub_0032DE99 + 0xBE](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032DBB4` → [sub_0032DE99 + 0x98](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032DBC0` → [sub_0032DE99 + 0x7C](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032DBF9` → [sub_006E1EDA](../6E/Unknown_function_006E1EDA.md) (`tail-transfer`)
  - `0x0032DC0C` → [sub_006E1EDA](../6E/Unknown_function_006E1EDA.md) (`tail-transfer`)
  - `0x0032DCA8` → [sub_0032DE99 + 0x107](Unknown_function_0032DE99.md) (`tail-transfer`)
  - `0x0032DCB4` → [sub_0032DE99 + 0x111](Unknown_function_0032DE99.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0032D782  48 89 B4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rsi
0032D78A  4D 8B E5                        mov r12, r13
0032D78D  49 C1 EC 09                     shr r12, 9
0032D791  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
0032D799  4C 23 E0                        and r12, rax
0032D79C  4C 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r14
0032D7A4  4C 89 5D AF                     mov qword ptr [rbp - 0x51], r11
0032D7A8  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
0032D7B2  49 8B C0                        mov rax, r8
0032D7B5  4C 03 E0                        add r12, rax
0032D7B8  49 B9 FF FF FF FF FF F6 FF FF   movabs r9, 0xfffff6ffffffffff
0032D7C2  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0032D7CC  4C 3B E8                        cmp r13, rax
0032D7CF  0F 83 FF 05 00 00               jae 0x14032ddd4
0032D7D5  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
0032D7DF  4D 8B F2                        mov r14, r10
0032D7E2  4C 3B E8                        cmp r13, rax
0032D7E5  0F 87 C1 05 00 00               ja 0x14032ddac
0032D7EB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032D7F4  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0032D7FB  8B 81 FC 05 00 00               mov eax, dword ptr [rcx + 0x5fc]
0032D801  A8 01                           test al, 1
0032D803  75 22                           jne 0x14032d827
0032D805  49 8B C5                        mov rax, r13
0032D808  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0032D80E  48 3D 00 00 FE 7F               cmp rax, 0x7ffe0000
0032D814  0F 84 C2 06 00 00               je 0x14032dedc
0032D81A  48 3B 05 57 03 B0 00            cmp rax, qword ptr [rip + 0xb00357]
0032D821  0F 84 F0 02 00 00               je 0x14032db17
0032D827  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032D830  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0032D837  48 8B 89 10 04 00 00            mov rcx, qword ptr [rcx + 0x410]
0032D83E  48 81 C1 EC 03 00 00            add rcx, 0x3ec
0032D845  F6 05 BA 92 C9 00 21            test byte ptr [rip + 0xc992ba], 0x21
0032D84C  0F 84 9F 02 00 00               je 0x14032daf1
0032D852  8B 05 00 06 BE 00               mov eax, dword ptr [rip + 0xbe0600]
0032D858  85 C0                           test eax, eax
0032D85A  0F 85 91 02 00 00               jne 0x14032daf1
0032D860  B2 FF                           mov dl, 0xff
0032D862  E8 B9 F4 F4 FF                  call 0x14027cd20
0032D867  45 33 D2                        xor r10d, r10d
0032D86A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032D873  4C 8B 88 B8 00 00 00            mov r9, qword ptr [rax + 0xb8]
0032D87A  49 8B 91 60 05 00 00            mov rdx, qword ptr [r9 + 0x560]
0032D881  48 85 D2                        test rdx, rdx
0032D884  0F 84 AC 02 00 00               je 0x14032db36
0032D88A  0F B6 4A 20                     movzx ecx, byte ptr [rdx + 0x20]
0032D88E  4D 8B C5                        mov r8, r13
0032D891  8B 42 18                        mov eax, dword ptr [rdx + 0x18]
0032D894  48 C1 E1 20                     shl rcx, 0x20
0032D898  48 0B C8                        or rcx, rax
0032D89B  49 C1 E8 0C                     shr r8, 0xc
0032D89F  4C 3B C1                        cmp r8, rcx
0032D8A2  72 17                           jb 0x14032d8bb
0032D8A4  0F B6 4A 21                     movzx ecx, byte ptr [rdx + 0x21]
0032D8A8  8B 42 1C                        mov eax, dword ptr [rdx + 0x1c]
0032D8AB  48 C1 E1 20                     shl rcx, 0x20
0032D8AF  48 0B C8                        or rcx, rax
0032D8B2  4C 3B C1                        cmp r8, rcx
0032D8B5  0F 86 6F 03 00 00               jbe 0x14032dc2a
0032D8BB  49 8B 81 58 05 00 00            mov rax, qword ptr [r9 + 0x558]
0032D8C2  48 85 C0                        test rax, rax
0032D8C5  0F 84 6B 02 00 00               je 0x14032db36
0032D8CB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0032D8D0  0F B6 50 21                     movzx edx, byte ptr [rax + 0x21]
0032D8D4  8B 48 1C                        mov ecx, dword ptr [rax + 0x1c]
0032D8D7  48 C1 E2 20                     shl rdx, 0x20
0032D8DB  48 0B D1                        or rdx, rcx
0032D8DE  4C 3B C2                        cmp r8, rdx
0032D8E1  77 18                           ja 0x14032d8fb
0032D8E3  0F B6 50 20                     movzx edx, byte ptr [rax + 0x20]
0032D8E7  8B 48 18                        mov ecx, dword ptr [rax + 0x18]
0032D8EA  48 C1 E2 20                     shl rdx, 0x20
0032D8EE  48 0B D1                        or rdx, rcx
0032D8F1  4C 3B C2                        cmp r8, rdx
0032D8F4  73 0E                           jae 0x14032d904
0032D8F6  48 8B 00                        mov rax, qword ptr [rax]
0032D8F9  EB 04                           jmp 0x14032d8ff
0032D8FB  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0032D8FF  48 85 C0                        test rax, rax
0032D902  75 CC                           jne 0x14032d8d0
0032D904  48 85 C0                        test rax, rax
0032D907  0F 84 29 02 00 00               je 0x14032db36
0032D90D  49 89 81 60 05 00 00            mov qword ptr [r9 + 0x560], rax
0032D914  4C 8B F0                        mov r14, rax
0032D917  48 8B D8                        mov rbx, rax
0032D91A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032D923  BF 01 00 00 00                  mov edi, 1
0032D928  4C 89 55 FF                     mov qword ptr [rbp - 1], r10
0032D92C  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0032D933  8B 81 FC 05 00 00               mov eax, dword ptr [rcx + 0x5fc]
0032D939  40 84 C7                        test dil, al
0032D93C  75 22                           jne 0x14032d960
0032D93E  49 8B C5                        mov rax, r13
0032D941  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0032D947  48 3D 00 00 FE 7F               cmp rax, 0x7ffe0000
0032D94D  0F 84 20 06 00 00               je 0x14032df73
0032D953  48 3B 05 1E 02 B0 00            cmp rax, qword ptr [rip + 0xb0021e]
0032D95A  0F 84 21 06 00 00               je 0x14032df81
0032D960  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
0032D964  A8 04                           test al, 4
0032D966  0F 85 2C 06 00 00               jne 0x14032df98
0032D96C  24 70                           and al, 0x70
0032D96E  3C 20                           cmp al, 0x20
0032D970  0F 84 5A 02 00 00               je 0x14032dbd0
0032D976  41 8B 4E 30                     mov ecx, dword ptr [r14 + 0x30]
0032D97A  0F BA E1 15                     bt ecx, 0x15
0032D97E  0F 82 1E 03 00 00               jb 0x14032dca2
0032D984  41 8B 46 40                     mov eax, dword ptr [r14 + 0x40]
0032D988  40 84 C7                        test dil, al
0032D98B  0F 85 23 06 00 00               jne 0x14032dfb4
0032D991  49 8B D5                        mov rdx, r13
0032D994  4C 8D 4D FF                     lea r9, [rbp - 1]
0032D998  48 C1 EA 0C                     shr rdx, 0xc
0032D99C  41 B8 0C 00 00 00               mov r8d, 0xc
0032D9A2  49 8B CE                        mov rcx, r14
0032D9A5  E8 C6 0F 00 00                  call 0x14032e970
0032D9AA  48 8B F0                        mov rsi, rax
0032D9AD  48 85 C0                        test rax, rax
0032D9B0  0F 84 15 06 00 00               je 0x14032dfcb
0032D9B6  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
0032D9BA  8B D8                           mov ebx, eax
0032D9BC  C1 EB 07                        shr ebx, 7
0032D9BF  24 70                           and al, 0x70
0032D9C1  83 E3 1F                        and ebx, 0x1f
0032D9C4  3C 20                           cmp al, 0x20
0032D9C6  0F 84 C3 02 00 00               je 0x14032dc8f
0032D9CC  49 8B D5                        mov rdx, r13
0032D9CF  49 8B CE                        mov rcx, r14
0032D9D2  E8 59 0F 00 00                  call 0x14032e930
0032D9D7  85 C0                           test eax, eax
0032D9D9  0F 84 41 02 00 00               je 0x14032dc20
0032D9DF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032D9E8  40 84 3D 17 91 C9 00            test byte ptr [rip + 0xc99117], dil
0032D9EF  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0032D9F6  4C 8B 81 10 04 00 00            mov r8, qword ptr [rcx + 0x410]
0032D9FD  0F 85 B6 04 00 00               jne 0x14032deb9
0032DA03  F0 41 81 A0 EC 03 00 00 FF FF FF BF  lock and dword ptr [r8 + 0x3ec], 0xbfffffff
0032DA0F  F0 41 FF 88 EC 03 00 00         lock dec dword ptr [r8 + 0x3ec]
0032DA17  83 FB 18                        cmp ebx, 0x18
0032DA1A  0F 84 15 03 00 00               je 0x14032dd35
0032DA20  8B C3                           mov eax, ebx
0032DA22  83 E0 F8                        and eax, 0xfffffff8
0032DA25  83 F8 10                        cmp eax, 0x10
0032DA28  75 3B                           jne 0x14032da65
0032DA2A  F6 45 A7 02                     test byte ptr [rbp - 0x59], 2
0032DA2E  0F 84 16 03 00 00               je 0x14032dd4a
0032DA34  33 C0                           xor eax, eax
0032DA36  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
0032DA3E  4C 8B B4 24 B0 00 00 00         mov r14, qword ptr [rsp + 0xb0]
0032DA46  48 8B BC 24 B8 00 00 00         mov rdi, qword ptr [rsp + 0xb8]
0032DA4E  48 8B B4 24 C0 00 00 00         mov rsi, qword ptr [rsp + 0xc0]
0032DA56  48 81 C4 C8 00 00 00            add rsp, 0xc8
0032DA5D  41 5D                           pop r13
0032DA5F  41 5C                           pop r12
0032DA61  5B                              pop rbx
0032DA62  5D                              pop rbp
0032DA63  C3                              ret
0032DA64  CC                              int3
0032DA65  8B 4D A7                        mov ecx, dword ptr [rbp - 0x59]
0032DA68  45 33 D2                        xor r10d, r10d
0032DA6B  4C 8B 5D 67                     mov r11, qword ptr [rbp + 0x67]
0032DA6F  49 8B 43 10                     mov rax, qword ptr [r11 + 0x10]
0032DA73  48 8B D0                        mov rdx, rax
0032DA76  4C 89 6D B7                     mov qword ptr [rbp - 0x49], r13
0032DA7A  48 83 E2 FE                     and rdx, 0xfffffffffffffffe
0032DA7E  89 5D C7                        mov dword ptr [rbp - 0x39], ebx
0032DA81  A8 01                           test al, 1
0032DA83  0F 85 03 03 00 00               jne 0x14032dd8c
0032DA89  41 8B C2                        mov eax, r10d
0032DA8C  89 45 D7                        mov dword ptr [rbp - 0x29], eax
0032DA8F  48 89 75 BF                     mov qword ptr [rbp - 0x41], rsi
0032DA93  4C 89 75 E7                     mov qword ptr [rbp - 0x19], r14
0032DA97  44 89 55 CB                     mov dword ptr [rbp - 0x35], r10d
0032DA9B  48 85 F6                        test rsi, rsi
0032DA9E  0F 84 DD 01 00 00               je 0x14032dc81
0032DAA4  F6 C1 02                        test cl, 2
0032DAA7  0F 85 95 01 00 00               jne 0x14032dc42
0032DAAD  4D 85 F6                        test r14, r14
0032DAB0  0F 84 8C 01 00 00               je 0x14032dc42
0032DAB6  49 8B 46 78                     mov rax, qword ptr [r14 + 0x78]
0032DABA  48 85 C0                        test rax, rax
0032DABD  0F 88 7F 01 00 00               js 0x14032dc42
0032DAC3  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0032DAC7  E8 14 11 00 00                  call 0x14032ebe0
0032DACC  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0032DAD0  3D 20 02 00 C0                  cmp eax, 0xc0000220
0032DAD5  0F 85 67 01 00 00               jne 0x14032dc42
0032DADB  F0 41 0F C1 7E 24               lock xadd dword ptr [r14 + 0x24], edi
0032DAE1  83 C7 01                        add edi, 1
0032DAE4  0F 85 4B 01 00 00               jne 0x14032dc35
0032DAEA  B9 0E 00 00 00                  mov ecx, 0xe
0032DAEF  CD 29                           int 0x29
0032DAF1  0F 0D 09                        prefetchw byte ptr [rcx]
0032DAF4  8B 01                           mov eax, dword ptr [rcx]
0032DAF6  0F BA F0 1F                     btr eax, 0x1f
0032DAFA  8D 50 01                        lea edx, [rax + 1]
0032DAFD  F0 0F B1 11                     lock cmpxchg dword ptr [rcx], edx
0032DB01  0F 84 63 FD FF FF               je 0x14032d86a
0032DB07  85 C0                           test eax, eax
0032DB09  79 EF                           jns 0x14032dafa
0032DB0B  B2 FF                           mov dl, 0xff
0032DB0D  E8 6E 48 03 00                  call 0x140362380
0032DB12  E9 50 FD FF FF                  jmp 0x14032d867
0032DB17  48 85 C0                        test rax, rax
0032DB1A  0F 84 07 FD FF FF               je 0x14032d827
0032DB20  48 8B 35 49 00 B0 00            mov rsi, qword ptr [rip + 0xb00049]
0032DB27  BF 01 00 00 00                  mov edi, 1
0032DB2C  8B 4D A7                        mov ecx, dword ptr [rbp - 0x59]
0032DB2F  8B DF                           mov ebx, edi
0032DB31  E9 39 FF FF FF                  jmp 0x14032da6f
0032DB36  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032DB3F  F6 05 C0 8F C9 00 01            test byte ptr [rip + 0xc98fc0], 1
0032DB46  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0032DB4D  4C 8B 81 10 04 00 00            mov r8, qword ptr [rcx + 0x410]
0032DB54  0F 85 98 03 00 00               jne 0x14032def2
0032DB5A  F0 41 81 A0 EC 03 00 00 FF FF FF BF  lock and dword ptr [r8 + 0x3ec], 0xbfffffff
0032DB66  F0 41 FF 88 EC 03 00 00         lock dec dword ptr [r8 + 0x3ec]
0032DB6E  8B 4D A7                        mov ecx, dword ptr [rbp - 0x59]
0032DB71  4C 8B 4D 67                     mov r9, qword ptr [rbp + 0x67]
0032DB75  49 8D 85 00 00 FF FF            lea rax, [r13 - 0x10000]
0032DB7C  48 BA FF FF FD FF FF 7F 00 00   movabs rdx, 0x7ffffffdffff
0032DB86  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
0032DB8A  48 3B C2                        cmp rax, rdx
0032DB8D  77 2E                           ja 0x14032dbbd
0032DB8F  4D 85 F6                        test r14, r14
0032DB92  75 29                           jne 0x14032dbbd
0032DB94  41 F6 C1 02                     test r9b, 2
0032DB98  74 23                           je 0x14032dbbd
0032DB9A  F7 83 FC 05 00 00 00 10 00 00   test dword ptr [rbx + 0x5fc], 0x1000
0032DBA4  0F 85 AD 03 00 00               jne 0x14032df57
0032DBAA  48 8B CB                        mov rcx, rbx
0032DBAD  E8 2E 87 F8 FF                  call 0x1402b62e0
0032DBB2  85 C0                           test eax, eax
0032DBB4  0F 85 77 03 00 00               jne 0x14032df31
0032DBBA  8B 4D A7                        mov ecx, dword ptr [rbp - 0x59]
0032DBBD  F6 C1 02                        test cl, 2
0032DBC0  0F 85 4F 03 00 00               jne 0x14032df15
0032DBC6  B8 05 00 00 C0                  mov eax, 0xc0000005
0032DBCB  E9 66 FE FF FF                  jmp 0x14032da36
0032DBD0  41 8B 46 40                     mov eax, dword ptr [r14 + 0x40]
0032DBD4  A8 10                           test al, 0x10
0032DBD6  0F 84 9A FD FF FF               je 0x14032d976
0032DBDC  8B D7                           mov edx, edi
0032DBDE  49 8B CE                        mov rcx, r14
0032DBE1  E8 8A 95 F6 FF                  call 0x140297170
0032DBE6  BA 20 00 00 00                  mov edx, 0x20
0032DBEB  49 8B CE                        mov rcx, r14
0032DBEE  E8 19 9E F7 FF                  call 0x1402a7a0c
0032DBF3  48 8B D0                        mov rdx, rax
0032DBF6  48 85 C0                        test rax, rax
0032DBF9  0F 84 DB 42 3B 00               je 0x1406e1eda
0032DBFF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032DC08  48 39 42 08                     cmp qword ptr [rdx + 8], rax
0032DC0C  0F 84 C8 42 3B 00               je 0x1406e1eda
0032DC12  B2 11                           mov dl, 0x11
0032DC14  48 8B CB                        mov rcx, rbx
0032DC17  E8 A4 35 10 00                  call 0x1404311c0
0032DC1C  33 C0                           xor eax, eax
0032DC1E  8B F0                           mov esi, eax
0032DC20  BB 18 00 00 00                  mov ebx, 0x18
0032DC25  E9 B5 FD FF FF                  jmp 0x14032d9df
0032DC2A  4C 8B F2                        mov r14, rdx
0032DC2D  48 8B DA                        mov rbx, rdx
0032DC30  E9 E5 FC FF FF                  jmp 0x14032d91a
0032DC35  4C 8B 4D 67                     mov r9, qword ptr [rbp + 0x67]
0032DC39  41 83 49 50 20                  or dword ptr [r9 + 0x50], 0x20
0032DC3E  4D 89 71 58                     mov qword ptr [r9 + 0x58], r14
0032DC42  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
0032DC46  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0032DC4A  C6 00 00                        mov byte ptr [rax], 0
0032DC4D  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0032DC51  89 18                           mov dword ptr [rax], ebx
0032DC53  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0032DC57  48 89 30                        mov qword ptr [rax], rsi
0032DC5A  E8 C1 12 00 00                  call 0x14032ef20
0032DC5F  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
0032DC63  8B 4D A7                        mov ecx, dword ptr [rbp - 0x59]
0032DC66  D1 E9                           shr ecx, 1
0032DC68  8B 42 50                        mov eax, dword ptr [rdx + 0x50]
0032DC6B  33 C8                           xor ecx, eax
0032DC6D  81 E1 00 FE 01 00               and ecx, 0x1fe00
0032DC73  33 C8                           xor ecx, eax
0032DC75  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
0032DC79  89 4A 50                        mov dword ptr [rdx + 0x50], ecx
0032DC7C  E9 B5 FD FF FF                  jmp 0x14032da36
0032DC81  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0032DC85  E8 D6 1A 00 00                  call 0x14032f760
0032DC8A  E9 A7 FD FF FF                  jmp 0x14032da36
0032DC8F  83 FB 07                        cmp ebx, 7
0032DC92  0F 85 34 FD FF FF               jne 0x14032d9cc
0032DC98  BB 00 01 00 00                  mov ebx, 0x100
0032DC9D  E9 2A FD FF FF                  jmp 0x14032d9cc
0032DCA2  8B C1                           mov eax, ecx
0032DCA4  24 70                           and al, 0x70
0032DCA6  3C 10                           cmp al, 0x10
0032DCA8  0F 84 F2 02 00 00               je 0x14032dfa0
0032DCAE  83 E1 70                        and ecx, 0x70
0032DCB1  80 F9 30                        cmp cl, 0x30
0032DCB4  0F 84 F0 02 00 00               je 0x14032dfaa
0032DCBA  49 8B CE                        mov rcx, r14
0032DCBD  E8 5E 1A 00 00                  call 0x14032f720
0032DCC2  BB 18 00 00 00                  mov ebx, 0x18
0032DCC7  85 C0                           test eax, eax
0032DCC9  75 13                           jne 0x14032dcde
0032DCCB  41 8B 4E 30                     mov ecx, dword ptr [r14 + 0x30]
0032DCCF  8B C1                           mov eax, ecx
0032DCD1  C1 E8 07                        shr eax, 7
0032DCD4  83 E0 1F                        and eax, 0x1f
0032DCD7  0F BA E1 19                     bt ecx, 0x19
0032DCDB  0F 42 D8                        cmovb ebx, eax
0032DCDE  49 8B F2                        mov rsi, r10
0032DCE1  E9 F9 FC FF FF                  jmp 0x14032d9df
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0032D782(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;

    v_stack_pC0 = v_rsi;
    v_r12 = (v_r13) >> (9);
    v_stack_pB8 = v_rdi;
    v_r12 = (v_r12) & (result);
    v_stack_pB0 = v_r14;
    *(unsigned __int64 *)(v_rbp - 81) = v_r11;
    v_r12 = (v_r12) + (a3);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1532)))) & (1)) != 0) goto loc_0032D827;
    result = (v_r13) & (0xFFFFFFFFFFFFF000ULL);
    if (result == (*(unsigned __int64 *)(v_rip + 11535191))) goto loc_0032DB17;
loc_0032D827:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040)) + (0x3ECULL);
    if (((*(unsigned __int8 *)(v_rip + 13210298)) & (33)) == 0) goto loc_0032DAF1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12453376))) != 0) goto loc_0032DAF1;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(a1, 255, a3, a4);
loc_0032D867:
    v_r10 = 0;
loc_0032D86A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) == 0) goto loc_0032DB36;
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) + 24)));
    a3 = (v_r13) >> (12);
    if (a3 < a1) goto loc_0032D8BB;
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) + 28)));
    if (a3 <= a1) goto loc_0032DC2A;
loc_0032D8BB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) == 0) goto loc_0032DB36;
loc_0032D8D0:
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 28)));
    if (a3 > a2) goto loc_0032D8FB;
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 32)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 24)));
    if (a3 >= a2) goto loc_0032D904;
    goto loc_0032D8FF;
loc_0032D8FB:
loc_0032D8FF:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) != 0) goto loc_0032D8D0;
loc_0032D904:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) == 0) goto loc_0032DB36;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1376) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8);
loc_0032D91A:
    *(unsigned __int64 *)(v_rbp - 1) = 0;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1532))))) != 0) goto loc_0032D960;
    result = (v_r13) & (0xFFFFFFFFFFFFF000ULL);
loc_0032D960:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) + 48))) & (112));
    if (((unsigned __int8)(result)) == 32) goto loc_0032DBD0;
loc_0032D976:
    if (((unsigned __int8)(result)) < 32) goto loc_0032DCA2;
    a2 = (v_r13) >> (12);
    result = MiGetProtoPteAddress(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8), a2, 12, v_rbp - 1);
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) + 48))))) >> (7));
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8) + 48))) & (112));
    v_rbx = (unsigned int)((v_rbx) & (31));
    if (((unsigned __int8)(result)) == 32) goto loc_0032DC8F;
loc_0032D9CC:
    result = MiVadExtentCommitted(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) + 8), v_r13, 12, v_rbp - 1);
    if ((unsigned int)(result) == 0) goto loc_0032DC20;
loc_0032D9DF:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (0xFFFFFFF8ULL));
    if (((unsigned int)(result)) != 16) goto loc_0032DA65;
    result = 0;
loc_0032DA36:
    v_rsp = (v_rsp) + (200);
    return result;
loc_0032DA65:
    v_r10 = 0;
loc_0032DA6F:
    *(unsigned __int64 *)(v_rbp - 73) = v_r13;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 16)) & (-2);
    *(unsigned int *)(v_rbp - 57) = (unsigned int)(v_rbx);
    *(unsigned int *)(v_rbp - 41) = 0;
    *(unsigned __int64 *)(v_rbp - 65) = a24;
    *(unsigned __int64 *)(v_rbp - 25) = a22;
    *(unsigned int *)(v_rbp - 53) = 0;
    if (a24 == 0) goto loc_0032DC81;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp - 89)))) & (2)) != 0) goto loc_0032DC42;
    if (a22 == 0) goto loc_0032DC42;
    if (sign_flag) goto loc_0032DC42;
    result = MiCheckVadSequential(v_rbp - 89, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), v_rbp - 1);
    *(unsigned __int64 *)(v_rbp - 9) = result;
    if (((unsigned int)(result)) != 0xC0000220ULL) goto loc_0032DC42;
    v_rdi = (unsigned int)((a23) + (1));
    if (condition_is_not_equal) goto loc_0032DC35;
loc_0032DAF1:
loc_0032DAFA:
    if (condition_is_equal) goto loc_0032D86A;
    if (!sign_flag) goto loc_0032DAFA;
    result = ExpWaitForSpinLockSharedAndAcquire(14, 255, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), v_rbp - 1);
    goto loc_0032D867;
loc_0032DB17:
    if (result == 0) goto loc_0032D827;
    goto loc_0032DA6F;
loc_0032DB36:
    if ((v_r13 - 65536) > 255) goto loc_0032DBBD;
    if (a22 != 0) goto loc_0032DBBD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 8))) & (2)) == 0) goto loc_0032DBBD;
    result = MiIsStoreProcess(1, 255, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 8));
loc_0032DBBD:
    goto loc_0032DA36;
loc_0032DBD0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a22 + 64)))) & (16)) == 0) goto loc_0032D976;
    result = MiLockVadCore(a22, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 8));
    result = MiLocateLockedVadEvent(a22, 32, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 8));
    result = MiUnlockVadCore(1, 17, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 8));
    result = 0;
loc_0032DC20:
    goto loc_0032D9DF;
loc_0032DC2A:
    goto loc_0032D91A;
loc_0032DC35:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 103) + 88) = 17;
loc_0032DC42:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 111)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 119)) = 17;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 127)) = 0;
    result = MiResolveSharedZeroFault(v_rbp - 89, 17, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), *(unsigned __int64 *)(v_rbp + 103));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp - 89))) >> (1));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp + 103) + 80)))));
    a1 = (unsigned int)((a1) & (0x1FE00ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp + 103) + 80)))));
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 103) + 80) = (unsigned int)(a1);
    goto loc_0032DA36;
loc_0032DC81:
    result = MiResolvePrivateZeroFault(v_rbp - 89, *(unsigned __int64 *)(v_rbp + 103), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), *(unsigned __int64 *)(v_rbp + 103));
    goto loc_0032DA36;
loc_0032DC8F:
    if (17 != 7) goto loc_0032D9CC;
    goto loc_0032D9CC;
loc_0032DCA2:
    result = (unsigned __int8)(((unsigned int)((unsigned int)(v_rbp - 89))) & (112));
    a1 = (unsigned int)((v_rbp - 89) & (112));
    result = MiIsVadLargePrivate(17, *(unsigned __int64 *)(v_rbp + 103), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040), *(unsigned __int64 *)(v_rbp + 103));
    v_rbx = 24;
    if ((unsigned int)(result) == 0) {
        a1 = *(unsigned int *)(17 + 48);
        result = (unsigned int)(a1);
        result = (unsigned int)((result) >> (7));
        result = (unsigned int)((result) & (31));
        v_rbx = 24;
        if (condition_is_below) { v_rbx = (unsigned int)(result); }
    }
    goto loc_0032D9DF;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0032D782(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, int64_t Arg21, int64_t Arg22, int64_t Arg23, int64_t Arg24)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;

    v_stack_pC0 = local_rsi;
    local_r12 = (local_r13) >> (9);
    v_stack_pB8 = local_rdi;
    local_r12 = (local_r12) & (result);
    v_stack_pB0 = local_r14;
    *(uint64_t *)(local_rbp - 0x51) = local_r11;
    local_r12 = (local_r12) + (Arg3);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x5FC)))) & (1)) != 0) goto loc_0032D827;
    result = (local_r13) & (0xFFFFFFFFFFFFF000ULL);
    if (result == (*(uint64_t *)(v_rip + 0xB00357))) goto loc_0032DB17;
loc_0032D827:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410)) + (0x3ECULL);
    if (((*(uint8_t *)(v_rip + 0xC992BA)) & (33)) == 0) goto loc_0032DAF1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBE0600))) != 0) goto loc_0032DAF1;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(Arg1, 255, Arg3, Arg4);
loc_0032D867:
    local_r10 = 0;
loc_0032D86A:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) == 0) goto loc_0032DB36;
    Arg1 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) + 0x18)));
    Arg3 = (local_r13) >> (12);
    if (Arg3 < Arg1) goto loc_0032D8BB;
    Arg1 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) + 0x1C)));
    if (Arg3 <= Arg1) goto loc_0032DC2A;
loc_0032D8BB:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) == 0) goto loc_0032DB36;
loc_0032D8D0:
    Arg2 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x21)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x1C)));
    if (Arg3 > Arg2) goto loc_0032D8FB;
    Arg2 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x20)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x18)));
    if (Arg3 >= Arg2) goto loc_0032D904;
    goto loc_0032D8FF;
loc_0032D8FB:
loc_0032D8FF:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) != 0) goto loc_0032D8D0;
loc_0032D904:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) == 0) goto loc_0032DB36;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x560) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8);
loc_0032D91A:
    *(uint64_t *)(local_rbp - 0x1) = 0;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x5FC))))) != 0) goto loc_0032D960;
    result = (local_r13) & (0xFFFFFFFFFFFFF000ULL);
loc_0032D960:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) + 0x30))) & (112));
    if (((uint8_t)(result)) == 32) goto loc_0032DBD0;
loc_0032D976:
    if (((uint8_t)(result)) < 32) goto loc_0032DCA2;
    Arg2 = (local_r13) >> (12);
    result = MiGetProtoPteAddress(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8), Arg2, 12, local_rbp - 1);
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) + 0x30))))) >> (7));
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8) + 0x30))) & (112));
    local_rbx = (uint32_t)((local_rbx) & (31));
    if (((uint8_t)(result)) == 32) goto loc_0032DC8F;
loc_0032D9CC:
    result = MiVadExtentCommitted(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) + 0x8), local_r13, 12, local_rbp - 1);
    if ((uint32_t)(result) == 0) goto loc_0032DC20;
loc_0032D9DF:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (0xFFFFFFF8ULL));
    if (((uint32_t)(result)) != 16) goto loc_0032DA65;
    result = 0;
loc_0032DA36:
    local_rsp = (local_rsp) + (200);
    return result;
loc_0032DA65:
    local_r10 = 0;
loc_0032DA6F:
    *(uint64_t *)(local_rbp - 0x49) = local_r13;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x10)) & (-2);
    *(uint32_t *)(local_rbp - 0x39) = (uint32_t)(local_rbx);
    *(uint32_t *)(local_rbp - 0x29) = 0;
    *(uint64_t *)(local_rbp - 0x41) = Arg24;
    *(uint64_t *)(local_rbp - 0x19) = Arg22;
    *(uint32_t *)(local_rbp - 0x35) = 0;
    if (Arg24 == 0) goto loc_0032DC81;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x59)))) & (2)) != 0) goto loc_0032DC42;
    if (Arg22 == 0) goto loc_0032DC42;
    if (sign_flag) goto loc_0032DC42;
    result = MiCheckVadSequential(local_rbp - 89, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), local_rbp - 1);
    *(uint64_t *)(local_rbp - 0x9) = result;
    if (((uint32_t)(result)) != 0xC0000220ULL) goto loc_0032DC42;
    local_rdi = (uint32_t)((Arg23) + (1));
    if (condition_is_not_equal) goto loc_0032DC35;
loc_0032DAF1:
loc_0032DAFA:
    if (condition_is_equal) goto loc_0032D86A;
    if (!sign_flag) goto loc_0032DAFA;
    result = ExpWaitForSpinLockSharedAndAcquire(14, 255, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), local_rbp - 1);
    goto loc_0032D867;
loc_0032DB17:
    if (result == 0) goto loc_0032D827;
    goto loc_0032DA6F;
loc_0032DB36:
    if ((local_r13 - 65536) > 255) goto loc_0032DBBD;
    if (Arg22 != 0) goto loc_0032DBBD;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8))) & (2)) == 0) goto loc_0032DBBD;
    result = MiIsStoreProcess(1, 255, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), *(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8));
loc_0032DBBD:
    goto loc_0032DA36;
loc_0032DBD0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg22 + 0x40)))) & (16)) == 0) goto loc_0032D976;
    result = MiLockVadCore(Arg22, 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), *(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8));
    result = MiLocateLockedVadEvent(Arg22, 32, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), *(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8));
    result = MiUnlockVadCore(1, 17, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), *(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x8));
    result = 0;
loc_0032DC20:
    goto loc_0032D9DF;
loc_0032DC2A:
    goto loc_0032D91A;
loc_0032DC35:
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x58) = 17;
loc_0032DC42:
    *(uint8_t *)(*(uint64_t *)(local_rbp + 0x6F)) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x77)) = 17;
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x7F)) = 0;
    result = MiResolveSharedZeroFault(local_rbp - 89, 17, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), *(uint64_t *)(local_rbp + 0x67));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp - 0x59))) >> (1));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x50)))));
    Arg1 = (uint32_t)((Arg1) & (0x1FE00ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x50)))));
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x67) + 0x50) = (uint32_t)(Arg1);
    goto loc_0032DA36;
loc_0032DC81:
    result = MiResolvePrivateZeroFault(local_rbp - 89, *(uint64_t *)(local_rbp + 0x67), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), *(uint64_t *)(local_rbp + 0x67));
    goto loc_0032DA36;
loc_0032DC8F:
    if (17 != 7) goto loc_0032D9CC;
    goto loc_0032D9CC;
loc_0032DCA2:
    result = (uint8_t)(((uint32_t)((uint32_t)(local_rbp - 89))) & (112));
    Arg1 = (uint32_t)((local_rbp - 89) & (112));
    result = MiIsVadLargePrivate(17, *(uint64_t *)(local_rbp + 0x67), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410), *(uint64_t *)(local_rbp + 0x67));
    local_rbx = 24;
    if ((uint32_t)(result) == 0) {
        Arg1 = *(uint32_t *)(17 + 0x30);
        result = (uint32_t)(Arg1);
        result = (uint32_t)((result) >> (7));
        result = (uint32_t)((result) & (31));
        local_rbx = 24;
        if (condition_is_below) { local_rbx = (uint32_t)(result); }
    }
    goto loc_0032D9DF;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0032D782&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
