# NtTraceEvent

- RVA: `0x002FA6C0`–`0x002FB2A4` (길이 `3,044` bytes)
- VA: `0x00000001402FA6C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00072A20`
- 디코드: `631`개 명령, `3,044/3,044` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **41**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x002FA7DC` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002FA819` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x002FA907` → [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) (function, `0x00AF2FEC`)
- `0x002FA9AD` → [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) (function, `0x00AF2FEC`)
- `0x002FA9E8` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x002FAA13` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002FAA58` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002FAB89` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002FABDE` → [EtwpTraceMessageVa](EtwpTraceMessageVa_function_002FB2B0.md) (function, `0x002FB2B0`)
- `0x002FAC29` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002FAC4B` → [PsGetCurrentServerSiloGlobals](PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x002FACC0` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002FAD3B` → [EtwpLogSystemEventUnsafe](EtwpLogSystemEventUnsafe_function_002FBF10.md) (function, `0x002FBF10`)
- `0x002FAD8B` → [EtwTraceEvent](EtwTraceEvent_function_002FD290.md) (function, `0x002FD290`)
- `0x002FADB7` → [KeAreInterruptsEnabled](KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x002FADE9` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x002FADF3` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x002FAE1F` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x002FAE41` → [PsGetCurrentServerSiloGlobals](PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x002FAE7C` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002FAF12` → [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) (function, `0x00AF2FEC`)
- `0x002FAF68` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002FAF72` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002FAFC3` → [PsGetCurrentServerSiloGlobals](PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x002FAFDA` → [EtwpFindGuidEntryByGuid](../../page/8C/EtwpFindGuidEntryByGuid_function_008C1DB0.md) (function, `0x008C1DB0`)
- `0x002FB001` → [EtwpAccessCheck](../../page/8C/EtwpAccessCheck_function_008C6C2C.md) (function, `0x008C6C2C`)
- `0x002FB041` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x002FB05A` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x002FB090` → [EtwpUpdateEnableMask](../../page/8C/EtwpUpdateEnableMask_function_008C0948.md) (function, `0x008C0948`)
- `0x002FB0CC` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x002FB0DA` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x002FB154` → [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) (function, `0x00AF2FEC`)
- `0x002FB172` → [EtwpUnreferenceGuidEntry](../../page/8C/EtwpUnreferenceGuidEntry_function_008C3320.md) (function, `0x008C3320`)
- `0x002FB17F` → [EtwpUnreferenceGuidEntry](../../page/8C/EtwpUnreferenceGuidEntry_function_008C3320.md) (function, `0x008C3320`)
- `0x002FB19B` → [ExfReleasePushLock](../26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x002FB1E3` → [KeGetEffectiveIrql](KeGetEffectiveIrql_function_002F8030.md) (function, `0x002F8030`)
- `0x002FB1F5` → [ExQueueWorkItem](ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x002FB20B` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x002FB227` → [PsGetCurrentServerSiloGlobals](PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x002FB27C` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x002FB299` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002FA6D3` → RVA `0x00E0A740` (`.data`; read)
- `0x002FA7F0` → RVA `0x00FC6D30` (`ALMOSTRO`; read)
- `0x002FA9CC` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x002FABF9` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x002FAC03` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x002FB1A5` → RVA `0x00F0F640` (`.data`; read)
- `0x002FB1EE` → RVA `0x00F0F620` (`.data`; read)
- `0x002FB204` → RVA `0x00F0F5E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x002FA7DC` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002FA819` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`.text` → `PAGE`)
  - `0x002FA907` → [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) (`.text` → `PAGE`)
  - `0x002FA9AD` → [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) (`.text` → `PAGE`)
  - `0x002FAB89` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002FACC0` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002FADE9` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x002FADF3` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x002FAE1F` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
  - `0x002FAE7C` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002FAF12` → [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) (`.text` → `PAGE`)
  - `0x002FAF68` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002FAF72` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002FAFDA` → [EtwpFindGuidEntryByGuid](../../page/8C/EtwpFindGuidEntryByGuid_function_008C1DB0.md) (`.text` → `PAGE`)
  - `0x002FB001` → [EtwpAccessCheck](../../page/8C/EtwpAccessCheck_function_008C6C2C.md) (`.text` → `PAGE`)
  - `0x002FB090` → [EtwpUpdateEnableMask](../../page/8C/EtwpUpdateEnableMask_function_008C0948.md) (`.text` → `PAGE`)
  - `0x002FB154` → [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) (`.text` → `PAGE`)
  - `0x002FB172` → [EtwpUnreferenceGuidEntry](../../page/8C/EtwpUnreferenceGuidEntry_function_008C3320.md) (`.text` → `PAGE`)
  - `0x002FB17F` → [EtwpUnreferenceGuidEntry](../../page/8C/EtwpUnreferenceGuidEntry_function_008C3320.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x002FA9C0` → [sub_006DF40E + 0x23B](../6D/Unknown_function_006DF40E.md) (`tail-transfer`)
  - `0x002FAF23` → [sub_006DF40E + 0xA7](../6D/Unknown_function_006DF40E.md) (`tail-transfer`)
  - `0x002FB23E` → [sub_006DF40E](../6D/Unknown_function_006DF40E.md) (`tail-transfer`)
  - `0x002FB246` → [sub_006DF40E](../6D/Unknown_function_006DF40E.md) (`tail-transfer`)
  - `0x002FB24C` → [sub_006DF40E + 0x8](../6D/Unknown_function_006DF40E.md) (`tail-transfer`)
  - `0x002FB28A` → [sub_006DF40E + 0x135](../6D/Unknown_function_006DF40E.md) (`tail-transfer`)
  - `0x002FB29F` → [sub_006DF40E + 0x135](../6D/Unknown_function_006DF40E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002FA6C0  40 53                           push rbx
002FA6C2  56                              push rsi
002FA6C3  57                              push rdi
002FA6C4  41 54                           push r12
002FA6C6  41 55                           push r13
002FA6C8  41 56                           push r14
002FA6CA  41 57                           push r15
002FA6CC  48 81 EC A0 01 00 00            sub rsp, 0x1a0
002FA6D3  48 8B 05 66 00 B1 00            mov rax, qword ptr [rip + 0xb10066]
002FA6DA  48 33 C4                        xor rax, rsp
002FA6DD  48 89 84 24 90 01 00 00         mov qword ptr [rsp + 0x190], rax
002FA6E5  49 8B D9                        mov rbx, r9
002FA6E8  41 8B F0                        mov esi, r8d
002FA6EB  44 8B FA                        mov r15d, edx
002FA6EE  4C 8B D1                        mov r10, rcx
002FA6F1  8B C2                           mov eax, edx
002FA6F3  25 00 FF 00 00                  and eax, 0xff00
002FA6F8  3D 00 03 00 00                  cmp eax, 0x300
002FA6FD  0F 85 5B 03 00 00               jne 0x1402faa5e
002FA703  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FA70C  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
002FA714  0F B6 80 32 02 00 00            movzx eax, byte ptr [rax + 0x232]
002FA71B  88 84 24 A1 00 00 00            mov byte ptr [rsp + 0xa1], al
002FA722  84 C0                           test al, al
002FA724  74 29                           je 0x1402fa74f
002FA726  F6 C3 03                        test bl, 3
002FA729  0F 85 AD 00 00 00               jne 0x1402fa7dc
002FA72F  49 8D 41 78                     lea rax, [r9 + 0x78]
002FA733  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
002FA73D  48 3B C2                        cmp rax, rdx
002FA740  0F 87 9B 00 00 00               ja 0x1402fa7e1
002FA746  48 3B C3                        cmp rax, rbx
002FA749  0F 82 92 00 00 00               jb 0x1402fa7e1
002FA74F  49 8B 41 58                     mov rax, qword ptr [r9 + 0x58]
002FA753  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
002FA75B  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
002FA763  41 8B 41 54                     mov eax, dword ptr [r9 + 0x54]
002FA767  89 84 24 9C 00 00 00            mov dword ptr [rsp + 0x9c], eax
002FA76E  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
002FA775  45 0F B7 61 52                  movzx r12d, word ptr [r9 + 0x52]
002FA77A  4C 89 A4 24 40 01 00 00         mov qword ptr [rsp + 0x140], r12
002FA782  41 8B 41 70                     mov eax, dword ptr [r9 + 0x70]
002FA786  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
002FA78D  89 84 24 0C 01 00 00            mov dword ptr [rsp + 0x10c], eax
002FA794  49 8B 41 30                     mov rax, qword ptr [r9 + 0x30]
002FA798  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
002FA7A0  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
002FA7A8  41 0F B6 41 2C                  movzx eax, byte ptr [r9 + 0x2c]
002FA7AD  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
002FA7B4  88 84 24 A2 00 00 00            mov byte ptr [rsp + 0xa2], al
002FA7BB  33 FF                           xor edi, edi
002FA7BD  44 8B F7                        mov r14d, edi
002FA7C0  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
002FA7C8  41 38 79 50                     cmp byte ptr [r9 + 0x50], dil
002FA7CC  74 1B                           je 0x1402fa7e9
002FA7CE  4D 8D 71 60                     lea r14, [r9 + 0x60]
002FA7D2  4C 89 B4 24 10 01 00 00         mov qword ptr [rsp + 0x110], r14
002FA7DA  EB 0D                           jmp 0x1402fa7e9
002FA7DC  E8 EF F7 59 00                  call 0x140899fd0
002FA7E1  0F B6 02                        movzx eax, byte ptr [rdx]
002FA7E4  E9 66 FF FF FF                  jmp 0x1402fa74f
002FA7E9  EB 05                           jmp 0x1402fa7f0
002FA7EB  E9 18 02 00 00                  jmp 0x1402faa08
002FA7F0  4C 8B 05 39 C5 CC 00            mov r8, qword ptr [rip + 0xccc539]
002FA7F7  48 89 BC 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdi
002FA7FF  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
002FA804  48 8D 84 24 D0 00 00 00         lea rax, [rsp + 0xd0]
002FA80C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002FA811  41 B1 01                        mov r9b, 1
002FA814  BA 00 08 00 00                  mov edx, 0x800
002FA819  E8 92 E5 56 00                  call 0x140868db0
002FA81E  8B F0                           mov esi, eax
002FA820  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
002FA827  85 C0                           test eax, eax
002FA829  0F 88 D7 01 00 00               js 0x1402faa06
002FA82F  48 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdi
002FA837  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
002FA83F  4C 8B 6E 20                     mov r13, qword ptr [rsi + 0x20]
002FA843  4C 8B 46 28                     mov r8, qword ptr [rsi + 0x28]
002FA847  4C 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r8
002FA84F  41 C1 EF 1F                     shr r15d, 0x1f
002FA853  0F 57 C0                        xorps xmm0, xmm0
002FA856  0F 11 84 24 70 01 00 00         movups xmmword ptr [rsp + 0x170], xmm0
002FA85E  0F 11 84 24 80 01 00 00         movups xmmword ptr [rsp + 0x180], xmm0
002FA866  48 8B 46 70                     mov rax, qword ptr [rsi + 0x70]
002FA86A  48 8D 48 1C                     lea rcx, [rax + 0x1c]
002FA86E  48 85 C0                        test rax, rax
002FA871  48 0F 44 CF                     cmove rcx, rdi
002FA875  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
002FA87D  0F B7 56 64                     movzx edx, word ptr [rsi + 0x64]
002FA881  66 85 D2                        test dx, dx
002FA884  0F 84 99 00 00 00               je 0x1402fa923
002FA88A  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
002FA892  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
002FA897  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
002FA89C  0F B7 46 62                     movzx eax, word ptr [rsi + 0x62]
002FA8A0  66 89 44 24 68                  mov word ptr [rsp + 0x68], ax
002FA8A5  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
002FA8AA  48 8D 84 24 70 01 00 00         lea rax, [rsp + 0x170]
002FA8B2  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002FA8B7  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
002FA8BF  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002FA8C4  8B 84 24 9C 00 00 00            mov eax, dword ptr [rsp + 0x9c]
002FA8CB  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
002FA8CF  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
002FA8D7  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002FA8DC  0F B6 84 24 80 00 00 00         movzx eax, byte ptr [rsp + 0x80]
002FA8E4  88 44 24 38                     mov byte ptr [rsp + 0x38], al
002FA8E8  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
002FA8ED  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
002FA8F2  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
002FA8F9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002FA8FD  4D 8B CC                        mov r9, r12
002FA900  45 0F B7 C7                     movzx r8d, r15w
002FA904  49 8B CD                        mov rcx, r13
002FA907  E8 E0 86 7F 00                  call 0x140af2fec
002FA90C  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
002FA913  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
002FA91B  4C 8B 84 24 F8 00 00 00         mov r8, qword ptr [rsp + 0xf8]
002FA923  0F B7 56 66                     movzx edx, word ptr [rsi + 0x66]
002FA927  66 85 D2                        test dx, dx
002FA92A  0F 84 89 00 00 00               je 0x1402fa9b9
002FA930  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
002FA938  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
002FA93D  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
002FA942  0F B7 46 62                     movzx eax, word ptr [rsi + 0x62]
002FA946  66 89 44 24 68                  mov word ptr [rsp + 0x68], ax
002FA94B  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
002FA950  48 8D 84 24 70 01 00 00         lea rax, [rsp + 0x170]
002FA958  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002FA95D  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
002FA965  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002FA96A  8B 84 24 9C 00 00 00            mov eax, dword ptr [rsp + 0x9c]
002FA971  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
002FA975  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
002FA97D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002FA982  0F B6 84 24 80 00 00 00         movzx eax, byte ptr [rsp + 0x80]
002FA98A  88 44 24 38                     mov byte ptr [rsp + 0x38], al
002FA98E  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
002FA993  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
002FA998  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
002FA99F  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002FA9A3  4D 8B CC                        mov r9, r12
002FA9A6  45 0F B7 C7                     movzx r8d, r15w
002FA9AA  49 8B CD                        mov rcx, r13
002FA9AD  E8 3A 86 7F 00                  call 0x140af2fec
002FA9B2  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
002FA9B9  49 39 BD 90 02 00 00            cmp qword ptr [r13 + 0x290], rdi
002FA9C0  0F 85 83 4C 3E 00               jne 0x1406df649
002FA9C6  48 8D 5E D0                     lea rbx, [rsi - 0x30]
002FA9CA  8B C7                           mov eax, edi
002FA9CC  39 05 3E A6 CC 00               cmp dword ptr [rip + 0xcca63e], eax
002FA9D2  0F 95 C0                        setne al
002FA9D5  85 C0                           test eax, eax
002FA9D7  74 14                           je 0x1402fa9ed
002FA9D9  33 D2                           xor edx, edx
002FA9DB  41 B9 44 66 6C 74               mov r9d, 0x746c6644
002FA9E1  44 8D 42 01                     lea r8d, [rdx + 1]
002FA9E5  48 8B CB                        mov rcx, rbx
002FA9E8  E8 F7 5F F1 FF                  call 0x1402109e4
002FA9ED  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
002FA9F4  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
002FA9F9  48 83 E8 01                     sub rax, 1
002FA9FD  7E 2D                           jle 0x1402faa2c
002FA9FF  8B B4 24 88 00 00 00            mov esi, dword ptr [rsp + 0x88]
002FAA06  8B C6                           mov eax, esi
002FAA08  48 8B 8C 24 90 01 00 00         mov rcx, qword ptr [rsp + 0x190]
002FAA10  48 33 CC                        xor rcx, rsp
002FAA13  E8 28 1C 3B 00                  call 0x1406ac640
002FAA18  48 81 C4 A0 01 00 00            add rsp, 0x1a0
002FAA1F  41 5F                           pop r15
002FAA21  41 5E                           pop r14
002FAA23  41 5D                           pop r13
002FAA25  41 5C                           pop r12
002FAA27  5F                              pop rdi
002FAA28  5E                              pop rsi
002FAA29  5B                              pop rbx
002FAA2A  C3                              ret
002FAA2B  CC                              int3
002FAA2C  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
002FAA30  48 85 C9                        test rcx, rcx
002FAA33  0F 85 AF 01 00 00               jne 0x1402fabe8
002FAA39  48 85 C0                        test rax, rax
002FAA3C  0F 89 5F 03 00 00               jns 0x1402fada1
002FAA42  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002FAA47  44 8D 49 02                     lea r9d, [rcx + 2]
002FAA4B  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
002FAA53  33 D2                           xor edx, edx
002FAA55  8D 4A 18                        lea ecx, [rdx + 0x18]
002FAA58  E8 03 2C 20 00                  call 0x1404fd660
002FAA5D  CC                              int3
002FAA5E  3D 00 02 00 00                  cmp eax, 0x200
002FAA63  0F 85 C6 01 00 00               jne 0x1402fac2f
002FAA69  4C 89 94 24 50 01 00 00         mov qword ptr [rsp + 0x150], r10
002FAA71  33 FF                           xor edi, edi
002FAA73  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
002FAA7B  83 FE 28                        cmp esi, 0x28
002FAA7E  0F 85 C3 02 00 00               jne 0x1402fad47
002FAA84  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FAA8D  80 B8 32 02 00 00 01            cmp byte ptr [rax + 0x232], 1
002FAA94  0F 85 FD 02 00 00               jne 0x1402fad97
002FAA9A  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
002FAAA2  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
002FAAAA  A8 03                           test al, 3
002FAAAC  0F 85 D7 00 00 00               jne 0x1402fab89
002FAAB2  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
002FAABA  48 83 C0 28                     add rax, 0x28
002FAABE  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
002FAAC8  48 3B C2                        cmp rax, rdx
002FAACB  0F 87 B0 00 00 00               ja 0x1402fab81
002FAAD1  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
002FAAD9  48 83 C1 28                     add rcx, 0x28
002FAADD  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
002FAAE5  48 3B C8                        cmp rcx, rax
002FAAE8  0F 82 93 00 00 00               jb 0x1402fab81
002FAAEE  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
002FAAF6  8B 48 18                        mov ecx, dword ptr [rax + 0x18]
002FAAF9  89 8C 24 98 00 00 00            mov dword ptr [rsp + 0x98], ecx
002FAB00  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
002FAB08  45 85 FF                        test r15d, r15d
002FAB0B  78 4C                           js 0x1402fab59
002FAB0D  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
002FAB11  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
002FAB19  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
002FAB21  8B 48 1C                        mov ecx, dword ptr [rax + 0x1c]
002FAB24  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
002FAB2B  81 F9 00 00 01 00               cmp ecx, 0x10000
002FAB31  77 3D                           ja 0x1402fab70
002FAB33  85 C9                           test ecx, ecx
002FAB35  74 57                           je 0x1402fab8e
002FAB37  4C 8B 84 24 B0 00 00 00         mov r8, qword ptr [rsp + 0xb0]
002FAB3F  4D 8D 0C 08                     lea r9, [r8 + rcx]
002FAB43  4C 3B CA                        cmp r9, rdx
002FAB46  77 05                           ja 0x1402fab4d
002FAB48  4D 3B C8                        cmp r9, r8
002FAB4B  73 41                           jae 0x1402fab8e
002FAB4D  0F B6 02                        movzx eax, byte ptr [rdx]
002FAB50  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
002FAB57  EB 35                           jmp 0x1402fab8e
002FAB59  8B 48 20                        mov ecx, dword ptr [rax + 0x20]
002FAB5C  89 8C 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], ecx
002FAB63  81 8C 24 98 00 00 00 80 00 00 00  or dword ptr [rsp + 0x98], 0x80
002FAB6E  EB A9                           jmp 0x1402fab19
002FAB70  BE 0D 00 00 C0                  mov esi, 0xc000000d
002FAB75  89 B4 24 88 00 00 00            mov dword ptr [rsp + 0x88], esi
002FAB7C  E9 85 FE FF FF                  jmp 0x1402faa06
002FAB81  0F B6 02                        movzx eax, byte ptr [rdx]
002FAB84  E9 65 FF FF FF                  jmp 0x1402faaee
002FAB89  E8 42 F4 59 00                  call 0x140899fd0
002FAB8E  83 8C 24 98 00 00 00 40         or dword ptr [rsp + 0x98], 0x40
002FAB96  89 8C 24 54 01 00 00            mov dword ptr [rsp + 0x154], ecx
002FAB9D  EB 05                           jmp 0x1402faba4
002FAB9F  E9 64 FE FF FF                  jmp 0x1402faa08
002FABA4  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
002FABAC  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
002FABB4  49 83 C0 08                     add r8, 8
002FABB8  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
002FABBD  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
002FABC5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002FABCA  45 0F B7 49 04                  movzx r9d, word ptr [r9 + 4]
002FABCF  8B 94 24 98 00 00 00            mov edx, dword ptr [rsp + 0x98]
002FABD6  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
002FABDE  E8 CD 06 00 00                  call 0x1402fb2b0
002FABE3  E9 20 FE FF FF                  jmp 0x1402faa08
002FABE8  48 8B C3                        mov rax, rbx
002FABEB  48 C1 E8 08                     shr rax, 8
002FABEF  0F B6 D0                        movzx edx, al
002FABF2  0F B6 43 18                     movzx eax, byte ptr [rbx + 0x18]
002FABF6  48 33 D0                        xor rdx, rax
002FABF9  0F B6 05 4C C2 CC 00            movzx eax, byte ptr [rip + 0xccc24c]
002FAC00  48 33 D0                        xor rdx, rax
002FAC03  4C 8D 15 F6 53 D0 FF            lea r10, [rip - 0x2fac0a]
002FAC0A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
002FAC0F  41 B9 01 00 00 00               mov r9d, 1
002FAC15  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
002FAC1D  49 8B 94 D2 00 78 FC 00         mov rdx, qword ptr [r10 + rdx*8 + 0xfc7800]
002FAC25  41 8D 49 17                     lea ecx, [r9 + 0x17]
002FAC29  E8 32 2A 20 00                  call 0x1404fd660
002FAC2E  CC                              int3
002FAC2F  3D 00 06 00 00                  cmp eax, 0x600
002FAC34  0F 87 E4 02 00 00               ja 0x1402faf1e
002FAC3A  0F 84 DF 05 00 00               je 0x1402fb21f
002FAC40  3D 00 04 00 00                  cmp eax, 0x400
002FAC45  0F 85 06 01 00 00               jne 0x1402fad51
002FAC4B  E8 A0 35 00 00                  call 0x1402fe1f0
002FAC50  4C 8B 98 40 03 00 00            mov r11, qword ptr [rax + 0x340]
002FAC57  41 0F B7 C2                     movzx eax, r10w
002FAC5B  B9 FF FF 00 00                  mov ecx, 0xffff
002FAC60  33 FF                           xor edi, edi
002FAC62  44 8B CF                        mov r9d, edi
002FAC65  66 3B C1                        cmp ax, cx
002FAC68  44 0F 45 C8                     cmovne r9d, eax
002FAC6C  45 3B 4B 10                     cmp r9d, dword ptr [r11 + 0x10]
002FAC70  0F 83 D1 00 00 00               jae 0x1402fad47
002FAC76  81 FE DF FF 00 00               cmp esi, 0xffdf
002FAC7C  0F 87 93 05 00 00               ja 0x1402fb215
002FAC82  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FAC8B  80 B8 32 02 00 00 01            cmp byte ptr [rax + 0x232], 1
002FAC92  0F 85 FF 00 00 00               jne 0x1402fad97
002FAC98  48 8B C6                        mov rax, rsi
002FAC9B  F6 C3 03                        test bl, 3
002FAC9E  75 20                           jne 0x1402facc0
002FACA0  48 83 C0 20                     add rax, 0x20
002FACA4  48 03 C3                        add rax, rbx
002FACA7  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
002FACB1  48 3B C2                        cmp rax, rdx
002FACB4  77 05                           ja 0x1402facbb
002FACB6  48 3B C3                        cmp rax, rbx
002FACB9  73 0A                           jae 0x1402facc5
002FACBB  0F B6 02                        movzx eax, byte ptr [rdx]
002FACBE  EB 05                           jmp 0x1402facc5
002FACC0  E8 0B F3 59 00                  call 0x140899fd0
002FACC5  48 8D 4B 20                     lea rcx, [rbx + 0x20]
002FACC9  48 89 8C 24 28 01 00 00         mov qword ptr [rsp + 0x128], rcx
002FACD1  0F B7 43 06                     movzx eax, word ptr [rbx + 6]
002FACD5  66 89 84 24 A4 00 00 00         mov word ptr [rsp + 0xa4], ax
002FACDD  EB 05                           jmp 0x1402face4
002FACDF  E9 24 FD FF FF                  jmp 0x1402faa08
002FACE4  48 89 8C 24 50 01 00 00         mov qword ptr [rsp + 0x150], rcx
002FACEC  89 B4 24 58 01 00 00            mov dword ptr [rsp + 0x158], esi
002FACF3  89 BC 24 5C 01 00 00            mov dword ptr [rsp + 0x15c], edi
002FACFA  41 81 E7 FF 31 0F C0            and r15d, 0xc00f31ff
002FAD01  41 81 CF 00 31 00 00            or r15d, 0x3100
002FAD08  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
002FAD11  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
002FAD16  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
002FAD1B  0F B7 84 24 A4 00 00 00         movzx eax, word ptr [rsp + 0xa4]
002FAD23  66 89 44 24 28                  mov word ptr [rsp + 0x28], ax
002FAD28  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
002FAD30  48 8D 94 24 50 01 00 00         lea rdx, [rsp + 0x150]
002FAD38  49 8B CB                        mov rcx, r11
002FAD3B  E8 D0 11 00 00                  call 0x1402fbf10
002FAD40  8B F7                           mov esi, edi
002FAD42  E9 BF FC FF FF                  jmp 0x1402faa06
002FAD47  B8 0D 00 00 C0                  mov eax, 0xc000000d
002FAD4C  E9 B7 FC FF FF                  jmp 0x1402faa08
002FAD51  3D 00 01 00 00                  cmp eax, 0x100
002FAD56  0F 85 CA 00 00 00               jne 0x1402fae26
002FAD5C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FAD65  0F B6 90 32 02 00 00            movzx edx, byte ptr [rax + 0x232]
002FAD6C  41 C1 FF 1F                     sar r15d, 0x1f
002FAD70  41 81 E7 00 00 F6 FF            and r15d, 0xfff60000
002FAD77  45 8D 8F 00 00 14 C0            lea r9d, [r15 - 0x3fec0000]
002FAD7E  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
002FAD82  41 B8 30 00 00 00               mov r8d, 0x30
002FAD88  48 8B D3                        mov rdx, rbx
002FAD8B  E8 00 25 00 00                  call 0x1402fd290
002FAD90  8B F0                           mov esi, eax
002FAD92  E9 6F FC FF FF                  jmp 0x1402faa06
002FAD97  B8 BB 00 00 C0                  mov eax, 0xc00000bb
002FAD9C  E9 67 FC FF FF                  jmp 0x1402faa08
002FADA1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FADAA  66 39 B8 E6 01 00 00            cmp word ptr [rax + 0x1e6], di
002FADB1  0F 85 EE 03 00 00               jne 0x1402fb1a5
002FADB7  E8 A4 D2 FF FF                  call 0x1402f8060
002FADBC  84 C0                           test al, al
002FADBE  0F 84 E1 03 00 00               je 0x1402fb1a5
002FADC4  44 0F 20 C0                     mov rax, cr8
002FADC8  3C 01                           cmp al, 1
002FADCA  0F 83 D5 03 00 00               jae 0x1402fb1a5
002FADD0  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
002FADD4  A8 40                           test al, 0x40
002FADD6  75 25                           jne 0x1402fadfd
002FADD8  39 3D 32 A2 CC 00               cmp dword ptr [rip + 0xcca232], edi
002FADDE  40 0F 95 C7                     setne dil
002FADE2  85 FF                           test edi, edi
002FADE4  74 08                           je 0x1402fadee
002FADE6  48 8B CB                        mov rcx, rbx
002FADE9  E8 8A D1 6D 00                  call 0x1409d7f78
002FADEE  33 D2                           xor edx, edx
002FADF0  48 8B CB                        mov rcx, rbx
002FADF3  E8 68 9C 56 00                  call 0x140864a60
002FADF8  E9 02 FC FF FF                  jmp 0x1402fa9ff
002FADFD  83 E0 7F                        and eax, 0x7f
002FAE00  4C 8D 15 F9 51 D0 FF            lea r10, [rip - 0x2fae07]
002FAE07  42 0F B6 84 10 80 FF F0 00      movzx eax, byte ptr [rax + r10 + 0xf0ff80]
002FAE10  48 8B CB                        mov rcx, rbx
002FAE13  48 2B C8                        sub rcx, rax
002FAE16  48 8B 09                        mov rcx, qword ptr [rcx]
002FAE19  40 38 79 18                     cmp byte ptr [rcx + 0x18], dil
002FAE1D  74 B9                           je 0x1402fadd8
002FAE1F  E8 0C D0 6D 00                  call 0x1409d7e30
002FAE24  EB B2                           jmp 0x1402fadd8
002FAE26  3D 00 05 00 00                  cmp eax, 0x500
002FAE2B  0F 85 20 04 00 00               jne 0x1402fb251
002FAE31  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FAE3A  48 8B 90 08 05 00 00            mov rdx, qword ptr [rax + 0x508]
002FAE41  E8 AA 33 00 00                  call 0x1402fe1f0
002FAE46  4C 8B 90 40 03 00 00            mov r10, qword ptr [rax + 0x340]
002FAE4D  41 39 92 F8 10 00 00            cmp dword ptr [r10 + 0x10f8], edx
002FAE54  0F 85 34 03 00 00               jne 0x1402fb18e
002FAE5A  F6 C3 03                        test bl, 3
002FAE5D  75 1D                           jne 0x1402fae7c
002FAE5F  49 8D 41 78                     lea rax, [r9 + 0x78]
002FAE63  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
002FAE6D  48 3B C2                        cmp rax, rdx
002FAE70  77 05                           ja 0x1402fae77
002FAE72  48 3B C3                        cmp rax, rbx
002FAE75  73 0A                           jae 0x1402fae81
002FAE77  0F B6 02                        movzx eax, byte ptr [rdx]
002FAE7A  EB 05                           jmp 0x1402fae81
002FAE7C  E8 4F F1 59 00                  call 0x140899fd0
002FAE81  49 8B 41 58                     mov rax, qword ptr [r9 + 0x58]
002FAE85  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
002FAE8D  41 8B 51 54                     mov edx, dword ptr [r9 + 0x54]
002FAE91  89 94 24 00 01 00 00            mov dword ptr [rsp + 0x100], edx
002FAE98  45 8B 49 70                     mov r9d, dword ptr [r9 + 0x70]
002FAE9C  44 89 8C 24 04 01 00 00         mov dword ptr [rsp + 0x104], r9d
002FAEA4  4C 8B 5B 30                     mov r11, qword ptr [rbx + 0x30]
002FAEA8  4C 89 9C 24 20 01 00 00         mov qword ptr [rsp + 0x120], r11
002FAEB0  0F B6 73 2C                     movzx esi, byte ptr [rbx + 0x2c]
002FAEB4  40 88 B4 24 A0 00 00 00         mov byte ptr [rsp + 0xa0], sil
002FAEBC  EB 05                           jmp 0x1402faec3
002FAEBE  E9 45 FB FF FF                  jmp 0x1402faa08
002FAEC3  33 FF                           xor edi, edi
002FAEC5  45 33 C0                        xor r8d, r8d
002FAEC8  49 8D 4A 18                     lea rcx, [r10 + 0x18]
002FAECC  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
002FAED1  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
002FAED6  66 89 7C 24 68                  mov word ptr [rsp + 0x68], di
002FAEDB  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
002FAEE0  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
002FAEE5  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002FAEEA  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
002FAEEE  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
002FAEF3  40 88 74 24 38                  mov byte ptr [rsp + 0x38], sil
002FAEF8  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
002FAEFD  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
002FAF02  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
002FAF07  45 33 C9                        xor r9d, r9d
002FAF0A  41 0F B7 92 F0 10 00 00         movzx edx, word ptr [r10 + 0x10f0]
002FAF12  E8 D5 80 7F 00                  call 0x140af2fec
002FAF17  8B F0                           mov esi, eax
002FAF19  E9 E8 FA FF FF                  jmp 0x1402faa06
002FAF1E  3D 00 07 00 00                  cmp eax, 0x700
002FAF23  0F 85 8C 45 3E 00               jne 0x1406df4b5
002FAF29  4D 85 D2                        test r10, r10
002FAF2C  0F 84 15 FE FF FF               je 0x1402fad47
002FAF32  F6 C3 03                        test bl, 3
002FAF35  75 31                           jne 0x1402faf68
002FAF37  49 8D 41 78                     lea rax, [r9 + 0x78]
002FAF3B  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
002FAF45  48 3B C2                        cmp rax, rdx
002FAF48  77 23                           ja 0x1402faf6d
002FAF4A  48 3B C3                        cmp rax, rbx
002FAF4D  72 1E                           jb 0x1402faf6d
002FAF4F  41 F6 C2 03                     test r10b, 3
002FAF53  75 1D                           jne 0x1402faf72
002FAF55  48 8D 41 10                     lea rax, [rcx + 0x10]
002FAF59  48 3B C2                        cmp rax, rdx
002FAF5C  77 05                           ja 0x1402faf63
002FAF5E  49 3B C2                        cmp rax, r10
002FAF61  73 14                           jae 0x1402faf77
002FAF63  0F B6 02                        movzx eax, byte ptr [rdx]
002FAF66  EB 0F                           jmp 0x1402faf77
002FAF68  E8 63 F0 59 00                  call 0x140899fd0
002FAF6D  0F B6 02                        movzx eax, byte ptr [rdx]
002FAF70  EB DD                           jmp 0x1402faf4f
002FAF72  E8 59 F0 59 00                  call 0x140899fd0
002FAF77  49 8B 41 58                     mov rax, qword ptr [r9 + 0x58]
002FAF7B  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
002FAF83  41 8B 41 54                     mov eax, dword ptr [r9 + 0x54]
002FAF87  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
002FAF8E  41 8B 41 70                     mov eax, dword ptr [r9 + 0x70]
002FAF92  89 84 24 AC 00 00 00            mov dword ptr [rsp + 0xac], eax
002FAF99  49 8B 41 30                     mov rax, qword ptr [r9 + 0x30]
002FAF9D  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
002FAFA5  41 0F B6 41 2C                  movzx eax, byte ptr [r9 + 0x2c]
002FAFAA  88 84 24 82 00 00 00            mov byte ptr [rsp + 0x82], al
002FAFB1  0F 10 01                        movups xmm0, xmmword ptr [rcx]
002FAFB4  0F 11 84 24 60 01 00 00         movups xmmword ptr [rsp + 0x160], xmm0
002FAFBC  EB 05                           jmp 0x1402fafc3
002FAFBE  E9 45 FA FF FF                  jmp 0x1402faa08
002FAFC3  E8 28 32 00 00                  call 0x1402fe1f0
002FAFC8  48 8B 88 40 03 00 00            mov rcx, qword ptr [rax + 0x340]
002FAFCF  45 33 C0                        xor r8d, r8d
002FAFD2  48 8D 94 24 60 01 00 00         lea rdx, [rsp + 0x160]
002FAFDA  E8 D1 6D 5C 00                  call 0x1408c1db0
002FAFDF  4C 8B E8                        mov r13, rax
002FAFE2  48 85 C0                        test rax, rax
002FAFE5  0F 84 99 01 00 00               je 0x1402fb184
002FAFEB  83 78 60 00                     cmp dword ptr [rax + 0x60], 0
002FAFEF  0F 84 87 01 00 00               je 0x1402fb17c
002FAFF5  45 33 C0                        xor r8d, r8d
002FAFF8  BA 00 08 00 00                  mov edx, 0x800
002FAFFD  48 8B 48 48                     mov rcx, qword ptr [rax + 0x48]
002FB001  E8 26 BC 5C 00                  call 0x1408c6c2c
002FB006  8B F0                           mov esi, eax
002FB008  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
002FB00F  85 C0                           test eax, eax
002FB011  0F 88 58 01 00 00               js 0x1402fb16f
002FB017  33 FF                           xor edi, edi
002FB019  66 89 BC 24 84 00 00 00         mov word ptr [rsp + 0x84], di
002FB021  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FB02A  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
002FB031  90                              nop
002FB032  4D 8D B5 98 02 00 00            lea r14, [r13 + 0x298]
002FB039  45 33 C0                        xor r8d, r8d
002FB03C  33 D2                           xor edx, edx
002FB03E  49 8B CE                        mov rcx, r14
002FB041  E8 EA 51 F1 FF                  call 0x140210230
002FB046  48 8B F0                        mov rsi, rax
002FB049  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
002FB04F  73 0E                           jae 0x1402fb05f
002FB051  4D 8B C6                        mov r8, r14
002FB054  48 8B D0                        mov rdx, rax
002FB057  49 8B CE                        mov rcx, r14
002FB05A  E8 31 4C F1 FF                  call 0x14020fc90
002FB05F  48 85 F6                        test rsi, rsi
002FB062  74 04                           je 0x1402fb068
002FB064  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
002FB068  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FB071  49 89 85 A0 02 00 00            mov qword ptr [r13 + 0x2a0], rax
002FB078  48 8D 84 24 84 00 00 00         lea rax, [rsp + 0x84]
002FB080  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002FB085  41 B1 01                        mov r9b, 1
002FB088  45 33 C0                        xor r8d, r8d
002FB08B  33 D2                           xor edx, edx
002FB08D  49 8B CD                        mov rcx, r13
002FB090  E8 B3 58 5C 00                  call 0x1408c0948
002FB095  49 89 BD A0 02 00 00            mov qword ptr [r13 + 0x2a0], rdi
002FB09C  41 0F 0D 0E                     prefetchw byte ptr [r14]
002FB0A0  49 8B 06                        mov rax, qword ptr [r14]
002FB0A3  48 8B C8                        mov rcx, rax
002FB0A6  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
002FB0AA  48 8D 50 F0                     lea rdx, [rax - 0x10]
002FB0AE  48 83 F9 10                     cmp rcx, 0x10
002FB0B2  48 0F 46 D7                     cmovbe rdx, rdi
002FB0B6  A8 02                           test al, 2
002FB0B8  0F 85 DA 00 00 00               jne 0x1402fb198
002FB0BE  F0 49 0F B1 16                  lock cmpxchg qword ptr [r14], rdx
002FB0C3  0F 85 CF 00 00 00               jne 0x1402fb198
002FB0C9  49 8B CE                        mov rcx, r14
002FB0CC  E8 2F 65 FE FF                  call 0x1402e1600
002FB0D1  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002FB0DA  E8 11 3F F6 FF                  call 0x14025eff0
002FB0DF  41 C1 EF 1F                     shr r15d, 0x1f
002FB0E3  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
002FB0E8  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
002FB0ED  66 89 7C 24 68                  mov word ptr [rsp + 0x68], di
002FB0F2  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
002FB0F7  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
002FB0FC  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
002FB104  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002FB109  8B 84 24 A8 00 00 00            mov eax, dword ptr [rsp + 0xa8]
002FB110  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
002FB114  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
002FB11C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002FB121  0F B6 84 24 82 00 00 00         movzx eax, byte ptr [rsp + 0x82]
002FB129  88 44 24 38                     mov byte ptr [rsp + 0x38], al
002FB12D  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
002FB132  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
002FB137  8B 84 24 AC 00 00 00            mov eax, dword ptr [rsp + 0xac]
002FB13E  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002FB142  45 33 C9                        xor r9d, r9d
002FB145  45 0F B7 C7                     movzx r8d, r15w
002FB149  0F B7 94 24 84 00 00 00         movzx edx, word ptr [rsp + 0x84]
002FB151  49 8B CD                        mov rcx, r13
002FB154  E8 93 7E 7F 00                  call 0x140af2fec
002FB159  8B F0                           mov esi, eax
002FB15B  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
002FB162  49 39 BD 90 02 00 00            cmp qword ptr [r13 + 0x290], rdi
002FB169  0F 85 EC 00 00 00               jne 0x1402fb25b
002FB16F  49 8B CD                        mov rcx, r13
002FB172  E8 A9 81 5C 00                  call 0x1408c3320
002FB177  E9 8A F8 FF FF                  jmp 0x1402faa06
002FB17C  49 8B CD                        mov rcx, r13
002FB17F  E8 9C 81 5C 00                  call 0x1408c3320
002FB184  B8 02 03 00 C0                  mov eax, 0xc0000302
002FB189  E9 7A F8 FF FF                  jmp 0x1402faa08
002FB18E  B8 22 00 00 C0                  mov eax, 0xc0000022
002FB193  E9 70 F8 FF FF                  jmp 0x1402faa08
002FB198  49 8B CE                        mov rcx, r14
002FB19B  E8 30 87 F6 FF                  call 0x1402638d0
002FB1A0  E9 24 FF FF FF                  jmp 0x1402fb0c9
002FB1A5  0F 0D 0D 94 44 C1 00            prefetchw byte ptr [rip + 0xc14494]
002FB1AC  48 8B 0D 8D 44 C1 00            mov rcx, qword ptr [rip + 0xc1448d]
002FB1B3  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
002FB1B7  48 8B C1                        mov rax, rcx
002FB1BA  F0 48 0F B1 1D 7D 44 C1 00      lock cmpxchg qword ptr [rip + 0xc1447d], rbx
002FB1C3  74 15                           je 0x1402fb1da
002FB1C5  48 8B C8                        mov rcx, rax
002FB1C8  48 89 43 08                     mov qword ptr [rbx + 8], rax
002FB1CC  F0 48 0F B1 1D 6B 44 C1 00      lock cmpxchg qword ptr [rip + 0xc1446b], rbx
002FB1D5  48 3B C1                        cmp rax, rcx
002FB1D8  75 EB                           jne 0x1402fb1c5
002FB1DA  48 85 C9                        test rcx, rcx
002FB1DD  0F 85 1C F8 FF FF               jne 0x1402fa9ff
002FB1E3  E8 48 CE FF FF                  call 0x1402f8030
002FB1E8  3C 02                           cmp al, 2
002FB1EA  77 13                           ja 0x1402fb1ff
002FB1EC  33 D2                           xor edx, edx
002FB1EE  48 8D 0D 2B 44 C1 00            lea rcx, [rip + 0xc1442b]
002FB1F5  E8 26 E3 FF FF                  call 0x1402f9520
002FB1FA  E9 00 F8 FF FF                  jmp 0x1402fa9ff
002FB1FF  45 33 C0                        xor r8d, r8d
002FB202  33 D2                           xor edx, edx
002FB204  48 8D 0D D5 43 C1 00            lea rcx, [rip + 0xc143d5]
002FB20B  E8 40 CA F0 FF                  call 0x140207c50
002FB210  E9 EA F7 FF FF                  jmp 0x1402fa9ff
002FB215  B8 95 00 00 C0                  mov eax, 0xc0000095
002FB21A  E9 E9 F7 FF FF                  jmp 0x1402faa08
002FB21F  C6 84 24 81 00 00 00 00         mov byte ptr [rsp + 0x81], 0
002FB227  E8 C4 2F 00 00                  call 0x1402fe1f0
002FB22C  4C 8B B0 40 03 00 00            mov r14, qword ptr [rax + 0x340]
002FB233  41 0F B7 FA                     movzx edi, r10w
002FB237  B9 FF FF 00 00                  mov ecx, 0xffff
002FB23C  3B F9                           cmp edi, ecx
002FB23E  0F 84 CA 41 3E 00               je 0x1406df40e
002FB244  85 FF                           test edi, edi
002FB246  0F 84 C2 41 3E 00               je 0x1406df40e
002FB24C  E9 C5 41 3E 00                  jmp 0x1406df416
002FB251  BE 0D 00 00 C0                  mov esi, 0xc000000d
002FB256  E9 AB F7 FF FF                  jmp 0x1402faa06
002FB25B  66 89 BC 24 84 00 00 00         mov word ptr [rsp + 0x84], di
002FB263  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FB26C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
002FB273  90                              nop
002FB274  45 33 C0                        xor r8d, r8d
002FB277  33 D2                           xor edx, edx
002FB279  49 8B CE                        mov rcx, r14
002FB27C  E8 AF 4F F1 FF                  call 0x140210230
002FB281  48 8B F0                        mov rsi, rax
002FB284  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
002FB28A  0F 83 B3 42 3E 00               jae 0x1406df543
002FB290  4D 8B C6                        mov r8, r14
002FB293  48 8B D0                        mov rdx, rax
002FB296  49 8B CE                        mov rcx, r14
002FB299  E8 F2 49 F1 FF                  call 0x14020fc90
002FB29E  90                              nop
002FB29F  E9 9F 42 3E 00                  jmp 0x1406df543
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtTraceEvent(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int8 v_stack_m136;
    unsigned __int8 v_stack_m137;
    unsigned int v_stack_m13C;
    unsigned int v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int8 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int16 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int8 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p100;
    unsigned int v_stack_p104;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p120;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p150;
    unsigned int v_stack_p154;
    unsigned int v_stack_p158;
    unsigned int v_stack_p15C;
    unsigned __int64 v_stack_p160;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int16 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int8 v_stack_p81;
    unsigned __int8 v_stack_p82;
    unsigned __int16 v_stack_p84;
    unsigned int v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned int v_stack_p98;
    unsigned __int8 v_stack_pA0;
    unsigned __int16 v_stack_pA4;
    unsigned int v_stack_pA8;
    unsigned int v_stack_pAC;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pD0;
    unsigned int v_stack_pD8;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;

    v_rsp = (v_rsp) - (416);
    result = (*(unsigned __int64 *)(v_rip + 11599974)) ^ (v_rsp);
    v_stack_m48 = result;
    result = (unsigned int)(((unsigned int)(a2)) & (0xFF00ULL));
    if (((unsigned int)(result)) != 768) goto loc_002FAA5E;
    v_stack_mA8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m137 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_002FA74F;
    if ((((unsigned __int8)(a4)) & (3)) != 0) goto loc_002FA7DC;
    if ((a4 + 120) > a2) goto loc_002FA7E1;
    if ((a4 + 120) < a4) goto loc_002FA7E1;
loc_002FA74F:
    v_stack_m120 = *(unsigned __int64 *)(a4 + 88);
    v_stack_mA0 = *(unsigned __int64 *)(a4 + 88);
    v_stack_m13C = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 84)));
    v_stack_mD0 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 84)));
    v_stack_m98 = *(unsigned __int16 *)(a4 + 82);
    v_stack_m148 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 112)));
    v_stack_mCC = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 112)));
    v_stack_m110 = *(unsigned __int64 *)(a4 + 48);
    v_stack_m90 = *(unsigned __int64 *)(a4 + 48);
    v_stack_m158 = (unsigned __int8)(*(unsigned __int8 *)(a4 + 44));
    v_stack_m136 = (unsigned __int8)(*(unsigned __int8 *)(a4 + 44));
    v_rdi = 0;
    v_stack_mC8 = 0;
    if ((*(unsigned __int8 *)(a4 + 80)) == 0) goto loc_002FA7E9;
    v_stack_mC8 = a4 + 96;
    goto loc_002FA7E9;
loc_002FA7DC:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_002FA7E1:
    goto loc_002FA74F;
loc_002FA7E9:
    goto loc_002FA7F0;
loc_002FA7F0:
    v_stack_m108 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1B8 = v_stack_m108;
    result = ObReferenceObjectByHandle(a1, (unsigned int)(0x800ULL), *(unsigned __int64 *)(v_rip + 13419833), 1);
    v_stack_m150 = (unsigned int)(result);
    if (sign_flag) goto loc_002FAA06;
    v_stack_m118 = 0;
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_m108 + 40);
    v_r15 = (unsigned int)(((unsigned int)(a2)) >> (31));
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    a1 = *(unsigned __int64 *)(v_stack_m108 + 112) + 28;
    if (*(unsigned __int64 *)(v_stack_m108 + 112) == 0) { a1 = 0; }
    v_stack_mF8 = a1;
    result = *(unsigned __int64 *)(v_stack_m108 + 112);
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m108 + 100)) != 0) {
        result = v_stack_m118;
        v_stack_m160 = result;
        v_stack_m168 = a1;
        result = *(unsigned __int16 *)(v_stack_m108 + 98);
        v_stack_m170 = (unsigned __int16)(result);
        v_stack_m178 = 0;
        result = v_stack_m68;
        v_stack_m180 = result;
        result = v_stack_m120;
        v_stack_m188 = result;
        result = v_stack_m13C;
        v_stack_m190 = (unsigned int)(result);
        result = v_stack_m110;
        v_stack_m198 = result;
        result = v_stack_m158;
        v_stack_m1A0 = (unsigned __int8)(result);
        v_stack_m1A8 = a4 + 96;
        v_stack_m1B0 = a4;
        result = v_stack_m148;
        v_stack_m1B8 = (unsigned int)(result);
        a4 = *(unsigned __int16 *)(a4 + 82);
        a3 = (unsigned __int16)(v_r15);
        a1 = *(unsigned __int64 *)(v_stack_m108 + 32);
        result = EtwpWriteUserEvent(a1, *(unsigned __int16 *)(v_stack_m108 + 100), a3, a4);
        v_stack_m150 = (unsigned int)(result);
        a1 = v_stack_mF8;
        a3 = v_stack_mE0;
    }
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m108 + 102)) != 0) {
        result = v_stack_m118;
        v_stack_m160 = result;
        v_stack_m168 = a1;
        result = *(unsigned __int16 *)(v_stack_m108 + 98);
        v_stack_m170 = (unsigned __int16)(result);
        v_stack_m178 = a3;
        result = v_stack_m68;
        v_stack_m180 = result;
        result = v_stack_m120;
        v_stack_m188 = result;
        result = v_stack_m13C;
        v_stack_m190 = (unsigned int)(result);
        result = v_stack_m110;
        v_stack_m198 = result;
        result = v_stack_m158;
        v_stack_m1A0 = (unsigned __int8)(result);
        v_stack_m1A8 = a4 + 96;
        v_stack_m1B0 = a4;
        result = v_stack_m148;
        v_stack_m1B8 = (unsigned int)(result);
        a4 = *(unsigned __int16 *)(a4 + 82);
        a3 = (unsigned __int16)(v_r15);
        a1 = *(unsigned __int64 *)(v_stack_m108 + 32);
        result = EtwpWriteUserEvent(a1, *(unsigned __int16 *)(v_stack_m108 + 102), a3, a4);
        v_stack_m150 = (unsigned int)(result);
    }
    result = ((*(unsigned int *)(v_rip + 13411902)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a2 = 0;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        a1 = v_stack_m108 - 48;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_002FAA2C;
loc_002FA9FF:
loc_002FAA06:
loc_002FAA08:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (416);
    return result;
loc_002FAA2C:
    if (*(unsigned __int64 *)(v_stack_m108 - 48 + 8) != 0) goto loc_002FABE8;
    if (!sign_flag) goto loc_002FADA1;
    v_stack_p20 = result;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, v_stack_pD0, *(unsigned __int64 *)(v_stack_m108 - 48 + 8) + 2);
loc_002FAA5E:
    if (((unsigned int)(result)) != 512) goto loc_002FAC2F;
    v_stack_p150 = a1;
    v_rdi = 0;
    v_stack_pB0 = 0;
    if (((unsigned int)((unsigned int)(v_stack_m150))) != 40) goto loc_002FAD47;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 1) goto loc_002FAD97;
    v_stack_p90 = v_stack_m108 - 48;
    if ((((unsigned __int8)(v_stack_p90)) & (3)) != 0) goto loc_002FAB89;
    result = (v_stack_p90) + (40);
    if (result > 0) goto loc_002FAB81;
    a1 = (v_stack_p90) + (40);
    if (a1 < v_stack_p90) goto loc_002FAB81;
loc_002FAAEE:
    v_stack_p98 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p90 + 24)));
    if (sign_flag) goto loc_002FAB59;
    v_stack_pB0 = *(unsigned __int64 *)(v_stack_p90 + 32);
loc_002FAB19:
    v_stack_pD8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p90 + 28)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p90 + 28)))) > 0x10000ULL) goto loc_002FAB70;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p90 + 28))) == 0) goto loc_002FAB8E;
    if ((v_stack_pB0 + (unsigned int)(*(unsigned int *)(v_stack_p90 + 28)) * 1) > 0) goto loc_002FAB4D;
    if ((v_stack_pB0 + (unsigned int)(*(unsigned int *)(v_stack_p90 + 28)) * 1) >= v_stack_pB0) goto loc_002FAB8E;
loc_002FAB4D:
    goto loc_002FAB8E;
loc_002FAB59:
    v_stack_pB0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(a2) + 32)));
    goto loc_002FAB19;
loc_002FAB70:
    v_stack_p88 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_002FAA06;
loc_002FAB81:
    goto loc_002FAAEE;
loc_002FAB89:
    result = ExRaiseDatatypeMisalignment((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(a2) + 32)), a2, v_stack_pB0, v_stack_pB0 + (unsigned int)(*(unsigned int *)(v_stack_p90 + 28)) * 1);
loc_002FAB8E:
    v_stack_p154 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(a2) + 32)));
    goto loc_002FABA4;
loc_002FABA4:
    a3 = (v_stack_p90) + (8);
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_pB0;
    result = EtwpTraceMessageVa(v_stack_p150, (unsigned int)(v_stack_p98), a3, *(unsigned __int16 *)(v_stack_p90 + 4));
    goto loc_002FAA08;
loc_002FABE8:
    result = (v_stack_m108 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_m108 - 48 + 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 13419084));
    v_stack_p20 = v_stack_p150;
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip - 3124234 + a2 * 8 + 16545792), v_stack_pD0, 1);
loc_002FAC2F:
    if (((unsigned int)(result)) > 0x600ULL) goto loc_002FAF1E;
    if (((unsigned int)(result)) == 0x600ULL) goto loc_002FB21F;
    if (((unsigned int)(result)) != 0x400ULL) goto loc_002FAD51;
    result = PsGetCurrentServerSiloGlobals(1 + 23, *(unsigned __int64 *)(v_rip - 3124234 + a2 * 8 + 16545792), v_stack_pD0, 1);
    v_rdi = 0;
    a4 = 0;
    if (((unsigned __int16)((unsigned __int16)(v_rip - 3124234))) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) { a4 = (unsigned int)((unsigned __int16)(v_rip - 3124234)); }
    if (((unsigned int)(a4)) >= (*(unsigned int *)(*(unsigned __int64 *)(result + 832) + 16))) goto loc_002FAD47;
    if (((unsigned int)((unsigned int)(0xC000000DULL))) > 0xFFDFULL) goto loc_002FB215;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 1) goto loc_002FAD97;
    if ((((unsigned __int8)(v_stack_m108 - 48)) & (3)) != 0) goto loc_002FACC0;
    result = ((unsigned int)(0xC000000DULL)) + (32);
    result = (result) + (v_stack_m108 - 48);
    if (result > (*(unsigned __int64 *)(v_rip - 3124234 + a2 * 8 + 16545792))) goto loc_002FACBB;
    if (result >= (v_stack_m108 - 48)) goto loc_002FACC5;
loc_002FACBB:
    goto loc_002FACC5;
loc_002FACC0:
    result = ExRaiseDatatypeMisalignment((unsigned int)(0xFFFFULL), *(unsigned __int64 *)(v_rip - 3124234 + a2 * 8 + 16545792), v_stack_pD0, a4);
loc_002FACC5:
    v_stack_p128 = v_stack_m108 - 48 + 32;
    v_stack_pA4 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m108 - 48 + 6));
    goto loc_002FACE4;
loc_002FACE4:
    v_stack_p150 = v_stack_m108 - 48 + 32;
    v_stack_p158 = (unsigned int)((unsigned int)(0xC000000DULL));
    v_stack_p15C = 0;
    v_r15 = (unsigned int)((v_r15) & (0xC00F31FFULL));
    v_r15 = (unsigned int)((v_r15) | (0x3100ULL));
    v_stack_p38 = 1;
    v_stack_p30 = (unsigned int)(v_r15);
    v_stack_p28 = (unsigned __int16)(v_stack_pA4);
    v_stack_p20 = 1;
    result = EtwpLogSystemEventUnsafe(*(unsigned __int64 *)(result + 832), v_stack_p150, *(unsigned __int64 *)(gs_base + (0 + 392)), a4);
    goto loc_002FAA06;
loc_002FAD47:
    goto loc_002FAA08;
loc_002FAD51:
    if (((unsigned int)((unsigned int)(0xC000000DULL))) != 256) goto loc_002FAE26;
    v_r15 = (unsigned int)((v_r15) >> (31));
    v_r15 = (unsigned int)((v_r15) & (0xFFF60000ULL));
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = EtwTraceEvent(*(unsigned __int64 *)(result + 832), v_stack_m108 - 48, 48, v_r15 - 1072431104);
    goto loc_002FAA06;
loc_002FAD97:
    goto loc_002FAA08;
loc_002FADA1:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_002FB1A5;
    result = KeAreInterruptsEnabled(*(unsigned __int64 *)(result + 832), v_stack_m108 - 48, 48, v_r15 - 1072431104);
    if ((unsigned __int8)(result) == 0) goto loc_002FB1A5;
    if (((unsigned __int8)(v_cr8)) >= 1) goto loc_002FB1A5;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m108 - 48 + 26))) & (64)) != 0) goto loc_002FADFD;
loc_002FADD8:
    v_rdi = ((*(unsigned int *)(v_rip + 13410866)) != 0) ? 1 : 0;
    result = *(unsigned __int8 *)(v_stack_m108 - 48 + 26);
    if ((unsigned int)(v_rdi) != 0) {
        a1 = v_stack_m108 - 48;
        result = ObpDeregisterObject(a1, v_stack_m108 - 48, 48, v_r15 - 1072431104);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_m108 - 48, a2, 48, v_r15 - 1072431104);
    goto loc_002FA9FF;
loc_002FADFD:
    result = (unsigned int)((result) & (127));
    a1 = (v_stack_m108 - 48) - (*(unsigned __int8 *)(result + v_rip - 3124743 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == ((unsigned __int8)(v_rdi))) goto loc_002FADD8;
    result = ObpHandleRevocationBlockRemoveObject(*(unsigned __int64 *)(a1), a2, 48, v_r15 - 1072431104);
    goto loc_002FADD8;
loc_002FAE26:
    if (((unsigned int)(result)) != 0x500ULL) goto loc_002FB251;
    result = PsGetCurrentServerSiloGlobals(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1288), 48, v_r15 - 1072431104);
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + 832) + 4344)) != ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1288)))) goto loc_002FB18E;
    if ((((unsigned __int8)(v_stack_m108 - 48)) & (3)) != 0) goto loc_002FAE7C;
    if ((v_r15 - 1072431104 + 120) > (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1288))) goto loc_002FAE77;
    if ((v_r15 - 1072431104 + 120) >= (v_stack_m108 - 48)) goto loc_002FAE81;
loc_002FAE77:
    goto loc_002FAE81;
loc_002FAE7C:
    result = ExRaiseDatatypeMisalignment(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1288), 48, v_r15 - 1072431104);
loc_002FAE81:
    v_stack_p118 = *(unsigned __int64 *)(v_r15 - 1072431104 + 88);
    v_stack_p100 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 - 1072431104 + 84)));
    v_stack_p104 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 - 1072431104 + 112)));
    v_stack_p120 = *(unsigned __int64 *)(v_stack_m108 - 48 + 48);
    v_stack_pA0 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m108 - 48 + 44));
    goto loc_002FAEC3;
loc_002FAEC3:
    v_rdi = 0;
    a3 = 0;
    v_stack_p78 = 0;
    v_stack_p70 = 0;
    v_stack_p68 = 0;
    v_stack_p60 = 0;
    v_stack_p58 = 0;
    v_stack_p50 = *(unsigned __int64 *)(v_r15 - 1072431104 + 88);
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 - 1072431104 + 84)));
    v_stack_p40 = *(unsigned __int64 *)(v_stack_m108 - 48 + 48);
    v_stack_p38 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m108 - 48 + 44));
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_m108 - 48;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 - 1072431104 + 112)));
    a4 = 0;
    result = EtwpWriteUserEvent(*(unsigned __int64 *)(result + 832) + 24, *(unsigned __int16 *)(*(unsigned __int64 *)(result + 832) + 4336), a3, a4);
    goto loc_002FAA06;
loc_002FAF1E:
    if (*(unsigned __int64 *)(result + 832) == 0) goto loc_002FAD47;
    if ((((unsigned __int8)(v_stack_m108 - 48)) & (3)) != 0) goto loc_002FAF68;
    if ((a4 + 120) > (*(unsigned __int16 *)(*(unsigned __int64 *)(result + 832) + 4336))) goto loc_002FAF6D;
    if ((a4 + 120) < (v_stack_m108 - 48)) goto loc_002FAF6D;
loc_002FAF4F:
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 832))) & (3)) != 0) goto loc_002FAF72;
    if ((*(unsigned __int64 *)(result + 832) + 24 + 16) > (*(unsigned __int16 *)(*(unsigned __int64 *)(result + 832) + 4336))) goto loc_002FAF63;
    if ((*(unsigned __int64 *)(result + 832) + 24 + 16) >= (*(unsigned __int64 *)(result + 832))) goto loc_002FAF77;
loc_002FAF63:
    goto loc_002FAF77;
loc_002FAF68:
    result = ExRaiseDatatypeMisalignment(*(unsigned __int64 *)(result + 832) + 24, *(unsigned __int16 *)(*(unsigned __int64 *)(result + 832) + 4336), a3, a4);
loc_002FAF6D:
    goto loc_002FAF4F;
loc_002FAF72:
    result = ExRaiseDatatypeMisalignment(*(unsigned __int64 *)(result + 832) + 24, *(unsigned __int16 *)(*(unsigned __int64 *)(result + 832) + 4336), a3, a4);
loc_002FAF77:
    v_stack_pE8 = *(unsigned __int64 *)(a4 + 88);
    v_stack_pA8 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 84)));
    v_stack_pAC = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 112)));
    v_stack_pF0 = *(unsigned __int64 *)(a4 + 48);
    v_stack_p82 = (unsigned __int8)(*(unsigned __int8 *)(a4 + 44));
    v_stack_p160 = v_xmm0;
    goto loc_002FAFC3;
loc_002FAFC3:
    result = PsGetCurrentServerSiloGlobals(*(unsigned __int64 *)(result + 832) + 24, *(unsigned __int16 *)(*(unsigned __int64 *)(result + 832) + 4336), a3, a4);
    a3 = 0;
    result = EtwpFindGuidEntryByGuid(*(unsigned __int64 *)(result + 832), v_stack_p160, a3, a4);
    if (result == 0) goto loc_002FB184;
    if ((*(unsigned int *)(result + 96)) == 0) goto loc_002FB17C;
    a3 = 0;
    result = EtwpAccessCheck(*(unsigned __int64 *)(result + 72), (unsigned int)(0x800ULL), a3, a4);
    v_stack_p88 = (unsigned int)(result);
    if (sign_flag) goto loc_002FB16F;
    v_rdi = 0;
    v_stack_p84 = 0;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 664, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = result + 664;
        a2 = result;
        a1 = result + 664;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(result + 672) = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_p20 = v_stack_p84;
    a3 = 0;
    a2 = 0;
    result = EtwpUpdateEnableMask(result, a2, a3, 1);
    *(unsigned __int64 *)(result + 672) = 0;
    a1 = (*(unsigned __int64 *)(result + 664)) & (-16);
    a2 = *(unsigned __int64 *)(result + 664) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 664))) & (2)) != 0) goto loc_002FB198;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 664))) & (2)) != 0) goto loc_002FB198;
loc_002FB0C9:
    result = KeAbPostRelease(result + 664, a2, a3, 1);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, 1);
    v_r15 = (unsigned int)((v_r15) >> (31));
    v_stack_p78 = 0;
    v_stack_p70 = 0;
    v_stack_p68 = 0;
    v_stack_p60 = 0;
    v_stack_p58 = 0;
    v_stack_p50 = v_stack_pE8;
    v_stack_p48 = (unsigned int)((unsigned int)(v_stack_pA8));
    v_stack_p40 = v_stack_pF0;
    v_stack_p38 = (unsigned __int8)(v_stack_p82);
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_m108 - 48;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_pAC));
    a4 = 0;
    result = EtwpWriteUserEvent(result, v_stack_p84, (unsigned __int16)(v_r15), a4);
    v_stack_p88 = (unsigned int)(result);
    if ((*(unsigned __int64 *)(result + 656)) != 0) goto loc_002FB25B;
loc_002FB16F:
    result = EtwpUnreferenceGuidEntry(result, v_stack_p84, (unsigned __int16)(v_r15), a4);
    goto loc_002FAA06;
loc_002FB17C:
    result = EtwpUnreferenceGuidEntry(result, v_stack_p84, (unsigned __int16)(v_r15), a4);
loc_002FB184:
    goto loc_002FAA08;
loc_002FB18E:
    goto loc_002FAA08;
loc_002FB198:
    result = ExfReleasePushLock(result + 664, v_stack_p84, (unsigned __int16)(v_r15), a4);
    goto loc_002FB0C9;
loc_002FB1A5:
    *(unsigned __int64 *)(v_stack_m108 - 48 + 8) = *(unsigned __int64 *)(v_rip + 12665997);
    if ((*(unsigned __int64 *)(result + 656)) == 0) goto loc_002FB1DA;
loc_002FB1C5:
    *(unsigned __int64 *)(v_stack_m108 - 48 + 8) = *(unsigned __int64 *)(v_rip + 12665997);
    if ((*(unsigned __int64 *)(v_rip + 12665997)) != (*(unsigned __int64 *)(v_rip + 12665997))) goto loc_002FB1C5;
loc_002FB1DA:
    if (*(unsigned __int64 *)(v_rip + 12665997) != 0) goto loc_002FA9FF;
    result = KeGetEffectiveIrql(*(unsigned __int64 *)(v_rip + 12665997), v_stack_p84, (unsigned __int16)(v_r15), a4);
    if (((unsigned __int8)(result)) > 2) goto loc_002FB1FF;
    a2 = 0;
    result = ExQueueWorkItem(v_rip + 12665899, a2, (unsigned __int16)(v_r15), a4);
    goto loc_002FA9FF;
loc_002FB1FF:
    a3 = 0;
    a2 = 0;
    result = KeInsertQueueDpc(v_rip + 12665813, a2, a3, a4);
    goto loc_002FA9FF;
loc_002FB215:
    goto loc_002FAA08;
loc_002FB21F:
    v_stack_p81 = 0;
    result = PsGetCurrentServerSiloGlobals(v_rip + 12665813, a2, a3, a4);
loc_002FB251:
    goto loc_002FAA06;
loc_002FB25B:
    v_stack_p84 = (unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(result + 832)));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(result + 832), a2, a3, a4);
    result = ExfAcquirePushLockExclusiveEx(*(unsigned __int64 *)(result + 832), result, *(unsigned __int64 *)(result + 832), a4);
}
```

## 5. (Beta) C Style

```c
int64_t NtTraceEvent(int64_t Arg1, int32_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint8_t v_stack_m136;
    uint8_t v_stack_m137;
    uint32_t v_stack_m13C;
    uint32_t v_stack_m148;
    uint32_t v_stack_m150;
    uint8_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint16_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint8_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p100;
    uint32_t v_stack_p104;
    uint64_t v_stack_p118;
    uint64_t v_stack_p120;
    uint64_t v_stack_p128;
    uint64_t v_stack_p150;
    uint32_t v_stack_p154;
    uint32_t v_stack_p158;
    uint32_t v_stack_p15C;
    uint64_t v_stack_p160;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;
    uint32_t v_stack_p30;
    uint8_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint16_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint8_t v_stack_p81;
    uint8_t v_stack_p82;
    uint16_t v_stack_p84;
    uint32_t v_stack_p88;
    uint64_t v_stack_p90;
    uint32_t v_stack_p98;
    uint8_t v_stack_pA0;
    uint16_t v_stack_pA4;
    uint32_t v_stack_pA8;
    uint32_t v_stack_pAC;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pD0;
    uint32_t v_stack_pD8;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;

    local_rsp = (local_rsp) - (416);
    result = (*(uint64_t *)(v_rip + 0xB10066)) ^ (local_rsp);
    v_stack_m48 = result;
    result = (uint32_t)(((uint32_t)(Arg2)) & (0xFF00ULL));
    if (((uint32_t)(result)) != 768) goto loc_002FAA5E;
    v_stack_mA8 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m137 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_002FA74F;
    if ((((uint8_t)(Arg4)) & (3)) != 0) goto loc_002FA7DC;
    if ((Arg4 + 120) > Arg2) goto loc_002FA7E1;
    if ((Arg4 + 120) < Arg4) goto loc_002FA7E1;
loc_002FA74F:
    v_stack_m120 = *(uint64_t *)(arg4 + 0x58);
    v_stack_mA0 = *(uint64_t *)(arg4 + 0x58);
    v_stack_m13C = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x54)));
    v_stack_mD0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x54)));
    v_stack_m98 = *(uint16_t *)(arg4 + 0x52);
    v_stack_m148 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x70)));
    v_stack_mCC = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x70)));
    v_stack_m110 = *(uint64_t *)(arg4 + 0x30);
    v_stack_m90 = *(uint64_t *)(arg4 + 0x30);
    v_stack_m158 = (uint8_t)(*(uint8_t *)(arg4 + 0x2C));
    v_stack_m136 = (uint8_t)(*(uint8_t *)(arg4 + 0x2C));
    local_rdi = 0;
    v_stack_mC8 = 0;
    if ((*(uint8_t *)(arg4 + 0x50)) == 0) goto loc_002FA7E9;
    v_stack_mC8 = Arg4 + 96;
    goto loc_002FA7E9;
loc_002FA7DC:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_002FA7E1:
    goto loc_002FA74F;
loc_002FA7E9:
    goto loc_002FA7F0;
loc_002FA7F0:
    v_stack_m108 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1B8 = v_stack_m108;
    result = ObReferenceObjectByHandle(Arg1, (uint32_t)(0x800ULL), *(uint64_t *)(v_rip + 0xCCC539), 1);
    v_stack_m150 = (uint32_t)(result);
    if (sign_flag) goto loc_002FAA06;
    v_stack_m118 = 0;
    v_stack_mE0 = *(uint64_t *)(v_stack_m108 + 0x28);
    local_r15 = (uint32_t)(((uint32_t)(Arg2)) >> (31));
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    Arg1 = *(uint64_t *)(v_stack_m108 + 0x70) + 28;
    if (*(uint64_t *)(v_stack_m108 + 0x70) == 0) { Arg1 = 0; }
    v_stack_mF8 = Arg1;
    result = *(uint64_t *)(v_stack_m108 + 0x70);
    if ((uint16_t)(*(uint16_t *)(v_stack_m108 + 0x64)) != 0) {
        result = v_stack_m118;
        v_stack_m160 = result;
        v_stack_m168 = Arg1;
        result = *(uint16_t *)(v_stack_m108 + 0x62);
        v_stack_m170 = (uint16_t)(result);
        v_stack_m178 = 0;
        result = v_stack_m68;
        v_stack_m180 = result;
        result = v_stack_m120;
        v_stack_m188 = result;
        result = v_stack_m13C;
        v_stack_m190 = (uint32_t)(result);
        result = v_stack_m110;
        v_stack_m198 = result;
        result = v_stack_m158;
        v_stack_m1A0 = (uint8_t)(result);
        v_stack_m1A8 = Arg4 + 96;
        v_stack_m1B0 = Arg4;
        result = v_stack_m148;
        v_stack_m1B8 = (uint32_t)(result);
        Arg4 = *(uint16_t *)(arg4 + 0x52);
        Arg3 = (uint16_t)(local_r15);
        Arg1 = *(uint64_t *)(v_stack_m108 + 0x20);
        result = EtwpWriteUserEvent(Arg1, *(uint16_t *)(v_stack_m108 + 0x64), Arg3, Arg4);
        v_stack_m150 = (uint32_t)(result);
        Arg1 = v_stack_mF8;
        Arg3 = v_stack_mE0;
    }
    if ((uint16_t)(*(uint16_t *)(v_stack_m108 + 0x66)) != 0) {
        result = v_stack_m118;
        v_stack_m160 = result;
        v_stack_m168 = Arg1;
        result = *(uint16_t *)(v_stack_m108 + 0x62);
        v_stack_m170 = (uint16_t)(result);
        v_stack_m178 = Arg3;
        result = v_stack_m68;
        v_stack_m180 = result;
        result = v_stack_m120;
        v_stack_m188 = result;
        result = v_stack_m13C;
        v_stack_m190 = (uint32_t)(result);
        result = v_stack_m110;
        v_stack_m198 = result;
        result = v_stack_m158;
        v_stack_m1A0 = (uint8_t)(result);
        v_stack_m1A8 = Arg4 + 96;
        v_stack_m1B0 = Arg4;
        result = v_stack_m148;
        v_stack_m1B8 = (uint32_t)(result);
        Arg4 = *(uint16_t *)(arg4 + 0x52);
        Arg3 = (uint16_t)(local_r15);
        Arg1 = *(uint64_t *)(v_stack_m108 + 0x20);
        result = EtwpWriteUserEvent(Arg1, *(uint16_t *)(v_stack_m108 + 0x66), Arg3, Arg4);
        v_stack_m150 = (uint32_t)(result);
    }
    result = ((*(uint32_t *)(v_rip + 0xCCA63E)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg2 = 0;
        Arg4 = 0x746C6644ULL;
        Arg3 = Arg2 + 1;
        Arg1 = v_stack_m108 - 48;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_002FAA2C;
loc_002FA9FF:
loc_002FAA06:
loc_002FAA08:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (416);
    return result;
loc_002FAA2C:
    if (*(uint64_t *)(v_stack_m108 - 0x30 + 0x8) != 0) goto loc_002FABE8;
    if (!sign_flag) goto loc_002FADA1;
    v_stack_p20 = result;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_pD0, *(uint64_t *)(v_stack_m108 - 0x30 + 0x8) + 2);
loc_002FAA5E:
    if (((uint32_t)(result)) != 512) goto loc_002FAC2F;
    v_stack_p150 = Arg1;
    local_rdi = 0;
    v_stack_pB0 = 0;
    if (((uint32_t)((uint32_t)(v_stack_m150))) != 40) goto loc_002FAD47;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 1) goto loc_002FAD97;
    v_stack_p90 = v_stack_m108 - 48;
    if ((((uint8_t)(v_stack_p90)) & (3)) != 0) goto loc_002FAB89;
    result = (v_stack_p90) + (40);
    if (result > 0) goto loc_002FAB81;
    Arg1 = (v_stack_p90) + (40);
    if (Arg1 < v_stack_p90) goto loc_002FAB81;
loc_002FAAEE:
    v_stack_p98 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p90 + 0x18)));
    if (sign_flag) goto loc_002FAB59;
    v_stack_pB0 = *(uint64_t *)(v_stack_p90 + 0x20);
loc_002FAB19:
    v_stack_pD8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p90 + 0x1C)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p90 + 0x1C)))) > 0x10000ULL) goto loc_002FAB70;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p90 + 0x1C))) == 0) goto loc_002FAB8E;
    if ((v_stack_pB0 + (uint32_t)(*(uint32_t *)(v_stack_p90 + 0x1C)) * 1) > 0) goto loc_002FAB4D;
    if ((v_stack_pB0 + (uint32_t)(*(uint32_t *)(v_stack_p90 + 0x1C)) * 1) >= v_stack_pB0) goto loc_002FAB8E;
loc_002FAB4D:
    goto loc_002FAB8E;
loc_002FAB59:
    v_stack_pB0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint8_t *)(Arg2) + 0x20)));
    goto loc_002FAB19;
loc_002FAB70:
    v_stack_p88 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_002FAA06;
loc_002FAB81:
    goto loc_002FAAEE;
loc_002FAB89:
    result = ExRaiseDatatypeMisalignment((uint32_t)(*(uint32_t *)(*(uint8_t *)(Arg2) + 0x20)), Arg2, v_stack_pB0, v_stack_pB0 + (uint32_t)(*(uint32_t *)(v_stack_p90 + 0x1C)) * 1);
loc_002FAB8E:
    v_stack_p154 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint8_t *)(Arg2) + 0x20)));
    goto loc_002FABA4;
loc_002FABA4:
    Arg3 = (v_stack_p90) + (8);
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_pB0;
    result = EtwpTraceMessageVa(v_stack_p150, (uint32_t)(v_stack_p98), Arg3, *(uint16_t *)(v_stack_p90 + 0x4));
    goto loc_002FAA08;
loc_002FABE8:
    result = (v_stack_m108 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_m108 - 0x30 + 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xCCC24C));
    v_stack_p20 = v_stack_p150;
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip - 0x2FAC0A + Arg2 * 8 + 0xFC7800), v_stack_pD0, 1);
loc_002FAC2F:
    if (((uint32_t)(result)) > 0x600ULL) goto loc_002FAF1E;
    if (((uint32_t)(result)) == 0x600ULL) goto loc_002FB21F;
    if (((uint32_t)(result)) != 0x400ULL) goto loc_002FAD51;
    result = PsGetCurrentServerSiloGlobals(1 + 23, *(uint64_t *)(v_rip - 0x2FAC0A + Arg2 * 8 + 0xFC7800), v_stack_pD0, 1);
    local_rdi = 0;
    Arg4 = 0;
    if (((uint16_t)((uint16_t)(v_rip - 3124234))) != ((uint16_t)((uint32_t)(0xFFFFULL)))) { Arg4 = (uint32_t)((uint16_t)(v_rip - 3124234)); }
    if (((uint32_t)(Arg4)) >= (*(uint32_t *)(*(uint64_t *)(result + 0x340) + 0x10))) goto loc_002FAD47;
    if (((uint32_t)((uint32_t)(0xC000000DULL))) > 0xFFDFULL) goto loc_002FB215;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 1) goto loc_002FAD97;
    if ((((uint8_t)(v_stack_m108 - 48)) & (3)) != 0) goto loc_002FACC0;
    result = ((uint32_t)(0xC000000DULL)) + (32);
    result = (result) + (v_stack_m108 - 48);
    if (result > (*(uint64_t *)(v_rip - 0x2FAC0A + Arg2 * 8 + 0xFC7800))) goto loc_002FACBB;
    if (result >= (v_stack_m108 - 48)) goto loc_002FACC5;
loc_002FACBB:
    goto loc_002FACC5;
loc_002FACC0:
    result = ExRaiseDatatypeMisalignment((uint32_t)(0xFFFFULL), *(uint64_t *)(v_rip - 0x2FAC0A + Arg2 * 8 + 0xFC7800), v_stack_pD0, Arg4);
loc_002FACC5:
    v_stack_p128 = v_stack_m108 - 48 + 32;
    v_stack_pA4 = (uint16_t)(*(uint16_t *)(v_stack_m108 - 0x30 + 0x6));
    goto loc_002FACE4;
loc_002FACE4:
    v_stack_p150 = v_stack_m108 - 48 + 32;
    v_stack_p158 = (uint32_t)((uint32_t)(0xC000000DULL));
    v_stack_p15C = 0;
    local_r15 = (uint32_t)((local_r15) & (0xC00F31FFULL));
    local_r15 = (uint32_t)((local_r15) | (0x3100ULL));
    v_stack_p38 = 1;
    v_stack_p30 = (uint32_t)(local_r15);
    v_stack_p28 = (uint16_t)(v_stack_pA4);
    v_stack_p20 = 1;
    result = EtwpLogSystemEventUnsafe(*(uint64_t *)(result + 0x340), v_stack_p150, *(uint64_t *)(gs_base + (0 + 0x188)), Arg4);
    goto loc_002FAA06;
loc_002FAD47:
    goto loc_002FAA08;
loc_002FAD51:
    if (((uint32_t)((uint32_t)(0xC000000DULL))) != 256) goto loc_002FAE26;
    local_r15 = (uint32_t)((local_r15) >> (31));
    local_r15 = (uint32_t)((local_r15) & (0xFFF60000ULL));
    v_stack_p20 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = EtwTraceEvent(*(uint64_t *)(result + 0x340), v_stack_m108 - 48, 48, local_r15 - 1072431104);
    goto loc_002FAA06;
loc_002FAD97:
    goto loc_002FAA08;
loc_002FADA1:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_002FB1A5;
    result = KeAreInterruptsEnabled(*(uint64_t *)(result + 0x340), v_stack_m108 - 48, 48, local_r15 - 1072431104);
    if ((uint8_t)(result) == 0) goto loc_002FB1A5;
    if (((uint8_t)(v_cr8)) >= 1) goto loc_002FB1A5;
    if ((((uint8_t)(*(uint8_t *)(v_stack_m108 - 0x30 + 0x1A))) & (64)) != 0) goto loc_002FADFD;
loc_002FADD8:
    local_rdi = ((*(uint32_t *)(v_rip + 0xCCA232)) != 0) ? 1 : 0;
    result = *(uint8_t *)(v_stack_m108 - 0x30 + 0x1A);
    if ((uint32_t)(local_rdi) != 0) {
        Arg1 = v_stack_m108 - 48;
        result = ObpDeregisterObject(Arg1, v_stack_m108 - 48, 48, local_r15 - 1072431104);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_m108 - 48, Arg2, 48, local_r15 - 1072431104);
    goto loc_002FA9FF;
loc_002FADFD:
    result = (uint32_t)((result) & (127));
    Arg1 = (v_stack_m108 - 48) - (*(uint8_t *)(result + v_rip - 0x2FAE07 * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(Arg1) + 0x18)) == ((uint8_t)(local_rdi))) goto loc_002FADD8;
    result = ObpHandleRevocationBlockRemoveObject(*(uint64_t *)(Arg1), Arg2, 48, local_r15 - 1072431104);
    goto loc_002FADD8;
loc_002FAE26:
    if (((uint32_t)(result)) != 0x500ULL) goto loc_002FB251;
    result = PsGetCurrentServerSiloGlobals(*(uint64_t *)(Arg1), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x508), 48, local_r15 - 1072431104);
    if ((*(uint32_t *)(*(uint64_t *)(result + 0x340) + 0x10F8)) != ((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x508)))) goto loc_002FB18E;
    if ((((uint8_t)(v_stack_m108 - 48)) & (3)) != 0) goto loc_002FAE7C;
    if ((local_r15 - 1072431104 + 120) > (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x508))) goto loc_002FAE77;
    if ((local_r15 - 1072431104 + 120) >= (v_stack_m108 - 48)) goto loc_002FAE81;
loc_002FAE77:
    goto loc_002FAE81;
loc_002FAE7C:
    result = ExRaiseDatatypeMisalignment(*(uint64_t *)(Arg1), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x508), 48, local_r15 - 1072431104);
loc_002FAE81:
    v_stack_p118 = *(uint64_t *)(local_r15 - 0x3FEC0000 + 0x58);
    v_stack_p100 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 - 0x3FEC0000 + 0x54)));
    v_stack_p104 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 - 0x3FEC0000 + 0x70)));
    v_stack_p120 = *(uint64_t *)(v_stack_m108 - 0x30 + 0x30);
    v_stack_pA0 = (uint8_t)(*(uint8_t *)(v_stack_m108 - 0x30 + 0x2C));
    goto loc_002FAEC3;
loc_002FAEC3:
    local_rdi = 0;
    Arg3 = 0;
    v_stack_p78 = 0;
    v_stack_p70 = 0;
    v_stack_p68 = 0;
    v_stack_p60 = 0;
    v_stack_p58 = 0;
    v_stack_p50 = *(uint64_t *)(local_r15 - 0x3FEC0000 + 0x58);
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 - 0x3FEC0000 + 0x54)));
    v_stack_p40 = *(uint64_t *)(v_stack_m108 - 0x30 + 0x30);
    v_stack_p38 = (uint8_t)(*(uint8_t *)(v_stack_m108 - 0x30 + 0x2C));
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_m108 - 48;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 - 0x3FEC0000 + 0x70)));
    Arg4 = 0;
    result = EtwpWriteUserEvent(*(uint64_t *)(result + 0x340) + 24, *(uint16_t *)(*(uint64_t *)(result + 0x340) + 0x10F0), Arg3, Arg4);
    goto loc_002FAA06;
loc_002FAF1E:
    if (*(uint64_t *)(result + 0x340) == 0) goto loc_002FAD47;
    if ((((uint8_t)(v_stack_m108 - 48)) & (3)) != 0) goto loc_002FAF68;
    if ((Arg4 + 120) > (*(uint16_t *)(*(uint64_t *)(result + 0x340) + 0x10F0))) goto loc_002FAF6D;
    if ((Arg4 + 120) < (v_stack_m108 - 48)) goto loc_002FAF6D;
loc_002FAF4F:
    if ((((uint8_t)(*(uint64_t *)(result + 0x340))) & (3)) != 0) goto loc_002FAF72;
    if ((*(uint64_t *)(result + 0x340) + 24 + 16) > (*(uint16_t *)(*(uint64_t *)(result + 0x340) + 0x10F0))) goto loc_002FAF63;
    if ((*(uint64_t *)(result + 0x340) + 24 + 16) >= (*(uint64_t *)(result + 0x340))) goto loc_002FAF77;
loc_002FAF63:
    goto loc_002FAF77;
loc_002FAF68:
    result = ExRaiseDatatypeMisalignment(*(uint64_t *)(result + 0x340) + 24, *(uint16_t *)(*(uint64_t *)(result + 0x340) + 0x10F0), Arg3, Arg4);
loc_002FAF6D:
    goto loc_002FAF4F;
loc_002FAF72:
    result = ExRaiseDatatypeMisalignment(*(uint64_t *)(result + 0x340) + 24, *(uint16_t *)(*(uint64_t *)(result + 0x340) + 0x10F0), Arg3, Arg4);
loc_002FAF77:
    v_stack_pE8 = *(uint64_t *)(arg4 + 0x58);
    v_stack_pA8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x54)));
    v_stack_pAC = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x70)));
    v_stack_pF0 = *(uint64_t *)(arg4 + 0x30);
    v_stack_p82 = (uint8_t)(*(uint8_t *)(arg4 + 0x2C));
    v_stack_p160 = v_xmm0;
    goto loc_002FAFC3;
loc_002FAFC3:
    result = PsGetCurrentServerSiloGlobals(*(uint64_t *)(result + 0x340) + 24, *(uint16_t *)(*(uint64_t *)(result + 0x340) + 0x10F0), Arg3, Arg4);
    Arg3 = 0;
    result = EtwpFindGuidEntryByGuid(*(uint64_t *)(result + 0x340), v_stack_p160, Arg3, Arg4);
    if (result == 0) goto loc_002FB184;
    if ((*(uint32_t *)(result + 0x60)) == 0) goto loc_002FB17C;
    Arg3 = 0;
    result = EtwpAccessCheck(*(uint64_t *)(result + 0x48), (uint32_t)(0x800ULL), Arg3, Arg4);
    v_stack_p88 = (uint32_t)(result);
    if (sign_flag) goto loc_002FB16F;
    local_rdi = 0;
    v_stack_p84 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 664, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 664;
        Arg2 = result;
        Arg1 = result + 664;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(result + 0x2A0) = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_p20 = v_stack_p84;
    Arg3 = 0;
    Arg2 = 0;
    result = EtwpUpdateEnableMask(result, Arg2, Arg3, 1);
    *(uint64_t *)(result + 0x2A0) = 0;
    Arg1 = (*(uint64_t *)(result + 0x298)) & (-16);
    Arg2 = *(uint64_t *)(result + 0x298) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(result + 0x298))) & (2)) != 0) goto loc_002FB198;
    if ((((uint8_t)(*(uint64_t *)(result + 0x298))) & (2)) != 0) goto loc_002FB198;
loc_002FB0C9:
    result = KeAbPostRelease(result + 664, Arg2, Arg3, 1);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, 1);
    local_r15 = (uint32_t)((local_r15) >> (31));
    v_stack_p78 = 0;
    v_stack_p70 = 0;
    v_stack_p68 = 0;
    v_stack_p60 = 0;
    v_stack_p58 = 0;
    v_stack_p50 = v_stack_pE8;
    v_stack_p48 = (uint32_t)((uint32_t)(v_stack_pA8));
    v_stack_p40 = v_stack_pF0;
    v_stack_p38 = (uint8_t)(v_stack_p82);
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_m108 - 48;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_pAC));
    Arg4 = 0;
    result = EtwpWriteUserEvent(result, v_stack_p84, (uint16_t)(local_r15), Arg4);
    v_stack_p88 = (uint32_t)(result);
    if ((*(uint64_t *)(result + 0x290)) != 0) goto loc_002FB25B;
loc_002FB16F:
    result = EtwpUnreferenceGuidEntry(result, v_stack_p84, (uint16_t)(local_r15), Arg4);
    goto loc_002FAA06;
loc_002FB17C:
    result = EtwpUnreferenceGuidEntry(result, v_stack_p84, (uint16_t)(local_r15), Arg4);
loc_002FB184:
    goto loc_002FAA08;
loc_002FB18E:
    goto loc_002FAA08;
loc_002FB198:
    result = ExfReleasePushLock(result + 664, v_stack_p84, (uint16_t)(local_r15), Arg4);
    goto loc_002FB0C9;
loc_002FB1A5:
    *(uint64_t *)(v_stack_m108 - 0x30 + 0x8) = *(uint64_t *)(v_rip + 0xC1448D);
    if ((*(uint64_t *)(result + 0x290)) == 0) goto loc_002FB1DA;
loc_002FB1C5:
    *(uint64_t *)(v_stack_m108 - 0x30 + 0x8) = *(uint64_t *)(v_rip + 0xC1448D);
    if ((*(uint64_t *)(v_rip + 0xC1448D)) != (*(uint64_t *)(v_rip + 0xC1448D))) goto loc_002FB1C5;
loc_002FB1DA:
    if (*(uint64_t *)(v_rip + 0xC1448D) != 0) goto loc_002FA9FF;
    result = KeGetEffectiveIrql(*(uint64_t *)(v_rip + 0xC1448D), v_stack_p84, (uint16_t)(local_r15), Arg4);
    if (((uint8_t)(result)) > 2) goto loc_002FB1FF;
    Arg2 = 0;
    result = ExQueueWorkItem(v_rip + 12665899, Arg2, (uint16_t)(local_r15), Arg4);
    goto loc_002FA9FF;
loc_002FB1FF:
    Arg3 = 0;
    Arg2 = 0;
    result = KeInsertQueueDpc(v_rip + 12665813, Arg2, Arg3, Arg4);
    goto loc_002FA9FF;
loc_002FB215:
    goto loc_002FAA08;
loc_002FB21F:
    v_stack_p81 = 0;
    result = PsGetCurrentServerSiloGlobals(v_rip + 12665813, Arg2, Arg3, Arg4);
loc_002FB251:
    goto loc_002FAA06;
loc_002FB25B:
    v_stack_p84 = (uint16_t)((uint16_t)(*(uint64_t *)(result + 0x340)));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(result + 0x340), Arg2, Arg3, Arg4);
    result = ExfAcquirePushLockExclusiveEx(*(uint64_t *)(result + 0x340), result, *(uint64_t *)(result + 0x340), Arg4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x78` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002FA6C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
