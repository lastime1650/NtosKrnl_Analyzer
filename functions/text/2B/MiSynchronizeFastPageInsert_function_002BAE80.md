# MiSynchronizeFastPageInsert

- RVA: `0x002BAE80`–`0x002BB686` (길이 `2,054` bytes)
- VA: `0x00000001402BAE80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006DD80`
- 디코드: `466`개 명령, `2,054/2,054` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x002BB250` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x002BB37B` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002BB3C3` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x002BB425` → [ExTryAcquireSpinLockExclusiveAtDpcLevel](ExTryAcquireSpinLockExclusiveAtDpcLevel_function_002BB800.md) (function, `0x002BB800`)
- `0x002BB442` → [MiPageToChannel](MiPageToChannel_function_002B9B48.md) (function, `0x002B9B48`)
- `0x002BB485` → [MiIsDecayPfn](MiIsDecayPfn_function_002B9240.md) (function, `0x002B9240`)
- `0x002BB4A7` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x002BB4D8` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002BB535` → [MiReleasePageListLock](MiReleasePageListLock_function_002B1050.md) (function, `0x002B1050`)
- `0x002BB55E` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002BB5D0` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002BB611` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)

### Direct callers
- [MiInsertPageInList](MiInsertPageInList_function_002BA000.md) at `0x002BA593`
- [sub_0033E2D1](../33/Unknown_function_0033E2D1.md) at `0x0033E6CD`

### Static image references
- `0x002BAFE9` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x002BB03E` → RVA `0x00E30088` (`.data`; read)
- `0x002BB05C` → RVA `0x00E2DBC0` (`.data`; read)
- `0x002BB063` → RVA `0x00E2DBC4` (`.data`; read)
- `0x002BB074` → RVA `0x00E2DC20` (`.data`; read)
- `0x002BB0C0` → RVA `0x00E2DBC0` (`.data`; write)
- `0x002BB104` → RVA `0x00E2DC28` (`.data`; read)
- `0x002BB381` → RVA `0x00E2DCE0` (`.data`; read)
- `0x002BB39B` → RVA `0x00E35C00` (`.data`; read)
- `0x002BB5EA` → RVA `0x00E3D240` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x002BB636` → [sub_006DBD20](../6D/Unknown_function_006DBD20.md) (`tail-transfer`)
  - `0x002BB647` → [sub_006DBD20 + 0x13](../6D/Unknown_function_006DBD20.md) (`tail-transfer`)
  - `0x002BB650` → [sub_006DBD20](../6D/Unknown_function_006DBD20.md) (`tail-transfer`)
  - `0x002BB656` → [sub_006DBD20 + 0x13](../6D/Unknown_function_006DBD20.md) (`tail-transfer`)
  - `0x002BB671` → [sub_006DBD20 + 0x17B](../6D/Unknown_function_006DBD20.md) (`tail-transfer`)
  - `0x002BB67B` → [sub_006DBD20 + 0x17B](../6D/Unknown_function_006DBD20.md) (`tail-transfer`)
  - `0x002BB681` → [sub_006DBD20 + 0x1CE](../6D/Unknown_function_006DBD20.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002BAE80  48 8B C4                        mov rax, rsp
002BAE83  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
002BAE87  48 89 48 08                     mov qword ptr [rax + 8], rcx
002BAE8B  53                              push rbx
002BAE8C  56                              push rsi
002BAE8D  57                              push rdi
002BAE8E  41 54                           push r12
002BAE90  41 55                           push r13
002BAE92  41 56                           push r14
002BAE94  41 57                           push r15
002BAE96  48 81 EC A0 00 00 00            sub rsp, 0xa0
002BAE9D  0F 57 C0                        xorps xmm0, xmm0
002BAEA0  4D 63 F9                        movsxd r15, r9d
002BAEA3  0F 11 40 88                     movups xmmword ptr [rax - 0x78], xmm0
002BAEA7  4C 8B E9                        mov r13, rcx
002BAEAA  48 BB 00 00 00 00 00 DE FF FF   movabs rbx, 0xffffde0000000000
002BAEB4  0F 11 40 98                     movups xmmword ptr [rax - 0x68], xmm0
002BAEB8  0F 11 40 A8                     movups xmmword ptr [rax - 0x58], xmm0
002BAEBC  48 8B C3                        mov rax, rbx
002BAEBF  4C 8B 94 24 00 01 00 00         mov r10, qword ptr [rsp + 0x100]
002BAEC7  4D 8B E0                        mov r12, r8
002BAECA  4C 2B E0                        sub r12, rax
002BAECD  48 B9 AB AA AA AA AA AA AA AA   movabs rcx, 0xaaaaaaaaaaaaaaab
002BAED7  49 C1 FC 04                     sar r12, 4
002BAEDB  4C 0F AF E1                     imul r12, rcx
002BAEDF  4D 85 D2                        test r10, r10
002BAEE2  0F 85 C4 00 00 00               jne 0x1402bafac
002BAEE8  41 8B 40 20                     mov eax, dword ptr [r8 + 0x20]
002BAEEC  41 B9 05 00 00 00               mov r9d, 5
002BAEF2  41 8B 48 20                     mov ecx, dword ptr [r8 + 0x20]
002BAEF6  C1 E9 18                        shr ecx, 0x18
002BAEF9  89 84 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], eax
002BAF00  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
002BAF05  49 BE 30 00 00 00 00 DE FF FF   movabs r14, 0xffffde0000000030
002BAF0F  F6 C1 08                        test cl, 8
002BAF12  0F 85 3F 04 00 00               jne 0x1402bb357
002BAF18  0F B6 84 24 F3 00 00 00         movzx eax, byte ptr [rsp + 0xf3]
002BAF20  83 E0 07                        and eax, 7
002BAF23  8B F8                           mov edi, eax
002BAF25  48 6B F7 58                     imul rsi, rdi, 0x58
002BAF29  48 81 C6 E0 0C 00 00            add rsi, 0xce0
002BAF30  45 33 DB                        xor r11d, r11d
002BAF33  4C 89 5C 24 50                  mov qword ptr [rsp + 0x50], r11
002BAF38  41 8B DB                        mov ebx, r11d
002BAF3B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
002BAF40  83 FB 02                        cmp ebx, 2
002BAF43  73 1E                           jae 0x1402baf63
002BAF45  8B C3                           mov eax, ebx
002BAF47  48 8D 0C C7                     lea rcx, [rdi + rax*8]
002BAF4B  49 8B 84 CD 40 3E 00 00         mov rax, qword ptr [r13 + rcx*8 + 0x3e40]
002BAF53  48 3D 00 10 00 00               cmp rax, 0x1000
002BAF59  0F 83 B6 04 00 00               jae 0x1402bb415
002BAF5F  FF C3                           inc ebx
002BAF61  EB DD                           jmp 0x1402baf40
002BAF63  0F 84 75 05 00 00               je 0x1402bb4de
002BAF69  8B C3                           mov eax, ebx
002BAF6B  48 8D 0C C7                     lea rcx, [rdi + rax*8]
002BAF6F  49 8B 84 CD 40 3E 00 00         mov rax, qword ptr [r13 + rcx*8 + 0x3e40]
002BAF77  48 3D 00 10 00 00               cmp rax, 0x1000
002BAF7D  0F 82 C0 03 00 00               jb 0x1402bb343
002BAF83  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
002BAF8B  49 C7 84 CD 40 3E 00 00 00 00 00 00  mov qword ptr [r13 + rcx*8 + 0x3e40], 0
002BAF97  C6 40 02 01                     mov byte ptr [rax + 2], 1
002BAF9B  85 DB                           test ebx, ebx
002BAF9D  74 04                           je 0x1402bafa3
002BAF9F  C6 40 02 02                     mov byte ptr [rax + 2], 2
002BAFA3  C6 40 01 01                     mov byte ptr [rax + 1], 1
002BAFA7  E9 97 03 00 00                  jmp 0x1402bb343
002BAFAC  48 8B C3                        mov rax, rbx
002BAFAF  49 8B FA                        mov rdi, r10
002BAFB2  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
002BAFBA  48 2B F8                        sub rdi, rax
002BAFBD  49 BE 30 00 00 00 00 DE FF FF   movabs r14, 0xffffde0000000030
002BAFC7  48 C1 FF 04                     sar rdi, 4
002BAFCB  BE 05 00 00 00                  mov esi, 5
002BAFD0  48 0F AF F9                     imul rdi, rcx
002BAFD4  45 33 DB                        xor r11d, r11d
002BAFD7  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
002BAFDB  4C 89 5C 24 50                  mov qword ptr [rsp + 0x50], r11
002BAFE0  65 44 8B 04 25 A4 01 00 00      mov r8d, dword ptr gs:[0x1a4]
002BAFE9  8B 05 91 BA D0 00               mov eax, dword ptr [rip + 0xd0ba91]
002BAFEF  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
002BAFF4  83 F8 40                        cmp eax, 0x40
002BAFF7  0F 83 B1 05 00 00               jae 0x1402bb5ae
002BAFFD  8B 0D 7D BA D0 00               mov ecx, dword ptr [rip + 0xd0ba7d]
002BB003  33 D2                           xor edx, edx
002BB005  B8 40 00 00 00                  mov eax, 0x40
002BB00A  F7 F1                           div ecx
002BB00C  83 F8 01                        cmp eax, 1
002BB00F  76 04                           jbe 0x1402bb015
002BB011  44 0F AF C0                     imul r8d, eax
002BB015  4F 8D 0C 64                     lea r9, [r12 + r12*2]
002BB019  44 89 44 24 40                  mov dword ptr [rsp + 0x40], r8d
002BB01E  49 C1 E1 04                     shl r9, 4
002BB022  45 8B EB                        mov r13d, r11d
002BB025  44 89 9C 24 F0 00 00 00         mov dword ptr [rsp + 0xf0], r11d
002BB02D  44 89 5C 24 44                  mov dword ptr [rsp + 0x44], r11d
002BB032  48 8B C3                        mov rax, rbx
002BB035  49 8D 1C 01                     lea rbx, [r9 + rax]
002BB039  49 8B 44 01 28                  mov rax, qword ptr [r9 + rax + 0x28]
002BB03E  48 8B 0D 43 50 B7 00            mov rcx, qword ptr [rip + 0xb75043]
002BB045  48 C1 E8 2B                     shr rax, 0x2b
002BB049  25 FF 03 00 00                  and eax, 0x3ff
002BB04E  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
002BB053  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
002BB057  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
002BB05C  48 63 15 5D 2B B7 00            movsxd rdx, dword ptr [rip + 0xb72b5d]
002BB063  8B 0D 5B 2B B7 00               mov ecx, dword ptr [rip + 0xb72b5b]
002BB069  3B D1                           cmp edx, ecx
002BB06B  77 1D                           ja 0x1402bb08a
002BB06D  48 8B C2                        mov rax, rdx
002BB070  48 C1 E0 04                     shl rax, 4
002BB074  48 03 05 A5 2B B7 00            add rax, qword ptr [rip + 0xb72ba5]
002BB07B  4C 3B 20                        cmp r12, qword ptr [rax]
002BB07E  72 0A                           jb 0x1402bb08a
002BB080  3B D1                           cmp edx, ecx
002BB082  74 43                           je 0x1402bb0c7
002BB084  4C 3B 60 10                     cmp r12, qword ptr [rax + 0x10]
002BB088  72 3D                           jb 0x1402bb0c7
002BB08A  41 8B D3                        mov edx, r11d
002BB08D  3B CA                           cmp ecx, edx
002BB08F  0F 8C D2 02 00 00               jl 0x1402bb367
002BB095  44 8D 04 0A                     lea r8d, [rdx + rcx]
002BB099  41 D1 F8                        sar r8d, 1
002BB09C  49 63 C0                        movsxd rax, r8d
002BB09F  48 C1 E0 04                     shl rax, 4
002BB0A3  48 03 05 76 2B B7 00            add rax, qword ptr [rip + 0xb72b76]
002BB0AA  4C 3B 20                        cmp r12, qword ptr [rax]
002BB0AD  0F 82 07 04 00 00               jb 0x1402bb4ba
002BB0B3  44 3B 05 0A 2B B7 00            cmp r8d, dword ptr [rip + 0xb72b0a]
002BB0BA  0F 85 42 03 00 00               jne 0x1402bb402
002BB0C0  44 89 05 F9 2A B7 00            mov dword ptr [rip + 0xb72af9], r8d
002BB0C7  8B 40 08                        mov eax, dword ptr [rax + 8]
002BB0CA  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
002BB0CE  4D 85 D2                        test r10, r10
002BB0D1  0F 85 C8 04 00 00               jne 0x1402bb59f
002BB0D7  44 8B 43 20                     mov r8d, dword ptr [rbx + 0x20]
002BB0DB  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
002BB0DE  C1 E8 18                        shr eax, 0x18
002BB0E1  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
002BB0E6  A8 08                           test al, 8
002BB0E8  0F 85 E5 02 00 00               jne 0x1402bb3d3
002BB0EE  49 BE AB AA AA AA AA AA AA AA   movabs r14, 0xaaaaaaaaaaaaaaab
002BB0F8  0F B6 74 24 37                  movzx esi, byte ptr [rsp + 0x37]
002BB0FD  83 E6 07                        and esi, 7
002BB100  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
002BB104  48 83 3D 1C 2B B7 00 00         cmp qword ptr [rip + 0xb72b1c], 0
002BB10C  89 74 24 7C                     mov dword ptr [rsp + 0x7c], esi
002BB110  0F 85 21 03 00 00               jne 0x1402bb437
002BB116  32 D2                           xor dl, dl
002BB118  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
002BB11C  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
002BB121  4C 69 D0 80 DF 00 00            imul r10, rax, 0xdf80
002BB128  88 94 24 80 00 00 00            mov byte ptr [rsp + 0x80], dl
002BB12F  4D 03 51 10                     add r10, qword ptr [r9 + 0x10]
002BB133  44 89 BC 24 84 00 00 00         mov dword ptr [rsp + 0x84], r15d
002BB13B  41 83 FF 09                     cmp r15d, 9
002BB13F  0F 8C 23 04 00 00               jl 0x1402bb568
002BB145  0F B6 C2                        movzx eax, dl
002BB148  44 8B C6                        mov r8d, esi
002BB14B  48 8D 0C C5 3B 00 00 00         lea rcx, [rax*8 + 0x3b]
002BB153  49 03 C8                        add rcx, r8
002BB156  48 6B C1 58                     imul rax, rcx, 0x58
002BB15A  49 03 C2                        add rax, r10
002BB15D  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
002BB162  8B 74 24 40                     mov esi, dword ptr [rsp + 0x40]
002BB166  49 81 C1 40 2E 00 00            add r9, 0x2e40
002BB16D  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
002BB171  45 8B F3                        mov r14d, r11d
002BB174  49 C1 E0 09                     shl r8, 9
002BB178  4D 8B D3                        mov r10, r11
002BB17B  4D 03 C1                        add r8, r9
002BB17E  4C 89 5C 24 58                  mov qword ptr [rsp + 0x58], r11
002BB183  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
002BB188  49 B9 FF FF FF FF FF FF FF 7F   movabs r9, 0x7fffffffffffffff
002BB192  44 3B F0                        cmp r14d, eax
002BB195  0F 83 C0 04 00 00               jae 0x1402bb65b
002BB19B  48 83 FF FF                     cmp rdi, -1
002BB19F  75 41                           jne 0x1402bb1e2
002BB1A1  8B C6                           mov eax, esi
002BB1A3  4D 8B 3C C0                     mov r15, qword ptr [r8 + rax*8]
002BB1A7  49 83 FF FF                     cmp r15, -1
002BB1AB  0F 85 07 01 00 00               jne 0x1402bb2b8
002BB1B1  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
002BB1B5  41 FF C5                        inc r13d
002BB1B8  41 FF C6                        inc r14d
002BB1BB  FF C6                           inc esi
002BB1BD  83 E6 3F                        and esi, 0x3f
002BB1C0  EB D0                           jmp 0x1402bb192
002BB1C2  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
002BB1C9  0F 83 06 01 00 00               jae 0x1402bb2d5
002BB1CF  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
002BB1D4  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
002BB1D8  41 FF C6                        inc r14d
002BB1DB  FF C6                           inc esi
002BB1DD  83 E6 3F                        and esi, 0x3f
002BB1E0  EB B0                           jmp 0x1402bb192
002BB1E2  83 BC 24 F0 00 00 00 00         cmp dword ptr [rsp + 0xf0], 0
002BB1EA  75 B5                           jne 0x1402bb1a1
002BB1EC  4C 8B FF                        mov r15, rdi
002BB1EF  48 8B BC 24 00 01 00 00         mov rdi, qword ptr [rsp + 0x100]
002BB1F7  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
002BB1FF  49 8B CB                        mov rcx, r11
002BB202  48 8D 43 10                     lea rax, [rbx + 0x10]
002BB206  48 83 F9 04                     cmp rcx, 4
002BB20A  7D B6                           jge 0x1402bb1c2
002BB20C  80 78 08 00                     cmp byte ptr [rax + 8], 0
002BB210  75 09                           jne 0x1402bb21b
002BB212  48 FF C1                        inc rcx
002BB215  48 83 C0 18                     add rax, 0x18
002BB219  EB EB                           jmp 0x1402bb206
002BB21B  48 3B 38                        cmp rdi, qword ptr [rax]
002BB21E  75 F2                           jne 0x1402bb212
002BB220  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
002BB225  83 7C 24 44 00                  cmp dword ptr [rsp + 0x44], 0
002BB22A  4B 8D 04 52                     lea rax, [r10 + r10*2]
002BB22E  48 8D 1C C3                     lea rbx, [rbx + rax*8]
002BB232  4C 89 7B 08                     mov qword ptr [rbx + 8], r15
002BB236  48 89 7B 10                     mov qword ptr [rbx + 0x10], rdi
002BB23A  75 35                           jne 0x1402bb271
002BB23C  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
002BB244  48 83 C1 20                     add rcx, 0x20
002BB248  C7 44 24 44 01 00 00 00         mov dword ptr [rsp + 0x44], 1
002BB250  E8 DB DB F8 FF                  call 0x140248e30
002BB255  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
002BB25A  45 33 DB                        xor r11d, r11d
002BB25D  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
002BB262  49 B9 FF FF FF FF FF FF FF 7F   movabs r9, 0x7fffffffffffffff
002BB26C  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
002BB271  83 BC 24 F0 00 00 00 00         cmp dword ptr [rsp + 0xf0], 0
002BB279  0F 84 A5 03 00 00               je 0x1402bb624
002BB27F  8B C6                           mov eax, esi
002BB281  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
002BB285  49 3B CF                        cmp rcx, r15
002BB288  0F 84 AD 03 00 00               je 0x1402bb63b
002BB28E  80 7B 18 00                     cmp byte ptr [rbx + 0x18], 0
002BB292  74 09                           je 0x1402bb29d
002BB294  F0 4C 21 4F 18                  lock and qword ptr [rdi + 0x18], r9
002BB299  C6 43 18 00                     mov byte ptr [rbx + 0x18], 0
002BB29D  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
002BB2A2  41 FF CE                        dec r14d
002BB2A5  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
002BB2A9  41 FF C6                        inc r14d
002BB2AC  FF CE                           dec esi
002BB2AE  FF C6                           inc esi
002BB2B0  83 E6 3F                        and esi, 0x3f
002BB2B3  E9 DA FE FF FF                  jmp 0x1402bb192
002BB2B8  4B 8D 3C 7F                     lea rdi, [r15 + r15*2]
002BB2BC  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002BB2C6  48 C1 E7 04                     shl rdi, 4
002BB2CA  48 8B C0                        mov rax, rax
002BB2CD  48 03 F8                        add rdi, rax
002BB2D0  E9 22 FF FF FF                  jmp 0x1402bb1f7
002BB2D5  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
002BB2DA  48 83 FA FF                     cmp rdx, -1
002BB2DE  0F 84 10 01 00 00               je 0x1402bb3f4
002BB2E4  83 BC 24 F0 00 00 00 00         cmp dword ptr [rsp + 0xf0], 0
002BB2EC  0F 85 02 01 00 00               jne 0x1402bb3f4
002BB2F2  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
002BB2F5  C1 E8 18                        shr eax, 0x18
002BB2F8  A8 08                           test al, 8
002BB2FA  0F 85 F4 00 00 00               jne 0x1402bb3f4
002BB300  F0 4C 21 4F 18                  lock and qword ptr [rdi + 0x18], r9
002BB305  41 FF C6                        inc r14d
002BB308  44 8B BC 24 F0 00 00 00         mov r15d, dword ptr [rsp + 0xf0]
002BB310  41 83 FE 40                     cmp r14d, 0x40
002BB314  0F 84 03 02 00 00               je 0x1402bb51d
002BB31A  41 83 FE 01                     cmp r14d, 1
002BB31E  0F 84 E6 01 00 00               je 0x1402bb50a
002BB324  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
002BB328  41 BE 01 00 00 00               mov r14d, 1
002BB32E  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
002BB336  C6 03 01                        mov byte ptr [rbx], 1
002BB339  41 83 FB 02                     cmp r11d, 2
002BB33D  0F 82 2A 03 00 00               jb 0x1402bb66d
002BB343  48 81 C4 A0 00 00 00            add rsp, 0xa0
002BB34A  41 5F                           pop r15
002BB34C  41 5E                           pop r14
002BB34E  41 5D                           pop r13
002BB350  41 5C                           pop r12
002BB352  5F                              pop rdi
002BB353  5E                              pop rsi
002BB354  5B                              pop rbx
002BB355  C3                              ret
002BB356  CC                              int3
002BB357  48 8B CB                        mov rcx, rbx
002BB35A  4C 3B C1                        cmp r8, rcx
002BB35D  73 22                           jae 0x1402bb381
002BB35F  41 8B C1                        mov eax, r9d
002BB362  E9 BC FB FF FF                  jmp 0x1402baf23
002BB367  45 33 C9                        xor r9d, r9d
002BB36A  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
002BB36F  4D 8B C4                        mov r8, r12
002BB372  BA 80 51 00 00                  mov edx, 0x5180
002BB377  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
002BB37B  E8 E0 22 24 00                  call 0x1404fd660
002BB380  CC                              int3
002BB381  48 8B 0D 58 29 B7 00            mov rcx, qword ptr [rip + 0xb72958]
002BB388  48 8D 14 49                     lea rdx, [rcx + rcx*2]
002BB38C  48 C1 E2 04                     shl rdx, 4
002BB390  49 8B CE                        mov rcx, r14
002BB393  48 03 D1                        add rdx, rcx
002BB396  4C 3B C2                        cmp r8, rdx
002BB399  73 C4                           jae 0x1402bb35f
002BB39B  48 8B 0D 5E A8 B7 00            mov rcx, qword ptr [rip + 0xb7a85e]
002BB3A2  4C 3B E1                        cmp r12, rcx
002BB3A5  72 0C                           jb 0x1402bb3b3
002BB3A7  48 81 C1 00 08 00 00            add rcx, 0x800
002BB3AE  4C 3B E1                        cmp r12, rcx
002BB3B1  72 AC                           jb 0x1402bb35f
002BB3B3  C1 E8 10                        shr eax, 0x10
002BB3B6  24 07                           and al, 7
002BB3B8  3C 06                           cmp al, 6
002BB3BA  0F 84 58 FB FF FF               je 0x1402baf18
002BB3C0  49 8B C8                        mov rcx, r8
002BB3C3  E8 08 2F FD FF                  call 0x14028e2d0
002BB3C8  83 F8 09                        cmp eax, 9
002BB3CB  0F 85 47 FB FF FF               jne 0x1402baf18
002BB3D1  EB 8C                           jmp 0x1402bb35f
002BB3D3  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002BB3DD  48 8B C0                        mov rax, rax
002BB3E0  48 3B D8                        cmp rbx, rax
002BB3E3  73 6D                           jae 0x1402bb452
002BB3E5  49 BE AB AA AA AA AA AA AA AA   movabs r14, 0xaaaaaaaaaaaaaaab
002BB3EF  E9 0C FD FF FF                  jmp 0x1402bb100
002BB3F4  4B 8D 04 52                     lea rax, [r10 + r10*2]
002BB3F8  C6 44 C3 18 01                  mov byte ptr [rbx + rax*8 + 0x18], 1
002BB3FD  E9 23 FE FF FF                  jmp 0x1402bb225
002BB402  4C 3B 60 10                     cmp r12, qword ptr [rax + 0x10]
002BB406  0F 82 B4 FC FF FF               jb 0x1402bb0c0
002BB40C  41 8D 50 01                     lea edx, [r8 + 1]
002BB410  E9 78 FC FF FF                  jmp 0x1402bb08d
002BB415  4A 8D 0C 2E                     lea rcx, [rsi + r13]
002BB419  48 3D 00 20 00 00               cmp rax, 0x2000
002BB41F  0F 83 EC 01 00 00               jae 0x1402bb611
002BB425  E8 D6 03 00 00                  call 0x1402bb800
002BB42A  85 C0                           test eax, eax
002BB42C  0F 85 37 FB FF FF               jne 0x1402baf69
002BB432  E9 28 FB FF FF                  jmp 0x1402baf5f
002BB437  49 C1 F9 04                     sar r9, 4
002BB43B  4D 0F AF CE                     imul r9, r14
002BB43F  49 8B C9                        mov rcx, r9
002BB442  E8 01 E7 FF FF                  call 0x1402b9b48
002BB447  0F B6 D0                        movzx edx, al
002BB44A  45 33 DB                        xor r11d, r11d
002BB44D  E9 C6 FC FF FF                  jmp 0x1402bb118
002BB452  48 8B 05 87 28 B7 00            mov rax, qword ptr [rip + 0xb72887]
002BB459  48 8D 0C 40                     lea rcx, [rax + rax*2]
002BB45D  48 C1 E1 04                     shl rcx, 4
002BB461  49 8B C6                        mov rax, r14
002BB464  48 03 C8                        add rcx, rax
002BB467  49 BE AB AA AA AA AA AA AA AA   movabs r14, 0xaaaaaaaaaaaaaaab
002BB471  48 3B D9                        cmp rbx, rcx
002BB474  0F 83 86 FC FF FF               jae 0x1402bb100
002BB47A  49 8B C9                        mov rcx, r9
002BB47D  48 C1 F9 04                     sar rcx, 4
002BB481  49 0F AF CE                     imul rcx, r14
002BB485  E8 B6 DD FF FF                  call 0x1402b9240
002BB48A  85 C0                           test eax, eax
002BB48C  0F 85 6E FC FF FF               jne 0x1402bb100
002BB492  41 C1 E8 10                     shr r8d, 0x10
002BB496  41 80 E0 07                     and r8b, 7
002BB49A  41 80 F8 06                     cmp r8b, 6
002BB49E  0F 84 54 FC FF FF               je 0x1402bb0f8
002BB4A4  48 8B CB                        mov rcx, rbx
002BB4A7  E8 24 2E FD FF                  call 0x14028e2d0
002BB4AC  83 F8 09                        cmp eax, 9
002BB4AF  0F 85 43 FC FF FF               jne 0x1402bb0f8
002BB4B5  E9 46 FC FF FF                  jmp 0x1402bb100
002BB4BA  45 85 C0                        test r8d, r8d
002BB4BD  0F 85 58 01 00 00               jne 0x1402bb61b
002BB4C3  4C 8B C8                        mov r9, rax
002BB4C6  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
002BB4CB  4D 8B C4                        mov r8, r12
002BB4CE  BA 80 51 00 00                  mov edx, 0x5180
002BB4D3  B9 1A 00 00 00                  mov ecx, 0x1a
002BB4D8  E8 83 21 24 00                  call 0x1404fd660
002BB4DD  CC                              int3
002BB4DE  4C 8B 94 24 00 01 00 00         mov r10, qword ptr [rsp + 0x100]
002BB4E6  48 C7 C7 FF FF FF FF            mov rdi, 0xffffffffffffffff
002BB4ED  C7 44 24 30 40 00 00 00         mov dword ptr [rsp + 0x30], 0x40
002BB4F5  45 33 DB                        xor r11d, r11d
002BB4F8  48 BB 00 00 00 00 00 DE FF FF   movabs rbx, 0xffffde0000000000
002BB502  8D 77 06                        lea esi, [rdi + 6]
002BB505  E9 D6 FA FF FF                  jmp 0x1402bafe0
002BB50A  48 83 FA FF                     cmp rdx, -1
002BB50E  0F 84 10 FE FF FF               je 0x1402bb324
002BB514  45 85 FF                        test r15d, r15d
002BB517  0F 85 07 FE FF FF               jne 0x1402bb324
002BB51D  83 7C 24 44 00                  cmp dword ptr [rsp + 0x44], 0
002BB522  48 8B BC 24 E8 00 00 00         mov rdi, qword ptr [rsp + 0xe8]
002BB52A  74 11                           je 0x1402bb53d
002BB52C  48 8B D3                        mov rdx, rbx
002BB52F  C6 03 01                        mov byte ptr [rbx], 1
002BB532  48 8B CF                        mov rcx, rdi
002BB535  E8 16 5B FF FF                  call 0x1402b1050
002BB53A  C6 03 00                        mov byte ptr [rbx], 0
002BB53D  41 83 FE 01                     cmp r14d, 1
002BB541  74 74                           je 0x1402bb5b7
002BB543  C6 43 02 01                     mov byte ptr [rbx + 2], 1
002BB547  45 85 FF                        test r15d, r15d
002BB54A  74 04                           je 0x1402bb550
002BB54C  C6 43 02 02                     mov byte ptr [rbx + 2], 2
002BB550  41 83 FD 20                     cmp r13d, 0x20
002BB554  72 04                           jb 0x1402bb55a
002BB556  C6 43 01 01                     mov byte ptr [rbx + 1], 1
002BB55A  48 8D 4F 20                     lea rcx, [rdi + 0x20]
002BB55E  E8 1D D9 F8 FF                  call 0x140248e80
002BB563  E9 DB FD FF FF                  jmp 0x1402bb343
002BB568  41 83 FF 08                     cmp r15d, 8
002BB56C  74 6C                           je 0x1402bb5da
002BB56E  C6 84 24 88 00 00 00 00         mov byte ptr [rsp + 0x88], 0
002BB576  32 C9                           xor cl, cl
002BB578  0F B6 C1                        movzx eax, cl
002BB57B  44 8B C6                        mov r8d, esi
002BB57E  49 8D 0C C0                     lea rcx, [r8 + rax*8]
002BB582  48 6B D1 58                     imul rdx, rcx, 0x58
002BB586  49 69 CF E8 00 00 00            imul rcx, r15, 0xe8
002BB58D  4A 03 94 11 98 3D 00 00         add rdx, qword ptr [rcx + r10 + 0x3d98]
002BB595  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
002BB59A  E9 C3 FB FF FF                  jmp 0x1402bb162
002BB59F  49 BE AB AA AA AA AA AA AA AA   movabs r14, 0xaaaaaaaaaaaaaaab
002BB5A9  E9 56 FB FF FF                  jmp 0x1402bb104
002BB5AE  41 83 E0 3F                     and r8d, 0x3f
002BB5B2  E9 5E FA FF FF                  jmp 0x1402bb015
002BB5B7  48 83 7C 24 38 FF               cmp qword ptr [rsp + 0x38], -1
002BB5BD  74 84                           je 0x1402bb543
002BB5BF  45 85 FF                        test r15d, r15d
002BB5C2  0F 85 7B FF FF FF               jne 0x1402bb543
002BB5C8  48 8D 4F 20                     lea rcx, [rdi + 0x20]
002BB5CC  C6 43 02 03                     mov byte ptr [rbx + 2], 3
002BB5D0  E8 AB D8 F8 FF                  call 0x140248e80
002BB5D5  E9 69 FD FF FF                  jmp 0x1402bb343
002BB5DA  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002BB5E4  48 8B C0                        mov rax, rax
002BB5E7  48 2B D8                        sub rbx, rax
002BB5EA  48 8B 05 4F 1C B8 00            mov rax, qword ptr [rip + 0xb81c4f]
002BB5F1  48 C1 FB 04                     sar rbx, 4
002BB5F5  49 0F AF DE                     imul rbx, r14
002BB5F9  48 C1 EB 09                     shr rbx, 9
002BB5FD  0F B6 4C 58 01                  movzx ecx, byte ptr [rax + rbx*2 + 1]
002BB602  80 E1 7F                        and cl, 0x7f
002BB605  88 8C 24 88 00 00 00            mov byte ptr [rsp + 0x88], cl
002BB60C  E9 67 FF FF FF                  jmp 0x1402bb578
002BB611  E8 6A D8 F8 FF                  call 0x140248e80
002BB616  E9 4E F9 FF FF                  jmp 0x1402baf69
002BB61B  41 8D 48 FF                     lea ecx, [r8 - 1]
002BB61F  E9 69 FA FF FF                  jmp 0x1402bb08d
002BB624  48 83 FA FF                     cmp rdx, -1
002BB628  0F 84 51 FC FF FF               je 0x1402bb27f
002BB62E  44 8B BC 24 F0 00 00 00         mov r15d, dword ptr [rsp + 0xf0]
002BB636  E9 E5 06 42 00                  jmp 0x1406dbd20
002BB63B  44 8B BC 24 F0 00 00 00         mov r15d, dword ptr [rsp + 0xf0]
002BB643  48 83 FA FF                     cmp rdx, -1
002BB647  0F 84 E6 06 42 00               je 0x1406dbd33
002BB64D  45 85 FF                        test r15d, r15d
002BB650  0F 84 CA 06 42 00               je 0x1406dbd20
002BB656  E9 D8 06 42 00                  jmp 0x1406dbd33
002BB65B  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
002BB660  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
002BB668  E9 9B FC FF FF                  jmp 0x1402bb308
002BB66D  48 83 FA FF                     cmp rdx, -1
002BB671  0F 84 24 08 42 00               je 0x1406dbe9b
002BB677  41 83 FE 01                     cmp r14d, 1
002BB67B  0F 85 1A 08 42 00               jne 0x1406dbe9b
002BB681  E9 68 08 42 00                  jmp 0x1406dbeee
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSynchronizeFastPageInsert(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m54;
    unsigned __int8 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int8 v_stack_mA1;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p1B;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;
    unsigned __int8 v_stack_p88;
    unsigned __int64 v_stack_pE8;
    unsigned int v_stack_pF0;

    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm0;
    v_r12 = (a3) - (v_rbx);
    v_r12 = (v_r12) >> (4);
    v_r12 = (v_r12) * (a1);
    if (a5 != 0) goto loc_002BAFAC;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 32))) >> (24));
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 32)));
    v_stack_mA4 = 5;
    if ((((unsigned __int8)(a1)) & (8)) != 0) goto loc_002BB357;
loc_002BAF18:
    result = (unsigned int)((v_stack_p1B) & (7));
loc_002BAF23:
    v_rsi = (v_rsi) * ((unsigned int)((unsigned int)(result)));
    v_rsi = (v_rsi) + (0xCE0ULL);
    v_r11 = 0;
    v_stack_m88 = 0;
loc_002BAF40:
    if (0 >= 2) goto loc_002BAF63;
    if ((*(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)(result)) + 0 * 8 * 8 + 15936)) >= 0x1000ULL) goto loc_002BB415;
loc_002BAF5F:
    v_rbx = (unsigned int)((0) + 1);
    goto loc_002BAF40;
loc_002BAF63:
    if ((*(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)(result)) + 0 * 8 * 8 + 15936)) == 0x1000ULL) goto loc_002BB4DE;
loc_002BAF69:
    if ((*(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(v_rbx)) * 8 * 8 + 15936)) < 0x1000ULL) goto loc_002BB343;
    *(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(v_rbx)) * 8 * 8 + 15936) = 0;
    *(unsigned __int8 *)(a6 + 2) = 1;
    if ((unsigned int)(v_rbx) != 0) {
        *(unsigned __int8 *)(a6 + 2) = 2;
    }
    *(unsigned __int8 *)(a6 + 1) = 1;
    goto loc_002BB343;
loc_002BAFAC:
    v_stack_mA8 = 1;
    v_rdi = (a5) - (v_rbx);
    v_rdi = (v_rdi) >> (4);
    v_rdi = (v_rdi) * ((unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(v_rbx)) * 8);
    v_r11 = 0;
    v_stack_mA4 = 5;
    v_stack_m88 = 0;
loc_002BAFE0:
    v_stack_mA0 = v_rdi;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13679249)))) >= 64) goto loc_002BB5AE;
    a2 = 0;
    if (64 >= = 1) {
        a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) * (64));
    }
    v_stack_m98 = (unsigned int)(a3);
    a4 = (v_r12 + v_r12 * 2) << (4);
    v_stack_p18 = 0;
    v_stack_m94 = 0;
    result = (*(unsigned __int64 *)(a4 + v_rbx * 1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m70 = a4 + v_rbx * 1;
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12013635) + result * 8);
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 12004189)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12004187))))) goto loc_002BB08A;
    result = ((int)(*(unsigned int *)(v_rip + 12004189))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 12004261));
    if (v_r12 < (*(unsigned __int64 *)(result))) goto loc_002BB08A;
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 12004189)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12004187))))) goto loc_002BB0C7;
    if (v_r12 < (*(unsigned __int64 *)(result + 16))) goto loc_002BB0C7;
loc_002BB08A:
loc_002BB08D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12004187)))) < 0) goto loc_002BB367;
    a3 = (unsigned int)((0 + (unsigned int)(*(unsigned int *)(v_rip + 12004187)) * 1) >> (1));
    result = ((int)((unsigned int)(a3))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 12004214));
    if (v_r12 < (*(unsigned __int64 *)(result))) goto loc_002BB4BA;
    if (((unsigned int)(a3)) != (*(unsigned int *)(v_rip + 12004106))) goto loc_002BB402;
loc_002BB0C0:
    *(unsigned int *)(v_rip + 12004089) = (unsigned int)(a3);
loc_002BB0C7:
    v_stack_m60 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    if (a5 != 0) goto loc_002BB59F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + v_rbx * 1 + 32))) >> (24));
    v_stack_mA4 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_rbx * 1 + 32)));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_002BB3D3;
loc_002BB0F8:
    v_rsi = (unsigned int)((v_stack_mA1) & (7));
loc_002BB100:
    v_stack_mA4 = (unsigned int)(v_rsi);
loc_002BB104:
    v_stack_m5C = (unsigned int)(v_rsi);
    if ((*(unsigned __int64 *)(v_rip + 12004124)) != 0) goto loc_002BB437;
    a2 = 0;
loc_002BB118:
    v_r10 = (a5) * ((unsigned int)(v_stack_m60));
    v_stack_m58 = 0;
    v_r10 = (v_r10) + (*(unsigned __int64 *)(v_stack_m78 + 16));
    v_stack_m54 = (unsigned int)((int)(a4));
    if (((unsigned int)((int)(a4))) < 9) goto loc_002BB568;
    a1 = (0 * 8 + 59) + ((unsigned int)((unsigned int)(v_rsi)));
    result = (0) * (a1);
    result = (result) + (v_r10);
    v_stack_m68 = result;
loc_002BB162:
    a4 = (v_stack_m78) + (0x2E40ULL);
    a3 = ((unsigned int)((unsigned int)(v_rsi))) << (9);
    a3 = (a3) + (a4);
    v_stack_m80 = 0;
    v_stack_m90 = a3;
loc_002BB192:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_mA8)))) goto loc_002BB65B;
    if (v_rdi != -1) goto loc_002BB1E2;
loc_002BB1A1:
    if ((*(unsigned __int64 *)(a3 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m98))) * 8)) != -1) goto loc_002BB2B8;
    v_r13 = (unsigned int)((0) + 1);
    v_r14 = (unsigned int)((0) + 1);
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m98)) + 1);
    v_rsi = (unsigned int)((v_rsi) & (63));
    goto loc_002BB192;
loc_002BB1C2:
    if (condition_is_above_or_equal) goto loc_002BB2D5;
    v_r14 = (unsigned int)((v_r14) + 1);
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_rsi = (unsigned int)((v_rsi) & (63));
    goto loc_002BB192;
loc_002BB1E2:
    if (v_stack_p18 != 0) goto loc_002BB1A1;
loc_002BB1F7:
loc_002BB206:
    if (0 >= 4) goto loc_002BB1C2;
    if ((*(unsigned __int8 *)(a6 + 16 + 8)) != 0) goto loc_002BB21B;
loc_002BB212:
    a1 = (0) + 1;
    result = (a6 + 16) + (24);
    goto loc_002BB206;
loc_002BB21B:
    if (a5 != (*(unsigned __int64 *)(result))) goto loc_002BB212;
loc_002BB225:
    *(unsigned __int64 *)(a6 + 0 + 0 * 2 * 8 + 8) = v_stack_mA0;
    *(unsigned __int64 *)(a6 + 0 + 0 * 2 * 8 + 16) = a5;
    result = 0 + 0 * 2;
    v_r10 = 0;
    if (v_stack_m94 == 0) {
        a1 = v_stack_p10;
        a1 = (a1) + (32);
        v_stack_m94 = 1;
        result = ExAcquireSpinLockSharedAtDpcLevel(a1, v_stack_mA0, a3, a4);
        a2 = v_stack_mA0;
        v_r11 = 0;
        a3 = v_stack_m90;
        v_r10 = v_stack_m80;
    }
    if (v_stack_p18 == 0) goto loc_002BB624;
loc_002BB27F:
    if ((*(unsigned __int64 *)(a3 + (unsigned int)((unsigned int)(v_rsi)) * 8)) == v_stack_mA0) goto loc_002BB63B;
    if ((*(unsigned __int8 *)(a6 + 0 + 0 * 2 * 8 + 24)) != 0) {
        *(unsigned __int8 *)(a6 + 0 + 0 * 2 * 8 + 24) = 0;
    }
    v_r14 = (unsigned int)((v_r14) - 1);
    v_r14 = (unsigned int)((v_r14) + 1);
    v_rsi = (unsigned int)((v_rsi) - 1);
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_rsi = (unsigned int)((v_rsi) & (63));
    goto loc_002BB192;
loc_002BB2B8:
    v_rdi = (v_stack_mA0 + v_stack_mA0 * 2) << (4);
    v_rdi = (v_rdi) + ((unsigned int)(v_stack_mA8));
    goto loc_002BB1F7;
loc_002BB2D5:
    if (v_stack_mA0 == -1) goto loc_002BB3F4;
    if (v_stack_p18 != 0) goto loc_002BB3F4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_002BB3F4;
    v_r14 = (unsigned int)((v_r14) + 1);
loc_002BB308:
    if (((unsigned int)(v_r14)) == 64) goto loc_002BB51D;
    if (((unsigned int)(v_r14)) == 1) goto loc_002BB50A;
loc_002BB324:
    *(unsigned __int8 *)(a6 + 0 + 0 * 2 * 8) = 1;
    if (0 < 2) goto loc_002BB66D;
loc_002BB343:
    v_rsp = (v_rsp) + (160);
    return result;
loc_002BB357:
    if (a3 >= (a6 + 0 + 0 * 2 * 8)) goto loc_002BB381;
loc_002BB35F:
    goto loc_002BAF23;
loc_002BB367:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x5180ULL), v_r12, a4);
loc_002BB381:
    a2 = (*(unsigned __int64 *)(v_rip + 12003672) + *(unsigned __int64 *)(v_rip + 12003672) * 2) << (4);
    a2 = (a2) + (1);
    if (v_r12 >= a2) goto loc_002BB35F;
    if (v_r12 < (*(unsigned __int64 *)(v_rip + 12036190))) goto loc_002BB3B3;
    a1 = (*(unsigned __int64 *)(v_rip + 12036190)) + (0x800ULL);
    if (v_r12 < a1) goto loc_002BB35F;
loc_002BB3B3:
    result = (unsigned int)((result) >> (16));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 6) goto loc_002BAF18;
    result = MiGetPfnSlabType(v_r12, a2, v_r12, a4);
    if (((unsigned int)(result)) != 9) goto loc_002BAF18;
    goto loc_002BB35F;
loc_002BB3D3:
    if ((a6 + 0 + 0 * 2 * 8) >= result) goto loc_002BB452;
    goto loc_002BB100;
loc_002BB3F4:
    *(unsigned __int8 *)(a6 + 0 + 0 * 2 * 8 + v_r10 + v_r10 * 2 * 8 + 24) = 1;
    goto loc_002BB225;
loc_002BB402:
    if (v_r12 < (*(unsigned __int64 *)(v_r10 + v_r10 * 2 + 16))) goto loc_002BB0C0;
    goto loc_002BB08D;
loc_002BB415:
    if ((v_r10 + v_r10 * 2) >= 0x2000ULL) goto loc_002BB611;
    result = ExTryAcquireSpinLockExclusiveAtDpcLevel(v_stack_p8 + v_r13 * 1, v_r12 + 1, v_r12, a4);
    if ((unsigned int)(result) != 0) goto loc_002BAF69;
    goto loc_002BAF5F;
loc_002BB437:
    a4 = (a4) >> (4);
    a4 = (a4) * (1);
    result = MiPageToChannel(a4, v_r12 + 1, v_r12, a4);
    v_r11 = 0;
    goto loc_002BB118;
loc_002BB452:
    a1 = (*(unsigned __int64 *)(v_rip + 12003463) + *(unsigned __int64 *)(v_rip + 12003463) * 2) << (4);
    a1 = (a1) + (1);
    if ((a6 + 0 + 0 * 2 * 8) >= a1) goto loc_002BB100;
    a1 = (a4) >> (4);
    a1 = (a1) * (1);
    result = MiIsDecayPfn(a1, (unsigned __int8)(result), v_r12, a4);
    if ((unsigned int)(result) != 0) goto loc_002BB100;
    a3 = (unsigned int)((v_r12) >> (16));
    a3 = (unsigned __int8)((a3) & (7));
    if (((unsigned __int8)(a3)) == 6) goto loc_002BB0F8;
    result = MiGetPfnSlabType(a6 + 0 + 0 * 2 * 8, (unsigned __int8)(result), a3, a4);
    if (((unsigned int)(result)) != 9) goto loc_002BB0F8;
    goto loc_002BB100;
loc_002BB4BA:
    if ((unsigned int)(a3) != 0) goto loc_002BB61B;
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (unsigned int)(0x5180ULL), v_r12, result);
loc_002BB4DE:
    v_stack_p30 = 64;
    v_r11 = 0;
    goto loc_002BAFE0;
loc_002BB50A:
    if (((unsigned int)(0x5180ULL)) == -1) goto loc_002BB324;
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_002BB324;
loc_002BB51D:
    if (v_stack_p44 != 0) {
        a2 = a6 + 0 + 0 * 2 * 8;
        *(unsigned __int8 *)(a6 + 0 + 0 * 2 * 8) = 1;
        a1 = v_stack_pE8;
        result = MiReleasePageListLock(a1, a2, v_r12, result);
        *(unsigned __int8 *)(a6 + 0 + 0 * 2 * 8) = 0;
    }
    if (1 == 1) goto loc_002BB5B7;
loc_002BB543:
    *(unsigned __int8 *)(a6 + 0 + 0 * 2 * 8 + 2) = 1;
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) {
        *(unsigned __int8 *)(a6 + 0 + 0 * 2 * 8 + 2) = 2;
    }
    if (((unsigned int)(v_r13)) >= 32) {
        *(unsigned __int8 *)(a6 + 0 + 0 * 2 * 8 + 1) = 1;
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_pE8 + 32, a2, v_r12, result);
    goto loc_002BB343;
loc_002BB568:
    if (((unsigned int)((unsigned int)(v_stack_p18))) == 8) goto loc_002BB5DA;
    v_stack_p88 = 0;
    a1 = 0;
loc_002BB578:
    a2 = (a2) * ((unsigned int)((unsigned int)(-1 + 6)) + 0 * 8);
    a1 = ((unsigned int)((unsigned int)(-1 + 6)) + 0 * 8) * ((unsigned int)(v_stack_p18));
    a2 = (a2) + (*(unsigned __int64 *)(a1 + a5 * 1 + 15768));
    v_stack_p70 = a2;
    goto loc_002BB162;
loc_002BB59F:
    goto loc_002BB104;
loc_002BB5AE:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(-1 + 6))) & (63));
    goto loc_002BB015;
loc_002BB5B7:
    if (v_stack_p38 == -1) goto loc_002BB543;
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_002BB543;
    *(unsigned __int8 *)(a6 + 0 + 0 * 2 * 8 + 2) = 3;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_pE8 + 32, a2, a3, result);
    goto loc_002BB343;
loc_002BB5DA:
    v_rbx = (a6 + 0 + 0 * 2 * 8) - (result);
    v_rbx = (v_rbx) >> (4);
    v_rbx = (v_rbx) * (1);
    v_rbx = (v_rbx) >> (9);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12065871) + v_rbx * 2 + 1)) & (127));
    v_stack_p88 = (unsigned __int8)(a1);
    goto loc_002BB578;
loc_002BB611:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(a1, a2, a3, result);
    goto loc_002BAF69;
loc_002BB61B:
    goto loc_002BB08D;
loc_002BB624:
    if (a2 == -1) goto loc_002BB27F;
loc_002BB63B:
loc_002BB65B:
    goto loc_002BB308;
loc_002BB66D:
}
```

## 5. (Beta) C Style

```c
int64_t MiSynchronizeFastPageInsert(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, int64_t Arg5, void *Arg6)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m54;
    uint8_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint8_t v_stack_mA1;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint8_t v_stack_p1B;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p44;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;
    uint8_t v_stack_p88;
    uint64_t v_stack_pE8;
    uint32_t v_stack_pF0;

    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    *(uint64_t *)(local_rsp - 0x78) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm0;
    local_r12 = (Arg3) - (local_rbx);
    local_r12 = (local_r12) >> (4);
    local_r12 = (local_r12) * (Arg1);
    if (Arg5 != 0) goto loc_002BAFAC;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3 + 0x20))) >> (24));
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x20)));
    v_stack_mA4 = 5;
    if ((((uint8_t)(Arg1)) & (8)) != 0) goto loc_002BB357;
loc_002BAF18:
    result = (uint32_t)((v_stack_p1B) & (7));
loc_002BAF23:
    local_rsi = (local_rsi) * ((uint32_t)((uint32_t)(result)));
    local_rsi = (local_rsi) + (0xCE0ULL);
    local_r11 = 0;
    v_stack_m88 = 0;
loc_002BAF40:
    if (0 >= 2) goto loc_002BAF63;
    if ((*(uint64_t *)(Arg1 + (uint32_t)((uint32_t)(result)) + 0x0 * 8 * 8 + 0x3E40)) >= 0x1000ULL) goto loc_002BB415;
loc_002BAF5F:
    local_rbx = (uint32_t)((0) + 1);
    goto loc_002BAF40;
loc_002BAF63:
    if ((*(uint64_t *)(Arg1 + (uint32_t)((uint32_t)(result)) + 0x0 * 8 * 8 + 0x3E40)) == 0x1000ULL) goto loc_002BB4DE;
loc_002BAF69:
    if ((*(uint64_t *)(Arg1 + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(local_rbx)) * 8 * 8 + 0x3E40)) < 0x1000ULL) goto loc_002BB343;
    *(uint64_t *)(Arg1 + (uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(local_rbx)) * 8 * 8 + 0x3E40) = 0;
    *(uint8_t *)(arg6 + 0x2) = 1;
    if ((uint32_t)(local_rbx) != 0) {
        *(uint8_t *)(arg6 + 0x2) = 2;
    }
    *(uint8_t *)(arg6 + 0x1) = 1;
    goto loc_002BB343;
loc_002BAFAC:
    v_stack_mA8 = 1;
    local_rdi = (Arg5) - (local_rbx);
    local_rdi = (local_rdi) >> (4);
    local_rdi = (local_rdi) * ((uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(local_rbx)) * 8);
    local_r11 = 0;
    v_stack_mA4 = 5;
    v_stack_m88 = 0;
loc_002BAFE0:
    v_stack_mA0 = local_rdi;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD0BA91)))) >= 64) goto loc_002BB5AE;
    Arg2 = 0;
    if (64 >= = 1) {
        Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) * (64));
    }
    v_stack_m98 = (uint32_t)(Arg3);
    Arg4 = (local_r12 + local_r12 * 2) << (4);
    v_stack_p18 = 0;
    v_stack_m94 = 0;
    result = (*(uint64_t *)(Arg4 + local_rbx * 1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m70 = Arg4 + local_rbx * 1;
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB75043) + result * 8);
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xB72B5D)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB72B5B))))) goto loc_002BB08A;
    result = ((int32_t)(*(uint32_t *)(v_rip + 0xB72B5D))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xB72BA5));
    if (local_r12 < (*(uint64_t *)(result))) goto loc_002BB08A;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xB72B5D)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB72B5B))))) goto loc_002BB0C7;
    if (local_r12 < (*(uint64_t *)(result + 0x10))) goto loc_002BB0C7;
loc_002BB08A:
loc_002BB08D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB72B5B)))) < 0) goto loc_002BB367;
    Arg3 = (uint32_t)((0 + (uint32_t)(*(uint32_t *)(v_rip + 0xB72B5B)) * 1) >> (1));
    result = ((int32_t)((uint32_t)(Arg3))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xB72B76));
    if (local_r12 < (*(uint64_t *)(result))) goto loc_002BB4BA;
    if (((uint32_t)(Arg3)) != (*(uint32_t *)(v_rip + 0xB72B0A))) goto loc_002BB402;
loc_002BB0C0:
    *(uint32_t *)(v_rip + 0xB72AF9) = (uint32_t)(Arg3);
loc_002BB0C7:
    v_stack_m60 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    if (Arg5 != 0) goto loc_002BB59F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4 + local_rbx * 1 + 0x20))) >> (24));
    v_stack_mA4 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + local_rbx * 1 + 0x20)));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_002BB3D3;
loc_002BB0F8:
    local_rsi = (uint32_t)((v_stack_mA1) & (7));
loc_002BB100:
    v_stack_mA4 = (uint32_t)(local_rsi);
loc_002BB104:
    v_stack_m5C = (uint32_t)(local_rsi);
    if ((*(uint64_t *)(v_rip + 0xB72B1C)) != 0) goto loc_002BB437;
    Arg2 = 0;
loc_002BB118:
    local_r10 = (Arg5) * ((uint32_t)(v_stack_m60));
    v_stack_m58 = 0;
    local_r10 = (local_r10) + (*(uint64_t *)(v_stack_m78 + 0x10));
    v_stack_m54 = (uint32_t)((int32_t)(Arg4));
    if (((uint32_t)((int32_t)(Arg4))) < 9) goto loc_002BB568;
    Arg1 = (0 * 8 + 59) + ((uint32_t)((uint32_t)(local_rsi)));
    result = (0) * (Arg1);
    result = (result) + (local_r10);
    v_stack_m68 = result;
loc_002BB162:
    Arg4 = (v_stack_m78) + (0x2E40ULL);
    Arg3 = ((uint32_t)((uint32_t)(local_rsi))) << (9);
    Arg3 = (Arg3) + (Arg4);
    v_stack_m80 = 0;
    v_stack_m90 = Arg3;
loc_002BB192:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_mA8)))) goto loc_002BB65B;
    if (local_rdi != -1) goto loc_002BB1E2;
loc_002BB1A1:
    if ((*(uint64_t *)(arg3 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m98))) * 8)) != -1) goto loc_002BB2B8;
    local_r13 = (uint32_t)((0) + 1);
    local_r14 = (uint32_t)((0) + 1);
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m98)) + 1);
    local_rsi = (uint32_t)((local_rsi) & (63));
    goto loc_002BB192;
loc_002BB1C2:
    if (condition_is_above_or_equal) goto loc_002BB2D5;
    local_r14 = (uint32_t)((local_r14) + 1);
    local_rsi = (uint32_t)((local_rsi) + 1);
    local_rsi = (uint32_t)((local_rsi) & (63));
    goto loc_002BB192;
loc_002BB1E2:
    if (v_stack_p18 != 0) goto loc_002BB1A1;
loc_002BB1F7:
loc_002BB206:
    if (0 >= 4) goto loc_002BB1C2;
    if ((*(uint8_t *)(arg6 + 0x10 + 0x8)) != 0) goto loc_002BB21B;
loc_002BB212:
    Arg1 = (0) + 1;
    result = (Arg6 + 16) + (24);
    goto loc_002BB206;
loc_002BB21B:
    if (Arg5 != (*(uint64_t *)(result))) goto loc_002BB212;
loc_002BB225:
    *(uint64_t *)(arg6 + 0x0 + 0x0 * 2 * 8 + 0x8) = v_stack_mA0;
    *(uint64_t *)(arg6 + 0x0 + 0x0 * 2 * 8 + 0x10) = Arg5;
    result = 0 + 0 * 2;
    local_r10 = 0;
    if (v_stack_m94 == 0) {
        Arg1 = v_stack_p10;
        Arg1 = (Arg1) + (32);
        v_stack_m94 = 1;
        result = ExAcquireSpinLockSharedAtDpcLevel(Arg1, v_stack_mA0, Arg3, Arg4);
        Arg2 = v_stack_mA0;
        local_r11 = 0;
        Arg3 = v_stack_m90;
        local_r10 = v_stack_m80;
    }
    if (v_stack_p18 == 0) goto loc_002BB624;
loc_002BB27F:
    if ((*(uint64_t *)(arg3 + (uint32_t)((uint32_t)(local_rsi)) * 8)) == v_stack_mA0) goto loc_002BB63B;
    if ((*(uint8_t *)(arg6 + 0x0 + 0x0 * 2 * 8 + 0x18)) != 0) {
        *(uint8_t *)(arg6 + 0x0 + 0x0 * 2 * 8 + 0x18) = 0;
    }
    local_r14 = (uint32_t)((local_r14) - 1);
    local_r14 = (uint32_t)((local_r14) + 1);
    local_rsi = (uint32_t)((local_rsi) - 1);
    local_rsi = (uint32_t)((local_rsi) + 1);
    local_rsi = (uint32_t)((local_rsi) & (63));
    goto loc_002BB192;
loc_002BB2B8:
    local_rdi = (v_stack_mA0 + v_stack_mA0 * 2) << (4);
    local_rdi = (local_rdi) + ((uint32_t)(v_stack_mA8));
    goto loc_002BB1F7;
loc_002BB2D5:
    if (v_stack_mA0 == -1) goto loc_002BB3F4;
    if (v_stack_p18 != 0) goto loc_002BB3F4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_002BB3F4;
    local_r14 = (uint32_t)((local_r14) + 1);
loc_002BB308:
    if (((uint32_t)(local_r14)) == 64) goto loc_002BB51D;
    if (((uint32_t)(local_r14)) == 1) goto loc_002BB50A;
loc_002BB324:
    *(uint8_t *)(arg6 + 0x0 + 0x0 * 2 * 8) = 1;
    if (0 < 2) goto loc_002BB66D;
loc_002BB343:
    local_rsp = (local_rsp) + (160);
    return result;
loc_002BB357:
    if (Arg3 >= (Arg6 + 0 + 0 * 2 * 8)) goto loc_002BB381;
loc_002BB35F:
    goto loc_002BAF23;
loc_002BB367:
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 26, (uint32_t)(0x5180ULL), local_r12, Arg4);
loc_002BB381:
    Arg2 = (*(uint64_t *)(v_rip + 0xB72958) + *(uint64_t *)(v_rip + 0xB72958) * 2) << (4);
    Arg2 = (Arg2) + (1);
    if (local_r12 >= Arg2) goto loc_002BB35F;
    if (local_r12 < (*(uint64_t *)(v_rip + 0xB7A85E))) goto loc_002BB3B3;
    Arg1 = (*(uint64_t *)(v_rip + 0xB7A85E)) + (0x800ULL);
    if (local_r12 < Arg1) goto loc_002BB35F;
loc_002BB3B3:
    result = (uint32_t)((result) >> (16));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 6) goto loc_002BAF18;
    result = MiGetPfnSlabType(local_r12, Arg2, local_r12, Arg4);
    if (((uint32_t)(result)) != 9) goto loc_002BAF18;
    goto loc_002BB35F;
loc_002BB3D3:
    if ((Arg6 + 0 + 0 * 2 * 8) >= result) goto loc_002BB452;
    goto loc_002BB100;
loc_002BB3F4:
    *(uint8_t *)(arg6 + 0x0 + 0x0 * 2 * 8 + local_r10 + local_r10 * 2 * 8 + 0x18) = 1;
    goto loc_002BB225;
loc_002BB402:
    if (local_r12 < (*(uint64_t *)(local_r10 + local_r10 * 2 + 0x10))) goto loc_002BB0C0;
    goto loc_002BB08D;
loc_002BB415:
    if ((local_r10 + local_r10 * 2) >= 0x2000ULL) goto loc_002BB611;
    result = ExTryAcquireSpinLockExclusiveAtDpcLevel(v_stack_p8 + local_r13 * 1, local_r12 + 1, local_r12, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002BAF69;
    goto loc_002BAF5F;
loc_002BB437:
    Arg4 = (Arg4) >> (4);
    Arg4 = (Arg4) * (1);
    result = MiPageToChannel(Arg4, local_r12 + 1, local_r12, Arg4);
    local_r11 = 0;
    goto loc_002BB118;
loc_002BB452:
    Arg1 = (*(uint64_t *)(v_rip + 0xB72887) + *(uint64_t *)(v_rip + 0xB72887) * 2) << (4);
    Arg1 = (Arg1) + (1);
    if ((Arg6 + 0 + 0 * 2 * 8) >= Arg1) goto loc_002BB100;
    Arg1 = (Arg4) >> (4);
    Arg1 = (Arg1) * (1);
    result = MiIsDecayPfn(Arg1, (uint8_t)(result), local_r12, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002BB100;
    Arg3 = (uint32_t)((local_r12) >> (16));
    Arg3 = (uint8_t)((Arg3) & (7));
    if (((uint8_t)(Arg3)) == 6) goto loc_002BB0F8;
    result = MiGetPfnSlabType(Arg6 + 0 + 0 * 2 * 8, (uint8_t)(result), Arg3, Arg4);
    if (((uint32_t)(result)) != 9) goto loc_002BB0F8;
    goto loc_002BB100;
loc_002BB4BA:
    if ((uint32_t)(Arg3) != 0) goto loc_002BB61B;
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (uint32_t)(0x5180ULL), local_r12, result);
loc_002BB4DE:
    v_stack_p30 = 64;
    local_r11 = 0;
    goto loc_002BAFE0;
loc_002BB50A:
    if (((uint32_t)(0x5180ULL)) == -1) goto loc_002BB324;
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_002BB324;
loc_002BB51D:
    if (v_stack_p44 != 0) {
        Arg2 = Arg6 + 0 + 0 * 2 * 8;
        *(uint8_t *)(arg6 + 0x0 + 0x0 * 2 * 8) = 1;
        Arg1 = v_stack_pE8;
        result = MiReleasePageListLock(Arg1, Arg2, local_r12, result);
        *(uint8_t *)(arg6 + 0x0 + 0x0 * 2 * 8) = 0;
    }
    if (1 == 1) goto loc_002BB5B7;
loc_002BB543:
    *(uint8_t *)(arg6 + 0x0 + 0x0 * 2 * 8 + 0x2) = 1;
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) {
        *(uint8_t *)(arg6 + 0x0 + 0x0 * 2 * 8 + 0x2) = 2;
    }
    if (((uint32_t)(local_r13)) >= 32) {
        *(uint8_t *)(arg6 + 0x0 + 0x0 * 2 * 8 + 0x1) = 1;
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_pE8 + 32, Arg2, local_r12, result);
    goto loc_002BB343;
loc_002BB568:
    if (((uint32_t)((uint32_t)(v_stack_p18))) == 8) goto loc_002BB5DA;
    v_stack_p88 = 0;
    Arg1 = 0;
loc_002BB578:
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(-1 + 6)) + 0 * 8);
    Arg1 = ((uint32_t)((uint32_t)(-1 + 6)) + 0 * 8) * ((uint32_t)(v_stack_p18));
    Arg2 = (Arg2) + (*(uint64_t *)(Arg1 + Arg5 * 1 + 0x3D98));
    v_stack_p70 = Arg2;
    goto loc_002BB162;
loc_002BB59F:
    goto loc_002BB104;
loc_002BB5AE:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(-1 + 6))) & (63));
    goto loc_002BB015;
loc_002BB5B7:
    if (v_stack_p38 == -1) goto loc_002BB543;
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_002BB543;
    *(uint8_t *)(arg6 + 0x0 + 0x0 * 2 * 8 + 0x2) = 3;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_pE8 + 32, Arg2, Arg3, result);
    goto loc_002BB343;
loc_002BB5DA:
    local_rbx = (Arg6 + 0 + 0 * 2 * 8) - (result);
    local_rbx = (local_rbx) >> (4);
    local_rbx = (local_rbx) * (1);
    local_rbx = (local_rbx) >> (9);
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0xB81C4F) + local_rbx * 2 + 0x1)) & (127));
    v_stack_p88 = (uint8_t)(Arg1);
    goto loc_002BB578;
loc_002BB611:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(Arg1, Arg2, Arg3, result);
    goto loc_002BAF69;
loc_002BB61B:
    goto loc_002BB08D;
loc_002BB624:
    if (Arg2 == -1) goto loc_002BB27F;
loc_002BB63B:
loc_002BB65B:
    goto loc_002BB308;
loc_002BB66D:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x20` | `32` | `R` |
| `Arg6` | `+ 0x0` | `8` | `W` |
| `Arg6` | `+ 0x0` | `64` | `R` |
| `Arg6` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg6` | `+ 0x1` | `8` | `W` |
| `Arg6` | `+ 0x2` | `8` | `W` |
| `Arg6` | `+ 0x8` | `8` | `R` |
| `Arg6` | `+ 0x8` | `64` | `W` |
| `Arg6` | `+ 0x10` | `64` | `R` |
| `Arg6` | `+ 0x10` | `64` | `W` |
| `Arg6` | `+ 0x18` | `8` | `R` |
| `Arg6` | `+ 0x18` | `8` | `W` |
| `Arg6` | `+ 0x18 + rax*8` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002BAE80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
