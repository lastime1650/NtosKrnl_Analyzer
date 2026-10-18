# AlpcpProcessSynchronousRequest

- RVA: `0x00921FCC`–`0x009224DE` (길이 `1,298` bytes)
- VA: `0x0000000140921FCC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008D0EC`
- 디코드: `299`개 명령, `1,298/1,298` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00922006` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009220B5` → [AlpcpSendMessage](../88/AlpcpSendMessage_function_0088BD40.md) (function, `0x0088BD40`)
- `0x00922116` → [AlpcpReceiveSynchronousReply](AlpcpReceiveSynchronousReply_function_009224F0.md) (function, `0x009224F0`)
- `0x009221CF` → [AlpcpGetDataFromMessage](AlpcpGetDataFromMessage_function_00922958.md) (function, `0x00922958`)
- `0x00922205` → [AlpcpExposeAttributes](../89/AlpcpExposeAttributes_function_00897630.md) (function, `0x00897630`)
- `0x009222D9` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0092232A` → [AlpcMessageCleanupProcedure](../88/AlpcMessageCleanupProcedure_function_0088BBA0.md) (function, `0x0088BBA0`)
- `0x0092233B` → [AlpcpEnterFreeEventMessageLog](../AC/AlpcpEnterFreeEventMessageLog_function_00ACCBB8.md) (function, `0x00ACCBB8`)
- `0x00922367` → [AlpcpProbeForWriteMessageHeader](../89/AlpcpProbeForWriteMessageHeader_function_00898660.md) (function, `0x00898660`)
- `0x009223AC` → [AlpcpProbeMessageAttributes](../89/AlpcpProbeMessageAttributes_function_008995A0.md) (function, `0x008995A0`)
- `0x00922401` → [AlpcpSendLegacySynchronousRequest](AlpcpSendLegacySynchronousRequest_function_0092376C.md) (function, `0x0092376C`)
- `0x0092241C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0092243D` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0092245C` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (function, `0x0041DAE0`)
- `0x00922478` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00922496` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x009224D4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [NtReplyWaitReplyPort](../74/NtReplyWaitReplyPort_function_0074BFB0.md) at `0x0074C06C`
- [sub_00868100](../86/Unknown_function_00868100.md) at `0x00868239`
- [NtRequestWaitReplyPort](NtRequestWaitReplyPort_function_00921E40.md) at `0x00921ED9`
- [LpcSendWaitReceivePort](LpcSendWaitReceivePort_function_00921F50.md) at `0x00921F95`

### Static image references
- `0x0092232F` → RVA `0x00F100D0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00922006` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0092241C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0092243D` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0092245C` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (`PAGE` → `.text`)
  - `0x00922478` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00922496` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x009224D4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x009223EE` → [sub_00B226A4 + 0x27](../B2/Unknown_function_00B226A4.md) (`tail-transfer`)
  - `0x0092246F` → [sub_00B226A4 + 0x15](../B2/Unknown_function_00B226A4.md) (`tail-transfer`)
  - `0x0092247E` → [sub_00B226A4 + 0x15](../B2/Unknown_function_00B226A4.md) (`tail-transfer`)
  - `0x0092248D` → [sub_00B226A4](../B2/Unknown_function_00B226A4.md) (`tail-transfer`)
  - `0x0092249C` → [sub_00B226A4](../B2/Unknown_function_00B226A4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00921FCC  48 8B C4                        mov rax, rsp
00921FCF  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00921FD3  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00921FD7  48 89 48 08                     mov qword ptr [rax + 8], rcx
00921FDB  53                              push rbx
00921FDC  56                              push rsi
00921FDD  57                              push rdi
00921FDE  41 54                           push r12
00921FE0  41 55                           push r13
00921FE2  41 56                           push r14
00921FE4  41 57                           push r15
00921FE6  48 81 EC D0 00 00 00            sub rsp, 0xd0
00921FED  4D 8B E0                        mov r12, r8
00921FF0  44 8B EA                        mov r13d, edx
00921FF3  4C 8B F9                        mov r15, rcx
00921FF6  33 FF                           xor edi, edi
00921FF8  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00921FFC  33 D2                           xor edx, edx
00921FFE  44 8D 47 40                     lea r8d, [rdi + 0x40]
00922002  48 8D 48 88                     lea rcx, [rax - 0x78]
00922006  E8 35 4C DA FF                  call 0x1406c6c40
0092200B  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00922010  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00922014  48 83 4C 24 50 FF               or qword ptr [rsp + 0x50], 0xffffffffffffffff
0092201A  40 38 BC 24 50 01 00 00         cmp byte ptr [rsp + 0x150], dil
00922022  0F 85 1A 03 00 00               jne 0x140922342
00922028  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
00922030  48 85 C9                        test rcx, rcx
00922033  74 08                           je 0x14092203d
00922035  48 8B 01                        mov rax, qword ptr [rcx]
00922038  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0092203D  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
00922045  4C 8B B4 24 30 01 00 00         mov r14, qword ptr [rsp + 0x130]
0092204D  48 85 C9                        test rcx, rcx
00922050  74 06                           je 0x140922058
00922052  8B 01                           mov eax, dword ptr [rcx]
00922054  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00922058  49 8D 87 A0 01 00 00            lea rax, [r15 + 0x1a0]
0092205F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00922064  8B 00                           mov eax, dword ptr [rax]
00922066  83 E0 06                        and eax, 6
00922069  3C 06                           cmp al, 6
0092206B  0F 84 9A 03 00 00               je 0x14092240b
00922071  49 8B F7                        mov rsi, r15
00922074  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
00922079  4C 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r15
00922081  44 89 AC 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r13d
00922089  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0092208E  44 8A 8C 24 50 01 00 00         mov r9b, byte ptr [rsp + 0x150]
00922096  F7 00 00 10 00 00               test dword ptr [rax], 0x1000
0092209C  0F 85 51 03 00 00               jne 0x1409223f3
009220A2  4C 8B 84 24 28 01 00 00         mov r8, qword ptr [rsp + 0x128]
009220AA  49 8B D4                        mov rdx, r12
009220AD  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
009220B5  E8 86 9C F6 FF                  call 0x14088bd40
009220BA  44 8B E0                        mov r12d, eax
009220BD  85 C0                           test eax, eax
009220BF  0F 88 19 02 00 00               js 0x1409222de
009220C5  41 0F BA E5 14                  bt r13d, 0x14
009220CA  0F 82 D1 03 00 00               jb 0x1409224a1
009220D0  41 0F BA E5 19                  bt r13d, 0x19
009220D5  0F 82 CD 03 00 00               jb 0x1409224a8
009220DB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009220E4  8A 90 32 02 00 00               mov dl, byte ptr [rax + 0x232]
009220EA  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
009220EF  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
009220F7  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
009220FF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00922104  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
00922109  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
0092210E  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
00922116  E8 D5 03 00 00                  call 0x1409224f0
0092211B  44 8B E0                        mov r12d, eax
0092211E  85 C0                           test eax, eax
00922120  0F 85 B8 01 00 00               jne 0x1409222de
00922126  45 85 ED                        test r13d, r13d
00922129  0F 88 8B 03 00 00               js 0x1409224ba
0092212F  B8 28 00 00 00                  mov eax, 0x28
00922134  8D 48 F0                        lea ecx, [rax - 0x10]
00922137  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0092213C  0F B7 93 F0 00 00 00            movzx edx, word ptr [rbx + 0xf0]
00922143  03 C2                           add eax, edx
00922145  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00922149  48 39 BC 24 38 01 00 00         cmp qword ptr [rsp + 0x138], rdi
00922151  0F 85 8C 02 00 00               jne 0x1409223e3
00922157  89 BC 24 50 01 00 00            mov dword ptr [rsp + 0x150], edi
0092215E  41 8B C5                        mov eax, r13d
00922161  25 00 00 00 C0                  and eax, 0xc0000000
00922166  3D 00 00 00 80                  cmp eax, 0x80000000
0092216B  0F 84 A7 00 00 00               je 0x140922218
00922171  0F 10 83 F0 00 00 00            movups xmm0, xmmword ptr [rbx + 0xf0]
00922178  41 0F 11 06                     movups xmmword ptr [r14], xmm0
0092217C  0F 10 8B 00 01 00 00            movups xmm1, xmmword ptr [rbx + 0x100]
00922183  41 0F 11 4E 10                  movups xmmword ptr [r14 + 0x10], xmm1
00922188  F2 0F 10 83 10 01 00 00         movsd xmm0, qword ptr [rbx + 0x110]
00922190  F2 41 0F 11 46 20               movsd qword ptr [r14 + 0x20], xmm0
00922196  41 0F BA A7 00 01 00 00 0C      bt dword ptr [r15 + 0x100], 0xc
0092219F  73 14                           jae 0x1409221b5
009221A1  0F B7 83 F4 00 00 00            movzx eax, word ptr [rbx + 0xf4]
009221A8  BA 0F C0 FF FF                  mov edx, 0xffffc00f
009221AD  66 23 C2                        and ax, dx
009221B0  66 41 89 46 04                  mov word ptr [r14 + 4], ax
009221B5  0F B7 83 F2 00 00 00            movzx eax, word ptr [rbx + 0xf2]
009221BC  89 84 24 50 01 00 00            mov dword ptr [rsp + 0x150], eax
009221C3  B9 28 00 00 00                  mov ecx, 0x28
009221C8  4A 8D 14 31                     lea rdx, [rcx + r14]
009221CC  48 8B CB                        mov rcx, rbx
009221CF  E8 84 07 00 00                  call 0x140922958
009221D4  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
009221DC  48 85 C9                        test rcx, rcx
009221DF  75 2E                           jne 0x14092220f
009221E1  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
009221E9  48 85 C0                        test rax, rax
009221EC  0F 84 C2 00 00 00               je 0x1409222b4
009221F2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009221F7  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
009221FC  4C 8B C3                        mov r8, rbx
009221FF  41 8B D5                        mov edx, r13d
00922202  49 8B CF                        mov rcx, r15
00922205  E8 26 54 F7 FF                  call 0x140897630
0092220A  E9 A5 00 00 00                  jmp 0x1409222b4
0092220F  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
00922213  48 89 11                        mov qword ptr [rcx], rdx
00922216  EB C9                           jmp 0x1409221e1
00922218  66 41 89 16                     mov word ptr [r14], dx
0092221C  0F B7 83 F0 00 00 00            movzx eax, word ptr [rbx + 0xf0]
00922223  03 C1                           add eax, ecx
00922225  89 84 24 50 01 00 00            mov dword ptr [rsp + 0x150], eax
0092222C  66 41 89 46 02                  mov word ptr [r14 + 2], ax
00922231  0F B7 83 F6 00 00 00            movzx eax, word ptr [rbx + 0xf6]
00922238  66 85 C0                        test ax, ax
0092223B  75 6C                           jne 0x1409222a9
0092223D  66 41 89 7E 06                  mov word ptr [r14 + 6], di
00922242  BA 00 10 00 00                  mov edx, 0x1000
00922247  44 8B C2                        mov r8d, edx
0092224A  66 44 0B 83 F4 00 00 00         or r8w, word ptr [rbx + 0xf4]
00922252  66 45 89 46 04                  mov word ptr [r14 + 4], r8w
00922257  8B 83 F8 00 00 00               mov eax, dword ptr [rbx + 0xf8]
0092225D  41 89 46 08                     mov dword ptr [r14 + 8], eax
00922261  8B 83 00 01 00 00               mov eax, dword ptr [rbx + 0x100]
00922267  41 89 46 0C                     mov dword ptr [r14 + 0xc], eax
0092226B  8B 83 08 01 00 00               mov eax, dword ptr [rbx + 0x108]
00922271  41 89 46 10                     mov dword ptr [r14 + 0x10], eax
00922275  8B 83 10 01 00 00               mov eax, dword ptr [rbx + 0x110]
0092227B  41 89 46 14                     mov dword ptr [r14 + 0x14], eax
0092227F  8B 83 10 01 00 00               mov eax, dword ptr [rbx + 0x110]
00922285  41 89 46 14                     mov dword ptr [r14 + 0x14], eax
00922289  41 85 97 00 01 00 00            test dword ptr [r15 + 0x100], edx
00922290  0F 84 32 FF FF FF               je 0x1409221c8
00922296  BA 0F C0 FF FF                  mov edx, 0xffffc00f
0092229B  66 44 23 C2                     and r8w, dx
0092229F  66 45 89 46 04                  mov word ptr [r14 + 4], r8w
009222A4  E9 1F FF FF FF                  jmp 0x1409221c8
009222A9  66 83 E8 10                     sub ax, 0x10
009222AD  66 41 89 46 06                  mov word ptr [r14 + 6], ax
009222B2  EB 8E                           jmp 0x140922242
009222B4  EB 17                           jmp 0x1409222cd
009222B6  44 8B E0                        mov r12d, eax
009222B9  33 FF                           xor edi, edi
009222BB  4C 8B BC 24 10 01 00 00         mov r15, qword ptr [rsp + 0x110]
009222C3  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
009222C8  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
009222CD  F7 43 28 00 02 00 00            test dword ptr [rbx + 0x28], 0x200
009222D4  75 28                           jne 0x1409222fe
009222D6  48 8B CB                        mov rcx, rbx
009222D9  E8 02 58 F7 FF                  call 0x140897ae0
009222DE  49 3B F7                        cmp rsi, r15
009222E1  0F 85 EA 01 00 00               jne 0x1409224d1
009222E7  41 8B C4                        mov eax, r12d
009222EA  48 81 C4 D0 00 00 00            add rsp, 0xd0
009222F1  41 5F                           pop r15
009222F3  41 5E                           pop r14
009222F5  41 5D                           pop r13
009222F7  41 5C                           pop r12
009222F9  5F                              pop rdi
009222FA  5E                              pop rsi
009222FB  5B                              pop rbx
009222FC  C3                              ret
009222FD  CC                              int3
009222FE  48 39 7B 60                     cmp qword ptr [rbx + 0x60], rdi
00922302  75 D2                           jne 0x1409222d6
00922304  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00922309  F7 00 00 20 00 00               test dword ptr [rax], 0x2000
0092230F  74 C5                           je 0x1409222d6
00922311  33 C0                           xor eax, eax
00922313  F0 49 0F B1 9F B8 01 00 00      lock cmpxchg qword ptr [r15 + 0x1b8], rbx
0092231C  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
00922321  75 B3                           jne 0x1409222d6
00922323  66 FF 43 E2                     inc word ptr [rbx - 0x1e]
00922327  48 8B CB                        mov rcx, rbx
0092232A  E8 71 98 F6 FF                  call 0x14088bba0
0092232F  83 3D 9A DD 5E 00 00            cmp dword ptr [rip + 0x5edd9a], 0
00922336  74 9E                           je 0x1409222d6
00922338  48 8B CB                        mov rcx, rbx
0092233B  E8 78 A8 1A 00                  call 0x140accbb8
00922340  EB 94                           jmp 0x1409222d6
00922342  48 8B 8C 24 48 01 00 00         mov rcx, qword ptr [rsp + 0x148]
0092234A  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00922354  48 85 C9                        test rcx, rcx
00922357  75 5E                           jne 0x1409223b7
00922359  41 8B D5                        mov edx, r13d
0092235C  4C 8B B4 24 30 01 00 00         mov r14, qword ptr [rsp + 0x130]
00922364  49 8B CE                        mov rcx, r14
00922367  E8 F4 62 F7 FF                  call 0x140898660
0092236C  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
00922374  48 85 C9                        test rcx, rcx
00922377  74 1D                           je 0x140922396
00922379  48 8B C3                        mov rax, rbx
0092237C  48 3B CB                        cmp rcx, rbx
0092237F  48 0F 42 C1                     cmovb rax, rcx
00922383  90                              nop
00922384  48 8B 00                        mov rax, qword ptr [rax]
00922387  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0092238C  48 0F 42 D9                     cmovb rbx, rcx
00922390  48 8B 03                        mov rax, qword ptr [rbx]
00922393  48 89 03                        mov qword ptr [rbx], rax
00922396  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
0092239E  48 85 C9                        test rcx, rcx
009223A1  74 36                           je 0x1409223d9
009223A3  41 B0 01                        mov r8b, 1
009223A6  48 8B D1                        mov rdx, rcx
009223A9  41 8B CD                        mov ecx, r13d
009223AC  E8 EF 71 F7 FF                  call 0x1408995a0
009223B1  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009223B5  EB 22                           jmp 0x1409223d9
009223B7  48 8B C3                        mov rax, rbx
009223BA  48 3B CB                        cmp rcx, rbx
009223BD  48 0F 42 C1                     cmovb rax, rcx
009223C1  90                              nop
009223C2  48 8B 00                        mov rax, qword ptr [rax]
009223C5  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009223CA  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009223CF  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
009223D7  EB 80                           jmp 0x140922359
009223D9  E9 7A FC FF FF                  jmp 0x140922058
009223DE  E9 07 FF FF FF                  jmp 0x1409222ea
009223E3  48 3B 44 24 50                  cmp rax, qword ptr [rsp + 0x50]
009223E8  0F 86 69 FD FF FF               jbe 0x140922157
009223EE  E9 D8 02 20 00                  jmp 0x140b226cb
009223F3  4D 8B C4                        mov r8, r12
009223F6  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
009223FE  49 8B CF                        mov rcx, r15
00922401  E8 66 13 00 00                  call 0x14092376c
00922406  E9 AF FC FF FF                  jmp 0x1409220ba
0092240B  4D 8B 67 10                     mov r12, qword ptr [r15 + 0x10]
0092240F  49 8D 5C 24 F0                  lea rbx, [r12 - 0x10]
00922414  45 33 C0                        xor r8d, r8d
00922417  33 D2                           xor edx, edx
00922419  48 8B CB                        mov rcx, rbx
0092241C  E8 0F DE 8E FF                  call 0x140210230
00922421  48 8B F0                        mov rsi, rax
00922424  B9 11 00 00 00                  mov ecx, 0x11
00922429  33 C0                           xor eax, eax
0092242B  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
00922430  74 10                           je 0x140922442
00922432  4C 8B CB                        mov r9, rbx
00922435  4C 8B C6                        mov r8, rsi
00922438  33 D2                           xor edx, edx
0092243A  48 8B CB                        mov rcx, rbx
0092243D  E8 0A E0 8E FF                  call 0x14021044c
00922442  48 85 F6                        test rsi, rsi
00922445  74 04                           je 0x14092244b
00922447  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0092244B  49 8B 34 24                     mov rsi, qword ptr [r12]
0092244F  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00922454  48 85 F6                        test rsi, rsi
00922457  74 0C                           je 0x140922465
00922459  48 8B CE                        mov rcx, rsi
0092245C  E8 7F B6 AF FF                  call 0x14041dae0
00922461  84 C0                           test al, al
00922463  75 1E                           jne 0x140922483
00922465  B8 11 00 00 00                  mov eax, 0x11
0092246A  F0 48 0F B1 3B                  lock cmpxchg qword ptr [rbx], rdi
0092246F  0F 84 44 02 20 00               je 0x140b226b9
00922475  48 8B CB                        mov rcx, rbx
00922478  E8 C3 0F 94 FF                  call 0x140263440
0092247D  90                              nop
0092247E  E9 36 02 20 00                  jmp 0x140b226b9
00922483  B8 11 00 00 00                  mov eax, 0x11
00922488  F0 48 0F B1 3B                  lock cmpxchg qword ptr [rbx], rdi
0092248D  0F 84 11 02 20 00               je 0x140b226a4
00922493  48 8B CB                        mov rcx, rbx
00922496  E8 A5 0F 94 FF                  call 0x140263440
0092249B  90                              nop
0092249C  E9 03 02 20 00                  jmp 0x140b226a4
009224A1  B2 01                           mov dl, 1
009224A3  E9 42 FC FF FF                  jmp 0x1409220ea
009224A8  41 F6 C5 02                     test r13b, 2
009224AC  0F 84 29 FC FF FF               je 0x1409220db
009224B2  40 8A D7                        mov dl, dil
009224B5  E9 30 FC FF FF                  jmp 0x1409220ea
009224BA  41 0F BA E5 1E                  bt r13d, 0x1e
009224BF  0F 82 6A FC FF FF               jb 0x14092212f
009224C5  B9 18 00 00 00                  mov ecx, 0x18
009224CA  8B C1                           mov eax, ecx
009224CC  E9 66 FC FF FF                  jmp 0x140922137
009224D1  48 8B CE                        mov rcx, rsi
009224D4  E8 77 6E 9D FF                  call 0x1402f9350
009224D9  E9 09 FE FF FF                  jmp 0x1409222e7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpProcessSynchronousRequest(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, unsigned __int8 a9)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p148;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p90;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (208);
    v_rdi = 0;
    v_stack_mD8 = 0;
    a2 = 0;
    result = memset(v_rsp - 120, a2, v_rdi + 64, a4);
    v_stack_mA8 = 0;
    v_stack_mD8 = 0;
    if (a9 != 0) goto loc_00922342;
    if (a6 != 0) {
        result = *(unsigned __int64 *)(a6);
        v_stack_mB8 = result;
    }
    if (a7 != 0) {
        result = *(unsigned int *)(a7);
        v_stack_mD8 = (unsigned int)(result);
    }
    v_stack_mB0 = a1 + 416;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 416))) & (6));
    if (((unsigned __int8)(result)) == 6) goto loc_0092240B;
    v_stack_mC0 = a1;
    v_stack_m78 = a1;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    if (((*(unsigned int *)(v_stack_mB0)) & (0x1000ULL)) != 0) goto loc_009223F3;
    result = AlpcpSendMessage(v_stack_m78, a3, v_stack_p20, a9);
loc_009220BA:
    if (sign_flag) goto loc_009222DE;
    if (condition_is_below) goto loc_009224A1;
    if (condition_is_below) goto loc_009224A8;
loc_009220DB:
loc_009220EA:
    v_stack_mD0 = 0;
    v_stack_m78 = a1;
    v_stack_mE8 = a8;
    result = AlpcpReceiveSynchronousReply(v_stack_m78, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), v_stack_mD0, (unsigned int)(v_stack_mD8));
    if ((unsigned int)(result) != 0) goto loc_009222DE;
    if (sign_flag) goto loc_009224BA;
loc_0092212F:
loc_00922137:
    result = (unsigned int)((40) + ((unsigned int)(*(unsigned __int16 *)(v_stack_mD0 + 240))));
    v_stack_mC8 = (unsigned int)(result);
    if (a6 != 0) goto loc_009223E3;
loc_00922157:
    v_stack_p48 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) & (0xC0000000ULL));
    if (((unsigned int)(result)) == 0x80000000ULL) goto loc_00922218;
    *(unsigned __int64 *)(a5) = v_xmm0;
    *(unsigned __int64 *)(a5 + 16) = v_xmm1;
    *(unsigned __int64 *)(a5 + 32) = v_xmm0;
    if (((unsigned int)(result)) < 0x80000000ULL) {
        result = *(unsigned __int16 *)(v_stack_mD0 + 244);
        a2 = 0xFFFFC00FULL;
        result = (unsigned __int16)((result) & ((unsigned __int16)(a2)));
        *(unsigned __int16 *)(a5 + 4) = (unsigned __int16)(result);
    }
    v_stack_p48 = (unsigned int)(*(unsigned __int16 *)(v_stack_mD0 + 242));
loc_009221C8:
    result = AlpcpGetDataFromMessage(v_stack_mD0, 40 + a5 * 1, v_stack_mD0, (unsigned int)(v_stack_mD8));
    if (a6 != 0) goto loc_0092220F;
loc_009221E1:
    if (a7 == 0) goto loc_009222B4;
    v_stack_mE8 = a7;
    result = AlpcpExposeAttributes(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_mD0, (unsigned int)(v_stack_mD8));
    goto loc_009222B4;
loc_0092220F:
    *(unsigned __int64 *)(a1) = (unsigned int)(v_stack_mC8);
    goto loc_009221E1;
loc_00922218:
    *(unsigned __int16 *)(a5) = (unsigned __int16)((unsigned int)(v_stack_mC8));
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_mD0 + 240)) + ((unsigned int)(a1)));
    v_stack_p48 = (unsigned int)(result);
    *(unsigned __int16 *)(a5 + 2) = (unsigned __int16)(result);
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_mD0 + 246)) != 0) goto loc_009222A9;
    *(unsigned __int16 *)(a5 + 6) = 0;
loc_00922242:
    a3 = (unsigned __int16)(((unsigned int)((unsigned int)((unsigned int)(0x1000ULL)))) | (*(unsigned __int16 *)(v_stack_mD0 + 244)));
    *(unsigned __int16 *)(a5 + 4) = (unsigned __int16)(a3);
    *(unsigned int *)(a5 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD0 + 248)));
    *(unsigned int *)(a5 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD0 + 256)));
    *(unsigned int *)(a5 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD0 + 264)));
    *(unsigned int *)(a5 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD0 + 272)));
    *(unsigned int *)(a5 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD0 + 272)));
    if (((*(unsigned int *)(a1 + 256)) & ((unsigned int)((unsigned int)(0x1000ULL)))) == 0) goto loc_009221C8;
    a3 = (unsigned __int16)((a3) & ((unsigned __int16)((unsigned int)(0xFFFFC00FULL))));
    *(unsigned __int16 *)(a5 + 4) = (unsigned __int16)(a3);
    goto loc_009221C8;
loc_009222A9:
    result = (unsigned __int16)(((unsigned int)(*(unsigned int *)(v_stack_mD0 + 272))) - (16));
    *(unsigned __int16 *)(a5 + 6) = (unsigned __int16)(result);
    goto loc_00922242;
loc_009222B4:
    goto loc_009222CD;
loc_009222CD:
    if (((*(unsigned int *)(v_stack_mD0 + 40)) & (512)) != 0) goto loc_009222FE;
loc_009222D6:
    result = AlpcpUnlockMessage(v_stack_mD0, (unsigned int)(0xFFFFC00FULL), a3, (unsigned int)(v_stack_mD8));
loc_009222DE:
    if (a1 != a1) goto loc_009224D1;
loc_009222E7:
loc_009222EA:
    v_rsp = (v_rsp) + (208);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_009222FE:
    if ((*(unsigned __int64 *)(v_stack_mD0 + 96)) != 0) goto loc_009222D6;
    if (((*(unsigned int *)(v_stack_p58)) & (0x2000ULL)) == 0) goto loc_009222D6;
    result = 0;
    if (condition_is_not_equal) goto loc_009222D6;
    result = AlpcMessageCleanupProcedure(v_stack_p38, (unsigned int)(0xFFFFC00FULL), a3, (unsigned int)(v_stack_mD8));
    if ((*(unsigned int *)(v_rip + 6217114)) == 0) goto loc_009222D6;
    result = AlpcpEnterFreeEventMessageLog(v_stack_p38, (unsigned int)(0xFFFFC00FULL), a3, (unsigned int)(v_stack_mD8));
    goto loc_009222D6;
loc_00922342:
    if (a8 != 0) goto loc_009223B7;
loc_00922359:
    result = AlpcpProbeForWriteMessageHeader(a5, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)(v_stack_mD8));
    v_rbx = v_stack_p38;
    if (a6 != 0) {
        result = v_stack_p38;
        if (a6 < v_stack_p38) { result = a6; }
        result = *(unsigned __int64 *)(result);
        v_stack_p50 = result;
        v_rbx = v_stack_p38;
        if (a6 < v_stack_p38) { v_rbx = a6; }
        result = *(unsigned __int64 *)(v_rbx);
        *(unsigned __int64 *)(v_rbx) = result;
    }
    if (a7 == 0) goto loc_009223D9;
    result = AlpcpProbeMessageAttributes((unsigned int)((unsigned int)((unsigned int)(a2))), a7, 1, (unsigned int)(v_stack_mD8));
    v_stack_p30 = (unsigned int)(result);
    goto loc_009223D9;
loc_009223B7:
    result = v_rbx;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) < v_rbx) { result = (unsigned int)((unsigned int)((unsigned int)(a2))); }
    v_stack_p60 = *(unsigned __int64 *)(result);
    v_stack_p148 = v_stack_p60;
    goto loc_00922359;
loc_009223D9:
    goto loc_00922058;
loc_009223E3:
    if (v_stack_p60 <= v_stack_p50) goto loc_00922157;
loc_009223F3:
    result = AlpcpSendLegacySynchronousRequest(a1, v_stack_p90, (unsigned int)((unsigned int)(result)), (unsigned int)(v_stack_mD8));
    goto loc_009220BA;
loc_0092240B:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 16) - 16, a2, a3, (unsigned int)(v_stack_mD8));
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(a1 + 16) - 16;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + 16) - 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_p48 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)) == 0) goto loc_00922465;
    result = ObReferenceObjectSafe(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)), a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00922483;
loc_00922465:
    result = ExfReleasePushLockShared(*(unsigned __int64 *)(a1 + 16) - 16, a2, a3, a4);
loc_00922483:
    result = ExfReleasePushLockShared(*(unsigned __int64 *)(a1 + 16) - 16, a2, a3, a4);
loc_009224A1:
    goto loc_009220EA;
loc_009224A8:
    if ((((unsigned __int8)((unsigned int)(a2))) & (2)) == 0) goto loc_009220DB;
    goto loc_009220EA;
loc_009224BA:
    if (condition_is_below) goto loc_0092212F;
    goto loc_00922137;
loc_009224D1:
    result = ObfDereferenceObject(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)), 0, a3, a4);
    goto loc_009222E7;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpProcessSynchronousRequest(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, uint8_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m48;
    uint64_t v_stack_m78;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p148;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p8;
    uint64_t v_stack_p90;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (208);
    local_rdi = 0;
    v_stack_mD8 = 0;
    Arg2 = 0;
    result = memset(local_rsp - 120, Arg2, local_rdi + 64, Arg4);
    v_stack_mA8 = 0;
    v_stack_mD8 = 0;
    if (Arg9 != 0) goto loc_00922342;
    if (Arg6 != 0) {
        result = *(uint64_t *)(Arg6);
        v_stack_mB8 = result;
    }
    if (Arg7 != 0) {
        result = *(uint32_t *)(Arg7);
        v_stack_mD8 = (uint32_t)(result);
    }
    v_stack_mB0 = Arg1 + 416;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1A0))) & (6));
    if (((uint8_t)(result)) == 6) goto loc_0092240B;
    v_stack_mC0 = Arg1;
    v_stack_m78 = Arg1;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    if (((*(uint32_t *)(v_stack_mB0)) & (0x1000ULL)) != 0) goto loc_009223F3;
    result = AlpcpSendMessage(v_stack_m78, Arg3, v_stack_p20, Arg9);
loc_009220BA:
    if (sign_flag) goto loc_009222DE;
    if (condition_is_below) goto loc_009224A1;
    if (condition_is_below) goto loc_009224A8;
loc_009220DB:
loc_009220EA:
    v_stack_mD0 = 0;
    v_stack_m78 = Arg1;
    v_stack_mE8 = Arg8;
    result = AlpcpReceiveSynchronousReply(v_stack_m78, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), v_stack_mD0, (uint32_t)(v_stack_mD8));
    if ((uint32_t)(result) != 0) goto loc_009222DE;
    if (sign_flag) goto loc_009224BA;
loc_0092212F:
loc_00922137:
    result = (uint32_t)((40) + ((uint32_t)(*(uint16_t *)(v_stack_mD0 + 0xF0))));
    v_stack_mC8 = (uint32_t)(result);
    if (Arg6 != 0) goto loc_009223E3;
loc_00922157:
    v_stack_p48 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) & (0xC0000000ULL));
    if (((uint32_t)(result)) == 0x80000000ULL) goto loc_00922218;
    *(uint64_t *)(arg5) = v_xmm0;
    *(uint64_t *)(arg5 + 0x10) = v_xmm1;
    *(uint64_t *)(arg5 + 0x20) = v_xmm0;
    if (((uint32_t)(result)) < 0x80000000ULL) {
        result = *(uint16_t *)(v_stack_mD0 + 0xF4);
        Arg2 = 0xFFFFC00FULL;
        result = (uint16_t)((result) & ((uint16_t)(Arg2)));
        *(uint16_t *)(arg5 + 0x4) = (uint16_t)(result);
    }
    v_stack_p48 = (uint32_t)(*(uint16_t *)(v_stack_mD0 + 0xF2));
loc_009221C8:
    result = AlpcpGetDataFromMessage(v_stack_mD0, 40 + Arg5 * 1, v_stack_mD0, (uint32_t)(v_stack_mD8));
    if (Arg6 != 0) goto loc_0092220F;
loc_009221E1:
    if (Arg7 == 0) goto loc_009222B4;
    v_stack_mE8 = Arg7;
    result = AlpcpExposeAttributes(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_mD0, (uint32_t)(v_stack_mD8));
    goto loc_009222B4;
loc_0092220F:
    *(uint64_t *)(arg1) = (uint32_t)(v_stack_mC8);
    goto loc_009221E1;
loc_00922218:
    *(uint16_t *)(arg5) = (uint16_t)((uint32_t)(v_stack_mC8));
    result = (uint32_t)((*(uint16_t *)(v_stack_mD0 + 0xF0)) + ((uint32_t)(Arg1)));
    v_stack_p48 = (uint32_t)(result);
    *(uint16_t *)(arg5 + 0x2) = (uint16_t)(result);
    if ((uint16_t)(*(uint16_t *)(v_stack_mD0 + 0xF6)) != 0) goto loc_009222A9;
    *(uint16_t *)(arg5 + 0x6) = 0;
loc_00922242:
    Arg3 = (uint16_t)(((uint32_t)((uint32_t)((uint32_t)(0x1000ULL)))) | (*(uint16_t *)(v_stack_mD0 + 0xF4)));
    *(uint16_t *)(arg5 + 0x4) = (uint16_t)(Arg3);
    *(uint32_t *)(arg5 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0xF8)));
    *(uint32_t *)(arg5 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x100)));
    *(uint32_t *)(arg5 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x108)));
    *(uint32_t *)(arg5 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x110)));
    *(uint32_t *)(arg5 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x110)));
    if (((*(uint32_t *)(arg1 + 0x100)) & ((uint32_t)((uint32_t)(0x1000ULL)))) == 0) goto loc_009221C8;
    Arg3 = (uint16_t)((Arg3) & ((uint16_t)((uint32_t)(0xFFFFC00FULL))));
    *(uint16_t *)(arg5 + 0x4) = (uint16_t)(Arg3);
    goto loc_009221C8;
loc_009222A9:
    result = (uint16_t)(((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x110))) - (16));
    *(uint16_t *)(arg5 + 0x6) = (uint16_t)(result);
    goto loc_00922242;
loc_009222B4:
    goto loc_009222CD;
loc_009222CD:
    if (((*(uint32_t *)(v_stack_mD0 + 0x28)) & (512)) != 0) goto loc_009222FE;
loc_009222D6:
    result = AlpcpUnlockMessage(v_stack_mD0, (uint32_t)(0xFFFFC00FULL), Arg3, (uint32_t)(v_stack_mD8));
loc_009222DE:
    if (Arg1 != Arg1) goto loc_009224D1;
loc_009222E7:
loc_009222EA:
    local_rsp = (local_rsp) + (208);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_009222FE:
    if ((*(uint64_t *)(v_stack_mD0 + 0x60)) != 0) goto loc_009222D6;
    if (((*(uint32_t *)(v_stack_p58)) & (0x2000ULL)) == 0) goto loc_009222D6;
    result = 0;
    if (condition_is_not_equal) goto loc_009222D6;
    result = AlpcMessageCleanupProcedure(v_stack_p38, (uint32_t)(0xFFFFC00FULL), Arg3, (uint32_t)(v_stack_mD8));
    if ((*(uint32_t *)(v_rip + 0x5EDD9A)) == 0) goto loc_009222D6;
    result = AlpcpEnterFreeEventMessageLog(v_stack_p38, (uint32_t)(0xFFFFC00FULL), Arg3, (uint32_t)(v_stack_mD8));
    goto loc_009222D6;
loc_00922342:
    if (Arg8 != 0) goto loc_009223B7;
loc_00922359:
    result = AlpcpProbeForWriteMessageHeader(Arg5, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)(v_stack_mD8));
    local_rbx = v_stack_p38;
    if (Arg6 != 0) {
        result = v_stack_p38;
        if (Arg6 < v_stack_p38) { result = Arg6; }
        result = *(uint64_t *)(result);
        v_stack_p50 = result;
        local_rbx = v_stack_p38;
        if (Arg6 < v_stack_p38) { local_rbx = Arg6; }
        result = *(uint64_t *)(local_rbx);
        *(uint64_t *)(local_rbx) = result;
    }
    if (Arg7 == 0) goto loc_009223D9;
    result = AlpcpProbeMessageAttributes((uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg7, 1, (uint32_t)(v_stack_mD8));
    v_stack_p30 = (uint32_t)(result);
    goto loc_009223D9;
loc_009223B7:
    result = local_rbx;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) < local_rbx) { result = (uint32_t)((uint32_t)((uint32_t)(Arg2))); }
    v_stack_p60 = *(uint64_t *)(result);
    v_stack_p148 = v_stack_p60;
    goto loc_00922359;
loc_009223D9:
    goto loc_00922058;
loc_009223E3:
    if (v_stack_p60 <= v_stack_p50) goto loc_00922157;
loc_009223F3:
    result = AlpcpSendLegacySynchronousRequest(Arg1, v_stack_p90, (uint32_t)((uint32_t)(result)), (uint32_t)(v_stack_mD8));
    goto loc_009220BA;
loc_0092240B:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0x10) - 16, Arg2, Arg3, (uint32_t)(v_stack_mD8));
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = *(uint64_t *)(arg1 + 0x10) - 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x10) - 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_p48 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10));
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)) == 0) goto loc_00922465;
    result = ObReferenceObjectSafe(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00922483;
loc_00922465:
    result = ExfReleasePushLockShared(*(uint64_t *)(arg1 + 0x10) - 16, Arg2, Arg3, Arg4);
loc_00922483:
    result = ExfReleasePushLockShared(*(uint64_t *)(arg1 + 0x10) - 16, Arg2, Arg3, Arg4);
loc_009224A1:
    goto loc_009220EA;
loc_009224A8:
    if ((((uint8_t)((uint32_t)(Arg2))) & (2)) == 0) goto loc_009220DB;
    goto loc_009220EA;
loc_009224BA:
    if (condition_is_below) goto loc_0092212F;
    goto loc_00922137;
loc_009224D1:
    result = ObfDereferenceObject(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)), 0, Arg3, Arg4);
    goto loc_009222E7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x100` | `32` | `R` |
| `Arg1` | `+ 0x1A0` | `64` | `R` |
| `Arg1` | `+ 0x1B8` | `64` | `R` |
| `Arg5` | `+ 0x0` | `16` | `W` |
| `Arg5` | `+ 0x0` | `128` | `R` |
| `Arg5` | `+ 0x2` | `16` | `W` |
| `Arg5` | `+ 0x4` | `16` | `W` |
| `Arg5` | `+ 0x6` | `16` | `W` |
| `Arg5` | `+ 0x8` | `32` | `W` |
| `Arg5` | `+ 0xC` | `32` | `W` |
| `Arg5` | `+ 0x10` | `32` | `W` |
| `Arg5` | `+ 0x10` | `128` | `R` |
| `Arg5` | `+ 0x14` | `32` | `W` |
| `Arg5` | `+ 0x20` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00921FCC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
