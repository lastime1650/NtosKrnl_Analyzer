# KiSwInterruptDispatch

- RVA: `0x0050A5C0`–`0x0050BD7E` (길이 `6,078` bytes)
- VA: `0x000000014050A5C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2BFC`
- 디코드: `1,464`개 명령, `6,078/6,078` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0050A5F3` → [KeExitRetpoline](../46/KeExitRetpoline_function_00468E7C.md) (function, `0x00468E7C`)
- `0x0050A64C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0050A68F` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0050A95D` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0050AC7C` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0050AE1A` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0050AE3A` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0050AEBA` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0050AFF4` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0050B125` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0050B154` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0050B1B7` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0050B2CF` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0050B34F` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0050B48C` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0050B5B9` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x0050BB9D` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x0050BBA5` → [KiGetTrapFrameMode](../45/KiGetTrapFrameMode_function_00450C30.md) (function, `0x00450C30`)
- `0x0050BBF3` → [KiReadKernelDr7](../5B/KiReadKernelDr7_function_005B8A98.md) (function, `0x005B8A98`)
- `0x0050BD46` → [KeGuardCheckICall](../../initkdbg/BE/KeGuardCheckICall_function_00BEAA70.md) (function, `0x00BEAA70`)
- `0x0050BD78` → [SdbpCheckDll](../../initkdbg/BE/SdbpCheckDll_function_00BEA7B0.md) (function, `0x00BEA7B0`)

### Direct callers
- [KiSwInterrupt](../6B/KiSwInterrupt_function_006B8070.md) at `0x006B840F`

### Static image references
- `0x0050A5DD` → RVA `0x00FC6A48` (`ALMOSTRO`; read)
- `0x0050A603` → RVA `0x00E0F290` (`.data`; read)
- `0x0050A66F` → RVA `0x0051AD30` (`.text`; read)
- `0x0050A80D` → RVA `0x00FC6A50` (`ALMOSTRO`; read)
- `0x0050BBDD` → RVA `0x00E0AA1D` (`.data`; read)
- `0x0050BBE6` → RVA `0x00F475DC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x0050A64C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0050A95D` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0050AC7C` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0050AE1A` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0050AE3A` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0050AEBA` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0050AFF4` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0050B125` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0050B154` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0050B1B7` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0050B2CF` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0050B34F` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0050B48C` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0050B5B9` → [sub_00BE8384](../../initkdbg/BE/Unknown_function_00BE8384.md) (`.text` → `INITKDBG`)
  - `0x0050BB9D` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`.text` → `INITKDBG`)
  - `0x0050BD46` → [KeGuardCheckICall](../../initkdbg/BE/KeGuardCheckICall_function_00BEAA70.md) (`.text` → `INITKDBG`)
  - `0x0050BD78` → [SdbpCheckDll](../../initkdbg/BE/SdbpCheckDll_function_00BEA7B0.md) (`.text` → `INITKDBG`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0050A5C0  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0050A5C5  55                              push rbp
0050A5C6  53                              push rbx
0050A5C7  56                              push rsi
0050A5C8  57                              push rdi
0050A5C9  41 54                           push r12
0050A5CB  41 55                           push r13
0050A5CD  41 56                           push r14
0050A5CF  41 57                           push r15
0050A5D1  48 8D 6C 24 E8                  lea rbp, [rsp - 0x18]
0050A5D6  48 81 EC 18 01 00 00            sub rsp, 0x118
0050A5DD  48 8B 3D 64 C4 AB 00            mov rdi, qword ptr [rip + 0xabc464]
0050A5E4  4C 8B E9                        mov r13, rcx
0050A5E7  F7 87 DC 09 00 00 00 00 10 00   test dword ptr [rdi + 0x9dc], 0x100000
0050A5F1  74 07                           je 0x14050a5fa
0050A5F3  E8 84 E8 F5 FF                  call 0x140468e7c
0050A5F8  EB 03                           jmp 0x14050a5fd
0050A5FA  0F AE E8                        lfence
0050A5FD  0F 31                           rdtsc
0050A5FF  48 C1 E2 20                     shl rdx, 0x20
0050A603  4C 8D 05 86 4C 90 00            lea r8, [rip + 0x904c86]
0050A60A  48 0B C2                        or rax, rdx
0050A60D  48 BE 01 20 00 04 80 00 10 70   movabs rsi, 0x7010008004002001
0050A617  48 8B C8                        mov rcx, rax
0050A61A  48 8B D0                        mov rdx, rax
0050A61D  48 C1 C9 03                     ror rcx, 3
0050A621  48 8B C6                        mov rax, rsi
0050A624  48 33 D1                        xor rdx, rcx
0050A627  B9 42 00 00 00                  mov ecx, 0x42
0050A62C  48 F7 E2                        mul rdx
0050A62F  48 89 55 A8                     mov qword ptr [rbp - 0x58], rdx
0050A633  48 33 D0                        xor rdx, rax
0050A636  48 83 E2 0F                     and rdx, 0xf
0050A63A  45 8B 04 90                     mov r8d, dword ptr [r8 + rdx*4]
0050A63E  48 8B 97 D8 0A 00 00            mov rdx, qword ptr [rdi + 0xad8]
0050A645  48 81 C2 3F 0B 00 00            add rdx, 0xb3f
0050A64C  E8 9F 7A 67 00                  call 0x140b820f0
0050A651  45 33 FF                        xor r15d, r15d
0050A654  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0050A659  4C 8B E0                        mov r12, rax
0050A65C  48 85 C0                        test rax, rax
0050A65F  0F 84 3D 15 00 00               je 0x14050bba2
0050A665  49 8D 5C 24 20                  lea rbx, [r12 + 0x20]
0050A66A  4D 89 64 24 18                  mov qword ptr [r12 + 0x18], r12
0050A66F  48 8D 05 BA 06 01 00            lea rax, [rip + 0x106ba]
0050A676  4D 89 3C 24                     mov qword ptr [r12], r15
0050A67A  48 8B CB                        mov rcx, rbx
0050A67D  49 89 44 24 10                  mov qword ptr [r12 + 0x10], rax
0050A682  48 8B D7                        mov rdx, rdi
0050A685  48 89 5D 68                     mov qword ptr [rbp + 0x68], rbx
0050A689  41 B8 E8 0A 00 00               mov r8d, 0xae8
0050A68F  E8 AC C1 1B 00                  call 0x1406c6840
0050A694  49 8D 84 24 08 0B 00 00         lea rax, [r12 + 0xb08]
0050A69C  49 89 BC 24 E0 0A 00 00         mov qword ptr [r12 + 0xae0], rdi
0050A6A4  48 89 83 C8 0A 00 00            mov qword ptr [rbx + 0xac8], rax
0050A6AB  0F 31                           rdtsc
0050A6AD  48 C1 E2 20                     shl rdx, 0x20
0050A6B1  48 0B C2                        or rax, rdx
0050A6B4  44 89 BB 48 08 00 00            mov dword ptr [rbx + 0x848], r15d
0050A6BB  48 8B C8                        mov rcx, rax
0050A6BE  48 8B D0                        mov rdx, rax
0050A6C1  48 C1 C9 03                     ror rcx, 3
0050A6C5  48 8B C6                        mov rax, rsi
0050A6C8  48 33 D1                        xor rdx, rcx
0050A6CB  8B 8B 2C 08 00 00               mov ecx, dword ptr [rbx + 0x82c]
0050A6D1  48 F7 E2                        mul rdx
0050A6D4  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
0050A6D8  48 33 C2                        xor rax, rdx
0050A6DB  33 D2                           xor edx, edx
0050A6DD  48 F7 F1                        div rcx
0050A6E0  89 93 40 08 00 00               mov dword ptr [rbx + 0x840], edx
0050A6E6  0F 31                           rdtsc
0050A6E8  4C 8B B3 C0 0A 00 00            mov r14, qword ptr [rbx + 0xac0]
0050A6EF  44 8B 93 34 08 00 00            mov r10d, dword ptr [rbx + 0x834]
0050A6F6  4D 8B CE                        mov r9, r14
0050A6F9  48 C1 E2 20                     shl rdx, 0x20
0050A6FD  48 0B C2                        or rax, rdx
0050A700  48 8B C8                        mov rcx, rax
0050A703  48 8B D0                        mov rdx, rax
0050A706  48 C1 C9 03                     ror rcx, 3
0050A70A  48 8B C6                        mov rax, rsi
0050A70D  48 8B B3 38 08 00 00            mov rsi, qword ptr [rbx + 0x838]
0050A714  48 33 D1                        xor rdx, rcx
0050A717  48 F7 E2                        mul rdx
0050A71A  48 89 55 B8                     mov qword ptr [rbp - 0x48], rdx
0050A71E  33 D0                           xor edx, eax
0050A720  49 8D 84 24 3F 0B 00 00         lea rax, [r12 + 0xb3f]
0050A728  89 93 50 08 00 00               mov dword ptr [rbx + 0x850], edx
0050A72E  48 83 E0 F8                     and rax, 0xfffffffffffffff8
0050A732  48 89 83 D0 0A 00 00            mov qword ptr [rbx + 0xad0], rax
0050A739  49 8B C6                        mov rax, r14
0050A73C  41 8B BE 04 08 00 00            mov edi, dword ptr [r14 + 0x804]
0050A743  49 8D 0C 3E                     lea rcx, [r14 + rdi]
0050A747  4C 3B F1                        cmp r14, rcx
0050A74A  73 0C                           jae 0x14050a758
0050A74C  0F 18 00                        prefetchnta byte ptr [rax]
0050A74F  48 83 C0 40                     add rax, 0x40
0050A753  48 3B C1                        cmp rax, rcx
0050A756  72 F4                           jb 0x14050a74c
0050A758  44 8B DF                        mov r11d, edi
0050A75B  4C 8B C6                        mov r8, rsi
0050A75E  41 C1 EB 07                     shr r11d, 7
0050A762  BA 01 00 00 00                  mov edx, 1
0050A767  45 85 DB                        test r11d, r11d
0050A76A  74 5D                           je 0x14050a7c9
0050A76C  49 BD 01 20 00 04 80 00 10 70   movabs r13, 0x7010008004002001
0050A776  B8 08 00 00 00                  mov eax, 8
0050A77B  4D 33 01                        xor r8, qword ptr [r9]
0050A77E  41 8B CA                        mov ecx, r10d
0050A781  49 D3 C0                        rol r8, cl
0050A784  4D 33 41 08                     xor r8, qword ptr [r9 + 8]
0050A788  49 83 C1 10                     add r9, 0x10
0050A78C  49 D3 C0                        rol r8, cl
0050A78F  48 2B C2                        sub rax, rdx
0050A792  75 E7                           jne 0x14050a77b
0050A794  49 8B C9                        mov rcx, r9
0050A797  49 2B CE                        sub rcx, r14
0050A79A  48 33 CE                        xor rcx, rsi
0050A79D  48 8B C1                        mov rax, rcx
0050A7A0  48 C1 C0 11                     rol rax, 0x11
0050A7A4  48 33 C8                        xor rcx, rax
0050A7A7  49 8B C5                        mov rax, r13
0050A7AA  48 F7 E1                        mul rcx
0050A7AD  33 C2                           xor eax, edx
0050A7AF  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
0050A7B3  44 33 D0                        xor r10d, eax
0050A7B6  BA 01 00 00 00                  mov edx, 1
0050A7BB  41 83 E2 3F                     and r10d, 0x3f
0050A7BF  44 0F 44 D2                     cmove r10d, edx
0050A7C3  41 83 C3 FF                     add r11d, -1
0050A7C7  75 AD                           jne 0x14050a776
0050A7C9  8B D7                           mov edx, edi
0050A7CB  41 BB 01 00 00 00               mov r11d, 1
0050A7D1  83 E2 7F                        and edx, 0x7f
0050A7D4  83 FA 08                        cmp edx, 8
0050A7D7  72 1B                           jb 0x14050a7f4
0050A7D9  8B C2                           mov eax, edx
0050A7DB  48 C1 E8 03                     shr rax, 3
0050A7DF  4D 33 01                        xor r8, qword ptr [r9]
0050A7E2  41 8B CA                        mov ecx, r10d
0050A7E5  49 D3 C0                        rol r8, cl
0050A7E8  49 83 C1 08                     add r9, 8
0050A7EC  83 C2 F8                        add edx, -8
0050A7EF  49 2B C3                        sub rax, r11
0050A7F2  75 EB                           jne 0x14050a7df
0050A7F4  85 D2                           test edx, edx
0050A7F6  74 15                           je 0x14050a80d
0050A7F8  41 0F B6 01                     movzx eax, byte ptr [r9]
0050A7FC  41 8B CA                        mov ecx, r10d
0050A7FF  4C 33 C0                        xor r8, rax
0050A802  4D 03 CB                        add r9, r11
0050A805  49 D3 C0                        rol r8, cl
0050A808  83 C2 FF                        add edx, -1
0050A80B  75 EB                           jne 0x14050a7f8
0050A80D  4C 3B 05 3C C2 AB 00            cmp r8, qword ptr [rip + 0xabc23c]
0050A814  48 B9 E8 B4 C8 91 58 3F A0 A3   movabs rcx, 0xa3a03f5891c8b4e8
0050A81E  0F 84 3E 01 00 00               je 0x14050a962
0050A824  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050A82B  4C 89 30                        mov qword ptr [rax], r14
0050A82E  89 78 10                        mov dword ptr [rax + 0x10], edi
0050A831  44 39 BB 18 09 00 00            cmp dword ptr [rbx + 0x918], r15d
0050A838  0F 85 24 01 00 00               jne 0x14050a962
0050A83E  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050A845  49 8B C8                        mov rcx, r8
0050A848  48 33 0D 01 C2 AB 00            xor rcx, qword ptr [rip + 0xabc201]
0050A84F  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0050A853  48 B9 E8 B4 C8 91 58 3F A0 A3   movabs rcx, 0xa3a03f5891c8b4e8
0050A85D  44 39 BB 18 09 00 00            cmp dword ptr [rbx + 0x918], r15d
0050A864  0F 85 F8 00 00 00               jne 0x14050a962
0050A86A  48 8D 04 0B                     lea rax, [rbx + rcx]
0050A86E  4C 89 BB 28 09 00 00            mov qword ptr [rbx + 0x928], r15
0050A875  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0050A87B  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0050A882  48 C7 83 30 09 00 00 11 01 00 00  mov qword ptr [rbx + 0x930], 0x111
0050A88D  4C 89 83 38 09 00 00            mov qword ptr [rbx + 0x938], r8
0050A894  44 89 9B 18 09 00 00            mov dword ptr [rbx + 0x918], r11d
0050A89B  0F BA E1 1D                     bt ecx, 0x1d
0050A89F  0F 82 BD 00 00 00               jb 0x14050a962
0050A8A5  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
0050A8AF  0F 84 AD 00 00 00               je 0x14050a962
0050A8B5  41 84 CB                        test r11b, cl
0050A8B8  0F 84 A4 00 00 00               je 0x14050a962
0050A8BE  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0050A8C4  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0050A8CA  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
0050A8D1  2B C1                           sub eax, ecx
0050A8D3  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0050A8DA  48 8D 14 19                     lea rdx, [rcx + rbx]
0050A8DE  8B C8                           mov ecx, eax
0050A8E0  48 C1 E9 03                     shr rcx, 3
0050A8E4  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
0050A8E8  EB 21                           jmp 0x14050a90b
0050A8EA  4C 31 02                        xor qword ptr [rdx], r8
0050A8ED  48 8B 02                        mov rax, qword ptr [rdx]
0050A8F0  41 0F B6 C8                     movzx ecx, r8b
0050A8F4  49 33 C2                        xor rax, r10
0050A8F7  83 E1 3F                        and ecx, 0x3f
0050A8FA  49 D3 C8                        ror r8, cl
0050A8FD  4C 03 C0                        add r8, rax
0050A900  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0050A907  48 83 C2 08                     add rdx, 8
0050A90B  49 3B D1                        cmp rdx, r9
0050A90E  75 DA                           jne 0x14050a8ea
0050A910  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
0050A918  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0050A91F  74 41                           je 0x14050a962
0050A921  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0050A927  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050A92E  48 89 18                        mov qword ptr [rax], rbx
0050A931  89 48 10                        mov dword ptr [rax + 0x10], ecx
0050A934  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0050A93B  44 39 BB 18 09 00 00            cmp dword ptr [rbx + 0x918], r15d
0050A942  75 0E                           jne 0x14050a952
0050A944  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050A94B  49 33 C8                        xor rcx, r8
0050A94E  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0050A952  33 D2                           xor edx, edx
0050A954  41 B9 00 01 00 00               mov r9d, 0x100
0050A95A  48 8B CB                        mov rcx, rbx
0050A95D  E8 22 DA 6D 00                  call 0x140be8384
0050A962  B9 04 00 00 00                  mov ecx, 4
0050A967  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
0050A96C  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0050A971  44 8D 59 FD                     lea r11d, [rcx - 3]
0050A975  44 88 38                        mov byte ptr [rax], r15b
0050A978  49 03 C3                        add rax, r11
0050A97B  83 C1 FF                        add ecx, -1
0050A97E  75 F5                           jne 0x14050a975
0050A980  BA 02 00 00 00                  mov edx, 2
0050A985  41 8B CF                        mov ecx, r15d
0050A988  45 33 D2                        xor r10d, r10d
0050A98B  89 4D 70                        mov dword ptr [rbp + 0x70], ecx
0050A98E  44 8D 7A 04                     lea r15d, [rdx + 4]
0050A992  44 8D 72 2E                     lea r14d, [rdx + 0x2e]
0050A996  44 39 93 2C 08 00 00            cmp dword ptr [rbx + 0x82c], r10d
0050A99D  0F 86 45 0C 00 00               jbe 0x14050b5e8
0050A9A3  45 33 ED                        xor r13d, r13d
0050A9A6  48 8B 83 C0 0A 00 00            mov rax, qword ptr [rbx + 0xac0]
0050A9AD  4C 8B C3                        mov r8, rbx
0050A9B0  48 85 C0                        test rax, rax
0050A9B3  45 8B CD                        mov r9d, r13d
0050A9B6  4C 0F 45 C0                     cmovne r8, rax
0050A9BA  41 8B B0 28 08 00 00            mov esi, dword ptr [r8 + 0x828]
0050A9C1  49 03 F0                        add rsi, r8
0050A9C4  44 39 6C 24 48                  cmp dword ptr [rsp + 0x48], r13d
0050A9C9  74 12                           je 0x14050a9dd
0050A9CB  39 4C 24 4C                     cmp dword ptr [rsp + 0x4c], ecx
0050A9CF  77 0C                           ja 0x14050a9dd
0050A9D1  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
0050A9D5  44 8B 4C 24 4C                  mov r9d, dword ptr [rsp + 0x4c]
0050A9DA  49 03 F0                        add rsi, r8
0050A9DD  44 3B C9                        cmp r9d, ecx
0050A9E0  0F 84 FA 00 00 00               je 0x14050aae0
0050A9E6  44 8B D1                        mov r10d, ecx
0050A9E9  48 BB AB AA AA AA AA AA AA AA   movabs rbx, 0xaaaaaaaaaaaaaaab
0050A9F3  45 2B D1                        sub r10d, r9d
0050A9F6  44 8B C9                        mov r9d, ecx
0050A9F9  8B 0E                           mov ecx, dword ptr [rsi]
0050A9FB  83 E9 01                        sub ecx, 1
0050A9FE  0F 84 B0 00 00 00               je 0x14050aab4
0050AA04  41 2B CF                        sub ecx, r15d
0050AA07  0F 84 9A 00 00 00               je 0x14050aaa7
0050AA0D  83 E9 01                        sub ecx, 1
0050AA10  0F 84 85 00 00 00               je 0x14050aa9b
0050AA16  2B CA                           sub ecx, edx
0050AA18  74 76                           je 0x14050aa90
0050AA1A  83 E9 12                        sub ecx, 0x12
0050AA1D  74 6B                           je 0x14050aa8a
0050AA1F  2B CA                           sub ecx, edx
0050AA21  74 3C                           je 0x14050aa5f
0050AA23  83 E9 03                        sub ecx, 3
0050AA26  74 11                           je 0x14050aa39
0050AA28  83 F9 0A                        cmp ecx, 0xa
0050AA2B  0F 84 83 00 00 00               je 0x14050aab4
0050AA31  41 8B C6                        mov eax, r14d
0050AA34  E9 94 00 00 00                  jmp 0x14050aacd
0050AA39  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
0050AA3C  8B 56 28                        mov edx, dword ptr [rsi + 0x28]
0050AA3F  81 E1 FF 0F 00 00               and ecx, 0xfff
0050AA45  48 81 C2 FF 0F 00 00            add rdx, 0xfff
0050AA4C  48 03 D1                        add rdx, rcx
0050AA4F  48 C1 EA 0C                     shr rdx, 0xc
0050AA53  8D 04 92                        lea eax, [rdx + rdx*4]
0050AA56  8D 04 85 30 00 00 00            lea eax, [rax*4 + 0x30]
0050AA5D  EB 69                           jmp 0x14050aac8
0050AA5F  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
0050AA62  8D 48 FF                        lea ecx, [rax - 1]
0050AA65  F7 D8                           neg eax
0050AA67  1B C0                           sbb eax, eax
0050AA69  23 C8                           and ecx, eax
0050AA6B  48 8B C3                        mov rax, rbx
0050AA6E  48 F7 E1                        mul rcx
0050AA71  0F B7 46 28                     movzx eax, word ptr [rsi + 0x28]
0050AA75  48 C1 EA 03                     shr rdx, 3
0050AA79  83 C2 07                        add edx, 7
0050AA7C  83 E2 F8                        and edx, 0xfffffff8
0050AA7F  83 C0 02                        add eax, 2
0050AA82  8D 04 40                        lea eax, [rax + rax*2]
0050AA85  8D 04 C2                        lea eax, [rdx + rax*8]
0050AA88  EB 3E                           jmp 0x14050aac8
0050AA8A  0F B7 46 28                     movzx eax, word ptr [rsi + 0x28]
0050AA8E  EB 0F                           jmp 0x14050aa9f
0050AA90  8B 46 1C                        mov eax, dword ptr [rsi + 0x1c]
0050AA93  83 C0 03                        add eax, 3
0050AA96  C1 E0 04                        shl eax, 4
0050AA99  EB 32                           jmp 0x14050aacd
0050AA9B  0F B7 46 20                     movzx eax, word ptr [rsi + 0x20]
0050AA9F  83 C0 37                        add eax, 0x37
0050AAA2  83 E0 F8                        and eax, 0xfffffff8
0050AAA5  EB 26                           jmp 0x14050aacd
0050AAA7  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
0050AAAA  03 C2                           add eax, edx
0050AAAC  8D 04 40                        lea eax, [rax + rax*2]
0050AAAF  C1 E0 03                        shl eax, 3
0050AAB2  EB 19                           jmp 0x14050aacd
0050AAB4  8B 4E 10                        mov ecx, dword ptr [rsi + 0x10]
0050AAB7  48 8B C3                        mov rax, rbx
0050AABA  48 F7 E1                        mul rcx
0050AABD  48 C1 EA 03                     shr rdx, 3
0050AAC1  8D 04 95 30 00 00 00            lea eax, [rdx*4 + 0x30]
0050AAC8  BA 02 00 00 00                  mov edx, 2
0050AACD  48 03 F0                        add rsi, rax
0050AAD0  4D 2B D3                        sub r10, r11
0050AAD3  0F 85 20 FF FF FF               jne 0x14050a9f9
0050AAD9  48 8B 5D 68                     mov rbx, qword ptr [rbp + 0x68]
0050AADD  8B 4D 70                        mov ecx, dword ptr [rbp + 0x70]
0050AAE0  8B C6                           mov eax, esi
0050AAE2  44 89 5C 24 48                  mov dword ptr [rsp + 0x48], r11d
0050AAE7  41 2B C0                        sub eax, r8d
0050AAEA  44 89 4C 24 4C                  mov dword ptr [rsp + 0x4c], r9d
0050AAEF  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0050AAF3  48 63 06                        movsxd rax, dword ptr [rsi]
0050AAF6  83 F8 24                        cmp eax, 0x24
0050AAF9  0F 85 98 07 00 00               jne 0x14050b297
0050AAFF  4C 8B 5E 08                     mov r11, qword ptr [rsi + 8]
0050AB03  44 8B 46 10                     mov r8d, dword ptr [rsi + 0x10]
0050AB07  4D 8B CB                        mov r9, r11
0050AB0A  44 01 83 48 08 00 00            add dword ptr [rbx + 0x848], r8d
0050AB11  49 8B C3                        mov rax, r11
0050AB14  44 8B B3 34 08 00 00            mov r14d, dword ptr [rbx + 0x834]
0050AB1B  4C 8B BB 38 08 00 00            mov r15, qword ptr [rbx + 0x838]
0050AB22  4B 8D 0C 03                     lea rcx, [r11 + r8]
0050AB26  4C 3B D9                        cmp r11, rcx
0050AB29  73 0C                           jae 0x14050ab37
0050AB2B  0F 18 00                        prefetchnta byte ptr [rax]
0050AB2E  48 83 C0 40                     add rax, 0x40
0050AB32  48 3B C1                        cmp rax, rcx
0050AB35  72 F4                           jb 0x14050ab2b
0050AB37  45 8B D0                        mov r10d, r8d
0050AB3A  49 8B FF                        mov rdi, r15
0050AB3D  41 C1 EA 07                     shr r10d, 7
0050AB41  45 85 D2                        test r10d, r10d
0050AB44  74 62                           je 0x14050aba8
0050AB46  48 BB 01 20 00 04 80 00 10 70   movabs rbx, 0x7010008004002001
0050AB50  41 BC 01 00 00 00               mov r12d, 1
0050AB56  B8 08 00 00 00                  mov eax, 8
0050AB5B  49 33 39                        xor rdi, qword ptr [r9]
0050AB5E  41 8B CE                        mov ecx, r14d
0050AB61  48 D3 C7                        rol rdi, cl
0050AB64  49 33 79 08                     xor rdi, qword ptr [r9 + 8]
0050AB68  49 83 C1 10                     add r9, 0x10
0050AB6C  48 D3 C7                        rol rdi, cl
0050AB6F  49 2B C4                        sub rax, r12
0050AB72  75 E7                           jne 0x14050ab5b
0050AB74  49 8B C9                        mov rcx, r9
0050AB77  49 2B CB                        sub rcx, r11
0050AB7A  49 33 CF                        xor rcx, r15
0050AB7D  48 8B C1                        mov rax, rcx
0050AB80  48 C1 C0 11                     rol rax, 0x11
0050AB84  48 33 C8                        xor rcx, rax
0050AB87  48 8B C3                        mov rax, rbx
0050AB8A  48 F7 E1                        mul rcx
0050AB8D  33 C2                           xor eax, edx
0050AB8F  48 89 55 C8                     mov qword ptr [rbp - 0x38], rdx
0050AB93  44 33 F0                        xor r14d, eax
0050AB96  41 83 E6 3F                     and r14d, 0x3f
0050AB9A  45 0F 44 F4                     cmove r14d, r12d
0050AB9E  41 83 C2 FF                     add r10d, -1
0050ABA2  75 B2                           jne 0x14050ab56
0050ABA4  48 8B 5D 68                     mov rbx, qword ptr [rbp + 0x68]
0050ABA8  41 83 E0 7F                     and r8d, 0x7f
0050ABAC  41 BA 01 00 00 00               mov r10d, 1
0050ABB2  41 83 F8 08                     cmp r8d, 8
0050ABB6  72 1D                           jb 0x14050abd5
0050ABB8  41 8B C0                        mov eax, r8d
0050ABBB  48 C1 E8 03                     shr rax, 3
0050ABBF  49 33 39                        xor rdi, qword ptr [r9]
0050ABC2  41 8B CE                        mov ecx, r14d
0050ABC5  48 D3 C7                        rol rdi, cl
0050ABC8  49 83 C1 08                     add r9, 8
0050ABCC  41 83 C0 F8                     add r8d, -8
0050ABD0  49 2B C2                        sub rax, r10
0050ABD3  75 EA                           jne 0x14050abbf
0050ABD5  45 85 C0                        test r8d, r8d
0050ABD8  74 16                           je 0x14050abf0
0050ABDA  41 0F B6 01                     movzx eax, byte ptr [r9]
0050ABDE  41 8B CE                        mov ecx, r14d
0050ABE1  48 33 F8                        xor rdi, rax
0050ABE4  4D 03 CA                        add r9, r10
0050ABE7  48 D3 C7                        rol rdi, cl
0050ABEA  41 83 C0 FF                     add r8d, -1
0050ABEE  75 EA                           jne 0x14050abda
0050ABF0  48 8B C7                        mov rax, rdi
0050ABF3  EB 02                           jmp 0x14050abf7
0050ABF5  33 F8                           xor edi, eax
0050ABF7  48 C1 E8 1F                     shr rax, 0x1f
0050ABFB  48 85 C0                        test rax, rax
0050ABFE  75 F5                           jne 0x14050abf5
0050AC00  0F BA F7 1F                     btr edi, 0x1f
0050AC04  45 8B E5                        mov r12d, r13d
0050AC07  3B 7E 14                        cmp edi, dword ptr [rsi + 0x14]
0050AC0A  0F 84 0F 02 00 00               je 0x14050ae1f
0050AC10  44 39 2E                        cmp dword ptr [rsi], r13d
0050AC13  75 08                           jne 0x14050ac1d
0050AC15  44 39 6E 18                     cmp dword ptr [rsi + 0x18], r13d
0050AC19  45 0F 45 E2                     cmovne r12d, r10d
0050AC1D  8B 4E 10                        mov ecx, dword ptr [rsi + 0x10]
0050AC20  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
0050AC24  48 85 C9                        test rcx, rcx
0050AC27  0F 84 AE 00 00 00               je 0x14050acdb
0050AC2D  8B 83 DC 09 00 00               mov eax, dword ptr [rbx + 0x9dc]
0050AC33  A8 40                           test al, 0x40
0050AC35  0F 84 A0 00 00 00               je 0x14050acdb
0050AC3B  45 0F 20 C5                     mov r13, cr8
0050AC3F  B8 02 00 00 00                  mov eax, 2
0050AC44  44 0F 22 C0                     mov cr8, rax
0050AC48  4C 8B FA                        mov r15, rdx
0050AC4B  48 8D 41 FF                     lea rax, [rcx - 1]
0050AC4F  49 81 E7 00 F0 FF FF            and r15, 0xfffffffffffff000
0050AC56  48 03 C2                        add rax, rdx
0050AC59  48 0D FF 0F 00 00               or rax, 0xfff
0050AC5F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0050AC64  49 8D 47 FF                     lea rax, [r15 - 1]
0050AC68  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
0050AC6C  45 0F B6 F5                     movzx r14d, r13b
0050AC70  48 8B 83 68 04 00 00            mov rax, qword ptr [rbx + 0x468]
0050AC77  33 D2                           xor edx, edx
0050AC79  49 8B CF                        mov rcx, r15
0050AC7C  E8 DF FD 6D 00                  call 0x140beaa60
0050AC81  3D 2D 02 00 C0                  cmp eax, 0xc000022d
0050AC86  75 25                           jne 0x14050acad
0050AC88  45 85 E4                        test r12d, r12d
0050AC8B  75 47                           jne 0x14050acd4
0050AC8D  41 80 FD 01                     cmp r13b, 1
0050AC91  77 1E                           ja 0x14050acb1
0050AC93  45 0F B6 F5                     movzx r14d, r13b
0050AC97  45 0F 22 C6                     mov cr8, r14
0050AC9B  41 8A 07                        mov al, byte ptr [r15]
0050AC9E  44 0F 20 C0                     mov rax, cr8
0050ACA2  41 8D 44 24 02                  lea eax, [r12 + 2]
0050ACA7  44 0F 22 C0                     mov cr8, rax
0050ACAB  EB C3                           jmp 0x14050ac70
0050ACAD  85 C0                           test eax, eax
0050ACAF  78 23                           js 0x14050acd4
0050ACB1  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
0050ACB5  B9 00 10 00 00                  mov ecx, 0x1000
0050ACBA  48 03 C1                        add rax, rcx
0050ACBD  4C 03 F9                        add r15, rcx
0050ACC0  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
0050ACC4  48 3B 44 24 58                  cmp rax, qword ptr [rsp + 0x58]
0050ACC9  75 A1                           jne 0x14050ac6c
0050ACCB  45 0F 22 C6                     mov cr8, r14
0050ACCF  E9 4B 01 00 00                  jmp 0x14050ae1f
0050ACD4  45 33 ED                        xor r13d, r13d
0050ACD7  45 0F 22 C6                     mov cr8, r14
0050ACDB  4C 8B CB                        mov r9, rbx
0050ACDE  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
0050ACE1  41 BA DC 09 00 00               mov r10d, 0x9dc
0050ACE7  44 39 AB 18 09 00 00            cmp dword ptr [rbx + 0x918], r13d
0050ACEE  75 12                           jne 0x14050ad02
0050ACF0  8B C8                           mov ecx, eax
0050ACF2  8B C7                           mov eax, edi
0050ACF4  48 33 C8                        xor rcx, rax
0050ACF7  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050ACFE  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0050AD02  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0050AD06  44 39 AB 18 09 00 00            cmp dword ptr [rbx + 0x918], r13d
0050AD0D  0F 85 0C 01 00 00               jne 0x14050ae1f
0050AD13  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0050AD1D  BA 01 00 00 00                  mov edx, 1
0050AD22  48 03 C3                        add rax, rbx
0050AD25  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0050AD2C  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
0050AD36  48 03 C6                        add rax, rsi
0050AD39  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0050AD40  48 63 06                        movsxd rax, dword ptr [rsi]
0050AD43  48 89 8B 38 09 00 00            mov qword ptr [rbx + 0x938], rcx
0050AD4A  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0050AD50  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0050AD57  89 93 18 09 00 00               mov dword ptr [rbx + 0x918], edx
0050AD5D  0F BA E1 1D                     bt ecx, 0x1d
0050AD61  0F 82 B8 00 00 00               jb 0x14050ae1f
0050AD67  43 F7 04 0A 00 00 20 00         test dword ptr [r10 + r9], 0x200000
0050AD6F  0F 84 AA 00 00 00               je 0x14050ae1f
0050AD75  84 CA                           test dl, cl
0050AD77  0F 84 A2 00 00 00               je 0x14050ae1f
0050AD7D  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0050AD83  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0050AD89  48 8B BB 38 08 00 00            mov rdi, qword ptr [rbx + 0x838]
0050AD90  2B C1                           sub eax, ecx
0050AD92  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0050AD99  48 8D 14 19                     lea rdx, [rcx + rbx]
0050AD9D  8B C8                           mov ecx, eax
0050AD9F  48 C1 E9 03                     shr rcx, 3
0050ADA3  4C 8D 1C CA                     lea r11, [rdx + rcx*8]
0050ADA7  EB 21                           jmp 0x14050adca
0050ADA9  4C 31 02                        xor qword ptr [rdx], r8
0050ADAC  48 8B 02                        mov rax, qword ptr [rdx]
0050ADAF  41 0F B6 C8                     movzx ecx, r8b
0050ADB3  48 33 C7                        xor rax, rdi
0050ADB6  83 E1 3F                        and ecx, 0x3f
0050ADB9  49 D3 C8                        ror r8, cl
0050ADBC  4C 03 C0                        add r8, rax
0050ADBF  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0050ADC6  48 83 C2 08                     add rdx, 8
0050ADCA  49 3B D3                        cmp rdx, r11
0050ADCD  75 DA                           jne 0x14050ada9
0050ADCF  43 0F BA 34 0A 15               btr dword ptr [r10 + r9], 0x15
0050ADD5  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0050ADDC  74 41                           je 0x14050ae1f
0050ADDE  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0050ADE4  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050ADEB  48 89 18                        mov qword ptr [rax], rbx
0050ADEE  89 48 10                        mov dword ptr [rax + 0x10], ecx
0050ADF1  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0050ADF8  44 39 AB 18 09 00 00            cmp dword ptr [rbx + 0x918], r13d
0050ADFF  75 0E                           jne 0x14050ae0f
0050AE01  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050AE08  49 33 C8                        xor rcx, r8
0050AE0B  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0050AE0F  33 D2                           xor edx, edx
0050AE11  41 B9 00 01 00 00               mov r9d, 0x100
0050AE17  48 8B CB                        mov rcx, rbx
0050AE1A  E8 65 D5 6D 00                  call 0x140be8384
0050AE1F  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
0050AE26  45 0F 20 C6                     mov r14, cr8
0050AE2A  B8 0F 00 00 00                  mov eax, 0xf
0050AE2F  44 0F 22 C0                     mov cr8, rax
0050AE33  48 8B 83 60 01 00 00            mov rax, qword ptr [rbx + 0x160]
0050AE3A  E8 21 FC 6D 00                  call 0x140beaa60
0050AE3F  48 8B 83 20 06 00 00            mov rax, qword ptr [rbx + 0x620]
0050AE46  48 8B 08                        mov rcx, qword ptr [rax]
0050AE49  8B 01                           mov eax, dword ptr [rcx]
0050AE4B  48 8D 79 10                     lea rdi, [rcx + 0x10]
0050AE4F  44 8A 79 0C                     mov r15b, byte ptr [rcx + 0xc]
0050AE53  48 8D 0C 40                     lea rcx, [rax + rax*2]
0050AE57  4C 8D 2C CF                     lea r13, [rdi + rcx*8]
0050AE5B  BA 18 00 00 00                  mov edx, 0x18
0050AE60  4C 8D 46 18                     lea r8, [rsi + 0x18]
0050AE64  4C 8B CF                        mov r9, rdi
0050AE67  49 8B 09                        mov rcx, qword ptr [r9]
0050AE6A  49 83 C1 08                     add r9, 8
0050AE6E  49 8B 00                        mov rax, qword ptr [r8]
0050AE71  49 83 C0 08                     add r8, 8
0050AE75  48 3B C8                        cmp rcx, rax
0050AE78  75 29                           jne 0x14050aea3
0050AE7A  83 C2 F8                        add edx, -8
0050AE7D  83 FA 08                        cmp edx, 8
0050AE80  73 E5                           jae 0x14050ae67
0050AE82  85 D2                           test edx, edx
0050AE84  74 26                           je 0x14050aeac
0050AE86  41 BA 01 00 00 00               mov r10d, 1
0050AE8C  41 8A 09                        mov cl, byte ptr [r9]
0050AE8F  4D 03 CA                        add r9, r10
0050AE92  41 8A 00                        mov al, byte ptr [r8]
0050AE95  4D 03 C2                        add r8, r10
0050AE98  3A C8                           cmp cl, al
0050AE9A  75 07                           jne 0x14050aea3
0050AE9C  83 C2 FF                        add edx, -1
0050AE9F  75 EB                           jne 0x14050ae8c
0050AEA1  EB 09                           jmp 0x14050aeac
0050AEA3  48 83 C7 18                     add rdi, 0x18
0050AEA7  49 3B FD                        cmp rdi, r13
0050AEAA  72 AF                           jb 0x14050ae5b
0050AEAC  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
0050AEB3  48 8B 83 A0 01 00 00            mov rax, qword ptr [rbx + 0x1a0]
0050AEBA  E8 A1 FB 6D 00                  call 0x140beaa60
0050AEBF  41 0F B6 C6                     movzx eax, r14b
0050AEC3  44 0F 22 C0                     mov cr8, rax
0050AEC7  41 BE 01 00 00 00               mov r14d, 1
0050AECD  45 84 FF                        test r15b, r15b
0050AED0  0F 84 2D 01 00 00               je 0x14050b003
0050AED6  8B 8B DC 09 00 00               mov ecx, dword ptr [rbx + 0x9dc]
0050AEDC  F6 C1 10                        test cl, 0x10
0050AEDF  0F 84 14 01 00 00               je 0x14050aff9
0050AEE5  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0050AEEC  0F 85 07 01 00 00               jne 0x14050aff9
0050AEF2  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0050AEFC  48 03 C3                        add rax, rbx
0050AEFF  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0050AF06  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
0050AF10  48 03 C6                        add rax, rsi
0050AF13  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0050AF1A  48 63 06                        movsxd rax, dword ptr [rsi]
0050AF1D  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0050AF24  8B 83 D8 09 00 00               mov eax, dword ptr [rbx + 0x9d8]
0050AF2A  4C 89 B3 38 09 00 00            mov qword ptr [rbx + 0x938], r14
0050AF31  44 89 B3 18 09 00 00            mov dword ptr [rbx + 0x918], r14d
0050AF38  0F BA E0 1D                     bt eax, 0x1d
0050AF3C  0F 82 B7 00 00 00               jb 0x14050aff9
0050AF42  0F BA E1 15                     bt ecx, 0x15
0050AF46  0F 83 AD 00 00 00               jae 0x14050aff9
0050AF4C  41 84 C6                        test r14b, al
0050AF4F  0F 84 A4 00 00 00               je 0x14050aff9
0050AF55  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0050AF5B  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0050AF61  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
0050AF68  2B C1                           sub eax, ecx
0050AF6A  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0050AF71  48 8D 14 19                     lea rdx, [rcx + rbx]
0050AF75  8B C8                           mov ecx, eax
0050AF77  48 C1 E9 03                     shr rcx, 3
0050AF7B  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
0050AF7F  EB 21                           jmp 0x14050afa2
0050AF81  4C 31 02                        xor qword ptr [rdx], r8
0050AF84  48 8B 02                        mov rax, qword ptr [rdx]
0050AF87  41 0F B6 C8                     movzx ecx, r8b
0050AF8B  49 33 C2                        xor rax, r10
0050AF8E  83 E1 3F                        and ecx, 0x3f
0050AF91  49 D3 C8                        ror r8, cl
0050AF94  4C 03 C0                        add r8, rax
0050AF97  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0050AF9E  48 83 C2 08                     add rdx, 8
0050AFA2  49 3B D1                        cmp rdx, r9
0050AFA5  75 DA                           jne 0x14050af81
0050AFA7  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
0050AFAF  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0050AFB6  74 41                           je 0x14050aff9
0050AFB8  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0050AFBE  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050AFC5  48 89 18                        mov qword ptr [rax], rbx
0050AFC8  89 48 10                        mov dword ptr [rax + 0x10], ecx
0050AFCB  83 BB 18 09 00 00 00            cmp dword ptr [rbx + 0x918], 0
0050AFD2  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0050AFD9  75 0E                           jne 0x14050afe9
0050AFDB  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050AFE2  49 33 C8                        xor rcx, r8
0050AFE5  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0050AFE9  33 D2                           xor edx, edx
0050AFEB  41 B9 00 01 00 00               mov r9d, 0x100
0050AFF1  48 8B CB                        mov rcx, rbx
0050AFF4  E8 8B D3 6D 00                  call 0x140be8384
0050AFF9  4C 39 76 18                     cmp qword ptr [rsi + 0x18], r14
0050AFFD  0F 84 29 01 00 00               je 0x14050b12c
0050B003  49 BC 15 34 45 E4 DE 4B B7 B3   movabs r12, 0xb3b74bdee4453415
0050B00D  49 3B FD                        cmp rdi, r13
0050B010  0F 85 20 01 00 00               jne 0x14050b136
0050B016  45 33 ED                        xor r13d, r13d
0050B019  44 39 AB 18 09 00 00            cmp dword ptr [rbx + 0x918], r13d
0050B020  0F 85 13 01 00 00               jne 0x14050b139
0050B026  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0050B02C  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0050B036  48 03 C3                        add rax, rbx
0050B039  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0050B040  4A 8D 04 26                     lea rax, [rsi + r12]
0050B044  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0050B04B  48 63 06                        movsxd rax, dword ptr [rsi]
0050B04E  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0050B055  48 89 BB 38 09 00 00            mov qword ptr [rbx + 0x938], rdi
0050B05C  44 89 B3 18 09 00 00            mov dword ptr [rbx + 0x918], r14d
0050B063  0F BA E1 1D                     bt ecx, 0x1d
0050B067  0F 82 CC 00 00 00               jb 0x14050b139
0050B06D  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
0050B077  0F 84 BC 00 00 00               je 0x14050b139
0050B07D  41 84 CE                        test r14b, cl
0050B080  0F 84 B3 00 00 00               je 0x14050b139
0050B086  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0050B08C  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0050B092  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
0050B099  2B C1                           sub eax, ecx
0050B09B  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0050B0A2  48 8D 14 19                     lea rdx, [rcx + rbx]
0050B0A6  8B C8                           mov ecx, eax
0050B0A8  48 C1 E9 03                     shr rcx, 3
0050B0AC  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
0050B0B0  EB 21                           jmp 0x14050b0d3
0050B0B2  4C 31 02                        xor qword ptr [rdx], r8
0050B0B5  48 8B 02                        mov rax, qword ptr [rdx]
0050B0B8  41 0F B6 C8                     movzx ecx, r8b
0050B0BC  49 33 C2                        xor rax, r10
0050B0BF  83 E1 3F                        and ecx, 0x3f
0050B0C2  49 D3 C8                        ror r8, cl
0050B0C5  4C 03 C0                        add r8, rax
0050B0C8  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0050B0CF  48 83 C2 08                     add rdx, 8
0050B0D3  49 3B D1                        cmp rdx, r9
0050B0D6  75 DA                           jne 0x14050b0b2
0050B0D8  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
0050B0E0  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0050B0E7  74 50                           je 0x14050b139
0050B0E9  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0050B0EF  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050B0F6  48 89 18                        mov qword ptr [rax], rbx
0050B0F9  89 48 10                        mov dword ptr [rax + 0x10], ecx
0050B0FC  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0050B103  44 39 AB 18 09 00 00            cmp dword ptr [rbx + 0x918], r13d
0050B10A  75 0E                           jne 0x14050b11a
0050B10C  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050B113  49 33 C8                        xor rcx, r8
0050B116  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0050B11A  33 D2                           xor edx, edx
0050B11C  41 B9 00 01 00 00               mov r9d, 0x100
0050B122  48 8B CB                        mov rcx, rbx
0050B125  E8 5A D2 6D 00                  call 0x140be8384
0050B12A  EB 0D                           jmp 0x14050b139
0050B12C  49 BC 15 34 45 E4 DE 4B B7 B3   movabs r12, 0xb3b74bdee4453415
0050B136  45 33 ED                        xor r13d, r13d
0050B139  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
0050B140  45 0F 20 C7                     mov r15, cr8
0050B144  B8 0F 00 00 00                  mov eax, 0xf
0050B149  44 0F 22 C0                     mov cr8, rax
0050B14D  48 8B 83 60 01 00 00            mov rax, qword ptr [rbx + 0x160]
0050B154  E8 07 F9 6D 00                  call 0x140beaa60
0050B159  48 8B 83 20 06 00 00            mov rax, qword ptr [rbx + 0x620]
0050B160  49 8B D5                        mov rdx, r13
0050B163  48 8B 08                        mov rcx, qword ptr [rax]
0050B166  8B 01                           mov eax, dword ptr [rcx]
0050B168  48 8D 79 10                     lea rdi, [rcx + 0x10]
0050B16C  48 8D 0C 40                     lea rcx, [rax + rax*2]
0050B170  4C 8D 34 CF                     lea r14, [rdi + rcx*8]
0050B174  EB 2A                           jmp 0x14050b1a0
0050B176  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0050B17A  48 3B CA                        cmp rcx, rdx
0050B17D  72 2A                           jb 0x14050b1a9
0050B17F  48 8B C1                        mov rax, rcx
0050B182  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0050B188  48 3B C1                        cmp rax, rcx
0050B18B  75 1C                           jne 0x14050b1a9
0050B18D  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0050B190  48 03 C1                        add rax, rcx
0050B193  48 3B C1                        cmp rax, rcx
0050B196  76 11                           jbe 0x14050b1a9
0050B198  48 3B C2                        cmp rax, rdx
0050B19B  74 0C                           je 0x14050b1a9
0050B19D  48 8B D0                        mov rdx, rax
0050B1A0  48 83 C7 18                     add rdi, 0x18
0050B1A4  49 3B FE                        cmp rdi, r14
0050B1A7  72 CD                           jb 0x14050b176
0050B1A9  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
0050B1B0  48 8B 83 A0 01 00 00            mov rax, qword ptr [rbx + 0x1a0]
0050B1B7  E8 A4 F8 6D 00                  call 0x140beaa60
0050B1BC  41 0F B6 C7                     movzx eax, r15b
0050B1C0  44 0F 22 C0                     mov cr8, rax
0050B1C4  49 3B FE                        cmp rdi, r14
0050B1C7  0F 84 F1 03 00 00               je 0x14050b5be
0050B1CD  44 39 AB 18 09 00 00            cmp dword ptr [rbx + 0x918], r13d
0050B1D4  0F 85 E4 03 00 00               jne 0x14050b5be
0050B1DA  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0050B1E0  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0050B1EA  48 03 C3                        add rax, rbx
0050B1ED  41 BE 01 00 00 00               mov r14d, 1
0050B1F3  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0050B1FA  4A 8D 04 26                     lea rax, [rsi + r12]
0050B1FE  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0050B205  48 63 06                        movsxd rax, dword ptr [rsi]
0050B208  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0050B20F  48 89 BB 38 09 00 00            mov qword ptr [rbx + 0x938], rdi
0050B216  44 89 B3 18 09 00 00            mov dword ptr [rbx + 0x918], r14d
0050B21D  0F BA E1 1D                     bt ecx, 0x1d
0050B221  0F 82 97 03 00 00               jb 0x14050b5be
0050B227  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
0050B231  0F 84 87 03 00 00               je 0x14050b5be
0050B237  41 84 CE                        test r14b, cl
0050B23A  0F 84 7E 03 00 00               je 0x14050b5be
0050B240  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0050B246  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0050B24C  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
0050B253  2B C1                           sub eax, ecx
0050B255  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0050B25C  48 8D 14 19                     lea rdx, [rcx + rbx]
0050B260  8B C8                           mov ecx, eax
0050B262  48 C1 E9 03                     shr rcx, 3
0050B266  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
0050B26A  EB 21                           jmp 0x14050b28d
0050B26C  4C 31 02                        xor qword ptr [rdx], r8
0050B26F  48 8B 02                        mov rax, qword ptr [rdx]
0050B272  41 0F B6 C8                     movzx ecx, r8b
0050B276  49 33 C2                        xor rax, r10
0050B279  83 E1 3F                        and ecx, 0x3f
0050B27C  49 D3 C8                        ror r8, cl
0050B27F  4C 03 C0                        add r8, rax
0050B282  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0050B289  48 83 C2 08                     add rdx, 8
0050B28D  49 3B D1                        cmp rdx, r9
0050B290  75 DA                           jne 0x14050b26c
0050B292  E9 D5 02 00 00                  jmp 0x14050b56c
0050B297  83 F8 2B                        cmp eax, 0x2b
0050B29A  0F 87 2B 03 00 00               ja 0x14050b5cb
0050B2A0  48 BA 02 00 00 00 02 08 00 00   movabs rdx, 0x80200000002
0050B2AA  48 0F A3 C2                     bt rdx, rax
0050B2AE  0F 83 17 03 00 00               jae 0x14050b5cb
0050B2B4  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
0050B2BB  45 0F 20 C6                     mov r14, cr8
0050B2BF  B8 0F 00 00 00                  mov eax, 0xf
0050B2C4  44 0F 22 C0                     mov cr8, rax
0050B2C8  48 8B 83 60 01 00 00            mov rax, qword ptr [rbx + 0x160]
0050B2CF  E8 8C F7 6D 00                  call 0x140beaa60
0050B2D4  48 8B 83 20 06 00 00            mov rax, qword ptr [rbx + 0x620]
0050B2DB  48 8B 08                        mov rcx, qword ptr [rax]
0050B2DE  8B 01                           mov eax, dword ptr [rcx]
0050B2E0  48 8D 79 10                     lea rdi, [rcx + 0x10]
0050B2E4  44 8A 79 0C                     mov r15b, byte ptr [rcx + 0xc]
0050B2E8  48 8D 0C 40                     lea rcx, [rax + rax*2]
0050B2EC  4C 8D 24 CF                     lea r12, [rdi + rcx*8]
0050B2F0  BA 18 00 00 00                  mov edx, 0x18
0050B2F5  4C 8D 46 18                     lea r8, [rsi + 0x18]
0050B2F9  4C 8B CF                        mov r9, rdi
0050B2FC  49 8B 09                        mov rcx, qword ptr [r9]
0050B2FF  49 83 C1 08                     add r9, 8
0050B303  49 8B 00                        mov rax, qword ptr [r8]
0050B306  49 83 C0 08                     add r8, 8
0050B30A  48 3B C8                        cmp rcx, rax
0050B30D  75 29                           jne 0x14050b338
0050B30F  83 C2 F8                        add edx, -8
0050B312  83 FA 08                        cmp edx, 8
0050B315  73 E5                           jae 0x14050b2fc
0050B317  85 D2                           test edx, edx
0050B319  74 26                           je 0x14050b341
0050B31B  41 BB 01 00 00 00               mov r11d, 1
0050B321  41 8A 09                        mov cl, byte ptr [r9]
0050B324  4D 03 CB                        add r9, r11
0050B327  41 8A 00                        mov al, byte ptr [r8]
0050B32A  4D 03 C3                        add r8, r11
0050B32D  3A C8                           cmp cl, al
0050B32F  75 07                           jne 0x14050b338
0050B331  83 C2 FF                        add edx, -1
0050B334  75 EB                           jne 0x14050b321
0050B336  EB 09                           jmp 0x14050b341
0050B338  48 83 C7 18                     add rdi, 0x18
0050B33C  49 3B FC                        cmp rdi, r12
0050B33F  72 AF                           jb 0x14050b2f0
0050B341  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
0050B348  48 8B 83 A0 01 00 00            mov rax, qword ptr [rbx + 0x1a0]
0050B34F  E8 0C F7 6D 00                  call 0x140beaa60
0050B354  41 0F B6 C6                     movzx eax, r14b
0050B358  44 0F 22 C0                     mov cr8, rax
0050B35C  41 BE 01 00 00 00               mov r14d, 1
0050B362  45 84 FF                        test r15b, r15b
0050B365  0F 84 30 01 00 00               je 0x14050b49b
0050B36B  8B 8B DC 09 00 00               mov ecx, dword ptr [rbx + 0x9dc]
0050B371  F6 C1 10                        test cl, 0x10
0050B374  0F 84 17 01 00 00               je 0x14050b491
0050B37A  44 39 AB 18 09 00 00            cmp dword ptr [rbx + 0x918], r13d
0050B381  0F 85 0A 01 00 00               jne 0x14050b491
0050B387  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0050B391  48 03 C3                        add rax, rbx
0050B394  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0050B39B  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
0050B3A5  48 03 C6                        add rax, rsi
0050B3A8  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0050B3AF  48 63 06                        movsxd rax, dword ptr [rsi]
0050B3B2  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0050B3B9  8B 83 D8 09 00 00               mov eax, dword ptr [rbx + 0x9d8]
0050B3BF  4C 89 B3 38 09 00 00            mov qword ptr [rbx + 0x938], r14
0050B3C6  44 89 B3 18 09 00 00            mov dword ptr [rbx + 0x918], r14d
0050B3CD  0F BA E0 1D                     bt eax, 0x1d
0050B3D1  0F 82 BA 00 00 00               jb 0x14050b491
0050B3D7  0F BA E1 15                     bt ecx, 0x15
0050B3DB  0F 83 B0 00 00 00               jae 0x14050b491
0050B3E1  41 84 C6                        test r14b, al
0050B3E4  0F 84 A7 00 00 00               je 0x14050b491
0050B3EA  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0050B3F0  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0050B3F6  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
0050B3FD  2B C1                           sub eax, ecx
0050B3FF  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0050B406  48 8D 14 19                     lea rdx, [rcx + rbx]
0050B40A  8B C8                           mov ecx, eax
0050B40C  48 C1 E9 03                     shr rcx, 3
0050B410  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
0050B414  EB 21                           jmp 0x14050b437
0050B416  4C 31 02                        xor qword ptr [rdx], r8
0050B419  48 8B 02                        mov rax, qword ptr [rdx]
0050B41C  41 0F B6 C8                     movzx ecx, r8b
0050B420  49 33 C2                        xor rax, r10
0050B423  83 E1 3F                        and ecx, 0x3f
0050B426  49 D3 C8                        ror r8, cl
0050B429  4C 03 C0                        add r8, rax
0050B42C  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0050B433  48 83 C2 08                     add rdx, 8
0050B437  49 3B D1                        cmp rdx, r9
0050B43A  75 DA                           jne 0x14050b416
0050B43C  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
0050B444  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0050B44B  74 44                           je 0x14050b491
0050B44D  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050B454  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0050B45A  48 89 18                        mov qword ptr [rax], rbx
0050B45D  89 48 10                        mov dword ptr [rax + 0x10], ecx
0050B460  48 8B 83 80 0A 00 00            mov rax, qword ptr [rbx + 0xa80]
0050B467  44 39 AB 18 09 00 00            cmp dword ptr [rbx + 0x918], r13d
0050B46E  75 11                           jne 0x14050b481
0050B470  49 8B C8                        mov rcx, r8
0050B473  48 33 C8                        xor rcx, rax
0050B476  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050B47D  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0050B481  33 D2                           xor edx, edx
0050B483  41 B9 00 01 00 00               mov r9d, 0x100
0050B489  48 8B CB                        mov rcx, rbx
0050B48C  E8 F3 CE 6D 00                  call 0x140be8384
0050B491  4C 39 76 18                     cmp qword ptr [rsi + 0x18], r14
0050B495  0F 84 23 01 00 00               je 0x14050b5be
0050B49B  49 3B FC                        cmp rdi, r12
0050B49E  0F 85 1A 01 00 00               jne 0x14050b5be
0050B4A4  44 39 AB 18 09 00 00            cmp dword ptr [rbx + 0x918], r13d
0050B4AB  0F 85 0D 01 00 00               jne 0x14050b5be
0050B4B1  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
0050B4B7  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
0050B4C1  48 03 C3                        add rax, rbx
0050B4C4  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
0050B4CB  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
0050B4D5  48 03 C6                        add rax, rsi
0050B4D8  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
0050B4DF  48 63 06                        movsxd rax, dword ptr [rsi]
0050B4E2  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
0050B4E9  48 89 BB 38 09 00 00            mov qword ptr [rbx + 0x938], rdi
0050B4F0  44 89 B3 18 09 00 00            mov dword ptr [rbx + 0x918], r14d
0050B4F7  0F BA E1 1D                     bt ecx, 0x1d
0050B4FB  0F 82 BD 00 00 00               jb 0x14050b5be
0050B501  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
0050B50B  0F 84 AD 00 00 00               je 0x14050b5be
0050B511  41 84 CE                        test r14b, cl
0050B514  0F 84 A4 00 00 00               je 0x14050b5be
0050B51A  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
0050B520  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
0050B526  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
0050B52D  2B C1                           sub eax, ecx
0050B52F  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
0050B536  48 8D 14 19                     lea rdx, [rcx + rbx]
0050B53A  8B C8                           mov ecx, eax
0050B53C  48 C1 E9 03                     shr rcx, 3
0050B540  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
0050B544  EB 21                           jmp 0x14050b567
0050B546  4C 31 02                        xor qword ptr [rdx], r8
0050B549  48 8B 02                        mov rax, qword ptr [rdx]
0050B54C  41 0F B6 C8                     movzx ecx, r8b
0050B550  49 33 C2                        xor rax, r10
0050B553  83 E1 3F                        and ecx, 0x3f
0050B556  49 D3 C8                        ror r8, cl
0050B559  4C 03 C0                        add r8, rax
0050B55C  49 81 F0 FA 0E 00 00            xor r8, 0xefa
0050B563  48 83 C2 08                     add rdx, 8
0050B567  49 3B D1                        cmp rdx, r9
0050B56A  75 DA                           jne 0x14050b546
0050B56C  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
0050B574  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
0050B57B  74 41                           je 0x14050b5be
0050B57D  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
0050B583  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050B58A  48 89 18                        mov qword ptr [rax], rbx
0050B58D  89 48 10                        mov dword ptr [rax + 0x10], ecx
0050B590  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
0050B597  44 39 AB 18 09 00 00            cmp dword ptr [rbx + 0x918], r13d
0050B59E  75 0E                           jne 0x14050b5ae
0050B5A0  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
0050B5A7  49 33 C8                        xor rcx, r8
0050B5AA  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0050B5AE  41 B9 00 01 00 00               mov r9d, 0x100
0050B5B4  33 D2                           xor edx, edx
0050B5B6  48 8B CB                        mov rcx, rbx
0050B5B9  E8 C6 CD 6D 00                  call 0x140be8384
0050B5BE  8B 4D 70                        mov ecx, dword ptr [rbp + 0x70]
0050B5C1  41 BE 30 00 00 00               mov r14d, 0x30
0050B5C7  45 8D 7E D6                     lea r15d, [r14 - 0x2a]
0050B5CB  FF C1                           inc ecx
0050B5CD  BA 02 00 00 00                  mov edx, 2
0050B5D2  89 4D 70                        mov dword ptr [rbp + 0x70], ecx
0050B5D5  44 8D 5A FF                     lea r11d, [rdx - 1]
0050B5D9  3B 8B 2C 08 00 00               cmp ecx, dword ptr [rbx + 0x82c]
0050B5DF  0F 82 C1 F3 FF FF               jb 0x14050a9a6
0050B5E5  45 33 D2                        xor r10d, r10d
0050B5E8  44 39 93 18 09 00 00            cmp dword ptr [rbx + 0x918], r10d
0050B5EF  0F 84 AC 04 00 00               je 0x14050baa1
0050B5F5  48 8B BB 30 09 00 00            mov rdi, qword ptr [rbx + 0x930]
0050B5FC  48 8B B3 38 09 00 00            mov rsi, qword ptr [rbx + 0x938]
0050B603  4C 8B B3 28 09 00 00            mov r14, qword ptr [rbx + 0x928]
0050B60A  4C 8B BB 20 09 00 00            mov r15, qword ptr [rbx + 0x920]
0050B611  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
0050B615  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
0050B619  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
0050B61E  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
0050B623  44 0F 20 C0                     mov rax, cr8
0050B627  3A C2                           cmp al, dl
0050B629  73 08                           jae 0x14050b633
0050B62B  44 0F 20 C0                     mov rax, cr8
0050B62F  44 0F 22 C2                     mov cr8, rdx
0050B633  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
0050B63C  48 8B 83 40 06 00 00            mov rax, qword ptr [rbx + 0x640]
0050B643  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0050B64C  4D 8B 0C 00                     mov r9, qword ptr [r8 + rax]
0050B650  48 8B 83 48 06 00 00            mov rax, qword ptr [rbx + 0x648]
0050B657  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
0050B65C  4A 8B 14 00                     mov rdx, qword ptr [rax + r8]
0050B660  48 8B 83 58 06 00 00            mov rax, qword ptr [rbx + 0x658]
0050B667  48 03 93 88 07 00 00            add rdx, qword ptr [rbx + 0x788]
0050B66E  4C 8B 1C 01                     mov r11, qword ptr [rcx + rax]
0050B672  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0050B677  4C 89 5D 88                     mov qword ptr [rbp - 0x78], r11
0050B67B  49 3B C1                        cmp rax, r9
0050B67E  77 16                           ja 0x14050b696
0050B680  8B 83 FC 05 00 00               mov eax, dword ptr [rbx + 0x5fc]
0050B686  49 8B C9                        mov rcx, r9
0050B689  48 2B C8                        sub rcx, rax
0050B68C  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0050B691  48 3B C1                        cmp rax, rcx
0050B694  73 44                           jae 0x14050b6da
0050B696  48 8B 83 50 06 00 00            mov rax, qword ptr [rbx + 0x650]
0050B69D  45 38 14 00                     cmp byte ptr [r8 + rax], r10b
0050B6A1  74 27                           je 0x14050b6ca
0050B6A3  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0050B6A8  48 3B C2                        cmp rax, rdx
0050B6AB  77 1D                           ja 0x14050b6ca
0050B6AD  8B 83 F8 05 00 00               mov eax, dword ptr [rbx + 0x5f8]
0050B6B3  48 8B CA                        mov rcx, rdx
0050B6B6  48 2B C8                        sub rcx, rax
0050B6B9  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0050B6BE  48 3B C1                        cmp rax, rcx
0050B6C1  72 07                           jb 0x14050b6ca
0050B6C3  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
0050B6C8  EB 10                           jmp 0x14050b6da
0050B6CA  48 8B 83 88 06 00 00            mov rax, qword ptr [rbx + 0x688]
0050B6D1  49 8B 04 03                     mov rax, qword ptr [r11 + rax]
0050B6D5  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0050B6DA  F7 83 D8 09 00 00 00 00 00 04   test dword ptr [rbx + 0x9d8], 0x4000000
0050B6E4  0F 85 58 05 00 00               jne 0x14050bc42
0050B6EA  F7 83 DC 09 00 00 00 00 40 00   test dword ptr [rbx + 0x9dc], 0x400000
0050B6F4  4C 89 55 80                     mov qword ptr [rbp - 0x80], r10
0050B6F8  75 12                           jne 0x14050b70c
0050B6FA  0F 20 C1                        mov rcx, cr0
0050B6FD  48 8B C1                        mov rax, rcx
0050B700  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
0050B704  48 0F BA F0 10                  btr rax, 0x10
0050B709  0F 22 C0                        mov cr0, rax
0050B70C  44 8B BB E8 0A 00 00            mov r15d, dword ptr [rbx + 0xae8]
0050B713  4C 8D B3 F0 0A 00 00            lea r14, [rbx + 0xaf0]
0050B71A  49 C1 E7 04                     shl r15, 4
0050B71E  41 BC 80 00 00 00               mov r12d, 0x80
0050B724  4D 03 FE                        add r15, r14
0050B727  41 8B D2                        mov edx, r10d
0050B72A  4D 8B DF                        mov r11, r15
0050B72D  4C 89 7D 90                     mov qword ptr [rbp - 0x70], r15
0050B731  45 8D 6C 24 81                  lea r13d, [r12 - 0x7f]
0050B736  44 39 93 EC 0A 00 00            cmp dword ptr [rbx + 0xaec], r10d
0050B73D  76 39                           jbe 0x14050b778
0050B73F  49 8B 0B                        mov rcx, qword ptr [r11]
0050B742  49 8B 43 08                     mov rax, qword ptr [r11 + 8]
0050B746  48 89 01                        mov qword ptr [rcx], rax
0050B749  0F 20 E1                        mov rcx, cr4
0050B74C  48 F7 C1 80 00 02 00            test rcx, 0x20080
0050B753  74 0E                           je 0x14050b763
0050B755  48 8B C1                        mov rax, rcx
0050B758  49 33 C4                        xor rax, r12
0050B75B  0F 22 E0                        mov cr4, rax
0050B75E  0F 22 E1                        mov cr4, rcx
0050B761  EB 06                           jmp 0x14050b769
0050B763  0F 20 D8                        mov rax, cr3
0050B766  0F 22 D8                        mov cr3, rax
0050B769  49 83 C3 10                     add r11, 0x10
0050B76D  41 03 D5                        add edx, r13d
0050B770  3B 93 EC 0A 00 00               cmp edx, dword ptr [rbx + 0xaec]
0050B776  72 C7                           jb 0x14050b73f
0050B778  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
0050B782  4D 3B F7                        cmp r14, r15
0050B785  0F 83 00 02 00 00               jae 0x14050b98b
0050B78B  F7 83 DC 09 00 00 00 00 40 00   test dword ptr [rbx + 0x9dc], 0x400000
0050B795  45 8B 66 08                     mov r12d, dword ptr [r14 + 8]
0050B799  4D 8B 06                        mov r8, qword ptr [r14]
0050B79C  44 89 65 78                     mov dword ptr [rbp + 0x78], r12d
0050B7A0  75 47                           jne 0x14050b7e9
0050B7A2  41 8B D4                        mov edx, r12d
0050B7A5  49 8B CB                        mov rcx, r11
0050B7A8  41 83 FC 08                     cmp r12d, 8
0050B7AC  72 1D                           jb 0x14050b7cb
0050B7AE  45 8B CC                        mov r9d, r12d
0050B7B1  49 C1 E9 03                     shr r9, 3
0050B7B5  48 8B 01                        mov rax, qword ptr [rcx]
0050B7B8  83 C2 F8                        add edx, -8
0050B7BB  49 89 00                        mov qword ptr [r8], rax
0050B7BE  48 83 C1 08                     add rcx, 8
0050B7C2  49 83 C0 08                     add r8, 8
0050B7C6  4D 2B CD                        sub r9, r13
0050B7C9  75 EA                           jne 0x14050b7b5
0050B7CB  85 D2                           test edx, edx
0050B7CD  0F 84 8D 01 00 00               je 0x14050b960
0050B7D3  4C 2B C1                        sub r8, rcx
0050B7D6  8A 01                           mov al, byte ptr [rcx]
0050B7D8  41 88 04 08                     mov byte ptr [r8 + rcx], al
0050B7DC  49 03 CD                        add rcx, r13
0050B7DF  83 C2 FF                        add edx, -1
0050B7E2  75 F2                           jne 0x14050b7d6
0050B7E4  E9 77 01 00 00                  jmp 0x14050b960
0050B7E9  49 8B C8                        mov rcx, r8
0050B7EC  44 89 65 70                     mov dword ptr [rbp + 0x70], r12d
0050B7F0  81 E1 FF 0F 00 00               and ecx, 0xfff
0050B7F6  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
0050B7FB  49 8D 94 24 FF 0F 00 00         lea rdx, [r12 + 0xfff]
0050B803  41 8B F4                        mov esi, r12d
0050B806  48 03 D1                        add rdx, rcx
0050B809  48 C1 EA 0C                     shr rdx, 0xc
0050B80D  85 D2                           test edx, edx
0050B80F  0F 84 4B 01 00 00               je 0x14050b960
0050B815  8B C2                           mov eax, edx
0050B817  41 BF 04 00 00 00               mov r15d, 4
0050B81D  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0050B822  4C 8B 93 D8 05 00 00            mov r10, qword ptr [rbx + 0x5d8]
0050B829  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0050B82D  49 8B C0                        mov rax, r8
0050B830  48 BF F8 FF FF FF 7F 00 00 00   movabs rdi, 0x7ffffffff8
0050B83A  48 C1 E8 09                     shr rax, 9
0050B83E  49 8B D7                        mov rdx, r15
0050B841  48 23 C7                        and rax, rdi
0050B844  45 8B CF                        mov r9d, r15d
0050B847  49 03 C2                        add rax, r10
0050B84A  48 89 01                        mov qword ptr [rcx], rax
0050B84D  48 8D 49 08                     lea rcx, [rcx + 8]
0050B851  48 C1 E8 09                     shr rax, 9
0050B855  48 23 C7                        and rax, rdi
0050B858  49 03 C2                        add rax, r10
0050B85B  49 2B D5                        sub rdx, r13
0050B85E  75 EA                           jne 0x14050b84a
0050B860  41 83 C1 FF                     add r9d, -1
0050B864  74 0F                           je 0x14050b875
0050B866  4A 8B 44 CD D0                  mov rax, qword ptr [rbp + r9*8 - 0x30]
0050B86B  8B 08                           mov ecx, dword ptr [rax]
0050B86D  C0 E9 07                        shr cl, 7
0050B870  41 84 CD                        test r13b, cl
0050B873  74 EB                           je 0x14050b860
0050B875  4E 8B 6C CD D0                  mov r13, qword ptr [rbp + r9*8 - 0x30]
0050B87A  49 8B 45 00                     mov rax, qword ptr [r13]
0050B87E  48 83 C8 62                     or rax, 0x62
0050B882  49 89 45 00                     mov qword ptr [r13], rax
0050B886  0F 20 E2                        mov rdx, cr4
0050B889  48 F7 C2 80 00 02 00            test rdx, 0x20080
0050B890  74 10                           je 0x14050b8a2
0050B892  48 8B CA                        mov rcx, rdx
0050B895  48 0F BA F9 07                  btc rcx, 7
0050B89A  0F 22 E1                        mov cr4, rcx
0050B89D  0F 22 E2                        mov cr4, rdx
0050B8A0  EB 06                           jmp 0x14050b8a8
0050B8A2  0F 20 D9                        mov rcx, cr3
0050B8A5  0F 22 D9                        mov cr3, rcx
0050B8A8  BA 00 10 00 00                  mov edx, 0x1000
0050B8AD  41 8B C8                        mov ecx, r8d
0050B8B0  81 E1 FF 0F 00 00               and ecx, 0xfff
0050B8B6  44 8B CE                        mov r9d, esi
0050B8B9  2B D1                           sub edx, ecx
0050B8BB  4D 8B D0                        mov r10, r8
0050B8BE  3B D6                           cmp edx, esi
0050B8C0  41 BC 01 00 00 00               mov r12d, 1
0050B8C6  44 0F 42 CA                     cmovb r9d, edx
0050B8CA  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0050B8CF  41 8B F9                        mov edi, r9d
0050B8D2  41 83 F9 08                     cmp r9d, 8
0050B8D6  72 20                           jb 0x14050b8f8
0050B8D8  41 8B F1                        mov esi, r9d
0050B8DB  48 C1 EE 03                     shr rsi, 3
0050B8DF  48 8B 0A                        mov rcx, qword ptr [rdx]
0050B8E2  83 C7 F8                        add edi, -8
0050B8E5  49 89 0A                        mov qword ptr [r10], rcx
0050B8E8  48 83 C2 08                     add rdx, 8
0050B8EC  49 83 C2 08                     add r10, 8
0050B8F0  49 2B F4                        sub rsi, r12
0050B8F3  75 EA                           jne 0x14050b8df
0050B8F5  8B 75 70                        mov esi, dword ptr [rbp + 0x70]
0050B8F8  85 FF                           test edi, edi
0050B8FA  74 11                           je 0x14050b90d
0050B8FC  4C 2B D2                        sub r10, rdx
0050B8FF  8A 0A                           mov cl, byte ptr [rdx]
0050B901  42 88 0C 12                     mov byte ptr [rdx + r10], cl
0050B905  49 03 D4                        add rdx, r12
0050B908  83 C7 FF                        add edi, -1
0050B90B  75 F2                           jne 0x14050b8ff
0050B90D  41 8B C9                        mov ecx, r9d
0050B910  48 01 4C 24 68                  add qword ptr [rsp + 0x68], rcx
0050B915  4C 03 C1                        add r8, rcx
0050B918  41 2B F1                        sub esi, r9d
0050B91B  49 89 45 00                     mov qword ptr [r13], rax
0050B91F  89 75 70                        mov dword ptr [rbp + 0x70], esi
0050B922  0F 20 E1                        mov rcx, cr4
0050B925  48 F7 C1 80 00 02 00            test rcx, 0x20080
0050B92C  74 10                           je 0x14050b93e
0050B92E  48 8B C1                        mov rax, rcx
0050B931  48 0F BA F8 07                  btc rax, 7
0050B936  0F 22 E0                        mov cr4, rax
0050B939  0F 22 E1                        mov cr4, rcx
0050B93C  EB 06                           jmp 0x14050b944
0050B93E  0F 20 D8                        mov rax, cr3
0050B941  0F 22 D8                        mov cr3, rax
0050B944  41 BD 01 00 00 00               mov r13d, 1
0050B94A  4C 29 6C 24 78                  sub qword ptr [rsp + 0x78], r13
0050B94F  0F 85 CD FE FF FF               jne 0x14050b822
0050B955  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0050B959  45 33 D2                        xor r10d, r10d
0050B95C  44 8B 65 78                     mov r12d, dword ptr [rbp + 0x78]
0050B960  41 8B C4                        mov eax, r12d
0050B963  49 83 C6 10                     add r14, 0x10
0050B967  4C 03 D8                        add r11, rax
0050B96A  4D 3B F7                        cmp r14, r15
0050B96D  0F 82 18 FE FF FF               jb 0x14050b78b
0050B973  48 8B 7D 98                     mov rdi, qword ptr [rbp - 0x68]
0050B977  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
0050B981  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
0050B985  41 BC 80 00 00 00               mov r12d, 0x80
0050B98B  F7 83 DC 09 00 00 00 00 40 00   test dword ptr [rbx + 0x9dc], 0x400000
0050B995  4C 8B 83 28 02 00 00            mov r8, qword ptr [rbx + 0x228]
0050B99C  75 10                           jne 0x14050b9ae
0050B99E  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
0050B9A2  41 C6 00 C3                     mov byte ptr [r8], 0xc3
0050B9A6  0F 22 C0                        mov cr0, rax
0050B9A9  E9 86 02 00 00                  jmp 0x14050bc34
0050B9AE  48 8B 93 D8 05 00 00            mov rdx, qword ptr [rbx + 0x5d8]
0050B9B5  4C 8D 4D 68                     lea r9, [rbp + 0x68]
0050B9B9  49 8B C0                        mov rax, r8
0050B9BC  C6 45 68 C3                     mov byte ptr [rbp + 0x68], 0xc3
0050B9C0  48 C1 E8 09                     shr rax, 9
0050B9C4  41 BB 04 00 00 00               mov r11d, 4
0050B9CA  48 23 C1                        and rax, rcx
0050B9CD  45 8B D3                        mov r10d, r11d
0050B9D0  48 03 C2                        add rax, rdx
0050B9D3  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0050B9D7  49 BE F8 FF FF FF 7F 00 00 00   movabs r14, 0x7ffffffff8
0050B9E1  48 89 01                        mov qword ptr [rcx], rax
0050B9E4  48 8D 49 08                     lea rcx, [rcx + 8]
0050B9E8  48 C1 E8 09                     shr rax, 9
0050B9EC  49 23 C6                        and rax, r14
0050B9EF  48 03 C2                        add rax, rdx
0050B9F2  4D 2B DD                        sub r11, r13
0050B9F5  75 EA                           jne 0x14050b9e1
0050B9F7  41 83 CF FF                     or r15d, 0xffffffff
0050B9FB  45 03 D7                        add r10d, r15d
0050B9FE  74 0F                           je 0x14050ba0f
0050BA00  4A 8B 44 D5 F0                  mov rax, qword ptr [rbp + r10*8 - 0x10]
0050BA05  8B 08                           mov ecx, dword ptr [rax]
0050BA07  C0 E9 07                        shr cl, 7
0050BA0A  41 84 CD                        test r13b, cl
0050BA0D  74 EC                           je 0x14050b9fb
0050BA0F  4E 8B 5C D5 F0                  mov r11, qword ptr [rbp + r10*8 - 0x10]
0050BA14  49 8B 03                        mov rax, qword ptr [r11]
0050BA17  48 83 C8 62                     or rax, 0x62
0050BA1B  49 89 03                        mov qword ptr [r11], rax
0050BA1E  0F 20 E2                        mov rdx, cr4
0050BA21  41 BE 80 00 02 00               mov r14d, 0x20080
0050BA27  49 85 D6                        test r14, rdx
0050BA2A  74 0E                           je 0x14050ba3a
0050BA2C  48 8B CA                        mov rcx, rdx
0050BA2F  49 33 CC                        xor rcx, r12
0050BA32  0F 22 E1                        mov cr4, rcx
0050BA35  0F 22 E2                        mov cr4, rdx
0050BA38  EB 06                           jmp 0x14050ba40
0050BA3A  0F 20 D9                        mov rcx, cr3
0050BA3D  0F 22 D9                        mov cr3, rcx
0050BA40  41 8B C8                        mov ecx, r8d
0050BA43  41 BA 00 10 00 00               mov r10d, 0x1000
0050BA49  81 E1 FF 0F 00 00               and ecx, 0xfff
0050BA4F  41 8B D5                        mov edx, r13d
0050BA52  44 2B D1                        sub r10d, ecx
0050BA55  45 3B D5                        cmp r10d, r13d
0050BA58  41 0F 42 D2                     cmovb edx, r10d
0050BA5C  83 FA 08                        cmp edx, 8
0050BA5F  72 1D                           jb 0x14050ba7e
0050BA61  44 8B D2                        mov r10d, edx
0050BA64  49 C1 EA 03                     shr r10, 3
0050BA68  49 8B 09                        mov rcx, qword ptr [r9]
0050BA6B  83 C2 F8                        add edx, -8
0050BA6E  49 89 08                        mov qword ptr [r8], rcx
0050BA71  49 83 C1 08                     add r9, 8
0050BA75  49 83 C0 08                     add r8, 8
0050BA79  4D 2B D5                        sub r10, r13
0050BA7C  75 EA                           jne 0x14050ba68
0050BA7E  45 33 D2                        xor r10d, r10d
0050BA81  85 D2                           test edx, edx
0050BA83  0F 84 8C 01 00 00               je 0x14050bc15
0050BA89  4D 2B C1                        sub r8, r9
0050BA8C  41 8A 09                        mov cl, byte ptr [r9]
0050BA8F  43 88 0C 01                     mov byte ptr [r9 + r8], cl
0050BA93  4D 03 CD                        add r9, r13
0050BA96  41 03 D7                        add edx, r15d
0050BA99  0F 84 76 01 00 00               je 0x14050bc15
0050BA9F  EB EB                           jmp 0x14050ba8c
0050BAA1  81 83 48 08 00 00 30 06 00 00   add dword ptr [rbx + 0x848], 0x630
0050BAAB  48 8D 8B 30 06 00 00            lea rcx, [rbx + 0x630]
0050BAB2  8B B3 C4 00 00 00               mov esi, dword ptr [rbx + 0xc4]
0050BAB8  4C 8B CB                        mov r9, rbx
0050BABB  4C 8B 9B 38 08 00 00            mov r11, qword ptr [rbx + 0x838]
0050BAC2  48 8B C3                        mov rax, rbx
0050BAC5  44 89 93 C4 00 00 00            mov dword ptr [rbx + 0xc4], r10d
0050BACC  44 8B 93 34 08 00 00            mov r10d, dword ptr [rbx + 0x834]
0050BAD3  48 3B D9                        cmp rbx, rcx
0050BAD6  73 0C                           jae 0x14050bae4
0050BAD8  0F 18 00                        prefetchnta byte ptr [rax]
0050BADB  48 83 C0 40                     add rax, 0x40
0050BADF  48 3B C1                        cmp rax, rcx
0050BAE2  72 F4                           jb 0x14050bad8
0050BAE4  BF 0C 00 00 00                  mov edi, 0xc
0050BAE9  4D 8B C3                        mov r8, r11
0050BAEC  49 BC 01 20 00 04 80 00 10 70   movabs r12, 0x7010008004002001
0050BAF6  44 8D 6F F5                     lea r13d, [rdi - 0xb]
0050BAFA  B8 08 00 00 00                  mov eax, 8
0050BAFF  4D 33 01                        xor r8, qword ptr [r9]
0050BB02  41 8B CA                        mov ecx, r10d
0050BB05  49 D3 C0                        rol r8, cl
0050BB08  4D 33 41 08                     xor r8, qword ptr [r9 + 8]
0050BB0C  49 83 C1 10                     add r9, 0x10
0050BB10  49 D3 C0                        rol r8, cl
0050BB13  49 2B C5                        sub rax, r13
0050BB16  75 E7                           jne 0x14050baff
0050BB18  49 8B C9                        mov rcx, r9
0050BB1B  48 2B CB                        sub rcx, rbx
0050BB1E  49 33 CB                        xor rcx, r11
0050BB21  48 8B C1                        mov rax, rcx
0050BB24  48 C1 C0 11                     rol rax, 0x11
0050BB28  48 33 C8                        xor rcx, rax
0050BB2B  49 8B C4                        mov rax, r12
0050BB2E  48 F7 E1                        mul rcx
0050BB31  44 33 D0                        xor r10d, eax
0050BB34  44 33 D2                        xor r10d, edx
0050BB37  41 83 E2 3F                     and r10d, 0x3f
0050BB3B  45 0F 44 D5                     cmove r10d, r13d
0050BB3F  83 CA FF                        or edx, 0xffffffff
0050BB42  03 FA                           add edi, edx
0050BB44  75 B4                           jne 0x14050bafa
0050BB46  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0050BB4B  44 8D 5F 01                     lea r11d, [rdi + 1]
0050BB4F  4C 8B 6D 60                     mov r13, qword ptr [rbp + 0x60]
0050BB53  4D 33 01                        xor r8, qword ptr [r9]
0050BB56  41 8B CA                        mov ecx, r10d
0050BB59  49 D3 C0                        rol r8, cl
0050BB5C  49 83 C1 08                     add r9, 8
0050BB60  41 83 C6 F8                     add r14d, -8
0050BB64  4D 2B FB                        sub r15, r11
0050BB67  75 EA                           jne 0x14050bb53
0050BB69  45 85 F6                        test r14d, r14d
0050BB6C  74 15                           je 0x14050bb83
0050BB6E  41 0F B6 01                     movzx eax, byte ptr [r9]
0050BB72  41 8B CA                        mov ecx, r10d
0050BB75  4C 33 C0                        xor r8, rax
0050BB78  4D 03 CB                        add r9, r11
0050BB7B  49 D3 C0                        rol r8, cl
0050BB7E  44 03 F2                        add r14d, edx
0050BB81  75 EB                           jne 0x14050bb6e
0050BB83  48 8B 83 20 01 00 00            mov rax, qword ptr [rbx + 0x120]
0050BB8A  41 8B D3                        mov edx, r11d
0050BB8D  49 8B CC                        mov rcx, r12
0050BB90  89 B3 C4 00 00 00               mov dword ptr [rbx + 0xc4], esi
0050BB96  4C 89 83 68 0A 00 00            mov qword ptr [rbx + 0xa68], r8
0050BB9D  E8 BE EE 6D 00                  call 0x140beaa60
0050BBA2  49 8B CD                        mov rcx, r13
0050BBA5  E8 86 50 F4 FF                  call 0x140450c30
0050BBAA  84 C0                           test al, al
0050BBAC  41 8B CF                        mov ecx, r15d
0050BBAF  0F 95 C1                        setne cl
0050BBB2  84 C0                           test al, al
0050BBB4  74 27                           je 0x14050bbdd
0050BBB6  FA                              cli
0050BBB7  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0050BBC0  48 8B 05 81 AE AB 00            mov rax, qword ptr [rip + 0xabae81]
0050BBC7  48 8B 88 58 06 00 00            mov rcx, qword ptr [rax + 0x658]
0050BBCE  48 8B 04 0A                     mov rax, qword ptr [rdx + rcx]
0050BBD2  FB                              sti
0050BBD3  0F BA 20 18                     bt dword ptr [rax], 0x18
0050BBD7  41 8B CF                        mov ecx, r15d
0050BBDA  0F 92 C1                        setb cl
0050BBDD  44 38 3D 39 EE 8F 00            cmp byte ptr [rip + 0x8fee39], r15b
0050BBE4  75 1A                           jne 0x14050bc00
0050BBE6  44 38 3D EF B9 A3 00            cmp byte ptr [rip + 0xa3b9ef], r15b
0050BBED  75 11                           jne 0x14050bc00
0050BBEF  85 C9                           test ecx, ecx
0050BBF1  75 0D                           jne 0x14050bc00
0050BBF3  E8 A0 CE 0A 00                  call 0x1405b8a98
0050BBF8  48 85 C0                        test rax, rax
0050BBFB  74 03                           je 0x14050bc00
0050BBFD  0F 23 F8                        mov dr7, rax
0050BC00  48 81 C4 18 01 00 00            add rsp, 0x118
0050BC07  41 5F                           pop r15
0050BC09  41 5E                           pop r14
0050BC0B  41 5D                           pop r13
0050BC0D  41 5C                           pop r12
0050BC0F  5F                              pop rdi
0050BC10  5E                              pop rsi
0050BC11  5B                              pop rbx
0050BC12  5D                              pop rbp
0050BC13  C3                              ret
0050BC14  CC                              int3
0050BC15  49 89 03                        mov qword ptr [r11], rax
0050BC18  0F 20 E1                        mov rcx, cr4
0050BC1B  49 85 CE                        test r14, rcx
0050BC1E  74 0E                           je 0x14050bc2e
0050BC20  48 8B C1                        mov rax, rcx
0050BC23  49 33 C4                        xor rax, r12
0050BC26  0F 22 E0                        mov cr4, rax
0050BC29  0F 22 E1                        mov cr4, rcx
0050BC2C  EB 06                           jmp 0x14050bc34
0050BC2E  0F 20 D8                        mov rax, cr3
0050BC31  0F 22 D8                        mov cr3, rax
0050BC34  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
0050BC39  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0050BC3E  4C 8B 5D 88                     mov r11, qword ptr [rbp - 0x78]
0050BC42  44 39 93 48 09 00 00            cmp dword ptr [rbx + 0x948], r10d
0050BC49  74 15                           je 0x14050bc60
0050BC4B  44 0F 20 C0                     mov rax, cr8
0050BC4F  B9 02 00 00 00                  mov ecx, 2
0050BC54  3A C1                           cmp al, cl
0050BC56  73 08                           jae 0x14050bc60
0050BC58  44 0F 20 C0                     mov rax, cr8
0050BC5C  44 0F 22 C1                     mov cr8, rcx
0050BC60  8B 8B 48 09 00 00               mov ecx, dword ptr [rbx + 0x948]
0050BC66  85 C9                           test ecx, ecx
0050BC68  0F 84 BB 00 00 00               je 0x14050bd29
0050BC6E  83 E9 01                        sub ecx, 1
0050BC71  0F 84 A5 00 00 00               je 0x14050bd1c
0050BC77  83 E9 01                        sub ecx, 1
0050BC7A  0F 84 93 00 00 00               je 0x14050bd13
0050BC80  83 E9 01                        sub ecx, 1
0050BC83  0F 84 81 00 00 00               je 0x14050bd0a
0050BC89  83 E9 01                        sub ecx, 1
0050BC8C  74 40                           je 0x14050bcce
0050BC8E  83 F9 01                        cmp ecx, 1
0050BC91  74 15                           je 0x14050bca8
0050BC93  48 8B 83 B0 05 00 00            mov rax, qword ptr [rbx + 0x5b0]
0050BC9A  F0 48 83 88 40 03 00 00 01      lock or qword ptr [rax + 0x340], 1
0050BCA3  E9 81 00 00 00                  jmp 0x14050bd29
0050BCA8  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0050BCB1  48 8B 83 58 06 00 00            mov rax, qword ptr [rbx + 0x658]
0050BCB8  8B 93 D8 09 00 00               mov edx, dword ptr [rbx + 0x9d8]
0050BCBE  C1 EA 09                        shr edx, 9
0050BCC1  83 E2 1F                        and edx, 0x1f
0050BCC4  48 8B 0C 08                     mov rcx, qword ptr [rax + rcx]
0050BCC8  F0 0F AB 11                     lock bts dword ptr [rcx], edx
0050BCCC  EB 5B                           jmp 0x14050bd29
0050BCCE  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0050BCD7  48 8B 83 58 06 00 00            mov rax, qword ptr [rbx + 0x658]
0050BCDE  44 8B 83 D8 09 00 00            mov r8d, dword ptr [rbx + 0x9d8]
0050BCE5  41 C1 E8 09                     shr r8d, 9
0050BCE9  41 83 E0 1F                     and r8d, 0x1f
0050BCED  48 8B 0C 08                     mov rcx, qword ptr [rax + rcx]
0050BCF1  48 03 8B B8 06 00 00            add rcx, qword ptr [rbx + 0x6b8]
0050BCF8  48 8B 83 98 06 00 00            mov rax, qword ptr [rbx + 0x698]
0050BCFF  48 8B 14 01                     mov rdx, qword ptr [rcx + rax]
0050BD03  F0 44 0F AB 02                  lock bts dword ptr [rdx], r8d
0050BD08  EB 1F                           jmp 0x14050bd29
0050BD0A  48 8B 83 58 05 00 00            mov rax, qword ptr [rbx + 0x558]
0050BD11  EB 10                           jmp 0x14050bd23
0050BD13  48 8B 83 50 05 00 00            mov rax, qword ptr [rbx + 0x550]
0050BD1A  EB 07                           jmp 0x14050bd23
0050BD1C  48 8B 83 40 05 00 00            mov rax, qword ptr [rbx + 0x540]
0050BD23  F0 48 0F BA 28 00               lock bts qword ptr [rax], 0
0050BD29  48 8B 83 A0 06 00 00            mov rax, qword ptr [rbx + 0x6a0]
0050BD30  4D 89 14 03                     mov qword ptr [r11 + rax], r10
0050BD34  48 8B 83 B0 06 00 00            mov rax, qword ptr [rbx + 0x6b0]
0050BD3B  4D 89 14 03                     mov qword ptr [r11 + rax], r10
0050BD3F  48 8B 8B 68 01 00 00            mov rcx, qword ptr [rbx + 0x168]
0050BD46  E8 25 ED 6D 00                  call 0x140beaa70
0050BD4B  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0050BD50  4C 8B CE                        mov r9, rsi
0050BD53  48 83 C0 F8                     add rax, -8
0050BD57  4D 8B C6                        mov r8, r14
0050BD5A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0050BD5F  49 8B D7                        mov rdx, r15
0050BD62  48 8B 83 68 01 00 00            mov rax, qword ptr [rbx + 0x168]
0050BD69  B9 09 01 00 00                  mov ecx, 0x109
0050BD6E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0050BD73  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0050BD78  E8 33 EA 6D 00                  call 0x140bea7b0
0050BD7D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSwInterruptDispatch(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_cr0;
    __int64 v_cr8;
    __int64 v_dr7;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (280);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11256932) + 2524)) & (0x100000ULL)) == 0) goto loc_0050A5FA;
    result = KeExitRetpoline(a1, a2, a3, a4);
    goto loc_0050A5FD;
loc_0050A5FA:
loc_0050A5FD:
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_mB0 = a2;
    a2 = (a2) ^ (v_rsi);
    a2 = (a2) & (15);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11256932) + 2776)) + (0xB3FULL);
    result = ExAllocatePool2(66, a2, (unsigned int)(*(unsigned int *)(v_rip + 9456774 + a2 * 4)), a4);
    v_r15 = 0;
    v_stack_m118 = result;
    if (result == 0) goto loc_0050BBA2;
    *(unsigned __int64 *)(result + 24) = result;
    *(unsigned __int64 *)(result) = 0;
    *(unsigned __int64 *)(result + 16) = v_rip + 67258;
    v_stack_p10 = result + 32;
    result = memcpy(result + 32, *(unsigned __int64 *)(v_rip + 11256932), (unsigned int)(0xAE8ULL), a4);
    *(unsigned __int64 *)(result + 2784) = *(unsigned __int64 *)(v_rip + 11256932);
    *(unsigned __int64 *)(result + 32 + 2760) = result + 2824;
    a2 = (*(unsigned __int64 *)(v_rip + 11256932)) << (32);
    result = (result + 2824) | (a2);
    *(unsigned int *)(result + 32 + 2120) = 0;
    a2 = (result) ^ (result);
    v_stack_mA8 = a2;
    result = (v_rsi) ^ (a2);
    a2 = 0;
    *(unsigned int *)(result + 32 + 2112) = 0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_mA0 = a2;
    a2 = (unsigned int)((a2) ^ ((unsigned int)(v_rsi)));
    *(unsigned int *)(result + 32 + 2128) = (unsigned int)(a2);
    result = (result + 2879) & (-8);
    *(unsigned __int64 *)(result + 32 + 2768) = result;
    if ((*(unsigned __int64 *)(result + 32 + 2752)) >= (*(unsigned __int64 *)(result + 32 + 2752) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32 + 2752) + 2052)) * 1)) goto loc_0050A758;
loc_0050A74C:
    result = (*(unsigned __int64 *)(result + 32 + 2752)) + (64);
    if (result < (*(unsigned __int64 *)(result + 32 + 2752) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32 + 2752) + 2052)) * 1)) goto loc_0050A74C;
loc_0050A758:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32 + 2752) + 2052))))) >> (7));
    if ((unsigned int)(v_r11) == 0) goto loc_0050A7C9;
loc_0050A776:
loc_0050A77B:
    a3 = (*(unsigned __int64 *)(result + 32 + 2104)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32 + 2752)));
    a3 = (a3) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32 + 2752) + 8));
    a4 = (*(unsigned __int64 *)(result + 32 + 2752)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_0050A77B;
    a1 = (a4) - (*(unsigned __int64 *)(result + 32 + 2752));
    a1 = (a1) ^ (*(unsigned __int64 *)(result + 32 + 2104));
    a1 = (a1) ^ (a1);
    result = (unsigned int)((a1) ^ (1));
    v_stack_m98 = 1;
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32 + 2100))) ^ ((unsigned int)(result)));
    v_r10 = (unsigned int)((v_r10) & (63));
    if (condition_is_equal) { v_r10 = 1; }
    v_r11 = (unsigned int)((v_r11) + (-1));
    if (condition_is_not_equal) goto loc_0050A776;
loc_0050A7C9:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32 + 2752) + 2052))))) & (127));
    if (((unsigned int)(a2)) < 8) goto loc_0050A7F4;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_0050A7DF:
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (8);
    a2 = (unsigned int)((a2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0050A7DF;
loc_0050A7F4:
    if ((unsigned int)(a2) == 0) goto loc_0050A80D;
loc_0050A7F8:
    a3 = (a3) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (1);
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_0050A7F8;
loc_0050A80D:
    if (a3 == (*(unsigned __int64 *)(v_rip + 11256380))) goto loc_0050A962;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32 + 1416)) = *(unsigned __int64 *)(result + 32 + 2752);
    *(unsigned int *)(*(unsigned __int64 *)(result + 32 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32 + 2752) + 2052)));
    if ((*(unsigned int *)(result + 32 + 2328)) != 0) goto loc_0050A962;
    a1 = (a3) ^ (*(unsigned __int64 *)(v_rip + 11256321));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32 + 1416) + 24) = a1;
    if ((*(unsigned int *)(result + 32 + 2328)) != 0) goto loc_0050A962;
    *(unsigned __int64 *)(result + 32 + 2344) = 0;
    *(unsigned __int64 *)(result + 32 + 2336) = result + 32 + a1 * 1;
    *(unsigned __int64 *)(result + 32 + 2352) = 273;
    *(unsigned __int64 *)(result + 32 + 2360) = a3;
    *(unsigned int *)(result + 32 + 2328) = 1;
    if ((*(unsigned int *)(result + 32 + 2328)) < 0) goto loc_0050A962;
    if (((*(unsigned int *)(result + 32 + 2524)) & (0x200000ULL)) == 0) goto loc_0050A962;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 32 + 2520))))) == 0) goto loc_0050A962;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(result + 32 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0050A90B;
loc_0050A8EA:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 32 + 2676)) + result + 32 * 1)) ^ (*(unsigned __int64 *)(result + 32 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(result + 32 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(result + 32 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(result + 32 + 2676)) + result + 32 * 1) + (8);
loc_0050A90B:
    if (a2 != ((unsigned int)(*(unsigned int *)(result + 32 + 2676)) + result + 32 * 1 + a1 * 8)) goto loc_0050A8EA;
    if (a3 == (*(unsigned __int64 *)(result + 32 + 2688))) goto loc_0050A962;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32 + 1416)) = result + 32;
    *(unsigned int *)(*(unsigned __int64 *)(result + 32 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 32 + 2052)));
    result = *(unsigned __int64 *)(result + 32 + 1416);
    if ((*(unsigned int *)(result + 32 + 2328)) == 0) {
        result = *(unsigned __int64 *)(result + 32 + 1416);
        a1 = (*(unsigned __int64 *)(result + 32 + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(result + 32, a2, a3, 256);
loc_0050A962:
    v_stack_m110 = 0;
loc_0050A975:
    *(unsigned __int8 *)(v_stack_m108) = 0;
    result = (v_stack_m108) + (4 - 3);
    a1 = (unsigned int)((4) + (-1));
    if (condition_is_not_equal) goto loc_0050A975;
    v_r10 = 0;
    v_stack_p18 = 0;
    if ((*(unsigned int *)(result + 32 + 2092)) <= 0) goto loc_0050B5E8;
    v_r13 = 0;
loc_0050A9A6:
    a3 = result + 32;
    if (*(unsigned __int64 *)(result + 32 + 2752) != 0) { a3 = *(unsigned __int64 *)(result + 32 + 2752); }
    v_rsi = ((unsigned int)(*(unsigned int *)(a3 + 2088))) + (a3);
    if (v_stack_m110 == 0) goto loc_0050A9DD;
    if (v_stack_m10C <= 0) {
        v_rsi = v_stack_m108;
        a4 = v_stack_m10C;
        v_rsi = (v_rsi) + (a3);
    }
    if (((unsigned int)(a4)) == 0) goto loc_0050AAE0;
    v_r10 = (unsigned int)((0) - ((unsigned int)(a4)));
loc_0050A9F9:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) - (1));
    if (condition_is_equal) goto loc_0050AAB4;
    a1 = (unsigned int)((a1) - ((unsigned int)(2 + 4)));
    if (condition_is_equal) goto loc_0050AAA7;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0050AA9B;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_0050AA90;
    a1 = (unsigned int)((a1) - (18));
    if (condition_is_equal) goto loc_0050AA8A;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_0050AA5F;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_0050AA39;
    if (((unsigned int)(a1)) == 10) goto loc_0050AAB4;
    goto loc_0050AACD;
loc_0050AA39:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) & (0xFFFULL));
    a2 = ((unsigned int)(*(unsigned int *)(v_rsi + 40))) + (0xFFFULL);
    a2 = (a2) + (a1);
    a2 = (a2) >> (12);
    goto loc_0050AAC8;
loc_0050AA5F:
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rsi + 36))));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 36)) - 1) & ((unsigned int)(result)));
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) + (7));
    a2 = (unsigned int)((a2) & (0xFFFFFFF8ULL));
    result = (unsigned int)((*(unsigned __int16 *)(v_rsi + 40)) + (2));
    goto loc_0050AAC8;
loc_0050AA8A:
    goto loc_0050AA9F;
loc_0050AA90:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 28))) + (3));
    result = (unsigned int)((result) << (4));
    goto loc_0050AACD;
loc_0050AA9B:
loc_0050AA9F:
    result = (unsigned int)((*(unsigned __int16 *)(v_rsi + 32)) + (55));
    result = (unsigned int)((result) & (0xFFFFFFF8ULL));
    goto loc_0050AACD;
loc_0050AAA7:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 24))) + ((unsigned int)(a2)));
    result = (unsigned int)((result + result * 2) << (3));
    goto loc_0050AACD;
loc_0050AAB4:
    a2 = (a2) >> (3);
loc_0050AAC8:
loc_0050AACD:
    v_rsi = (v_rsi) + (a2 * 4 + 48);
    v_r10 = (v_r10) - (4 - 3);
    if (condition_is_not_equal) goto loc_0050A9F9;
loc_0050AAE0:
    v_stack_m110 = (unsigned int)(4 - 3);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - ((unsigned int)(a3)));
    v_stack_m10C = 0;
    v_stack_m108 = (unsigned int)(result);
    if (((unsigned int)((int)(*(unsigned int *)(v_rsi)))) != 36) goto loc_0050B297;
    if ((*(unsigned __int64 *)(v_rsi + 8)) >= (*(unsigned __int64 *)(v_rsi + 8) + (unsigned int)(*(unsigned int *)(v_rsi + 16)) * 1)) goto loc_0050AB37;
loc_0050AB2B:
    result = (*(unsigned __int64 *)(v_rsi + 8)) + (64);
    if (result < (*(unsigned __int64 *)(v_rsi + 8) + (unsigned int)(*(unsigned int *)(v_rsi + 16)) * 1)) goto loc_0050AB2B;
loc_0050AB37:
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 16))))) >> (7));
    if ((unsigned int)(v_r10) == 0) goto loc_0050ABA8;
loc_0050AB56:
loc_0050AB5B:
    v_rdi = (*(unsigned __int64 *)(v_stack_p10 + 2104)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8)));
    v_rdi = (v_rdi) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 8));
    a4 = (*(unsigned __int64 *)(v_rsi + 8)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_0050AB5B;
    a1 = (a4) - (*(unsigned __int64 *)(v_rsi + 8));
    a1 = (a1) ^ (*(unsigned __int64 *)(v_stack_p10 + 2104));
    a1 = (a1) ^ (a1);
    result = (unsigned int)((v_stack_p10) ^ (2));
    v_stack_m90 = 2;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 2100))) ^ ((unsigned int)(result)));
    v_r14 = (unsigned int)((v_r14) & (63));
    if (condition_is_equal) { v_r14 = 1; }
    v_r10 = (unsigned int)((v_r10) + (-1));
    if (condition_is_not_equal) goto loc_0050AB56;
loc_0050ABA8:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 16))) & (127));
    if (((unsigned int)(a3)) < 8) goto loc_0050ABD5;
    result = ((unsigned int)((unsigned int)(a3))) >> (3);
loc_0050ABBF:
    v_rdi = (v_rdi) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (8);
    a3 = (unsigned int)((a3) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0050ABBF;
loc_0050ABD5:
    if ((unsigned int)(a3) == 0) goto loc_0050ABF0;
loc_0050ABDA:
    v_rdi = (v_rdi) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (1);
    a3 = (unsigned int)((a3) + (-1));
    if (condition_is_not_equal) goto loc_0050ABDA;
loc_0050ABF0:
    goto loc_0050ABF7;
loc_0050ABF5:
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)(v_rdi)));
loc_0050ABF7:
    result = (v_rdi) >> (31);
    if (result != 0) goto loc_0050ABF5;
    if (((unsigned int)(v_rdi)) == (*(unsigned int *)(v_rsi + 20))) goto loc_0050AE1F;
    v_r12 = 0;
    if ((*(unsigned int *)(v_rsi)) == 0) {
        v_r12 = 0;
        if ((*(unsigned int *)(v_rsi + 24)) != 0) { v_r12 = 1; }
    }
    if ((unsigned int)(*(unsigned int *)(v_rsi + 16)) == 0) goto loc_0050ACDB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2524)))) & (64)) == 0) goto loc_0050ACDB;
    v_r15 = (*(unsigned __int64 *)(v_rsi + 8)) & (0xFFFFFFFFFFFFF000ULL);
    result = ((unsigned int)(*(unsigned int *)(v_rsi + 16)) - 1) + (*(unsigned __int64 *)(v_rsi + 8));
    result = (result) | (0xFFFULL);
    v_stack_m100 = result;
    v_stack_p20 = v_r15 - 1;
loc_0050AC6C:
loc_0050AC70:
    a2 = 0;
    result = KeGuardDispatchICall(v_r15, a2, a3, a4);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_0050ACAD;
    if ((unsigned int)(v_r12) != 0) goto loc_0050ACD4;
    if (((unsigned __int8)(v_cr8)) > 1) goto loc_0050ACB1;
    goto loc_0050AC70;
loc_0050ACAD:
    if (sign_flag) goto loc_0050ACD4;
loc_0050ACB1:
    result = (v_stack_p20) + ((unsigned int)(0x1000ULL));
    v_r15 = (v_r15) + ((unsigned int)(0x1000ULL));
    v_stack_p20 = result;
    if (result != v_stack_m100) goto loc_0050AC6C;
    goto loc_0050AE1F;
loc_0050ACD4:
    v_r13 = 0;
loc_0050ACDB:
    result = (unsigned int)(*(unsigned int *)(v_rsi + 20));
    if ((*(unsigned int *)(v_stack_p10 + 2328)) == 0) {
        a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 20)));
        result = (unsigned int)(v_rdi);
        a1 = (a1) ^ (result);
        result = *(unsigned __int64 *)(v_stack_p10 + 1416);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    if ((*(unsigned int *)(v_stack_p10 + 2328)) != 0) goto loc_0050AE1F;
    result = (result) + (v_stack_p10);
    *(unsigned __int64 *)(v_stack_p10 + 2336) = result;
    result = (result) + (v_rsi);
    *(unsigned __int64 *)(v_stack_p10 + 2344) = result;
    *(unsigned __int64 *)(v_stack_p10 + 2360) = *(unsigned __int64 *)(v_rsi + 8);
    *(unsigned __int64 *)(v_stack_p10 + 2352) = (int)(*(unsigned int *)(v_rsi));
    *(unsigned int *)(v_stack_p10 + 2328) = 1;
    if (condition_is_below) goto loc_0050AE1F;
    if (((*(unsigned int *)((unsigned int)(0x9DCULL) + v_stack_p10 * 1)) & (0x200000ULL)) == 0) goto loc_0050AE1F;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2520))))) == 0) goto loc_0050AE1F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0050ADCA;
loc_0050ADA9:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1)) ^ (*(unsigned __int64 *)(v_stack_p10 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(v_stack_p10 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1) + (8);
loc_0050ADCA:
    if (a2 != ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1 + a1 * 8)) goto loc_0050ADA9;
    if (a3 == (*(unsigned __int64 *)(v_stack_p10 + 2688))) goto loc_0050AE1F;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1416)) = v_stack_p10;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2052)));
    result = *(unsigned __int64 *)(v_stack_p10 + 1416);
    if ((*(unsigned int *)(v_stack_p10 + 2328)) == 0) {
        result = *(unsigned __int64 *)(v_stack_p10 + 1416);
        a1 = (*(unsigned __int64 *)(v_stack_p10 + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(v_stack_p10, a2, a3, 256);
loc_0050AE1F:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_stack_p10 + 1336), a2, a3, 256);
loc_0050AE5B:
loc_0050AE67:
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16) + (8);
    a3 = (v_rsi + 24) + (8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16)) != (*(unsigned __int64 *)(v_rsi + 24))) goto loc_0050AEA3;
    a2 = (unsigned int)((24) + (-8));
    if (((unsigned int)(a2)) >= 8) goto loc_0050AE67;
    if ((unsigned int)(a2) == 0) goto loc_0050AEAC;
loc_0050AE8C:
    a4 = (a4) + (1);
    a3 = (a3) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) != ((unsigned __int8)(*(unsigned __int8 *)(a3)))) goto loc_0050AEA3;
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_0050AE8C;
    goto loc_0050AEAC;
loc_0050AEA3:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16) + (24);
    if (v_rdi < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) * 2 * 8)) goto loc_0050AE5B;
loc_0050AEAC:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_stack_p10 + 1336), a2, a3, a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 12)) == 0) goto loc_0050B003;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2524)))) & (16)) == 0) goto loc_0050AFF9;
    if ((*(unsigned int *)(v_stack_p10 + 2328)) != 0) goto loc_0050AFF9;
    result = ((unsigned __int8)((unsigned __int8)(v_cr8))) + (v_stack_p10);
    *(unsigned __int64 *)(v_stack_p10 + 2336) = result;
    result = (result) + (v_rsi);
    *(unsigned __int64 *)(v_stack_p10 + 2344) = result;
    *(unsigned __int64 *)(v_stack_p10 + 2352) = (int)(*(unsigned int *)(v_rsi));
    *(unsigned __int64 *)(v_stack_p10 + 2360) = 1;
    *(unsigned int *)(v_stack_p10 + 2328) = 1;
    if (condition_is_below) goto loc_0050AFF9;
    if (condition_is_above_or_equal) goto loc_0050AFF9;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2520))))) == 0) goto loc_0050AFF9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0050AFA2;
loc_0050AF81:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1)) ^ (*(unsigned __int64 *)(v_stack_p10 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(v_stack_p10 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1) + (8);
loc_0050AFA2:
    if (a2 != ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1 + a1 * 8)) goto loc_0050AF81;
    if (a3 == (*(unsigned __int64 *)(v_stack_p10 + 2688))) goto loc_0050AFF9;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1416)) = v_stack_p10;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2052)));
    result = *(unsigned __int64 *)(v_stack_p10 + 1416);
    if ((*(unsigned int *)(v_stack_p10 + 2328)) == 0) {
        result = *(unsigned __int64 *)(v_stack_p10 + 1416);
        a1 = (*(unsigned __int64 *)(v_stack_p10 + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(v_stack_p10, a2, a3, 256);
loc_0050AFF9:
    if ((*(unsigned __int64 *)(v_rsi + 24)) == 1) goto loc_0050B12C;
loc_0050B003:
    if (v_rdi != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) * 2 * 8)) goto loc_0050B136;
    v_r13 = 0;
    if ((*(unsigned int *)(v_stack_p10 + 2328)) != 0) goto loc_0050B139;
    result = (result) + (v_stack_p10);
    *(unsigned __int64 *)(v_stack_p10 + 2336) = result;
    *(unsigned __int64 *)(v_stack_p10 + 2344) = v_rsi + v_r12 * 1;
    *(unsigned __int64 *)(v_stack_p10 + 2352) = (int)(*(unsigned int *)(v_rsi));
    *(unsigned __int64 *)(v_stack_p10 + 2360) = v_rdi;
    *(unsigned int *)(v_stack_p10 + 2328) = 1;
    if (condition_is_below) goto loc_0050B139;
    if (((*(unsigned int *)(v_stack_p10 + 2524)) & (0x200000ULL)) == 0) goto loc_0050B139;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2520))))) == 0) goto loc_0050B139;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0050B0D3;
loc_0050B0B2:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1)) ^ (*(unsigned __int64 *)(v_stack_p10 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(v_stack_p10 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1) + (8);
loc_0050B0D3:
    if (a2 != ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1 + a1 * 8)) goto loc_0050B0B2;
    if (a3 == (*(unsigned __int64 *)(v_stack_p10 + 2688))) goto loc_0050B139;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1416)) = v_stack_p10;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2052)));
    result = *(unsigned __int64 *)(v_stack_p10 + 1416);
    if ((*(unsigned int *)(v_stack_p10 + 2328)) == 0) {
        result = *(unsigned __int64 *)(v_stack_p10 + 1416);
        a1 = (*(unsigned __int64 *)(v_stack_p10 + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(v_stack_p10, a2, a3, 256);
    goto loc_0050B139;
loc_0050B12C:
loc_0050B136:
    v_r13 = 0;
loc_0050B139:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_stack_p10 + 1336), a2, a3, 256);
    goto loc_0050B1A0;
loc_0050B176:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + 8)) < 0) goto loc_0050B1A9;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + 8))) goto loc_0050B1A9;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + 16))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + 8));
    if (result <= (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + 8))) goto loc_0050B1A9;
    if (result == 0) goto loc_0050B1A9;
loc_0050B1A0:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16) + (24);
    if (v_rdi < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) * 2 * 8)) goto loc_0050B176;
loc_0050B1A9:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_stack_p10 + 1336), result, a3, 256);
    if (v_rdi == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) * 2 * 8)) goto loc_0050B5BE;
    if ((*(unsigned int *)(v_stack_p10 + 2328)) != 0) goto loc_0050B5BE;
    result = ((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)))) + (v_stack_p10);
    *(unsigned __int64 *)(v_stack_p10 + 2336) = result;
    *(unsigned __int64 *)(v_stack_p10 + 2344) = v_rsi + v_r12 * 1;
    *(unsigned __int64 *)(v_stack_p10 + 2352) = (int)(*(unsigned int *)(v_rsi));
    *(unsigned __int64 *)(v_stack_p10 + 2360) = v_rdi;
    *(unsigned int *)(v_stack_p10 + 2328) = 1;
    if (condition_is_below) goto loc_0050B5BE;
    if (((*(unsigned int *)(v_stack_p10 + 2524)) & (0x200000ULL)) == 0) goto loc_0050B5BE;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2520))))) == 0) goto loc_0050B5BE;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0050B28D;
loc_0050B26C:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1)) ^ (*(unsigned __int64 *)(v_stack_p10 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(v_stack_p10 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1) + (8);
loc_0050B28D:
    if (a2 != ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1 + a1 * 8)) goto loc_0050B26C;
    goto loc_0050B56C;
loc_0050B297:
    if (((unsigned int)(result)) > 43) goto loc_0050B5CB;
    if (((unsigned int)(result)) >= 43) goto loc_0050B5CB;
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_stack_p10 + 1336), a2, a3, (unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1 + a1 * 8);
loc_0050B2F0:
loc_0050B2FC:
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16) + (8);
    a3 = (v_rsi + 24) + (8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16)) != (*(unsigned __int64 *)(v_rsi + 24))) goto loc_0050B338;
    a2 = (unsigned int)((24) + (-8));
    if (((unsigned int)(a2)) >= 8) goto loc_0050B2FC;
    if ((unsigned int)(a2) == 0) goto loc_0050B341;
loc_0050B321:
    a4 = (a4) + (1);
    a3 = (a3) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) != ((unsigned __int8)(*(unsigned __int8 *)(a3)))) goto loc_0050B338;
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_0050B321;
    goto loc_0050B341;
loc_0050B338:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16) + (24);
    if (v_rdi < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) * 2 * 8)) goto loc_0050B2F0;
loc_0050B341:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_stack_p10 + 1336), a2, a3, a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 12)) == 0) goto loc_0050B49B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2524)))) & (16)) == 0) goto loc_0050B491;
    if ((*(unsigned int *)(v_stack_p10 + 2328)) != 0) goto loc_0050B491;
    result = ((unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8))))) + (v_stack_p10);
    *(unsigned __int64 *)(v_stack_p10 + 2336) = result;
    result = (result) + (v_rsi);
    *(unsigned __int64 *)(v_stack_p10 + 2344) = result;
    *(unsigned __int64 *)(v_stack_p10 + 2352) = (int)(*(unsigned int *)(v_rsi));
    *(unsigned __int64 *)(v_stack_p10 + 2360) = 1;
    *(unsigned int *)(v_stack_p10 + 2328) = 1;
    if (condition_is_below) goto loc_0050B491;
    if (condition_is_above_or_equal) goto loc_0050B491;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2520))))) == 0) goto loc_0050B491;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0050B437;
loc_0050B416:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1)) ^ (*(unsigned __int64 *)(v_stack_p10 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(v_stack_p10 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1) + (8);
loc_0050B437:
    if (a2 != ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1 + a1 * 8)) goto loc_0050B416;
    if (a3 == (*(unsigned __int64 *)(v_stack_p10 + 2688))) goto loc_0050B491;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1416)) = v_stack_p10;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2052)));
    result = *(unsigned __int64 *)(v_stack_p10 + 2688);
    if ((*(unsigned int *)(v_stack_p10 + 2328)) == 0) {
        a1 = a3;
        a1 = (a1) ^ (*(unsigned __int64 *)(v_stack_p10 + 2688));
        result = *(unsigned __int64 *)(v_stack_p10 + 1416);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(v_stack_p10, a2, a3, 256);
loc_0050B491:
    if ((*(unsigned __int64 *)(v_rsi + 24)) == 1) goto loc_0050B5BE;
loc_0050B49B:
    if (v_rdi != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)) + 16 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1568)))) * 2 * 8)) goto loc_0050B5BE;
    if ((*(unsigned int *)(v_stack_p10 + 2328)) != 0) goto loc_0050B5BE;
    result = (result) + (v_stack_p10);
    *(unsigned __int64 *)(v_stack_p10 + 2336) = result;
    result = (result) + (v_rsi);
    *(unsigned __int64 *)(v_stack_p10 + 2344) = result;
    *(unsigned __int64 *)(v_stack_p10 + 2352) = (int)(*(unsigned int *)(v_rsi));
    *(unsigned __int64 *)(v_stack_p10 + 2360) = v_rdi;
    *(unsigned int *)(v_stack_p10 + 2328) = 1;
    if (condition_is_below) goto loc_0050B5BE;
    if (((*(unsigned int *)(v_stack_p10 + 2524)) & (0x200000ULL)) == 0) goto loc_0050B5BE;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2520))))) == 0) goto loc_0050B5BE;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_0050B567;
loc_0050B546:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1)) ^ (*(unsigned __int64 *)(v_stack_p10 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(v_stack_p10 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1) + (8);
loc_0050B567:
    if (a2 != ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2676)) + v_stack_p10 * 1 + a1 * 8)) goto loc_0050B546;
loc_0050B56C:
    if (a3 == (*(unsigned __int64 *)(v_stack_p10 + 2688))) goto loc_0050B5BE;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1416)) = v_stack_p10;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2052)));
    result = *(unsigned __int64 *)(v_stack_p10 + 1416);
    if ((*(unsigned int *)(v_stack_p10 + 2328)) == 0) {
        result = *(unsigned __int64 *)(v_stack_p10 + 1416);
        a1 = (*(unsigned __int64 *)(v_stack_p10 + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(v_stack_p10, a2, a3, 256);
loc_0050B5BE:
loc_0050B5CB:
    a1 = (unsigned int)(((unsigned int)(v_stack_p18)) + 1);
    v_stack_p18 = (unsigned int)(a1);
    if (((unsigned int)(a1)) < (*(unsigned int *)(v_stack_p10 + 2092))) goto loc_0050A9A6;
    v_r10 = 0;
loc_0050B5E8:
    if ((*(unsigned int *)(v_stack_p10 + 2328)) == 0) goto loc_0050BAA1;
    v_stack_mC0 = *(unsigned __int64 *)(v_stack_p10 + 2352);
    v_stack_mB8 = *(unsigned __int64 *)(v_stack_p10 + 2360);
    v_stack_m100 = *(unsigned __int64 *)(v_stack_p10 + 2344);
    v_stack_m118 = *(unsigned __int64 *)(v_stack_p10 + 2336);
    result = (unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8))));
    v_cr8 = (unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8))));
    if (((unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)))))) < 2) {
        result = (unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8))));
        v_cr8 = 2;
    }
    v_stack_mE8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(v_stack_p10 + 1600) * 1);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1608) + *(unsigned __int64 *)(gs_base + (0 + 32)) * 1)) + (*(unsigned __int64 *)(v_stack_p10 + 1928));
    v_stack_mD0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(v_stack_p10 + 1624) * 1);
    if (v_stack_mF8 > (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(v_stack_p10 + 1600) * 1))) goto loc_0050B696;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(v_stack_p10 + 1600) * 1)) - ((unsigned int)(*(unsigned int *)(v_stack_p10 + 1532)));
    if (v_stack_mF8 >= a1) goto loc_0050B6DA;
loc_0050B696:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(v_stack_p10 + 1616) * 1)) == 0) goto loc_0050B6CA;
    if (v_stack_mF8 > a2) goto loc_0050B6CA;
    a1 = (a2) - ((unsigned int)(*(unsigned int *)(v_stack_p10 + 1528)));
    if (v_stack_mF8 < a1) goto loc_0050B6CA;
    v_stack_mE8 = a2;
    goto loc_0050B6DA;
loc_0050B6CA:
    v_stack_mE8 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(v_stack_p10 + 1624) * 1) + *(unsigned __int64 *)(v_stack_p10 + 1672) * 1);
loc_0050B6DA:
    if (((*(unsigned int *)(v_stack_p10 + 2520)) & (0x4000000ULL)) != 0) goto loc_0050BC42;
    v_stack_mD8 = 0;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(v_stack_p10 + 1624) * 1) + *(unsigned __int64 *)(v_stack_p10 + 1672) * 1);
    if (((*(unsigned int *)(v_stack_p10 + 2524)) & (0x400000ULL)) == 0) {
        a1 = v_cr0;
        result = a1;
        v_stack_mD8 = a1;
        v_cr0 = result;
    }
    v_r15 = ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2792))) << (4);
    v_r15 = (v_r15) + (v_stack_p10 + 2800);
    v_stack_mC8 = v_r15;
    if ((*(unsigned int *)(v_stack_p10 + 2796)) <= 0) goto loc_0050B778;
loc_0050B73F:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15)) = *(unsigned __int64 *)(v_r15 + 8);
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_0050B763;
    result = (v_cr4) ^ (128);
    goto loc_0050B769;
loc_0050B763:
loc_0050B769:
    v_r11 = (v_r15) + (16);
    a2 = (unsigned int)((0) + ((unsigned int)(128 - 127)));
    if (((unsigned int)(a2)) < (*(unsigned int *)(v_stack_p10 + 2796))) goto loc_0050B73F;
loc_0050B778:
    if ((v_stack_p10 + 2800) >= v_r15) goto loc_0050B98B;
loc_0050B78B:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2800 + 8)));
    if (((*(unsigned int *)(v_stack_p10 + 2524)) & (0x400000ULL)) != 0) goto loc_0050B7E9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2800 + 8)))) < 8) goto loc_0050B7CB;
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2800 + 8))))) >> (3);
loc_0050B7B5:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2800 + 8))))) + (-8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 2800)) = *(unsigned __int64 *)(v_r11);
    a1 = (v_r11) + (8);
    a3 = (*(unsigned __int64 *)(v_stack_p10 + 2800)) + (8);
    a4 = (a4) - (128 - 127);
    if (condition_is_not_equal) goto loc_0050B7B5;
loc_0050B7CB:
    if ((unsigned int)(a2) == 0) goto loc_0050B960;
    a3 = (a3) - (a1);
loc_0050B7D6:
    *(unsigned __int8 *)(a3 + a1 * 1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    a1 = (a1) + (128 - 127);
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_0050B7D6;
    goto loc_0050B960;
loc_0050B7E9:
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2800 + 8)));
    a1 = (unsigned int)((a3) & (0xFFFULL));
    v_stack_mF0 = v_r11;
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_p10 + 2800 + 8)) + 4095) + (a1);
    a2 = (a2) >> (12);
    if ((unsigned int)(a2) == 0) goto loc_0050B960;
    v_stack_mE0 = (unsigned int)((unsigned int)(a2));
loc_0050B822:
    result = (a3) >> (9);
    result = (result) & (*(unsigned __int64 *)(v_stack_p10 + 2352));
    result = (result) + (*(unsigned __int64 *)(v_stack_p10 + 1496));
loc_0050B84A:
    *(unsigned __int64 *)(v_stack_m88) = result;
    result = (result) >> (9);
    result = (result) & (*(unsigned __int64 *)(v_stack_p10 + 2352));
    result = (result) + (*(unsigned __int64 *)(v_stack_p10 + 1496));
    a2 = (4) - (128 - 127);
    if (condition_is_not_equal) goto loc_0050B84A;
loc_0050B860:
    a4 = (unsigned int)((4) + (-1));
    if (condition_is_equal) goto loc_0050B875;
    a1 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m58 + a4 * 8 - 48)))) >> (7));
    if ((((unsigned __int8)(128 - 127)) & ((unsigned __int8)(a1))) == 0) goto loc_0050B860;
loc_0050B875:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58 + a4 * 8 - 48))) | (98);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58 + a4 * 8 - 48)) = result;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_0050B8A2;
    goto loc_0050B8A8;
loc_0050B8A2:
loc_0050B8A8:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a3))) & (0xFFFULL));
    a2 = (unsigned int)(((unsigned int)(0x1000ULL)) - ((unsigned int)(a1)));
    a4 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2800 + 8))))));
    if (((unsigned int)(a2)) < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2800 + 8))))))) { a4 = (unsigned int)(a2); }
    if (((unsigned int)(a4)) < 8) goto loc_0050B8F8;
    v_rsi = ((unsigned int)((unsigned int)(a4))) >> (3);
loc_0050B8DF:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(a4))) + (-8));
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(v_stack_mF0);
    a2 = (v_stack_mF0) + (8);
    v_r10 = (a3) + (8);
    v_rsi = (v_rsi) - (1);
    if (condition_is_not_equal) goto loc_0050B8DF;
loc_0050B8F8:
    if ((unsigned int)(v_rdi) == 0) goto loc_0050B90D;
    v_r10 = (v_r10) - (a2);
loc_0050B8FF:
    *(unsigned __int8 *)(a2 + v_r10 * 1) = (unsigned __int8)(*(unsigned __int8 *)(a2));
    a2 = (a2) + (1);
    v_rdi = (unsigned int)((v_rdi) + (-1));
    if (condition_is_not_equal) goto loc_0050B8FF;
loc_0050B90D:
    a3 = (a3) + ((unsigned int)((unsigned int)(a4)));
    v_rsi = (unsigned int)(((unsigned int)(v_stack_p18)) - ((unsigned int)(a4)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58 + a4 * 8 - 48)) = result;
    v_stack_p18 = (unsigned int)(v_rsi);
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_0050B93E;
    goto loc_0050B944;
loc_0050B93E:
loc_0050B944:
    if (((v_cr4) & (0x20080ULL)) != 0) goto loc_0050B822;
    v_r10 = 0;
loc_0050B960:
    v_r14 = (v_stack_p10 + 2800) + (16);
    v_r11 = (v_r11) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_p20))));
    if (v_r14 < v_stack_mC8) goto loc_0050B78B;
loc_0050B98B:
    if (((*(unsigned int *)(v_stack_p10 + 2524)) & (0x400000ULL)) != 0) goto loc_0050B9AE;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p10 + 552)) = 195;
    goto loc_0050BC34;
loc_0050B9AE:
    v_stack_p10 = 195;
    result = (*(unsigned __int64 *)(v_stack_p10 + 552)) >> (9);
    result = (result) & (v_cr4);
    result = (result) + (*(unsigned __int64 *)(v_stack_p10 + 1496));
loc_0050B9E1:
    *(unsigned __int64 *)(v_stack_m68) = result;
    result = (result) >> (9);
    result = (result) & (v_r14);
    result = (result) + (*(unsigned __int64 *)(v_stack_p10 + 1496));
    v_r11 = (4) - (1);
    if (condition_is_not_equal) goto loc_0050B9E1;
    v_r15 = (unsigned int)((v_stack_mC8) | (0xFFFFFFFFULL));
loc_0050B9FB:
    v_r10 = (unsigned int)((4) + ((unsigned int)(v_r15)));
    if (condition_is_equal) goto loc_0050BA0F;
    a1 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m58 + v_r10 * 8 - 16)))) >> (7));
    if (((1) & ((unsigned __int8)(a1))) == 0) goto loc_0050B9FB;
loc_0050BA0F:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58 + v_r10 * 8 - 16))) | (98);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58 + v_r10 * 8 - 16)) = result;
    if ((((unsigned int)(0x20080ULL)) & (v_cr4)) == 0) goto loc_0050BA3A;
    a1 = (v_cr4) ^ (128);
    goto loc_0050BA40;
loc_0050BA3A:
loc_0050BA40:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p10 + 552)))) & (0xFFFULL));
    v_r10 = (unsigned int)(((unsigned int)(0x1000ULL)) - ((unsigned int)(a1)));
    a2 = 1;
    if (((unsigned int)(v_r10)) < 1) { a2 = (unsigned int)(v_r10); }
    if (((unsigned int)(a2)) < 8) goto loc_0050BA7E;
    v_r10 = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_0050BA68:
    a2 = (unsigned int)((a2) + (-8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 552)) = *(unsigned __int64 *)(v_stack_p10);
    a4 = (v_stack_p10) + (8);
    a3 = (*(unsigned __int64 *)(v_stack_p10 + 552)) + (8);
    v_r10 = (v_r10) - (1);
    if (condition_is_not_equal) goto loc_0050BA68;
loc_0050BA7E:
    v_r10 = 0;
    if ((unsigned int)(a2) == 0) goto loc_0050BC15;
    a3 = (a3) - (a4);
loc_0050BA8C:
    *(unsigned __int8 *)(a4 + a3 * 1) = (unsigned __int8)(*(unsigned __int8 *)(a4));
    a4 = (a4) + (1);
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r15)));
    if (condition_is_equal) goto loc_0050BC15;
    goto loc_0050BA8C;
loc_0050BAA1:
    *(unsigned int *)(v_stack_p10 + 196) = 0;
    if (v_stack_p10 >= (v_stack_p10 + 1584)) goto loc_0050BAE4;
loc_0050BAD8:
    result = (v_stack_p10) + (64);
    if (result < (v_stack_p10 + 1584)) goto loc_0050BAD8;
loc_0050BAE4:
loc_0050BAFA:
loc_0050BAFF:
    a3 = (*(unsigned __int64 *)(v_stack_p10 + 2104)) ^ (*(unsigned __int64 *)(v_stack_p10));
    a3 = (a3) ^ (*(unsigned __int64 *)(v_stack_p10 + 8));
    a4 = (v_stack_p10) + (16);
    result = (8) - (12 - 11);
    if (condition_is_not_equal) goto loc_0050BAFF;
    a1 = (a4) - (v_stack_p10);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_stack_p10 + 2104));
    a1 = (a1) ^ (a1);
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 2100))) ^ (128));
    v_r10 = (unsigned int)((v_r10) ^ ((unsigned int)(a2)));
    v_r10 = (unsigned int)((v_r10) & (63));
    if (condition_is_equal) { v_r10 = (unsigned int)(12 - 11); }
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    v_rdi = (unsigned int)((12) + ((unsigned int)(a2)));
    if (condition_is_not_equal) goto loc_0050BAFA;
loc_0050BB53:
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (8);
    v_r14 = (unsigned int)(((unsigned int)(0x20080ULL)) + (-8));
    v_r15 = (v_r15) - (v_rdi + 1);
    if (condition_is_not_equal) goto loc_0050BB53;
    if ((unsigned int)(v_r14) == 0) goto loc_0050BB83;
loc_0050BB6E:
    a3 = (a3) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (v_rdi + 1);
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(a2)));
    if (condition_is_not_equal) goto loc_0050BB6E;
loc_0050BB83:
    *(unsigned int *)(v_stack_p10 + 196) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 196)));
    *(unsigned __int64 *)(v_stack_p10 + 2664) = a3;
    result = KeGuardDispatchICall(v_stack_m118, (unsigned int)((unsigned int)(v_rdi + 1)), a3, a4);
loc_0050BBA2:
    result = KiGetTrapFrameMode(v_stack_p8, (unsigned int)((unsigned int)(v_rdi + 1)), a3, a4);
    a1 = ((unsigned __int8)(result) != 0) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) {
        a2 = *(unsigned __int64 *)(gs_base + (0 + 32));
        result = *(unsigned __int64 *)(v_rip + 11251329);
        a1 = *(unsigned __int64 *)(result + 1624);
        result = *(unsigned __int64 *)(a2 + a1 * 1);
        a1 = (unsigned int)(v_r15);
        a1 = (condition_is_below) ? 1 : 0;
    }
    if ((*(unsigned __int8 *)(v_rip + 9432633)) != ((unsigned __int8)(v_r15))) goto loc_0050BC00;
    if ((*(unsigned __int8 *)(v_rip + 10729967)) != ((unsigned __int8)(v_r15))) goto loc_0050BC00;
    if ((unsigned int)(a1) != 0) goto loc_0050BC00;
    result = KiReadKernelDr7(a1, a2, a3, a4);
    if (result != 0) {
        v_dr7 = result;
    }
    v_rsp = (v_rsp) + (280);
    return result;
loc_0050BC15:
    *(unsigned __int64 *)(v_rdi + 1) = result;
    if (((v_r14) & (v_cr4)) == 0) goto loc_0050BC2E;
    result = (v_cr4) ^ (v_stack_m118);
    goto loc_0050BC34;
loc_0050BC2E:
loc_0050BC34:
loc_0050BC42:
    if ((*(unsigned int *)(v_stack_p10 + 2376)) == ((unsigned int)(v_r10))) goto loc_0050BC60;
    result = v_cr8;
    if (((unsigned __int8)(v_cr8)) < 2) {
        result = v_cr8;
        v_cr8 = 2;
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 2376))) == 0) goto loc_0050BD29;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 2376))) - (1));
    if (condition_is_equal) goto loc_0050BD1C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0050BD13;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0050BD0A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0050BCCE;
    if (((unsigned int)(a1)) == 1) goto loc_0050BCA8;
    goto loc_0050BD29;
loc_0050BCA8:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 2520))) >> (9));
    a2 = (unsigned int)((a2) & (31));
    goto loc_0050BD29;
loc_0050BCCE:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 2520))) >> (9));
    a3 = (unsigned int)((a3) & (31));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 1624) + *(unsigned __int64 *)(gs_base + (0 + 32)) * 1)) + (*(unsigned __int64 *)(v_stack_p10 + 1720));
    goto loc_0050BD29;
loc_0050BD0A:
    goto loc_0050BD23;
loc_0050BD13:
    goto loc_0050BD23;
loc_0050BD1C:
loc_0050BD23:
loc_0050BD29:
    *(unsigned __int64 *)(v_stack_mD0 + *(unsigned __int64 *)(v_stack_p10 + 1696) * 1) = v_r10;
    *(unsigned __int64 *)(v_stack_mD0 + *(unsigned __int64 *)(v_stack_p10 + 1712) * 1) = v_r10;
    result = KeGuardCheckICall(*(unsigned __int64 *)(v_stack_p10 + 360), *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_stack_p10 + 1688) * 1), a3, a4);
    result = (v_stack_p70) + (-8);
    v_stack_p30 = result;
    v_stack_p28 = *(unsigned __int64 *)(v_stack_p10 + 360);
    v_stack_p20 = v_rdi;
    result = SdbpCheckDll(265, v_stack_p40, v_stack_p58, (unsigned int)(*(unsigned int *)(v_stack_p10 + 196)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiSwInterruptDispatch(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t v_cr0;
    int64_t v_cr8;
    int64_t v_dr7;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p58;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (280);
    if (((*(uint32_t *)(*(uint64_t *)(v_rip + 0xABC464) + 0x9DC)) & (0x100000ULL)) == 0) goto loc_0050A5FA;
    result = KeExitRetpoline(Arg1, Arg2, a3, a4);
    goto loc_0050A5FD;
loc_0050A5FA:
loc_0050A5FD:
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_mB0 = Arg2;
    Arg2 = (Arg2) ^ (local_rsi);
    Arg2 = (Arg2) & (15);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xABC464) + 0xAD8)) + (0xB3FULL);
    result = ExAllocatePool2(66, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x904C86 + Arg2 * 4)), a4);
    local_r15 = 0;
    v_stack_m118 = result;
    if (result == 0) goto loc_0050BBA2;
    *(uint64_t *)(result + 0x18) = result;
    *(uint64_t *)(result) = 0;
    *(uint64_t *)(result + 0x10) = v_rip + 67258;
    v_stack_p10 = result + 32;
    result = memcpy(result + 32, *(uint64_t *)(v_rip + 0xABC464), (uint32_t)(0xAE8ULL), a4);
    *(uint64_t *)(result + 0xAE0) = *(uint64_t *)(v_rip + 0xABC464);
    *(uint64_t *)(result + 0x20 + 0xAC8) = result + 2824;
    Arg2 = (*(uint64_t *)(v_rip + 0xABC464)) << (32);
    result = (result + 2824) | (Arg2);
    *(uint32_t *)(result + 0x20 + 0x848) = 0;
    Arg2 = (result) ^ (result);
    v_stack_mA8 = Arg2;
    result = (local_rsi) ^ (Arg2);
    Arg2 = 0;
    *(uint32_t *)(result + 0x20 + 0x840) = 0;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_mA0 = Arg2;
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(local_rsi)));
    *(uint32_t *)(result + 0x20 + 0x850) = (uint32_t)(Arg2);
    result = (result + 2879) & (-8);
    *(uint64_t *)(result + 0x20 + 0xAD0) = result;
    if ((*(uint64_t *)(result + 0x20 + 0xAC0)) >= (*(uint64_t *)(result + 0x20 + 0xAC0) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20 + 0xAC0) + 0x804)) * 1)) goto loc_0050A758;
loc_0050A74C:
    result = (*(uint64_t *)(result + 0x20 + 0xAC0)) + (64);
    if (result < (*(uint64_t *)(result + 0x20 + 0xAC0) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20 + 0xAC0) + 0x804)) * 1)) goto loc_0050A74C;
loc_0050A758:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20 + 0xAC0) + 0x804))))) >> (7));
    if ((uint32_t)(local_r11) == 0) goto loc_0050A7C9;
loc_0050A776:
loc_0050A77B:
    a3 = (*(uint64_t *)(result + 0x20 + 0x838)) ^ (*(uint64_t *)(*(uint64_t *)(result + 0x20 + 0xAC0)));
    a3 = (a3) ^ (*(uint64_t *)(*(uint64_t *)(result + 0x20 + 0xAC0) + 0x8));
    a4 = (*(uint64_t *)(result + 0x20 + 0xAC0)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_0050A77B;
    Arg1 = (a4) - (*(uint64_t *)(result + 0x20 + 0xAC0));
    Arg1 = (Arg1) ^ (*(uint64_t *)(result + 0x20 + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    result = (uint32_t)((Arg1) ^ (1));
    v_stack_m98 = 1;
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20 + 0x834))) ^ ((uint32_t)(result)));
    local_r10 = (uint32_t)((local_r10) & (63));
    if (condition_is_equal) { local_r10 = 1; }
    local_r11 = (uint32_t)((local_r11) + (-1));
    if (condition_is_not_equal) goto loc_0050A776;
loc_0050A7C9:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20 + 0xAC0) + 0x804))))) & (127));
    if (((uint32_t)(Arg2)) < 8) goto loc_0050A7F4;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_0050A7DF:
    a3 = (a3) ^ (*(uint64_t *)(a4));
    a4 = (a4) + (8);
    Arg2 = (uint32_t)((Arg2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0050A7DF;
loc_0050A7F4:
    if ((uint32_t)(Arg2) == 0) goto loc_0050A80D;
loc_0050A7F8:
    a3 = (a3) ^ (*(uint8_t *)(a4));
    a4 = (a4) + (1);
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_0050A7F8;
loc_0050A80D:
    if (a3 == (*(uint64_t *)(v_rip + 0xABC23C))) goto loc_0050A962;
    *(uint64_t *)(*(uint64_t *)(result + 0x20 + 0x588)) = *(uint64_t *)(result + 0x20 + 0xAC0);
    *(uint32_t *)(*(uint64_t *)(result + 0x20 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20 + 0xAC0) + 0x804)));
    if ((*(uint32_t *)(result + 0x20 + 0x918)) != 0) goto loc_0050A962;
    Arg1 = (a3) ^ (*(uint64_t *)(v_rip + 0xABC201));
    *(uint64_t *)(*(uint64_t *)(result + 0x20 + 0x588) + 0x18) = Arg1;
    if ((*(uint32_t *)(result + 0x20 + 0x918)) != 0) goto loc_0050A962;
    *(uint64_t *)(result + 0x20 + 0x928) = 0;
    *(uint64_t *)(result + 0x20 + 0x920) = result + 32 + Arg1 * 1;
    *(uint64_t *)(result + 0x20 + 0x930) = 273;
    *(uint64_t *)(result + 0x20 + 0x938) = a3;
    *(uint32_t *)(result + 0x20 + 0x918) = 1;
    if ((*(uint32_t *)(result + 0x20 + 0x918)) < 0) goto loc_0050A962;
    if (((*(uint32_t *)(result + 0x20 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_0050A962;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x20 + 0x9D8))))) == 0) goto loc_0050A962;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0050A90B;
loc_0050A8EA:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x20 + 0xA74)) + result + 0x20 * 1)) ^ (*(uint64_t *)(result + 0x20 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(result + 0x20 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(result + 0x20 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(result + 0x20 + 0xA74)) + result + 32 * 1) + (8);
loc_0050A90B:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(result + 0x20 + 0xA74)) + result + 32 * 1 + Arg1 * 8)) goto loc_0050A8EA;
    if (a3 == (*(uint64_t *)(result + 0x20 + 0xA80))) goto loc_0050A962;
    *(uint64_t *)(*(uint64_t *)(result + 0x20 + 0x588)) = result + 32;
    *(uint32_t *)(*(uint64_t *)(result + 0x20 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20 + 0x804)));
    result = *(uint64_t *)(result + 0x20 + 0x588);
    if ((*(uint32_t *)(result + 0x20 + 0x918)) == 0) {
        result = *(uint64_t *)(result + 0x20 + 0x588);
        Arg1 = (*(uint64_t *)(result + 0x20 + 0xA80)) ^ (a3);
        *(uint64_t *)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(result + 32, Arg2, a3, 256);
loc_0050A962:
    v_stack_m110 = 0;
loc_0050A975:
    *(uint8_t *)(v_stack_m108) = 0;
    result = (v_stack_m108) + (4 - 3);
    Arg1 = (uint32_t)((4) + (-1));
    if (condition_is_not_equal) goto loc_0050A975;
    local_r10 = 0;
    v_stack_p18 = 0;
    if ((*(uint32_t *)(result + 0x20 + 0x82C)) <= 0) goto loc_0050B5E8;
    local_r13 = 0;
loc_0050A9A6:
    a3 = result + 32;
    if (*(uint64_t *)(result + 0x20 + 0xAC0) != 0) { a3 = *(uint64_t *)(result + 0x20 + 0xAC0); }
    local_rsi = ((uint32_t)(*(uint32_t *)(a3 + 0x828))) + (a3);
    if (v_stack_m110 == 0) goto loc_0050A9DD;
    if (v_stack_m10C <= 0) {
        local_rsi = v_stack_m108;
        a4 = v_stack_m10C;
        local_rsi = (local_rsi) + (a3);
    }
    if (((uint32_t)(a4)) == 0) goto loc_0050AAE0;
    local_r10 = (uint32_t)((0) - ((uint32_t)(a4)));
loc_0050A9F9:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) - (1));
    if (condition_is_equal) goto loc_0050AAB4;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(2 + 4)));
    if (condition_is_equal) goto loc_0050AAA7;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0050AA9B;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_0050AA90;
    Arg1 = (uint32_t)((Arg1) - (18));
    if (condition_is_equal) goto loc_0050AA8A;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_0050AA5F;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_0050AA39;
    if (((uint32_t)(Arg1)) == 10) goto loc_0050AAB4;
    goto loc_0050AACD;
loc_0050AA39:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) & (0xFFFULL));
    Arg2 = ((uint32_t)(*(uint32_t *)(local_rsi + 0x28))) + (0xFFFULL);
    Arg2 = (Arg2) + (Arg1);
    Arg2 = (Arg2) >> (12);
    goto loc_0050AAC8;
loc_0050AA5F:
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(local_rsi + 0x24))));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x24)) - 1) & ((uint32_t)(result)));
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) + (7));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFF8ULL));
    result = (uint32_t)((*(uint16_t *)(local_rsi + 0x28)) + (2));
    goto loc_0050AAC8;
loc_0050AA8A:
    goto loc_0050AA9F;
loc_0050AA90:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x1C))) + (3));
    result = (uint32_t)((result) << (4));
    goto loc_0050AACD;
loc_0050AA9B:
loc_0050AA9F:
    result = (uint32_t)((*(uint16_t *)(local_rsi + 0x20)) + (55));
    result = (uint32_t)((result) & (0xFFFFFFF8ULL));
    goto loc_0050AACD;
loc_0050AAA7:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x18))) + ((uint32_t)(Arg2)));
    result = (uint32_t)((result + result * 2) << (3));
    goto loc_0050AACD;
loc_0050AAB4:
    Arg2 = (Arg2) >> (3);
loc_0050AAC8:
loc_0050AACD:
    local_rsi = (local_rsi) + (Arg2 * 4 + 48);
    local_r10 = (local_r10) - (4 - 3);
    if (condition_is_not_equal) goto loc_0050A9F9;
loc_0050AAE0:
    v_stack_m110 = (uint32_t)(4 - 3);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - ((uint32_t)(a3)));
    v_stack_m10C = 0;
    v_stack_m108 = (uint32_t)(result);
    if (((uint32_t)((int32_t)(*(uint32_t *)(local_rsi)))) != 36) goto loc_0050B297;
    if ((*(uint64_t *)(local_rsi + 0x8)) >= (*(uint64_t *)(local_rsi + 0x8) + (uint32_t)(*(uint32_t *)(local_rsi + 0x10)) * 1)) goto loc_0050AB37;
loc_0050AB2B:
    result = (*(uint64_t *)(local_rsi + 0x8)) + (64);
    if (result < (*(uint64_t *)(local_rsi + 0x8) + (uint32_t)(*(uint32_t *)(local_rsi + 0x10)) * 1)) goto loc_0050AB2B;
loc_0050AB37:
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x10))))) >> (7));
    if ((uint32_t)(local_r10) == 0) goto loc_0050ABA8;
loc_0050AB56:
loc_0050AB5B:
    local_rdi = (*(uint64_t *)(v_stack_p10 + 0x838)) ^ (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8)));
    local_rdi = (local_rdi) ^ (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x8));
    a4 = (*(uint64_t *)(local_rsi + 0x8)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_0050AB5B;
    Arg1 = (a4) - (*(uint64_t *)(local_rsi + 0x8));
    Arg1 = (Arg1) ^ (*(uint64_t *)(v_stack_p10 + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    result = (uint32_t)((v_stack_p10) ^ (2));
    v_stack_m90 = 2;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x834))) ^ ((uint32_t)(result)));
    local_r14 = (uint32_t)((local_r14) & (63));
    if (condition_is_equal) { local_r14 = 1; }
    local_r10 = (uint32_t)((local_r10) + (-1));
    if (condition_is_not_equal) goto loc_0050AB56;
loc_0050ABA8:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x10))) & (127));
    if (((uint32_t)(a3)) < 8) goto loc_0050ABD5;
    result = ((uint32_t)((uint32_t)(a3))) >> (3);
loc_0050ABBF:
    local_rdi = (local_rdi) ^ (*(uint64_t *)(a4));
    a4 = (a4) + (8);
    a3 = (uint32_t)((a3) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0050ABBF;
loc_0050ABD5:
    if ((uint32_t)(a3) == 0) goto loc_0050ABF0;
loc_0050ABDA:
    local_rdi = (local_rdi) ^ (*(uint8_t *)(a4));
    a4 = (a4) + (1);
    a3 = (uint32_t)((a3) + (-1));
    if (condition_is_not_equal) goto loc_0050ABDA;
loc_0050ABF0:
    goto loc_0050ABF7;
loc_0050ABF5:
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)(local_rdi)));
loc_0050ABF7:
    result = (local_rdi) >> (31);
    if (result != 0) goto loc_0050ABF5;
    if (((uint32_t)(local_rdi)) == (*(uint32_t *)(local_rsi + 0x14))) goto loc_0050AE1F;
    local_r12 = 0;
    if ((*(uint32_t *)(local_rsi)) == 0) {
        local_r12 = 0;
        if ((*(uint32_t *)(local_rsi + 0x18)) != 0) { local_r12 = 1; }
    }
    if ((uint32_t)(*(uint32_t *)(local_rsi + 0x10)) == 0) goto loc_0050ACDB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x9DC)))) & (64)) == 0) goto loc_0050ACDB;
    local_r15 = (*(uint64_t *)(local_rsi + 0x8)) & (0xFFFFFFFFFFFFF000ULL);
    result = ((uint32_t)(*(uint32_t *)(local_rsi + 0x10)) - 1) + (*(uint64_t *)(local_rsi + 0x8));
    result = (result) | (0xFFFULL);
    v_stack_m100 = result;
    v_stack_p20 = local_r15 - 1;
loc_0050AC6C:
loc_0050AC70:
    Arg2 = 0;
    result = KeGuardDispatchICall(local_r15, Arg2, a3, a4);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_0050ACAD;
    if ((uint32_t)(local_r12) != 0) goto loc_0050ACD4;
    if (((uint8_t)(v_cr8)) > 1) goto loc_0050ACB1;
    goto loc_0050AC70;
loc_0050ACAD:
    if (sign_flag) goto loc_0050ACD4;
loc_0050ACB1:
    result = (v_stack_p20) + ((uint32_t)(0x1000ULL));
    local_r15 = (local_r15) + ((uint32_t)(0x1000ULL));
    v_stack_p20 = result;
    if (result != v_stack_m100) goto loc_0050AC6C;
    goto loc_0050AE1F;
loc_0050ACD4:
    local_r13 = 0;
loc_0050ACDB:
    result = (uint32_t)(*(uint32_t *)(local_rsi + 0x14));
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) == 0) {
        Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x14)));
        result = (uint32_t)(local_rdi);
        Arg1 = (Arg1) ^ (result);
        result = *(uint64_t *)(v_stack_p10 + 0x588);
        *(uint64_t *)(result + 0x18) = Arg1;
    }
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) != 0) goto loc_0050AE1F;
    result = (result) + (v_stack_p10);
    *(uint64_t *)(v_stack_p10 + 0x920) = result;
    result = (result) + (local_rsi);
    *(uint64_t *)(v_stack_p10 + 0x928) = result;
    *(uint64_t *)(v_stack_p10 + 0x938) = *(uint64_t *)(local_rsi + 0x8);
    *(uint64_t *)(v_stack_p10 + 0x930) = (int32_t)(*(uint32_t *)(local_rsi));
    *(uint32_t *)(v_stack_p10 + 0x918) = 1;
    if (condition_is_below) goto loc_0050AE1F;
    if (((*(uint32_t *)((uint32_t)(0x9DCULL) + v_stack_p10 * 1)) & (0x200000ULL)) == 0) goto loc_0050AE1F;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x9D8))))) == 0) goto loc_0050AE1F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0050ADCA;
loc_0050ADA9:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1)) ^ (*(uint64_t *)(v_stack_p10 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(v_stack_p10 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(v_stack_p10 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1) + (8);
loc_0050ADCA:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1 + Arg1 * 8)) goto loc_0050ADA9;
    if (a3 == (*(uint64_t *)(v_stack_p10 + 0xA80))) goto loc_0050AE1F;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x588)) = v_stack_p10;
    *(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x804)));
    result = *(uint64_t *)(v_stack_p10 + 0x588);
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) == 0) {
        result = *(uint64_t *)(v_stack_p10 + 0x588);
        Arg1 = (*(uint64_t *)(v_stack_p10 + 0xA80)) ^ (a3);
        *(uint64_t *)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(v_stack_p10, Arg2, a3, 256);
loc_0050AE1F:
    result = KeGuardDispatchICall(*(uint64_t *)(v_stack_p10 + 0x538), Arg2, a3, 256);
loc_0050AE5B:
loc_0050AE67:
    a4 = (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 16) + (8);
    a3 = (local_rsi + 24) + (8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 0x10)) != (*(uint64_t *)(local_rsi + 0x18))) goto loc_0050AEA3;
    Arg2 = (uint32_t)((24) + (-8));
    if (((uint32_t)(Arg2)) >= 8) goto loc_0050AE67;
    if ((uint32_t)(Arg2) == 0) goto loc_0050AEAC;
loc_0050AE8C:
    a4 = (a4) + (1);
    a3 = (a3) + (1);
    if (((uint8_t)(*(uint8_t *)(a4))) != ((uint8_t)(*(uint8_t *)(a3)))) goto loc_0050AEA3;
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_0050AE8C;
    goto loc_0050AEAC;
loc_0050AEA3:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 16) + (24);
    if (local_rdi < (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 16 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) * 2 * 8)) goto loc_0050AE5B;
loc_0050AEAC:
    result = KeGuardDispatchICall(*(uint64_t *)(v_stack_p10 + 0x538), Arg2, a3, a4);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 0xC)) == 0) goto loc_0050B003;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x9DC)))) & (16)) == 0) goto loc_0050AFF9;
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) != 0) goto loc_0050AFF9;
    result = ((uint8_t)((uint8_t)(v_cr8))) + (v_stack_p10);
    *(uint64_t *)(v_stack_p10 + 0x920) = result;
    result = (result) + (local_rsi);
    *(uint64_t *)(v_stack_p10 + 0x928) = result;
    *(uint64_t *)(v_stack_p10 + 0x930) = (int32_t)(*(uint32_t *)(local_rsi));
    *(uint64_t *)(v_stack_p10 + 0x938) = 1;
    *(uint32_t *)(v_stack_p10 + 0x918) = 1;
    if (condition_is_below) goto loc_0050AFF9;
    if (condition_is_above_or_equal) goto loc_0050AFF9;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x9D8))))) == 0) goto loc_0050AFF9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0050AFA2;
loc_0050AF81:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1)) ^ (*(uint64_t *)(v_stack_p10 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(v_stack_p10 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(v_stack_p10 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1) + (8);
loc_0050AFA2:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1 + Arg1 * 8)) goto loc_0050AF81;
    if (a3 == (*(uint64_t *)(v_stack_p10 + 0xA80))) goto loc_0050AFF9;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x588)) = v_stack_p10;
    *(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x804)));
    result = *(uint64_t *)(v_stack_p10 + 0x588);
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) == 0) {
        result = *(uint64_t *)(v_stack_p10 + 0x588);
        Arg1 = (*(uint64_t *)(v_stack_p10 + 0xA80)) ^ (a3);
        *(uint64_t *)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(v_stack_p10, Arg2, a3, 256);
loc_0050AFF9:
    if ((*(uint64_t *)(local_rsi + 0x18)) == 1) goto loc_0050B12C;
loc_0050B003:
    if (local_rdi != (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 16 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) * 2 * 8)) goto loc_0050B136;
    local_r13 = 0;
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) != 0) goto loc_0050B139;
    result = (result) + (v_stack_p10);
    *(uint64_t *)(v_stack_p10 + 0x920) = result;
    *(uint64_t *)(v_stack_p10 + 0x928) = local_rsi + local_r12 * 1;
    *(uint64_t *)(v_stack_p10 + 0x930) = (int32_t)(*(uint32_t *)(local_rsi));
    *(uint64_t *)(v_stack_p10 + 0x938) = local_rdi;
    *(uint32_t *)(v_stack_p10 + 0x918) = 1;
    if (condition_is_below) goto loc_0050B139;
    if (((*(uint32_t *)(v_stack_p10 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_0050B139;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x9D8))))) == 0) goto loc_0050B139;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0050B0D3;
loc_0050B0B2:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1)) ^ (*(uint64_t *)(v_stack_p10 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(v_stack_p10 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(v_stack_p10 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1) + (8);
loc_0050B0D3:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1 + Arg1 * 8)) goto loc_0050B0B2;
    if (a3 == (*(uint64_t *)(v_stack_p10 + 0xA80))) goto loc_0050B139;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x588)) = v_stack_p10;
    *(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x804)));
    result = *(uint64_t *)(v_stack_p10 + 0x588);
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) == 0) {
        result = *(uint64_t *)(v_stack_p10 + 0x588);
        Arg1 = (*(uint64_t *)(v_stack_p10 + 0xA80)) ^ (a3);
        *(uint64_t *)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(v_stack_p10, Arg2, a3, 256);
    goto loc_0050B139;
loc_0050B12C:
loc_0050B136:
    local_r13 = 0;
loc_0050B139:
    result = KeGuardDispatchICall(*(uint64_t *)(v_stack_p10 + 0x538), Arg2, a3, 256);
    goto loc_0050B1A0;
loc_0050B176:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 0x10 + 0x8)) < 0) goto loc_0050B1A9;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 0x10 + 0x8)) & (0xFFFFFFFFFFFFF000ULL);
    if (result != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 0x10 + 0x8))) goto loc_0050B1A9;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 0x10 + 0x10))) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 0x10 + 0x8));
    if (result <= (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 0x10 + 0x8))) goto loc_0050B1A9;
    if (result == 0) goto loc_0050B1A9;
loc_0050B1A0:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 16) + (24);
    if (local_rdi < (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 16 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) * 2 * 8)) goto loc_0050B176;
loc_0050B1A9:
    result = KeGuardDispatchICall(*(uint64_t *)(v_stack_p10 + 0x538), result, a3, 256);
    if (local_rdi == (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 16 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) * 2 * 8)) goto loc_0050B5BE;
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) != 0) goto loc_0050B5BE;
    result = ((uint8_t)((uint8_t)((uint8_t)(v_cr8)))) + (v_stack_p10);
    *(uint64_t *)(v_stack_p10 + 0x920) = result;
    *(uint64_t *)(v_stack_p10 + 0x928) = local_rsi + local_r12 * 1;
    *(uint64_t *)(v_stack_p10 + 0x930) = (int32_t)(*(uint32_t *)(local_rsi));
    *(uint64_t *)(v_stack_p10 + 0x938) = local_rdi;
    *(uint32_t *)(v_stack_p10 + 0x918) = 1;
    if (condition_is_below) goto loc_0050B5BE;
    if (((*(uint32_t *)(v_stack_p10 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_0050B5BE;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x9D8))))) == 0) goto loc_0050B5BE;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0050B28D;
loc_0050B26C:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1)) ^ (*(uint64_t *)(v_stack_p10 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(v_stack_p10 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(v_stack_p10 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1) + (8);
loc_0050B28D:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1 + Arg1 * 8)) goto loc_0050B26C;
    goto loc_0050B56C;
loc_0050B297:
    if (((uint32_t)(result)) > 43) goto loc_0050B5CB;
    if (((uint32_t)(result)) >= 43) goto loc_0050B5CB;
    result = KeGuardDispatchICall(*(uint64_t *)(v_stack_p10 + 0x538), Arg2, a3, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1 + Arg1 * 8);
loc_0050B2F0:
loc_0050B2FC:
    a4 = (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 16) + (8);
    a3 = (local_rsi + 24) + (8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 0x10)) != (*(uint64_t *)(local_rsi + 0x18))) goto loc_0050B338;
    Arg2 = (uint32_t)((24) + (-8));
    if (((uint32_t)(Arg2)) >= 8) goto loc_0050B2FC;
    if ((uint32_t)(Arg2) == 0) goto loc_0050B341;
loc_0050B321:
    a4 = (a4) + (1);
    a3 = (a3) + (1);
    if (((uint8_t)(*(uint8_t *)(a4))) != ((uint8_t)(*(uint8_t *)(a3)))) goto loc_0050B338;
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_0050B321;
    goto loc_0050B341;
loc_0050B338:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 16) + (24);
    if (local_rdi < (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 16 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) * 2 * 8)) goto loc_0050B2F0;
loc_0050B341:
    result = KeGuardDispatchICall(*(uint64_t *)(v_stack_p10 + 0x538), Arg2, a3, a4);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 0xC)) == 0) goto loc_0050B49B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x9DC)))) & (16)) == 0) goto loc_0050B491;
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) != 0) goto loc_0050B491;
    result = ((uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8))))) + (v_stack_p10);
    *(uint64_t *)(v_stack_p10 + 0x920) = result;
    result = (result) + (local_rsi);
    *(uint64_t *)(v_stack_p10 + 0x928) = result;
    *(uint64_t *)(v_stack_p10 + 0x930) = (int32_t)(*(uint32_t *)(local_rsi));
    *(uint64_t *)(v_stack_p10 + 0x938) = 1;
    *(uint32_t *)(v_stack_p10 + 0x918) = 1;
    if (condition_is_below) goto loc_0050B491;
    if (condition_is_above_or_equal) goto loc_0050B491;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x9D8))))) == 0) goto loc_0050B491;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0050B437;
loc_0050B416:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1)) ^ (*(uint64_t *)(v_stack_p10 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(v_stack_p10 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(v_stack_p10 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1) + (8);
loc_0050B437:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1 + Arg1 * 8)) goto loc_0050B416;
    if (a3 == (*(uint64_t *)(v_stack_p10 + 0xA80))) goto loc_0050B491;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x588)) = v_stack_p10;
    *(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x804)));
    result = *(uint64_t *)(v_stack_p10 + 0xA80);
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) == 0) {
        Arg1 = a3;
        Arg1 = (Arg1) ^ (*(uint64_t *)(v_stack_p10 + 0xA80));
        result = *(uint64_t *)(v_stack_p10 + 0x588);
        *(uint64_t *)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(v_stack_p10, Arg2, a3, 256);
loc_0050B491:
    if ((*(uint64_t *)(local_rsi + 0x18)) == 1) goto loc_0050B5BE;
loc_0050B49B:
    if (local_rdi != (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)) + 16 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x620)))) * 2 * 8)) goto loc_0050B5BE;
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) != 0) goto loc_0050B5BE;
    result = (result) + (v_stack_p10);
    *(uint64_t *)(v_stack_p10 + 0x920) = result;
    result = (result) + (local_rsi);
    *(uint64_t *)(v_stack_p10 + 0x928) = result;
    *(uint64_t *)(v_stack_p10 + 0x930) = (int32_t)(*(uint32_t *)(local_rsi));
    *(uint64_t *)(v_stack_p10 + 0x938) = local_rdi;
    *(uint32_t *)(v_stack_p10 + 0x918) = 1;
    if (condition_is_below) goto loc_0050B5BE;
    if (((*(uint32_t *)(v_stack_p10 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_0050B5BE;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x9D8))))) == 0) goto loc_0050B5BE;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_0050B567;
loc_0050B546:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1)) ^ (*(uint64_t *)(v_stack_p10 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(v_stack_p10 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(v_stack_p10 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1) + (8);
loc_0050B567:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xA74)) + v_stack_p10 * 1 + Arg1 * 8)) goto loc_0050B546;
loc_0050B56C:
    if (a3 == (*(uint64_t *)(v_stack_p10 + 0xA80))) goto loc_0050B5BE;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x588)) = v_stack_p10;
    *(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x804)));
    result = *(uint64_t *)(v_stack_p10 + 0x588);
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) == 0) {
        result = *(uint64_t *)(v_stack_p10 + 0x588);
        Arg1 = (*(uint64_t *)(v_stack_p10 + 0xA80)) ^ (a3);
        *(uint64_t *)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(v_stack_p10, Arg2, a3, 256);
loc_0050B5BE:
loc_0050B5CB:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p18)) + 1);
    v_stack_p18 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < (*(uint32_t *)(v_stack_p10 + 0x82C))) goto loc_0050A9A6;
    local_r10 = 0;
loc_0050B5E8:
    if ((*(uint32_t *)(v_stack_p10 + 0x918)) == 0) goto loc_0050BAA1;
    v_stack_mC0 = *(uint64_t *)(v_stack_p10 + 0x930);
    v_stack_mB8 = *(uint64_t *)(v_stack_p10 + 0x938);
    v_stack_m100 = *(uint64_t *)(v_stack_p10 + 0x928);
    v_stack_m118 = *(uint64_t *)(v_stack_p10 + 0x920);
    result = (uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8))));
    v_cr8 = (uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8))));
    if (((uint8_t)((uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8)))))) < 2) {
        result = (uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8))));
        v_cr8 = 2;
    }
    v_stack_mE8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(v_stack_p10 + 0x640) * 1);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x648) + *(uint64_t *)(gs_base + (0 + 0x20)) * 1)) + (*(uint64_t *)(v_stack_p10 + 0x788));
    v_stack_mD0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(v_stack_p10 + 0x658) * 1);
    if (v_stack_mF8 > (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(v_stack_p10 + 0x640) * 1))) goto loc_0050B696;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(v_stack_p10 + 0x640) * 1)) - ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x5FC)));
    if (v_stack_mF8 >= Arg1) goto loc_0050B6DA;
loc_0050B696:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(v_stack_p10 + 0x650) * 1)) == 0) goto loc_0050B6CA;
    if (v_stack_mF8 > Arg2) goto loc_0050B6CA;
    Arg1 = (Arg2) - ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x5F8)));
    if (v_stack_mF8 < Arg1) goto loc_0050B6CA;
    v_stack_mE8 = Arg2;
    goto loc_0050B6DA;
loc_0050B6CA:
    v_stack_mE8 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(v_stack_p10 + 0x658) * 1) + *(uint64_t *)(v_stack_p10 + 0x688) * 1);
loc_0050B6DA:
    if (((*(uint32_t *)(v_stack_p10 + 0x9D8)) & (0x4000000ULL)) != 0) goto loc_0050BC42;
    v_stack_mD8 = 0;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(v_stack_p10 + 0x658) * 1) + *(uint64_t *)(v_stack_p10 + 0x688) * 1);
    if (((*(uint32_t *)(v_stack_p10 + 0x9DC)) & (0x400000ULL)) == 0) {
        Arg1 = v_cr0;
        result = Arg1;
        v_stack_mD8 = Arg1;
        v_cr0 = result;
    }
    local_r15 = ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xAE8))) << (4);
    local_r15 = (local_r15) + (v_stack_p10 + 2800);
    v_stack_mC8 = local_r15;
    if ((*(uint32_t *)(v_stack_p10 + 0xAEC)) <= 0) goto loc_0050B778;
loc_0050B73F:
    *(uint64_t *)(*(uint64_t *)(local_r15)) = *(uint64_t *)(local_r15 + 0x8);
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_0050B763;
    result = (v_cr4) ^ (128);
    goto loc_0050B769;
loc_0050B763:
loc_0050B769:
    local_r11 = (local_r15) + (16);
    Arg2 = (uint32_t)((0) + ((uint32_t)(128 - 127)));
    if (((uint32_t)(Arg2)) < (*(uint32_t *)(v_stack_p10 + 0xAEC))) goto loc_0050B73F;
loc_0050B778:
    if ((v_stack_p10 + 2800) >= local_r15) goto loc_0050B98B;
loc_0050B78B:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xAF0 + 0x8)));
    if (((*(uint32_t *)(v_stack_p10 + 0x9DC)) & (0x400000ULL)) != 0) goto loc_0050B7E9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xAF0 + 0x8)))) < 8) goto loc_0050B7CB;
    a4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xAF0 + 0x8))))) >> (3);
loc_0050B7B5:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xAF0 + 0x8))))) + (-8));
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0xAF0)) = *(uint64_t *)(local_r11);
    Arg1 = (local_r11) + (8);
    a3 = (*(uint64_t *)(v_stack_p10 + 0xAF0)) + (8);
    a4 = (a4) - (128 - 127);
    if (condition_is_not_equal) goto loc_0050B7B5;
loc_0050B7CB:
    if ((uint32_t)(Arg2) == 0) goto loc_0050B960;
    a3 = (a3) - (Arg1);
loc_0050B7D6:
    *(uint8_t *)(a3 + Arg1 * 1) = (uint8_t)(*(uint8_t *)(Arg1));
    Arg1 = (Arg1) + (128 - 127);
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_0050B7D6;
    goto loc_0050B960;
loc_0050B7E9:
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xAF0 + 0x8)));
    Arg1 = (uint32_t)((a3) & (0xFFFULL));
    v_stack_mF0 = local_r11;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xAF0 + 0x8)) + 4095) + (Arg1);
    Arg2 = (Arg2) >> (12);
    if ((uint32_t)(Arg2) == 0) goto loc_0050B960;
    v_stack_mE0 = (uint32_t)((uint32_t)(Arg2));
loc_0050B822:
    result = (a3) >> (9);
    result = (result) & (*(uint64_t *)(v_stack_p10 + 0x930));
    result = (result) + (*(uint64_t *)(v_stack_p10 + 0x5D8));
loc_0050B84A:
    *(uint64_t *)(v_stack_m88) = result;
    result = (result) >> (9);
    result = (result) & (*(uint64_t *)(v_stack_p10 + 0x930));
    result = (result) + (*(uint64_t *)(v_stack_p10 + 0x5D8));
    Arg2 = (4) - (128 - 127);
    if (condition_is_not_equal) goto loc_0050B84A;
loc_0050B860:
    a4 = (uint32_t)((4) + (-1));
    if (condition_is_equal) goto loc_0050B875;
    Arg1 = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m58 + a4 * 8 - 0x30)))) >> (7));
    if ((((uint8_t)(128 - 127)) & ((uint8_t)(Arg1))) == 0) goto loc_0050B860;
loc_0050B875:
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m58 + a4 * 8 - 0x30))) | (98);
    *(uint64_t *)(*(uint64_t *)(v_stack_m58 + a4 * 8 - 0x30)) = result;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_0050B8A2;
    goto loc_0050B8A8;
loc_0050B8A2:
loc_0050B8A8:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(a3))) & (0xFFFULL));
    Arg2 = (uint32_t)(((uint32_t)(0x1000ULL)) - ((uint32_t)(Arg1)));
    a4 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xAF0 + 0x8))))));
    if (((uint32_t)(Arg2)) < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xAF0 + 0x8))))))) { a4 = (uint32_t)(Arg2); }
    if (((uint32_t)(a4)) < 8) goto loc_0050B8F8;
    local_rsi = ((uint32_t)((uint32_t)(a4))) >> (3);
loc_0050B8DF:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(a4))) + (-8));
    *(uint64_t *)(a3) = *(uint64_t *)(v_stack_mF0);
    Arg2 = (v_stack_mF0) + (8);
    local_r10 = (a3) + (8);
    local_rsi = (local_rsi) - (1);
    if (condition_is_not_equal) goto loc_0050B8DF;
loc_0050B8F8:
    if ((uint32_t)(local_rdi) == 0) goto loc_0050B90D;
    local_r10 = (local_r10) - (Arg2);
loc_0050B8FF:
    *(uint8_t *)(Arg2 + local_r10 * 1) = (uint8_t)(*(uint8_t *)(Arg2));
    Arg2 = (Arg2) + (1);
    local_rdi = (uint32_t)((local_rdi) + (-1));
    if (condition_is_not_equal) goto loc_0050B8FF;
loc_0050B90D:
    a3 = (a3) + ((uint32_t)((uint32_t)(a4)));
    local_rsi = (uint32_t)(((uint32_t)(v_stack_p18)) - ((uint32_t)(a4)));
    *(uint64_t *)(*(uint64_t *)(v_stack_m58 + a4 * 8 - 0x30)) = result;
    v_stack_p18 = (uint32_t)(local_rsi);
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_0050B93E;
    goto loc_0050B944;
loc_0050B93E:
loc_0050B944:
    if (((v_cr4) & (0x20080ULL)) != 0) goto loc_0050B822;
    local_r10 = 0;
loc_0050B960:
    local_r14 = (v_stack_p10 + 2800) + (16);
    local_r11 = (local_r11) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_p20))));
    if (local_r14 < v_stack_mC8) goto loc_0050B78B;
loc_0050B98B:
    if (((*(uint32_t *)(v_stack_p10 + 0x9DC)) & (0x400000ULL)) != 0) goto loc_0050B9AE;
    *(uint8_t *)(*(uint64_t *)(v_stack_p10 + 0x228)) = 195;
    goto loc_0050BC34;
loc_0050B9AE:
    v_stack_p10 = 195;
    result = (*(uint64_t *)(v_stack_p10 + 0x228)) >> (9);
    result = (result) & (v_cr4);
    result = (result) + (*(uint64_t *)(v_stack_p10 + 0x5D8));
loc_0050B9E1:
    *(uint64_t *)(v_stack_m68) = result;
    result = (result) >> (9);
    result = (result) & (local_r14);
    result = (result) + (*(uint64_t *)(v_stack_p10 + 0x5D8));
    local_r11 = (4) - (1);
    if (condition_is_not_equal) goto loc_0050B9E1;
    local_r15 = (uint32_t)((v_stack_mC8) | (0xFFFFFFFFULL));
loc_0050B9FB:
    local_r10 = (uint32_t)((4) + ((uint32_t)(local_r15)));
    if (condition_is_equal) goto loc_0050BA0F;
    Arg1 = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m58 + local_r10 * 8 - 0x10)))) >> (7));
    if (((1) & ((uint8_t)(Arg1))) == 0) goto loc_0050B9FB;
loc_0050BA0F:
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m58 + local_r10 * 8 - 0x10))) | (98);
    *(uint64_t *)(*(uint64_t *)(v_stack_m58 + local_r10 * 8 - 0x10)) = result;
    if ((((uint32_t)(0x20080ULL)) & (v_cr4)) == 0) goto loc_0050BA3A;
    Arg1 = (v_cr4) ^ (128);
    goto loc_0050BA40;
loc_0050BA3A:
loc_0050BA40:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p10 + 0x228)))) & (0xFFFULL));
    local_r10 = (uint32_t)(((uint32_t)(0x1000ULL)) - ((uint32_t)(Arg1)));
    Arg2 = 1;
    if (((uint32_t)(local_r10)) < 1) { Arg2 = (uint32_t)(local_r10); }
    if (((uint32_t)(Arg2)) < 8) goto loc_0050BA7E;
    local_r10 = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_0050BA68:
    Arg2 = (uint32_t)((Arg2) + (-8));
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x228)) = *(uint64_t *)(v_stack_p10);
    a4 = (v_stack_p10) + (8);
    a3 = (*(uint64_t *)(v_stack_p10 + 0x228)) + (8);
    local_r10 = (local_r10) - (1);
    if (condition_is_not_equal) goto loc_0050BA68;
loc_0050BA7E:
    local_r10 = 0;
    if ((uint32_t)(Arg2) == 0) goto loc_0050BC15;
    a3 = (a3) - (a4);
loc_0050BA8C:
    *(uint8_t *)(a4 + a3 * 1) = (uint8_t)(*(uint8_t *)(a4));
    a4 = (a4) + (1);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r15)));
    if (condition_is_equal) goto loc_0050BC15;
    goto loc_0050BA8C;
loc_0050BAA1:
    *(uint32_t *)(v_stack_p10 + 0xC4) = 0;
    if (v_stack_p10 >= (v_stack_p10 + 1584)) goto loc_0050BAE4;
loc_0050BAD8:
    result = (v_stack_p10) + (64);
    if (result < (v_stack_p10 + 1584)) goto loc_0050BAD8;
loc_0050BAE4:
loc_0050BAFA:
loc_0050BAFF:
    a3 = (*(uint64_t *)(v_stack_p10 + 0x838)) ^ (*(uint64_t *)(v_stack_p10));
    a3 = (a3) ^ (*(uint64_t *)(v_stack_p10 + 0x8));
    a4 = (v_stack_p10) + (16);
    result = (8) - (12 - 11);
    if (condition_is_not_equal) goto loc_0050BAFF;
    Arg1 = (a4) - (v_stack_p10);
    Arg1 = (Arg1) ^ (*(uint64_t *)(v_stack_p10 + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x834))) ^ (128));
    local_r10 = (uint32_t)((local_r10) ^ ((uint32_t)(Arg2)));
    local_r10 = (uint32_t)((local_r10) & (63));
    if (condition_is_equal) { local_r10 = (uint32_t)(12 - 11); }
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    local_rdi = (uint32_t)((12) + ((uint32_t)(Arg2)));
    if (condition_is_not_equal) goto loc_0050BAFA;
loc_0050BB53:
    a3 = (a3) ^ (*(uint64_t *)(a4));
    a4 = (a4) + (8);
    local_r14 = (uint32_t)(((uint32_t)(0x20080ULL)) + (-8));
    local_r15 = (local_r15) - (local_rdi + 1);
    if (condition_is_not_equal) goto loc_0050BB53;
    if ((uint32_t)(local_r14) == 0) goto loc_0050BB83;
loc_0050BB6E:
    a3 = (a3) ^ (*(uint8_t *)(a4));
    a4 = (a4) + (local_rdi + 1);
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(Arg2)));
    if (condition_is_not_equal) goto loc_0050BB6E;
loc_0050BB83:
    *(uint32_t *)(v_stack_p10 + 0xC4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0xC4)));
    *(uint64_t *)(v_stack_p10 + 0xA68) = a3;
    result = KeGuardDispatchICall(v_stack_m118, (uint32_t)((uint32_t)(local_rdi + 1)), a3, a4);
loc_0050BBA2:
    result = KiGetTrapFrameMode(v_stack_p8, (uint32_t)((uint32_t)(local_rdi + 1)), a3, a4);
    Arg1 = ((uint8_t)(result) != 0) ? 1 : 0;
    if ((uint8_t)(result) != 0) {
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x20));
        result = *(uint64_t *)(v_rip + 0xABAE81);
        Arg1 = *(uint64_t *)(result + 0x658);
        result = *(uint64_t *)(Arg2 + Arg1 * 1);
        Arg1 = (uint32_t)(local_r15);
        Arg1 = (condition_is_below) ? 1 : 0;
    }
    if ((*(uint8_t *)(v_rip + 0x8FEE39)) != ((uint8_t)(local_r15))) goto loc_0050BC00;
    if ((*(uint8_t *)(v_rip + 0xA3B9EF)) != ((uint8_t)(local_r15))) goto loc_0050BC00;
    if ((uint32_t)(Arg1) != 0) goto loc_0050BC00;
    result = KiReadKernelDr7(Arg1, Arg2, a3, a4);
    if (result != 0) {
        v_dr7 = result;
    }
    local_rsp = (local_rsp) + (280);
    return result;
loc_0050BC15:
    *(uint64_t *)(local_rdi + 0x1) = result;
    if (((local_r14) & (v_cr4)) == 0) goto loc_0050BC2E;
    result = (v_cr4) ^ (v_stack_m118);
    goto loc_0050BC34;
loc_0050BC2E:
loc_0050BC34:
loc_0050BC42:
    if ((*(uint32_t *)(v_stack_p10 + 0x948)) == ((uint32_t)(local_r10))) goto loc_0050BC60;
    result = v_cr8;
    if (((uint8_t)(v_cr8)) < 2) {
        result = v_cr8;
        v_cr8 = 2;
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x948))) == 0) goto loc_0050BD29;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x948))) - (1));
    if (condition_is_equal) goto loc_0050BD1C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0050BD13;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0050BD0A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0050BCCE;
    if (((uint32_t)(Arg1)) == 1) goto loc_0050BCA8;
    goto loc_0050BD29;
loc_0050BCA8:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x9D8))) >> (9));
    Arg2 = (uint32_t)((Arg2) & (31));
    goto loc_0050BD29;
loc_0050BCCE:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x9D8))) >> (9));
    a3 = (uint32_t)((a3) & (31));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x658) + *(uint64_t *)(gs_base + (0 + 0x20)) * 1)) + (*(uint64_t *)(v_stack_p10 + 0x6B8));
    goto loc_0050BD29;
loc_0050BD0A:
    goto loc_0050BD23;
loc_0050BD13:
    goto loc_0050BD23;
loc_0050BD1C:
loc_0050BD23:
loc_0050BD29:
    *(uint64_t *)(v_stack_mD0 + *(uint64_t *)(v_stack_p10 + 0x6A0) * 1) = local_r10;
    *(uint64_t *)(v_stack_mD0 + *(uint64_t *)(v_stack_p10 + 0x6B0) * 1) = local_r10;
    result = KeGuardCheckICall(*(uint64_t *)(v_stack_p10 + 0x168), *(uint64_t *)(Arg1 + *(uint64_t *)(v_stack_p10 + 0x698) * 1), a3, a4);
    result = (v_stack_p70) + (-8);
    v_stack_p30 = result;
    v_stack_p28 = *(uint64_t *)(v_stack_p10 + 0x168);
    v_stack_p20 = local_rdi;
    result = SdbpCheckDll(265, v_stack_p40, v_stack_p58, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0xC4)));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0050A5C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
