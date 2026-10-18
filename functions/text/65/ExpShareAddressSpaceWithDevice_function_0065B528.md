# ExpShareAddressSpaceWithDevice

- RVA: `0x0065B528`–`0x0065BB2B` (길이 `1,539` bytes)
- VA: `0x000000014065B528`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD684`
- 디코드: `387`개 명령, `1,539/1,539` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **42**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0065B55D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0065B5CB` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0065B606` → [IoQueryInterface](../../page/72/IoQueryInterface_function_00729930.md) (function, `0x00729930`)
- `0x0065B631` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0065B64A` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0065B668` → [ExpAllocateAsid](ExpAllocateAsid_function_0065AF68.md) (function, `0x0065AF68`)
- `0x0065B683` → [ExpAssignPasid](../../page/7D/ExpAssignPasid_function_007D0AB8.md) (function, `0x007D0AB8`)
- `0x0065B6C7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0065B6EC` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0065B6FC` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x0065B729` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0065B73D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0065B75D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0065B76E` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0065B793` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0065B7EC` → [ExpPrepareNewSvmDevice](ExpPrepareNewSvmDevice_function_0065B288.md) (function, `0x0065B288`)
- `0x0065B817` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0065B823` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0065B836` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0065B876` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0065B882` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0065B89C` → [ExpConvertSvmDevice](ExpConvertSvmDevice_function_0065B124.md) (function, `0x0065B124`)
- `0x0065B8DC` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0065B8EC` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x0065B937` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0065B94C` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0065B963` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0065B986` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x0065B9B5` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0065B9D4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0065B9F9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0065BA26` → [ExpSvmDereferenceDevice](ExpSvmDereferenceDevice_function_0065BBCC.md) (function, `0x0065BBCC`)
- `0x0065BA4F` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0065BA5F` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x0065BA89` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0065BA9E` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0065BAB0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0065BABD` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0065BAE5` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0065BAF1` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0065BAF9` → [KiLeaveCriticalRegionUnsafe](../25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x0065BB01` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- [ExShareAddressSpaceWithDevice](../../page/7D/ExShareAddressSpaceWithDevice_function_007D0A40.md) at `0x007D0A47`

### Static image references
- `0x0065B56E` → RVA `0x00EFA8E0` (`.data`; read)
- `0x0065B5ED` → RVA `0x00019F50` (`.rdata`; read)
- `0x0065B6B0` → RVA `0x00E06D28` (`.data`; read)
- `0x0065B6DE` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0065B765` → RVA `0x00EFA8E8` (`.data`; read)
- `0x0065B773` → RVA `0x00EFA8E8` (`.data`; read/write)
- `0x0065B7A2` → RVA `0x00EFA8F0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x0065B606` → [IoQueryInterface](../../page/72/IoQueryInterface_function_00729930.md) (`.text` → `PAGE`)
  - `0x0065B683` → [ExpAssignPasid](../../page/7D/ExpAssignPasid_function_007D0AB8.md) (`.text` → `PAGE`)
  - `0x0065B836` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0065B963` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0065BAB0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065B528  48 8B C4                        mov rax, rsp
0065B52B  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0065B52F  88 50 10                        mov byte ptr [rax + 0x10], dl
0065B532  48 89 48 08                     mov qword ptr [rax + 8], rcx
0065B536  55                              push rbp
0065B537  53                              push rbx
0065B538  56                              push rsi
0065B539  57                              push rdi
0065B53A  41 54                           push r12
0065B53C  41 55                           push r13
0065B53E  41 56                           push r14
0065B540  41 57                           push r15
0065B542  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0065B546  48 81 EC C8 00 00 00            sub rsp, 0xc8
0065B54D  33 D2                           xor edx, edx
0065B54F  49 8B F8                        mov rdi, r8
0065B552  48 8B D9                        mov rbx, rcx
0065B555  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0065B559  44 8D 42 50                     lea r8d, [rdx + 0x50]
0065B55D  E8 DE B6 06 00                  call 0x1406c6c40
0065B562  83 0F FF                        or dword ptr [rdi], 0xffffffff
0065B565  45 33 ED                        xor r13d, r13d
0065B568  33 C0                           xor eax, eax
0065B56A  4C 89 6D 9F                     mov qword ptr [rbp - 0x61], r13
0065B56E  4C 39 2D 6B F3 89 00            cmp qword ptr [rip + 0x89f36b], r13
0065B575  0F 57 C0                        xorps xmm0, xmm0
0065B578  0F 11 45 A7                     movups xmmword ptr [rbp - 0x59], xmm0
0065B57C  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0065B580  41 8B F5                        mov esi, r13d
0065B583  4C 89 6D 97                     mov qword ptr [rbp - 0x69], r13
0065B587  0F 84 84 05 00 00               je 0x14065bb11
0065B58D  48 85 DB                        test rbx, rbx
0065B590  75 0A                           jne 0x14065b59c
0065B592  B8 EF 00 00 C0                  mov eax, 0xc00000ef
0065B597  E9 7A 05 00 00                  jmp 0x14065bb16
0065B59C  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
0065B5A5  4C 89 7D BF                     mov qword ptr [rbp - 0x41], r15
0065B5A9  4D 8B B7 B8 00 00 00            mov r14, qword ptr [r15 + 0xb8]
0065B5B0  41 F7 86 FC 05 00 00 00 10 00 00  test dword ptr [r14 + 0x5fc], 0x1000
0065B5BB  0F 85 50 05 00 00               jne 0x14065bb11
0065B5C1  4D 8D A6 E8 01 00 00            lea r12, [r14 + 0x1e8]
0065B5C8  49 8B CC                        mov rcx, r12
0065B5CB  E8 50 B0 BB FF                  call 0x140216620
0065B5D0  84 C0                           test al, al
0065B5D2  75 0A                           jne 0x14065b5de
0065B5D4  B8 0A 01 00 C0                  mov eax, 0xc000010a
0065B5D9  E9 38 05 00 00                  jmp 0x14065bb16
0065B5DE  48 8D 45 C7                     lea rax, [rbp - 0x39]
0065B5E2  41 B9 50 00 00 00               mov r9d, 0x50
0065B5E8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0065B5ED  4C 8D 05 5C E9 9B FF            lea r8, [rip - 0x6416a4]
0065B5F4  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0065B5F9  41 8B D5                        mov edx, r13d
0065B5FC  48 8B CB                        mov rcx, rbx
0065B5FF  66 C7 44 24 20 01 00            mov word ptr [rsp + 0x20], 1
0065B606  E8 25 E3 0C 00                  call 0x140729930
0065B60B  48 83 CB FF                     or rbx, 0xffffffffffffffff
0065B60F  8B F8                           mov edi, eax
0065B611  85 C0                           test eax, eax
0065B613  0F 88 B4 04 00 00               js 0x14065bacd
0065B619  66 41 01 9F E4 01 00 00         add word ptr [r15 + 0x1e4], bx
0065B621  45 33 C0                        xor r8d, r8d
0065B624  4D 8D BE 10 06 00 00            lea r15, [r14 + 0x610]
0065B62B  33 D2                           xor edx, edx
0065B62D  49 8B CF                        mov rcx, r15
0065B630  90                              nop
0065B631  E8 FA 4B BB FF                  call 0x140210230
0065B636  F0 49 0F BA 2F 00               lock bts qword ptr [r15], 0
0065B63C  4C 8B E8                        mov r13, rax
0065B63F  73 0E                           jae 0x14065b64f
0065B641  4D 8B C7                        mov r8, r15
0065B644  48 8B D0                        mov rdx, rax
0065B647  49 8B CF                        mov rcx, r15
0065B64A  E8 41 46 BB FF                  call 0x14020fc90
0065B64F  4D 85 ED                        test r13, r13
0065B652  74 05                           je 0x14065b659
0065B654  41 C6 45 0A 01                  mov byte ptr [r13 + 0xa], 1
0065B659  45 8B A6 00 06 00 00            mov r12d, dword ptr [r14 + 0x600]
0065B660  45 85 E4                        test r12d, r12d
0065B663  75 2E                           jne 0x14065b693
0065B665  49 8B D6                        mov rdx, r14
0065B668  E8 FB F8 FF FF                  call 0x14065af68
0065B66D  44 8B E0                        mov r12d, eax
0065B670  85 C0                           test eax, eax
0065B672  75 0A                           jne 0x14065b67e
0065B674  BF 73 00 00 C0                  mov edi, 0xc0000073
0065B679  E9 37 04 00 00                  jmp 0x14065bab5
0065B67E  8B D0                           mov edx, eax
0065B680  49 8B CE                        mov rcx, r14
0065B683  E8 30 54 17 00                  call 0x1407d0ab8
0065B688  85 C0                           test eax, eax
0065B68A  75 07                           jne 0x14065b693
0065B68C  45 8B A6 00 06 00 00            mov r12d, dword ptr [r14 + 0x600]
0065B693  49 8B 86 08 06 00 00            mov rax, qword ptr [r14 + 0x608]
0065B69A  41 FF CC                        dec r12d
0065B69D  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
0065B6A1  41 BD 0F 00 00 00               mov r13d, 0xf
0065B6A7  48 85 C0                        test rax, rax
0065B6AA  0F 85 B2 00 00 00               jne 0x14065b762
0065B6B0  48 8B 05 71 B6 7A 00            mov rax, qword ptr [rip + 0x7ab671]
0065B6B7  4C 8D 4D 97                     lea r9, [rbp - 0x69]
0065B6BB  41 B0 01                        mov r8b, 1
0065B6BE  33 D2                           xor edx, edx
0065B6C0  41 8B CC                        mov ecx, r12d
0065B6C3  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
0065B6C7  E8 04 F4 05 00                  call 0x1406baad0
0065B6CC  8B F8                           mov edi, eax
0065B6CE  85 C0                           test eax, eax
0065B6D0  0F 88 DF 03 00 00               js 0x14065bab5
0065B6D6  45 0F 20 C7                     mov r15, cr8
0065B6DA  45 0F 22 C5                     mov cr8, r13
0065B6DE  39 35 3C B6 96 00               cmp dword ptr [rip + 0x96b63c], esi
0065B6E4  74 0B                           je 0x14065b6f1
0065B6E6  41 8A D5                        mov dl, r13b
0065B6E9  41 8A CF                        mov cl, r15b
0065B6EC  E8 0B A0 E9 FF                  call 0x1404f56fc
0065B6F1  49 8D 8E 18 06 00 00            lea rcx, [r14 + 0x618]
0065B6F8  48 8D 55 A7                     lea rdx, [rbp - 0x59]
0065B6FC  E8 3F A0 C1 FF                  call 0x140275740
0065B701  49 8B 86 08 06 00 00            mov rax, qword ptr [r14 + 0x608]
0065B708  48 85 C0                        test rax, rax
0065B70B  74 0A                           je 0x14065b717
0065B70D  4C 8B 6D 97                     mov r13, qword ptr [rbp - 0x69]
0065B711  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
0065B715  EB 0E                           jmp 0x14065b725
0065B717  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
0065B71B  4C 8B EE                        mov r13, rsi
0065B71E  49 89 86 08 06 00 00            mov qword ptr [r14 + 0x608], rax
0065B725  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0065B729  E8 82 BA BB FF                  call 0x1402171b0
0065B72E  39 35 EC B5 96 00               cmp dword ptr [rip + 0x96b5ec], esi
0065B734  74 0C                           je 0x14065b742
0065B736  44 0F 20 C1                     mov rcx, cr8
0065B73A  41 8A D7                        mov dl, r15b
0065B73D  E8 56 9F E9 FF                  call 0x1404f5698
0065B742  41 0F B6 C7                     movzx eax, r15b
0065B746  44 0F 22 C0                     mov cr8, rax
0065B74A  4D 85 ED                        test r13, r13
0065B74D  74 13                           je 0x14065b762
0065B74F  48 8B 05 D2 B5 7A 00            mov rax, qword ptr [rip + 0x7ab5d2]
0065B756  49 8B CD                        mov rcx, r13
0065B759  48 8B 40 40                     mov rax, qword ptr [rax + 0x40]
0065B75D  E8 6E F3 05 00                  call 0x1406baad0
0065B762  45 33 C0                        xor r8d, r8d
0065B765  48 8D 0D 7C F1 89 00            lea rcx, [rip + 0x89f17c]
0065B76C  33 D2                           xor edx, edx
0065B76E  E8 BD 4A BB FF                  call 0x140210230
0065B773  F0 48 0F BA 2D 6B F1 89 00 00   lock bts qword ptr [rip + 0x89f16b], 0
0065B77D  4C 8B F8                        mov r15, rax
0065B780  73 16                           jae 0x14065b798
0065B782  4C 8D 05 5F F1 89 00            lea r8, [rip + 0x89f15f]
0065B789  48 8B D0                        mov rdx, rax
0065B78C  48 8D 0D 55 F1 89 00            lea rcx, [rip + 0x89f155]
0065B793  E8 F8 44 BB FF                  call 0x14020fc90
0065B798  4D 85 FF                        test r15, r15
0065B79B  74 05                           je 0x14065b7a2
0065B79D  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
0065B7A2  48 8B 05 47 F1 89 00            mov rax, qword ptr [rip + 0x89f147]
0065B7A9  48 8D 15 40 F1 89 00            lea rdx, [rip + 0x89f140]
0065B7B0  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
0065B7B4  48 3B C2                        cmp rax, rdx
0065B7B7  74 22                           je 0x14065b7db
0065B7B9  4C 8B E8                        mov r13, rax
0065B7BC  4C 8B F8                        mov r15, rax
0065B7BF  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
0065B7C3  48 39 48 18                     cmp qword ptr [rax + 0x18], rcx
0065B7C7  74 08                           je 0x14065b7d1
0065B7C9  48 8B 00                        mov rax, qword ptr [rax]
0065B7CC  48 3B C2                        cmp rax, rdx
0065B7CF  75 E8                           jne 0x14065b7b9
0065B7D1  49 39 4D 18                     cmp qword ptr [r13 + 0x18], rcx
0065B7D5  74 76                           je 0x14065b84d
0065B7D7  48 21 75 9F                     and qword ptr [rbp - 0x61], rsi
0065B7DB  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
0065B7DF  48 8D 45 9F                     lea rax, [rbp - 0x61]
0065B7E3  4C 8D 45 C7                     lea r8, [rbp - 0x39]
0065B7E7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0065B7EC  E8 97 FA FF FF                  call 0x14065b288
0065B7F1  8B F8                           mov edi, eax
0065B7F3  85 C0                           test eax, eax
0065B7F5  78 66                           js 0x14065b85d
0065B7F7  41 B7 01                        mov r15b, 1
0065B7FA  48 8B C3                        mov rax, rbx
0065B7FD  44 88 7D 6F                     mov byte ptr [rbp + 0x6f], r15b
0065B801  F0 48 0F C1 05 DE F0 89 00      lock xadd qword ptr [rip + 0x89f0de], rax
0065B80A  24 06                           and al, 6
0065B80C  3C 02                           cmp al, 2
0065B80E  75 0C                           jne 0x14065b81c
0065B810  48 8D 0D D1 F0 89 00            lea rcx, [rip + 0x89f0d1]
0065B817  E8 B4 A5 C0 FF                  call 0x140265dd0
0065B81C  48 8D 0D C5 F0 89 00            lea rcx, [rip + 0x89f0c5]
0065B823  E8 D8 5D C8 FF                  call 0x1402e1600
0065B828  BA 18 00 00 00                  mov edx, 0x18
0065B82D  41 B8 45 78 50 64               mov r8d, 0x64507845
0065B833  8D 4A 28                        lea ecx, [rdx + 0x28]
0065B836  E8 B5 68 52 00                  call 0x140b820f0
0065B83B  48 8B F0                        mov rsi, rax
0065B83E  48 85 C0                        test rax, rax
0065B841  75 75                           jne 0x14065b8b8
0065B843  BF 9A 00 00 C0                  mov edi, 0xc000009a
0065B848  E9 C7 01 00 00                  jmp 0x14065ba14
0065B84D  4D 85 ED                        test r13, r13
0065B850  74 89                           je 0x14065b7db
0065B852  41 38 75 11                     cmp byte ptr [r13 + 0x11], sil
0065B856  74 37                           je 0x14065b88f
0065B858  BF BB 00 00 C0                  mov edi, 0xc00000bb
0065B85D  48 8B C3                        mov rax, rbx
0065B860  F0 48 0F C1 05 7F F0 89 00      lock xadd qword ptr [rip + 0x89f07f], rax
0065B869  24 06                           and al, 6
0065B86B  3C 02                           cmp al, 2
0065B86D  75 0C                           jne 0x14065b87b
0065B86F  48 8D 0D 72 F0 89 00            lea rcx, [rip + 0x89f072]
0065B876  E8 55 A5 C0 FF                  call 0x140265dd0
0065B87B  48 8D 0D 66 F0 89 00            lea rcx, [rip + 0x89f066]
0065B882  E8 79 5D C8 FF                  call 0x1402e1600
0065B887  44 8A FE                        mov r15b, sil
0065B88A  E9 85 01 00 00                  jmp 0x14065ba14
0065B88F  41 38 75 10                     cmp byte ptr [r13 + 0x10], sil
0065B893  74 16                           je 0x14065b8ab
0065B895  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0065B899  49 8B D7                        mov rdx, r15
0065B89C  E8 83 F8 FF FF                  call 0x14065b124
0065B8A1  8B F8                           mov edi, eax
0065B8A3  85 C0                           test eax, eax
0065B8A5  78 B6                           js 0x14065b85d
0065B8A7  41 88 75 10                     mov byte ptr [r13 + 0x10], sil
0065B8AB  41 FF 47 20                     inc dword ptr [r15 + 0x20]
0065B8AF  41 FF 47 24                     inc dword ptr [r15 + 0x24]
0065B8B3  E9 3F FF FF FF                  jmp 0x14065b7f7
0065B8B8  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
0065B8BC  45 32 ED                        xor r13b, r13b
0065B8BF  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
0065B8C3  45 0F 20 C7                     mov r15, cr8
0065B8C7  BA 0F 00 00 00                  mov edx, 0xf
0065B8CC  44 0F 22 C2                     mov cr8, rdx
0065B8D0  83 3D 49 B4 96 00 00            cmp dword ptr [rip + 0x96b449], 0
0065B8D7  74 08                           je 0x14065b8e1
0065B8D9  41 8A CF                        mov cl, r15b
0065B8DC  E8 1B 9E E9 FF                  call 0x1404f56fc
0065B8E1  49 8D 8E 18 06 00 00            lea rcx, [r14 + 0x618]
0065B8E8  48 8D 55 A7                     lea rdx, [rbp - 0x59]
0065B8EC  E8 4F 9E C1 FF                  call 0x140275740
0065B8F1  4C 8B 45 67                     mov r8, qword ptr [rbp + 0x67]
0065B8F5  49 8D 8E 20 06 00 00            lea rcx, [r14 + 0x620]
0065B8FC  48 8B 11                        mov rdx, qword ptr [rcx]
0065B8FF  48 3B D1                        cmp rdx, rcx
0065B902  74 14                           je 0x14065b918
0065B904  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
0065B908  4C 39 40 18                     cmp qword ptr [rax + 0x18], r8
0065B90C  74 05                           je 0x14065b913
0065B90E  48 8B 12                        mov rdx, qword ptr [rdx]
0065B911  EB EC                           jmp 0x14065b8ff
0065B913  41 B5 01                        mov r13b, 1
0065B916  EB 1B                           jmp 0x14065b933
0065B918  48 8B 01                        mov rax, qword ptr [rcx]
0065B91B  48 39 48 08                     cmp qword ptr [rax + 8], rcx
0065B91F  0F 85 E5 01 00 00               jne 0x14065bb0a
0065B925  48 89 06                        mov qword ptr [rsi], rax
0065B928  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
0065B92C  48 89 70 08                     mov qword ptr [rax + 8], rsi
0065B930  48 89 31                        mov qword ptr [rcx], rsi
0065B933  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0065B937  E8 74 B8 BB FF                  call 0x1402171b0
0065B93C  83 3D DD B3 96 00 00            cmp dword ptr [rip + 0x96b3dd], 0
0065B943  74 0C                           je 0x14065b951
0065B945  44 0F 20 C1                     mov rcx, cr8
0065B949  41 8A D7                        mov dl, r15b
0065B94C  E8 47 9D E9 FF                  call 0x1404f5698
0065B951  41 0F B6 C7                     movzx eax, r15b
0065B955  44 0F 22 C0                     mov cr8, rax
0065B959  45 84 ED                        test r13b, r13b
0065B95C  74 11                           je 0x14065b96f
0065B95E  33 D2                           xor edx, edx
0065B960  48 8B CE                        mov rcx, rsi
0065B963  E8 08 6F 52 00                  call 0x140b82870
0065B968  33 F6                           xor esi, esi
0065B96A  E9 91 00 00 00                  jmp 0x14065ba00
0065B96F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0065B978  48 8B B8 B8 00 00 00            mov rdi, qword ptr [rax + 0xb8]
0065B97F  48 8D 8F 00 04 00 00            lea rcx, [rdi + 0x400]
0065B986  E8 15 7F CC FF                  call 0x1403238a0
0065B98B  8B 97 B8 04 00 00               mov edx, dword ptr [rdi + 0x4b8]
0065B991  48 8D 8F 00 04 00 00            lea rcx, [rdi + 0x400]
0065B998  89 55 7F                        mov dword ptr [rbp + 0x7f], edx
0065B99B  C1 EA 18                        shr edx, 0x18
0065B99E  80 CA 02                        or dl, 2
0065B9A1  88 95 82 00 00 00               mov byte ptr [rbp + 0x82], dl
0065B9A7  8B 55 7F                        mov edx, dword ptr [rbp + 0x7f]
0065B9AA  C1 EA 18                        shr edx, 0x18
0065B9AD  88 97 BB 04 00 00               mov byte ptr [rdi + 0x4bb], dl
0065B9B3  8A D0                           mov dl, al
0065B9B5  E8 B6 32 C2 FF                  call 0x14027ec70
0065B9BA  48 8B 05 67 B3 7A 00            mov rax, qword ptr [rip + 0x7ab367]
0065B9C1  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
0065B9C5  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0065B9C9  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
0065B9CD  48 8B 92 B0 00 00 00            mov rdx, qword ptr [rdx + 0xb0]
0065B9D4  E8 F7 F0 05 00                  call 0x1406baad0
0065B9D9  8B F8                           mov edi, eax
0065B9DB  85 C0                           test eax, eax
0065B9DD  78 31                           js 0x14065ba10
0065B9DF  48 8B 05 42 B3 7A 00            mov rax, qword ptr [rip + 0x7ab342]
0065B9E6  49 8B 56 28                     mov rdx, qword ptr [r14 + 0x28]
0065B9EA  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0065B9EE  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
0065B9F5  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
0065B9F9  E8 D2 F0 05 00                  call 0x1406baad0
0065B9FE  8B F8                           mov edi, eax
0065BA00  85 FF                           test edi, edi
0065BA02  78 0C                           js 0x14065ba10
0065BA04  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0065BA08  44 89 20                        mov dword ptr [rax], r12d
0065BA0B  E9 A5 00 00 00                  jmp 0x14065bab5
0065BA10  44 8A 7D 6F                     mov r15b, byte ptr [rbp + 0x6f]
0065BA14  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
0065BA18  48 85 C9                        test rcx, rcx
0065BA1B  74 0E                           je 0x14065ba2b
0065BA1D  45 84 FF                        test r15b, r15b
0065BA20  74 09                           je 0x14065ba2b
0065BA22  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
0065BA26  E8 A1 01 00 00                  call 0x14065bbcc
0065BA2B  48 85 F6                        test rsi, rsi
0065BA2E  0F 84 81 00 00 00               je 0x14065bab5
0065BA34  45 0F 20 C7                     mov r15, cr8
0065BA38  B8 0F 00 00 00                  mov eax, 0xf
0065BA3D  44 0F 22 C0                     mov cr8, rax
0065BA41  83 3D D8 B2 96 00 00            cmp dword ptr [rip + 0x96b2d8], 0
0065BA48  74 0A                           je 0x14065ba54
0065BA4A  8A D0                           mov dl, al
0065BA4C  41 8A CF                        mov cl, r15b
0065BA4F  E8 A8 9C E9 FF                  call 0x1404f56fc
0065BA54  49 8D 8E 18 06 00 00            lea rcx, [r14 + 0x618]
0065BA5B  48 8D 55 A7                     lea rdx, [rbp - 0x59]
0065BA5F  E8 DC 9C C1 FF                  call 0x140275740
0065BA64  48 8B 0E                        mov rcx, qword ptr [rsi]
0065BA67  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
0065BA6B  0F 85 99 00 00 00               jne 0x14065bb0a
0065BA71  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0065BA75  48 39 30                        cmp qword ptr [rax], rsi
0065BA78  0F 85 8C 00 00 00               jne 0x14065bb0a
0065BA7E  48 89 08                        mov qword ptr [rax], rcx
0065BA81  48 89 41 08                     mov qword ptr [rcx + 8], rax
0065BA85  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0065BA89  E8 22 B7 BB FF                  call 0x1402171b0
0065BA8E  83 3D 8B B2 96 00 00            cmp dword ptr [rip + 0x96b28b], 0
0065BA95  74 0C                           je 0x14065baa3
0065BA97  44 0F 20 C1                     mov rcx, cr8
0065BA9B  41 8A D7                        mov dl, r15b
0065BA9E  E8 F5 9B E9 FF                  call 0x1404f5698
0065BAA3  41 0F B6 C7                     movzx eax, r15b
0065BAA7  44 0F 22 C0                     mov cr8, rax
0065BAAB  33 D2                           xor edx, edx
0065BAAD  48 8B CE                        mov rcx, rsi
0065BAB0  E8 BB 6D 52 00                  call 0x140b82870
0065BAB5  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0065BAB9  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
0065BABD  E8 0E F0 05 00                  call 0x1406baad0
0065BAC2  4C 8B 7D BF                     mov r15, qword ptr [rbp - 0x41]
0065BAC6  4D 8D A6 E8 01 00 00            lea r12, [r14 + 0x1e8]
0065BACD  F0 49 0F C1 9E 10 06 00 00      lock xadd qword ptr [r14 + 0x610], rbx
0065BAD6  80 E3 06                        and bl, 6
0065BAD9  80 FB 02                        cmp bl, 2
0065BADC  75 0C                           jne 0x14065baea
0065BADE  49 8D 8E 10 06 00 00            lea rcx, [r14 + 0x610]
0065BAE5  E8 E6 A2 C0 FF                  call 0x140265dd0
0065BAEA  49 8D 8E 10 06 00 00            lea rcx, [r14 + 0x610]
0065BAF1  E8 0A 5B C8 FF                  call 0x1402e1600
0065BAF6  49 8B CF                        mov rcx, r15
0065BAF9  E8 12 35 C0 FF                  call 0x14025f010
0065BAFE  49 8B CC                        mov rcx, r12
0065BB01  E8 7A E3 CE FF                  call 0x140349e80
0065BB06  8B C7                           mov eax, edi
0065BB08  EB 0C                           jmp 0x14065bb16
0065BB0A  B9 03 00 00 00                  mov ecx, 3
0065BB0F  CD 29                           int 0x29
0065BB11  B8 BB 00 00 C0                  mov eax, 0xc00000bb
0065BB16  48 81 C4 C8 00 00 00            add rsp, 0xc8
0065BB1D  41 5F                           pop r15
0065BB1F  41 5E                           pop r14
0065BB21  41 5D                           pop r13
0065BB23  41 5C                           pop r12
0065BB25  5F                              pop rdi
0065BB26  5E                              pop rsi
0065BB27  5B                              pop rbx
0065BB28  5D                              pop rbp
0065BB29  C3                              ret
0065BB2A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpShareAddressSpaceWithDevice(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int16 v_stack_mE8;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int8 *)(v_rsp + 16) = (unsigned __int8)(a2);
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (200);
    a2 = 0;
    result = memset(v_rsp - 95 - 57, a2, a2 + 80, a4);
    v_r13 = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 97) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 89) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 73) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 105) = 0;
    if ((*(unsigned __int64 *)(v_rip + 9040747)) == 0) goto loc_0065BB11;
    if (a1 != 0) goto loc_0065B59C;
    goto loc_0065BB16;
loc_0065B59C:
    *(unsigned __int64 *)(v_rsp - 95 - 65) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1532)) & (0x1000ULL)) != 0) goto loc_0065BB11;
    result = ExAcquireRundownProtection(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 488, a2, a2 + 80, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0065B5DE;
    goto loc_0065BB16;
loc_0065B5DE:
    v_stack_mD8 = v_rsp - 95 - 57;
    v_stack_mE0 = a1;
    v_stack_mE8 = 1;
    result = IoQueryInterface(a1, 0, v_rip - 6559396, 80);
    v_rbx = (a1) | (-1);
    if (sign_flag) goto loc_0065BACD;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1552, a2, a3, 80);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1552;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1552;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, 80);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1536))) != 0) goto loc_0065B693;
    result = ExpAllocateAsid(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, 80);
    if ((unsigned int)(result) != 0) goto loc_0065B67E;
    goto loc_0065BAB5;
loc_0065B67E:
    result = ExpAssignPasid(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)((unsigned int)(result)), a3, 80);
    v_r12 = (unsigned int)((unsigned int)(result));
    if ((unsigned int)(result) == 0) {
        v_r12 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1536);
    }
    v_r12 = (unsigned int)((v_r12) - 1);
    *(unsigned __int64 *)(v_rsp - 95 - 105) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1544);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1544) != 0) goto loc_0065B762;
    a2 = 0;
    result = guard_dispatch_icall((unsigned int)((unsigned int)(v_r12)), a2, 1, v_rsp - 95 - 105);
    if (sign_flag) goto loc_0065BAB5;
    if ((*(unsigned int *)(v_rip + 9877052)) != 0) {
        a2 = 15;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, 1, v_rsp - 95 - 105);
    }
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1560, v_rsp - 95 - 89, 1, v_rsp - 95 - 105);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1544) == 0) goto loc_0065B717;
    *(unsigned __int64 *)(v_rsp - 95 - 105) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1544);
    goto loc_0065B725;
loc_0065B717:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1544) = *(unsigned __int64 *)(v_rsp - 95 - 105);
loc_0065B725:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_rsp - 95 - 89, v_rsp - 95 - 89, 1, v_rsp - 95 - 105);
    if ((*(unsigned int *)(v_rip + 9876972)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, v_rsp - 95 - 105);
    }
    result = (unsigned __int8)(v_cr8);
    if (0 != 0) {
        result = *(unsigned __int64 *)(v_rip + 8041938);
        a1 = 0;
        result = *(unsigned __int64 *)(result + 64);
        result = guard_dispatch_icall(a1, a2, 1, v_rsp - 95 - 105);
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 9040252, a2, a3, v_rsp - 95 - 105);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 9040223;
        a2 = result;
        a1 = v_rip + 9040213;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_rsp - 95 - 105);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(v_rip + 9040199)) == (v_rip + 9040192)) goto loc_0065B7DB;
loc_0065B7B9:
    *(unsigned __int64 *)(v_rsp - 95 - 97) = *(unsigned __int64 *)(v_rip + 9040199);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9040199) + 24)) == (*(unsigned __int64 *)(v_rsp - 95 + 103))) goto loc_0065B7D1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9040199))) != (v_rip + 9040192)) goto loc_0065B7B9;
loc_0065B7D1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9040199) + 24)) == (*(unsigned __int64 *)(v_rsp - 95 + 103))) goto loc_0065B84D;
loc_0065B7DB:
    v_stack_mE8 = v_rsp - 95 - 97;
    result = ExpPrepareNewSvmDevice(*(unsigned __int64 *)(v_rsp - 95 + 103), *(unsigned __int64 *)(v_rsp - 95 - 105), v_rsp - 95 - 57, v_rsp - 95 - 105);
    if (sign_flag) goto loc_0065B85D;
loc_0065B7F7:
    *(unsigned __int8 *)(v_rsp - 95 + 111) = 1;
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_rip + 9040081;
        result = ExfTryToWakePushLock(a1, *(unsigned __int64 *)(v_rsp - 95 - 105), v_rsp - 95 - 57, v_rsp - 95 - 105);
    }
    result = KeAbPostRelease(v_rip + 9040069, *(unsigned __int64 *)(v_rsp - 95 - 105), v_rsp - 95 - 57, v_rsp - 95 - 105);
    result = ExAllocatePool2(24 + 40, 24, (unsigned int)(0x64507845ULL), v_rsp - 95 - 105);
    if (result != 0) goto loc_0065B8B8;
    goto loc_0065BA14;
loc_0065B84D:
    if (*(unsigned __int64 *)(v_rip + 9040199) == 0) goto loc_0065B7DB;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9040199) + 17)) == ((unsigned __int8)(result))) goto loc_0065B88F;
loc_0065B85D:
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_rip + 9039986;
        result = ExfTryToWakePushLock(a1, 24, (unsigned int)(0x64507845ULL), v_rsp - 95 - 105);
    }
    result = KeAbPostRelease(v_rip + 9039974, 24, (unsigned int)(0x64507845ULL), v_rsp - 95 - 105);
    goto loc_0065BA14;
loc_0065B88F:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9040199) + 16)) == ((unsigned __int8)(result))) goto loc_0065B8AB;
    result = ExpConvertSvmDevice(*(unsigned __int64 *)(v_rsp - 95 - 105), (unsigned __int8)(result), (unsigned int)(0x64507845ULL), v_rsp - 95 - 105);
    if (sign_flag) goto loc_0065B85D;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9040199) + 16) = (unsigned __int8)(result);
loc_0065B8AB:
    goto loc_0065B7F7;
loc_0065B8B8:
    v_r13 = 0;
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(v_rsp - 95 - 97);
    result = *(unsigned __int64 *)(v_rsp - 95 - 97);
    if ((*(unsigned int *)(v_rip + 9876553)) != 0) {
        a1 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(a1, 15, (unsigned int)(0x64507845ULL), v_rsp - 95 - 105);
    }
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1560, v_rsp - 95 - 89, (unsigned int)(0x64507845ULL), v_rsp - 95 - 105);
loc_0065B8FF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1568)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1568)) goto loc_0065B918;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1568) + 16) + 24)) == (*(unsigned __int64 *)(v_rsp - 95 + 103))) goto loc_0065B913;
    goto loc_0065B8FF;
loc_0065B913:
    goto loc_0065B933;
loc_0065B918:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1568) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1568)) goto loc_0065BB0A;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1568);
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1568;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1568) + 8) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1568) = result;
loc_0065B933:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_rsp - 95 - 89, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1568)), *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    if ((*(unsigned int *)(v_rip + 9876445)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    }
    if (1 == 0) goto loc_0065B96F;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    v_rsi = 0;
    goto loc_0065BA00;
loc_0065B96F:
    result = MiLockWorkingSetExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    *(unsigned int *)(v_rsp - 95 + 127) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1208)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1208))) >> (24));
    a2 = (unsigned __int8)((a2) | (2));
    *(unsigned __int8 *)(v_rsp - 95 + 130) = (unsigned __int8)(a2);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 + 127))) >> (24));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1211) = (unsigned __int8)(a2);
    result = MiUnlockWorkingSetExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, (unsigned __int8)(result), *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rsp - 95 - 105), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 97) + 176), *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    if (sign_flag) goto loc_0065BA10;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 40)) & (0xFFFFFFFFFFFFF000ULL);
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rsp - 95 - 105), a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
loc_0065BA00:
    if (sign_flag) goto loc_0065BA10;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 119)) = (unsigned int)(v_r12);
    goto loc_0065BAB5;
loc_0065BA10:
loc_0065BA14:
    if (*(unsigned __int64 *)(v_rsp - 95 - 97) == 0) goto loc_0065BA2B;
    result = *(unsigned __int64 *)(v_rsp - 95 + 119);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 95 + 111)) != 0) {
        a2 = *(unsigned __int64 *)(v_rsp - 95 - 105);
        result = ExpSvmDereferenceDevice(*(unsigned __int64 *)(v_rsp - 95 - 97), a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    }
    if (0 == 0) goto loc_0065BAB5;
    result = 15;
    if ((*(unsigned int *)(v_rip + 9876184)) != 0) {
        a2 = 15;
        a1 = (unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)));
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    }
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1560, v_rsp - 95 - 89, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 8)) != 0) goto loc_0065BB0A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8))) != 0) goto loc_0065BB0A;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8)) = *(unsigned __int64 *)(v_rsi);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 8) = *(unsigned __int64 *)(v_rsi + 8);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_rsp - 95 - 89, v_rsp - 95 - 89, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    if ((*(unsigned int *)(v_rip + 9876107)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    }
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
loc_0065BAB5:
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rsp - 95 - 49), a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
loc_0065BACD:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1552;
        result = ExfTryToWakePushLock(a1, a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1552, a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(v_rsp - 95 - 65), a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    result = ExReleaseRundownProtection(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 488, a2, *(unsigned __int64 *)(v_rsp - 95 + 103), v_rsp - 95 - 105);
    goto loc_0065BB16;
loc_0065BB0A:
loc_0065BB11:
loc_0065BB16:
    v_rsp = (v_rsp) + (200);
    return (unsigned int)(0xC00000BBULL);
}
```

## 5. (Beta) C Style

```c
int64_t ExpShareAddressSpaceWithDevice(int64_t Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint16_t v_stack_mE8;

    *(void **)(local_rsp + 0x18) = Arg3;
    *(uint8_t *)(local_rsp + 0x10) = (uint8_t)(Arg2);
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (200);
    Arg2 = 0;
    result = memset(local_rsp - 95 - 57, Arg2, Arg2 + 80, a4);
    local_r13 = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x61) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x59) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x49) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x69) = 0;
    if ((*(uint64_t *)(v_rip + 0x89F36B)) == 0) goto loc_0065BB11;
    if (Arg1 != 0) goto loc_0065B59C;
    goto loc_0065BB16;
loc_0065B59C:
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = *(uint64_t *)(gs_base + (0 + 0x188));
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x5FC)) & (0x1000ULL)) != 0) goto loc_0065BB11;
    result = ExAcquireRundownProtection(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 488, Arg2, Arg2 + 80, a4);
    if ((uint8_t)(result) != 0) goto loc_0065B5DE;
    goto loc_0065BB16;
loc_0065B5DE:
    v_stack_mD8 = local_rsp - 95 - 57;
    v_stack_mE0 = Arg1;
    v_stack_mE8 = 1;
    result = IoQueryInterface(Arg1, 0, v_rip - 6559396, 80);
    local_rbx = (Arg1) | (-1);
    if (sign_flag) goto loc_0065BACD;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1552, Arg2, Arg3, 80);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1552;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1552;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, 80);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x600))) != 0) goto loc_0065B693;
    result = ExpAllocateAsid(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, 80);
    if ((uint32_t)(result) != 0) goto loc_0065B67E;
    goto loc_0065BAB5;
loc_0065B67E:
    result = ExpAssignPasid(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)((uint32_t)(result)), Arg3, 80);
    local_r12 = (uint32_t)((uint32_t)(result));
    if ((uint32_t)(result) == 0) {
        local_r12 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x600);
    }
    local_r12 = (uint32_t)((local_r12) - 1);
    *(uint64_t *)(local_rsp - 0x5F - 0x69) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x608);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x608) != 0) goto loc_0065B762;
    Arg2 = 0;
    result = guard_dispatch_icall((uint32_t)((uint32_t)(local_r12)), Arg2, 1, local_rsp - 95 - 105);
    if (sign_flag) goto loc_0065BAB5;
    if ((*(uint32_t *)(v_rip + 0x96B63C)) != 0) {
        Arg2 = 15;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, 1, local_rsp - 95 - 105);
    }
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1560, local_rsp - 95 - 89, 1, local_rsp - 95 - 105);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x608) == 0) goto loc_0065B717;
    *(uint64_t *)(local_rsp - 0x5F - 0x69) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x608);
    goto loc_0065B725;
loc_0065B717:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x608) = *(uint64_t *)(local_rsp - 0x5F - 0x69);
loc_0065B725:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(local_rsp - 95 - 89, local_rsp - 95 - 89, 1, local_rsp - 95 - 105);
    if ((*(uint32_t *)(v_rip + 0x96B5EC)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, local_rsp - 95 - 105);
    }
    result = (uint8_t)(v_cr8);
    if (0 != 0) {
        result = *(uint64_t *)(v_rip + 0x7AB5D2);
        Arg1 = 0;
        result = *(uint64_t *)(result + 0x40);
        result = guard_dispatch_icall(Arg1, Arg2, 1, local_rsp - 95 - 105);
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 9040252, Arg2, Arg3, local_rsp - 95 - 105);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 9040223;
        Arg2 = result;
        Arg1 = v_rip + 9040213;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, local_rsp - 95 - 105);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(v_rip + 0x89F147)) == (v_rip + 9040192)) goto loc_0065B7DB;
loc_0065B7B9:
    *(uint64_t *)(local_rsp - 0x5F - 0x61) = *(uint64_t *)(v_rip + 0x89F147);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x89F147) + 0x18)) == (*(uint64_t *)(local_rsp - 0x5F + 0x67))) goto loc_0065B7D1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x89F147))) != (v_rip + 9040192)) goto loc_0065B7B9;
loc_0065B7D1:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x89F147) + 0x18)) == (*(uint64_t *)(local_rsp - 0x5F + 0x67))) goto loc_0065B84D;
loc_0065B7DB:
    v_stack_mE8 = local_rsp - 95 - 97;
    result = ExpPrepareNewSvmDevice(*(uint64_t *)(local_rsp - 0x5F + 0x67), *(uint64_t *)(local_rsp - 0x5F - 0x69), local_rsp - 95 - 57, local_rsp - 95 - 105);
    if (sign_flag) goto loc_0065B85D;
loc_0065B7F7:
    *(uint8_t *)(local_rsp - 0x5F + 0x6F) = 1;
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = v_rip + 9040081;
        result = ExfTryToWakePushLock(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x69), local_rsp - 95 - 57, local_rsp - 95 - 105);
    }
    result = KeAbPostRelease(v_rip + 9040069, *(uint64_t *)(local_rsp - 0x5F - 0x69), local_rsp - 95 - 57, local_rsp - 95 - 105);
    result = ExAllocatePool2(24 + 40, 24, (uint32_t)(0x64507845ULL), local_rsp - 95 - 105);
    if (result != 0) goto loc_0065B8B8;
    goto loc_0065BA14;
loc_0065B84D:
    if (*(uint64_t *)(v_rip + 0x89F147) == 0) goto loc_0065B7DB;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x89F147) + 0x11)) == ((uint8_t)(result))) goto loc_0065B88F;
loc_0065B85D:
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = v_rip + 9039986;
        result = ExfTryToWakePushLock(Arg1, 24, (uint32_t)(0x64507845ULL), local_rsp - 95 - 105);
    }
    result = KeAbPostRelease(v_rip + 9039974, 24, (uint32_t)(0x64507845ULL), local_rsp - 95 - 105);
    goto loc_0065BA14;
loc_0065B88F:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x89F147) + 0x10)) == ((uint8_t)(result))) goto loc_0065B8AB;
    result = ExpConvertSvmDevice(*(uint64_t *)(local_rsp - 0x5F - 0x69), (uint8_t)(result), (uint32_t)(0x64507845ULL), local_rsp - 95 - 105);
    if (sign_flag) goto loc_0065B85D;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x89F147) + 0x10) = (uint8_t)(result);
loc_0065B8AB:
    goto loc_0065B7F7;
loc_0065B8B8:
    local_r13 = 0;
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(local_rsp - 0x5F - 0x61);
    result = *(uint64_t *)(local_rsp - 0x5F - 0x61);
    if ((*(uint32_t *)(v_rip + 0x96B449)) != 0) {
        Arg1 = (uint8_t)((uint8_t)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, 15, (uint32_t)(0x64507845ULL), local_rsp - 95 - 105);
    }
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1560, local_rsp - 95 - 89, (uint32_t)(0x64507845ULL), local_rsp - 95 - 105);
loc_0065B8FF:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x620)) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1568)) goto loc_0065B918;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x620) + 0x10) + 0x18)) == (*(uint64_t *)(local_rsp - 0x5F + 0x67))) goto loc_0065B913;
    goto loc_0065B8FF;
loc_0065B913:
    goto loc_0065B933;
loc_0065B918:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x620) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1568)) goto loc_0065BB0A;
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x620);
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1568;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x620) + 0x8) = result;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x620) = result;
loc_0065B933:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(local_rsp - 95 - 89, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x620)), *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    if ((*(uint32_t *)(v_rip + 0x96B3DD)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    }
    if (1 == 0) goto loc_0065B96F;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    local_rsi = 0;
    goto loc_0065BA00;
loc_0065B96F:
    result = MiLockWorkingSetExclusive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    *(uint32_t *)(local_rsp - 0x5F + 0x7F) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4B8)));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4B8))) >> (24));
    Arg2 = (uint8_t)((Arg2) | (2));
    *(uint8_t *)(local_rsp - 0x5F + 0x82) = (uint8_t)(Arg2);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x7F))) >> (24));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4BB) = (uint8_t)(Arg2);
    result = MiUnlockWorkingSetExclusive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, (uint8_t)(result), *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    result = guard_dispatch_icall(*(uint64_t *)(local_rsp - 0x5F - 0x69), *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x61) + 0xB0), *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    if (sign_flag) goto loc_0065BA10;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x28)) & (0xFFFFFFFFFFFFF000ULL);
    result = guard_dispatch_icall(*(uint64_t *)(local_rsp - 0x5F - 0x69), Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
loc_0065BA00:
    if (sign_flag) goto loc_0065BA10;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x77)) = (uint32_t)(local_r12);
    goto loc_0065BAB5;
loc_0065BA10:
loc_0065BA14:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x61) == 0) goto loc_0065BA2B;
    result = *(uint64_t *)(local_rsp - 0x5F + 0x77);
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x5F + 0x6F)) != 0) {
        Arg2 = *(uint64_t *)(local_rsp - 0x5F - 0x69);
        result = ExpSvmDereferenceDevice(*(uint64_t *)(local_rsp - 0x5F - 0x61), Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    }
    if (0 == 0) goto loc_0065BAB5;
    result = 15;
    if ((*(uint32_t *)(v_rip + 0x96B2D8)) != 0) {
        Arg2 = 15;
        Arg1 = (uint8_t)((uint8_t)((uint8_t)(v_cr8)));
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    }
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1560, local_rsp - 95 - 89, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi) + 0x8)) != 0) goto loc_0065BB0A;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8))) != 0) goto loc_0065BB0A;
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x8)) = *(uint64_t *)(local_rsi);
    *(uint64_t *)(*(uint64_t *)(local_rsi) + 0x8) = *(uint64_t *)(local_rsi + 0x8);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(local_rsp - 95 - 89, local_rsp - 95 - 89, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    if ((*(uint32_t *)(v_rip + 0x96B28B)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)((uint8_t)((uint8_t)(v_cr8)));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
loc_0065BAB5:
    result = guard_dispatch_icall(*(uint64_t *)(local_rsp - 0x5F - 0x31), Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
loc_0065BACD:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1552;
        result = ExfTryToWakePushLock(Arg1, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    }
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1552, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(local_rsp - 0x5F - 0x41), Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    result = ExReleaseRundownProtection(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 488, Arg2, *(uint64_t *)(local_rsp - 0x5F + 0x67), local_rsp - 95 - 105);
    goto loc_0065BB16;
loc_0065BB0A:
loc_0065BB11:
loc_0065BB16:
    local_rsp = (local_rsp) + (200);
    return (uint32_t)(0xC00000BBULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065B528&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
