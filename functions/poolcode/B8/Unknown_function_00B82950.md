# sub_00B82950

- RVA: `0x00B82950`–`0x00B830A8` (길이 `1,880` bytes)
- VA: `0x0000000140B82950`
- 실행 섹션: `POOLCODE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007BE0C`
- 디코드: `455`개 명령, `1,880/1,880` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **19**

### Outgoing calls
- `0x00B82A9B` → [VfPtFreePoolNotification](../../pagevrfy/BB/VfPtFreePoolNotification_function_00BB96DC.md) (function, `0x00BB96DC`)
- `0x00B82C2A` → [KeReleaseInStackQueuedSpinLock](../../text/34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00B82C51` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (function, `0x00BB8FC0`)
- `0x00B82CA8` → [RtlCSparseBitmapBitmaskRead](../../text/36/RtlCSparseBitmapBitmaskRead_function_0036190C.md) (function, `0x0036190C`)
- `0x00B82FA5` → [RtlpLogHeapFailure](../../text/35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x00B82FC7` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (function, `0x00BB8FC0`)
- `0x00B83064` → [ExpRemovePoolTrackerExpansion](../../text/36/ExpRemovePoolTrackerExpansion_function_00361300.md) (function, `0x00361300`)
- `0x00B8306F` → [RtlpHpFreeHeap](../../text/35/RtlpHpFreeHeap_function_0035F600.md) (function, `0x0035F600`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B82950` → RVA `0x00EFED20` (`.data`; read)
- `0x00B82994` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00B82A70` → RVA `0x00FC6BD0` (`ALMOSTRO`; read)
- `0x00B82AA0` → RVA `0x00FC514C` (`ALMOSTRO`; read)
- `0x00B82AB7` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x00B82AD4` → RVA `0x00EFED58` (`.data`; read)
- `0x00B82B2C` → RVA `0x00EFAD00` (`.data`; read)
- `0x00B82B53` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00B82B60` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00B82B75` → RVA `0x00EFAD00` (`.data`; read/write)
- `0x00B82B85` → RVA `0x00EFED48` (`.data`; read)
- `0x00B82B8F` → RVA `0x00EFED40` (`.data`; read)
- `0x00B82BC9` → RVA `0x00EEEF40` (`.data`; read)
- `0x00B82BD0` → RVA `0x00EEEF60` (`.data`; read)
- `0x00B82C56` → RVA `0x00FCEC68` (`ALMOSTRO`; read)
- `0x00B82C93` → RVA `0x00E68610` (`.data`; read)
- `0x00B82C9A` → RVA `0x00E68608` (`.data`; read)
- `0x00B82CE2` → RVA `0x00E28300` (`.data`; read)
- `0x00B82D53` → RVA `0x00E28308` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00B82A9B` → [VfPtFreePoolNotification](../../pagevrfy/BB/VfPtFreePoolNotification_function_00BB96DC.md) (`POOLCODE` → `PAGEVRFY`)
  - `0x00B82C2A` → [KeReleaseInStackQueuedSpinLock](../../text/34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (`POOLCODE` → `.text`)
  - `0x00B82C51` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (`POOLCODE` → `PAGEVRFY`)
  - `0x00B82CA8` → [RtlCSparseBitmapBitmaskRead](../../text/36/RtlCSparseBitmapBitmaskRead_function_0036190C.md) (`POOLCODE` → `.text`)
  - `0x00B82FA5` → [RtlpLogHeapFailure](../../text/35/RtlpLogHeapFailure_function_0035B7BC.md) (`POOLCODE` → `.text`)
  - `0x00B82FC7` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (`POOLCODE` → `PAGEVRFY`)
  - `0x00B83064` → [ExpRemovePoolTrackerExpansion](../../text/36/ExpRemovePoolTrackerExpansion_function_00361300.md) (`POOLCODE` → `.text`)
  - `0x00B8306F` → [RtlpHpFreeHeap](../../text/35/RtlpHpFreeHeap_function_0035F600.md) (`POOLCODE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **30**
  - `0x00B82985` → [sub_00B830A9 + 0x1D](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B829A6` → [sub_00B830A9 + 0x104](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B82A03` → [sub_00B830A9](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B82A7F` → [sub_00B8371E + 0x3E5](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82ABF` → [sub_00B8371E + 0x480](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82B16` → [sub_00B830A9 + 0x573](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B82B5A` → [sub_00B830A9 + 0x516](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B82B6B` → [sub_00B830A9 + 0x4A5](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B82B7F` → [sub_00B8371E + 0x5F](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82BA5` → [sub_00B8371E + 0x1AB](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82BBF` → [sub_00B8371E + 0x1AB](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82BE3` → [sub_00B8371E + 0x765](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82BF4` → [sub_00B830A9 + 0xD](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B82C20` → [sub_00B8371E + 0x4D3](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82C34` → [sub_00B8371E + 0x1A2](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82C5D` → [sub_00B8371E + 0x231](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82C74` → [sub_00B8371E + 0x2DA](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82CB0` → [sub_00B8371E + 0x5A2](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82CB9` → [sub_00B8371E + 0x5A2](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82CC9` → [sub_00B8371E + 0x2B8](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82D38` → [sub_00B830A9 + 0x3D2](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B82DD6` → [sub_00B8371E + 0x678](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82DE0` → [sub_00B8371E + 0x62D](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82E01` → [sub_00B830A9 + 0x53E](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B82E71` → [sub_00B830A9 + 0x5A6](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B82F04` → [sub_00B830A9 + 0x4C4](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B82F82` → [sub_00B8371E + 0x5F3](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B82FEE` → [sub_00B8371E + 0x535](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B83041` → [sub_00B830A9 + 0x3B7](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83049` → [sub_00B830A9 + 0x5EB](Unknown_function_00B830A9.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B82950  8B 05 CA C3 37 00               mov eax, dword ptr [rip + 0x37c3ca]
00B82956  48 89 9C 24 08 01 00 00         mov qword ptr [rsp + 0x108], rbx
00B8295E  48 89 BC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rdi
00B82966  4C 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r14
00B8296E  85 C0                           test eax, eax
00B82970  0F 85 53 02 00 00               jne 0x140b82bc9
00B82976  BF 80 00 00 00                  mov edi, 0x80
00B8297B  8D 57 82                        lea edx, [rdi - 0x7e]
00B8297E  49 F7 C5 FF 0F 00 00            test r13, 0xfff
00B82985  0F 84 3B 07 00 00               je 0x140b830c6
00B8298B  41 0F B6 45 F3                  movzx eax, byte ptr [r13 - 0xd]
00B82990  4D 8D 75 F0                     lea r14, [r13 - 0x10]
00B82994  48 8D 1D 65 D6 47 FF            lea rbx, [rip - 0xb8299b]
00B8299B  BA 00 01 00 00                  mov edx, 0x100
00B829A0  44 8D 47 7F                     lea r8d, [rdi + 0x7f]
00B829A4  A8 08                           test al, 8
00B829A6  0F 85 01 08 00 00               jne 0x140b831ad
00B829AC  41 F6 46 03 04                  test byte ptr [r14 + 3], 4
00B829B1  74 1E                           je 0x140b829d1
00B829B3  41 0F B7 06                     movzx eax, word ptr [r14]
00B829B7  B9 FF 00 00 00                  mov ecx, 0xff
00B829BC  66 23 C1                        and ax, cx
00B829BF  0F B7 C8                        movzx ecx, ax
00B829C2  48 F7 D9                        neg rcx
00B829C5  48 C1 E1 04                     shl rcx, 4
00B829C9  4C 03 F1                        add r14, rcx
00B829CC  41 80 4E 03 04                  or byte ptr [r14 + 3], 4
00B829D1  45 0F B6 46 03                  movzx r8d, byte ptr [r14 + 3]
00B829D6  48 8B CA                        mov rcx, rdx
00B829D9  41 8B 5E 04                     mov ebx, dword ptr [r14 + 4]
00B829DD  41 F6 C0 01                     test r8b, 1
00B829E1  45 8B C8                        mov r9d, r8d
00B829E4  48 0F 44 CF                     cmove rcx, rdi
00B829E8  48 8B D1                        mov rdx, rcx
00B829EB  48 83 CA 04                     or rdx, 4
00B829EF  41 F6 C0 20                     test r8b, 0x20
00B829F3  48 0F 44 D1                     cmove rdx, rcx
00B829F7  48 83 CA 02                     or rdx, 2
00B829FB  48 89 55 97                     mov qword ptr [rbp - 0x69], rdx
00B829FF  41 83 E1 08                     and r9d, 8
00B82A03  0F 85 A0 06 00 00               jne 0x140b830a9
00B82A09  41 F6 C0 DE                     test r8b, 0xde
00B82A0D  74 4D                           je 0x140b82a5c
00B82A0F  48 8B CA                        mov rcx, rdx
00B82A12  48 83 C9 08                     or rcx, 8
00B82A16  41 F6 C0 04                     test r8b, 4
00B82A1A  48 0F 44 CA                     cmove rcx, rdx
00B82A1E  48 8B D1                        mov rdx, rcx
00B82A21  48 0F BA EA 09                  bts rdx, 9
00B82A26  41 F6 C0 80                     test r8b, 0x80
00B82A2A  48 0F 44 D1                     cmove rdx, rcx
00B82A2E  48 8B CA                        mov rcx, rdx
00B82A31  48 0F BA E9 0A                  bts rcx, 0xa
00B82A36  41 F6 C0 40                     test r8b, 0x40
00B82A3A  48 0F 44 CA                     cmove rcx, rdx
00B82A3E  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
00B82A42  45 85 C9                        test r9d, r9d
00B82A45  75 15                           jne 0x140b82a5c
00B82A47  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
00B82A4B  41 F6 C0 10                     test r8b, 0x10
00B82A4F  74 0B                           je 0x140b82a5c
00B82A51  48 8B C1                        mov rax, rcx
00B82A54  48 83 C8 20                     or rax, 0x20
00B82A58  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00B82A5C  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
00B82A61  49 8D 7E 10                     lea rdi, [r14 + 0x10]
00B82A65  0F B6 D0                        movzx edx, al
00B82A68  48 C1 E2 04                     shl rdx, 4
00B82A6C  48 89 55 9F                     mov qword ptr [rbp - 0x61], rdx
00B82A70  8B 05 5A 41 44 00               mov eax, dword ptr [rip + 0x44415a]
00B82A76  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
00B82A7A  A9 07 02 00 00                  test eax, 0x207
00B82A7F  0F 85 7E 10 00 00               jne 0x140b83b03
00B82A85  8B 05 45 41 44 00               mov eax, dword ptr [rip + 0x444145]
00B82A8B  A8 10                           test al, 0x10
00B82A8D  74 11                           je 0x140b82aa0
00B82A8F  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
00B82A93  4D 8B CD                        mov r9, r13
00B82A96  8B D3                           mov edx, ebx
00B82A98  49 8B CE                        mov rcx, r14
00B82A9B  E8 3C 6C 03 00                  call 0x140bb96dc
00B82AA0  8B 05 A6 26 44 00               mov eax, dword ptr [rip + 0x4426a6]
00B82AA6  44 89 65 AF                     mov dword ptr [rbp - 0x51], r12d
00B82AAA  C6 45 77 00                     mov byte ptr [rbp + 0x77], 0
00B82AAE  C6 45 A8 00                     mov byte ptr [rbp - 0x58], 0
00B82AB2  3B D8                           cmp ebx, eax
00B82AB4  75 01                           jne 0x140b82ab7
00B82AB6  CC                              int3
00B82AB7  8B 05 47 40 44 00               mov eax, dword ptr [rip + 0x444047]
00B82ABD  A8 41                           test al, 0x41
00B82ABF  0F 85 D9 10 00 00               jne 0x140b83b9e
00B82AC5  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
00B82ACD  4C 8D 1D 2C D5 47 FF            lea r11, [rip - 0xb82ad4]
00B82AD4  4C 8B 0D 7D C2 37 00            mov r9, qword ptr [rip + 0x37c27d]
00B82ADB  4D 8B 9C C3 20 AD EF 00         mov r11, qword ptr [r11 + rax*8 + 0xefad20]
00B82AE3  8B C3                           mov eax, ebx
00B82AE5  48 69 C8 5F 9E 00 00            imul rcx, rax, 0x9e5f
00B82AEC  48 8B D1                        mov rdx, rcx
00B82AEF  48 C1 EA 20                     shr rdx, 0x20
00B82AF3  33 D1                           xor edx, ecx
00B82AF5  41 23 D1                        and edx, r9d
00B82AF8  44 8B D2                        mov r10d, edx
00B82AFB  8B C2                           mov eax, edx
00B82AFD  48 8D 0C 80                     lea rcx, [rax + rax*4]
00B82B01  48 03 C9                        add rcx, rcx
00B82B04  41 8B 04 CB                     mov eax, dword ptr [r11 + rcx*8]
00B82B08  4D 8D 04 CB                     lea r8, [r11 + rcx*8]
00B82B0C  3B C3                           cmp eax, ebx
00B82B0E  0F 84 EB 03 00 00               je 0x140b82eff
00B82B14  85 C0                           test eax, eax
00B82B16  0F 84 00 0B 00 00               je 0x140b8361c
00B82B1C  8D 42 01                        lea eax, [rdx + 1]
00B82B1F  41 23 C1                        and eax, r9d
00B82B22  8B D0                           mov edx, eax
00B82B24  41 3B C2                        cmp eax, r10d
00B82B27  75 D2                           jne 0x140b82afb
00B82B29  0F 57 C0                        xorps xmm0, xmm0
00B82B2C  48 8D 0D CD 81 37 00            lea rcx, [rip + 0x3781cd]
00B82B33  0F 11 45 C7                     movups xmmword ptr [rbp - 0x39], xmm0
00B82B37  33 C0                           xor eax, eax
00B82B39  48 89 4D CF                     mov qword ptr [rbp - 0x31], rcx
00B82B3D  4C 89 65 C7                     mov qword ptr [rbp - 0x39], r12
00B82B41  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00B82B45  90                              nop
00B82B46  44 0F 20 C7                     mov rdi, cr8
00B82B4A  B8 02 00 00 00                  mov eax, 2
00B82B4F  44 0F 22 C0                     mov cr8, rax
00B82B53  83 3D C6 41 44 00 00            cmp dword ptr [rip + 0x4441c6], 0
00B82B5A  0F 85 5F 0A 00 00               jne 0x140b835bf
00B82B60  F6 05 9F 3F 44 00 21            test byte ptr [rip + 0x443f9f], 0x21
00B82B67  40 88 7D D7                     mov byte ptr [rbp - 0x29], dil
00B82B6B  0F 85 DD 09 00 00               jne 0x140b8354e
00B82B71  48 8D 55 C7                     lea rdx, [rbp - 0x39]
00B82B75  48 87 15 84 81 37 00            xchg qword ptr [rip + 0x378184], rdx
00B82B7C  48 85 D2                        test rdx, rdx
00B82B7F  0F 85 F8 0B 00 00               jne 0x140b8377d
00B82B85  4C 8B 0D BC C1 37 00            mov r9, qword ptr [rip + 0x37c1bc]
00B82B8C  41 8B D4                        mov edx, r12d
00B82B8F  4C 8B 15 AA C1 37 00            mov r10, qword ptr [rip + 0x37c1aa]
00B82B96  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00B82BA0  8B C2                           mov eax, edx
00B82BA2  49 3B C1                        cmp rax, r9
00B82BA5  0F 83 1E 0D 00 00               jae 0x140b838c9
00B82BAB  4C 8D 04 80                     lea r8, [rax + rax*4]
00B82BAF  49 C1 E0 04                     shl r8, 4
00B82BB3  4D 03 C2                        add r8, r10
00B82BB6  41 8B 00                        mov eax, dword ptr [r8]
00B82BB9  3B C3                           cmp eax, ebx
00B82BBB  74 32                           je 0x140b82bef
00B82BBD  85 C0                           test eax, eax
00B82BBF  0F 84 04 0D 00 00               je 0x140b838c9
00B82BC5  FF C2                           inc edx
00B82BC7  EB D7                           jmp 0x140b82ba0
00B82BC9  48 8D 05 70 C3 36 00            lea rax, [rip + 0x36c370]
00B82BD0  48 8D 0D 89 C3 36 00            lea rcx, [rip + 0x36c389]
00B82BD7  48 3B C1                        cmp rax, rcx
00B82BDA  0F 8D 96 FD FF FF               jge 0x140b82976
00B82BE0  4C 3B 38                        cmp r15, qword ptr [rax]
00B82BE3  0F 84 9A 12 00 00               je 0x140b83e83
00B82BE9  48 83 C0 08                     add rax, 8
00B82BED  EB E8                           jmp 0x140b82bd7
00B82BEF  48 0F BA E6 08                  bt rsi, 8
00B82BF4  0F 82 BC 04 00 00               jb 0x140b830b6
00B82BFA  41 B9 01 00 00 00               mov r9d, 1
00B82C00  49 8D 50 08                     lea rdx, [r8 + 8]
00B82C04  49 8D 40 18                     lea rax, [r8 + 0x18]
00B82C08  F0 48 FF 00                     lock inc qword ptr [rax]
00B82C0C  4C 8B 55 9F                     mov r10, qword ptr [rbp - 0x61]
00B82C10  49 8B CA                        mov rcx, r10
00B82C13  48 F7 D9                        neg rcx
00B82C16  F0 48 0F C1 0A                  lock xadd qword ptr [rdx], rcx
00B82C1B  49 83 78 48 00                  cmp qword ptr [r8 + 0x48], 0
00B82C20  0F 85 CB 0F 00 00               jne 0x140b83bf1
00B82C26  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00B82C2A  E8 B1 00 7C FF                  call 0x140342ce0
00B82C2F  48 0F BA E6 0A                  bt rsi, 0xa
00B82C34  0F 83 86 0C 00 00               jae 0x140b838c0
00B82C3A  48 C1 EE 08                     shr rsi, 8
00B82C3E  45 33 C9                        xor r9d, r9d
00B82C41  83 E6 01                        and esi, 1
00B82C44  49 8B CD                        mov rcx, r13
00B82C47  44 8B C6                        mov r8d, esi
00B82C4A  48 8B 75 9F                     mov rsi, qword ptr [rbp - 0x61]
00B82C4E  48 8B D6                        mov rdx, rsi
00B82C51  E8 6A 63 03 00                  call 0x140bb8fc0
00B82C56  80 3D 0B C0 44 00 00            cmp byte ptr [rip + 0x44c00b], 0
00B82C5D  0F 85 EC 0C 00 00               jne 0x140b8394f
00B82C63  49 8B 57 38                     mov rdx, qword ptr [r15 + 0x38]
00B82C67  48 8D 86 FF FD FF FF            lea rax, [rsi - 0x201]
00B82C6E  48 3D 7F 0D 00 00               cmp rax, 0xd7f
00B82C74  0F 86 7E 0D 00 00               jbe 0x140b839f8
00B82C7A  48 8D 35 7F D3 47 FF            lea rsi, [rip - 0xb82c81]
00B82C81  66 45 85 F6                     test r14w, r14w
00B82C85  74 09                           je 0x140b82c90
00B82C87  49 8D 9F 40 01 00 00            lea rbx, [r15 + 0x140]
00B82C8E  EB 3F                           jmp 0x140b82ccf
00B82C90  49 8B D6                        mov rdx, r14
00B82C93  48 8D 0D 76 59 2E 00            lea rcx, [rip + 0x2e5976]
00B82C9A  48 2B 15 67 59 2E 00            sub rdx, qword ptr [rip + 0x2e5967]
00B82CA1  48 C1 EA 14                     shr rdx, 0x14
00B82CA5  48 03 D2                        add rdx, rdx
00B82CA8  E8 5F EC 7D FF                  call 0x14036190c
00B82CAD  48 85 C0                        test rax, rax
00B82CB0  0F 84 0A 10 00 00               je 0x140b83cc0
00B82CB6  83 F8 03                        cmp eax, 3
00B82CB9  0F 84 01 10 00 00               je 0x140b83cc0
00B82CBF  49 8D 9F 40 01 00 00            lea rbx, [r15 + 0x140]
00B82CC6  83 F8 02                        cmp eax, 2
00B82CC9  0F 84 07 0D 00 00               je 0x140b839d6
00B82CCF  4C 8B 0B                        mov r9, qword ptr [rbx]
00B82CD2  49 8B D1                        mov rdx, r9
00B82CD5  49 23 D6                        and rdx, r14
00B82CD8  48 8B C2                        mov rax, rdx
00B82CDB  48 33 42 10                     xor rax, qword ptr [rdx + 0x10]
00B82CDF  48 33 C3                        xor rax, rbx
00B82CE2  48 33 05 17 56 2A 00            xor rax, qword ptr [rip + 0x2a5617]
00B82CE9  0F 85 9E 02 00 00               jne 0x140b82f8d
00B82CEF  44 0F B6 53 08                  movzx r10d, byte ptr [rbx + 8]
00B82CF4  45 8B C6                        mov r8d, r14d
00B82CF7  44 2B C2                        sub r8d, edx
00B82CFA  41 8B CA                        mov ecx, r10d
00B82CFD  41 D3 E8                        shr r8d, cl
00B82D00  49 C1 E0 05                     shl r8, 5
00B82D04  4C 03 C2                        add r8, rdx
00B82D07  41 0F B6 40 1A                  movzx eax, byte ptr [r8 + 0x1a]
00B82D0C  48 F7 D8                        neg rax
00B82D0F  48 C1 E0 05                     shl rax, 5
00B82D13  4C 03 C0                        add r8, rax
00B82D16  49 8B F8                        mov rdi, r8
00B82D19  48 2B FA                        sub rdi, rdx
00B82D1C  48 C1 FF 05                     sar rdi, 5
00B82D20  45 0F B6 58 18                  movzx r11d, byte ptr [r8 + 0x18]
00B82D25  48 D3 E7                        shl rdi, cl
00B82D28  48 03 FA                        add rdi, rdx
00B82D2B  49 3B FE                        cmp rdi, r14
00B82D2E  0F 94 C0                        sete al
00B82D31  42 8D 0C 18                     lea ecx, [rax + r11]
00B82D35  80 F9 0B                        cmp cl, 0xb
00B82D38  0F 85 3D 07 00 00               jne 0x140b8347b
00B82D3E  48 8B 73 18                     mov rsi, qword ptr [rbx + 0x18]
00B82D42  48 8B C7                        mov rax, rdi
00B82D45  0F B7 57 2C                     movzx edx, word ptr [rdi + 0x2c]
00B82D49  45 8B C6                        mov r8d, r14d
00B82D4C  48 C1 E8 0C                     shr rax, 0xc
00B82D50  33 47 28                        xor eax, dword ptr [rdi + 0x28]
00B82D53  33 05 AF 55 2A 00               xor eax, dword ptr [rip + 0x2a55af]
00B82D59  0F B7 C8                        movzx ecx, ax
00B82D5C  48 C1 E8 10                     shr rax, 0x10
00B82D60  48 03 C7                        add rax, rdi
00B82D63  48 C1 E2 06                     shl rdx, 6
00B82D67  44 2B C0                        sub r8d, eax
00B82D6A  41 8B C0                        mov eax, r8d
00B82D6D  8B 5C 32 48                     mov ebx, dword ptr [rdx + rsi + 0x48]
00B82D71  48 0F AF D8                     imul rbx, rax
00B82D75  48 C1 EB 20                     shr rbx, 0x20
00B82D79  8B C3                           mov eax, ebx
00B82D7B  0F AF C1                        imul eax, ecx
00B82D7E  44 3B C0                        cmp r8d, eax
00B82D81  0F 85 ED 02 00 00               jne 0x140b83074
00B82D87  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00B82D90  41 B9 01 00 00 00               mov r9d, 1
00B82D96  44 8B 46 4C                     mov r8d, dword ptr [rsi + 0x4c]
00B82D9A  41 8B C0                        mov eax, r8d
00B82D9D  C1 E8 0D                        shr eax, 0xd
00B82DA0  25 FF FF 03 00                  and eax, 0x3ffff
00B82DA5  49 C1 E8 04                     shr r8, 4
00B82DA9  0F BD C8                        bsr ecx, eax
00B82DAC  41 81 E0 FF 01 00 00            and r8d, 0x1ff
00B82DB3  41 D3 E1                        shl r9d, cl
00B82DB6  83 C1 FE                        add ecx, -2
00B82DB9  44 33 C8                        xor r9d, eax
00B82DBC  89 4D B7                        mov dword ptr [rbp - 0x49], ecx
00B82DBF  48 8B 82 B0 8B 00 00            mov rax, qword ptr [rdx + 0x8bb0]
00B82DC6  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00B82DCA  4A 8B 44 C8 08                  mov rax, qword ptr [rax + r9*8 + 8]
00B82DCF  4A 8B 04 C0                     mov rax, qword ptr [rax + r8*8]
00B82DD3  48 85 C0                        test rax, rax
00B82DD6  0F 84 BA 0F 00 00               je 0x140b83d96
00B82DDC  66 3B 47 2E                     cmp ax, word ptr [rdi + 0x2e]
00B82DE0  0F 84 65 0F 00 00               je 0x140b83d4b
00B82DE6  8B C3                           mov eax, ebx
00B82DE8  4C 8B CB                        mov r9, rbx
00B82DEB  83 E0 3F                        and eax, 0x3f
00B82DEE  0F B6 C8                        movzx ecx, al
00B82DF1  48 8B C3                        mov rax, rbx
00B82DF4  48 C1 E8 06                     shr rax, 6
00B82DF8  48 8B 44 C7 40                  mov rax, qword ptr [rdi + rax*8 + 0x40]
00B82DFD  48 0F A3 C8                     bt rax, rcx
00B82E01  0F 83 E0 07 00 00               jae 0x140b835e7
00B82E07  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00B82E0B  48 8B C8                        mov rcx, rax
00B82E0E  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
00B82E12  48 C1 E9 30                     shr rcx, 0x30
00B82E16  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00B82E1A  80 F9 01                        cmp cl, 1
00B82E1D  75 04                           jne 0x140b82e23
00B82E1F  C6 45 9D 02                     mov byte ptr [rbp - 0x63], 2
00B82E23  4D 85 F6                        test r14, r14
00B82E26  74 2C                           je 0x140b82e54
00B82E28  4C 8B 46 50                     mov r8, qword ptr [rsi + 0x50]
00B82E2C  0F B7 4D 97                     movzx ecx, word ptr [rbp - 0x69]
00B82E30  41 8B D0                        mov edx, r8d
00B82E33  66 41 89 0E                     mov word ptr [r14], cx
00B82E37  41 33 16                        xor edx, dword ptr [r14]
00B82E3A  0F B6 C9                        movzx ecx, cl
00B82E3D  D3 C2                           rol edx, cl
00B82E3F  8D 4B 01                        lea ecx, [rbx + 1]
00B82E42  49 C1 E8 20                     shr r8, 0x20
00B82E46  41 33 D0                        xor edx, r8d
00B82E49  66 89 4D 97                     mov word ptr [rbp - 0x69], cx
00B82E4D  41 33 D6                        xor edx, r14d
00B82E50  41 89 56 08                     mov dword ptr [r14 + 8], edx
00B82E54  66 FF 45 99                     inc word ptr [rbp - 0x67]
00B82E58  0F B7 57 2C                     movzx edx, word ptr [rdi + 0x2c]
00B82E5C  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00B82E60  48 C1 E2 06                     shl rdx, 6
00B82E64  F0 48 0F B1 4F 10               lock cmpxchg qword ptr [rdi + 0x10], rcx
00B82E6A  75 9F                           jne 0x140b82e0b
00B82E6C  80 7C 32 5C 00                  cmp byte ptr [rdx + rsi + 0x5c], 0
00B82E71  0F 84 D8 07 00 00               je 0x140b8364f
00B82E77  80 7D A5 01                     cmp byte ptr [rbp - 0x5b], 1
00B82E7B  0F 85 F3 01 00 00               jne 0x140b83074
00B82E81  44 0F B7 4D A3                  movzx r9d, word ptr [rbp - 0x5d]
00B82E86  41 C1 E1 06                     shl r9d, 6
00B82E8A  4C 03 CE                        add r9, rsi
00B82E8D  41 0F 0D 49 08                  prefetchw byte ptr [r9 + 8]
00B82E92  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00B82E96  4C 8B 57 18                     mov r10, qword ptr [rdi + 0x18]
00B82E9A  48 8B D0                        mov rdx, rax
00B82E9D  81 E2 FF 0F 00 00               and edx, 0xfff
00B82EA3  4D 8B C2                        mov r8, r10
00B82EA6  41 81 E0 FF 0F 00 00            and r8d, 0xfff
00B82EAD  48 8B C8                        mov rcx, rax
00B82EB0  48 2B CA                        sub rcx, rdx
00B82EB3  49 0B C8                        or rcx, r8
00B82EB6  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
00B82EBA  48 8B CF                        mov rcx, rdi
00B82EBD  48 0B CA                        or rcx, rdx
00B82EC0  F0 49 0F B1 49 08               lock cmpxchg qword ptr [r9 + 8], rcx
00B82EC6  0F 84 A8 01 00 00               je 0x140b83074
00B82ECC  48 8B D0                        mov rdx, rax
00B82ECF  49 8B CA                        mov rcx, r10
00B82ED2  48 33 C8                        xor rcx, rax
00B82ED5  81 E2 FF 0F 00 00               and edx, 0xfff
00B82EDB  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00B82EE2  4C 8B C0                        mov r8, rax
00B82EE5  49 33 CA                        xor rcx, r10
00B82EE8  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
00B82EEC  48 0B D7                        or rdx, rdi
00B82EEF  F0 49 0F B1 51 08               lock cmpxchg qword ptr [r9 + 8], rdx
00B82EF5  49 3B C0                        cmp rax, r8
00B82EF8  75 D2                           jne 0x140b82ecc
00B82EFA  E9 75 01 00 00                  jmp 0x140b83074
00B82EFF  48 0F BA E6 08                  bt rsi, 8
00B82F04  0F 83 63 06 00 00               jae 0x140b8356d
00B82F0A  45 8B CC                        mov r9d, r12d
00B82F0D  49 8D 50 20                     lea rdx, [r8 + 0x20]
00B82F11  49 8D 40 30                     lea rax, [r8 + 0x30]
00B82F15  4D 8B D4                        mov r10, r12
00B82F18  F0 48 FF 00                     lock inc qword ptr [rax]
00B82F1C  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
00B82F20  48 8B CB                        mov rcx, rbx
00B82F23  48 F7 D9                        neg rcx
00B82F26  F0 48 0F C1 0A                  lock xadd qword ptr [rdx], rcx
00B82F2B  49 83 78 48 00                  cmp qword ptr [r8 + 0x48], 0
00B82F30  0F 84 F9 FC FF FF               je 0x140b82c2f
00B82F36  41 8B C1                        mov eax, r9d
00B82F39  41 F6 44 C0 38 01               test byte ptr [r8 + rax*8 + 0x38], 1
00B82F3F  4D 8D 1C C0                     lea r11, [r8 + rax*8]
00B82F43  0F 85 E6 FC FF FF               jne 0x140b82c2f
00B82F49  49 8B 43 38                     mov rax, qword ptr [r11 + 0x38]
00B82F4D  4C 8D 0C 9D 3F 00 00 00         lea r9, [rbx*4 + 0x3f]
00B82F55  49 83 E1 C0                     and r9, 0xffffffffffffffc0
00B82F59  BB 80 00 00 00                  mov ebx, 0x80
00B82F5E  49 83 F9 40                     cmp r9, 0x40
00B82F62  4C 0F 44 CB                     cmove r9, rbx
00B82F66  49 8D 1C 09                     lea rbx, [r9 + rcx]
00B82F6A  48 3B C8                        cmp rcx, rax
00B82F6D  0F 8D BC FC FF FF               jge 0x140b82c2f
00B82F73  48 3B D8                        cmp rbx, rax
00B82F76  0F 8D B3 FC FF FF               jge 0x140b82c2f
00B82F7C  F0 49 0F B1 5B 38               lock cmpxchg qword ptr [r11 + 0x38], rbx
00B82F82  0F 84 89 0D 00 00               je 0x140b83d11
00B82F88  48 8B 0A                        mov rcx, qword ptr [rdx]
00B82F8B  EB D9                           jmp 0x140b82f66
00B82F8D  48 8B 53 38                     mov rdx, qword ptr [rbx + 0x38]
00B82F91  45 33 C9                        xor r9d, r9d
00B82F94  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00B82F99  4D 8B C6                        mov r8, r14
00B82F9C  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B82FA1  41 8D 49 09                     lea ecx, [r9 + 9]
00B82FA5  E8 12 88 7D FF                  call 0x14035b7bc
00B82FAA  E9 C5 00 00 00                  jmp 0x140b83074
00B82FAF  45 85 D2                        test r10d, r10d
00B82FB2  74 18                           je 0x140b82fcc
00B82FB4  4D 85 DB                        test r11, r11
00B82FB7  45 8B C4                        mov r8d, r12d
00B82FBA  41 B9 01 00 00 00               mov r9d, 1
00B82FC0  49 8B CD                        mov rcx, r13
00B82FC3  41 0F 95 C0                     setne r8b
00B82FC7  E8 F4 5F 03 00                  call 0x140bb8fc0
00B82FCC  8B 73 04                        mov esi, dword ptr [rbx + 4]
00B82FCF  8B 05 77 21 44 00               mov eax, dword ptr [rip + 0x442177]
00B82FD5  44 89 65 AB                     mov dword ptr [rbp - 0x55], r12d
00B82FD9  44 88 65 67                     mov byte ptr [rbp + 0x67], r12b
00B82FDD  44 88 65 7F                     mov byte ptr [rbp + 0x7f], r12b
00B82FE1  3B F0                           cmp esi, eax
00B82FE3  75 01                           jne 0x140b82fe6
00B82FE5  CC                              int3
00B82FE6  8B 05 18 3B 44 00               mov eax, dword ptr [rip + 0x443b18]
00B82FEC  A8 41                           test al, 0x41
00B82FEE  0F 85 5F 0C 00 00               jne 0x140b83c53
00B82FF4  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
00B82FFC  48 83 E7 FB                     and rdi, 0xfffffffffffffffb
00B83000  4C 8B 05 51 BD 37 00            mov r8, qword ptr [rip + 0x37bd51]
00B83007  8B C8                           mov ecx, eax
00B83009  48 8D 05 F0 CF 47 FF            lea rax, [rip - 0xb83010]
00B83010  4C 8B 9C C8 20 AD EF 00         mov r11, qword ptr [rax + rcx*8 + 0xefad20]
00B83018  48 69 CE 5F 9E 00 00            imul rcx, rsi, 0x9e5f
00B8301F  48 8B D1                        mov rdx, rcx
00B83022  48 C1 EA 20                     shr rdx, 0x20
00B83026  33 D1                           xor edx, ecx
00B83028  41 23 D0                        and edx, r8d
00B8302B  44 8B D2                        mov r10d, edx
00B8302E  8B C2                           mov eax, edx
00B83030  48 8D 0C 80                     lea rcx, [rax + rax*4]
00B83034  48 03 C9                        add rcx, rcx
00B83037  41 8B 04 CB                     mov eax, dword ptr [r11 + rcx*8]
00B8303B  4D 8D 0C CB                     lea r9, [r11 + rcx*8]
00B8303F  3B C6                           cmp eax, esi
00B83041  0F 84 19 04 00 00               je 0x140b83460
00B83047  85 C0                           test eax, eax
00B83049  0F 84 45 06 00 00               je 0x140b83694
00B8304F  8D 42 01                        lea eax, [rdx + 1]
00B83052  41 23 C0                        and eax, r8d
00B83055  8B D0                           mov edx, eax
00B83057  41 3B C2                        cmp eax, r10d
00B8305A  75 D2                           jne 0x140b8302e
00B8305C  4C 8B C7                        mov r8, rdi
00B8305F  49 8B D6                        mov rdx, r14
00B83062  8B CE                           mov ecx, esi
00B83064  E8 97 E2 7D FF                  call 0x140361300
00B83069  48 8B D3                        mov rdx, rbx
00B8306C  49 8B CF                        mov rcx, r15
00B8306F  E8 8C C5 7D FF                  call 0x14035f600
00B83074  4C 8B B4 24 C8 00 00 00         mov r14, qword ptr [rsp + 0xc8]
00B8307C  48 8B BC 24 D8 00 00 00         mov rdi, qword ptr [rsp + 0xd8]
00B83084  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
00B8308C  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
00B83094  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
00B8309C  48 81 C4 E0 00 00 00            add rsp, 0xe0
00B830A3  41 5D                           pop r13
00B830A5  5E                              pop rsi
00B830A6  5D                              pop rbp
00B830A7  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B82950(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD8;

    v_stack_p108 = v_rbx;
    v_stack_pD8 = v_rdi;
    v_stack_pC8 = v_r14;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3654602))) != 0) goto loc_00B82BC9;
loc_00B82976:
    result = *(unsigned __int8 *)(v_r13 - 13);
    v_r14 = v_r13 - 16;
    if (((*(unsigned __int8 *)(v_r13 - 16 + 3)) & (4)) != 0) {
        result = *(unsigned __int16 *)(v_r13 - 16);
        a1 = 255;
        result = (unsigned __int16)((result) & ((unsigned __int16)(a1)));
        a1 = (unsigned __int16)(result);
        a1 = -(a1);
        a1 = (a1) << (4);
        v_r14 = (v_r13 - 16) + (a1);
    }
    a1 = 256;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (1)) == 0) { a1 = 128; }
    a2 = (a1) | (4);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (32)) == 0) { a2 = a1; }
    a2 = (a2) | (2);
    *(unsigned __int64 *)(v_rbp - 105) = a2;
    a4 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r14 + 3)))) & (8));
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (222)) == 0) goto loc_00B82A5C;
    a1 = (a2) | (8);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (4)) == 0) { a1 = a2; }
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (128)) == 0) { a1 = a1; }
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (64)) == 0) { a1 = a1; }
    *(unsigned __int64 *)(v_rbp - 105) = a1;
    if ((unsigned int)(a4) != 0) goto loc_00B82A5C;
    *(unsigned __int64 *)(v_rbp - 105) = a1;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (16)) != 0) {
        result = a1;
        result = (result) | (32);
        *(unsigned __int64 *)(v_rbp - 105) = result;
    }
    a2 = ((unsigned __int8)(*(unsigned __int16 *)(v_r14 + 2))) << (4);
    *(unsigned __int64 *)(v_rbp - 97) = a2;
    result = (unsigned int)(*(unsigned int *)(v_rip + 4473157));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4473157)))) & (16)) != 0) {
        a3 = *(unsigned __int64 *)(v_rbp - 97);
        a4 = v_r13;
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 4)));
        a1 = v_r14;
        result = VfPtFreePoolNotification(a1, a2, a3, a4);
    }
    *(unsigned int *)(v_rbp - 81) = (unsigned int)(v_r12);
    *(unsigned __int8 *)(v_rbp + 119) = 0;
    *(unsigned __int8 *)(v_rbp - 88) = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 4)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4466342))))) {
    }
    a1 = (a1) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 4)))));
    a2 = (a1) >> (32);
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 3654269))));
loc_00B82AFB:
    a1 = ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4) + ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 12069588 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 15707424) + a1 * 8)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 4))))) goto loc_00B82EFF;
    result = (unsigned int)((a2 + 1) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 3654269))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00B82AFB;
    *(unsigned __int64 *)(v_rbp - 57) = v_xmm0;
    result = 0;
    *(unsigned __int64 *)(v_rbp - 49) = v_rip + 3637709;
    *(unsigned __int64 *)(v_rbp - 57) = v_r12;
    *(unsigned __int64 *)(v_rbp - 41) = 0;
    *(unsigned __int8 *)(v_rbp - 41) = (unsigned __int8)(v_cr8);
loc_00B82BA0:
    a3 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 4) << (4);
    a3 = (a3) + (*(unsigned __int64 *)(v_rip + 3654058));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 4))))) goto loc_00B82BEF;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + 1);
    goto loc_00B82BA0;
loc_00B82BC9:
loc_00B82BD7:
    if ((v_rip + 3588976) >= (v_rip + 3589001)) goto loc_00B82976;
    result = (v_rip + 3588976) + (8);
    goto loc_00B82BD7;
loc_00B82BEF:
    a1 = -(*(unsigned __int64 *)(v_rbp - 97));
    result = KeReleaseInStackQueuedSpinLock(v_rbp - 57, a3 + 8, a3, 1);
loc_00B82C2F:
    v_rsi = (*(unsigned __int64 *)(v_rbp - 105)) >> (8);
    a4 = 0;
    v_rsi = (unsigned int)((v_rsi) & (1));
    result = ViFreeTrackedPool(v_r13, *(unsigned __int64 *)(v_rbp - 97), (unsigned int)((unsigned int)(v_rsi)), a4);
    if ((unsigned __int16)(v_r14) == 0) goto loc_00B82C90;
    goto loc_00B82CCF;
loc_00B82C90:
    a2 = (v_r14) - (*(unsigned __int64 *)(v_rip + 3037543));
    a2 = (a2) >> (20);
    a2 = (a2) + (a2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 3037558, a2, (unsigned int)((unsigned int)(v_rsi)), a4);
loc_00B82CCF:
    a2 = (*(unsigned __int64 *)(v_r15 + 320)) & (v_r14);
    result = (a2) ^ (*(unsigned __int64 *)(a2 + 16));
    result = (result) ^ (v_r15 + 320);
    result = (result) ^ (*(unsigned __int64 *)(v_rip + 2774551));
    if (condition_is_not_equal) goto loc_00B82F8D;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(a2)));
    a3 = (unsigned int)((a3) >> ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r15 + 320 + 8))))));
    a3 = (a3) << (5);
    a3 = (a3) + (a2);
    result = -(*(unsigned __int8 *)(a3 + 26));
    result = (result) << (5);
    a3 = (a3) + (result);
    v_rdi = (a3) - (a2);
    v_rdi = (v_rdi) >> (5);
    v_rdi = (v_rdi) << ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r15 + 320 + 8)))));
    v_rdi = (v_rdi) + (a2);
    result = (v_rdi == v_r14) ? 1 : 0;
    result = (v_rdi) >> (12);
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rdi + 40)));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 2774447)));
    result = (result) >> (16);
    result = (result) + (v_rdi);
    a2 = (*(unsigned __int16 *)(v_rdi + 44)) << (6);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(result)));
    v_rbx = ((unsigned int)(*(unsigned int *)(a2 + *(unsigned __int64 *)(v_r15 + 320 + 24) * 1 + 72))) * ((unsigned int)((unsigned int)(a3)));
    v_rbx = (v_rbx) >> (32);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) * ((unsigned int)((unsigned __int16)(result))));
    if (((unsigned int)(a3)) != ((unsigned int)(result))) goto loc_00B83074;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 320 + 24) + 76))))) >> (13));
    result = (unsigned int)((result) & (0x3FFFFULL));
    a3 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 320 + 24) + 76))) >> (4);
    a3 = (unsigned int)((a3) & (511));
    a4 = (unsigned int)((1) << ((unsigned __int8)((unsigned __int16)(result))));
    a1 = (unsigned int)(((unsigned __int16)(result)) + (-2));
    a4 = (unsigned int)((a4) ^ ((unsigned int)(result)));
    *(unsigned int *)(v_rbp - 73) = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (63));
    result = (v_rbx) >> (6);
loc_00B82E0B:
    *(unsigned __int64 *)(v_rbp - 97) = *(unsigned __int64 *)(v_rdi + 16);
    a1 = (*(unsigned __int64 *)(v_rdi + 16)) >> (48);
    *(unsigned __int64 *)(v_rbp - 105) = *(unsigned __int64 *)(v_rdi + 16);
    if (((unsigned __int8)(a1)) == 1) {
        *(unsigned __int8 *)(v_rbp - 99) = 2;
    }
    if (v_r14 != 0) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 320 + 24) + 80);
        a1 = *(unsigned __int16 *)(v_rbp - 105);
        a2 = (unsigned int)(a3);
        *(unsigned __int16 *)(v_r14) = (unsigned __int16)(a1);
        a2 = (unsigned int)((a2) ^ (*(unsigned int *)(v_r14)));
        a1 = (unsigned __int8)(a1);
        a1 = v_rbx + 1;
        a3 = (a3) >> (32);
        a2 = (unsigned int)((a2) ^ ((unsigned int)(a3)));
        *(unsigned __int16 *)(v_rbp - 105) = (unsigned __int16)(a1);
        a2 = (unsigned int)((a2) ^ ((unsigned int)(v_r14)));
        *(unsigned int *)(v_r14 + 8) = (unsigned int)(a2);
    }
    a2 = (*(unsigned __int16 *)(v_rdi + 44)) << (6);
    if (condition_is_not_equal) goto loc_00B82E0B;
    if ((*(unsigned __int8 *)(v_rbp - 91)) != 1) goto loc_00B83074;
    a4 = (unsigned int)((*(unsigned __int16 *)(v_rbp - 93)) << (6));
    a4 = (a4) + (*(unsigned __int64 *)(v_r15 + 320 + 24));
    a2 = (unsigned int)((*(unsigned __int64 *)(a4 + 8)) & (0xFFFULL));
    a3 = (unsigned int)((*(unsigned __int64 *)(v_rdi + 24)) & (0xFFFULL));
    a1 = (*(unsigned __int64 *)(a4 + 8)) - (a2);
    a1 = (a1) | (a3);
    *(unsigned __int64 *)(v_rdi + 24) = a1;
    a1 = (v_rdi) | (a2);
    if (condition_is_equal) goto loc_00B83074;
loc_00B82ECC:
    a1 = (*(unsigned __int64 *)(v_rdi + 24)) ^ (*(unsigned __int64 *)(a4 + 8));
    a2 = (unsigned int)((*(unsigned __int64 *)(a4 + 8)) & (0xFFFULL));
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_rdi + 24));
    *(unsigned __int64 *)(v_rdi + 24) = a1;
    a2 = (a2) | (v_rdi);
    if ((*(unsigned __int64 *)(a4 + 8)) != (*(unsigned __int64 *)(a4 + 8))) goto loc_00B82ECC;
    goto loc_00B83074;
loc_00B82EFF:
    a1 = -(*(unsigned __int64 *)(v_rbp - 97));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 8) + 72)) == 0) goto loc_00B82C2F;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a4 + 8) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 8 + 56)) & (1)) != 0) goto loc_00B82C2F;
    a4 = (*(unsigned __int64 *)(v_rbp - 97) * 4 + 63) & (-64);
    if (a4 == 64) { a4 = 128; }
loc_00B82F66:
    if (a1 >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 8) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 8 + 56))) goto loc_00B82C2F;
    if ((a4 + a1 * 1) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 8) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))) * 8 + 56))) goto loc_00B82C2F;
    goto loc_00B82F66;
loc_00B82F8D:
    a4 = 0;
    v_stack_p28 = v_r12;
    v_stack_p20 = v_r12;
    result = RtlpLogHeapFailure(a4 + 9, *(unsigned __int64 *)(a4 + a1 * 1 + 56), v_r14, a4);
    goto loc_00B83074;
loc_00B83074:
    v_rsp = (v_rsp) + (224);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B82950(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, int64_t Arg24, int64_t Arg25, int64_t Arg26, int64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, int64_t Arg33)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p108;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD8;

    v_stack_p108 = local_rbx;
    v_stack_pD8 = local_rdi;
    v_stack_pC8 = local_r14;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x37C3CA))) != 0) goto loc_00B82BC9;
loc_00B82976:
    result = *(uint8_t *)(local_r13 - 0xD);
    local_r14 = local_r13 - 16;
    if (((*(uint8_t *)(local_r13 - 0x10 + 0x3)) & (4)) != 0) {
        result = *(uint16_t *)(local_r13 - 0x10);
        Arg1 = 255;
        result = (uint16_t)((result) & ((uint16_t)(Arg1)));
        Arg1 = (uint16_t)(result);
        Arg1 = -(Arg1);
        Arg1 = (Arg1) << (4);
        local_r14 = (local_r13 - 16) + (Arg1);
    }
    Arg1 = 256;
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (1)) == 0) { Arg1 = 128; }
    Arg2 = (Arg1) | (4);
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (32)) == 0) { Arg2 = Arg1; }
    Arg2 = (Arg2) | (2);
    *(uint64_t *)(local_rbp - 0x69) = Arg2;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(local_r14 + 0x3)))) & (8));
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (222)) == 0) goto loc_00B82A5C;
    Arg1 = (Arg2) | (8);
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (4)) == 0) { Arg1 = Arg2; }
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (128)) == 0) { Arg1 = Arg1; }
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (64)) == 0) { Arg1 = Arg1; }
    *(uint64_t *)(local_rbp - 0x69) = Arg1;
    if ((uint32_t)(Arg4) != 0) goto loc_00B82A5C;
    *(uint64_t *)(local_rbp - 0x69) = Arg1;
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (16)) != 0) {
        result = Arg1;
        result = (result) | (32);
        *(uint64_t *)(local_rbp - 0x69) = result;
    }
    Arg2 = ((uint8_t)(*(uint16_t *)(local_r14 + 0x2))) << (4);
    *(uint64_t *)(local_rbp - 0x61) = Arg2;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x444145));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x444145)))) & (16)) != 0) {
        Arg3 = *(uint64_t *)(local_rbp - 0x61);
        Arg4 = local_r13;
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x4)));
        Arg1 = local_r14;
        result = VfPtFreePoolNotification(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint32_t *)(local_rbp - 0x51) = (uint32_t)(local_r12);
    *(uint8_t *)(local_rbp + 0x77) = 0;
    *(uint8_t *)(local_rbp - 0x58) = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x4)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4426A6))))) {
    }
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x4)))));
    Arg2 = (Arg1) >> (32);
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)(*(uint64_t *)(v_rip + 0x37C27D))));
loc_00B82AFB:
    Arg1 = ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4) + ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0xB82AD4 + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xEFAD20) + Arg1 * 8)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x4))))) goto loc_00B82EFF;
    result = (uint32_t)((Arg2 + 1) & ((uint32_t)(*(uint64_t *)(v_rip + 0x37C27D))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00B82AFB;
    *(uint64_t *)(local_rbp - 0x39) = v_xmm0;
    result = 0;
    *(uint64_t *)(local_rbp - 0x31) = v_rip + 3637709;
    *(uint64_t *)(local_rbp - 0x39) = local_r12;
    *(uint64_t *)(local_rbp - 0x29) = 0;
    *(uint8_t *)(local_rbp - 0x29) = (uint8_t)(v_cr8);
loc_00B82BA0:
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 4) << (4);
    Arg3 = (Arg3) + (*(uint64_t *)(v_rip + 0x37C1AA));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x4))))) goto loc_00B82BEF;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + 1);
    goto loc_00B82BA0;
loc_00B82BC9:
loc_00B82BD7:
    if ((v_rip + 3588976) >= (v_rip + 3589001)) goto loc_00B82976;
    result = (v_rip + 3588976) + (8);
    goto loc_00B82BD7;
loc_00B82BEF:
    Arg1 = -(*(uint64_t *)(local_rbp - 0x61));
    result = KeReleaseInStackQueuedSpinLock(local_rbp - 57, Arg3 + 8, Arg3, 1);
loc_00B82C2F:
    local_rsi = (*(uint64_t *)(local_rbp - 0x69)) >> (8);
    Arg4 = 0;
    local_rsi = (uint32_t)((local_rsi) & (1));
    result = ViFreeTrackedPool(local_r13, *(uint64_t *)(local_rbp - 0x61), (uint32_t)((uint32_t)(local_rsi)), Arg4);
    if ((uint16_t)(local_r14) == 0) goto loc_00B82C90;
    goto loc_00B82CCF;
loc_00B82C90:
    Arg2 = (local_r14) - (*(uint64_t *)(v_rip + 0x2E5967));
    Arg2 = (Arg2) >> (20);
    Arg2 = (Arg2) + (Arg2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 3037558, Arg2, (uint32_t)((uint32_t)(local_rsi)), Arg4);
loc_00B82CCF:
    Arg2 = (*(uint64_t *)(local_r15 + 0x140)) & (local_r14);
    result = (Arg2) ^ (*(uint64_t *)(Arg2 + 0x10));
    result = (result) ^ (local_r15 + 320);
    result = (result) ^ (*(uint64_t *)(v_rip + 0x2A5617));
    if (condition_is_not_equal) goto loc_00B82F8D;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)((Arg3) >> ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_r15 + 0x140 + 0x8))))));
    Arg3 = (Arg3) << (5);
    Arg3 = (Arg3) + (Arg2);
    result = -(*(uint8_t *)(Arg3 + 0x1A));
    result = (result) << (5);
    Arg3 = (Arg3) + (result);
    local_rdi = (Arg3) - (Arg2);
    local_rdi = (local_rdi) >> (5);
    local_rdi = (local_rdi) << ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_r15 + 0x140 + 0x8)))));
    local_rdi = (local_rdi) + (Arg2);
    result = (local_rdi == local_r14) ? 1 : 0;
    result = (local_rdi) >> (12);
    result = (uint32_t)((result) ^ (*(uint32_t *)(local_rdi + 0x28)));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0x2A55AF)));
    result = (result) >> (16);
    result = (result) + (local_rdi);
    Arg2 = (*(uint16_t *)(local_rdi + 0x2C)) << (6);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(result)));
    local_rbx = ((uint32_t)(*(uint32_t *)(Arg2 + *(uint64_t *)(local_r15 + 0x140 + 0x18) * 1 + 0x48))) * ((uint32_t)((uint32_t)(Arg3)));
    local_rbx = (local_rbx) >> (32);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) * ((uint32_t)((uint16_t)(result))));
    if (((uint32_t)(Arg3)) != ((uint32_t)(result))) goto loc_00B83074;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x140 + 0x18) + 0x4C))))) >> (13));
    result = (uint32_t)((result) & (0x3FFFFULL));
    Arg3 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x140 + 0x18) + 0x4C))) >> (4);
    Arg3 = (uint32_t)((Arg3) & (511));
    Arg4 = (uint32_t)((1) << ((uint8_t)((uint16_t)(result))));
    Arg1 = (uint32_t)(((uint16_t)(result)) + (-2));
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(result)));
    *(uint32_t *)(local_rbp - 0x49) = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (63));
    result = (local_rbx) >> (6);
loc_00B82E0B:
    *(uint64_t *)(local_rbp - 0x61) = *(uint64_t *)(local_rdi + 0x10);
    Arg1 = (*(uint64_t *)(local_rdi + 0x10)) >> (48);
    *(uint64_t *)(local_rbp - 0x69) = *(uint64_t *)(local_rdi + 0x10);
    if (((uint8_t)(Arg1)) == 1) {
        *(uint8_t *)(local_rbp - 0x63) = 2;
    }
    if (local_r14 != 0) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(local_r15 + 0x140 + 0x18) + 0x50);
        Arg1 = *(uint16_t *)(local_rbp - 0x69);
        Arg2 = (uint32_t)(Arg3);
        *(uint16_t *)(local_r14) = (uint16_t)(Arg1);
        Arg2 = (uint32_t)((Arg2) ^ (*(uint32_t *)(local_r14)));
        Arg1 = (uint8_t)(Arg1);
        Arg1 = local_rbx + 1;
        Arg3 = (Arg3) >> (32);
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg3)));
        *(uint16_t *)(local_rbp - 0x69) = (uint16_t)(Arg1);
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(local_r14)));
        *(uint32_t *)(local_r14 + 0x8) = (uint32_t)(Arg2);
    }
    Arg2 = (*(uint16_t *)(local_rdi + 0x2C)) << (6);
    if (condition_is_not_equal) goto loc_00B82E0B;
    if ((*(uint8_t *)(local_rbp - 0x5B)) != 1) goto loc_00B83074;
    Arg4 = (uint32_t)((*(uint16_t *)(local_rbp - 0x5D)) << (6));
    Arg4 = (Arg4) + (*(uint64_t *)(local_r15 + 0x140 + 0x18));
    Arg2 = (uint32_t)((*(uint64_t *)(Arg4 + 0x8)) & (0xFFFULL));
    Arg3 = (uint32_t)((*(uint64_t *)(local_rdi + 0x18)) & (0xFFFULL));
    Arg1 = (*(uint64_t *)(Arg4 + 0x8)) - (Arg2);
    Arg1 = (Arg1) | (Arg3);
    *(uint64_t *)(local_rdi + 0x18) = Arg1;
    Arg1 = (local_rdi) | (Arg2);
    if (condition_is_equal) goto loc_00B83074;
loc_00B82ECC:
    Arg1 = (*(uint64_t *)(local_rdi + 0x18)) ^ (*(uint64_t *)(Arg4 + 0x8));
    Arg2 = (uint32_t)((*(uint64_t *)(Arg4 + 0x8)) & (0xFFFULL));
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(local_rdi + 0x18));
    *(uint64_t *)(local_rdi + 0x18) = Arg1;
    Arg2 = (Arg2) | (local_rdi);
    if ((*(uint64_t *)(Arg4 + 0x8)) != (*(uint64_t *)(Arg4 + 0x8))) goto loc_00B82ECC;
    goto loc_00B83074;
loc_00B82EFF:
    Arg1 = -(*(uint64_t *)(local_rbp - 0x61));
    if ((*(uint64_t *)(*(uint64_t *)(Arg4 + 0x8) + 0x48)) == 0) goto loc_00B82C2F;
    if (((*(uint8_t *)(*(uint64_t *)(Arg4 + 0x8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 8 + 0x38)) & (1)) != 0) goto loc_00B82C2F;
    Arg4 = (*(uint64_t *)(local_rbp - 0x61) * 4 + 63) & (-64);
    if (Arg4 == 64) { Arg4 = 128; }
loc_00B82F66:
    if (Arg1 >= (*(uint64_t *)(*(uint64_t *)(Arg4 + 0x8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 8 + 0x38))) goto loc_00B82C2F;
    if ((Arg4 + Arg1 * 1) >= (*(uint64_t *)(*(uint64_t *)(Arg4 + 0x8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))) * 8 + 0x38))) goto loc_00B82C2F;
    goto loc_00B82F66;
loc_00B82F8D:
    Arg4 = 0;
    v_stack_p28 = local_r12;
    v_stack_p20 = local_r12;
    result = RtlpLogHeapFailure(Arg4 + 9, *(uint64_t *)(Arg4 + Arg1 * 1 + 0x38), local_r14, Arg4);
    goto loc_00B83074;
loc_00B83074:
    local_rsp = (local_rsp) + (224);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=poolcode&rva=0x00B82950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
