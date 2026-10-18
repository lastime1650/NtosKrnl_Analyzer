# sub_0035FB85

- RVA: `0x0035FB85`–`0x003602E2` (길이 `1,885` bytes)
- VA: `0x000000014035FB85`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079C44`
- 디코드: `453`개 명령, `1,885/1,885` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **18**

### Outgoing calls
- `0x0035FCD9` → [VfPtFreePoolNotification](../../pagevrfy/BB/VfPtFreePoolNotification_function_00BB96DC.md) (function, `0x00BB96DC`)
- `0x0035FE69` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0035FE91` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (function, `0x00BB8FC0`)
- `0x0035FEE7` → [RtlCSparseBitmapBitmaskRead](../36/RtlCSparseBitmapBitmaskRead_function_0036190C.md) (function, `0x0036190C`)
- `0x003601EE` → [RtlpLogHeapFailure](RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x00360210` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (function, `0x00BB8FC0`)
- `0x003602AD` → [ExpRemovePoolTrackerExpansion](../36/ExpRemovePoolTrackerExpansion_function_00361300.md) (function, `0x00361300`)
- `0x003602B8` → [RtlpHpFreeHeap](RtlpHpFreeHeap_function_0035F600.md) (function, `0x0035F600`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0035FBDC` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0035FCAF` → RVA `0x00FC6BD0` (`ALMOSTRO`; read)
- `0x0035FCDE` → RVA `0x00FC514C` (`ALMOSTRO`; read)
- `0x0035FCF8` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0035FD15` → RVA `0x00EFED58` (`.data`; read)
- `0x0035FD6D` → RVA `0x00EFAD00` (`.data`; read)
- `0x0035FD94` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0035FDA1` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0035FDB6` → RVA `0x00EFAD00` (`.data`; read/write)
- `0x0035FDC6` → RVA `0x00EFED48` (`.data`; read)
- `0x0035FDD0` → RVA `0x00EFED40` (`.data`; read)
- `0x0035FE09` → RVA `0x00EEEF40` (`.data`; read)
- `0x0035FE10` → RVA `0x00EEEF60` (`.data`; read)
- `0x0035FE96` → RVA `0x00FCEC68` (`ALMOSTRO`; read)
- `0x0035FED2` → RVA `0x00E68610` (`.data`; read)
- `0x0035FED9` → RVA `0x00E68608` (`.data`; read)
- `0x0035FF21` → RVA `0x00E28300` (`.data`; read)
- `0x0035FF96` → RVA `0x00E28308` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0035FCD9` → [VfPtFreePoolNotification](../../pagevrfy/BB/VfPtFreePoolNotification_function_00BB96DC.md) (`.text` → `PAGEVRFY`)
  - `0x0035FE91` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (`.text` → `PAGEVRFY`)
  - `0x00360210` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (`.text` → `PAGEVRFY`)
- call이 아닌 외부 분기/꼬리 이동: **31**
  - `0x0035FBBD` → [sub_003602E3 + 0x1D](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x0035FBE8` → [sub_003602E3 + 0x10F](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x0035FC3E` → [sub_003602E3](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x0035FCBE` → [sub_00360968 + 0x3E2](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FD00` → [sub_00360968 + 0x47D](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FD57` → [sub_003602E3 + 0x57F](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x0035FD9B` → [sub_003602E3 + 0x522](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x0035FDAC` → [sub_003602E3 + 0x4B1](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x0035FDC0` → [sub_00360968 + 0x5F](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FDE5` → [sub_00360968 + 0x1A6](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FDFF` → [sub_00360968 + 0x1A6](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FE23` → [sub_00360968 + 0x762](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FE34` → [sub_003602E3 + 0xD](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x0035FE5F` → [sub_00360968 + 0x4D1](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FE73` → [sub_00360968 + 0x19D](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FE9D` → [sub_00360968 + 0x22C](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FEB4` → [sub_00360968 + 0x2D5](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FEEF` → [sub_00360968 + 0x59E](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FEF8` → [sub_00360968 + 0x59E](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FF08` → [sub_00360968 + 0x2B3](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0035FF77` → [sub_003602E3 + 0x3DE](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00360019` → [sub_00360968 + 0x674](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x00360023` → [sub_00360968 + 0x629](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x00360044` → [sub_003602E3 + 0x54A](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x003600BA` → [sub_003602E3 + 0x5B2](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x0036014D` → [sub_003602E3 + 0x4D0](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x003601CA` → [sub_00360968 + 0x5EF](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x00360237` → [sub_00360968 + 0x533](../36/Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0036028A` → [sub_003602E3 + 0x3C3](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00360292` → [sub_003602E3 + 0x5FB](../36/Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x003602DD` → [sub_003612E1](../36/Unknown_function_003612E1.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0035FB85  48 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rbx
0035FB8D  48 89 B4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rsi
0035FB95  48 89 BC 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdi
0035FB9D  4C 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r14
0035FBA5  85 C0                           test eax, eax
0035FBA7  0F 85 5C 02 00 00               jne 0x14035fe09
0035FBAD  BA 80 00 00 00                  mov edx, 0x80
0035FBB2  44 8D 42 82                     lea r8d, [rdx - 0x7e]
0035FBB6  49 F7 C4 FF 0F 00 00            test r12, 0xfff
0035FBBD  0F 84 3D 07 00 00               je 0x140360300
0035FBC3  41 0F B6 44 24 F3               movzx eax, byte ptr [r12 - 0xd]
0035FBC9  49 8D 74 24 F0                  lea rsi, [r12 - 0x10]
0035FBCE  48 89 75 7F                     mov qword ptr [rbp + 0x7f], rsi
0035FBD2  48 BB 00 00 00 00 00 80 FF FF   movabs rbx, 0xffff800000000000
0035FBDC  4C 8D 05 1D 04 CA FF            lea r8, [rip - 0x35fbe3]
0035FBE3  8D 7A 7F                        lea edi, [rdx + 0x7f]
0035FBE6  A8 08                           test al, 8
0035FBE8  0F 85 04 08 00 00               jne 0x1403603f2
0035FBEE  F6 46 03 04                     test byte ptr [rsi + 3], 4
0035FBF2  74 17                           je 0x14035fc0b
0035FBF4  0F B7 06                        movzx eax, word ptr [rsi]
0035FBF7  66 23 C7                        and ax, di
0035FBFA  0F B7 C8                        movzx ecx, ax
0035FBFD  48 F7 D9                        neg rcx
0035FC00  48 C1 E1 04                     shl rcx, 4
0035FC04  48 03 F1                        add rsi, rcx
0035FC07  80 4E 03 04                     or byte ptr [rsi + 3], 4
0035FC0B  44 0F B6 46 03                  movzx r8d, byte ptr [rsi + 3]
0035FC10  B9 00 01 00 00                  mov ecx, 0x100
0035FC15  8B 5E 04                        mov ebx, dword ptr [rsi + 4]
0035FC18  41 F6 C0 01                     test r8b, 1
0035FC1C  45 8B C8                        mov r9d, r8d
0035FC1F  48 0F 44 CA                     cmove rcx, rdx
0035FC23  48 8B D1                        mov rdx, rcx
0035FC26  48 83 CA 04                     or rdx, 4
0035FC2A  41 F6 C0 20                     test r8b, 0x20
0035FC2E  48 0F 44 D1                     cmove rdx, rcx
0035FC32  48 83 CA 02                     or rdx, 2
0035FC36  48 89 55 97                     mov qword ptr [rbp - 0x69], rdx
0035FC3A  41 83 E1 08                     and r9d, 8
0035FC3E  0F 85 9F 06 00 00               jne 0x1403602e3
0035FC44  48 89 75 7F                     mov qword ptr [rbp + 0x7f], rsi
0035FC48  41 F6 C0 DE                     test r8b, 0xde
0035FC4C  74 4D                           je 0x14035fc9b
0035FC4E  48 8B CA                        mov rcx, rdx
0035FC51  48 83 C9 08                     or rcx, 8
0035FC55  41 F6 C0 04                     test r8b, 4
0035FC59  48 0F 44 CA                     cmove rcx, rdx
0035FC5D  48 8B D1                        mov rdx, rcx
0035FC60  48 0F BA EA 09                  bts rdx, 9
0035FC65  41 F6 C0 80                     test r8b, 0x80
0035FC69  48 0F 44 D1                     cmove rdx, rcx
0035FC6D  48 8B CA                        mov rcx, rdx
0035FC70  48 0F BA E9 0A                  bts rcx, 0xa
0035FC75  41 F6 C0 40                     test r8b, 0x40
0035FC79  48 0F 44 CA                     cmove rcx, rdx
0035FC7D  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
0035FC81  45 85 C9                        test r9d, r9d
0035FC84  75 15                           jne 0x14035fc9b
0035FC86  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
0035FC8A  41 F6 C0 10                     test r8b, 0x10
0035FC8E  74 0B                           je 0x14035fc9b
0035FC90  4C 8B F1                        mov r14, rcx
0035FC93  49 83 CE 20                     or r14, 0x20
0035FC97  4C 89 75 97                     mov qword ptr [rbp - 0x69], r14
0035FC9B  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
0035FC9F  48 8D 7E 10                     lea rdi, [rsi + 0x10]
0035FCA3  44 0F B6 F0                     movzx r14d, al
0035FCA7  49 C1 E6 04                     shl r14, 4
0035FCAB  4C 89 75 8F                     mov qword ptr [rbp - 0x71], r14
0035FCAF  8B 05 1B 6F C6 00               mov eax, dword ptr [rip + 0xc66f1b]
0035FCB5  4C 8B 7D 97                     mov r15, qword ptr [rbp - 0x69]
0035FCB9  A9 07 02 00 00                  test eax, 0x207
0035FCBE  0F 85 86 10 00 00               jne 0x140360d4a
0035FCC4  8B 05 06 6F C6 00               mov eax, dword ptr [rip + 0xc66f06]
0035FCCA  A8 10                           test al, 0x10
0035FCCC  74 10                           je 0x14035fcde
0035FCCE  4D 8B CC                        mov r9, r12
0035FCD1  4D 8B C6                        mov r8, r14
0035FCD4  8B D3                           mov edx, ebx
0035FCD6  48 8B CE                        mov rcx, rsi
0035FCD9  E8 FE 99 85 00                  call 0x140bb96dc
0035FCDE  8B 05 68 54 C6 00               mov eax, dword ptr [rip + 0xc65468]
0035FCE4  45 33 F6                        xor r14d, r14d
0035FCE7  44 89 75 A3                     mov dword ptr [rbp - 0x5d], r14d
0035FCEB  44 88 75 6F                     mov byte ptr [rbp + 0x6f], r14b
0035FCEF  44 88 75 87                     mov byte ptr [rbp - 0x79], r14b
0035FCF3  3B D8                           cmp ebx, eax
0035FCF5  75 01                           jne 0x14035fcf8
0035FCF7  CC                              int3
0035FCF8  8B 05 06 6E C6 00               mov eax, dword ptr [rip + 0xc66e06]
0035FCFE  A8 41                           test al, 0x41
0035FD00  0F 85 DF 10 00 00               jne 0x140360de5
0035FD06  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0035FD0E  4C 8D 1D EB 02 CA FF            lea r11, [rip - 0x35fd15]
0035FD15  4C 8B 0D 3C F0 B9 00            mov r9, qword ptr [rip + 0xb9f03c]
0035FD1C  4D 8B 9C C3 20 AD EF 00         mov r11, qword ptr [r11 + rax*8 + 0xefad20]
0035FD24  8B C3                           mov eax, ebx
0035FD26  48 69 C8 5F 9E 00 00            imul rcx, rax, 0x9e5f
0035FD2D  48 8B D1                        mov rdx, rcx
0035FD30  48 C1 EA 20                     shr rdx, 0x20
0035FD34  33 D1                           xor edx, ecx
0035FD36  41 23 D1                        and edx, r9d
0035FD39  44 8B D2                        mov r10d, edx
0035FD3C  8B C2                           mov eax, edx
0035FD3E  48 8D 0C 80                     lea rcx, [rax + rax*4]
0035FD42  48 03 C9                        add rcx, rcx
0035FD45  41 8B 04 CB                     mov eax, dword ptr [r11 + rcx*8]
0035FD49  4D 8D 04 CB                     lea r8, [r11 + rcx*8]
0035FD4D  3B C3                           cmp eax, ebx
0035FD4F  0F 84 F3 03 00 00               je 0x140360148
0035FD55  85 C0                           test eax, eax
0035FD57  0F 84 05 0B 00 00               je 0x140360862
0035FD5D  8D 42 01                        lea eax, [rdx + 1]
0035FD60  41 23 C1                        and eax, r9d
0035FD63  8B D0                           mov edx, eax
0035FD65  41 3B C2                        cmp eax, r10d
0035FD68  75 D2                           jne 0x14035fd3c
0035FD6A  0F 57 C0                        xorps xmm0, xmm0
0035FD6D  48 8D 0D 8C AF B9 00            lea rcx, [rip + 0xb9af8c]
0035FD74  0F 11 45 B7                     movups xmmword ptr [rbp - 0x49], xmm0
0035FD78  33 C0                           xor eax, eax
0035FD7A  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
0035FD7E  4C 89 75 B7                     mov qword ptr [rbp - 0x49], r14
0035FD82  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0035FD86  90                              nop
0035FD87  44 0F 20 C7                     mov rdi, cr8
0035FD8B  B8 02 00 00 00                  mov eax, 2
0035FD90  44 0F 22 C0                     mov cr8, rax
0035FD94  44 39 35 85 6F C6 00            cmp dword ptr [rip + 0xc66f85], r14d
0035FD9B  0F 85 64 0A 00 00               jne 0x140360805
0035FDA1  F6 05 5E 6D C6 00 21            test byte ptr [rip + 0xc66d5e], 0x21
0035FDA8  40 88 7D C7                     mov byte ptr [rbp - 0x39], dil
0035FDAC  0F 85 E2 09 00 00               jne 0x140360794
0035FDB2  48 8D 55 B7                     lea rdx, [rbp - 0x49]
0035FDB6  48 87 15 43 AF B9 00            xchg qword ptr [rip + 0xb9af43], rdx
0035FDBD  48 85 D2                        test rdx, rdx
0035FDC0  0F 85 01 0C 00 00               jne 0x1403609c7
0035FDC6  4C 8B 0D 7B EF B9 00            mov r9, qword ptr [rip + 0xb9ef7b]
0035FDCD  41 8B D6                        mov edx, r14d
0035FDD0  4C 8B 15 69 EF B9 00            mov r10, qword ptr [rip + 0xb9ef69]
0035FDD7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0035FDE0  8B C2                           mov eax, edx
0035FDE2  49 3B C1                        cmp rax, r9
0035FDE5  0F 83 23 0D 00 00               jae 0x140360b0e
0035FDEB  4C 8D 04 80                     lea r8, [rax + rax*4]
0035FDEF  49 C1 E0 04                     shl r8, 4
0035FDF3  4D 03 C2                        add r8, r10
0035FDF6  41 8B 00                        mov eax, dword ptr [r8]
0035FDF9  3B C3                           cmp eax, ebx
0035FDFB  74 32                           je 0x14035fe2f
0035FDFD  85 C0                           test eax, eax
0035FDFF  0F 84 09 0D 00 00               je 0x140360b0e
0035FE05  FF C2                           inc edx
0035FE07  EB D7                           jmp 0x14035fde0
0035FE09  48 8D 05 30 F1 B8 00            lea rax, [rip + 0xb8f130]
0035FE10  48 8D 0D 49 F1 B8 00            lea rcx, [rip + 0xb8f149]
0035FE17  48 3B C1                        cmp rax, rcx
0035FE1A  0F 8D 8D FD FF FF               jge 0x14035fbad
0035FE20  4C 3B 28                        cmp r13, qword ptr [rax]
0035FE23  0F 84 A1 12 00 00               je 0x1403610ca
0035FE29  48 83 C0 08                     add rax, 8
0035FE2D  EB E8                           jmp 0x14035fe17
0035FE2F  49 0F BA E7 08                  bt r15, 8
0035FE34  0F 82 B6 04 00 00               jb 0x1403602f0
0035FE3A  41 B9 01 00 00 00               mov r9d, 1
0035FE40  49 8D 50 08                     lea rdx, [r8 + 8]
0035FE44  49 8D 40 18                     lea rax, [r8 + 0x18]
0035FE48  F0 48 FF 00                     lock inc qword ptr [rax]
0035FE4C  4C 8B 55 8F                     mov r10, qword ptr [rbp - 0x71]
0035FE50  49 8B CA                        mov rcx, r10
0035FE53  48 F7 D9                        neg rcx
0035FE56  F0 48 0F C1 0A                  lock xadd qword ptr [rdx], rcx
0035FE5B  4D 39 70 48                     cmp qword ptr [r8 + 0x48], r14
0035FE5F  0F 85 D4 0F 00 00               jne 0x140360e39
0035FE65  48 8D 4D B7                     lea rcx, [rbp - 0x49]
0035FE69  E8 72 2E FE FF                  call 0x140342ce0
0035FE6E  49 0F BA E7 0A                  bt r15, 0xa
0035FE73  0F 83 8C 0C 00 00               jae 0x140360b05
0035FE79  49 C1 EF 08                     shr r15, 8
0035FE7D  45 33 C9                        xor r9d, r9d
0035FE80  41 83 E7 01                     and r15d, 1
0035FE84  49 8B CC                        mov rcx, r12
0035FE87  45 8B C7                        mov r8d, r15d
0035FE8A  4C 8B 7D 8F                     mov r15, qword ptr [rbp - 0x71]
0035FE8E  49 8B D7                        mov rdx, r15
0035FE91  E8 2A 91 85 00                  call 0x140bb8fc0
0035FE96  44 38 35 CB ED C6 00            cmp byte ptr [rip + 0xc6edcb], r14b
0035FE9D  0F 85 F1 0C 00 00               jne 0x140360b94
0035FEA3  49 8B 55 38                     mov rdx, qword ptr [r13 + 0x38]
0035FEA7  49 8D 87 FF FD FF FF            lea rax, [r15 - 0x201]
0035FEAE  48 3D 7F 0D 00 00               cmp rax, 0xd7f
0035FEB4  0F 86 83 0D 00 00               jbe 0x140360c3d
0035FEBA  4C 8D 3D 3F 01 CA FF            lea r15, [rip - 0x35fec1]
0035FEC1  66 85 F6                        test si, si
0035FEC4  74 09                           je 0x14035fecf
0035FEC6  49 8D 9D 40 01 00 00            lea rbx, [r13 + 0x140]
0035FECD  EB 3F                           jmp 0x14035ff0e
0035FECF  48 8B D6                        mov rdx, rsi
0035FED2  48 8D 0D 37 87 B0 00            lea rcx, [rip + 0xb08737]
0035FED9  48 2B 15 28 87 B0 00            sub rdx, qword ptr [rip + 0xb08728]
0035FEE0  48 C1 EA 14                     shr rdx, 0x14
0035FEE4  48 03 D2                        add rdx, rdx
0035FEE7  E8 20 1A 00 00                  call 0x14036190c
0035FEEC  48 85 C0                        test rax, rax
0035FEEF  0F 84 11 10 00 00               je 0x140360f06
0035FEF5  83 F8 03                        cmp eax, 3
0035FEF8  0F 84 08 10 00 00               je 0x140360f06
0035FEFE  49 8D 9D 40 01 00 00            lea rbx, [r13 + 0x140]
0035FF05  83 F8 02                        cmp eax, 2
0035FF08  0F 84 0D 0D 00 00               je 0x140360c1b
0035FF0E  4C 8B 0B                        mov r9, qword ptr [rbx]
0035FF11  48 8B C3                        mov rax, rbx
0035FF14  49 8B D1                        mov rdx, r9
0035FF17  48 23 D6                        and rdx, rsi
0035FF1A  48 33 42 10                     xor rax, qword ptr [rdx + 0x10]
0035FF1E  48 33 C2                        xor rax, rdx
0035FF21  48 33 05 D8 83 AC 00            xor rax, qword ptr [rip + 0xac83d8]
0035FF28  0F 85 A7 02 00 00               jne 0x1403601d5
0035FF2E  44 0F B6 53 08                  movzx r10d, byte ptr [rbx + 8]
0035FF33  44 8B C6                        mov r8d, esi
0035FF36  44 2B C2                        sub r8d, edx
0035FF39  41 8B CA                        mov ecx, r10d
0035FF3C  41 D3 E8                        shr r8d, cl
0035FF3F  49 C1 E0 05                     shl r8, 5
0035FF43  4C 03 C2                        add r8, rdx
0035FF46  41 0F B6 40 1A                  movzx eax, byte ptr [r8 + 0x1a]
0035FF4B  48 F7 D8                        neg rax
0035FF4E  48 C1 E0 05                     shl rax, 5
0035FF52  4C 03 C0                        add r8, rax
0035FF55  49 8B F8                        mov rdi, r8
0035FF58  48 2B FA                        sub rdi, rdx
0035FF5B  48 C1 FF 05                     sar rdi, 5
0035FF5F  45 0F B6 58 18                  movzx r11d, byte ptr [r8 + 0x18]
0035FF64  48 D3 E7                        shl rdi, cl
0035FF67  48 03 FA                        add rdi, rdx
0035FF6A  48 3B FE                        cmp rdi, rsi
0035FF6D  0F 94 C0                        sete al
0035FF70  42 8D 0C 18                     lea ecx, [rax + r11]
0035FF74  80 F9 0B                        cmp cl, 0xb
0035FF77  0F 85 44 07 00 00               jne 0x1403606c1
0035FF7D  48 8B 73 18                     mov rsi, qword ptr [rbx + 0x18]
0035FF81  48 8B C7                        mov rax, rdi
0035FF84  0F B7 57 2C                     movzx edx, word ptr [rdi + 0x2c]
0035FF88  4C 8B 7D 7F                     mov r15, qword ptr [rbp + 0x7f]
0035FF8C  48 C1 E8 0C                     shr rax, 0xc
0035FF90  45 8B C7                        mov r8d, r15d
0035FF93  33 47 28                        xor eax, dword ptr [rdi + 0x28]
0035FF96  33 05 6C 83 AC 00               xor eax, dword ptr [rip + 0xac836c]
0035FF9C  0F B7 C8                        movzx ecx, ax
0035FF9F  48 C1 E8 10                     shr rax, 0x10
0035FFA3  48 03 C7                        add rax, rdi
0035FFA6  48 C1 E2 06                     shl rdx, 6
0035FFAA  44 2B C0                        sub r8d, eax
0035FFAD  41 8B C0                        mov eax, r8d
0035FFB0  8B 5C 32 48                     mov ebx, dword ptr [rdx + rsi + 0x48]
0035FFB4  48 0F AF D8                     imul rbx, rax
0035FFB8  48 C1 EB 20                     shr rbx, 0x20
0035FFBC  8B C3                           mov eax, ebx
0035FFBE  0F AF C1                        imul eax, ecx
0035FFC1  44 3B C0                        cmp r8d, eax
0035FFC4  0F 85 F3 02 00 00               jne 0x1403602bd
0035FFCA  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0035FFD3  41 B9 01 00 00 00               mov r9d, 1
0035FFD9  44 8B 46 4C                     mov r8d, dword ptr [rsi + 0x4c]
0035FFDD  41 8B C0                        mov eax, r8d
0035FFE0  C1 E8 0D                        shr eax, 0xd
0035FFE3  25 FF FF 03 00                  and eax, 0x3ffff
0035FFE8  49 C1 E8 04                     shr r8, 4
0035FFEC  0F BD C8                        bsr ecx, eax
0035FFEF  41 81 E0 FF 01 00 00            and r8d, 0x1ff
0035FFF6  41 D3 E1                        shl r9d, cl
0035FFF9  83 C1 FE                        add ecx, -2
0035FFFC  44 33 C8                        xor r9d, eax
0035FFFF  89 4D AB                        mov dword ptr [rbp - 0x55], ecx
00360002  48 8B 82 B0 8B 00 00            mov rax, qword ptr [rdx + 0x8bb0]
00360009  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0036000D  4A 8B 44 C8 08                  mov rax, qword ptr [rax + r9*8 + 8]
00360012  4A 8B 04 C0                     mov rax, qword ptr [rax + r8*8]
00360016  48 85 C0                        test rax, rax
00360019  0F 84 BD 0F 00 00               je 0x140360fdc
0036001F  66 3B 47 2E                     cmp ax, word ptr [rdi + 0x2e]
00360023  0F 84 68 0F 00 00               je 0x140360f91
00360029  8B C3                           mov eax, ebx
0036002B  4C 8B CB                        mov r9, rbx
0036002E  83 E0 3F                        and eax, 0x3f
00360031  0F B6 C8                        movzx ecx, al
00360034  48 8B C3                        mov rax, rbx
00360037  48 C1 E8 06                     shr rax, 6
0036003B  48 8B 44 C7 40                  mov rax, qword ptr [rdi + rax*8 + 0x40]
00360040  48 0F A3 C8                     bt rax, rcx
00360044  0F 83 E3 07 00 00               jae 0x14036082d
0036004A  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0036004E  48 8B C8                        mov rcx, rax
00360051  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00360055  48 C1 E9 30                     shr rcx, 0x30
00360059  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0036005D  80 F9 01                        cmp cl, 1
00360060  75 07                           jne 0x140360069
00360062  C6 85 85 00 00 00 02            mov byte ptr [rbp + 0x85], 2
00360069  4D 85 FF                        test r15, r15
0036006C  74 2C                           je 0x14036009a
0036006E  4C 8B 46 50                     mov r8, qword ptr [rsi + 0x50]
00360072  0F B7 4D 7F                     movzx ecx, word ptr [rbp + 0x7f]
00360076  41 8B D0                        mov edx, r8d
00360079  66 41 89 0F                     mov word ptr [r15], cx
0036007D  41 33 17                        xor edx, dword ptr [r15]
00360080  0F B6 C9                        movzx ecx, cl
00360083  D3 C2                           rol edx, cl
00360085  8D 4B 01                        lea ecx, [rbx + 1]
00360088  49 C1 E8 20                     shr r8, 0x20
0036008C  41 33 D0                        xor edx, r8d
0036008F  66 89 4D 7F                     mov word ptr [rbp + 0x7f], cx
00360093  41 33 D7                        xor edx, r15d
00360096  41 89 57 08                     mov dword ptr [r15 + 8], edx
0036009A  66 FF 85 81 00 00 00            inc word ptr [rbp + 0x81]
003600A1  0F B7 57 2C                     movzx edx, word ptr [rdi + 0x2c]
003600A5  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
003600A9  48 C1 E2 06                     shl rdx, 6
003600AD  F0 48 0F B1 4F 10               lock cmpxchg qword ptr [rdi + 0x10], rcx
003600B3  75 99                           jne 0x14036004e
003600B5  44 38 74 32 5C                  cmp byte ptr [rdx + rsi + 0x5c], r14b
003600BA  0F 84 D5 07 00 00               je 0x140360895
003600C0  80 7D 9D 01                     cmp byte ptr [rbp - 0x63], 1
003600C4  0F 85 F3 01 00 00               jne 0x1403602bd
003600CA  44 0F B7 4D 9B                  movzx r9d, word ptr [rbp - 0x65]
003600CF  41 C1 E1 06                     shl r9d, 6
003600D3  4C 03 CE                        add r9, rsi
003600D6  41 0F 0D 49 08                  prefetchw byte ptr [r9 + 8]
003600DB  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
003600DF  4C 8B 57 18                     mov r10, qword ptr [rdi + 0x18]
003600E3  48 8B D0                        mov rdx, rax
003600E6  81 E2 FF 0F 00 00               and edx, 0xfff
003600EC  4D 8B C2                        mov r8, r10
003600EF  41 81 E0 FF 0F 00 00            and r8d, 0xfff
003600F6  48 8B C8                        mov rcx, rax
003600F9  48 2B CA                        sub rcx, rdx
003600FC  49 0B C8                        or rcx, r8
003600FF  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
00360103  48 8B CF                        mov rcx, rdi
00360106  48 0B CA                        or rcx, rdx
00360109  F0 49 0F B1 49 08               lock cmpxchg qword ptr [r9 + 8], rcx
0036010F  0F 84 A8 01 00 00               je 0x1403602bd
00360115  48 8B D0                        mov rdx, rax
00360118  49 8B CA                        mov rcx, r10
0036011B  48 33 C8                        xor rcx, rax
0036011E  81 E2 FF 0F 00 00               and edx, 0xfff
00360124  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
0036012B  4C 8B C0                        mov r8, rax
0036012E  49 33 CA                        xor rcx, r10
00360131  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
00360135  48 0B D7                        or rdx, rdi
00360138  F0 49 0F B1 51 08               lock cmpxchg qword ptr [r9 + 8], rdx
0036013E  49 3B C0                        cmp rax, r8
00360141  75 D2                           jne 0x140360115
00360143  E9 75 01 00 00                  jmp 0x1403602bd
00360148  49 0F BA E7 08                  bt r15, 8
0036014D  0F 83 60 06 00 00               jae 0x1403607b3
00360153  45 8B CE                        mov r9d, r14d
00360156  49 8D 50 20                     lea rdx, [r8 + 0x20]
0036015A  49 8D 40 30                     lea rax, [r8 + 0x30]
0036015E  4D 8B D6                        mov r10, r14
00360161  F0 48 FF 00                     lock inc qword ptr [rax]
00360165  48 8B 5D 8F                     mov rbx, qword ptr [rbp - 0x71]
00360169  48 8B CB                        mov rcx, rbx
0036016C  48 F7 D9                        neg rcx
0036016F  F0 48 0F C1 0A                  lock xadd qword ptr [rdx], rcx
00360174  4D 39 70 48                     cmp qword ptr [r8 + 0x48], r14
00360178  0F 84 F0 FC FF FF               je 0x14035fe6e
0036017E  41 8B C1                        mov eax, r9d
00360181  41 F6 44 C0 38 01               test byte ptr [r8 + rax*8 + 0x38], 1
00360187  4D 8D 1C C0                     lea r11, [r8 + rax*8]
0036018B  0F 85 DD FC FF FF               jne 0x14035fe6e
00360191  49 8B 43 38                     mov rax, qword ptr [r11 + 0x38]
00360195  4C 8D 0C 9D 3F 00 00 00         lea r9, [rbx*4 + 0x3f]
0036019D  49 83 E1 C0                     and r9, 0xffffffffffffffc0
003601A1  BB 80 00 00 00                  mov ebx, 0x80
003601A6  49 83 F9 40                     cmp r9, 0x40
003601AA  4C 0F 44 CB                     cmove r9, rbx
003601AE  49 8D 1C 09                     lea rbx, [r9 + rcx]
003601B2  48 3B C8                        cmp rcx, rax
003601B5  0F 8D B3 FC FF FF               jge 0x14035fe6e
003601BB  48 3B D8                        cmp rbx, rax
003601BE  0F 8D AA FC FF FF               jge 0x14035fe6e
003601C4  F0 49 0F B1 5B 38               lock cmpxchg qword ptr [r11 + 0x38], rbx
003601CA  0F 84 87 0D 00 00               je 0x140360f57
003601D0  48 8B 0A                        mov rcx, qword ptr [rdx]
003601D3  EB D9                           jmp 0x1403601ae
003601D5  48 8B 53 38                     mov rdx, qword ptr [rbx + 0x38]
003601D9  B9 09 00 00 00                  mov ecx, 9
003601DE  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
003601E3  4C 8B C6                        mov r8, rsi
003601E6  45 33 C9                        xor r9d, r9d
003601E9  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
003601EE  E8 C9 B5 FF FF                  call 0x14035b7bc
003601F3  E9 C5 00 00 00                  jmp 0x1403602bd
003601F8  45 85 D2                        test r10d, r10d
003601FB  74 18                           je 0x140360215
003601FD  4D 85 DB                        test r11, r11
00360200  45 8B C7                        mov r8d, r15d
00360203  41 B9 01 00 00 00               mov r9d, 1
00360209  49 8B CC                        mov rcx, r12
0036020C  41 0F 95 C0                     setne r8b
00360210  E8 AB 8D 85 00                  call 0x140bb8fc0
00360215  8B 73 04                        mov esi, dword ptr [rbx + 4]
00360218  8B 05 2E 4F C6 00               mov eax, dword ptr [rip + 0xc64f2e]
0036021E  44 89 7D 9F                     mov dword ptr [rbp - 0x61], r15d
00360222  44 88 7D 67                     mov byte ptr [rbp + 0x67], r15b
00360226  44 88 7D 77                     mov byte ptr [rbp + 0x77], r15b
0036022A  3B F0                           cmp esi, eax
0036022C  75 01                           jne 0x14036022f
0036022E  CC                              int3
0036022F  8B 05 CF 68 C6 00               mov eax, dword ptr [rip + 0xc668cf]
00360235  A8 41                           test al, 0x41
00360237  0F 85 5E 0C 00 00               jne 0x140360e9b
0036023D  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
00360245  48 83 E7 FB                     and rdi, 0xfffffffffffffffb
00360249  4C 8B 05 08 EB B9 00            mov r8, qword ptr [rip + 0xb9eb08]
00360250  8B C8                           mov ecx, eax
00360252  48 8D 05 A7 FD C9 FF            lea rax, [rip - 0x360259]
00360259  4C 8B 9C C8 20 AD EF 00         mov r11, qword ptr [rax + rcx*8 + 0xefad20]
00360261  48 69 CE 5F 9E 00 00            imul rcx, rsi, 0x9e5f
00360268  48 8B D1                        mov rdx, rcx
0036026B  48 C1 EA 20                     shr rdx, 0x20
0036026F  33 D1                           xor edx, ecx
00360271  41 23 D0                        and edx, r8d
00360274  44 8B D2                        mov r10d, edx
00360277  8B C2                           mov eax, edx
00360279  48 8D 0C 80                     lea rcx, [rax + rax*4]
0036027D  48 03 C9                        add rcx, rcx
00360280  41 8B 04 CB                     mov eax, dword ptr [r11 + rcx*8]
00360284  4D 8D 0C CB                     lea r9, [r11 + rcx*8]
00360288  3B C6                           cmp eax, esi
0036028A  0F 84 16 04 00 00               je 0x1403606a6
00360290  85 C0                           test eax, eax
00360292  0F 84 46 06 00 00               je 0x1403608de
00360298  8D 42 01                        lea eax, [rdx + 1]
0036029B  41 23 C0                        and eax, r8d
0036029E  8B D0                           mov edx, eax
003602A0  41 3B C2                        cmp eax, r10d
003602A3  75 D2                           jne 0x140360277
003602A5  4C 8B C7                        mov r8, rdi
003602A8  49 8B D6                        mov rdx, r14
003602AB  8B CE                           mov ecx, esi
003602AD  E8 4E 10 00 00                  call 0x140361300
003602B2  48 8B D3                        mov rdx, rbx
003602B5  49 8B CD                        mov rcx, r13
003602B8  E8 43 F3 FF FF                  call 0x14035f600
003602BD  48 8B BC 24 D0 00 00 00         mov rdi, qword ptr [rsp + 0xd0]
003602C5  48 8B B4 24 D8 00 00 00         mov rsi, qword ptr [rsp + 0xd8]
003602CD  48 8B 9C 24 E0 00 00 00         mov rbx, qword ptr [rsp + 0xe0]
003602D5  4C 8B B4 24 C8 00 00 00         mov r14, qword ptr [rsp + 0xc8]
003602DD  E9 FF 0F 00 00                  jmp 0x1403612e1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0035FB85(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;

    v_stack_pE0 = v_rbx;
    v_stack_pD8 = v_rsi;
    v_stack_pD0 = v_rdi;
    v_stack_pC8 = v_r14;
    if ((unsigned int)(result) != 0) goto loc_0035FE09;
loc_0035FBAD:
    *(unsigned __int64 *)(v_rbp + 127) = v_r12 - 16;
    result = *(unsigned __int8 *)(v_r12 - 13);
    v_rsi = v_r12 - 16;
    if (((*(unsigned __int8 *)(v_r12 - 16 + 3)) & (4)) != 0) {
        result = *(unsigned __int16 *)(v_r12 - 16);
        result = (unsigned __int16)((result) & ((unsigned __int16)(128 + 127)));
        a1 = (unsigned __int16)(result);
        a1 = -(a1);
        a1 = (a1) << (4);
        v_rsi = (v_r12 - 16) + (a1);
    }
    a1 = 256;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 3))) & (1)) == 0) { a1 = 128; }
    a2 = (a1) | (4);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 3))) & (32)) == 0) { a2 = a1; }
    a2 = (a2) | (2);
    *(unsigned __int64 *)(v_rbp - 105) = a2;
    a4 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rsi + 3)))) & (8));
    *(unsigned __int64 *)(v_rbp + 127) = v_rsi;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 3))) & (222)) == 0) goto loc_0035FC9B;
    a1 = (a2) | (8);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 3))) & (4)) == 0) { a1 = a2; }
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 3))) & (128)) == 0) { a1 = a1; }
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 3))) & (64)) == 0) { a1 = a1; }
    *(unsigned __int64 *)(v_rbp - 105) = a1;
    if ((unsigned int)(a4) != 0) goto loc_0035FC9B;
    *(unsigned __int64 *)(v_rbp - 105) = a1;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 3))) & (16)) != 0) {
        v_r14 = a1;
        v_r14 = (v_r14) | (32);
        *(unsigned __int64 *)(v_rbp - 105) = v_r14;
    }
    v_r14 = ((unsigned __int8)(*(unsigned __int16 *)(v_rsi + 2))) << (4);
    *(unsigned __int64 *)(v_rbp - 113) = v_r14;
    result = (unsigned int)(*(unsigned int *)(v_rip + 13004550));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13004550)))) & (16)) != 0) {
        a4 = v_r12;
        a3 = v_r14;
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4)));
        a1 = v_rsi;
        result = VfPtFreePoolNotification(a1, a2, a3, a4);
    }
    v_r14 = 0;
    *(unsigned int *)(v_rbp - 93) = 0;
    *(unsigned __int8 *)(v_rbp + 111) = 0;
    *(unsigned __int8 *)(v_rbp - 121) = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12997736))))) {
    }
    a1 = (a1) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4)))));
    a2 = (a1) >> (32);
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 12185660))));
loc_0035FD3C:
    a1 = ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4) + ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3538197 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 15707424) + a1 * 8)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4))))) goto loc_00360148;
    result = (unsigned int)((a2 + 1) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 12185660))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_0035FD3C;
    *(unsigned __int64 *)(v_rbp - 73) = v_xmm0;
    result = 0;
    *(unsigned __int64 *)(v_rbp - 65) = v_rip + 12169100;
    *(unsigned __int64 *)(v_rbp - 73) = 0;
    *(unsigned __int64 *)(v_rbp - 57) = 0;
    *(unsigned __int8 *)(v_rbp - 57) = (unsigned __int8)(v_cr8);
loc_0035FDE0:
    a3 = (0 + 0 * 4) << (4);
    a3 = (a3) + (*(unsigned __int64 *)(v_rip + 12185449));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4))))) goto loc_0035FE2F;
    a2 = (unsigned int)((0) + 1);
    goto loc_0035FDE0;
loc_0035FE09:
loc_0035FE17:
    if ((v_rip + 12120368) >= (v_rip + 12120393)) goto loc_0035FBAD;
    result = (v_rip + 12120368) + (8);
    goto loc_0035FE17;
loc_0035FE2F:
    a1 = -(*(unsigned __int64 *)(v_rbp - 113));
    result = KeReleaseInStackQueuedSpinLock(v_rbp - 73, a3 + 8, a3, 1);
loc_0035FE6E:
    v_r15 = (*(unsigned __int64 *)(v_rbp - 105)) >> (8);
    a4 = 0;
    v_r15 = (unsigned int)((v_r15) & (1));
    result = ViFreeTrackedPool(v_r12, *(unsigned __int64 *)(v_rbp - 113), (unsigned int)((unsigned int)(v_r15)), a4);
    if ((unsigned __int16)(v_rsi) == 0) goto loc_0035FECF;
    goto loc_0035FF0E;
loc_0035FECF:
    a2 = (v_rsi) - (*(unsigned __int64 *)(v_rip + 11568936));
    a2 = (a2) >> (20);
    a2 = (a2) + (a2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 11568951, a2, (unsigned int)((unsigned int)(v_r15)), a4);
loc_0035FF0E:
    a2 = (*(unsigned __int64 *)(v_r13 + 320)) & (v_rsi);
    result = (v_r13 + 320) ^ (*(unsigned __int64 *)(a2 + 16));
    result = (result) ^ (a2);
    result = (result) ^ (*(unsigned __int64 *)(v_rip + 11305944));
    if (condition_is_not_equal) goto loc_003601D5;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - ((unsigned int)(a2)));
    a3 = (unsigned int)((a3) >> ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r13 + 320 + 8))))));
    a3 = (a3) << (5);
    a3 = (a3) + (a2);
    result = -(*(unsigned __int8 *)(a3 + 26));
    result = (result) << (5);
    a3 = (a3) + (result);
    v_rdi = (a3) - (a2);
    v_rdi = (v_rdi) >> (5);
    v_rdi = (v_rdi) << ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r13 + 320 + 8)))));
    v_rdi = (v_rdi) + (a2);
    result = (v_rdi == v_rsi) ? 1 : 0;
    result = (v_rdi) >> (12);
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rdi + 40)));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11305836)));
    result = (result) >> (16);
    result = (result) + (v_rdi);
    a2 = (*(unsigned __int16 *)(v_rdi + 44)) << (6);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp + 127)))) - ((unsigned int)(result)));
    v_rbx = ((unsigned int)(*(unsigned int *)(a2 + *(unsigned __int64 *)(v_r13 + 320 + 24) * 1 + 72))) * ((unsigned int)((unsigned int)(a3)));
    v_rbx = (v_rbx) >> (32);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) * ((unsigned int)((unsigned __int16)(result))));
    if (((unsigned int)(a3)) != ((unsigned int)(result))) goto loc_003602BD;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r13 + 320 + 24) + 76))))) >> (13));
    result = (unsigned int)((result) & (0x3FFFFULL));
    a3 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r13 + 320 + 24) + 76))) >> (4);
    a3 = (unsigned int)((a3) & (511));
    a4 = (unsigned int)((1) << ((unsigned __int8)((unsigned __int16)(result))));
    a1 = (unsigned int)(((unsigned __int16)(result)) + (-2));
    a4 = (unsigned int)((a4) ^ ((unsigned int)(result)));
    *(unsigned int *)(v_rbp - 85) = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (63));
    result = (v_rbx) >> (6);
loc_0036004E:
    *(unsigned __int64 *)(v_rbp - 105) = *(unsigned __int64 *)(v_rdi + 16);
    a1 = (*(unsigned __int64 *)(v_rdi + 16)) >> (48);
    *(unsigned __int64 *)(v_rbp + 127) = *(unsigned __int64 *)(v_rdi + 16);
    if (((unsigned __int8)(a1)) == 1) {
        *(unsigned __int8 *)(v_rbp + 133) = 2;
    }
    if (*(unsigned __int64 *)(v_rbp + 127) != 0) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 320 + 24) + 80);
        a1 = *(unsigned __int16 *)(v_rbp + 127);
        a2 = (unsigned int)(a3);
        *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 127)) = (unsigned __int16)(a1);
        a2 = (unsigned int)((a2) ^ (*(unsigned int *)(*(unsigned __int64 *)(v_rbp + 127))));
        a1 = (unsigned __int8)(a1);
        a1 = v_rbx + 1;
        a3 = (a3) >> (32);
        a2 = (unsigned int)((a2) ^ ((unsigned int)(a3)));
        *(unsigned __int16 *)(v_rbp + 127) = (unsigned __int16)(a1);
        a2 = (unsigned int)((a2) ^ ((unsigned int)(*(unsigned __int64 *)(v_rbp + 127))));
        *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 127) + 8) = (unsigned int)(a2);
    }
    a2 = (*(unsigned __int16 *)(v_rdi + 44)) << (6);
    if (condition_is_not_equal) goto loc_0036004E;
    if ((*(unsigned __int8 *)(v_rbp - 99)) != 1) goto loc_003602BD;
    a4 = (unsigned int)((*(unsigned __int16 *)(v_rbp - 101)) << (6));
    a4 = (a4) + (*(unsigned __int64 *)(v_r13 + 320 + 24));
    a2 = (unsigned int)((*(unsigned __int64 *)(a4 + 8)) & (0xFFFULL));
    a3 = (unsigned int)((*(unsigned __int64 *)(v_rdi + 24)) & (0xFFFULL));
    a1 = (*(unsigned __int64 *)(a4 + 8)) - (a2);
    a1 = (a1) | (a3);
    *(unsigned __int64 *)(v_rdi + 24) = a1;
    a1 = (v_rdi) | (a2);
    if (condition_is_equal) goto loc_003602BD;
loc_00360115:
    a1 = (*(unsigned __int64 *)(v_rdi + 24)) ^ (*(unsigned __int64 *)(a4 + 8));
    a2 = (unsigned int)((*(unsigned __int64 *)(a4 + 8)) & (0xFFFULL));
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_rdi + 24));
    *(unsigned __int64 *)(v_rdi + 24) = a1;
    a2 = (a2) | (v_rdi);
    if ((*(unsigned __int64 *)(a4 + 8)) != (*(unsigned __int64 *)(a4 + 8))) goto loc_00360115;
    goto loc_003602BD;
loc_00360148:
    a1 = -(*(unsigned __int64 *)(v_rbp - 113));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 8) + 72)) == 0) goto loc_0035FE6E;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a4 + 8) + 0 * 8 + 56)) & (1)) != 0) goto loc_0035FE6E;
    a4 = (*(unsigned __int64 *)(v_rbp - 113) * 4 + 63) & (-64);
    if (a4 == 64) { a4 = 128; }
loc_003601AE:
    if (a1 >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 8) + 0 * 8 + 56))) goto loc_0035FE6E;
    if ((a4 + a1 * 1) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 8) + 0 * 8 + 56))) goto loc_0035FE6E;
    goto loc_003601AE;
loc_003601D5:
    v_stack_p28 = 0;
    a4 = 0;
    v_stack_p20 = 0;
    result = RtlpLogHeapFailure(9, *(unsigned __int64 *)(a4 + a1 * 1 + 56), *(unsigned __int64 *)(v_r13 + 320 + 24), a4);
    goto loc_003602BD;
loc_003602BD:
}
```

## 5. (Beta) C Style

```c
int64_t sub_0035FB85(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, int64_t Arg25, int64_t Arg26, int64_t Arg27, int64_t Arg28)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;

    v_stack_pE0 = local_rbx;
    v_stack_pD8 = local_rsi;
    v_stack_pD0 = local_rdi;
    v_stack_pC8 = local_r14;
    if ((uint32_t)(result) != 0) goto loc_0035FE09;
loc_0035FBAD:
    *(uint64_t *)(local_rbp + 0x7F) = local_r12 - 16;
    result = *(uint8_t *)(local_r12 - 0xD);
    local_rsi = local_r12 - 16;
    if (((*(uint8_t *)(local_r12 - 0x10 + 0x3)) & (4)) != 0) {
        result = *(uint16_t *)(local_r12 - 0x10);
        result = (uint16_t)((result) & ((uint16_t)(128 + 127)));
        Arg1 = (uint16_t)(result);
        Arg1 = -(Arg1);
        Arg1 = (Arg1) << (4);
        local_rsi = (local_r12 - 16) + (Arg1);
    }
    Arg1 = 256;
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x3))) & (1)) == 0) { Arg1 = 128; }
    Arg2 = (Arg1) | (4);
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x3))) & (32)) == 0) { Arg2 = Arg1; }
    Arg2 = (Arg2) | (2);
    *(uint64_t *)(local_rbp - 0x69) = Arg2;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(local_rsi + 0x3)))) & (8));
    *(uint64_t *)(local_rbp + 0x7F) = local_rsi;
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x3))) & (222)) == 0) goto loc_0035FC9B;
    Arg1 = (Arg2) | (8);
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x3))) & (4)) == 0) { Arg1 = Arg2; }
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x3))) & (128)) == 0) { Arg1 = Arg1; }
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x3))) & (64)) == 0) { Arg1 = Arg1; }
    *(uint64_t *)(local_rbp - 0x69) = Arg1;
    if ((uint32_t)(Arg4) != 0) goto loc_0035FC9B;
    *(uint64_t *)(local_rbp - 0x69) = Arg1;
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x3))) & (16)) != 0) {
        local_r14 = Arg1;
        local_r14 = (local_r14) | (32);
        *(uint64_t *)(local_rbp - 0x69) = local_r14;
    }
    local_r14 = ((uint8_t)(*(uint16_t *)(local_rsi + 0x2))) << (4);
    *(uint64_t *)(local_rbp - 0x71) = local_r14;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xC66F06));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC66F06)))) & (16)) != 0) {
        Arg4 = local_r12;
        Arg3 = local_r14;
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)));
        Arg1 = local_rsi;
        result = VfPtFreePoolNotification(Arg1, Arg2, Arg3, Arg4);
    }
    local_r14 = 0;
    *(uint32_t *)(local_rbp - 0x5D) = 0;
    *(uint8_t *)(local_rbp + 0x6F) = 0;
    *(uint8_t *)(local_rbp - 0x79) = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC65468))))) {
    }
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)))));
    Arg2 = (Arg1) >> (32);
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)(*(uint64_t *)(v_rip + 0xB9F03C))));
loc_0035FD3C:
    Arg1 = ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4) + ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x35FD15 + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xEFAD20) + Arg1 * 8)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4))))) goto loc_00360148;
    result = (uint32_t)((Arg2 + 1) & ((uint32_t)(*(uint64_t *)(v_rip + 0xB9F03C))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_0035FD3C;
    *(uint64_t *)(local_rbp - 0x49) = v_xmm0;
    result = 0;
    *(uint64_t *)(local_rbp - 0x41) = v_rip + 12169100;
    *(uint64_t *)(local_rbp - 0x49) = 0;
    *(uint64_t *)(local_rbp - 0x39) = 0;
    *(uint8_t *)(local_rbp - 0x39) = (uint8_t)(v_cr8);
loc_0035FDE0:
    Arg3 = (0 + 0 * 4) << (4);
    Arg3 = (Arg3) + (*(uint64_t *)(v_rip + 0xB9EF69));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4))))) goto loc_0035FE2F;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_0035FDE0;
loc_0035FE09:
loc_0035FE17:
    if ((v_rip + 12120368) >= (v_rip + 12120393)) goto loc_0035FBAD;
    result = (v_rip + 12120368) + (8);
    goto loc_0035FE17;
loc_0035FE2F:
    Arg1 = -(*(uint64_t *)(local_rbp - 0x71));
    result = KeReleaseInStackQueuedSpinLock(local_rbp - 73, Arg3 + 8, Arg3, 1);
loc_0035FE6E:
    local_r15 = (*(uint64_t *)(local_rbp - 0x69)) >> (8);
    Arg4 = 0;
    local_r15 = (uint32_t)((local_r15) & (1));
    result = ViFreeTrackedPool(local_r12, *(uint64_t *)(local_rbp - 0x71), (uint32_t)((uint32_t)(local_r15)), Arg4);
    if ((uint16_t)(local_rsi) == 0) goto loc_0035FECF;
    goto loc_0035FF0E;
loc_0035FECF:
    Arg2 = (local_rsi) - (*(uint64_t *)(v_rip + 0xB08728));
    Arg2 = (Arg2) >> (20);
    Arg2 = (Arg2) + (Arg2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 11568951, Arg2, (uint32_t)((uint32_t)(local_r15)), Arg4);
loc_0035FF0E:
    Arg2 = (*(uint64_t *)(local_r13 + 0x140)) & (local_rsi);
    result = (local_r13 + 320) ^ (*(uint64_t *)(Arg2 + 0x10));
    result = (result) ^ (Arg2);
    result = (result) ^ (*(uint64_t *)(v_rip + 0xAC83D8));
    if (condition_is_not_equal) goto loc_003601D5;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)((Arg3) >> ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_r13 + 0x140 + 0x8))))));
    Arg3 = (Arg3) << (5);
    Arg3 = (Arg3) + (Arg2);
    result = -(*(uint8_t *)(Arg3 + 0x1A));
    result = (result) << (5);
    Arg3 = (Arg3) + (result);
    local_rdi = (Arg3) - (Arg2);
    local_rdi = (local_rdi) >> (5);
    local_rdi = (local_rdi) << ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_r13 + 0x140 + 0x8)))));
    local_rdi = (local_rdi) + (Arg2);
    result = (local_rdi == local_rsi) ? 1 : 0;
    result = (local_rdi) >> (12);
    result = (uint32_t)((result) ^ (*(uint32_t *)(local_rdi + 0x28)));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xAC836C)));
    result = (result) >> (16);
    result = (result) + (local_rdi);
    Arg2 = (*(uint16_t *)(local_rdi + 0x2C)) << (6);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_rbp + 0x7F)))) - ((uint32_t)(result)));
    local_rbx = ((uint32_t)(*(uint32_t *)(Arg2 + *(uint64_t *)(local_r13 + 0x140 + 0x18) * 1 + 0x48))) * ((uint32_t)((uint32_t)(Arg3)));
    local_rbx = (local_rbx) >> (32);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) * ((uint32_t)((uint16_t)(result))));
    if (((uint32_t)(Arg3)) != ((uint32_t)(result))) goto loc_003602BD;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r13 + 0x140 + 0x18) + 0x4C))))) >> (13));
    result = (uint32_t)((result) & (0x3FFFFULL));
    Arg3 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r13 + 0x140 + 0x18) + 0x4C))) >> (4);
    Arg3 = (uint32_t)((Arg3) & (511));
    Arg4 = (uint32_t)((1) << ((uint8_t)((uint16_t)(result))));
    Arg1 = (uint32_t)(((uint16_t)(result)) + (-2));
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(result)));
    *(uint32_t *)(local_rbp - 0x55) = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (63));
    result = (local_rbx) >> (6);
loc_0036004E:
    *(uint64_t *)(local_rbp - 0x69) = *(uint64_t *)(local_rdi + 0x10);
    Arg1 = (*(uint64_t *)(local_rdi + 0x10)) >> (48);
    *(uint64_t *)(local_rbp + 0x7F) = *(uint64_t *)(local_rdi + 0x10);
    if (((uint8_t)(Arg1)) == 1) {
        *(uint8_t *)(local_rbp + 0x85) = 2;
    }
    if (*(uint64_t *)(local_rbp + 0x7F) != 0) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(local_r13 + 0x140 + 0x18) + 0x50);
        Arg1 = *(uint16_t *)(local_rbp + 0x7F);
        Arg2 = (uint32_t)(Arg3);
        *(uint16_t *)(*(uint64_t *)(local_rbp + 0x7F)) = (uint16_t)(Arg1);
        Arg2 = (uint32_t)((Arg2) ^ (*(uint32_t *)(*(uint64_t *)(local_rbp + 0x7F))));
        Arg1 = (uint8_t)(Arg1);
        Arg1 = local_rbx + 1;
        Arg3 = (Arg3) >> (32);
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg3)));
        *(uint16_t *)(local_rbp + 0x7F) = (uint16_t)(Arg1);
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(*(uint64_t *)(local_rbp + 0x7F))));
        *(uint32_t *)(*(uint64_t *)(local_rbp + 0x7F) + 0x8) = (uint32_t)(Arg2);
    }
    Arg2 = (*(uint16_t *)(local_rdi + 0x2C)) << (6);
    if (condition_is_not_equal) goto loc_0036004E;
    if ((*(uint8_t *)(local_rbp - 0x63)) != 1) goto loc_003602BD;
    Arg4 = (uint32_t)((*(uint16_t *)(local_rbp - 0x65)) << (6));
    Arg4 = (Arg4) + (*(uint64_t *)(local_r13 + 0x140 + 0x18));
    Arg2 = (uint32_t)((*(uint64_t *)(Arg4 + 0x8)) & (0xFFFULL));
    Arg3 = (uint32_t)((*(uint64_t *)(local_rdi + 0x18)) & (0xFFFULL));
    Arg1 = (*(uint64_t *)(Arg4 + 0x8)) - (Arg2);
    Arg1 = (Arg1) | (Arg3);
    *(uint64_t *)(local_rdi + 0x18) = Arg1;
    Arg1 = (local_rdi) | (Arg2);
    if (condition_is_equal) goto loc_003602BD;
loc_00360115:
    Arg1 = (*(uint64_t *)(local_rdi + 0x18)) ^ (*(uint64_t *)(Arg4 + 0x8));
    Arg2 = (uint32_t)((*(uint64_t *)(Arg4 + 0x8)) & (0xFFFULL));
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(local_rdi + 0x18));
    *(uint64_t *)(local_rdi + 0x18) = Arg1;
    Arg2 = (Arg2) | (local_rdi);
    if ((*(uint64_t *)(Arg4 + 0x8)) != (*(uint64_t *)(Arg4 + 0x8))) goto loc_00360115;
    goto loc_003602BD;
loc_00360148:
    Arg1 = -(*(uint64_t *)(local_rbp - 0x71));
    if ((*(uint64_t *)(*(uint64_t *)(Arg4 + 0x8) + 0x48)) == 0) goto loc_0035FE6E;
    if (((*(uint8_t *)(*(uint64_t *)(Arg4 + 0x8) + 0x0 * 8 + 0x38)) & (1)) != 0) goto loc_0035FE6E;
    Arg4 = (*(uint64_t *)(local_rbp - 0x71) * 4 + 63) & (-64);
    if (Arg4 == 64) { Arg4 = 128; }
loc_003601AE:
    if (Arg1 >= (*(uint64_t *)(*(uint64_t *)(Arg4 + 0x8) + 0x0 * 8 + 0x38))) goto loc_0035FE6E;
    if ((Arg4 + Arg1 * 1) >= (*(uint64_t *)(*(uint64_t *)(Arg4 + 0x8) + 0x0 * 8 + 0x38))) goto loc_0035FE6E;
    goto loc_003601AE;
loc_003601D5:
    v_stack_p28 = 0;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = RtlpLogHeapFailure(9, *(uint64_t *)(Arg4 + Arg1 * 1 + 0x38), *(uint64_t *)(local_r13 + 0x140 + 0x18), Arg4);
    goto loc_003602BD;
loc_003602BD:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0035FB85&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
