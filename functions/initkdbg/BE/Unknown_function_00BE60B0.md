# sub_00BE60B0

- RVA: `0x00BE60B0`–`0x00BE7AF0` (길이 `6,720` bytes)
- VA: `0x0000000140BE60B0`
- 실행 섹션: `INITKDBG`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2B84`
- 디코드: `1,756`개 명령, `6,720/6,720` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BE60EC` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE6172` → [sub_00BE7AF8](Unknown_function_00BE7AF8.md) (function, `0x00BE7AF8`)
- `0x00BE6216` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE6230` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE63ED` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE644A` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE657B` → [KeInitializeGate](../../text/49/KeInitializeGate_function_004953F8.md) (function, `0x004953F8`)
- `0x00BE65BE` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE6917` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE6BBF` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE6C30` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BE6C3F` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00BE6C62` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BE6DF6` → [sub_00BE8384](Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x00BE71BE` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE7229` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BE723B` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00BE725B` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BE72E2` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE757F` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE75F0` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BE75FF` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00BE7622` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BE7646` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BE777C` → [sub_00BE8384](Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x00BE79DC` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE7A47` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BE7A55` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00BE7A75` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BE7A9A` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (function, `0x002CA794`)
- `0x00BE7AEA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [sub_0050C0E0](../../text/50/Unknown_function_0050C0E0.md) at `0x00511AD5`
- [FsRtlMdlReadCompleteDevEx](../BD/FsRtlMdlReadCompleteDevEx_function_00BD1010.md) at `0x00BD7B42`
- [sub_00BE3A04](Unknown_function_00BE3A04.md) at `0x00BE45A5`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BF9EAD`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BFD5F9`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C00C14`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C118AD`

### Static image references
- `0x00BE6BF9` → RVA `0x00BF1290` (`INIT`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00BE657B` → [KeInitializeGate](../../text/49/KeInitializeGate_function_004953F8.md) (`INITKDBG` → `.text`)
  - `0x00BE6C30` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INITKDBG` → `.text`)
  - `0x00BE6C3F` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`INITKDBG` → `.text`)
  - `0x00BE6C62` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INITKDBG` → `.text`)
  - `0x00BE7229` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INITKDBG` → `.text`)
  - `0x00BE723B` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`INITKDBG` → `.text`)
  - `0x00BE725B` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INITKDBG` → `.text`)
  - `0x00BE75F0` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INITKDBG` → `.text`)
  - `0x00BE75FF` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`INITKDBG` → `.text`)
  - `0x00BE7622` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INITKDBG` → `.text`)
  - `0x00BE7646` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INITKDBG` → `.text`)
  - `0x00BE7A47` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INITKDBG` → `.text`)
  - `0x00BE7A55` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`INITKDBG` → `.text`)
  - `0x00BE7A75` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INITKDBG` → `.text`)
  - `0x00BE7A9A` → [KeWaitForGate](../../text/2C/KeWaitForGate_function_002CA794.md) (`INITKDBG` → `.text`)
  - `0x00BE7AEA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INITKDBG` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BE60B0  48 8B C4                        mov rax, rsp
00BE60B3  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
00BE60B7  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00BE60BB  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00BE60BF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00BE60C3  55                              push rbp
00BE60C4  56                              push rsi
00BE60C5  57                              push rdi
00BE60C6  41 54                           push r12
00BE60C8  41 55                           push r13
00BE60CA  41 56                           push r14
00BE60CC  41 57                           push r15
00BE60CE  48 8D A8 B8 FE FF FF            lea rbp, [rax - 0x148]
00BE60D5  48 81 EC 10 02 00 00            sub rsp, 0x210
00BE60DC  48 8B 39                        mov rdi, qword ptr [rcx]
00BE60DF  49 8B C9                        mov rcx, r9
00BE60E2  45 8B F0                        mov r14d, r8d
00BE60E5  48 8B 87 08 02 00 00            mov rax, qword ptr [rdi + 0x208]
00BE60EC  E8 6F 49 00 00                  call 0x140beaa60
00BE60F1  45 33 C9                        xor r9d, r9d
00BE60F4  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00BE60F9  48 85 C0                        test rax, rax
00BE60FC  0F 84 A4 19 00 00               je 0x140be7aa6
00BE6102  44 8B BF 04 08 00 00            mov r15d, dword ptr [rdi + 0x804]
00BE6109  45 8D 51 01                     lea r10d, [r9 + 1]
00BE610D  44 8B 87 44 09 00 00            mov r8d, dword ptr [rdi + 0x944]
00BE6114  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00BE611E  49 F7 E6                        mul r14
00BE6121  8B 85 70 01 00 00               mov eax, dword ptr [rbp + 0x170]
00BE6127  24 10                           and al, 0x10
00BE6129  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
00BE612E  48 8B CA                        mov rcx, rdx
00BE6131  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
00BE6136  48 C1 E9 03                     shr rcx, 3
00BE613A  F6 D8                           neg al
00BE613C  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
00BE6141  41 8D 47 30                     lea eax, [r15 + 0x30]
00BE6145  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00BE614A  45 1B E4                        sbb r12d, r12d
00BE614D  41 83 E4 2A                     and r12d, 0x2a
00BE6151  8D 34 8D 00 00 00 00            lea esi, [rcx*4]
00BE6158  45 03 E2                        add r12d, r10d
00BE615B  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
00BE615F  03 C6                           add eax, esi
00BE6161  3B 87 64 0A 00 00               cmp eax, dword ptr [rdi + 0xa64]
00BE6167  0F 86 E0 00 00 00               jbe 0x140be624d
00BE616D  8B D0                           mov edx, eax
00BE616F  48 8B CF                        mov rcx, rdi
00BE6172  E8 81 19 00 00                  call 0x140be7af8
00BE6177  45 33 C9                        xor r9d, r9d
00BE617A  48 8B D8                        mov rbx, rax
00BE617D  48 85 C0                        test rax, rax
00BE6180  75 0A                           jne 0x140be618c
00BE6182  B8 9A 00 00 C0                  mov eax, 0xc000009a
00BE6187  E9 1F 19 00 00                  jmp 0x140be7aab
00BE618C  8B 8F D8 09 00 00               mov ecx, dword ptr [rdi + 0x9d8]
00BE6192  F6 C1 02                        test cl, 2
00BE6195  0F 85 A3 00 00 00               jne 0x140be623e
00BE619B  8B 87 04 08 00 00               mov eax, dword ptr [rdi + 0x804]
00BE61A1  81 E1 00 00 00 10               and ecx, 0x10000000
00BE61A7  4C 8B 87 E8 07 00 00            mov r8, qword ptr [rdi + 0x7e8]
00BE61AE  F7 D9                           neg ecx
00BE61B0  41 BA 01 00 00 00               mov r10d, 1
00BE61B6  1B C9                           sbb ecx, ecx
00BE61B8  23 8F 44 09 00 00               and ecx, dword ptr [rdi + 0x944]
00BE61BE  83 F8 08                        cmp eax, 8
00BE61C1  72 15                           jb 0x140be61d8
00BE61C3  8B D0                           mov edx, eax
00BE61C5  48 C1 EA 03                     shr rdx, 3
00BE61C9  4C 89 0F                        mov qword ptr [rdi], r9
00BE61CC  83 C0 F8                        add eax, -8
00BE61CF  48 83 C7 08                     add rdi, 8
00BE61D3  49 2B D2                        sub rdx, r10
00BE61D6  75 F1                           jne 0x140be61c9
00BE61D8  85 C0                           test eax, eax
00BE61DA  74 0B                           je 0x140be61e7
00BE61DC  44 88 0F                        mov byte ptr [rdi], r9b
00BE61DF  49 03 FA                        add rdi, r10
00BE61E2  83 C0 FF                        add eax, -1
00BE61E5  75 F5                           jne 0x140be61dc
00BE61E7  8B BB 44 09 00 00               mov edi, dword ptr [rbx + 0x944]
00BE61ED  89 8B 44 09 00 00               mov dword ptr [rbx + 0x944], ecx
00BE61F3  83 F9 03                        cmp ecx, 3
00BE61F6  74 2E                           je 0x140be6226
00BE61F8  F7 83 D8 09 00 00 00 00 00 08   test dword ptr [rbx + 0x9d8], 0x8000000
00BE6202  75 19                           jne 0x140be621d
00BE6204  85 C9                           test ecx, ecx
00BE6206  74 15                           je 0x140be621d
00BE6208  48 8B 83 38 02 00 00            mov rax, qword ptr [rbx + 0x238]
00BE620F  49 8D 48 F8                     lea rcx, [r8 - 8]
00BE6213  48 8B 11                        mov rdx, qword ptr [rcx]
00BE6216  E8 45 48 00 00                  call 0x140beaa60
00BE621B  EB 18                           jmp 0x140be6235
00BE621D  48 8B 83 08 01 00 00            mov rax, qword ptr [rbx + 0x108]
00BE6224  EB 07                           jmp 0x140be622d
00BE6226  48 8B 83 68 03 00 00            mov rax, qword ptr [rbx + 0x368]
00BE622D  49 8B C8                        mov rcx, r8
00BE6230  E8 2B 48 00 00                  call 0x140beaa60
00BE6235  89 BB 44 09 00 00               mov dword ptr [rbx + 0x944], edi
00BE623B  45 33 C9                        xor r9d, r9d
00BE623E  83 A3 D8 09 00 00 FD            and dword ptr [rbx + 0x9d8], 0xfffffffd
00BE6245  41 BA 01 00 00 00               mov r10d, 1
00BE624B  EB 09                           jmp 0x140be6256
00BE624D  48 8B DF                        mov rbx, rdi
00BE6250  89 87 04 08 00 00               mov dword ptr [rdi + 0x804], eax
00BE6256  44 01 93 2C 08 00 00            add dword ptr [rbx + 0x82c], r10d
00BE625D  B9 30 00 00 00                  mov ecx, 0x30
00BE6262  4C 03 FB                        add r15, rbx
00BE6265  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
00BE626A  49 8B C7                        mov rax, r15
00BE626D  8D 51 D6                        lea edx, [rcx - 0x2a]
00BE6270  4C 89 08                        mov qword ptr [rax], r9
00BE6273  83 C1 F8                        add ecx, -8
00BE6276  48 83 C0 08                     add rax, 8
00BE627A  49 2B D2                        sub rdx, r10
00BE627D  75 F1                           jne 0x140be6270
00BE627F  85 C9                           test ecx, ecx
00BE6281  74 0B                           je 0x140be628e
00BE6283  44 88 08                        mov byte ptr [rax], r9b
00BE6286  49 03 C2                        add rax, r10
00BE6289  83 C1 FF                        add ecx, -1
00BE628C  75 F5                           jne 0x140be6283
00BE628E  48 8B 95 58 01 00 00            mov rdx, qword ptr [rbp + 0x158]
00BE6295  45 89 27                        mov dword ptr [r15], r12d
00BE6298  4C 8B CA                        mov r9, rdx
00BE629B  49 89 57 08                     mov qword ptr [r15 + 8], rdx
00BE629F  48 8B C2                        mov rax, rdx
00BE62A2  45 89 77 10                     mov dword ptr [r15 + 0x10], r14d
00BE62A6  44 01 B3 48 08 00 00            add dword ptr [rbx + 0x848], r14d
00BE62AD  4A 8D 0C 32                     lea rcx, [rdx + r14]
00BE62B1  44 8B 93 34 08 00 00            mov r10d, dword ptr [rbx + 0x834]
00BE62B8  48 8B BB 38 08 00 00            mov rdi, qword ptr [rbx + 0x838]
00BE62BF  48 3B D1                        cmp rdx, rcx
00BE62C2  73 0C                           jae 0x140be62d0
00BE62C4  0F 18 00                        prefetchnta byte ptr [rax]
00BE62C7  48 83 C0 40                     add rax, 0x40
00BE62CB  48 3B C1                        cmp rax, rcx
00BE62CE  72 F4                           jb 0x140be62c4
00BE62D0  45 8B DE                        mov r11d, r14d
00BE62D3  4C 8B C7                        mov r8, rdi
00BE62D6  41 C1 EB 07                     shr r11d, 7
00BE62DA  45 85 DB                        test r11d, r11d
00BE62DD  74 71                           je 0x140be6350
00BE62DF  48 8B B5 58 01 00 00            mov rsi, qword ptr [rbp + 0x158]
00BE62E6  41 BD 01 00 00 00               mov r13d, 1
00BE62EC  49 BF 01 20 00 04 80 00 10 70   movabs r15, 0x7010008004002001
00BE62F6  B8 08 00 00 00                  mov eax, 8
00BE62FB  4D 33 01                        xor r8, qword ptr [r9]
00BE62FE  41 8B CA                        mov ecx, r10d
00BE6301  49 D3 C0                        rol r8, cl
00BE6304  4D 33 41 08                     xor r8, qword ptr [r9 + 8]
00BE6308  49 83 C1 10                     add r9, 0x10
00BE630C  49 D3 C0                        rol r8, cl
00BE630F  49 2B C5                        sub rax, r13
00BE6312  75 E7                           jne 0x140be62fb
00BE6314  49 8B C9                        mov rcx, r9
00BE6317  48 2B CE                        sub rcx, rsi
00BE631A  48 33 CF                        xor rcx, rdi
00BE631D  48 8B C1                        mov rax, rcx
00BE6320  48 C1 C0 11                     rol rax, 0x11
00BE6324  48 33 C8                        xor rcx, rax
00BE6327  49 8B C7                        mov rax, r15
00BE632A  48 F7 E1                        mul rcx
00BE632D  33 C2                           xor eax, edx
00BE632F  48 89 95 B8 00 00 00            mov qword ptr [rbp + 0xb8], rdx
00BE6336  44 33 D0                        xor r10d, eax
00BE6339  41 83 E2 3F                     and r10d, 0x3f
00BE633D  45 0F 44 D5                     cmove r10d, r13d
00BE6341  41 83 C3 FF                     add r11d, -1
00BE6345  75 AF                           jne 0x140be62f6
00BE6347  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
00BE634B  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00BE6350  41 8B D6                        mov edx, r14d
00BE6353  41 BB 01 00 00 00               mov r11d, 1
00BE6359  83 E2 7F                        and edx, 0x7f
00BE635C  83 FA 08                        cmp edx, 8
00BE635F  72 1B                           jb 0x140be637c
00BE6361  8B C2                           mov eax, edx
00BE6363  48 C1 E8 03                     shr rax, 3
00BE6367  4D 33 01                        xor r8, qword ptr [r9]
00BE636A  41 8B CA                        mov ecx, r10d
00BE636D  49 D3 C0                        rol r8, cl
00BE6370  49 83 C1 08                     add r9, 8
00BE6374  83 C2 F8                        add edx, -8
00BE6377  49 2B C3                        sub rax, r11
00BE637A  75 EB                           jne 0x140be6367
00BE637C  85 D2                           test edx, edx
00BE637E  74 15                           je 0x140be6395
00BE6380  41 0F B6 01                     movzx eax, byte ptr [r9]
00BE6384  41 8B CA                        mov ecx, r10d
00BE6387  4C 33 C0                        xor r8, rax
00BE638A  4D 03 CB                        add r9, r11
00BE638D  49 D3 C0                        rol r8, cl
00BE6390  83 C2 FF                        add edx, -1
00BE6393  75 EB                           jne 0x140be6380
00BE6395  49 8B C0                        mov rax, r8
00BE6398  EB 03                           jmp 0x140be639d
00BE639A  44 33 C0                        xor r8d, eax
00BE639D  48 C1 E8 1F                     shr rax, 0x1f
00BE63A1  48 85 C0                        test rax, rax
00BE63A4  75 F4                           jne 0x140be639a
00BE63A6  48 8B 85 50 01 00 00            mov rax, qword ptr [rbp + 0x150]
00BE63AD  41 0F BA F0 1F                  btr r8d, 0x1f
00BE63B2  45 89 47 14                     mov dword ptr [r15 + 0x14], r8d
00BE63B6  44 01 B3 48 08 00 00            add dword ptr [rbx + 0x848], r14d
00BE63BD  4D 8D 77 18                     lea r14, [r15 + 0x18]
00BE63C1  41 BF 25 02 00 C0               mov r15d, 0xc0000225
00BE63C7  48 89 18                        mov qword ptr [rax], rbx
00BE63CA  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
00BE63D1  44 0F 20 C0                     mov rax, cr8
00BE63D5  48 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], rax
00BE63DC  41 BD 0F 00 00 00               mov r13d, 0xf
00BE63E2  45 0F 22 C5                     mov cr8, r13
00BE63E6  48 8B 83 60 01 00 00            mov rax, qword ptr [rbx + 0x160]
00BE63ED  E8 6E 46 00 00                  call 0x140beaa60
00BE63F2  48 8B 83 20 06 00 00            mov rax, qword ptr [rbx + 0x620]
00BE63F9  41 8D 7D 09                     lea edi, [r13 + 9]
00BE63FD  48 8B 08                        mov rcx, qword ptr [rax]
00BE6400  8B 01                           mov eax, dword ptr [rcx]
00BE6402  48 8D 51 10                     lea rdx, [rcx + 0x10]
00BE6406  48 8D 0C 40                     lea rcx, [rax + rax*2]
00BE640A  48 8D 04 CA                     lea rax, [rdx + rcx*8]
00BE640E  48 8B 8D 68 01 00 00            mov rcx, qword ptr [rbp + 0x168]
00BE6415  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
00BE6419  74 0A                           je 0x140be6425
00BE641B  48 03 D7                        add rdx, rdi
00BE641E  48 3B D0                        cmp rdx, rax
00BE6421  72 F2                           jb 0x140be6415
00BE6423  EB 17                           jmp 0x140be643c
00BE6425  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00BE6428  33 C9                           xor ecx, ecx
00BE642A  44 8B F9                        mov r15d, ecx
00BE642D  41 0F 11 06                     movups xmmword ptr [r14], xmm0
00BE6431  F2 0F 10 4A 10                  movsd xmm1, qword ptr [rdx + 0x10]
00BE6436  F2 41 0F 11 4E 10               movsd qword ptr [r14 + 0x10], xmm1
00BE643C  48 8B 8B 38 05 00 00            mov rcx, qword ptr [rbx + 0x538]
00BE6443  48 8B 83 A0 01 00 00            mov rax, qword ptr [rbx + 0x1a0]
00BE644A  E8 11 46 00 00                  call 0x140beaa60
00BE644F  0F B6 85 50 01 00 00            movzx eax, byte ptr [rbp + 0x150]
00BE6456  44 0F 22 C0                     mov cr8, rax
00BE645A  33 D2                           xor edx, edx
00BE645C  41 BA F8 FF FF FF               mov r10d, 0xfffffff8
00BE6462  44 8D 42 01                     lea r8d, [rdx + 1]
00BE6466  45 85 FF                        test r15d, r15d
00BE6469  79 44                           jns 0x140be64af
00BE646B  49 8B C6                        mov rax, r14
00BE646E  8D 4A 03                        lea ecx, [rdx + 3]
00BE6471  48 89 10                        mov qword ptr [rax], rdx
00BE6474  41 03 FA                        add edi, r10d
00BE6477  48 83 C0 08                     add rax, 8
00BE647B  49 2B C8                        sub rcx, r8
00BE647E  75 F1                           jne 0x140be6471
00BE6480  85 FF                           test edi, edi
00BE6482  74 0A                           je 0x140be648e
00BE6484  88 10                           mov byte ptr [rax], dl
00BE6486  49 03 C0                        add rax, r8
00BE6489  83 C7 FF                        add edi, -1
00BE648C  75 F6                           jne 0x140be6484
00BE648E  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00BE6493  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
00BE6498  48 8B BD 68 01 00 00            mov rdi, qword ptr [rbp + 0x168]
00BE649F  48 89 79 20                     mov qword ptr [rcx + 0x20], rdi
00BE64A3  41 8B 47 50                     mov eax, dword ptr [r15 + 0x50]
00BE64A7  89 41 28                        mov dword ptr [rcx + 0x28], eax
00BE64AA  4D 89 06                        mov qword ptr [r14], r8
00BE64AD  EB 11                           jmp 0x140be64c0
00BE64AF  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00BE64B4  48 8B BD 68 01 00 00            mov rdi, qword ptr [rbp + 0x168]
00BE64BB  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
00BE64C0  48 8D 41 30                     lea rax, [rcx + 0x30]
00BE64C4  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00BE64C9  83 FE 08                        cmp esi, 8
00BE64CC  72 19                           jb 0x140be64e7
00BE64CE  8B CE                           mov ecx, esi
00BE64D0  48 C1 E9 03                     shr rcx, 3
00BE64D4  48 C7 00 FF FF FF FF            mov qword ptr [rax], 0xffffffffffffffff
00BE64DB  41 03 F2                        add esi, r10d
00BE64DE  48 83 C0 08                     add rax, 8
00BE64E2  49 2B C8                        sub rcx, r8
00BE64E5  75 ED                           jne 0x140be64d4
00BE64E7  41 83 C9 FF                     or r9d, 0xffffffff
00BE64EB  85 F6                           test esi, esi
00BE64ED  74 0B                           je 0x140be64fa
00BE64EF  C6 00 FF                        mov byte ptr [rax], 0xff
00BE64F2  49 03 C0                        add rax, r8
00BE64F5  41 03 F1                        add esi, r9d
00BE64F8  75 F5                           jne 0x140be64ef
00BE64FA  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00BE64FE  8B F2                           mov esi, edx
00BE6500  4C 8B B5 58 01 00 00            mov r14, qword ptr [rbp + 0x158]
00BE6507  44 89 4C 24 3C                  mov dword ptr [rsp + 0x3c], r9d
00BE650C  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
00BE6510  48 8D 0C 40                     lea rcx, [rax + rax*2]
00BE6514  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
00BE6519  8B 83 DC 09 00 00               mov eax, dword ptr [rbx + 0x9dc]
00BE651F  49 8D 0C 8E                     lea rcx, [r14 + rcx*4]
00BE6523  A8 40                           test al, 0x40
00BE6525  48 89 8D B0 00 00 00            mov qword ptr [rbp + 0xb0], rcx
00BE652C  B8 F7 FF FF FF                  mov eax, 0xfffffff7
00BE6531  0F 45 85 70 01 00 00            cmovne eax, dword ptr [rbp + 0x170]
00BE6538  89 45 08                        mov dword ptr [rbp + 8], eax
00BE653B  4C 3B F1                        cmp r14, rcx
00BE653E  75 19                           jne 0x140be6559
00BE6540  48 8B 85 78 01 00 00            mov rax, qword ptr [rbp + 0x178]
00BE6547  89 10                           mov dword ptr [rax], edx
00BE6549  48 8B 85 80 01 00 00            mov rax, qword ptr [rbp + 0x180]
00BE6550  89 10                           mov dword ptr [rax], edx
00BE6552  33 C0                           xor eax, eax
00BE6554  E9 52 15 00 00                  jmp 0x140be7aab
00BE6559  F7 83 D8 09 00 00 00 00 10 00   test dword ptr [rbx + 0x9d8], 0x100000
00BE6563  75 1D                           jne 0x140be6582
00BE6565  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00BE6569  C7 85 50 01 00 00 00 04 00 00   mov dword ptr [rbp + 0x150], 0x400
00BE6573  48 89 5D 80                     mov qword ptr [rbp - 0x80], rbx
00BE6577  48 89 55 A0                     mov qword ptr [rbp - 0x60], rdx
00BE657B  E8 78 EE 8A FF                  call 0x1404953f8
00BE6580  EB 2C                           jmp 0x140be65ae
00BE6582  89 95 50 01 00 00               mov dword ptr [rbp + 0x150], edx
00BE6588  48 8D 45 80                     lea rax, [rbp - 0x80]
00BE658C  B9 78 00 00 00                  mov ecx, 0x78
00BE6591  48 89 10                        mov qword ptr [rax], rdx
00BE6594  41 03 CA                        add ecx, r10d
00BE6597  48 83 C0 08                     add rax, 8
00BE659B  4D 2B E8                        sub r13, r8
00BE659E  75 F1                           jne 0x140be6591
00BE65A0  85 C9                           test ecx, ecx
00BE65A2  74 0A                           je 0x140be65ae
00BE65A4  88 10                           mov byte ptr [rax], dl
00BE65A6  49 03 C0                        add rax, r8
00BE65A9  41 03 C9                        add ecx, r9d
00BE65AC  75 F6                           jne 0x140be65a4
00BE65AE  48 8B 83 20 02 00 00            mov rax, qword ptr [rbx + 0x220]
00BE65B5  48 8B D7                        mov rdx, rdi
00BE65B8  45 8B 06                        mov r8d, dword ptr [r14]
00BE65BB  49 8B CF                        mov rcx, r15
00BE65BE  E8 9D 44 00 00                  call 0x140beaa60
00BE65C3  4C 8B D8                        mov r11, rax
00BE65C6  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00BE65CB  41 8B C4                        mov eax, r12d
00BE65CE  33 D2                           xor edx, edx
00BE65D0  48 89 85 A8 00 00 00            mov qword ptr [rbp + 0xa8], rax
00BE65D7  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
00BE65E1  BF 44 50 77 72                  mov edi, 0x72775044
00BE65E6  41 BC 43 63 42 63               mov r12d, 0x63426343
00BE65EC  41 BA 4F 62 44 69               mov r10d, 0x6944624f
00BE65F2  41 BD 46 4F 43 58               mov r13d, 0x58434f46
00BE65F8  41 BF 4E 74 46 57               mov r15d, 0x5746744e
00BE65FE  4D 85 DB                        test r11, r11
00BE6601  0F 84 5F 10 00 00               je 0x140be7666
00BE6607  41 F7 43 24 00 00 00 02         test dword ptr [r11 + 0x24], 0x2000000
00BE660F  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00BE6613  75 40                           jne 0x140be6655
00BE6615  41 8B 0B                        mov ecx, dword ptr [r11]
00BE6618  49 8D 43 04                     lea rax, [r11 + 4]
00BE661C  81 F9 49 4E 49 54               cmp ecx, 0x54494e49
00BE6622  75 08                           jne 0x140be662c
00BE6624  81 38 4B 44 42 47               cmp dword ptr [rax], 0x4742444b
00BE662A  74 29                           je 0x140be6655
00BE662C  81 F9 50 41 47 45               cmp ecx, 0x45474150
00BE6632  75 2F                           jne 0x140be6663
00BE6634  0F B7 08                        movzx ecx, word ptr [rax]
00BE6637  B8 77 78 00 00                  mov eax, 0x7877
00BE663C  66 3B C8                        cmp cx, ax
00BE663F  74 14                           je 0x140be6655
00BE6641  B8 77 72 00 00                  mov eax, 0x7277
00BE6646  66 3B C8                        cmp cx, ax
00BE6649  74 0A                           je 0x140be6655
00BE664B  B8 77 77 00 00                  mov eax, 0x7777
00BE6650  66 3B C8                        cmp cx, ax
00BE6653  75 20                           jne 0x140be6675
00BE6655  41 B8 01 00 00 00               mov r8d, 1
00BE665B  45 8B C8                        mov r9d, r8d
00BE665E  E9 FE 00 00 00                  jmp 0x140be6761
00BE6663  81 F9 45 52 52 41               cmp ecx, 0x41525245
00BE6669  75 0A                           jne 0x140be6675
00BE666B  B9 54 41 00 00                  mov ecx, 0x4154
00BE6670  66 39 08                        cmp word ptr [rax], cx
00BE6673  74 E0                           je 0x140be6655
00BE6675  48 8B 93 50 09 00 00            mov rdx, qword ptr [rbx + 0x950]
00BE667C  41 BB 07 00 00 00               mov r11d, 7
00BE6682  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
00BE6687  4C 8B 8B 58 09 00 00            mov r9, qword ptr [rbx + 0x958]
00BE668E  4C 2B C2                        sub r8, rdx
00BE6691  4C 8B 93 60 09 00 00            mov r10, qword ptr [rbx + 0x960]
00BE6698  48 8B BB 68 09 00 00            mov rdi, qword ptr [rbx + 0x968]
00BE669F  41 8A 0C 10                     mov cl, byte ptr [r8 + rdx]
00BE66A3  8A 02                           mov al, byte ptr [rdx]
00BE66A5  48 FF C2                        inc rdx
00BE66A8  3A C8                           cmp cl, al
00BE66AA  75 10                           jne 0x140be66bc
00BE66AC  41 83 C3 FF                     add r11d, -1
00BE66B0  75 ED                           jne 0x140be669f
00BE66B2  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
00BE66B7  E9 87 00 00 00                  jmp 0x140be6743
00BE66BC  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
00BE66C1  BA 08 00 00 00                  mov edx, 8
00BE66C6  4D 8B C3                        mov r8, r11
00BE66C9  49 8B 08                        mov rcx, qword ptr [r8]
00BE66CC  49 83 C0 08                     add r8, 8
00BE66D0  49 8B 01                        mov rax, qword ptr [r9]
00BE66D3  49 83 C1 08                     add r9, 8
00BE66D7  48 3B C8                        cmp rcx, rax
00BE66DA  75 23                           jne 0x140be66ff
00BE66DC  83 C2 F8                        add edx, -8
00BE66DF  83 FA 08                        cmp edx, 8
00BE66E2  73 E5                           jae 0x140be66c9
00BE66E4  85 D2                           test edx, edx
00BE66E6  74 5B                           je 0x140be6743
00BE66E8  41 8A 08                        mov cl, byte ptr [r8]
00BE66EB  49 FF C0                        inc r8
00BE66EE  41 8A 01                        mov al, byte ptr [r9]
00BE66F1  49 FF C1                        inc r9
00BE66F4  3A C8                           cmp cl, al
00BE66F6  75 07                           jne 0x140be66ff
00BE66F8  83 C2 FF                        add edx, -1
00BE66FB  75 EB                           jne 0x140be66e8
00BE66FD  EB 44                           jmp 0x140be6743
00BE66FF  41 B8 04 00 00 00               mov r8d, 4
00BE6705  49 8B D3                        mov rdx, r11
00BE6708  49 2B D2                        sub rdx, r10
00BE670B  45 8D 48 FD                     lea r9d, [r8 - 3]
00BE670F  41 8A 0C 12                     mov cl, byte ptr [r10 + rdx]
00BE6713  41 8A 02                        mov al, byte ptr [r10]
00BE6716  4D 03 D1                        add r10, r9
00BE6719  3A C8                           cmp cl, al
00BE671B  75 08                           jne 0x140be6725
00BE671D  41 83 C0 FF                     add r8d, -1
00BE6721  75 EC                           jne 0x140be670f
00BE6723  EB 1E                           jmp 0x140be6743
00BE6725  49 8B D3                        mov rdx, r11
00BE6728  41 B8 06 00 00 00               mov r8d, 6
00BE672E  48 2B D7                        sub rdx, rdi
00BE6731  8A 0C 17                        mov cl, byte ptr [rdi + rdx]
00BE6734  8A 07                           mov al, byte ptr [rdi]
00BE6736  49 03 F9                        add rdi, r9
00BE6739  3A C8                           cmp cl, al
00BE673B  75 11                           jne 0x140be674e
00BE673D  41 83 C0 FF                     add r8d, -1
00BE6741  75 EE                           jne 0x140be6731
00BE6743  41 B8 01 00 00 00               mov r8d, 1
00BE6749  45 8B C8                        mov r9d, r8d
00BE674C  EB 0B                           jmp 0x140be6759
00BE674E  44 8B 4C 24 38                  mov r9d, dword ptr [rsp + 0x38]
00BE6753  41 B8 01 00 00 00               mov r8d, 1
00BE6759  41 BA 4F 62 44 69               mov r10d, 0x6944624f
00BE675F  33 D2                           xor edx, edx
00BE6761  41 8B 43 24                     mov eax, dword ptr [r11 + 0x24]
00BE6765  85 C0                           test eax, eax
00BE6767  45 0F 48 C8                     cmovs r9d, r8d
00BE676B  48 83 BD A8 00 00 00 2B         cmp qword ptr [rbp + 0xa8], 0x2b
00BE6773  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
00BE6778  75 10                           jne 0x140be678a
00BE677A  0F BA E0 1D                     bt eax, 0x1d
00BE677E  72 0A                           jb 0x140be678a
00BE6780  45 8B C8                        mov r9d, r8d
00BE6783  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00BE6788  EB 05                           jmp 0x140be678f
00BE678A  45 85 C9                        test r9d, r9d
00BE678D  74 26                           je 0x140be67b5
00BE678F  41 81 3B 49 4E 49 54            cmp dword ptr [r11], 0x54494e49
00BE6796  75 1D                           jne 0x140be67b5
00BE6798  41 81 7B 04 4B 44 42 47         cmp dword ptr [r11 + 4], 0x4742444b
00BE67A0  75 13                           jne 0x140be67b5
00BE67A2  F7 83 DC 09 00 00 00 20 00 00   test dword ptr [rbx + 0x9dc], 0x2000
00BE67AC  44 0F 45 CA                     cmovne r9d, edx
00BE67B0  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
00BE67B5  41 8B 53 10                     mov edx, dword ptr [r11 + 0x10]
00BE67B9  41 8B 43 08                     mov eax, dword ptr [r11 + 8]
00BE67BD  3B D0                           cmp edx, eax
00BE67BF  41 8B 4B 0C                     mov ecx, dword ptr [r11 + 0xc]
00BE67C3  0F 46 D0                        cmovbe edx, eax
00BE67C6  03 D1                           add edx, ecx
00BE67C8  89 55 34                        mov dword ptr [rbp + 0x34], edx
00BE67CB  EB 06                           jmp 0x140be67d3
00BE67CD  41 B8 01 00 00 00               mov r8d, 1
00BE67D3  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00BE67D7  8B 54 24 3C                     mov edx, dword ptr [rsp + 0x3c]
00BE67DB  41 84 C0                        test r8b, al
00BE67DE  75 23                           jne 0x140be6803
00BE67E0  3B C2                           cmp eax, edx
00BE67E2  44 8B C0                        mov r8d, eax
00BE67E5  44 0F 43 C2                     cmovae r8d, edx
00BE67E9  44 89 44 24 3C                  mov dword ptr [rsp + 0x3c], r8d
00BE67EE  3B 44 24 34                     cmp eax, dword ptr [rsp + 0x34]
00BE67F2  76 09                           jbe 0x140be67fd
00BE67F4  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00BE67F8  44 89 44 24 3C                  mov dword ptr [rsp + 0x3c], r8d
00BE67FD  41 B8 01 00 00 00               mov r8d, 1
00BE6803  41 8B 06                        mov eax, dword ptr [r14]
00BE6806  45 33 DB                        xor r11d, r11d
00BE6809  45 8B 76 04                     mov r14d, dword ptr [r14 + 4]
00BE680D  8B F8                           mov edi, eax
00BE680F  48 03 BD 68 01 00 00            add rdi, qword ptr [rbp + 0x168]
00BE6816  44 2B F0                        sub r14d, eax
00BE6819  48 83 BD A8 00 00 00 2B         cmp qword ptr [rbp + 0xa8], 0x2b
00BE6821  0F 85 1F 01 00 00               jne 0x140be6946
00BE6827  45 85 C9                        test r9d, r9d
00BE682A  0F 85 1F 01 00 00               jne 0x140be694f
00BE6830  2B C8                           sub ecx, eax
00BE6832  83 F9 06                        cmp ecx, 6
00BE6835  0F 82 14 01 00 00               jb 0x140be694f
00BE683B  2B C6                           sub eax, esi
00BE683D  83 F8 06                        cmp eax, 6
00BE6840  0F 82 09 01 00 00               jb 0x140be694f
00BE6846  8A 47 FF                        mov al, byte ptr [rdi - 1]
00BE6849  80 7F FA 4C                     cmp byte ptr [rdi - 6], 0x4c
00BE684D  0F 85 FC 00 00 00               jne 0x140be694f
00BE6853  80 7F FB 87                     cmp byte ptr [rdi - 5], 0x87
00BE6857  0F 85 F2 00 00 00               jne 0x140be694f
00BE685D  44 38 5F FC                     cmp byte ptr [rdi - 4], r11b
00BE6861  0F 85 E8 00 00 00               jne 0x140be694f
00BE6867  80 7F FD 98                     cmp byte ptr [rdi - 3], 0x98
00BE686B  0F 85 DE 00 00 00               jne 0x140be694f
00BE6871  80 7F FE C3                     cmp byte ptr [rdi - 2], 0xc3
00BE6875  0F 85 D4 00 00 00               jne 0x140be694f
00BE687B  3C 90                           cmp al, 0x90
00BE687D  74 08                           je 0x140be6887
00BE687F  3C F1                           cmp al, 0xf1
00BE6881  0F 85 C8 00 00 00               jne 0x140be694f
00BE6887  F6 45 08 08                     test byte ptr [rbp + 8], 8
00BE688B  0F 84 8D 05 00 00               je 0x140be6e1e
00BE6891  48 8B C7                        mov rax, rdi
00BE6894  41 8B D6                        mov edx, r14d
00BE6897  41 B9 FF 0F 00 00               mov r9d, 0xfff
00BE689D  49 8D 8E FF 0F 00 00            lea rcx, [r14 + 0xfff]
00BE68A4  49 23 C1                        and rax, r9
00BE68A7  48 03 C8                        add rcx, rax
00BE68AA  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00BE68B1  48 81 F9 00 10 00 00            cmp rcx, 0x1000
00BE68B8  75 14                           jne 0x140be68ce
00BE68BA  48 8B C7                        mov rax, rdi
00BE68BD  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
00BE68C3  48 3B 44 24 70                  cmp rax, qword ptr [rsp + 0x70]
00BE68C8  0F 84 50 05 00 00               je 0x140be6e1e
00BE68CE  45 85 F6                        test r14d, r14d
00BE68D1  0F 84 F1 03 00 00               je 0x140be6cc8
00BE68D7  8B 83 DC 09 00 00               mov eax, dword ptr [rbx + 0x9dc]
00BE68DD  A8 40                           test al, 0x40
00BE68DF  0F 84 E3 03 00 00               je 0x140be6cc8
00BE68E5  45 0F 20 C7                     mov r15, cr8
00BE68E9  48 8B F7                        mov rsi, rdi
00BE68EC  4C 8D 6F FF                     lea r13, [rdi - 1]
00BE68F0  48 81 E6 00 F0 FF FF            and rsi, 0xfffffffffffff000
00BE68F7  4C 03 EA                        add r13, rdx
00BE68FA  4D 0B E9                        or r13, r9
00BE68FD  4C 8D 66 FF                     lea r12, [rsi - 1]
00BE6901  B8 02 00 00 00                  mov eax, 2
00BE6906  44 0F 22 C0                     mov cr8, rax
00BE690A  48 8B 83 68 04 00 00            mov rax, qword ptr [rbx + 0x468]
00BE6911  41 8B D0                        mov edx, r8d
00BE6914  48 8B CE                        mov rcx, rsi
00BE6917  E8 44 41 00 00                  call 0x140beaa60
00BE691C  3D 2D 02 00 C0                  cmp eax, 0xc000022d
00BE6921  0F 85 6D 03 00 00               jne 0x140be6c94
00BE6927  41 B8 01 00 00 00               mov r8d, 1
00BE692D  45 3A F8                        cmp r15b, r8b
00BE6930  0F 87 69 03 00 00               ja 0x140be6c9f
00BE6936  41 0F B6 C7                     movzx eax, r15b
00BE693A  44 0F 22 C0                     mov cr8, rax
00BE693E  8A 06                           mov al, byte ptr [rsi]
00BE6940  44 0F 20 C0                     mov rax, cr8
00BE6944  EB BB                           jmp 0x140be6901
00BE6946  45 85 C9                        test r9d, r9d
00BE6949  0F 84 38 FF FF FF               je 0x140be6887
00BE694F  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
00BE6953  85 F6                           test esi, esi
00BE6955  0F 84 25 03 00 00               je 0x140be6c80
00BE695B  0F 31                           rdtsc
00BE695D  48 C1 E2 20                     shl rdx, 0x20
00BE6961  49 B9 01 20 00 04 80 00 10 70   movabs r9, 0x7010008004002001
00BE696B  48 0B C2                        or rax, rdx
00BE696E  48 8B C8                        mov rcx, rax
00BE6971  48 8B D0                        mov rdx, rax
00BE6974  48 C1 C9 03                     ror rcx, 3
00BE6978  49 8B C1                        mov rax, r9
00BE697B  48 33 D1                        xor rdx, rcx
00BE697E  48 F7 E2                        mul rdx
00BE6981  4C 8B C2                        mov r8, rdx
00BE6984  48 89 95 C0 00 00 00            mov qword ptr [rbp + 0xc0], rdx
00BE698B  4C 33 C0                        xor r8, rax
00BE698E  48 B8 A3 8B 2E BA E8 A2 8B 2E   movabs rax, 0x2e8ba2e8ba2e8ba3
00BE6998  49 F7 E0                        mul r8
00BE699B  48 D1 EA                        shr rdx, 1
00BE699E  48 6B C2 0B                     imul rax, rdx, 0xb
00BE69A2  4C 2B C0                        sub r8, rax
00BE69A5  41 83 F8 05                     cmp r8d, 5
00BE69A9  0F 87 CD 00 00 00               ja 0x140be6a7c
00BE69AF  0F 84 AD 00 00 00               je 0x140be6a62
00BE69B5  41 8B C0                        mov eax, r8d
00BE69B8  45 85 C0                        test r8d, r8d
00BE69BB  0F 84 86 00 00 00               je 0x140be6a47
00BE69C1  83 E8 01                        sub eax, 1
00BE69C4  74 62                           je 0x140be6a28
00BE69C6  83 E8 01                        sub eax, 1
00BE69C9  74 41                           je 0x140be6a0c
00BE69CB  83 F8 01                        cmp eax, 1
00BE69CE  74 19                           je 0x140be69e9
00BE69D0  41 8B C8                        mov ecx, r8d
00BE69D3  B8 46 49 76 70                  mov eax, 0x70764946
00BE69D8  D3 C8                           ror eax, cl
00BE69DA  89 85 88 00 00 00               mov dword ptr [rbp + 0x88], eax
00BE69E0  44 8B 8D 88 00 00 00            mov r9d, dword ptr [rbp + 0x88]
00BE69E7  EB 56                           jmp 0x140be6a3f
00BE69E9  41 8D 40 02                     lea eax, [r8 + 2]
00BE69ED  8D 0C 40                        lea ecx, [rax + rax*2]
00BE69F0  B8 44 50 77 72                  mov eax, 0x72775044
00BE69F5  D3 C0                           rol eax, cl
00BE69F7  41 33 C0                        xor eax, r8d
00BE69FA  89 85 8C 00 00 00               mov dword ptr [rbp + 0x8c], eax
00BE6A00  44 8B 8D 8C 00 00 00            mov r9d, dword ptr [rbp + 0x8c]
00BE6A07  E9 9B 01 00 00                  jmp 0x140be6ba7
00BE6A0C  41 8B C8                        mov ecx, r8d
00BE6A0F  B8 43 64 6D 61                  mov eax, 0x616d6443
00BE6A14  D3 C0                           rol eax, cl
00BE6A16  89 85 90 00 00 00               mov dword ptr [rbp + 0x90], eax
00BE6A1C  44 8B 8D 90 00 00 00            mov r9d, dword ptr [rbp + 0x90]
00BE6A23  E9 82 01 00 00                  jmp 0x140be6baa
00BE6A28  41 8B C8                        mov ecx, r8d
00BE6A2B  B8 43 63 5A 65                  mov eax, 0x655a6343
00BE6A30  D3 C8                           ror eax, cl
00BE6A32  89 85 94 00 00 00               mov dword ptr [rbp + 0x94], eax
00BE6A38  44 8B 8D 94 00 00 00            mov r9d, dword ptr [rbp + 0x94]
00BE6A3F  41 D3 C1                        rol r9d, cl
00BE6A42  E9 66 01 00 00                  jmp 0x140be6bad
00BE6A47  41 8D 40 02                     lea eax, [r8 + 2]
00BE6A4B  8D 0C 40                        lea ecx, [rax + rax*2]
00BE6A4E  41 8B C4                        mov eax, r12d
00BE6A51  D3 C0                           rol eax, cl
00BE6A53  41 33 C0                        xor eax, r8d
00BE6A56  89 45 54                        mov dword ptr [rbp + 0x54], eax
00BE6A59  44 8B 4D 54                     mov r9d, dword ptr [rbp + 0x54]
00BE6A5D  E9 45 01 00 00                  jmp 0x140be6ba7
00BE6A62  41 8B C8                        mov ecx, r8d
00BE6A65  41 8B C2                        mov eax, r10d
00BE6A68  D3 C0                           rol eax, cl
00BE6A6A  89 85 98 00 00 00               mov dword ptr [rbp + 0x98], eax
00BE6A70  44 8B 8D 98 00 00 00            mov r9d, dword ptr [rbp + 0x98]
00BE6A77  E9 2E 01 00 00                  jmp 0x140be6baa
00BE6A7C  41 8B C0                        mov eax, r8d
00BE6A7F  83 E8 06                        sub eax, 6
00BE6A82  0F 84 09 01 00 00               je 0x140be6b91
00BE6A88  83 E8 01                        sub eax, 1
00BE6A8B  0F 84 EA 00 00 00               je 0x140be6b7b
00BE6A91  83 E8 01                        sub eax, 1
00BE6A94  0F 84 C8 00 00 00               je 0x140be6b62
00BE6A9A  83 F8 01                        cmp eax, 1
00BE6A9D  0F 84 A1 00 00 00               je 0x140be6b44
00BE6AA3  0F 31                           rdtsc
00BE6AA5  48 C1 E2 20                     shl rdx, 0x20
00BE6AA9  41 BA 4F EC C4 4E               mov r10d, 0x4ec4ec4f
00BE6AAF  48 0B C2                        or rax, rdx
00BE6AB2  48 8B C8                        mov rcx, rax
00BE6AB5  48 8B D0                        mov rdx, rax
00BE6AB8  48 C1 C9 03                     ror rcx, 3
00BE6ABC  49 8B C1                        mov rax, r9
00BE6ABF  48 33 D1                        xor rdx, rcx
00BE6AC2  48 F7 E2                        mul rdx
00BE6AC5  4C 8B CA                        mov r9, rdx
00BE6AC8  48 89 95 00 01 00 00            mov qword ptr [rbp + 0x100], rdx
00BE6ACF  44 33 C8                        xor r9d, eax
00BE6AD2  41 8B C2                        mov eax, r10d
00BE6AD5  41 F7 E1                        mul r9d
00BE6AD8  41 8B C9                        mov ecx, r9d
00BE6ADB  41 C1 E9 05                     shr r9d, 5
00BE6ADF  C1 EA 03                        shr edx, 3
00BE6AE2  45 8B C1                        mov r8d, r9d
00BE6AE5  6B C2 1A                        imul eax, edx, 0x1a
00BE6AE8  2B C8                           sub ecx, eax
00BE6AEA  41 8B C2                        mov eax, r10d
00BE6AED  41 F7 E1                        mul r9d
00BE6AF0  83 C1 61                        add ecx, 0x61
00BE6AF3  41 C1 E9 05                     shr r9d, 5
00BE6AF7  C1 E1 08                        shl ecx, 8
00BE6AFA  C1 EA 03                        shr edx, 3
00BE6AFD  6B C2 1A                        imul eax, edx, 0x1a
00BE6B00  44 2B C0                        sub r8d, eax
00BE6B03  41 8B C2                        mov eax, r10d
00BE6B06  41 F7 E1                        mul r9d
00BE6B09  41 83 C0 41                     add r8d, 0x41
00BE6B0D  44 0B C1                        or r8d, ecx
00BE6B10  C1 EA 03                        shr edx, 3
00BE6B13  6B C2 1A                        imul eax, edx, 0x1a
00BE6B16  41 8B C9                        mov ecx, r9d
00BE6B19  41 C1 E9 05                     shr r9d, 5
00BE6B1D  41 C1 E0 08                     shl r8d, 8
00BE6B21  2B C8                           sub ecx, eax
00BE6B23  41 8B C2                        mov eax, r10d
00BE6B26  41 F7 E1                        mul r9d
00BE6B29  83 C1 61                        add ecx, 0x61
00BE6B2C  C1 EA 03                        shr edx, 3
00BE6B2F  41 0B C8                        or ecx, r8d
00BE6B32  6B C2 1A                        imul eax, edx, 0x1a
00BE6B35  C1 E1 08                        shl ecx, 8
00BE6B38  44 2B C8                        sub r9d, eax
00BE6B3B  41 83 C1 41                     add r9d, 0x41
00BE6B3F  44 0B C9                        or r9d, ecx
00BE6B42  EB 69                           jmp 0x140be6bad
00BE6B44  41 8D 40 02                     lea eax, [r8 + 2]
00BE6B48  8D 0C 40                        lea ecx, [rax + rax*2]
00BE6B4B  41 8B C5                        mov eax, r13d
00BE6B4E  D3 C0                           rol eax, cl
00BE6B50  41 33 C0                        xor eax, r8d
00BE6B53  89 85 9C 00 00 00               mov dword ptr [rbp + 0x9c], eax
00BE6B59  44 8B 8D 9C 00 00 00            mov r9d, dword ptr [rbp + 0x9c]
00BE6B60  EB 45                           jmp 0x140be6ba7
00BE6B62  41 8B C8                        mov ecx, r8d
00BE6B65  B8 41 66 64 42                  mov eax, 0x42646641
00BE6B6A  D3 C0                           rol eax, cl
00BE6B6C  89 85 A0 00 00 00               mov dword ptr [rbp + 0xa0], eax
00BE6B72  44 8B 8D A0 00 00 00            mov r9d, dword ptr [rbp + 0xa0]
00BE6B79  EB 2F                           jmp 0x140be6baa
00BE6B7B  41 8B C8                        mov ecx, r8d
00BE6B7E  B8 41 6C 53 63                  mov eax, 0x63536c41
00BE6B83  D3 C8                           ror eax, cl
00BE6B85  89 45 00                        mov dword ptr [rbp], eax
00BE6B88  44 8B 4D 00                     mov r9d, dword ptr [rbp]
00BE6B8C  E9 AE FE FF FF                  jmp 0x140be6a3f
00BE6B91  41 8D 40 02                     lea eax, [r8 + 2]
00BE6B95  8D 0C 40                        lea ecx, [rax + rax*2]
00BE6B98  41 8B C7                        mov eax, r15d
00BE6B9B  D3 C0                           rol eax, cl
00BE6B9D  41 33 C0                        xor eax, r8d
00BE6BA0  89 45 04                        mov dword ptr [rbp + 4], eax
00BE6BA3  44 8B 4D 04                     mov r9d, dword ptr [rbp + 4]
00BE6BA7  45 33 C8                        xor r9d, r8d
00BE6BAA  41 D3 C9                        ror r9d, cl
00BE6BAD  48 8B 83 00 01 00 00            mov rax, qword ptr [rbx + 0x100]
00BE6BB4  BA 50 00 00 00                  mov edx, 0x50
00BE6BB9  45 8B C1                        mov r8d, r9d
00BE6BBC  8D 4A F0                        lea ecx, [rdx - 0x10]
00BE6BBF  E8 9C 3E 00 00                  call 0x140beaa60
00BE6BC4  33 C9                           xor ecx, ecx
00BE6BC6  48 8D 7D A8                     lea rdi, [rbp - 0x58]
00BE6BCA  48 85 C0                        test rax, rax
00BE6BCD  48 0F 45 F8                     cmovne rdi, rax
00BE6BD1  48 8D 45 80                     lea rax, [rbp - 0x80]
00BE6BD5  44 8D 71 01                     lea r14d, [rcx + 1]
00BE6BD9  48 89 07                        mov qword ptr [rdi], rax
00BE6BDC  48 8B 85 68 01 00 00            mov rax, qword ptr [rbp + 0x168]
00BE6BE3  48 89 47 08                     mov qword ptr [rdi + 8], rax
00BE6BE7  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00BE6BEC  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00BE6BF0  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00BE6BF5  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00BE6BF9  48 8D 05 90 A6 00 00            lea rax, [rip + 0xa690]
00BE6C00  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
00BE6C04  41 8B C6                        mov eax, r14d
00BE6C07  89 77 20                        mov dword ptr [rdi + 0x20], esi
00BE6C0A  89 4F 28                        mov dword ptr [rdi + 0x28], ecx
00BE6C0D  48 89 7F 48                     mov qword ptr [rdi + 0x48], rdi
00BE6C11  48 89 4F 30                     mov qword ptr [rdi + 0x30], rcx
00BE6C15  F0 0F C1 45 A0                  lock xadd dword ptr [rbp - 0x60], eax
00BE6C1A  41 03 C6                        add eax, r14d
00BE6C1D  41 3B C6                        cmp eax, r14d
00BE6C20  75 13                           jne 0x140be6c35
00BE6C22  39 4D A4                        cmp dword ptr [rbp - 0x5c], ecx
00BE6C25  74 0E                           je 0x140be6c35
00BE6C27  45 33 C0                        xor r8d, r8d
00BE6C2A  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00BE6C2E  33 D2                           xor edx, edx
00BE6C30  E8 5F 3B 6E FF                  call 0x1402ca794
00BE6C35  33 D2                           xor edx, edx
00BE6C37  44 89 75 A4                     mov dword ptr [rbp - 0x5c], r14d
00BE6C3B  48 8D 4F 30                     lea rcx, [rdi + 0x30]
00BE6C3F  E8 DC 28 71 FF                  call 0x1402f9520
00BE6C44  48 8D 45 A8                     lea rax, [rbp - 0x58]
00BE6C48  45 33 DB                        xor r11d, r11d
00BE6C4B  48 3B F8                        cmp rdi, rax
00BE6C4E  75 2B                           jne 0x140be6c7b
00BE6C50  44 39 5D A4                     cmp dword ptr [rbp - 0x5c], r11d
00BE6C54  74 25                           je 0x140be6c7b
00BE6C56  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE6C59  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00BE6C5D  45 33 C0                        xor r8d, r8d
00BE6C60  33 D2                           xor edx, edx
00BE6C62  E8 2D 3B 6E FF                  call 0x1402ca794
00BE6C67  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE6C6A  85 C0                           test eax, eax
00BE6C6C  75 E8                           jne 0x140be6c56
00BE6C6E  45 33 DB                        xor r11d, r11d
00BE6C71  41 BC 43 63 42 63               mov r12d, 0x63426343
00BE6C77  44 89 5D A4                     mov dword ptr [rbp - 0x5c], r11d
00BE6C7B  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
00BE6C80  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00BE6C85  C7 00 00 00 00 80               mov dword ptr [rax], 0x80000000
00BE6C8B  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00BE6C8F  E9 E4 05 00 00                  jmp 0x140be7278
00BE6C94  45 33 DB                        xor r11d, r11d
00BE6C97  85 C0                           test eax, eax
00BE6C99  78 25                           js 0x140be6cc0
00BE6C9B  45 8D 43 01                     lea r8d, [r11 + 1]
00BE6C9F  B8 00 10 00 00                  mov eax, 0x1000
00BE6CA4  48 03 F0                        add rsi, rax
00BE6CA7  4C 03 E0                        add r12, rax
00BE6CAA  4D 3B E5                        cmp r12, r13
00BE6CAD  0F 85 57 FC FF FF               jne 0x140be690a
00BE6CB3  41 0F B6 C7                     movzx eax, r15b
00BE6CB7  44 0F 22 C0                     mov cr8, rax
00BE6CBB  E9 3B 01 00 00                  jmp 0x140be6dfb
00BE6CC0  41 0F B6 C7                     movzx eax, r15b
00BE6CC4  44 0F 22 C0                     mov cr8, rax
00BE6CC8  44 39 9B 18 09 00 00            cmp dword ptr [rbx + 0x918], r11d
00BE6CCF  0F 85 26 01 00 00               jne 0x140be6dfb
00BE6CD5  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00BE6CDA  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
00BE6CE4  48 03 C3                        add rax, rbx
00BE6CE7  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
00BE6CEE  48 85 C9                        test rcx, rcx
00BE6CF1  74 19                           je 0x140be6d0c
00BE6CF3  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
00BE6CFD  48 03 C1                        add rax, rcx
00BE6D00  48 89 83 28 09 00 00            mov qword ptr [rbx + 0x928], rax
00BE6D07  48 63 01                        movsxd rax, dword ptr [rcx]
00BE6D0A  EB 0A                           jmp 0x140be6d16
00BE6D0C  4C 89 9B 28 09 00 00            mov qword ptr [rbx + 0x928], r11
00BE6D13  49 8B C3                        mov rax, r11
00BE6D16  48 89 83 30 09 00 00            mov qword ptr [rbx + 0x930], rax
00BE6D1D  BA 01 00 00 00                  mov edx, 1
00BE6D22  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
00BE6D28  48 89 BB 38 09 00 00            mov qword ptr [rbx + 0x938], rdi
00BE6D2F  89 93 18 09 00 00               mov dword ptr [rbx + 0x918], edx
00BE6D35  0F BA E1 1D                     bt ecx, 0x1d
00BE6D39  0F 82 BC 00 00 00               jb 0x140be6dfb
00BE6D3F  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
00BE6D49  0F 84 AC 00 00 00               je 0x140be6dfb
00BE6D4F  84 CA                           test dl, cl
00BE6D51  0F 84 A4 00 00 00               je 0x140be6dfb
00BE6D57  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
00BE6D5D  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
00BE6D63  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
00BE6D6A  2B C1                           sub eax, ecx
00BE6D6C  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
00BE6D73  48 8D 14 19                     lea rdx, [rcx + rbx]
00BE6D77  8B C8                           mov ecx, eax
00BE6D79  48 C1 E9 03                     shr rcx, 3
00BE6D7D  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
00BE6D81  EB 21                           jmp 0x140be6da4
00BE6D83  4C 31 02                        xor qword ptr [rdx], r8
00BE6D86  48 8B 02                        mov rax, qword ptr [rdx]
00BE6D89  41 0F B6 C8                     movzx ecx, r8b
00BE6D8D  49 33 C2                        xor rax, r10
00BE6D90  83 E1 3F                        and ecx, 0x3f
00BE6D93  49 D3 C8                        ror r8, cl
00BE6D96  4C 03 C0                        add r8, rax
00BE6D99  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE6DA0  48 83 C2 08                     add rdx, 8
00BE6DA4  49 3B D1                        cmp rdx, r9
00BE6DA7  75 DA                           jne 0x140be6d83
00BE6DA9  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
00BE6DB1  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
00BE6DB8  74 41                           je 0x140be6dfb
00BE6DBA  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
00BE6DC0  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BE6DC7  48 89 18                        mov qword ptr [rax], rbx
00BE6DCA  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE6DCD  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
00BE6DD4  44 39 9B 18 09 00 00            cmp dword ptr [rbx + 0x918], r11d
00BE6DDB  75 0E                           jne 0x140be6deb
00BE6DDD  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BE6DE4  49 33 C8                        xor rcx, r8
00BE6DE7  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE6DEB  33 D2                           xor edx, edx
00BE6DED  41 B9 00 01 00 00               mov r9d, 0x100
00BE6DF3  48 8B CB                        mov rcx, rbx
00BE6DF6  E8 89 15 00 00                  call 0x140be8384
00BE6DFB  41 8B C6                        mov eax, r14d
00BE6DFE  41 BF 4E 74 46 57               mov r15d, 0x5746744e
00BE6E04  48 03 C7                        add rax, rdi
00BE6E07  41 BC 43 63 42 63               mov r12d, 0x63426343
00BE6E0D  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
00BE6E13  41 BD 46 4F 43 58               mov r13d, 0x58434f46
00BE6E19  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00BE6E1E  44 8B 85 50 01 00 00            mov r8d, dword ptr [rbp + 0x150]
00BE6E25  45 85 C0                        test r8d, r8d
00BE6E28  0F 85 19 01 00 00               jne 0x140be6f47
00BE6E2E  44 01 B3 48 08 00 00            add dword ptr [rbx + 0x848], r14d
00BE6E35  4C 8B CF                        mov r9, rdi
00BE6E38  44 8B 93 34 08 00 00            mov r10d, dword ptr [rbx + 0x834]
00BE6E3F  48 8B C7                        mov rax, rdi
00BE6E42  48 8B B3 38 08 00 00            mov rsi, qword ptr [rbx + 0x838]
00BE6E49  41 8B CE                        mov ecx, r14d
00BE6E4C  48 03 CF                        add rcx, rdi
00BE6E4F  48 3B F9                        cmp rdi, rcx
00BE6E52  73 0C                           jae 0x140be6e60
00BE6E54  0F 18 00                        prefetchnta byte ptr [rax]
00BE6E57  48 83 C0 40                     add rax, 0x40
00BE6E5B  48 3B C1                        cmp rax, rcx
00BE6E5E  72 F4                           jb 0x140be6e54
00BE6E60  45 8B DE                        mov r11d, r14d
00BE6E63  4C 8B C6                        mov r8, rsi
00BE6E66  41 C1 EB 07                     shr r11d, 7
00BE6E6A  45 85 DB                        test r11d, r11d
00BE6E6D  74 6D                           je 0x140be6edc
00BE6E6F  41 BF 01 00 00 00               mov r15d, 1
00BE6E75  49 BD 01 20 00 04 80 00 10 70   movabs r13, 0x7010008004002001
00BE6E7F  B8 08 00 00 00                  mov eax, 8
00BE6E84  4D 33 01                        xor r8, qword ptr [r9]
00BE6E87  41 8B CA                        mov ecx, r10d
00BE6E8A  49 D3 C0                        rol r8, cl
00BE6E8D  4D 33 41 08                     xor r8, qword ptr [r9 + 8]
00BE6E91  49 83 C1 10                     add r9, 0x10
00BE6E95  49 D3 C0                        rol r8, cl
00BE6E98  49 2B C7                        sub rax, r15
00BE6E9B  75 E7                           jne 0x140be6e84
00BE6E9D  49 8B C9                        mov rcx, r9
00BE6EA0  48 2B CF                        sub rcx, rdi
00BE6EA3  48 33 CE                        xor rcx, rsi
00BE6EA6  48 8B C1                        mov rax, rcx
00BE6EA9  48 C1 C0 11                     rol rax, 0x11
00BE6EAD  48 33 C8                        xor rcx, rax
00BE6EB0  49 8B C5                        mov rax, r13
00BE6EB3  48 F7 E1                        mul rcx
00BE6EB6  33 C2                           xor eax, edx
00BE6EB8  48 89 95 C8 00 00 00            mov qword ptr [rbp + 0xc8], rdx
00BE6EBF  44 33 D0                        xor r10d, eax
00BE6EC2  41 83 E2 3F                     and r10d, 0x3f
00BE6EC6  45 0F 44 D7                     cmove r10d, r15d
00BE6ECA  41 83 C3 FF                     add r11d, -1
00BE6ECE  75 AF                           jne 0x140be6e7f
00BE6ED0  41 BF 4E 74 46 57               mov r15d, 0x5746744e
00BE6ED6  41 BD 46 4F 43 58               mov r13d, 0x58434f46
00BE6EDC  41 83 E6 7F                     and r14d, 0x7f
00BE6EE0  41 BB 01 00 00 00               mov r11d, 1
00BE6EE6  41 83 FE 08                     cmp r14d, 8
00BE6EEA  72 1D                           jb 0x140be6f09
00BE6EEC  41 8B C6                        mov eax, r14d
00BE6EEF  48 C1 E8 03                     shr rax, 3
00BE6EF3  4D 33 01                        xor r8, qword ptr [r9]
00BE6EF6  41 8B CA                        mov ecx, r10d
00BE6EF9  49 D3 C0                        rol r8, cl
00BE6EFC  49 83 C1 08                     add r9, 8
00BE6F00  41 83 C6 F8                     add r14d, -8
00BE6F04  49 2B C3                        sub rax, r11
00BE6F07  75 EA                           jne 0x140be6ef3
00BE6F09  45 85 F6                        test r14d, r14d
00BE6F0C  74 16                           je 0x140be6f24
00BE6F0E  41 0F B6 01                     movzx eax, byte ptr [r9]
00BE6F12  41 8B CA                        mov ecx, r10d
00BE6F15  4C 33 C0                        xor r8, rax
00BE6F18  4D 03 CB                        add r9, r11
00BE6F1B  49 D3 C0                        rol r8, cl
00BE6F1E  41 83 C6 FF                     add r14d, -1
00BE6F22  75 EA                           jne 0x140be6f0e
00BE6F24  49 8B C0                        mov rax, r8
00BE6F27  EB 03                           jmp 0x140be6f2c
00BE6F29  44 33 C0                        xor r8d, eax
00BE6F2C  48 C1 E8 1F                     shr rax, 0x1f
00BE6F30  48 85 C0                        test rax, rax
00BE6F33  75 F4                           jne 0x140be6f29
00BE6F35  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00BE6F3A  41 0F BA F0 1F                  btr r8d, 0x1f
00BE6F3F  44 89 00                        mov dword ptr [rax], r8d
00BE6F42  E9 44 FD FF FF                  jmp 0x140be6c8b
00BE6F47  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00BE6F4B  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00BE6F50  85 FF                           test edi, edi
00BE6F52  75 19                           jne 0x140be6f6d
00BE6F54  48 8B 95 58 01 00 00            mov rdx, qword ptr [rbp + 0x158]
00BE6F5B  4C 8B F0                        mov r14, rax
00BE6F5E  48 8B F2                        mov rsi, rdx
00BE6F61  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
00BE6F66  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00BE6F6B  EB 0A                           jmp 0x140be6f77
00BE6F6D  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00BE6F72  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00BE6F77  FF C7                           inc edi
00BE6F79  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00BE6F7D  41 3B F8                        cmp edi, r8d
00BE6F80  0F 82 F9 02 00 00               jb 0x140be727f
00BE6F86  0F 31                           rdtsc
00BE6F88  48 C1 E2 20                     shl rdx, 0x20
00BE6F8C  49 B9 01 20 00 04 80 00 10 70   movabs r9, 0x7010008004002001
00BE6F96  48 0B C2                        or rax, rdx
00BE6F99  48 8B C8                        mov rcx, rax
00BE6F9C  48 8B D0                        mov rdx, rax
00BE6F9F  48 C1 C9 03                     ror rcx, 3
00BE6FA3  49 8B C1                        mov rax, r9
00BE6FA6  48 33 D1                        xor rdx, rcx
00BE6FA9  48 F7 E2                        mul rdx
00BE6FAC  4C 8B C2                        mov r8, rdx
00BE6FAF  48 89 95 D0 00 00 00            mov qword ptr [rbp + 0xd0], rdx
00BE6FB6  4C 33 C0                        xor r8, rax
00BE6FB9  48 B8 A3 8B 2E BA E8 A2 8B 2E   movabs rax, 0x2e8ba2e8ba2e8ba3
00BE6FC3  49 F7 E0                        mul r8
00BE6FC6  48 D1 EA                        shr rdx, 1
00BE6FC9  48 6B C2 0B                     imul rax, rdx, 0xb
00BE6FCD  4C 2B C0                        sub r8, rax
00BE6FD0  41 83 F8 05                     cmp r8d, 5
00BE6FD4  0F 87 AD 00 00 00               ja 0x140be7087
00BE6FDA  0F 84 91 00 00 00               je 0x140be7071
00BE6FE0  41 8B C0                        mov eax, r8d
00BE6FE3  45 85 C0                        test r8d, r8d
00BE6FE6  74 6E                           je 0x140be7056
00BE6FE8  83 E8 01                        sub eax, 1
00BE6FEB  74 50                           je 0x140be703d
00BE6FED  83 E8 01                        sub eax, 1
00BE6FF0  74 35                           je 0x140be7027
00BE6FF2  83 F8 01                        cmp eax, 1
00BE6FF5  74 13                           je 0x140be700a
00BE6FF7  41 8B C8                        mov ecx, r8d
00BE6FFA  B8 46 49 76 70                  mov eax, 0x70764946
00BE6FFF  D3 C8                           ror eax, cl
00BE7001  89 45 0C                        mov dword ptr [rbp + 0xc], eax
00BE7004  44 8B 4D 0C                     mov r9d, dword ptr [rbp + 0xc]
00BE7008  EB 44                           jmp 0x140be704e
00BE700A  41 8D 40 02                     lea eax, [r8 + 2]
00BE700E  8D 0C 40                        lea ecx, [rax + rax*2]
00BE7011  B8 44 50 77 72                  mov eax, 0x72775044
00BE7016  D3 C0                           rol eax, cl
00BE7018  41 33 C0                        xor eax, r8d
00BE701B  89 45 10                        mov dword ptr [rbp + 0x10], eax
00BE701E  44 8B 4D 10                     mov r9d, dword ptr [rbp + 0x10]
00BE7022  E9 7F 01 00 00                  jmp 0x140be71a6
00BE7027  41 8B C8                        mov ecx, r8d
00BE702A  B8 43 64 6D 61                  mov eax, 0x616d6443
00BE702F  D3 C0                           rol eax, cl
00BE7031  89 45 14                        mov dword ptr [rbp + 0x14], eax
00BE7034  44 8B 4D 14                     mov r9d, dword ptr [rbp + 0x14]
00BE7038  E9 6C 01 00 00                  jmp 0x140be71a9
00BE703D  41 8B C8                        mov ecx, r8d
00BE7040  B8 43 63 5A 65                  mov eax, 0x655a6343
00BE7045  D3 C8                           ror eax, cl
00BE7047  89 45 18                        mov dword ptr [rbp + 0x18], eax
00BE704A  44 8B 4D 18                     mov r9d, dword ptr [rbp + 0x18]
00BE704E  41 D3 C1                        rol r9d, cl
00BE7051  E9 56 01 00 00                  jmp 0x140be71ac
00BE7056  41 8D 40 02                     lea eax, [r8 + 2]
00BE705A  8D 0C 40                        lea ecx, [rax + rax*2]
00BE705D  41 8B C4                        mov eax, r12d
00BE7060  D3 C0                           rol eax, cl
00BE7062  41 33 C0                        xor eax, r8d
00BE7065  89 45 1C                        mov dword ptr [rbp + 0x1c], eax
00BE7068  44 8B 4D 1C                     mov r9d, dword ptr [rbp + 0x1c]
00BE706C  E9 35 01 00 00                  jmp 0x140be71a6
00BE7071  41 8B C8                        mov ecx, r8d
00BE7074  B8 4F 62 44 69                  mov eax, 0x6944624f
00BE7079  D3 C0                           rol eax, cl
00BE707B  89 45 20                        mov dword ptr [rbp + 0x20], eax
00BE707E  44 8B 4D 20                     mov r9d, dword ptr [rbp + 0x20]
00BE7082  E9 22 01 00 00                  jmp 0x140be71a9
00BE7087  41 8B C0                        mov eax, r8d
00BE708A  83 E8 06                        sub eax, 6
00BE708D  0F 84 FD 00 00 00               je 0x140be7190
00BE7093  83 E8 01                        sub eax, 1
00BE7096  0F 84 DE 00 00 00               je 0x140be717a
00BE709C  83 E8 01                        sub eax, 1
00BE709F  0F 84 C2 00 00 00               je 0x140be7167
00BE70A5  83 F8 01                        cmp eax, 1
00BE70A8  0F 84 A1 00 00 00               je 0x140be714f
00BE70AE  0F 31                           rdtsc
00BE70B0  48 C1 E2 20                     shl rdx, 0x20
00BE70B4  41 BA 4F EC C4 4E               mov r10d, 0x4ec4ec4f
00BE70BA  48 0B C2                        or rax, rdx
00BE70BD  48 8B C8                        mov rcx, rax
00BE70C0  48 8B D0                        mov rdx, rax
00BE70C3  48 C1 C9 03                     ror rcx, 3
00BE70C7  49 8B C1                        mov rax, r9
00BE70CA  48 33 D1                        xor rdx, rcx
00BE70CD  48 F7 E2                        mul rdx
00BE70D0  4C 8B CA                        mov r9, rdx
00BE70D3  48 89 95 D8 00 00 00            mov qword ptr [rbp + 0xd8], rdx
00BE70DA  44 33 C8                        xor r9d, eax
00BE70DD  41 8B C2                        mov eax, r10d
00BE70E0  41 F7 E1                        mul r9d
00BE70E3  41 8B C9                        mov ecx, r9d
00BE70E6  41 C1 E9 05                     shr r9d, 5
00BE70EA  C1 EA 03                        shr edx, 3
00BE70ED  45 8B C1                        mov r8d, r9d
00BE70F0  6B C2 1A                        imul eax, edx, 0x1a
00BE70F3  2B C8                           sub ecx, eax
00BE70F5  41 8B C2                        mov eax, r10d
00BE70F8  41 F7 E1                        mul r9d
00BE70FB  83 C1 61                        add ecx, 0x61
00BE70FE  41 C1 E9 05                     shr r9d, 5
00BE7102  C1 E1 08                        shl ecx, 8
00BE7105  C1 EA 03                        shr edx, 3
00BE7108  6B C2 1A                        imul eax, edx, 0x1a
00BE710B  44 2B C0                        sub r8d, eax
00BE710E  41 8B C2                        mov eax, r10d
00BE7111  41 F7 E1                        mul r9d
00BE7114  41 83 C0 41                     add r8d, 0x41
00BE7118  44 0B C1                        or r8d, ecx
00BE711B  C1 EA 03                        shr edx, 3
00BE711E  6B C2 1A                        imul eax, edx, 0x1a
00BE7121  41 8B C9                        mov ecx, r9d
00BE7124  41 C1 E9 05                     shr r9d, 5
00BE7128  41 C1 E0 08                     shl r8d, 8
00BE712C  2B C8                           sub ecx, eax
00BE712E  41 8B C2                        mov eax, r10d
00BE7131  41 F7 E1                        mul r9d
00BE7134  83 C1 61                        add ecx, 0x61
00BE7137  C1 EA 03                        shr edx, 3
00BE713A  41 0B C8                        or ecx, r8d
00BE713D  6B C2 1A                        imul eax, edx, 0x1a
00BE7140  C1 E1 08                        shl ecx, 8
00BE7143  44 2B C8                        sub r9d, eax
00BE7146  41 83 C1 41                     add r9d, 0x41
00BE714A  44 0B C9                        or r9d, ecx
00BE714D  EB 5D                           jmp 0x140be71ac
00BE714F  41 8D 40 02                     lea eax, [r8 + 2]
00BE7153  8D 0C 40                        lea ecx, [rax + rax*2]
00BE7156  41 8B C5                        mov eax, r13d
00BE7159  D3 C0                           rol eax, cl
00BE715B  41 33 C0                        xor eax, r8d
00BE715E  89 45 24                        mov dword ptr [rbp + 0x24], eax
00BE7161  44 8B 4D 24                     mov r9d, dword ptr [rbp + 0x24]
00BE7165  EB 3F                           jmp 0x140be71a6
00BE7167  41 8B C8                        mov ecx, r8d
00BE716A  B8 41 66 64 42                  mov eax, 0x42646641
00BE716F  D3 C0                           rol eax, cl
00BE7171  89 45 28                        mov dword ptr [rbp + 0x28], eax
00BE7174  44 8B 4D 28                     mov r9d, dword ptr [rbp + 0x28]
00BE7178  EB 2F                           jmp 0x140be71a9
00BE717A  41 8B C8                        mov ecx, r8d
00BE717D  B8 41 6C 53 63                  mov eax, 0x63536c41
00BE7182  D3 C8                           ror eax, cl
00BE7184  89 45 2C                        mov dword ptr [rbp + 0x2c], eax
00BE7187  44 8B 4D 2C                     mov r9d, dword ptr [rbp + 0x2c]
00BE718B  E9 BE FE FF FF                  jmp 0x140be704e
00BE7190  41 8D 40 02                     lea eax, [r8 + 2]
00BE7194  8D 0C 40                        lea ecx, [rax + rax*2]
00BE7197  41 8B C7                        mov eax, r15d
00BE719A  D3 C0                           rol eax, cl
00BE719C  41 33 C0                        xor eax, r8d
00BE719F  89 45 30                        mov dword ptr [rbp + 0x30], eax
00BE71A2  44 8B 4D 30                     mov r9d, dword ptr [rbp + 0x30]
00BE71A6  45 33 C8                        xor r9d, r8d
00BE71A9  41 D3 C9                        ror r9d, cl
00BE71AC  48 8B 83 00 01 00 00            mov rax, qword ptr [rbx + 0x100]
00BE71B3  BA 50 00 00 00                  mov edx, 0x50
00BE71B8  45 8B C1                        mov r8d, r9d
00BE71BB  8D 4A F0                        lea ecx, [rdx - 0x10]
00BE71BE  E8 9D 38 00 00                  call 0x140beaa60
00BE71C3  48 85 C0                        test rax, rax
00BE71C6  48 8D 7D A8                     lea rdi, [rbp - 0x58]
00BE71CA  48 0F 45 F8                     cmovne rdi, rax
00BE71CE  48 8D 45 80                     lea rax, [rbp - 0x80]
00BE71D2  48 89 07                        mov qword ptr [rdi], rax
00BE71D5  48 8B 85 68 01 00 00            mov rax, qword ptr [rbp + 0x168]
00BE71DC  48 89 47 08                     mov qword ptr [rdi + 8], rax
00BE71E0  48 8D 05 A9 A0 00 00            lea rax, [rip + 0xa0a9]
00BE71E7  4C 89 77 18                     mov qword ptr [rdi + 0x18], r14
00BE71EB  45 33 F6                        xor r14d, r14d
00BE71EE  48 89 77 10                     mov qword ptr [rdi + 0x10], rsi
00BE71F2  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
00BE71F6  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
00BE71FA  41 8D 4E 01                     lea ecx, [r14 + 1]
00BE71FE  89 77 20                        mov dword ptr [rdi + 0x20], esi
00BE7201  8B C1                           mov eax, ecx
00BE7203  44 89 77 28                     mov dword ptr [rdi + 0x28], r14d
00BE7207  48 89 7F 48                     mov qword ptr [rdi + 0x48], rdi
00BE720B  4C 89 77 30                     mov qword ptr [rdi + 0x30], r14
00BE720F  F0 0F C1 45 A0                  lock xadd dword ptr [rbp - 0x60], eax
00BE7214  03 C1                           add eax, ecx
00BE7216  3B C1                           cmp eax, ecx
00BE7218  75 18                           jne 0x140be7232
00BE721A  44 39 75 A4                     cmp dword ptr [rbp - 0x5c], r14d
00BE721E  74 12                           je 0x140be7232
00BE7220  45 33 C0                        xor r8d, r8d
00BE7223  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00BE7227  33 D2                           xor edx, edx
00BE7229  E8 66 35 6E FF                  call 0x1402ca794
00BE722E  41 8D 4E 01                     lea ecx, [r14 + 1]
00BE7232  89 4D A4                        mov dword ptr [rbp - 0x5c], ecx
00BE7235  33 D2                           xor edx, edx
00BE7237  48 8D 4F 30                     lea rcx, [rdi + 0x30]
00BE723B  E8 E0 22 71 FF                  call 0x1402f9520
00BE7240  48 8D 45 A8                     lea rax, [rbp - 0x58]
00BE7244  48 3B F8                        cmp rdi, rax
00BE7247  75 22                           jne 0x140be726b
00BE7249  44 39 75 A4                     cmp dword ptr [rbp - 0x5c], r14d
00BE724D  74 1C                           je 0x140be726b
00BE724F  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE7252  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00BE7256  45 33 C0                        xor r8d, r8d
00BE7259  33 D2                           xor edx, edx
00BE725B  E8 34 35 6E FF                  call 0x1402ca794
00BE7260  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE7263  85 C0                           test eax, eax
00BE7265  75 E8                           jne 0x140be724f
00BE7267  44 89 75 A4                     mov dword ptr [rbp - 0x5c], r14d
00BE726B  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00BE7270  41 8B FE                        mov edi, r14d
00BE7273  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00BE7278  44 8B 85 50 01 00 00            mov r8d, dword ptr [rbp + 0x150]
00BE727F  4C 8B B5 58 01 00 00            mov r14, qword ptr [rbp + 0x158]
00BE7286  41 8B 76 04                     mov esi, dword ptr [r14 + 4]
00BE728A  49 83 C6 0C                     add r14, 0xc
00BE728E  4C 89 B5 58 01 00 00            mov qword ptr [rbp + 0x158], r14
00BE7295  4C 3B B5 B0 00 00 00            cmp r14, qword ptr [rbp + 0xb0]
00BE729C  74 67                           je 0x140be7305
00BE729E  45 8B 06                        mov r8d, dword ptr [r14]
00BE72A1  48 83 C0 04                     add rax, 4
00BE72A5  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00BE72AA  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00BE72AF  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00BE72B2  44 3B C1                        cmp r8d, ecx
00BE72B5  72 18                           jb 0x140be72cf
00BE72B7  8B 45 34                        mov eax, dword ptr [rbp + 0x34]
00BE72BA  41 BA 4F 62 44 69               mov r10d, 0x6944624f
00BE72C0  44 8B 4C 24 38                  mov r9d, dword ptr [rsp + 0x38]
00BE72C5  41 39 46 04                     cmp dword ptr [r14 + 4], eax
00BE72C9  0F 86 FE F4 FF FF               jbe 0x140be67cd
00BE72CF  48 8B 83 20 02 00 00            mov rax, qword ptr [rbx + 0x220]
00BE72D6  48 8B 95 68 01 00 00            mov rdx, qword ptr [rbp + 0x168]
00BE72DD  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00BE72E2  E8 79 37 00 00                  call 0x140beaa60
00BE72E7  33 D2                           xor edx, edx
00BE72E9  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00BE72EE  4C 8B D8                        mov r11, rax
00BE72F1  48 85 C0                        test rax, rax
00BE72F4  0F 84 5D 03 00 00               je 0x140be7657
00BE72FA  41 BA 4F 62 44 69               mov r10d, 0x6944624f
00BE7300  E9 02 F3 FF FF                  jmp 0x140be6607
00BE7305  8B 54 24 3C                     mov edx, dword ptr [rsp + 0x3c]
00BE7309  83 FA FF                        cmp edx, -1
00BE730C  75 0A                           jne 0x140be7318
00BE730E  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00BE7312  F7 D8                           neg eax
00BE7314  1B C9                           sbb ecx, ecx
00BE7316  23 D1                           and edx, ecx
00BE7318  48 8B 85 78 01 00 00            mov rax, qword ptr [rbp + 0x178]
00BE731F  33 F6                           xor esi, esi
00BE7321  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
00BE7325  89 10                           mov dword ptr [rax], edx
00BE7327  48 8B 85 80 01 00 00            mov rax, qword ptr [rbp + 0x180]
00BE732E  89 08                           mov dword ptr [rax], ecx
00BE7330  45 85 C0                        test r8d, r8d
00BE7333  0F 84 19 F2 FF FF               je 0x140be6552
00BE7339  85 FF                           test edi, edi
00BE733B  0F 84 F0 02 00 00               je 0x140be7631
00BE7341  0F 31                           rdtsc
00BE7343  48 C1 E2 20                     shl rdx, 0x20
00BE7347  49 B9 01 20 00 04 80 00 10 70   movabs r9, 0x7010008004002001
00BE7351  48 0B C2                        or rax, rdx
00BE7354  48 8B C8                        mov rcx, rax
00BE7357  48 8B D0                        mov rdx, rax
00BE735A  48 C1 C9 03                     ror rcx, 3
00BE735E  49 8B C1                        mov rax, r9
00BE7361  48 33 D1                        xor rdx, rcx
00BE7364  48 F7 E2                        mul rdx
00BE7367  4C 8B C2                        mov r8, rdx
00BE736A  48 89 95 E0 00 00 00            mov qword ptr [rbp + 0xe0], rdx
00BE7371  4C 33 C0                        xor r8, rax
00BE7374  48 B8 A3 8B 2E BA E8 A2 8B 2E   movabs rax, 0x2e8ba2e8ba2e8ba3
00BE737E  49 F7 E0                        mul r8
00BE7381  48 D1 EA                        shr rdx, 1
00BE7384  48 6B C2 0B                     imul rax, rdx, 0xb
00BE7388  4C 2B C0                        sub r8, rax
00BE738B  41 83 F8 05                     cmp r8d, 5
00BE738F  0F 87 AC 00 00 00               ja 0x140be7441
00BE7395  0F 84 90 00 00 00               je 0x140be742b
00BE739B  41 8B C0                        mov eax, r8d
00BE739E  45 85 C0                        test r8d, r8d
00BE73A1  74 6E                           je 0x140be7411
00BE73A3  83 E8 01                        sub eax, 1
00BE73A6  74 50                           je 0x140be73f8
00BE73A8  83 E8 01                        sub eax, 1
00BE73AB  74 35                           je 0x140be73e2
00BE73AD  83 F8 01                        cmp eax, 1
00BE73B0  74 13                           je 0x140be73c5
00BE73B2  41 8B C8                        mov ecx, r8d
00BE73B5  B8 46 49 76 70                  mov eax, 0x70764946
00BE73BA  D3 C8                           ror eax, cl
00BE73BC  89 45 38                        mov dword ptr [rbp + 0x38], eax
00BE73BF  44 8B 55 38                     mov r10d, dword ptr [rbp + 0x38]
00BE73C3  EB 44                           jmp 0x140be7409
00BE73C5  41 8D 40 02                     lea eax, [r8 + 2]
00BE73C9  8D 0C 40                        lea ecx, [rax + rax*2]
00BE73CC  B8 44 50 77 72                  mov eax, 0x72775044
00BE73D1  D3 C0                           rol eax, cl
00BE73D3  41 33 C0                        xor eax, r8d
00BE73D6  89 45 3C                        mov dword ptr [rbp + 0x3c], eax
00BE73D9  44 8B 55 3C                     mov r10d, dword ptr [rbp + 0x3c]
00BE73DD  E9 85 01 00 00                  jmp 0x140be7567
00BE73E2  41 8B C8                        mov ecx, r8d
00BE73E5  B8 43 64 6D 61                  mov eax, 0x616d6443
00BE73EA  D3 C0                           rol eax, cl
00BE73EC  89 45 40                        mov dword ptr [rbp + 0x40], eax
00BE73EF  44 8B 55 40                     mov r10d, dword ptr [rbp + 0x40]
00BE73F3  E9 72 01 00 00                  jmp 0x140be756a
00BE73F8  41 8B C8                        mov ecx, r8d
00BE73FB  B8 43 63 5A 65                  mov eax, 0x655a6343
00BE7400  D3 C8                           ror eax, cl
00BE7402  89 45 44                        mov dword ptr [rbp + 0x44], eax
00BE7405  44 8B 55 44                     mov r10d, dword ptr [rbp + 0x44]
00BE7409  41 D3 C2                        rol r10d, cl
00BE740C  E9 5C 01 00 00                  jmp 0x140be756d
00BE7411  41 8D 40 02                     lea eax, [r8 + 2]
00BE7415  8D 0C 40                        lea ecx, [rax + rax*2]
00BE7418  41 D3 C4                        rol r12d, cl
00BE741B  45 33 E0                        xor r12d, r8d
00BE741E  44 89 65 48                     mov dword ptr [rbp + 0x48], r12d
00BE7422  44 8B 55 48                     mov r10d, dword ptr [rbp + 0x48]
00BE7426  E9 3C 01 00 00                  jmp 0x140be7567
00BE742B  41 8B C8                        mov ecx, r8d
00BE742E  B8 4F 62 44 69                  mov eax, 0x6944624f
00BE7433  D3 C0                           rol eax, cl
00BE7435  89 45 4C                        mov dword ptr [rbp + 0x4c], eax
00BE7438  44 8B 55 4C                     mov r10d, dword ptr [rbp + 0x4c]
00BE743C  E9 29 01 00 00                  jmp 0x140be756a
00BE7441  41 8B C8                        mov ecx, r8d
00BE7444  83 E9 06                        sub ecx, 6
00BE7447  0F 84 05 01 00 00               je 0x140be7552
00BE744D  83 E9 01                        sub ecx, 1
00BE7450  0F 84 E6 00 00 00               je 0x140be753c
00BE7456  83 E9 01                        sub ecx, 1
00BE7459  0F 84 C4 00 00 00               je 0x140be7523
00BE745F  83 F9 01                        cmp ecx, 1
00BE7462  0F 84 A4 00 00 00               je 0x140be750c
00BE7468  0F 31                           rdtsc
00BE746A  48 C1 E2 20                     shl rdx, 0x20
00BE746E  41 BF 4F EC C4 4E               mov r15d, 0x4ec4ec4f
00BE7474  48 0B C2                        or rax, rdx
00BE7477  48 8B C8                        mov rcx, rax
00BE747A  48 8B D0                        mov rdx, rax
00BE747D  48 C1 C9 03                     ror rcx, 3
00BE7481  49 8B C1                        mov rax, r9
00BE7484  48 33 D1                        xor rdx, rcx
00BE7487  48 F7 E2                        mul rdx
00BE748A  4C 8B D2                        mov r10, rdx
00BE748D  48 89 95 E8 00 00 00            mov qword ptr [rbp + 0xe8], rdx
00BE7494  44 33 D0                        xor r10d, eax
00BE7497  41 8B C7                        mov eax, r15d
00BE749A  41 F7 E2                        mul r10d
00BE749D  41 8B CA                        mov ecx, r10d
00BE74A0  41 C1 EA 05                     shr r10d, 5
00BE74A4  C1 EA 03                        shr edx, 3
00BE74A7  45 8B C2                        mov r8d, r10d
00BE74AA  6B C2 1A                        imul eax, edx, 0x1a
00BE74AD  2B C8                           sub ecx, eax
00BE74AF  41 8B C7                        mov eax, r15d
00BE74B2  41 F7 E2                        mul r10d
00BE74B5  41 C1 EA 05                     shr r10d, 5
00BE74B9  83 C1 61                        add ecx, 0x61
00BE74BC  C1 EA 03                        shr edx, 3
00BE74BF  45 8B CA                        mov r9d, r10d
00BE74C2  6B C2 1A                        imul eax, edx, 0x1a
00BE74C5  C1 E1 08                        shl ecx, 8
00BE74C8  44 2B C0                        sub r8d, eax
00BE74CB  41 8B C7                        mov eax, r15d
00BE74CE  41 F7 E2                        mul r10d
00BE74D1  41 C1 EA 05                     shr r10d, 5
00BE74D5  41 83 C0 41                     add r8d, 0x41
00BE74D9  C1 EA 03                        shr edx, 3
00BE74DC  44 0B C1                        or r8d, ecx
00BE74DF  6B CA 1A                        imul ecx, edx, 0x1a
00BE74E2  41 8B C7                        mov eax, r15d
00BE74E5  41 F7 E2                        mul r10d
00BE74E8  44 2B C9                        sub r9d, ecx
00BE74EB  41 C1 E0 08                     shl r8d, 8
00BE74EF  41 83 C1 61                     add r9d, 0x61
00BE74F3  C1 EA 03                        shr edx, 3
00BE74F6  6B C2 1A                        imul eax, edx, 0x1a
00BE74F9  45 0B C8                        or r9d, r8d
00BE74FC  41 C1 E1 08                     shl r9d, 8
00BE7500  44 2B D0                        sub r10d, eax
00BE7503  41 83 C2 41                     add r10d, 0x41
00BE7507  45 0B D1                        or r10d, r9d
00BE750A  EB 61                           jmp 0x140be756d
00BE750C  41 8D 40 02                     lea eax, [r8 + 2]
00BE7510  8D 0C 40                        lea ecx, [rax + rax*2]
00BE7513  41 D3 C5                        rol r13d, cl
00BE7516  45 33 E8                        xor r13d, r8d
00BE7519  44 89 6D 50                     mov dword ptr [rbp + 0x50], r13d
00BE751D  44 8B 55 50                     mov r10d, dword ptr [rbp + 0x50]
00BE7521  EB 44                           jmp 0x140be7567
00BE7523  41 8B C8                        mov ecx, r8d
00BE7526  B8 41 66 64 42                  mov eax, 0x42646641
00BE752B  D3 C0                           rol eax, cl
00BE752D  89 85 A4 00 00 00               mov dword ptr [rbp + 0xa4], eax
00BE7533  44 8B 95 A4 00 00 00            mov r10d, dword ptr [rbp + 0xa4]
00BE753A  EB 2E                           jmp 0x140be756a
00BE753C  41 8B C8                        mov ecx, r8d
00BE753F  B8 41 6C 53 63                  mov eax, 0x63536c41
00BE7544  D3 C8                           ror eax, cl
00BE7546  89 45 58                        mov dword ptr [rbp + 0x58], eax
00BE7549  44 8B 55 58                     mov r10d, dword ptr [rbp + 0x58]
00BE754D  E9 B7 FE FF FF                  jmp 0x140be7409
00BE7552  41 8D 40 02                     lea eax, [r8 + 2]
00BE7556  8D 0C 40                        lea ecx, [rax + rax*2]
00BE7559  41 D3 C7                        rol r15d, cl
00BE755C  45 33 F8                        xor r15d, r8d
00BE755F  44 89 7D 5C                     mov dword ptr [rbp + 0x5c], r15d
00BE7563  44 8B 55 5C                     mov r10d, dword ptr [rbp + 0x5c]
00BE7567  45 33 D0                        xor r10d, r8d
00BE756A  41 D3 CA                        ror r10d, cl
00BE756D  48 8B 83 00 01 00 00            mov rax, qword ptr [rbx + 0x100]
00BE7574  BA 50 00 00 00                  mov edx, 0x50
00BE7579  45 8B C2                        mov r8d, r10d
00BE757C  8D 4A F0                        lea ecx, [rdx - 0x10]
00BE757F  E8 DC 34 00 00                  call 0x140beaa60
00BE7584  48 85 C0                        test rax, rax
00BE7587  48 8D 5D A8                     lea rbx, [rbp - 0x58]
00BE758B  41 BE 01 00 00 00               mov r14d, 1
00BE7591  48 0F 45 D8                     cmovne rbx, rax
00BE7595  48 8D 45 80                     lea rax, [rbp - 0x80]
00BE7599  48 89 03                        mov qword ptr [rbx], rax
00BE759C  48 8B 85 68 01 00 00            mov rax, qword ptr [rbp + 0x168]
00BE75A3  48 89 43 08                     mov qword ptr [rbx + 8], rax
00BE75A7  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00BE75AC  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00BE75B0  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00BE75B5  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00BE75B9  48 8D 05 D0 9C 00 00            lea rax, [rip + 0x9cd0]
00BE75C0  48 89 43 40                     mov qword ptr [rbx + 0x40], rax
00BE75C4  41 8B C6                        mov eax, r14d
00BE75C7  89 7B 20                        mov dword ptr [rbx + 0x20], edi
00BE75CA  89 73 28                        mov dword ptr [rbx + 0x28], esi
00BE75CD  48 89 5B 48                     mov qword ptr [rbx + 0x48], rbx
00BE75D1  48 89 73 30                     mov qword ptr [rbx + 0x30], rsi
00BE75D5  F0 0F C1 45 A0                  lock xadd dword ptr [rbp - 0x60], eax
00BE75DA  41 03 C6                        add eax, r14d
00BE75DD  41 3B C6                        cmp eax, r14d
00BE75E0  75 13                           jne 0x140be75f5
00BE75E2  39 75 A4                        cmp dword ptr [rbp - 0x5c], esi
00BE75E5  74 0E                           je 0x140be75f5
00BE75E7  45 33 C0                        xor r8d, r8d
00BE75EA  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00BE75EE  33 D2                           xor edx, edx
00BE75F0  E8 9F 31 6E FF                  call 0x1402ca794
00BE75F5  33 D2                           xor edx, edx
00BE75F7  44 89 75 A4                     mov dword ptr [rbp - 0x5c], r14d
00BE75FB  48 8D 4B 30                     lea rcx, [rbx + 0x30]
00BE75FF  E8 1C 1F 71 FF                  call 0x1402f9520
00BE7604  48 8D 45 A8                     lea rax, [rbp - 0x58]
00BE7608  48 3B D8                        cmp rbx, rax
00BE760B  75 24                           jne 0x140be7631
00BE760D  39 75 A4                        cmp dword ptr [rbp - 0x5c], esi
00BE7610  0F 84 3C EF FF FF               je 0x140be6552
00BE7616  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE7619  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00BE761D  45 33 C0                        xor r8d, r8d
00BE7620  33 D2                           xor edx, edx
00BE7622  E8 6D 31 6E FF                  call 0x1402ca794
00BE7627  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE762A  85 C0                           test eax, eax
00BE762C  75 E8                           jne 0x140be7616
00BE762E  89 75 A4                        mov dword ptr [rbp - 0x5c], esi
00BE7631  39 75 A4                        cmp dword ptr [rbp - 0x5c], esi
00BE7634  0F 84 18 EF FF FF               je 0x140be6552
00BE763A  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE763D  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00BE7641  45 33 C0                        xor r8d, r8d
00BE7644  33 D2                           xor edx, edx
00BE7646  E8 49 31 6E FF                  call 0x1402ca794
00BE764B  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE764E  85 C0                           test eax, eax
00BE7650  75 E8                           jne 0x140be763a
00BE7652  E9 FB EE FF FF                  jmp 0x140be6552
00BE7657  BF 44 50 77 72                  mov edi, 0x72775044
00BE765C  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
00BE7666  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
00BE766C  0F BA E1 14                     bt ecx, 0x14
00BE7670  0F 83 51 04 00 00               jae 0x140be7ac7
00BE7676  4C 8B B5 68 01 00 00            mov r14, qword ptr [rbp + 0x168]
00BE767D  39 93 18 09 00 00               cmp dword ptr [rbx + 0x918], edx
00BE7683  0F 85 FA 00 00 00               jne 0x140be7783
00BE7689  48 03 C3                        add rax, rbx
00BE768C  48 89 93 28 09 00 00            mov qword ptr [rbx + 0x928], rdx
00BE7693  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
00BE769A  41 B8 01 00 00 00               mov r8d, 1
00BE76A0  48 C7 83 30 09 00 00 0F 01 00 00  mov qword ptr [rbx + 0x930], 0x10f
00BE76AB  4C 89 B3 38 09 00 00            mov qword ptr [rbx + 0x938], r14
00BE76B2  44 89 83 18 09 00 00            mov dword ptr [rbx + 0x918], r8d
00BE76B9  0F BA E1 1D                     bt ecx, 0x1d
00BE76BD  0F 82 C0 00 00 00               jb 0x140be7783
00BE76C3  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
00BE76CD  0F 84 B0 00 00 00               je 0x140be7783
00BE76D3  41 84 C8                        test r8b, cl
00BE76D6  0F 84 A7 00 00 00               je 0x140be7783
00BE76DC  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
00BE76E2  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
00BE76E8  4C 8B 93 38 08 00 00            mov r10, qword ptr [rbx + 0x838]
00BE76EF  2B C1                           sub eax, ecx
00BE76F1  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
00BE76F8  48 8D 14 19                     lea rdx, [rcx + rbx]
00BE76FC  8B C8                           mov ecx, eax
00BE76FE  48 C1 E9 03                     shr rcx, 3
00BE7702  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
00BE7706  EB 21                           jmp 0x140be7729
00BE7708  4C 31 02                        xor qword ptr [rdx], r8
00BE770B  48 8B 02                        mov rax, qword ptr [rdx]
00BE770E  41 0F B6 C8                     movzx ecx, r8b
00BE7712  49 33 C2                        xor rax, r10
00BE7715  83 E1 3F                        and ecx, 0x3f
00BE7718  49 D3 C8                        ror r8, cl
00BE771B  4C 03 C0                        add r8, rax
00BE771E  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE7725  48 83 C2 08                     add rdx, 8
00BE7729  49 3B D1                        cmp rdx, r9
00BE772C  75 DA                           jne 0x140be7708
00BE772E  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
00BE7736  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
00BE773D  74 42                           je 0x140be7781
00BE773F  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BE7746  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
00BE774C  48 89 18                        mov qword ptr [rax], rbx
00BE774F  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE7752  33 C0                           xor eax, eax
00BE7754  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
00BE775B  39 83 18 09 00 00               cmp dword ptr [rbx + 0x918], eax
00BE7761  75 0E                           jne 0x140be7771
00BE7763  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BE776A  49 33 C8                        xor rcx, r8
00BE776D  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE7771  33 D2                           xor edx, edx
00BE7773  41 B9 00 01 00 00               mov r9d, 0x100
00BE7779  48 8B CB                        mov rcx, rbx
00BE777C  E8 03 0C 00 00                  call 0x140be8384
00BE7781  33 D2                           xor edx, edx
00BE7783  39 95 50 01 00 00               cmp dword ptr [rbp + 0x150], edx
00BE7789  0F 84 17 03 00 00               je 0x140be7aa6
00BE778F  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
00BE7793  85 F6                           test esi, esi
00BE7795  0F 84 EE 02 00 00               je 0x140be7a89
00BE779B  0F 31                           rdtsc
00BE779D  48 C1 E2 20                     shl rdx, 0x20
00BE77A1  49 B9 01 20 00 04 80 00 10 70   movabs r9, 0x7010008004002001
00BE77AB  48 0B C2                        or rax, rdx
00BE77AE  48 8B C8                        mov rcx, rax
00BE77B1  48 8B D0                        mov rdx, rax
00BE77B4  48 C1 C9 03                     ror rcx, 3
00BE77B8  49 8B C1                        mov rax, r9
00BE77BB  48 33 D1                        xor rdx, rcx
00BE77BE  48 F7 E2                        mul rdx
00BE77C1  4C 8B C2                        mov r8, rdx
00BE77C4  48 89 95 F0 00 00 00            mov qword ptr [rbp + 0xf0], rdx
00BE77CB  4C 33 C0                        xor r8, rax
00BE77CE  48 B8 A3 8B 2E BA E8 A2 8B 2E   movabs rax, 0x2e8ba2e8ba2e8ba3
00BE77D8  49 F7 E0                        mul r8
00BE77DB  48 D1 EA                        shr rdx, 1
00BE77DE  48 6B C2 0B                     imul rax, rdx, 0xb
00BE77E2  4C 2B C0                        sub r8, rax
00BE77E5  41 83 F8 05                     cmp r8d, 5
00BE77E9  0F 87 A7 00 00 00               ja 0x140be7896
00BE77EF  0F 84 8B 00 00 00               je 0x140be7880
00BE77F5  41 8B C0                        mov eax, r8d
00BE77F8  45 85 C0                        test r8d, r8d
00BE77FB  74 69                           je 0x140be7866
00BE77FD  83 E8 01                        sub eax, 1
00BE7800  74 4B                           je 0x140be784d
00BE7802  83 E8 01                        sub eax, 1
00BE7805  74 30                           je 0x140be7837
00BE7807  83 F8 01                        cmp eax, 1
00BE780A  74 13                           je 0x140be781f
00BE780C  41 8B C8                        mov ecx, r8d
00BE780F  B8 46 49 76 70                  mov eax, 0x70764946
00BE7814  D3 C8                           ror eax, cl
00BE7816  89 45 64                        mov dword ptr [rbp + 0x64], eax
00BE7819  44 8B 4D 64                     mov r9d, dword ptr [rbp + 0x64]
00BE781D  EB 3F                           jmp 0x140be785e
00BE781F  41 8D 40 02                     lea eax, [r8 + 2]
00BE7823  8D 0C 40                        lea ecx, [rax + rax*2]
00BE7826  D3 C7                           rol edi, cl
00BE7828  41 33 F8                        xor edi, r8d
00BE782B  89 7D 68                        mov dword ptr [rbp + 0x68], edi
00BE782E  44 8B 4D 68                     mov r9d, dword ptr [rbp + 0x68]
00BE7832  E9 8D 01 00 00                  jmp 0x140be79c4
00BE7837  41 8B C8                        mov ecx, r8d
00BE783A  B8 43 64 6D 61                  mov eax, 0x616d6443
00BE783F  D3 C0                           rol eax, cl
00BE7841  89 45 6C                        mov dword ptr [rbp + 0x6c], eax
00BE7844  44 8B 4D 6C                     mov r9d, dword ptr [rbp + 0x6c]
00BE7848  E9 7A 01 00 00                  jmp 0x140be79c7
00BE784D  41 8B C8                        mov ecx, r8d
00BE7850  B8 43 63 5A 65                  mov eax, 0x655a6343
00BE7855  D3 C8                           ror eax, cl
00BE7857  89 45 70                        mov dword ptr [rbp + 0x70], eax
00BE785A  44 8B 4D 70                     mov r9d, dword ptr [rbp + 0x70]
00BE785E  41 D3 C1                        rol r9d, cl
00BE7861  E9 64 01 00 00                  jmp 0x140be79ca
00BE7866  41 8D 40 02                     lea eax, [r8 + 2]
00BE786A  8D 0C 40                        lea ecx, [rax + rax*2]
00BE786D  41 D3 C4                        rol r12d, cl
00BE7870  45 33 E0                        xor r12d, r8d
00BE7873  44 89 65 74                     mov dword ptr [rbp + 0x74], r12d
00BE7877  44 8B 4D 74                     mov r9d, dword ptr [rbp + 0x74]
00BE787B  E9 44 01 00 00                  jmp 0x140be79c4
00BE7880  41 8B C8                        mov ecx, r8d
00BE7883  B8 4F 62 44 69                  mov eax, 0x6944624f
00BE7888  D3 C0                           rol eax, cl
00BE788A  89 45 78                        mov dword ptr [rbp + 0x78], eax
00BE788D  44 8B 4D 78                     mov r9d, dword ptr [rbp + 0x78]
00BE7891  E9 31 01 00 00                  jmp 0x140be79c7
00BE7896  41 8B C0                        mov eax, r8d
00BE7899  83 E8 06                        sub eax, 6
00BE789C  0F 84 0B 01 00 00               je 0x140be79ad
00BE78A2  83 E8 01                        sub eax, 1
00BE78A5  0F 84 E6 00 00 00               je 0x140be7991
00BE78AB  83 E8 01                        sub eax, 1
00BE78AE  0F 84 C4 00 00 00               je 0x140be7978
00BE78B4  83 F8 01                        cmp eax, 1
00BE78B7  0F 84 A4 00 00 00               je 0x140be7961
00BE78BD  0F 31                           rdtsc
00BE78BF  48 C1 E2 20                     shl rdx, 0x20
00BE78C3  41 BA 4F EC C4 4E               mov r10d, 0x4ec4ec4f
00BE78C9  48 0B C2                        or rax, rdx
00BE78CC  48 8B C8                        mov rcx, rax
00BE78CF  48 8B D0                        mov rdx, rax
00BE78D2  49 8B C1                        mov rax, r9
00BE78D5  48 C1 C9 03                     ror rcx, 3
00BE78D9  48 33 D1                        xor rdx, rcx
00BE78DC  48 F7 E2                        mul rdx
00BE78DF  4C 8B C8                        mov r9, rax
00BE78E2  48 89 95 F8 00 00 00            mov qword ptr [rbp + 0xf8], rdx
00BE78E9  44 33 CA                        xor r9d, edx
00BE78EC  41 8B C2                        mov eax, r10d
00BE78EF  41 F7 E1                        mul r9d
00BE78F2  45 8B C1                        mov r8d, r9d
00BE78F5  41 8B C2                        mov eax, r10d
00BE78F8  C1 EA 03                        shr edx, 3
00BE78FB  6B CA 1A                        imul ecx, edx, 0x1a
00BE78FE  41 C1 E9 05                     shr r9d, 5
00BE7902  41 F7 E1                        mul r9d
00BE7905  44 2B C1                        sub r8d, ecx
00BE7908  41 8B C9                        mov ecx, r9d
00BE790B  41 83 C0 61                     add r8d, 0x61
00BE790F  C1 EA 03                        shr edx, 3
00BE7912  6B C2 1A                        imul eax, edx, 0x1a
00BE7915  41 C1 E0 08                     shl r8d, 8
00BE7919  41 C1 E9 05                     shr r9d, 5
00BE791D  2B C8                           sub ecx, eax
00BE791F  41 8B C2                        mov eax, r10d
00BE7922  41 F7 E1                        mul r9d
00BE7925  83 C1 41                        add ecx, 0x41
00BE7928  41 0B C8                        or ecx, r8d
00BE792B  C1 EA 03                        shr edx, 3
00BE792E  6B C2 1A                        imul eax, edx, 0x1a
00BE7931  45 8B C1                        mov r8d, r9d
00BE7934  41 C1 E9 05                     shr r9d, 5
00BE7938  C1 E1 08                        shl ecx, 8
00BE793B  44 2B C0                        sub r8d, eax
00BE793E  41 8B C2                        mov eax, r10d
00BE7941  41 F7 E1                        mul r9d
00BE7944  41 83 C0 61                     add r8d, 0x61
00BE7948  C1 EA 03                        shr edx, 3
00BE794B  44 0B C1                        or r8d, ecx
00BE794E  6B C2 1A                        imul eax, edx, 0x1a
00BE7951  41 C1 E0 08                     shl r8d, 8
00BE7955  44 2B C8                        sub r9d, eax
00BE7958  41 83 C1 41                     add r9d, 0x41
00BE795C  45 0B C8                        or r9d, r8d
00BE795F  EB 69                           jmp 0x140be79ca
00BE7961  41 8D 40 02                     lea eax, [r8 + 2]
00BE7965  8D 0C 40                        lea ecx, [rax + rax*2]
00BE7968  41 D3 C5                        rol r13d, cl
00BE796B  45 33 E8                        xor r13d, r8d
00BE796E  44 89 6D 7C                     mov dword ptr [rbp + 0x7c], r13d
00BE7972  44 8B 4D 7C                     mov r9d, dword ptr [rbp + 0x7c]
00BE7976  EB 4C                           jmp 0x140be79c4
00BE7978  41 8B C8                        mov ecx, r8d
00BE797B  B8 41 66 64 42                  mov eax, 0x42646641
00BE7980  D3 C0                           rol eax, cl
00BE7982  89 85 80 00 00 00               mov dword ptr [rbp + 0x80], eax
00BE7988  44 8B 8D 80 00 00 00            mov r9d, dword ptr [rbp + 0x80]
00BE798F  EB 36                           jmp 0x140be79c7
00BE7991  41 8B C8                        mov ecx, r8d
00BE7994  B8 41 6C 53 63                  mov eax, 0x63536c41
00BE7999  D3 C8                           ror eax, cl
00BE799B  89 85 84 00 00 00               mov dword ptr [rbp + 0x84], eax
00BE79A1  44 8B 8D 84 00 00 00            mov r9d, dword ptr [rbp + 0x84]
00BE79A8  E9 B1 FE FF FF                  jmp 0x140be785e
00BE79AD  41 8D 40 02                     lea eax, [r8 + 2]
00BE79B1  8D 0C 40                        lea ecx, [rax + rax*2]
00BE79B4  41 D3 C7                        rol r15d, cl
00BE79B7  45 33 F8                        xor r15d, r8d
00BE79BA  44 89 7C 24 48                  mov dword ptr [rsp + 0x48], r15d
00BE79BF  44 8B 4C 24 48                  mov r9d, dword ptr [rsp + 0x48]
00BE79C4  45 33 C8                        xor r9d, r8d
00BE79C7  41 D3 C9                        ror r9d, cl
00BE79CA  48 8B 83 00 01 00 00            mov rax, qword ptr [rbx + 0x100]
00BE79D1  BA 50 00 00 00                  mov edx, 0x50
00BE79D6  45 8B C1                        mov r8d, r9d
00BE79D9  8D 4A F0                        lea ecx, [rdx - 0x10]
00BE79DC  E8 7F 30 00 00                  call 0x140beaa60
00BE79E1  45 33 E4                        xor r12d, r12d
00BE79E4  48 8D 5D A8                     lea rbx, [rbp - 0x58]
00BE79E8  48 85 C0                        test rax, rax
00BE79EB  48 0F 45 D8                     cmovne rbx, rax
00BE79EF  48 8D 45 80                     lea rax, [rbp - 0x80]
00BE79F3  48 89 03                        mov qword ptr [rbx], rax
00BE79F6  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00BE79FB  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00BE79FF  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00BE7A04  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00BE7A08  48 8D 05 81 98 00 00            lea rax, [rip + 0x9881]
00BE7A0F  89 73 20                        mov dword ptr [rbx + 0x20], esi
00BE7A12  41 8D 74 24 01                  lea esi, [r12 + 1]
00BE7A17  48 89 43 40                     mov qword ptr [rbx + 0x40], rax
00BE7A1B  8B C6                           mov eax, esi
00BE7A1D  4C 89 73 08                     mov qword ptr [rbx + 8], r14
00BE7A21  44 89 63 28                     mov dword ptr [rbx + 0x28], r12d
00BE7A25  48 89 5B 48                     mov qword ptr [rbx + 0x48], rbx
00BE7A29  4C 89 63 30                     mov qword ptr [rbx + 0x30], r12
00BE7A2D  F0 0F C1 45 A0                  lock xadd dword ptr [rbp - 0x60], eax
00BE7A32  03 C6                           add eax, esi
00BE7A34  3B C6                           cmp eax, esi
00BE7A36  75 14                           jne 0x140be7a4c
00BE7A38  44 39 65 A4                     cmp dword ptr [rbp - 0x5c], r12d
00BE7A3C  74 0E                           je 0x140be7a4c
00BE7A3E  45 33 C0                        xor r8d, r8d
00BE7A41  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00BE7A45  33 D2                           xor edx, edx
00BE7A47  E8 48 2D 6E FF                  call 0x1402ca794
00BE7A4C  33 D2                           xor edx, edx
00BE7A4E  89 75 A4                        mov dword ptr [rbp - 0x5c], esi
00BE7A51  48 8D 4B 30                     lea rcx, [rbx + 0x30]
00BE7A55  E8 C6 1A 71 FF                  call 0x1402f9520
00BE7A5A  48 8D 45 A8                     lea rax, [rbp - 0x58]
00BE7A5E  48 3B D8                        cmp rbx, rax
00BE7A61  75 26                           jne 0x140be7a89
00BE7A63  44 39 65 A4                     cmp dword ptr [rbp - 0x5c], r12d
00BE7A67  74 3D                           je 0x140be7aa6
00BE7A69  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE7A6C  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00BE7A70  45 33 C0                        xor r8d, r8d
00BE7A73  33 D2                           xor edx, edx
00BE7A75  E8 1A 2D 6E FF                  call 0x1402ca794
00BE7A7A  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE7A7D  85 C0                           test eax, eax
00BE7A7F  75 E8                           jne 0x140be7a69
00BE7A81  41 8B C4                        mov eax, r12d
00BE7A84  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00BE7A87  EB 19                           jmp 0x140be7aa2
00BE7A89  8B 45 A4                        mov eax, dword ptr [rbp - 0x5c]
00BE7A8C  EB 14                           jmp 0x140be7aa2
00BE7A8E  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE7A91  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00BE7A95  45 33 C0                        xor r8d, r8d
00BE7A98  33 D2                           xor edx, edx
00BE7A9A  E8 F5 2C 6E FF                  call 0x1402ca794
00BE7A9F  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00BE7AA2  85 C0                           test eax, eax
00BE7AA4  75 E8                           jne 0x140be7a8e
00BE7AA6  B8 7B 00 00 C0                  mov eax, 0xc000007b
00BE7AAB  48 8B 9C 24 60 02 00 00         mov rbx, qword ptr [rsp + 0x260]
00BE7AB3  48 81 C4 10 02 00 00            add rsp, 0x210
00BE7ABA  41 5F                           pop r15
00BE7ABC  41 5E                           pop r14
00BE7ABE  41 5D                           pop r13
00BE7AC0  41 5C                           pop r12
00BE7AC2  5F                              pop rdi
00BE7AC3  5E                              pop rsi
00BE7AC4  5D                              pop rbp
00BE7AC5  C3                              ret
00BE7AC6  CC                              int3
00BE7AC7  4C 8B 85 68 01 00 00            mov r8, qword ptr [rbp + 0x168]
00BE7ACE  41 B9 08 00 00 00               mov r9d, 8
00BE7AD4  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00BE7AD9  C7 45 60 09 00 00 E8            mov dword ptr [rbp + 0x60], 0xe8000009
00BE7AE0  8B 4D 60                        mov ecx, dword ptr [rbp + 0x60]
00BE7AE3  41 8D 51 02                     lea edx, [r9 + 2]
00BE7AE7  C1 C1 65                        rol ecx, 0x65
00BE7AEA  E8 71 5B 91 FF                  call 0x1404fd660
00BE7AEF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00BE60B0(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m20C;
    unsigned int v_stack_m210;
    unsigned int v_stack_m214;
    unsigned int v_stack_m218;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (528);
    result = KeGuardDispatchICall(a4, a2, a3, a4);
    a4 = 0;
    v_stack_m200 = result;
    if (result == 0) goto loc_00BE7AA6;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rsp - 328 + 368))) & (16));
    v_stack_m1F0 = 0;
    v_stack_m218 = 0;
    a1 = (a2) >> (3);
    result = (unsigned __int8)(-(result));
    v_stack_m1E8 = 0;
    v_stack_m1D8 = a1;
    v_r12 = (unsigned int)((v_r12) & (42));
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(a4 + 1)));
    v_stack_m214 = (unsigned int)(a1 * 4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2052)) + 48) + ((unsigned int)(a1 * 4)));
    if (((unsigned int)(result)) <= (*(unsigned int *)(*(unsigned __int64 *)(a1) + 2660))) goto loc_00BE624D;
    result = sub_00BE7AF8(*(unsigned __int64 *)(a1), (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2372)), a4);
    a4 = 0;
    if (result != 0) goto loc_00BE618C;
    goto loc_00BE7AAB;
loc_00BE618C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2520)))) & (2)) != 0) goto loc_00BE623E;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2520))) & (0x10000000ULL));
    a1 = (unsigned int)(-(a1));
    a1 = (unsigned int)((a1) & (*(unsigned int *)(*(unsigned __int64 *)(a1) + 2372)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2052)))) < 8) goto loc_00BE61D8;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2052))))) >> (3);
loc_00BE61C9:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1)) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2052))) + (-8));
    v_rdi = (*(unsigned __int64 *)(a1)) + (8);
    a2 = (a2) - (1);
    if (condition_is_not_equal) goto loc_00BE61C9;
loc_00BE61D8:
    if ((unsigned int)(result) == 0) goto loc_00BE61E7;
loc_00BE61DC:
    *(unsigned __int8 *)(v_rdi) = 0;
    v_rdi = (v_rdi) + (1);
    result = (unsigned int)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BE61DC;
loc_00BE61E7:
    *(unsigned int *)(result + 2372) = (unsigned int)(a1);
    if (((unsigned int)(a1)) == 3) goto loc_00BE6226;
    if (((*(unsigned int *)(result + 2520)) & (0x8000000ULL)) != 0) goto loc_00BE621D;
    if ((unsigned int)(a1) == 0) goto loc_00BE621D;
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024) - 8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024), a4);
    goto loc_00BE6235;
loc_00BE621D:
    goto loc_00BE622D;
loc_00BE6226:
loc_00BE622D:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 2024), a4);
loc_00BE6235:
    *(unsigned int *)(result + 2372) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 2372)));
    a4 = 0;
loc_00BE623E:
    goto loc_00BE6256;
loc_00BE624D:
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2052) = (unsigned int)(result);
loc_00BE6256:
    v_r15 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 2052))) + ((unsigned int)(*(unsigned int *)(result + 2372)));
    v_stack_m1E0 = v_r15;
loc_00BE6270:
    *(unsigned __int64 *)(v_r15) = 0;
    a1 = (unsigned int)((48) + (-8));
    result = (v_r15) + (8);
    a2 = (48 - 42) - (1);
    if (condition_is_not_equal) goto loc_00BE6270;
    if ((unsigned int)(a1) == 0) goto loc_00BE628E;
loc_00BE6283:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (1);
    a1 = (unsigned int)((a1) + (-1));
    if (condition_is_not_equal) goto loc_00BE6283;
loc_00BE628E:
    *(unsigned int *)(v_r15) = (unsigned int)(v_r12);
    *(unsigned __int64 *)(v_r15 + 8) = *(unsigned __int64 *)(v_rsp - 328 + 344);
    *(unsigned int *)(v_r15 + 16) = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int64 *)(v_rsp - 328 + 344)) >= (*(unsigned __int64 *)(v_rsp - 328 + 344) + (unsigned int)(a3) * 1)) goto loc_00BE62D0;
loc_00BE62C4:
    result = (*(unsigned __int64 *)(v_rsp - 328 + 344)) + (64);
    if (result < (*(unsigned __int64 *)(v_rsp - 328 + 344) + (unsigned int)(a3) * 1)) goto loc_00BE62C4;
loc_00BE62D0:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) >> (7));
    if ((unsigned int)(v_r11) == 0) goto loc_00BE6350;
loc_00BE62F6:
loc_00BE62FB:
    a3 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 328 + 344)));
    a3 = (a3) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 328 + 344) + 8));
    a4 = (*(unsigned __int64 *)(v_rsp - 328 + 344)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BE62FB;
    a1 = (a4) - (*(unsigned __int64 *)(v_rsp - 328 + 344));
    a1 = (a1) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104));
    a1 = (a1) ^ (a1);
    result = (unsigned int)((v_r15) ^ ((unsigned int)(*(unsigned __int64 *)(v_rsp - 328 + 344))));
    *(unsigned __int64 *)(v_rsp - 328 + 184) = *(unsigned __int64 *)(v_rsp - 328 + 344);
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2100))) ^ ((unsigned int)(result)));
    v_r10 = (unsigned int)((v_r10) & (63));
    if (condition_is_equal) { v_r10 = 1; }
    v_r11 = (unsigned int)((v_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BE62F6;
loc_00BE6350:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (127));
    if (((unsigned int)(a2)) < 8) goto loc_00BE637C;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00BE6367:
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (8);
    a2 = (unsigned int)((a2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE6367;
loc_00BE637C:
    if ((unsigned int)(a2) == 0) goto loc_00BE6395;
loc_00BE6380:
    a3 = (a3) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (1);
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BE6380;
loc_00BE6395:
    goto loc_00BE639D;
loc_00BE639A:
    a3 = (unsigned int)((a3) ^ (a3));
loc_00BE639D:
    result = (a3) >> (31);
    if (result != 0) goto loc_00BE639A;
    *(unsigned int *)(v_stack_m1E0 + 20) = a3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 328 + 336)) = (unsigned int)(*(unsigned int *)(result + 2372));
    *(unsigned __int64 *)(v_rsp - 328 + 336) = v_cr8;
    result = KeGuardDispatchICall(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1336), a2, a3, a4);
loc_00BE6415:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1568)) + 16 + 8)) == (*(unsigned __int64 *)(v_rsp - 328 + 360))) goto loc_00BE6425;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1568)) + 16) + (15 + 9);
    if (a2 < (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1568)) + 16 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1568)))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1568)))) * 2 * 8)) goto loc_00BE6415;
    goto loc_00BE643C;
loc_00BE6425:
    a1 = 0;
    *(unsigned __int64 *)(v_stack_m1E0 + 24) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m1E0 + 24 + 16) = v_xmm1;
loc_00BE643C:
    result = KeGuardDispatchICall(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1336), a2, a3, a4);
    a2 = 0;
    if (!sign_flag) goto loc_00BE64AF;
loc_00BE6471:
    *(unsigned __int64 *)(v_stack_m1E0 + 24) = 0;
    v_rdi = (unsigned int)((15 + 9) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (v_stack_m1E0 + 24) + (8);
    a1 = (a2 + 3) - (a2 + 1);
    if (condition_is_not_equal) goto loc_00BE6471;
    if ((unsigned int)(v_rdi) == 0) goto loc_00BE648E;
loc_00BE6484:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (a2 + 1);
    v_rdi = (unsigned int)((v_rdi) + (-1));
    if (condition_is_not_equal) goto loc_00BE6484;
loc_00BE648E:
    *(unsigned __int64 *)(v_stack_m1E0 + 32) = *(unsigned __int64 *)(v_rsp - 328 + 360);
    *(unsigned int *)(v_stack_m1E0 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m200 + 80)));
    *(unsigned __int64 *)(v_stack_m1E0 + 24) = a2 + 1;
    goto loc_00BE64C0;
loc_00BE64AF:
loc_00BE64C0:
    v_stack_m208 = v_stack_m1E0 + 48;
    if (((unsigned int)((unsigned int)(v_stack_m214))) < 8) goto loc_00BE64E7;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m214)))) >> (3);
loc_00BE64D4:
    *(unsigned __int64 *)(v_stack_m1E0 + 48) = -1;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m214)) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (v_stack_m1E0 + 48) + (8);
    a1 = (a1) - (a2 + 1);
    if (condition_is_not_equal) goto loc_00BE64D4;
loc_00BE64E7:
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
    if ((unsigned int)(v_rsi) == 0) goto loc_00BE64FA;
loc_00BE64EF:
    *(unsigned __int8 *)(result) = 255;
    result = (result) + (a2 + 1);
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(a4)));
    if (condition_is_not_equal) goto loc_00BE64EF;
loc_00BE64FA:
    v_stack_m20C = (unsigned int)(a4);
    v_stack_m214 = 0;
    v_stack_m1D8 = 0;
    *(unsigned __int64 *)(v_rsp - 328 + 176) = *(unsigned __int64 *)(v_rsp - 328 + 344) + (unsigned int)(v_stack_m1D8) + (unsigned int)(v_stack_m1D8) * 2 * 4;
    result = (unsigned int)(0xFFFFFFF7ULL);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2524)))) & (64)) != 0) { result = *(unsigned int *)(v_rsp - 328 + 368); }
    *(unsigned int *)(v_rsp - 328 + 8) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(v_rsp - 328 + 344)) != (*(unsigned __int64 *)(v_rsp - 328 + 344) + (unsigned int)(v_stack_m1D8) + (unsigned int)(v_stack_m1D8) * 2 * 4)) goto loc_00BE6559;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 376)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 384)) = 0;
loc_00BE6552:
    result = 0;
    goto loc_00BE7AAB;
loc_00BE6559:
    if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2520)) & (0x100000ULL)) != 0) goto loc_00BE6582;
    *(unsigned int *)(v_rsp - 328 + 336) = 0x400ULL;
    *(unsigned __int64 *)(v_rsp - 328 - 128) = (unsigned int)(*(unsigned int *)(result + 2372));
    *(unsigned __int64 *)(v_rsp - 328 - 96) = 0;
    result = KeInitializeGate(v_rsp - 328 - 120, a2, a2 + 1, a4);
    goto loc_00BE65AE;
loc_00BE6582:
    *(unsigned int *)(v_rsp - 328 + 336) = 0;
loc_00BE6591:
    *(unsigned __int64 *)(v_rsp - 328 - 128) = 0;
    a1 = (unsigned int)((120) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (v_rsp - 328 - 128) + (8);
    v_r13 = (15) - (a2 + 1);
    if (condition_is_not_equal) goto loc_00BE6591;
    if ((unsigned int)(a1) == 0) goto loc_00BE65AE;
loc_00BE65A4:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (a2 + 1);
    a1 = (unsigned int)((a1) + ((unsigned int)(a4)));
    if (condition_is_not_equal) goto loc_00BE65A4;
loc_00BE65AE:
    result = KeGuardDispatchICall(v_stack_m200, *(unsigned __int64 *)(v_rsp - 328 + 360), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 344))), a4);
    v_stack_m1F8 = result;
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 328 + 168) = (unsigned int)((unsigned int)(v_r12));
    if (result == 0) goto loc_00BE7666;
loc_00BE6607:
    v_stack_m210 = 0;
    if (((*(unsigned int *)(result + 36)) & (0x2000000ULL)) != 0) goto loc_00BE6655;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) != 0x54494E49ULL) goto loc_00BE662C;
    if ((*(unsigned int *)(result + 4)) == 0x4742444BULL) goto loc_00BE6655;
loc_00BE662C:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) != 0x45474150ULL) goto loc_00BE6663;
    if (((unsigned __int16)(*(unsigned __int16 *)(result + 4))) == ((unsigned __int16)((unsigned int)(0x7877ULL)))) goto loc_00BE6655;
    if (((unsigned __int16)(*(unsigned __int16 *)(result + 4))) == ((unsigned __int16)((unsigned int)(0x7277ULL)))) goto loc_00BE6655;
    if (((unsigned __int16)(*(unsigned __int16 *)(result + 4))) != ((unsigned __int16)((unsigned int)(0x7777ULL)))) goto loc_00BE6675;
loc_00BE6655:
    goto loc_00BE6761;
loc_00BE6663:
    if (((unsigned int)(*(unsigned __int16 *)(result + 4))) != 0x41525245ULL) goto loc_00BE6675;
    if ((*(unsigned __int16 *)((unsigned int)(0x7777ULL))) == ((unsigned __int16)((unsigned int)(0x4154ULL)))) goto loc_00BE6655;
loc_00BE6675:
    a3 = (v_stack_m1F8) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384));
loc_00BE669F:
    a2 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384)) + 1;
    if (((unsigned __int8)(*(unsigned __int8 *)(a3 + *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384) * 1))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2384))))) goto loc_00BE66BC;
    v_r11 = (unsigned int)((7) + (-1));
    if (condition_is_not_equal) goto loc_00BE669F;
    goto loc_00BE6743;
loc_00BE66BC:
loc_00BE66C9:
    a3 = (v_stack_m1F8) + (8);
    a4 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2392)) + (8);
    if ((*(unsigned __int64 *)(v_stack_m1F8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2392)))) goto loc_00BE66FF;
    a2 = (unsigned int)((8) + (-8));
    if (((unsigned int)(a2)) >= 8) goto loc_00BE66C9;
    if ((unsigned int)(a2) == 0) goto loc_00BE6743;
loc_00BE66E8:
    a3 = (a3) + 1;
    a4 = (a4) + 1;
    if (((unsigned __int8)(*(unsigned __int8 *)(a3))) != ((unsigned __int8)(*(unsigned __int8 *)(a4)))) goto loc_00BE66FF;
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BE66E8;
    goto loc_00BE6743;
loc_00BE66FF:
    a2 = (v_stack_m1F8) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400));
loc_00BE670F:
    v_r10 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400)) + (4 - 3);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400) + a2 * 1))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2400))))) goto loc_00BE6725;
    a3 = (unsigned int)((4) + (-1));
    if (condition_is_not_equal) goto loc_00BE670F;
    goto loc_00BE6743;
loc_00BE6725:
    a2 = (v_stack_m1F8) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408));
loc_00BE6731:
    v_rdi = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408)) + (4 - 3);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408) + a2 * 1))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2408))))) goto loc_00BE674E;
    a3 = (unsigned int)((6) + (-1));
    if (condition_is_not_equal) goto loc_00BE6731;
loc_00BE6743:
    goto loc_00BE6759;
loc_00BE674E:
loc_00BE6759:
    a2 = 0;
loc_00BE6761:
    a4 = (unsigned int)(v_stack_m210);
    if (sign_flag) { a4 = 1; }
    v_stack_m210 = (unsigned int)(a4);
    if ((*(unsigned __int64 *)(v_rsp - 328 + 168)) != 43) goto loc_00BE678A;
    if ((*(unsigned __int64 *)(v_rsp - 328 + 168)) < 43) goto loc_00BE678A;
    v_stack_m210 = 1;
    goto loc_00BE678F;
loc_00BE678A:
    if (1 == 0) goto loc_00BE67B5;
loc_00BE678F:
    if ((*(unsigned int *)(v_stack_m1F8)) != 0x54494E49ULL) goto loc_00BE67B5;
    if ((*(unsigned int *)(v_stack_m1F8 + 4)) == 0x4742444BULL) {
        a4 = 1;
        if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2524)) & (0x2000ULL)) != 0) { a4 = 0; }
        v_stack_m210 = (unsigned int)(a4);
    }
    a2 = (unsigned int)(*(unsigned int *)(v_stack_m1F8 + 16));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1F8 + 16)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1F8 + 8))))) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1F8 + 8))); }
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1F8 + 12)))));
    *(unsigned int *)(v_rsp - 328 + 52) = (unsigned int)(a2);
    goto loc_00BE67D3;
loc_00BE67CD:
loc_00BE67D3:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 344) + 8))))) != 0) goto loc_00BE6803;
    a3 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 344) + 8))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 344) + 8)))) >= ((unsigned int)((unsigned int)(v_stack_m20C)))) { a3 = (unsigned int)((unsigned int)(v_stack_m20C)); }
    v_stack_m20C = a3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 344) + 8)))) >= = v_stack_m214) {
        v_stack_m214 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 344) + 8)));
        v_stack_m20C = a3;
    }
loc_00BE6803:
    v_r11 = 0;
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 344)))))) + (*(unsigned __int64 *)(v_rsp - 328 + 360));
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 344) + 4))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 344))))));
    if ((*(unsigned __int64 *)(v_rsp - 328 + 168)) != 43) goto loc_00BE6946;
    if ((unsigned int)(a4) != 0) goto loc_00BE694F;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1F8 + 12))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 344))))));
    if (((unsigned int)(a1)) < 6) goto loc_00BE694F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 344)))) - (0));
    if (((unsigned int)(result)) < 6) goto loc_00BE694F;
    if ((*(unsigned __int8 *)(v_rdi - 6)) != 76) goto loc_00BE694F;
    if ((*(unsigned __int8 *)(v_rdi - 5)) != 135) goto loc_00BE694F;
    if ((*(unsigned __int8 *)(v_rdi - 4)) != 0) goto loc_00BE694F;
    if ((*(unsigned __int8 *)(v_rdi - 3)) != 152) goto loc_00BE694F;
    if ((*(unsigned __int8 *)(v_rdi - 2)) != 195) goto loc_00BE694F;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi - 1))) == 144) goto loc_00BE6887;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi - 1))) != 241) goto loc_00BE694F;
loc_00BE6887:
    if (((*(unsigned __int8 *)(v_rsp - 328 + 8)) & (8)) == 0) goto loc_00BE6E1E;
    result = (v_rdi) & ((unsigned int)(0xFFFULL));
    a1 = (v_r14 + 4095) + (result);
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    if (a1 != 0x1000ULL) goto loc_00BE68CE;
    result = (v_rdi) & (0xFFFFFFFFFFFFF000ULL);
    if (result == v_stack_m1D8) goto loc_00BE6E1E;
loc_00BE68CE:
    if ((unsigned int)(v_r14) == 0) goto loc_00BE6CC8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2524)))) & (64)) == 0) goto loc_00BE6CC8;
    v_rsi = (v_rdi) & (0xFFFFFFFFFFFFF000ULL);
    v_r13 = (v_rdi - 1) + ((unsigned int)((unsigned int)(v_r14)));
    v_r13 = (v_r13) | ((unsigned int)(0xFFFULL));
loc_00BE6901:
loc_00BE690A:
    result = KeGuardDispatchICall(v_rsi, 1, 1, (unsigned int)(0xFFFULL));
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_00BE6C94;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 328 + 336))) > 1) goto loc_00BE6C9F;
    goto loc_00BE6901;
loc_00BE6946:
    if ((unsigned int)((unsigned int)(0xFFFULL)) == 0) goto loc_00BE6887;
loc_00BE694F:
    if ((unsigned int)((unsigned int)(v_stack_m218)) == 0) goto loc_00BE6C80;
    a2 = (1) << (32);
    result = ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 328 + 336))) | (a2);
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rsp - 328 + 192) = a2;
    a3 = (a2) ^ ((unsigned int)(0xFFFULL));
    a2 = (a2) >> (1);
    result = ((unsigned int)(0xFFFULL)) * (a2);
    a3 = (a3) - (result);
    if (a3 > 5) goto loc_00BE6A7C;
    if (a3 == 5) goto loc_00BE6A62;
    if (a3 == 0) goto loc_00BE6A47;
    result = (unsigned int)(((unsigned int)(a3)) - (1));
    if (condition_is_equal) goto loc_00BE6A28;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BE6A0C;
    if (((unsigned int)(result)) == 1) goto loc_00BE69E9;
    *(unsigned int *)(v_rsp - 328 + 136) = (unsigned int)((unsigned int)(0x70764946ULL));
    goto loc_00BE6A3F;
loc_00BE69E9:
    result = (unsigned int)(((unsigned int)(0x72775044ULL)) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 140) = (unsigned int)(result);
    goto loc_00BE6BA7;
loc_00BE6A0C:
    *(unsigned int *)(v_rsp - 328 + 144) = (unsigned int)((unsigned int)(0x616D6443ULL));
    goto loc_00BE6BAA;
loc_00BE6A28:
    *(unsigned int *)(v_rsp - 328 + 148) = (unsigned int)((unsigned int)(0x655A6343ULL));
loc_00BE6A3F:
    goto loc_00BE6BAD;
loc_00BE6A47:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi - 1))) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 84) = (unsigned int)(result);
    goto loc_00BE6BA7;
loc_00BE6A62:
    *(unsigned int *)(v_rsp - 328 + 152) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x6944624FULL))));
    goto loc_00BE6BAA;
loc_00BE6A7C:
    result = (unsigned int)(((unsigned int)(a3)) - (6));
    if (condition_is_equal) goto loc_00BE6B91;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BE6B7B;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BE6B62;
    if (((unsigned int)(result)) == 1) goto loc_00BE6B44;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rsp - 328 + 256) = a2;
    a4 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 328 + 152)))));
    a4 = (unsigned int)((a4) >> (5));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + (97));
    a4 = (unsigned int)((a4) >> (5));
    a1 = (unsigned int)((a1) << (8));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a3 = (unsigned int)((a3) + (65));
    a3 = (unsigned int)((a3) | ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a4 = (unsigned int)((a4) >> (5));
    a3 = (unsigned int)((a3) << (8));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + (97));
    a2 = (unsigned int)((a2) >> (3));
    a1 = (unsigned int)((a1) | (a3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a1 = (unsigned int)((a1) << (8));
    a4 = (unsigned int)((a4) - ((unsigned int)(result)));
    a4 = (unsigned int)((a4) + (65));
    a4 = (unsigned int)((a4) | ((unsigned int)(a1)));
    goto loc_00BE6BAD;
loc_00BE6B44:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 156) = (unsigned int)(result);
    goto loc_00BE6BA7;
loc_00BE6B62:
    *(unsigned int *)(v_rsp - 328 + 160) = (unsigned int)((unsigned int)(0x42646641ULL));
    goto loc_00BE6BAA;
loc_00BE6B7B:
    *(unsigned int *)(v_rsp - 328) = (unsigned int)((unsigned int)(0x63536C41ULL));
    goto loc_00BE6A3F;
loc_00BE6B91:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rsp - 328 + 336)))) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 4) = (unsigned int)(result);
loc_00BE6BA7:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 328 + 4))) ^ (a3));
loc_00BE6BAA:
loc_00BE6BAD:
    result = KeGuardDispatchICall(80 - 16, 80, (unsigned int)((unsigned int)(a4)), a4);
    a1 = 0;
    v_rdi = v_rsp - 328 - 88;
    if (result != 0) { v_rdi = result; }
    *(unsigned __int64 *)(v_rdi) = v_rsp - 328 - 128;
    *(unsigned __int64 *)(v_rdi + 8) = *(unsigned __int64 *)(v_rsp - 328 + 360);
    *(unsigned __int64 *)(v_rdi + 16) = v_stack_m1F0;
    *(unsigned __int64 *)(v_rdi + 24) = v_stack_m1E8;
    *(unsigned __int64 *)(v_rdi + 64) = v_rip + 42640;
    *(unsigned int *)(v_rdi + 32) = (unsigned int)((unsigned int)(v_stack_m218));
    *(unsigned int *)(v_rdi + 40) = 0;
    *(unsigned __int64 *)(v_rdi + 72) = v_rdi;
    *(unsigned __int64 *)(v_rdi + 48) = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(a1 + 1))) + ((unsigned int)(a1 + 1)));
    if (((unsigned int)(result)) != ((unsigned int)(a1 + 1))) goto loc_00BE6C35;
    if ((*(unsigned int *)(v_rsp - 328 - 92)) != 0) {
        a3 = 0;
        a1 = v_rsp - 328 - 120;
        a2 = 0;
        result = KeWaitForGate(a1, a2, a3, a4);
    }
    a2 = 0;
    *(unsigned int *)(v_rsp - 328 - 92) = (unsigned int)(a1 + 1);
    result = ExQueueWorkItem(v_rdi + 48, a2, a3, a4);
    v_r11 = 0;
    if (v_rdi != (v_rsp - 328 - 88)) goto loc_00BE6C7B;
    if ((*(unsigned int *)(v_rsp - 328 - 92)) == 0) goto loc_00BE6C7B;
loc_00BE6C56:
    a3 = 0;
    a2 = 0;
    result = KeWaitForGate(v_rsp - 328 - 120, a2, a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 328 - 96))) != 0) goto loc_00BE6C56;
    v_r11 = 0;
    *(unsigned int *)(v_rsp - 328 - 92) = 0;
loc_00BE6C7B:
    v_stack_m218 = 0;
loc_00BE6C80:
    *(unsigned int *)(v_stack_m208) = 0x80000000ULL;
loc_00BE6C8B:
    goto loc_00BE7278;
loc_00BE6C94:
    v_r11 = 0;
    if (sign_flag) goto loc_00BE6CC0;
loc_00BE6C9F:
    v_rsi = ((unsigned int)(v_stack_m218)) + ((unsigned int)(0x1000ULL));
    v_r12 = ((unsigned int)(0x63426343ULL)) + ((unsigned int)(0x1000ULL));
    if (v_r12 != v_r13) goto loc_00BE690A;
    goto loc_00BE6DFB;
loc_00BE6CC0:
loc_00BE6CC8:
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2328)) != 0) goto loc_00BE6DFB;
    result = ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 328 + 336))) + ((unsigned int)(*(unsigned int *)(result + 2372)));
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2336) = result;
    if (v_stack_m1E0 == 0) goto loc_00BE6D0C;
    result = (result) + (v_stack_m1E0);
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2344) = result;
    goto loc_00BE6D16;
loc_00BE6D0C:
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2344) = 0;
loc_00BE6D16:
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2352) = 0;
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2360) = (unsigned int)(v_stack_m218);
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2328) = 1;
    if (condition_is_below) goto loc_00BE6DFB;
    if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2524)) & (0x200000ULL)) == 0) goto loc_00BE6DFB;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2520))))) == 0) goto loc_00BE6DFB;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE6DA4;
loc_00BE6D83:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2676)) + (unsigned int)(*(unsigned int *)(result + 2372)) * 1)) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2680))) & (63));
    a3 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2676)) + (unsigned int)(*(unsigned int *)(result + 2372)) * 1) + (8);
loc_00BE6DA4:
    if (a2 != ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2676)) + (unsigned int)(*(unsigned int *)(result + 2372)) * 1 + a1 * 8)) goto loc_00BE6D83;
    if (a3 == (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2688))) goto loc_00BE6DFB;
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1416)) = (unsigned int)(*(unsigned int *)(result + 2372));
    *(unsigned int *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2052)));
    result = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1416);
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2328)) == 0) {
        result = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 1416);
        a1 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384((unsigned int)(*(unsigned int *)(result + 2372)), a2, a3, 256);
loc_00BE6DFB:
    result = ((unsigned int)((unsigned int)(a1 + 1))) + ((unsigned int)(v_stack_m218));
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m1D8 = result;
loc_00BE6E1E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 328 + 336))) != 0) goto loc_00BE6F47;
    a1 = ((unsigned int)((unsigned int)(a1 + 1))) + ((unsigned int)(v_stack_m218));
    if (((unsigned int)(v_stack_m218)) >= a1) goto loc_00BE6E60;
loc_00BE6E54:
    result = ((unsigned int)(v_stack_m218)) + (64);
    if (result < a1) goto loc_00BE6E54;
loc_00BE6E60:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(a1 + 1))) >> (7));
    if ((unsigned int)(v_r11) == 0) goto loc_00BE6EDC;
loc_00BE6E7F:
loc_00BE6E84:
    a3 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104)) ^ (*(unsigned __int64 *)((unsigned int)(v_stack_m218)));
    a3 = (a3) ^ (*(unsigned __int64 *)((unsigned int)(v_stack_m218) + 8));
    a4 = ((unsigned int)(v_stack_m218)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BE6E84;
    a1 = (a4) - ((unsigned int)(v_stack_m218));
    a1 = (a1) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104));
    a1 = (a1) ^ (a1);
    result = (unsigned int)(((unsigned int)(0x58434F46ULL)) ^ (0));
    *(unsigned __int64 *)(v_rsp - 328 + 200) = 0;
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2100))) ^ ((unsigned int)(result)));
    v_r10 = (unsigned int)((v_r10) & (63));
    if (condition_is_equal) { v_r10 = 1; }
    v_r11 = (unsigned int)((v_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BE6E7F;
loc_00BE6EDC:
    v_r14 = (unsigned int)((a1 + 1) & (127));
    if (((unsigned int)(v_r14)) < 8) goto loc_00BE6F09;
    result = ((unsigned int)((unsigned int)(v_r14))) >> (3);
loc_00BE6EF3:
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (8);
    v_r14 = (unsigned int)((v_r14) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE6EF3;
loc_00BE6F09:
    if ((unsigned int)(v_r14) == 0) goto loc_00BE6F24;
loc_00BE6F0E:
    a3 = (a3) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (1);
    v_r14 = (unsigned int)((v_r14) + (-1));
    if (condition_is_not_equal) goto loc_00BE6F0E;
loc_00BE6F24:
    goto loc_00BE6F2C;
loc_00BE6F29:
    a3 = (unsigned int)((a3) ^ (a3));
loc_00BE6F2C:
    result = (a3) >> (31);
    if (result != 0) goto loc_00BE6F29;
    *(unsigned int *)(v_stack_m208) = a3;
    goto loc_00BE6C8B;
loc_00BE6F47:
    if ((unsigned int)((unsigned int)(v_stack_m218)) != 0) goto loc_00BE6F6D;
    v_stack_m1F0 = *(unsigned __int64 *)(v_rsp - 328 + 344);
    v_stack_m1E8 = v_stack_m208;
    goto loc_00BE6F77;
loc_00BE6F6D:
loc_00BE6F77:
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m218)) + 1);
    v_stack_m218 = (unsigned int)(v_rdi);
    if (((unsigned int)(v_rdi)) < a3) goto loc_00BE727F;
    a2 = (*(unsigned __int64 *)(v_rsp - 328 + 344)) << (32);
    result = (v_stack_m208) | (a2);
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rsp - 328 + 208) = a2;
    a3 = (a2) ^ (a4);
    a2 = (a2) >> (1);
    result = (a4) * (a2);
    a3 = (a3) - (result);
    if (a3 > 5) goto loc_00BE7087;
    if (a3 == 5) goto loc_00BE7071;
    if (a3 == 0) goto loc_00BE7056;
    result = (unsigned int)(((unsigned int)(a3)) - (1));
    if (condition_is_equal) goto loc_00BE703D;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BE7027;
    if (((unsigned int)(result)) == 1) goto loc_00BE700A;
    *(unsigned int *)(v_rsp - 328 + 12) = (unsigned int)((unsigned int)(0x70764946ULL));
    goto loc_00BE704E;
loc_00BE700A:
    result = (unsigned int)(((unsigned int)(0x72775044ULL)) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 16) = (unsigned int)(result);
    goto loc_00BE71A6;
loc_00BE7027:
    *(unsigned int *)(v_rsp - 328 + 20) = (unsigned int)((unsigned int)(0x616D6443ULL));
    goto loc_00BE71A9;
loc_00BE703D:
    *(unsigned int *)(v_rsp - 328 + 24) = (unsigned int)((unsigned int)(0x655A6343ULL));
loc_00BE704E:
    goto loc_00BE71AC;
loc_00BE7056:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x63426343ULL)))) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 28) = (unsigned int)(result);
    goto loc_00BE71A6;
loc_00BE7071:
    *(unsigned int *)(v_rsp - 328 + 32) = (unsigned int)((unsigned int)(0x6944624FULL));
    goto loc_00BE71A9;
loc_00BE7087:
    result = (unsigned int)(((unsigned int)(a3)) - (6));
    if (condition_is_equal) goto loc_00BE7190;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BE717A;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BE7167;
    if (((unsigned int)(result)) == 1) goto loc_00BE714F;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rsp - 328 + 216) = a2;
    a4 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 328 + 32)))));
    a4 = (unsigned int)((a4) >> (5));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + (97));
    a4 = (unsigned int)((a4) >> (5));
    a1 = (unsigned int)((a1) << (8));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a3 = (unsigned int)((a3) + (65));
    a3 = (unsigned int)((a3) | ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a4 = (unsigned int)((a4) >> (5));
    a3 = (unsigned int)((a3) << (8));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + (97));
    a2 = (unsigned int)((a2) >> (3));
    a1 = (unsigned int)((a1) | (a3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a1 = (unsigned int)((a1) << (8));
    a4 = (unsigned int)((a4) - ((unsigned int)(result)));
    a4 = (unsigned int)((a4) + (65));
    a4 = (unsigned int)((a4) | ((unsigned int)(a1)));
    goto loc_00BE71AC;
loc_00BE714F:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x58434F46ULL)))) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 36) = (unsigned int)(result);
    goto loc_00BE71A6;
loc_00BE7167:
    *(unsigned int *)(v_rsp - 328 + 40) = (unsigned int)((unsigned int)(0x42646641ULL));
    goto loc_00BE71A9;
loc_00BE717A:
    *(unsigned int *)(v_rsp - 328 + 44) = (unsigned int)((unsigned int)(0x63536C41ULL));
    goto loc_00BE704E;
loc_00BE7190:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x5746744EULL)))) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 48) = (unsigned int)(result);
loc_00BE71A6:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 328 + 48))) ^ (a3));
loc_00BE71A9:
loc_00BE71AC:
    result = KeGuardDispatchICall(80 - 16, 80, (unsigned int)((unsigned int)(a4)), a4);
    v_rdi = v_rsp - 328 - 88;
    if (result != 0) { v_rdi = result; }
    *(unsigned __int64 *)(v_rdi) = v_rsp - 328 - 128;
    *(unsigned __int64 *)(v_rdi + 8) = *(unsigned __int64 *)(v_rsp - 328 + 360);
    *(unsigned __int64 *)(v_rdi + 24) = v_stack_m1E8;
    v_r14 = 0;
    *(unsigned __int64 *)(v_rdi + 16) = v_stack_m1F0;
    *(unsigned __int64 *)(v_rdi + 64) = v_rip + 41129;
    *(unsigned int *)(v_rdi + 32) = (unsigned int)((unsigned int)(v_stack_m218));
    *(unsigned int *)(v_rdi + 40) = 0;
    *(unsigned __int64 *)(v_rdi + 72) = v_rdi;
    *(unsigned __int64 *)(v_rdi + 48) = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14 + 1))) + ((unsigned int)(v_r14 + 1)));
    if (((unsigned int)(result)) != ((unsigned int)(v_r14 + 1))) goto loc_00BE7232;
    if ((*(unsigned int *)(v_rsp - 328 - 92)) != 0) {
        a3 = 0;
        a1 = v_rsp - 328 - 120;
        a2 = 0;
        result = KeWaitForGate(a1, a2, a3, a4);
        a1 = v_r14 + 1;
    }
    *(unsigned int *)(v_rsp - 328 - 92) = (unsigned int)(a1);
    a2 = 0;
    result = ExQueueWorkItem(v_rdi + 48, a2, a3, a4);
    if (v_rdi != (v_rsp - 328 - 88)) goto loc_00BE726B;
    if ((*(unsigned int *)(v_rsp - 328 - 92)) == 0) goto loc_00BE726B;
loc_00BE724F:
    a3 = 0;
    a2 = 0;
    result = KeWaitForGate(v_rsp - 328 - 120, a2, a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 328 - 96))) != 0) goto loc_00BE724F;
    *(unsigned int *)(v_rsp - 328 - 92) = 0;
loc_00BE726B:
    v_stack_m218 = 0;
loc_00BE7278:
loc_00BE727F:
    v_r14 = (*(unsigned __int64 *)(v_rsp - 328 + 344)) + (12);
    *(unsigned __int64 *)(v_rsp - 328 + 344) = v_r14;
    if (v_r14 == (*(unsigned __int64 *)(v_rsp - 328 + 176))) goto loc_00BE7305;
    result = (v_stack_m208) + (4);
    v_stack_m208 = result;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1F8 + 12))))) goto loc_00BE72CF;
    if ((*(unsigned int *)(v_r14 + 4)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 328 + 52))))) goto loc_00BE67CD;
loc_00BE72CF:
    result = KeGuardDispatchICall(v_stack_m200, *(unsigned __int64 *)(v_rsp - 328 + 360), (unsigned int)(*(unsigned int *)(v_r14)), (unsigned int)(v_stack_m210));
    a2 = 0;
    v_stack_m1F8 = result;
    if (result == 0) goto loc_00BE7657;
    goto loc_00BE6607;
loc_00BE7305:
    if (((unsigned int)((unsigned int)(v_stack_m20C))) == -1) {
        result = v_stack_m214;
        result = (unsigned int)(-(result));
        a2 = (unsigned int)(((unsigned int)(v_stack_m20C)) & ((unsigned int)(v_stack_m200)));
    }
    v_rsi = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 376)) = (unsigned int)(a2);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 328 + 384)) = (unsigned int)((unsigned int)(v_stack_m214));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14))) == 0) goto loc_00BE6552;
    if (0 == 0) goto loc_00BE7631;
    a2 = (a2) << (32);
    result = (*(unsigned __int64 *)(v_rsp - 328 + 384)) | (a2);
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rsp - 328 + 224) = a2;
    a3 = (a2) ^ ((unsigned int)(v_stack_m210));
    a2 = (a2) >> (1);
    result = ((unsigned int)(v_stack_m210)) * (a2);
    a3 = (a3) - (result);
    if (a3 > 5) goto loc_00BE7441;
    if (a3 == 5) goto loc_00BE742B;
    if (a3 == 0) goto loc_00BE7411;
    result = (unsigned int)(((unsigned int)(a3)) - (1));
    if (condition_is_equal) goto loc_00BE73F8;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BE73E2;
    if (((unsigned int)(result)) == 1) goto loc_00BE73C5;
    *(unsigned int *)(v_rsp - 328 + 56) = (unsigned int)((unsigned int)(0x70764946ULL));
    goto loc_00BE7409;
loc_00BE73C5:
    result = (unsigned int)(((unsigned int)(0x72775044ULL)) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 60) = (unsigned int)(result);
    goto loc_00BE7567;
loc_00BE73E2:
    *(unsigned int *)(v_rsp - 328 + 64) = (unsigned int)((unsigned int)(0x616D6443ULL));
    goto loc_00BE756A;
loc_00BE73F8:
    *(unsigned int *)(v_rsp - 328 + 68) = (unsigned int)((unsigned int)(0x655A6343ULL));
loc_00BE7409:
    goto loc_00BE756D;
loc_00BE7411:
    v_r12 = (unsigned int)(((unsigned int)(0x63426343ULL)) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 72) = (unsigned int)(v_r12);
    goto loc_00BE7567;
loc_00BE742B:
    *(unsigned int *)(v_rsp - 328 + 76) = (unsigned int)((unsigned int)(0x6944624FULL));
    goto loc_00BE756A;
loc_00BE7441:
    a1 = (unsigned int)(((unsigned int)(a3)) - (6));
    if (condition_is_equal) goto loc_00BE7552;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BE753C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BE7523;
    if (((unsigned int)(a1)) == 1) goto loc_00BE750C;
    a2 = (a2) << (32);
    result = ((unsigned int)(0x6944624FULL)) | (a2);
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rsp - 328 + 232) = a2;
    v_r10 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(v_stack_m210))));
    v_r10 = (unsigned int)((v_r10) >> (5));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(result)));
    v_r10 = (unsigned int)((v_r10) >> (5));
    a1 = (unsigned int)((a1) + (97));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a1 = (unsigned int)((a1) << (8));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(result)));
    v_r10 = (unsigned int)((v_r10) >> (5));
    a3 = (unsigned int)((a3) + (65));
    a2 = (unsigned int)((a2) >> (3));
    a3 = (unsigned int)((a3) | ((unsigned int)(a1)));
    a1 = (unsigned int)((a1) * ((unsigned int)(a2)));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(a1)));
    a3 = (unsigned int)((a3) << (8));
    a4 = (unsigned int)((a4) + (97));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a4 = (unsigned int)((a4) | (a3));
    a4 = (unsigned int)((a4) << (8));
    v_r10 = (unsigned int)((v_r10) - ((unsigned int)(result)));
    v_r10 = (unsigned int)((v_r10) + (65));
    v_r10 = (unsigned int)((v_r10) | ((unsigned int)(a4)));
    goto loc_00BE756D;
loc_00BE750C:
    v_r13 = (unsigned int)(((unsigned int)(0x58434F46ULL)) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 80) = (unsigned int)(v_r13);
    goto loc_00BE7567;
loc_00BE7523:
    *(unsigned int *)(v_rsp - 328 + 164) = (unsigned int)((unsigned int)(0x42646641ULL));
    goto loc_00BE756A;
loc_00BE753C:
    *(unsigned int *)(v_rsp - 328 + 88) = (unsigned int)((unsigned int)(0x63536C41ULL));
    goto loc_00BE7409;
loc_00BE7552:
    v_r15 = (unsigned int)(((unsigned int)(0x4EC4EC4FULL)) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 92) = (unsigned int)(v_r15);
loc_00BE7567:
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 328 + 92))) ^ (a3));
loc_00BE756A:
loc_00BE756D:
    result = KeGuardDispatchICall(80 - 16, 80, (unsigned int)((unsigned int)(v_r10)), a4);
    v_rbx = v_rsp - 328 - 88;
    if (result != 0) { v_rbx = result; }
    *(unsigned __int64 *)(v_rbx) = v_rsp - 328 - 128;
    *(unsigned __int64 *)(v_rbx + 8) = *(unsigned __int64 *)(v_rsp - 328 + 360);
    *(unsigned __int64 *)(v_rbx + 16) = v_stack_m1F0;
    *(unsigned __int64 *)(v_rbx + 24) = v_stack_m1E8;
    *(unsigned __int64 *)(v_rbx + 64) = v_rip + 40144;
    *(unsigned int *)(v_rbx + 32) = 0;
    *(unsigned int *)(v_rbx + 40) = 0;
    *(unsigned __int64 *)(v_rbx + 72) = v_rbx;
    *(unsigned __int64 *)(v_rbx + 48) = 0;
    result = (unsigned int)((1) + (1));
    if (((unsigned int)(result)) != 1) goto loc_00BE75F5;
    if ((*(unsigned int *)(v_rsp - 328 - 92)) != 0) {
        a3 = 0;
        a1 = v_rsp - 328 - 120;
        a2 = 0;
        result = KeWaitForGate(a1, a2, a3, a4);
    }
    a2 = 0;
    *(unsigned int *)(v_rsp - 328 - 92) = 1;
    result = ExQueueWorkItem(v_rbx + 48, a2, a3, a4);
    if (v_rbx != (v_rsp - 328 - 88)) goto loc_00BE7631;
    if ((*(unsigned int *)(v_rsp - 328 - 92)) == 0) goto loc_00BE6552;
loc_00BE7616:
    a3 = 0;
    a2 = 0;
    result = KeWaitForGate(v_rsp - 328 - 120, a2, a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 328 - 96))) != 0) goto loc_00BE7616;
    *(unsigned int *)(v_rsp - 328 - 92) = 0;
loc_00BE7631:
    if ((*(unsigned int *)(v_rsp - 328 - 92)) == 0) goto loc_00BE6552;
loc_00BE763A:
    a3 = 0;
    a2 = 0;
    result = KeWaitForGate(v_rsp - 328 - 120, a2, a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 328 - 96))) != 0) goto loc_00BE763A;
    goto loc_00BE6552;
loc_00BE7657:
loc_00BE7666:
    if (condition_is_above_or_equal) goto loc_00BE7AC7;
    if ((*(unsigned int *)(v_rbx + 2328)) != 0) goto loc_00BE7783;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 328 - 96))) + (v_rbx);
    *(unsigned __int64 *)(v_rbx + 2344) = 0;
    *(unsigned __int64 *)(v_rbx + 2336) = result;
    *(unsigned __int64 *)(v_rbx + 2352) = 271;
    *(unsigned __int64 *)(v_rbx + 2360) = *(unsigned __int64 *)(v_rsp - 328 + 360);
    *(unsigned int *)(v_rbx + 2328) = 1;
    if (condition_is_below) goto loc_00BE7783;
    if (((*(unsigned int *)(v_rbx + 2524)) & (0x200000ULL)) == 0) goto loc_00BE7783;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 2520))))) == 0) goto loc_00BE7783;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE7729;
loc_00BE7708:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rbx + 2676)) + v_rbx * 1)) ^ (*(unsigned __int64 *)(v_rbx + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_rbx + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(v_rbx + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(v_rbx + 2676)) + v_rbx * 1) + (8);
loc_00BE7729:
    if (a2 != ((unsigned int)(*(unsigned int *)(v_rbx + 2676)) + v_rbx * 1 + a1 * 8)) goto loc_00BE7708;
    if (a3 == (*(unsigned __int64 *)(v_rbx + 2688))) goto loc_00BE7781;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 1416)) = v_rbx;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbx + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 2052)));
    result = 0;
    if ((*(unsigned int *)(v_rbx + 2328)) == 0) {
        result = *(unsigned __int64 *)(v_rbx + 1416);
        a1 = (*(unsigned __int64 *)(v_rbx + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(v_rbx, a2, a3, 256);
loc_00BE7781:
    a2 = 0;
loc_00BE7783:
    if ((*(unsigned int *)(v_rsp - 328 + 336)) == 0) goto loc_00BE7AA6;
    if ((unsigned int)((unsigned int)(v_stack_m218)) == 0) goto loc_00BE7A89;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rsp - 328 + 240) = a2;
    a3 = (a2) ^ (256);
    a2 = (a2) >> (1);
    result = (256) * (a2);
    a3 = (a3) - (result);
    if (a3 > 5) goto loc_00BE7896;
    if (a3 == 5) goto loc_00BE7880;
    if (a3 == 0) goto loc_00BE7866;
    result = (unsigned int)(((unsigned int)(a3)) - (1));
    if (condition_is_equal) goto loc_00BE784D;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BE7837;
    if (((unsigned int)(result)) == 1) goto loc_00BE781F;
    *(unsigned int *)(v_rsp - 328 + 100) = (unsigned int)((unsigned int)(0x70764946ULL));
    goto loc_00BE785E;
loc_00BE781F:
    v_rdi = (unsigned int)(((unsigned int)(0x72775044ULL)) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 104) = (unsigned int)(v_rdi);
    goto loc_00BE79C4;
loc_00BE7837:
    *(unsigned int *)(v_rsp - 328 + 108) = (unsigned int)((unsigned int)(0x616D6443ULL));
    goto loc_00BE79C7;
loc_00BE784D:
    *(unsigned int *)(v_rsp - 328 + 112) = (unsigned int)((unsigned int)(0x655A6343ULL));
loc_00BE785E:
    goto loc_00BE79CA;
loc_00BE7866:
    v_r12 = (unsigned int)((v_r12) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 116) = (unsigned int)(v_r12);
    goto loc_00BE79C4;
loc_00BE7880:
    *(unsigned int *)(v_rsp - 328 + 120) = (unsigned int)((unsigned int)(0x6944624FULL));
    goto loc_00BE79C7;
loc_00BE7896:
    result = (unsigned int)(((unsigned int)(a3)) - (6));
    if (condition_is_equal) goto loc_00BE79AD;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BE7991;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BE7978;
    if (((unsigned int)(result)) == 1) goto loc_00BE7961;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rsp - 328 + 248) = a2;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 328 + 120))) ^ ((unsigned int)(a2)));
    a2 = (unsigned int)((a2) >> (3));
    a1 = (unsigned int)((result) * ((unsigned int)(a2)));
    a4 = (unsigned int)((a4) >> (5));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(a1)));
    a3 = (unsigned int)((a3) + (97));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a3 = (unsigned int)((a3) << (8));
    a4 = (unsigned int)((a4) >> (5));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + (65));
    a1 = (unsigned int)((a1) | (a3));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a4 = (unsigned int)((a4) >> (5));
    a1 = (unsigned int)((a1) << (8));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a3 = (unsigned int)((a3) + (97));
    a2 = (unsigned int)((a2) >> (3));
    a3 = (unsigned int)((a3) | ((unsigned int)(a1)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a3 = (unsigned int)((a3) << (8));
    a4 = (unsigned int)((a4) - ((unsigned int)(result)));
    a4 = (unsigned int)((a4) + (65));
    a4 = (unsigned int)((a4) | (a3));
    goto loc_00BE79CA;
loc_00BE7961:
    v_r13 = (unsigned int)((v_r13) ^ (a3));
    *(unsigned int *)(v_rsp - 328 + 124) = (unsigned int)(v_r13);
    goto loc_00BE79C4;
loc_00BE7978:
    *(unsigned int *)(v_rsp - 328 + 128) = (unsigned int)((unsigned int)(0x42646641ULL));
    goto loc_00BE79C7;
loc_00BE7991:
    *(unsigned int *)(v_rsp - 328 + 132) = (unsigned int)((unsigned int)(0x63536C41ULL));
    goto loc_00BE785E;
loc_00BE79AD:
    v_r15 = (unsigned int)((v_r15) ^ (a3));
    v_stack_m200 = (unsigned int)(v_r15);
loc_00BE79C4:
    a4 = (unsigned int)(((unsigned int)(v_stack_m200)) ^ (a3));
loc_00BE79C7:
loc_00BE79CA:
    result = KeGuardDispatchICall(80 - 16, 80, (unsigned int)((unsigned int)(a4)), a4);
    v_r12 = 0;
    v_rbx = v_rsp - 328 - 88;
    if (result != 0) { v_rbx = result; }
    *(unsigned __int64 *)(v_rbx) = v_rsp - 328 - 128;
    *(unsigned __int64 *)(v_rbx + 16) = v_stack_m1F0;
    *(unsigned __int64 *)(v_rbx + 24) = v_stack_m1E8;
    *(unsigned int *)(v_rbx + 32) = (unsigned int)((unsigned int)(v_stack_m218));
    *(unsigned __int64 *)(v_rbx + 64) = v_rip + 39041;
    *(unsigned __int64 *)(v_rbx + 8) = *(unsigned __int64 *)(v_rsp - 328 + 360);
    *(unsigned int *)(v_rbx + 40) = 0;
    *(unsigned __int64 *)(v_rbx + 72) = v_rbx;
    *(unsigned __int64 *)(v_rbx + 48) = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12 + 1))) + ((unsigned int)(v_r12 + 1)));
    if (((unsigned int)(result)) != ((unsigned int)(v_r12 + 1))) goto loc_00BE7A4C;
    if ((*(unsigned int *)(v_rsp - 328 - 92)) != 0) {
        a3 = 0;
        a1 = v_rsp - 328 - 120;
        a2 = 0;
        result = KeWaitForGate(a1, a2, a3, a4);
    }
    a2 = 0;
    *(unsigned int *)(v_rsp - 328 - 92) = (unsigned int)(v_r12 + 1);
    result = ExQueueWorkItem(v_rbx + 48, a2, a3, a4);
    if (v_rbx != (v_rsp - 328 - 88)) goto loc_00BE7A89;
    if ((*(unsigned int *)(v_rsp - 328 - 92)) == 0) goto loc_00BE7AA6;
loc_00BE7A69:
    a3 = 0;
    a2 = 0;
    result = KeWaitForGate(v_rsp - 328 - 120, a2, a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 328 - 96))) != 0) goto loc_00BE7A69;
    *(unsigned int *)(v_rsp - 328 - 92) = 0;
    goto loc_00BE7AA2;
loc_00BE7A89:
    goto loc_00BE7AA2;
loc_00BE7A8E:
    a3 = 0;
    a2 = 0;
    result = KeWaitForGate(v_rsp - 328 - 120, a2, a3, a4);
loc_00BE7AA2:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 328 - 96))) != 0) goto loc_00BE7A8E;
loc_00BE7AA6:
loc_00BE7AAB:
    v_rsp = (v_rsp) + (528);
    return (unsigned int)(0xC000007BULL);
loc_00BE7AC7:
    v_stack_p20 = 0;
    *(unsigned int *)(v_rsp - 328 + 96) = 0xE8000009ULL;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 328 + 96)), 8 + 2, *(unsigned __int64 *)(v_rsp - 328 + 360), 8);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00BE60B0(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint32_t v_stack_m20C;
    uint32_t v_stack_m210;
    uint32_t v_stack_m214;
    uint32_t v_stack_m218;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (528);
    result = KeGuardDispatchICall(Arg4, Arg2, Arg3, Arg4);
    Arg4 = 0;
    v_stack_m200 = result;
    if (result == 0) goto loc_00BE7AA6;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x148 + 0x170))) & (16));
    v_stack_m1F0 = 0;
    v_stack_m218 = 0;
    Arg1 = (Arg2) >> (3);
    result = (uint8_t)(-(result));
    v_stack_m1E8 = 0;
    v_stack_m1D8 = Arg1;
    local_r12 = (uint32_t)((local_r12) & (42));
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(Arg4 + 1)));
    v_stack_m214 = (uint32_t)(Arg1 * 4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x804)) + 48) + ((uint32_t)(Arg1 * 4)));
    if (((uint32_t)(result)) <= (*(uint32_t *)(*(uint64_t *)(arg1) + 0xA64))) goto loc_00BE624D;
    result = sub_00BE7AF8(*(uint64_t *)(arg1), (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x944)), Arg4);
    Arg4 = 0;
    if (result != 0) goto loc_00BE618C;
    goto loc_00BE7AAB;
loc_00BE618C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x9D8)))) & (2)) != 0) goto loc_00BE623E;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x9D8))) & (0x10000000ULL));
    Arg1 = (uint32_t)(-(Arg1));
    Arg1 = (uint32_t)((Arg1) & (*(uint32_t *)(*(uint64_t *)(arg1) + 0x944)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x804)))) < 8) goto loc_00BE61D8;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x804))))) >> (3);
loc_00BE61C9:
    *(uint64_t *)(*(uint64_t *)(arg1)) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x804))) + (-8));
    local_rdi = (*(uint64_t *)(arg1)) + (8);
    Arg2 = (Arg2) - (1);
    if (condition_is_not_equal) goto loc_00BE61C9;
loc_00BE61D8:
    if ((uint32_t)(result) == 0) goto loc_00BE61E7;
loc_00BE61DC:
    *(uint8_t *)(local_rdi) = 0;
    local_rdi = (local_rdi) + (1);
    result = (uint32_t)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BE61DC;
loc_00BE61E7:
    *(uint32_t *)(result + 0x944) = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) == 3) goto loc_00BE6226;
    if (((*(uint32_t *)(result + 0x9D8)) & (0x8000000ULL)) != 0) goto loc_00BE621D;
    if ((uint32_t)(Arg1) == 0) goto loc_00BE621D;
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8) - 8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8) - 0x8), *(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8), Arg4);
    goto loc_00BE6235;
loc_00BE621D:
    goto loc_00BE622D;
loc_00BE6226:
loc_00BE622D:
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8) - 0x8), *(uint64_t *)(*(uint64_t *)(arg1) + 0x7E8), Arg4);
loc_00BE6235:
    *(uint32_t *)(result + 0x944) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x944)));
    Arg4 = 0;
loc_00BE623E:
    goto loc_00BE6256;
loc_00BE624D:
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x804) = (uint32_t)(result);
loc_00BE6256:
    local_r15 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x804))) + ((uint32_t)(*(uint32_t *)(result + 0x944)));
    v_stack_m1E0 = local_r15;
loc_00BE6270:
    *(uint64_t *)(local_r15) = 0;
    Arg1 = (uint32_t)((48) + (-8));
    result = (local_r15) + (8);
    Arg2 = (48 - 42) - (1);
    if (condition_is_not_equal) goto loc_00BE6270;
    if ((uint32_t)(Arg1) == 0) goto loc_00BE628E;
loc_00BE6283:
    *(uint8_t *)(result) = 0;
    result = (result) + (1);
    Arg1 = (uint32_t)((Arg1) + (-1));
    if (condition_is_not_equal) goto loc_00BE6283;
loc_00BE628E:
    *(uint32_t *)(local_r15) = (uint32_t)(local_r12);
    *(uint64_t *)(local_r15 + 0x8) = *(uint64_t *)(local_rsp - 0x148 + 0x158);
    *(uint32_t *)(local_r15 + 0x10) = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint64_t *)(local_rsp - 0x148 + 0x158)) >= (*(uint64_t *)(local_rsp - 0x148 + 0x158) + (uint32_t)(Arg3) * 1)) goto loc_00BE62D0;
loc_00BE62C4:
    result = (*(uint64_t *)(local_rsp - 0x148 + 0x158)) + (64);
    if (result < (*(uint64_t *)(local_rsp - 0x148 + 0x158) + (uint32_t)(Arg3) * 1)) goto loc_00BE62C4;
loc_00BE62D0:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> (7));
    if ((uint32_t)(local_r11) == 0) goto loc_00BE6350;
loc_00BE62F6:
loc_00BE62FB:
    Arg3 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838)) ^ (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158)));
    Arg3 = (Arg3) ^ (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158) + 0x8));
    Arg4 = (*(uint64_t *)(local_rsp - 0x148 + 0x158)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BE62FB;
    Arg1 = (Arg4) - (*(uint64_t *)(local_rsp - 0x148 + 0x158));
    Arg1 = (Arg1) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    result = (uint32_t)((local_r15) ^ ((uint32_t)(*(uint64_t *)(local_rsp - 0x148 + 0x158))));
    *(uint64_t *)(local_rsp - 0x148 + 0xB8) = *(uint64_t *)(local_rsp - 0x148 + 0x158);
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x834))) ^ ((uint32_t)(result)));
    local_r10 = (uint32_t)((local_r10) & (63));
    if (condition_is_equal) { local_r10 = 1; }
    local_r11 = (uint32_t)((local_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BE62F6;
loc_00BE6350:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (127));
    if (((uint32_t)(Arg2)) < 8) goto loc_00BE637C;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_00BE6367:
    Arg3 = (Arg3) ^ (*(uint64_t *)(Arg4));
    Arg4 = (Arg4) + (8);
    Arg2 = (uint32_t)((Arg2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE6367;
loc_00BE637C:
    if ((uint32_t)(Arg2) == 0) goto loc_00BE6395;
loc_00BE6380:
    Arg3 = (Arg3) ^ (*(uint8_t *)(Arg4));
    Arg4 = (Arg4) + (1);
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_00BE6380;
loc_00BE6395:
    goto loc_00BE639D;
loc_00BE639A:
    Arg3 = (uint32_t)((Arg3) ^ (Arg3));
loc_00BE639D:
    result = (Arg3) >> (31);
    if (result != 0) goto loc_00BE639A;
    *(uint32_t *)(v_stack_m1E0 + 0x14) = Arg3;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x150)) = (uint32_t)(*(uint32_t *)(result + 0x944));
    *(uint64_t *)(local_rsp - 0x148 + 0x150) = v_cr8;
    result = KeGuardDispatchICall(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x538), Arg2, Arg3, Arg4);
loc_00BE6415:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x620)) + 0x10 + 0x8)) == (*(uint64_t *)(local_rsp - 0x148 + 0x168))) goto loc_00BE6425;
    Arg2 = (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x620)) + 16) + (15 + 9);
    if (Arg2 < (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x620)) + 16 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x620)))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x620)))) * 2 * 8)) goto loc_00BE6415;
    goto loc_00BE643C;
loc_00BE6425:
    Arg1 = 0;
    *(uint64_t *)(v_stack_m1E0 + 0x18) = v_xmm0;
    *(uint64_t *)(v_stack_m1E0 + 0x18 + 0x10) = v_xmm1;
loc_00BE643C:
    result = KeGuardDispatchICall(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x538), Arg2, Arg3, Arg4);
    Arg2 = 0;
    if (!sign_flag) goto loc_00BE64AF;
loc_00BE6471:
    *(uint64_t *)(v_stack_m1E0 + 0x18) = 0;
    local_rdi = (uint32_t)((15 + 9) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (v_stack_m1E0 + 24) + (8);
    Arg1 = (Arg2 + 3) - (Arg2 + 1);
    if (condition_is_not_equal) goto loc_00BE6471;
    if ((uint32_t)(local_rdi) == 0) goto loc_00BE648E;
loc_00BE6484:
    *(uint8_t *)(result) = 0;
    result = (result) + (Arg2 + 1);
    local_rdi = (uint32_t)((local_rdi) + (-1));
    if (condition_is_not_equal) goto loc_00BE6484;
loc_00BE648E:
    *(uint64_t *)(v_stack_m1E0 + 0x20) = *(uint64_t *)(local_rsp - 0x148 + 0x168);
    *(uint32_t *)(v_stack_m1E0 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m200 + 0x50)));
    *(uint64_t *)(v_stack_m1E0 + 0x18) = Arg2 + 1;
    goto loc_00BE64C0;
loc_00BE64AF:
loc_00BE64C0:
    v_stack_m208 = v_stack_m1E0 + 48;
    if (((uint32_t)((uint32_t)(v_stack_m214))) < 8) goto loc_00BE64E7;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m214)))) >> (3);
loc_00BE64D4:
    *(uint64_t *)(v_stack_m1E0 + 0x30) = -1;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m214)) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (v_stack_m1E0 + 48) + (8);
    Arg1 = (Arg1) - (Arg2 + 1);
    if (condition_is_not_equal) goto loc_00BE64D4;
loc_00BE64E7:
    Arg4 = (uint32_t)((Arg4) | (0xFFFFFFFFULL));
    if ((uint32_t)(local_rsi) == 0) goto loc_00BE64FA;
loc_00BE64EF:
    *(uint8_t *)(result) = 255;
    result = (result) + (Arg2 + 1);
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(Arg4)));
    if (condition_is_not_equal) goto loc_00BE64EF;
loc_00BE64FA:
    v_stack_m20C = (uint32_t)(Arg4);
    v_stack_m214 = 0;
    v_stack_m1D8 = 0;
    *(uint64_t *)(local_rsp - 0x148 + 0xB0) = *(uint64_t *)(local_rsp - 0x148 + 0x158) + (uint32_t)(v_stack_m1D8) + (uint32_t)(v_stack_m1D8) * 2 * 4;
    result = (uint32_t)(0xFFFFFFF7ULL);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9DC)))) & (64)) != 0) { result = *(uint32_t *)(local_rsp - 0x148 + 0x170); }
    *(uint32_t *)(local_rsp - 0x148 + 0x8) = (uint32_t)(result);
    if ((*(uint64_t *)(local_rsp - 0x148 + 0x158)) != (*(uint64_t *)(local_rsp - 0x148 + 0x158) + (uint32_t)(v_stack_m1D8) + (uint32_t)(v_stack_m1D8) * 2 * 4)) goto loc_00BE6559;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x178)) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x180)) = 0;
loc_00BE6552:
    result = 0;
    goto loc_00BE7AAB;
loc_00BE6559:
    if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9D8)) & (0x100000ULL)) != 0) goto loc_00BE6582;
    *(uint32_t *)(local_rsp - 0x148 + 0x150) = 0x400ULL;
    *(uint64_t *)(local_rsp - 0x148 - 0x80) = (uint32_t)(*(uint32_t *)(result + 0x944));
    *(uint64_t *)(local_rsp - 0x148 - 0x60) = 0;
    result = KeInitializeGate(local_rsp - 328 - 120, Arg2, Arg2 + 1, Arg4);
    goto loc_00BE65AE;
loc_00BE6582:
    *(uint32_t *)(local_rsp - 0x148 + 0x150) = 0;
loc_00BE6591:
    *(uint64_t *)(local_rsp - 0x148 - 0x80) = 0;
    Arg1 = (uint32_t)((120) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (local_rsp - 328 - 128) + (8);
    local_r13 = (15) - (Arg2 + 1);
    if (condition_is_not_equal) goto loc_00BE6591;
    if ((uint32_t)(Arg1) == 0) goto loc_00BE65AE;
loc_00BE65A4:
    *(uint8_t *)(result) = 0;
    result = (result) + (Arg2 + 1);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg4)));
    if (condition_is_not_equal) goto loc_00BE65A4;
loc_00BE65AE:
    result = KeGuardDispatchICall(v_stack_m200, *(uint64_t *)(local_rsp - 0x148 + 0x168), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158))), Arg4);
    v_stack_m1F8 = result;
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x148 + 0xA8) = (uint32_t)((uint32_t)(local_r12));
    if (result == 0) goto loc_00BE7666;
loc_00BE6607:
    v_stack_m210 = 0;
    if (((*(uint32_t *)(result + 0x24)) & (0x2000000ULL)) != 0) goto loc_00BE6655;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) != 0x54494E49ULL) goto loc_00BE662C;
    if ((*(uint32_t *)(result + 0x4)) == 0x4742444BULL) goto loc_00BE6655;
loc_00BE662C:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) != 0x45474150ULL) goto loc_00BE6663;
    if (((uint16_t)(*(uint16_t *)(result + 0x4))) == ((uint16_t)((uint32_t)(0x7877ULL)))) goto loc_00BE6655;
    if (((uint16_t)(*(uint16_t *)(result + 0x4))) == ((uint16_t)((uint32_t)(0x7277ULL)))) goto loc_00BE6655;
    if (((uint16_t)(*(uint16_t *)(result + 0x4))) != ((uint16_t)((uint32_t)(0x7777ULL)))) goto loc_00BE6675;
loc_00BE6655:
    goto loc_00BE6761;
loc_00BE6663:
    if (((uint32_t)(*(uint16_t *)(result + 0x4))) != 0x41525245ULL) goto loc_00BE6675;
    if ((*(uint16_t *)((uint32_t)(0x7777ULL))) == ((uint16_t)((uint32_t)(0x4154ULL)))) goto loc_00BE6655;
loc_00BE6675:
    Arg3 = (v_stack_m1F8) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950));
loc_00BE669F:
    Arg2 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950)) + 1;
    if (((uint8_t)(*(uint8_t *)(Arg3 + *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950) * 1))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x950))))) goto loc_00BE66BC;
    local_r11 = (uint32_t)((7) + (-1));
    if (condition_is_not_equal) goto loc_00BE669F;
    goto loc_00BE6743;
loc_00BE66BC:
loc_00BE66C9:
    Arg3 = (v_stack_m1F8) + (8);
    Arg4 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x958)) + (8);
    if ((*(uint64_t *)(v_stack_m1F8)) != (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x958)))) goto loc_00BE66FF;
    Arg2 = (uint32_t)((8) + (-8));
    if (((uint32_t)(Arg2)) >= 8) goto loc_00BE66C9;
    if ((uint32_t)(Arg2) == 0) goto loc_00BE6743;
loc_00BE66E8:
    Arg3 = (Arg3) + 1;
    Arg4 = (Arg4) + 1;
    if (((uint8_t)(*(uint8_t *)(Arg3))) != ((uint8_t)(*(uint8_t *)(Arg4)))) goto loc_00BE66FF;
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_00BE66E8;
    goto loc_00BE6743;
loc_00BE66FF:
    Arg2 = (v_stack_m1F8) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960));
loc_00BE670F:
    local_r10 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960)) + (4 - 3);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960) + Arg2 * 1))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x960))))) goto loc_00BE6725;
    Arg3 = (uint32_t)((4) + (-1));
    if (condition_is_not_equal) goto loc_00BE670F;
    goto loc_00BE6743;
loc_00BE6725:
    Arg2 = (v_stack_m1F8) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968));
loc_00BE6731:
    local_rdi = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968)) + (4 - 3);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968) + Arg2 * 1))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x968))))) goto loc_00BE674E;
    Arg3 = (uint32_t)((6) + (-1));
    if (condition_is_not_equal) goto loc_00BE6731;
loc_00BE6743:
    goto loc_00BE6759;
loc_00BE674E:
loc_00BE6759:
    Arg2 = 0;
loc_00BE6761:
    Arg4 = (uint32_t)(v_stack_m210);
    if (sign_flag) { Arg4 = 1; }
    v_stack_m210 = (uint32_t)(Arg4);
    if ((*(uint64_t *)(local_rsp - 0x148 + 0xA8)) != 43) goto loc_00BE678A;
    if ((*(uint64_t *)(local_rsp - 0x148 + 0xA8)) < 43) goto loc_00BE678A;
    v_stack_m210 = 1;
    goto loc_00BE678F;
loc_00BE678A:
    if (1 == 0) goto loc_00BE67B5;
loc_00BE678F:
    if ((*(uint32_t *)(v_stack_m1F8)) != 0x54494E49ULL) goto loc_00BE67B5;
    if ((*(uint32_t *)(v_stack_m1F8 + 0x4)) == 0x4742444BULL) {
        Arg4 = 1;
        if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9DC)) & (0x2000ULL)) != 0) { Arg4 = 0; }
        v_stack_m210 = (uint32_t)(Arg4);
    }
    Arg2 = (uint32_t)(*(uint32_t *)(v_stack_m1F8 + 0x10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1F8 + 0x10)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1F8 + 0x8))))) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1F8 + 0x8))); }
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1F8 + 0xC)))));
    *(uint32_t *)(local_rsp - 0x148 + 0x34) = (uint32_t)(Arg2);
    goto loc_00BE67D3;
loc_00BE67CD:
loc_00BE67D3:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158) + 0x8))))) != 0) goto loc_00BE6803;
    Arg3 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158) + 0x8))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158) + 0x8)))) >= ((uint32_t)((uint32_t)(v_stack_m20C)))) { Arg3 = (uint32_t)((uint32_t)(v_stack_m20C)); }
    v_stack_m20C = Arg3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158) + 0x8)))) >= = v_stack_m214) {
        v_stack_m214 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158) + 0x8)));
        v_stack_m20C = Arg3;
    }
loc_00BE6803:
    local_r11 = 0;
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158)))))) + (*(uint64_t *)(local_rsp - 0x148 + 0x168));
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158) + 0x4))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158))))));
    if ((*(uint64_t *)(local_rsp - 0x148 + 0xA8)) != 43) goto loc_00BE6946;
    if ((uint32_t)(Arg4) != 0) goto loc_00BE694F;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1F8 + 0xC))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158))))));
    if (((uint32_t)(Arg1)) < 6) goto loc_00BE694F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x158)))) - (0));
    if (((uint32_t)(result)) < 6) goto loc_00BE694F;
    if ((*(uint8_t *)(local_rdi - 0x6)) != 76) goto loc_00BE694F;
    if ((*(uint8_t *)(local_rdi - 0x5)) != 135) goto loc_00BE694F;
    if ((*(uint8_t *)(local_rdi - 0x4)) != 0) goto loc_00BE694F;
    if ((*(uint8_t *)(local_rdi - 0x3)) != 152) goto loc_00BE694F;
    if ((*(uint8_t *)(local_rdi - 0x2)) != 195) goto loc_00BE694F;
    if (((uint8_t)(*(uint8_t *)(local_rdi - 0x1))) == 144) goto loc_00BE6887;
    if (((uint8_t)(*(uint8_t *)(local_rdi - 0x1))) != 241) goto loc_00BE694F;
loc_00BE6887:
    if (((*(uint8_t *)(local_rsp - 0x148 + 0x8)) & (8)) == 0) goto loc_00BE6E1E;
    result = (local_rdi) & ((uint32_t)(0xFFFULL));
    Arg1 = (local_r14 + 4095) + (result);
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    if (Arg1 != 0x1000ULL) goto loc_00BE68CE;
    result = (local_rdi) & (0xFFFFFFFFFFFFF000ULL);
    if (result == v_stack_m1D8) goto loc_00BE6E1E;
loc_00BE68CE:
    if ((uint32_t)(local_r14) == 0) goto loc_00BE6CC8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9DC)))) & (64)) == 0) goto loc_00BE6CC8;
    local_rsi = (local_rdi) & (0xFFFFFFFFFFFFF000ULL);
    local_r13 = (local_rdi - 1) + ((uint32_t)((uint32_t)(local_r14)));
    local_r13 = (local_r13) | ((uint32_t)(0xFFFULL));
loc_00BE6901:
loc_00BE690A:
    result = KeGuardDispatchICall(local_rsi, 1, 1, (uint32_t)(0xFFFULL));
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_00BE6C94;
    if (((uint8_t)(*(uint8_t *)(local_rsp - 0x148 + 0x150))) > 1) goto loc_00BE6C9F;
    goto loc_00BE6901;
loc_00BE6946:
    if ((uint32_t)((uint32_t)(0xFFFULL)) == 0) goto loc_00BE6887;
loc_00BE694F:
    if ((uint32_t)((uint32_t)(v_stack_m218)) == 0) goto loc_00BE6C80;
    Arg2 = (1) << (32);
    result = ((uint8_t)(*(uint8_t *)(local_rsp - 0x148 + 0x150))) | (Arg2);
    Arg2 = (result) ^ (result);
    *(uint64_t *)(local_rsp - 0x148 + 0xC0) = Arg2;
    Arg3 = (Arg2) ^ ((uint32_t)(0xFFFULL));
    Arg2 = (Arg2) >> (1);
    result = ((uint32_t)(0xFFFULL)) * (Arg2);
    Arg3 = (Arg3) - (result);
    if (Arg3 > 5) goto loc_00BE6A7C;
    if (Arg3 == 5) goto loc_00BE6A62;
    if (Arg3 == 0) goto loc_00BE6A47;
    result = (uint32_t)(((uint32_t)(Arg3)) - (1));
    if (condition_is_equal) goto loc_00BE6A28;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BE6A0C;
    if (((uint32_t)(result)) == 1) goto loc_00BE69E9;
    *(uint32_t *)(local_rsp - 0x148 + 0x88) = (uint32_t)((uint32_t)(0x70764946ULL));
    goto loc_00BE6A3F;
loc_00BE69E9:
    result = (uint32_t)(((uint32_t)(0x72775044ULL)) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x8C) = (uint32_t)(result);
    goto loc_00BE6BA7;
loc_00BE6A0C:
    *(uint32_t *)(local_rsp - 0x148 + 0x90) = (uint32_t)((uint32_t)(0x616D6443ULL));
    goto loc_00BE6BAA;
loc_00BE6A28:
    *(uint32_t *)(local_rsp - 0x148 + 0x94) = (uint32_t)((uint32_t)(0x655A6343ULL));
loc_00BE6A3F:
    goto loc_00BE6BAD;
loc_00BE6A47:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi - 1))) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x54) = (uint32_t)(result);
    goto loc_00BE6BA7;
loc_00BE6A62:
    *(uint32_t *)(local_rsp - 0x148 + 0x98) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x6944624FULL))));
    goto loc_00BE6BAA;
loc_00BE6A7C:
    result = (uint32_t)(((uint32_t)(Arg3)) - (6));
    if (condition_is_equal) goto loc_00BE6B91;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BE6B7B;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BE6B62;
    if (((uint32_t)(result)) == 1) goto loc_00BE6B44;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    *(uint64_t *)(local_rsp - 0x148 + 0x100) = Arg2;
    Arg4 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x148 + 0x98)))));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + (97));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg3 = (uint32_t)((Arg3) + (65));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg3 = (uint32_t)((Arg3) << (8));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + (97));
    Arg2 = (uint32_t)((Arg2) >> (3));
    Arg1 = (uint32_t)((Arg1) | (Arg3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg4 = (uint32_t)((Arg4) - ((uint32_t)(result)));
    Arg4 = (uint32_t)((Arg4) + (65));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(Arg1)));
    goto loc_00BE6BAD;
loc_00BE6B44:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x9C) = (uint32_t)(result);
    goto loc_00BE6BA7;
loc_00BE6B62:
    *(uint32_t *)(local_rsp - 0x148 + 0xA0) = (uint32_t)((uint32_t)(0x42646641ULL));
    goto loc_00BE6BAA;
loc_00BE6B7B:
    *(uint32_t *)(local_rsp - 0x148) = (uint32_t)((uint32_t)(0x63536C41ULL));
    goto loc_00BE6A3F;
loc_00BE6B91:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(local_rsp - 0x148 + 0x150)))) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x4) = (uint32_t)(result);
loc_00BE6BA7:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x148 + 0x4))) ^ (Arg3));
loc_00BE6BAA:
loc_00BE6BAD:
    result = KeGuardDispatchICall(80 - 16, 80, (uint32_t)((uint32_t)(Arg4)), Arg4);
    Arg1 = 0;
    local_rdi = local_rsp - 328 - 88;
    if (result != 0) { local_rdi = result; }
    *(uint64_t *)(local_rdi) = local_rsp - 328 - 128;
    *(uint64_t *)(local_rdi + 0x8) = *(uint64_t *)(local_rsp - 0x148 + 0x168);
    *(uint64_t *)(local_rdi + 0x10) = v_stack_m1F0;
    *(uint64_t *)(local_rdi + 0x18) = v_stack_m1E8;
    *(uint64_t *)(local_rdi + 0x40) = v_rip + 42640;
    *(uint32_t *)(local_rdi + 0x20) = (uint32_t)((uint32_t)(v_stack_m218));
    *(uint32_t *)(local_rdi + 0x28) = 0;
    *(uint64_t *)(local_rdi + 0x48) = local_rdi;
    *(uint64_t *)(local_rdi + 0x30) = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1 + 1))) + ((uint32_t)(Arg1 + 1)));
    if (((uint32_t)(result)) != ((uint32_t)(Arg1 + 1))) goto loc_00BE6C35;
    if ((*(uint32_t *)(local_rsp - 0x148 - 0x5C)) != 0) {
        Arg3 = 0;
        Arg1 = local_rsp - 328 - 120;
        Arg2 = 0;
        result = KeWaitForGate(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x148 - 0x5C) = (uint32_t)(Arg1 + 1);
    result = ExQueueWorkItem(local_rdi + 48, Arg2, Arg3, Arg4);
    local_r11 = 0;
    if (local_rdi != (local_rsp - 328 - 88)) goto loc_00BE6C7B;
    if ((*(uint32_t *)(local_rsp - 0x148 - 0x5C)) == 0) goto loc_00BE6C7B;
loc_00BE6C56:
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForGate(local_rsp - 328 - 120, Arg2, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x148 - 0x60))) != 0) goto loc_00BE6C56;
    local_r11 = 0;
    *(uint32_t *)(local_rsp - 0x148 - 0x5C) = 0;
loc_00BE6C7B:
    v_stack_m218 = 0;
loc_00BE6C80:
    *(uint32_t *)(v_stack_m208) = 0x80000000ULL;
loc_00BE6C8B:
    goto loc_00BE7278;
loc_00BE6C94:
    local_r11 = 0;
    if (sign_flag) goto loc_00BE6CC0;
loc_00BE6C9F:
    local_rsi = ((uint32_t)(v_stack_m218)) + ((uint32_t)(0x1000ULL));
    local_r12 = ((uint32_t)(0x63426343ULL)) + ((uint32_t)(0x1000ULL));
    if (local_r12 != local_r13) goto loc_00BE690A;
    goto loc_00BE6DFB;
loc_00BE6CC0:
loc_00BE6CC8:
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x918)) != 0) goto loc_00BE6DFB;
    result = ((uint8_t)(*(uint8_t *)(local_rsp - 0x148 + 0x150))) + ((uint32_t)(*(uint32_t *)(result + 0x944)));
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x920) = result;
    if (v_stack_m1E0 == 0) goto loc_00BE6D0C;
    result = (result) + (v_stack_m1E0);
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x928) = result;
    goto loc_00BE6D16;
loc_00BE6D0C:
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x928) = 0;
loc_00BE6D16:
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x930) = 0;
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x938) = (uint32_t)(v_stack_m218);
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x918) = 1;
    if (condition_is_below) goto loc_00BE6DFB;
    if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BE6DFB;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x9D8))))) == 0) goto loc_00BE6DFB;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE6DA4;
loc_00BE6D83:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA74)) + (uint32_t)(*(uint32_t *)(result + 0x944)) * 1)) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA78))) & (63));
    Arg3 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA78)) + (result);
    Arg3 = (Arg3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA74)) + (uint32_t)(*(uint32_t *)(result + 0x944)) * 1) + (8);
loc_00BE6DA4:
    if (Arg2 != ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA74)) + (uint32_t)(*(uint32_t *)(result + 0x944)) * 1 + Arg1 * 8)) goto loc_00BE6D83;
    if (Arg3 == (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA80))) goto loc_00BE6DFB;
    *(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x588)) = (uint32_t)(*(uint32_t *)(result + 0x944));
    *(uint32_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x804)));
    result = *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x588);
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x918)) == 0) {
        result = *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x588);
        Arg1 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0xA80)) ^ (Arg3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384((uint32_t)(*(uint32_t *)(result + 0x944)), Arg2, Arg3, 256);
loc_00BE6DFB:
    result = ((uint32_t)((uint32_t)(Arg1 + 1))) + ((uint32_t)(v_stack_m218));
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m1D8 = result;
loc_00BE6E1E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x148 + 0x150))) != 0) goto loc_00BE6F47;
    Arg1 = ((uint32_t)((uint32_t)(Arg1 + 1))) + ((uint32_t)(v_stack_m218));
    if (((uint32_t)(v_stack_m218)) >= Arg1) goto loc_00BE6E60;
loc_00BE6E54:
    result = ((uint32_t)(v_stack_m218)) + (64);
    if (result < Arg1) goto loc_00BE6E54;
loc_00BE6E60:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(Arg1 + 1))) >> (7));
    if ((uint32_t)(local_r11) == 0) goto loc_00BE6EDC;
loc_00BE6E7F:
loc_00BE6E84:
    Arg3 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838)) ^ (*(uint64_t *)((uint32_t)(v_stack_m218)));
    Arg3 = (Arg3) ^ (*(uint64_t *)((uint32_t)(v_stack_m218) + 0x8));
    Arg4 = ((uint32_t)(v_stack_m218)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BE6E84;
    Arg1 = (Arg4) - ((uint32_t)(v_stack_m218));
    Arg1 = (Arg1) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    result = (uint32_t)(((uint32_t)(0x58434F46ULL)) ^ (0));
    *(uint64_t *)(local_rsp - 0x148 + 0xC8) = 0;
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x834))) ^ ((uint32_t)(result)));
    local_r10 = (uint32_t)((local_r10) & (63));
    if (condition_is_equal) { local_r10 = 1; }
    local_r11 = (uint32_t)((local_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BE6E7F;
loc_00BE6EDC:
    local_r14 = (uint32_t)((Arg1 + 1) & (127));
    if (((uint32_t)(local_r14)) < 8) goto loc_00BE6F09;
    result = ((uint32_t)((uint32_t)(local_r14))) >> (3);
loc_00BE6EF3:
    Arg3 = (Arg3) ^ (*(uint64_t *)(Arg4));
    Arg4 = (Arg4) + (8);
    local_r14 = (uint32_t)((local_r14) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE6EF3;
loc_00BE6F09:
    if ((uint32_t)(local_r14) == 0) goto loc_00BE6F24;
loc_00BE6F0E:
    Arg3 = (Arg3) ^ (*(uint8_t *)(Arg4));
    Arg4 = (Arg4) + (1);
    local_r14 = (uint32_t)((local_r14) + (-1));
    if (condition_is_not_equal) goto loc_00BE6F0E;
loc_00BE6F24:
    goto loc_00BE6F2C;
loc_00BE6F29:
    Arg3 = (uint32_t)((Arg3) ^ (Arg3));
loc_00BE6F2C:
    result = (Arg3) >> (31);
    if (result != 0) goto loc_00BE6F29;
    *(uint32_t *)(v_stack_m208) = Arg3;
    goto loc_00BE6C8B;
loc_00BE6F47:
    if ((uint32_t)((uint32_t)(v_stack_m218)) != 0) goto loc_00BE6F6D;
    v_stack_m1F0 = *(uint64_t *)(local_rsp - 0x148 + 0x158);
    v_stack_m1E8 = v_stack_m208;
    goto loc_00BE6F77;
loc_00BE6F6D:
loc_00BE6F77:
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m218)) + 1);
    v_stack_m218 = (uint32_t)(local_rdi);
    if (((uint32_t)(local_rdi)) < Arg3) goto loc_00BE727F;
    Arg2 = (*(uint64_t *)(local_rsp - 0x148 + 0x158)) << (32);
    result = (v_stack_m208) | (Arg2);
    Arg2 = (result) ^ (result);
    *(uint64_t *)(local_rsp - 0x148 + 0xD0) = Arg2;
    Arg3 = (Arg2) ^ (Arg4);
    Arg2 = (Arg2) >> (1);
    result = (Arg4) * (Arg2);
    Arg3 = (Arg3) - (result);
    if (Arg3 > 5) goto loc_00BE7087;
    if (Arg3 == 5) goto loc_00BE7071;
    if (Arg3 == 0) goto loc_00BE7056;
    result = (uint32_t)(((uint32_t)(Arg3)) - (1));
    if (condition_is_equal) goto loc_00BE703D;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BE7027;
    if (((uint32_t)(result)) == 1) goto loc_00BE700A;
    *(uint32_t *)(local_rsp - 0x148 + 0xC) = (uint32_t)((uint32_t)(0x70764946ULL));
    goto loc_00BE704E;
loc_00BE700A:
    result = (uint32_t)(((uint32_t)(0x72775044ULL)) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x10) = (uint32_t)(result);
    goto loc_00BE71A6;
loc_00BE7027:
    *(uint32_t *)(local_rsp - 0x148 + 0x14) = (uint32_t)((uint32_t)(0x616D6443ULL));
    goto loc_00BE71A9;
loc_00BE703D:
    *(uint32_t *)(local_rsp - 0x148 + 0x18) = (uint32_t)((uint32_t)(0x655A6343ULL));
loc_00BE704E:
    goto loc_00BE71AC;
loc_00BE7056:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x63426343ULL)))) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x1C) = (uint32_t)(result);
    goto loc_00BE71A6;
loc_00BE7071:
    *(uint32_t *)(local_rsp - 0x148 + 0x20) = (uint32_t)((uint32_t)(0x6944624FULL));
    goto loc_00BE71A9;
loc_00BE7087:
    result = (uint32_t)(((uint32_t)(Arg3)) - (6));
    if (condition_is_equal) goto loc_00BE7190;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BE717A;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BE7167;
    if (((uint32_t)(result)) == 1) goto loc_00BE714F;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    *(uint64_t *)(local_rsp - 0x148 + 0xD8) = Arg2;
    Arg4 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x148 + 0x20)))));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + (97));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg3 = (uint32_t)((Arg3) + (65));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg3 = (uint32_t)((Arg3) << (8));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + (97));
    Arg2 = (uint32_t)((Arg2) >> (3));
    Arg1 = (uint32_t)((Arg1) | (Arg3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg4 = (uint32_t)((Arg4) - ((uint32_t)(result)));
    Arg4 = (uint32_t)((Arg4) + (65));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(Arg1)));
    goto loc_00BE71AC;
loc_00BE714F:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x58434F46ULL)))) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x24) = (uint32_t)(result);
    goto loc_00BE71A6;
loc_00BE7167:
    *(uint32_t *)(local_rsp - 0x148 + 0x28) = (uint32_t)((uint32_t)(0x42646641ULL));
    goto loc_00BE71A9;
loc_00BE717A:
    *(uint32_t *)(local_rsp - 0x148 + 0x2C) = (uint32_t)((uint32_t)(0x63536C41ULL));
    goto loc_00BE704E;
loc_00BE7190:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x5746744EULL)))) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x30) = (uint32_t)(result);
loc_00BE71A6:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x148 + 0x30))) ^ (Arg3));
loc_00BE71A9:
loc_00BE71AC:
    result = KeGuardDispatchICall(80 - 16, 80, (uint32_t)((uint32_t)(Arg4)), Arg4);
    local_rdi = local_rsp - 328 - 88;
    if (result != 0) { local_rdi = result; }
    *(uint64_t *)(local_rdi) = local_rsp - 328 - 128;
    *(uint64_t *)(local_rdi + 0x8) = *(uint64_t *)(local_rsp - 0x148 + 0x168);
    *(uint64_t *)(local_rdi + 0x18) = v_stack_m1E8;
    local_r14 = 0;
    *(uint64_t *)(local_rdi + 0x10) = v_stack_m1F0;
    *(uint64_t *)(local_rdi + 0x40) = v_rip + 41129;
    *(uint32_t *)(local_rdi + 0x20) = (uint32_t)((uint32_t)(v_stack_m218));
    *(uint32_t *)(local_rdi + 0x28) = 0;
    *(uint64_t *)(local_rdi + 0x48) = local_rdi;
    *(uint64_t *)(local_rdi + 0x30) = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14 + 1))) + ((uint32_t)(local_r14 + 1)));
    if (((uint32_t)(result)) != ((uint32_t)(local_r14 + 1))) goto loc_00BE7232;
    if ((*(uint32_t *)(local_rsp - 0x148 - 0x5C)) != 0) {
        Arg3 = 0;
        Arg1 = local_rsp - 328 - 120;
        Arg2 = 0;
        result = KeWaitForGate(Arg1, Arg2, Arg3, Arg4);
        Arg1 = local_r14 + 1;
    }
    *(uint32_t *)(local_rsp - 0x148 - 0x5C) = (uint32_t)(Arg1);
    Arg2 = 0;
    result = ExQueueWorkItem(local_rdi + 48, Arg2, Arg3, Arg4);
    if (local_rdi != (local_rsp - 328 - 88)) goto loc_00BE726B;
    if ((*(uint32_t *)(local_rsp - 0x148 - 0x5C)) == 0) goto loc_00BE726B;
loc_00BE724F:
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForGate(local_rsp - 328 - 120, Arg2, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x148 - 0x60))) != 0) goto loc_00BE724F;
    *(uint32_t *)(local_rsp - 0x148 - 0x5C) = 0;
loc_00BE726B:
    v_stack_m218 = 0;
loc_00BE7278:
loc_00BE727F:
    local_r14 = (*(uint64_t *)(local_rsp - 0x148 + 0x158)) + (12);
    *(uint64_t *)(local_rsp - 0x148 + 0x158) = local_r14;
    if (local_r14 == (*(uint64_t *)(local_rsp - 0x148 + 0xB0))) goto loc_00BE7305;
    result = (v_stack_m208) + (4);
    v_stack_m208 = result;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1F8 + 0xC))))) goto loc_00BE72CF;
    if ((*(uint32_t *)(local_r14 + 0x4)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x148 + 0x34))))) goto loc_00BE67CD;
loc_00BE72CF:
    result = KeGuardDispatchICall(v_stack_m200, *(uint64_t *)(local_rsp - 0x148 + 0x168), (uint32_t)(*(uint32_t *)(local_r14)), (uint32_t)(v_stack_m210));
    Arg2 = 0;
    v_stack_m1F8 = result;
    if (result == 0) goto loc_00BE7657;
    goto loc_00BE6607;
loc_00BE7305:
    if (((uint32_t)((uint32_t)(v_stack_m20C))) == -1) {
        result = v_stack_m214;
        result = (uint32_t)(-(result));
        Arg2 = (uint32_t)(((uint32_t)(v_stack_m20C)) & ((uint32_t)(v_stack_m200)));
    }
    local_rsi = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x178)) = (uint32_t)(Arg2);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x148 + 0x180)) = (uint32_t)((uint32_t)(v_stack_m214));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14))) == 0) goto loc_00BE6552;
    if (0 == 0) goto loc_00BE7631;
    Arg2 = (Arg2) << (32);
    result = (*(uint64_t *)(local_rsp - 0x148 + 0x180)) | (Arg2);
    Arg2 = (result) ^ (result);
    *(uint64_t *)(local_rsp - 0x148 + 0xE0) = Arg2;
    Arg3 = (Arg2) ^ ((uint32_t)(v_stack_m210));
    Arg2 = (Arg2) >> (1);
    result = ((uint32_t)(v_stack_m210)) * (Arg2);
    Arg3 = (Arg3) - (result);
    if (Arg3 > 5) goto loc_00BE7441;
    if (Arg3 == 5) goto loc_00BE742B;
    if (Arg3 == 0) goto loc_00BE7411;
    result = (uint32_t)(((uint32_t)(Arg3)) - (1));
    if (condition_is_equal) goto loc_00BE73F8;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BE73E2;
    if (((uint32_t)(result)) == 1) goto loc_00BE73C5;
    *(uint32_t *)(local_rsp - 0x148 + 0x38) = (uint32_t)((uint32_t)(0x70764946ULL));
    goto loc_00BE7409;
loc_00BE73C5:
    result = (uint32_t)(((uint32_t)(0x72775044ULL)) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x3C) = (uint32_t)(result);
    goto loc_00BE7567;
loc_00BE73E2:
    *(uint32_t *)(local_rsp - 0x148 + 0x40) = (uint32_t)((uint32_t)(0x616D6443ULL));
    goto loc_00BE756A;
loc_00BE73F8:
    *(uint32_t *)(local_rsp - 0x148 + 0x44) = (uint32_t)((uint32_t)(0x655A6343ULL));
loc_00BE7409:
    goto loc_00BE756D;
loc_00BE7411:
    local_r12 = (uint32_t)(((uint32_t)(0x63426343ULL)) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x48) = (uint32_t)(local_r12);
    goto loc_00BE7567;
loc_00BE742B:
    *(uint32_t *)(local_rsp - 0x148 + 0x4C) = (uint32_t)((uint32_t)(0x6944624FULL));
    goto loc_00BE756A;
loc_00BE7441:
    Arg1 = (uint32_t)(((uint32_t)(Arg3)) - (6));
    if (condition_is_equal) goto loc_00BE7552;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BE753C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BE7523;
    if (((uint32_t)(Arg1)) == 1) goto loc_00BE750C;
    Arg2 = (Arg2) << (32);
    result = ((uint32_t)(0x6944624FULL)) | (Arg2);
    Arg2 = (result) ^ (result);
    *(uint64_t *)(local_rsp - 0x148 + 0xE8) = Arg2;
    local_r10 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(v_stack_m210))));
    local_r10 = (uint32_t)((local_r10) >> (5));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(result)));
    local_r10 = (uint32_t)((local_r10) >> (5));
    Arg1 = (uint32_t)((Arg1) + (97));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(result)));
    local_r10 = (uint32_t)((local_r10) >> (5));
    Arg3 = (uint32_t)((Arg3) + (65));
    Arg2 = (uint32_t)((Arg2) >> (3));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(Arg1)));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)(Arg2)));
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(Arg1)));
    Arg3 = (uint32_t)((Arg3) << (8));
    Arg4 = (uint32_t)((Arg4) + (97));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg4 = (uint32_t)((Arg4) | (Arg3));
    Arg4 = (uint32_t)((Arg4) << (8));
    local_r10 = (uint32_t)((local_r10) - ((uint32_t)(result)));
    local_r10 = (uint32_t)((local_r10) + (65));
    local_r10 = (uint32_t)((local_r10) | ((uint32_t)(Arg4)));
    goto loc_00BE756D;
loc_00BE750C:
    local_r13 = (uint32_t)(((uint32_t)(0x58434F46ULL)) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x50) = (uint32_t)(local_r13);
    goto loc_00BE7567;
loc_00BE7523:
    *(uint32_t *)(local_rsp - 0x148 + 0xA4) = (uint32_t)((uint32_t)(0x42646641ULL));
    goto loc_00BE756A;
loc_00BE753C:
    *(uint32_t *)(local_rsp - 0x148 + 0x58) = (uint32_t)((uint32_t)(0x63536C41ULL));
    goto loc_00BE7409;
loc_00BE7552:
    local_r15 = (uint32_t)(((uint32_t)(0x4EC4EC4FULL)) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x5C) = (uint32_t)(local_r15);
loc_00BE7567:
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x148 + 0x5C))) ^ (Arg3));
loc_00BE756A:
loc_00BE756D:
    result = KeGuardDispatchICall(80 - 16, 80, (uint32_t)((uint32_t)(local_r10)), Arg4);
    local_rbx = local_rsp - 328 - 88;
    if (result != 0) { local_rbx = result; }
    *(uint64_t *)(local_rbx) = local_rsp - 328 - 128;
    *(uint64_t *)(local_rbx + 0x8) = *(uint64_t *)(local_rsp - 0x148 + 0x168);
    *(uint64_t *)(local_rbx + 0x10) = v_stack_m1F0;
    *(uint64_t *)(local_rbx + 0x18) = v_stack_m1E8;
    *(uint64_t *)(local_rbx + 0x40) = v_rip + 40144;
    *(uint32_t *)(local_rbx + 0x20) = 0;
    *(uint32_t *)(local_rbx + 0x28) = 0;
    *(uint64_t *)(local_rbx + 0x48) = local_rbx;
    *(uint64_t *)(local_rbx + 0x30) = 0;
    result = (uint32_t)((1) + (1));
    if (((uint32_t)(result)) != 1) goto loc_00BE75F5;
    if ((*(uint32_t *)(local_rsp - 0x148 - 0x5C)) != 0) {
        Arg3 = 0;
        Arg1 = local_rsp - 328 - 120;
        Arg2 = 0;
        result = KeWaitForGate(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x148 - 0x5C) = 1;
    result = ExQueueWorkItem(local_rbx + 48, Arg2, Arg3, Arg4);
    if (local_rbx != (local_rsp - 328 - 88)) goto loc_00BE7631;
    if ((*(uint32_t *)(local_rsp - 0x148 - 0x5C)) == 0) goto loc_00BE6552;
loc_00BE7616:
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForGate(local_rsp - 328 - 120, Arg2, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x148 - 0x60))) != 0) goto loc_00BE7616;
    *(uint32_t *)(local_rsp - 0x148 - 0x5C) = 0;
loc_00BE7631:
    if ((*(uint32_t *)(local_rsp - 0x148 - 0x5C)) == 0) goto loc_00BE6552;
loc_00BE763A:
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForGate(local_rsp - 328 - 120, Arg2, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x148 - 0x60))) != 0) goto loc_00BE763A;
    goto loc_00BE6552;
loc_00BE7657:
loc_00BE7666:
    if (condition_is_above_or_equal) goto loc_00BE7AC7;
    if ((*(uint32_t *)(local_rbx + 0x918)) != 0) goto loc_00BE7783;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x148 - 0x60))) + (local_rbx);
    *(uint64_t *)(local_rbx + 0x928) = 0;
    *(uint64_t *)(local_rbx + 0x920) = result;
    *(uint64_t *)(local_rbx + 0x930) = 271;
    *(uint64_t *)(local_rbx + 0x938) = *(uint64_t *)(local_rsp - 0x148 + 0x168);
    *(uint32_t *)(local_rbx + 0x918) = 1;
    if (condition_is_below) goto loc_00BE7783;
    if (((*(uint32_t *)(local_rbx + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BE7783;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x9D8))))) == 0) goto loc_00BE7783;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE7729;
loc_00BE7708:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(local_rbx + 0xA74)) + local_rbx * 1)) ^ (*(uint64_t *)(local_rbx + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(local_rbx + 0xA78))) & (63));
    Arg3 = (*(uint64_t *)(local_rbx + 0xA78)) + (result);
    Arg3 = (Arg3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(local_rbx + 0xA74)) + local_rbx * 1) + (8);
loc_00BE7729:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(local_rbx + 0xA74)) + local_rbx * 1 + Arg1 * 8)) goto loc_00BE7708;
    if (Arg3 == (*(uint64_t *)(local_rbx + 0xA80))) goto loc_00BE7781;
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x588)) = local_rbx;
    *(uint32_t *)(*(uint64_t *)(local_rbx + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x804)));
    result = 0;
    if ((*(uint32_t *)(local_rbx + 0x918)) == 0) {
        result = *(uint64_t *)(local_rbx + 0x588);
        Arg1 = (*(uint64_t *)(local_rbx + 0xA80)) ^ (Arg3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(local_rbx, Arg2, Arg3, 256);
loc_00BE7781:
    Arg2 = 0;
loc_00BE7783:
    if ((*(uint32_t *)(local_rsp - 0x148 + 0x150)) == 0) goto loc_00BE7AA6;
    if ((uint32_t)((uint32_t)(v_stack_m218)) == 0) goto loc_00BE7A89;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    *(uint64_t *)(local_rsp - 0x148 + 0xF0) = Arg2;
    Arg3 = (Arg2) ^ (256);
    Arg2 = (Arg2) >> (1);
    result = (256) * (Arg2);
    Arg3 = (Arg3) - (result);
    if (Arg3 > 5) goto loc_00BE7896;
    if (Arg3 == 5) goto loc_00BE7880;
    if (Arg3 == 0) goto loc_00BE7866;
    result = (uint32_t)(((uint32_t)(Arg3)) - (1));
    if (condition_is_equal) goto loc_00BE784D;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BE7837;
    if (((uint32_t)(result)) == 1) goto loc_00BE781F;
    *(uint32_t *)(local_rsp - 0x148 + 0x64) = (uint32_t)((uint32_t)(0x70764946ULL));
    goto loc_00BE785E;
loc_00BE781F:
    local_rdi = (uint32_t)(((uint32_t)(0x72775044ULL)) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x68) = (uint32_t)(local_rdi);
    goto loc_00BE79C4;
loc_00BE7837:
    *(uint32_t *)(local_rsp - 0x148 + 0x6C) = (uint32_t)((uint32_t)(0x616D6443ULL));
    goto loc_00BE79C7;
loc_00BE784D:
    *(uint32_t *)(local_rsp - 0x148 + 0x70) = (uint32_t)((uint32_t)(0x655A6343ULL));
loc_00BE785E:
    goto loc_00BE79CA;
loc_00BE7866:
    local_r12 = (uint32_t)((local_r12) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x74) = (uint32_t)(local_r12);
    goto loc_00BE79C4;
loc_00BE7880:
    *(uint32_t *)(local_rsp - 0x148 + 0x78) = (uint32_t)((uint32_t)(0x6944624FULL));
    goto loc_00BE79C7;
loc_00BE7896:
    result = (uint32_t)(((uint32_t)(Arg3)) - (6));
    if (condition_is_equal) goto loc_00BE79AD;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BE7991;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BE7978;
    if (((uint32_t)(result)) == 1) goto loc_00BE7961;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    *(uint64_t *)(local_rsp - 0x148 + 0xF8) = Arg2;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x148 + 0x78))) ^ ((uint32_t)(Arg2)));
    Arg2 = (uint32_t)((Arg2) >> (3));
    Arg1 = (uint32_t)((result) * ((uint32_t)(Arg2)));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(Arg1)));
    Arg3 = (uint32_t)((Arg3) + (97));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)((Arg3) << (8));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + (65));
    Arg1 = (uint32_t)((Arg1) | (Arg3));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg3 = (uint32_t)((Arg3) + (97));
    Arg2 = (uint32_t)((Arg2) >> (3));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(Arg1)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)((Arg3) << (8));
    Arg4 = (uint32_t)((Arg4) - ((uint32_t)(result)));
    Arg4 = (uint32_t)((Arg4) + (65));
    Arg4 = (uint32_t)((Arg4) | (Arg3));
    goto loc_00BE79CA;
loc_00BE7961:
    local_r13 = (uint32_t)((local_r13) ^ (Arg3));
    *(uint32_t *)(local_rsp - 0x148 + 0x7C) = (uint32_t)(local_r13);
    goto loc_00BE79C4;
loc_00BE7978:
    *(uint32_t *)(local_rsp - 0x148 + 0x80) = (uint32_t)((uint32_t)(0x42646641ULL));
    goto loc_00BE79C7;
loc_00BE7991:
    *(uint32_t *)(local_rsp - 0x148 + 0x84) = (uint32_t)((uint32_t)(0x63536C41ULL));
    goto loc_00BE785E;
loc_00BE79AD:
    local_r15 = (uint32_t)((local_r15) ^ (Arg3));
    v_stack_m200 = (uint32_t)(local_r15);
loc_00BE79C4:
    Arg4 = (uint32_t)(((uint32_t)(v_stack_m200)) ^ (Arg3));
loc_00BE79C7:
loc_00BE79CA:
    result = KeGuardDispatchICall(80 - 16, 80, (uint32_t)((uint32_t)(Arg4)), Arg4);
    local_r12 = 0;
    local_rbx = local_rsp - 328 - 88;
    if (result != 0) { local_rbx = result; }
    *(uint64_t *)(local_rbx) = local_rsp - 328 - 128;
    *(uint64_t *)(local_rbx + 0x10) = v_stack_m1F0;
    *(uint64_t *)(local_rbx + 0x18) = v_stack_m1E8;
    *(uint32_t *)(local_rbx + 0x20) = (uint32_t)((uint32_t)(v_stack_m218));
    *(uint64_t *)(local_rbx + 0x40) = v_rip + 39041;
    *(uint64_t *)(local_rbx + 0x8) = *(uint64_t *)(local_rsp - 0x148 + 0x168);
    *(uint32_t *)(local_rbx + 0x28) = 0;
    *(uint64_t *)(local_rbx + 0x48) = local_rbx;
    *(uint64_t *)(local_rbx + 0x30) = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12 + 1))) + ((uint32_t)(local_r12 + 1)));
    if (((uint32_t)(result)) != ((uint32_t)(local_r12 + 1))) goto loc_00BE7A4C;
    if ((*(uint32_t *)(local_rsp - 0x148 - 0x5C)) != 0) {
        Arg3 = 0;
        Arg1 = local_rsp - 328 - 120;
        Arg2 = 0;
        result = KeWaitForGate(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x148 - 0x5C) = (uint32_t)(local_r12 + 1);
    result = ExQueueWorkItem(local_rbx + 48, Arg2, Arg3, Arg4);
    if (local_rbx != (local_rsp - 328 - 88)) goto loc_00BE7A89;
    if ((*(uint32_t *)(local_rsp - 0x148 - 0x5C)) == 0) goto loc_00BE7AA6;
loc_00BE7A69:
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForGate(local_rsp - 328 - 120, Arg2, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x148 - 0x60))) != 0) goto loc_00BE7A69;
    *(uint32_t *)(local_rsp - 0x148 - 0x5C) = 0;
    goto loc_00BE7AA2;
loc_00BE7A89:
    goto loc_00BE7AA2;
loc_00BE7A8E:
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForGate(local_rsp - 328 - 120, Arg2, Arg3, Arg4);
loc_00BE7AA2:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x148 - 0x60))) != 0) goto loc_00BE7A8E;
loc_00BE7AA6:
loc_00BE7AAB:
    local_rsp = (local_rsp) + (528);
    return (uint32_t)(0xC000007BULL);
loc_00BE7AC7:
    v_stack_p20 = 0;
    *(uint32_t *)(local_rsp - 0x148 + 0x60) = 0xE8000009ULL;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0x148 + 0x60)), 8 + 2, *(uint64_t *)(local_rsp - 0x148 + 0x168), 8);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=initkdbg&rva=0x00BE60B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
