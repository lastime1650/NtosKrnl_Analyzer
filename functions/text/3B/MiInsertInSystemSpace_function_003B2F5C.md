# MiInsertInSystemSpace

- RVA: `0x003B2F5C`–`0x003B36C6` (길이 `1,898` bytes)
- VA: `0x00000001403B2F5C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008C464`
- 디코드: `461`개 명령, `1,898/1,898` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x003B2F9B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003B2FE4` → [MiSectionControlArea](../29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x003B3005` → [MiOffsetToProtos](../24/MiOffsetToProtos_function_0024D880.md) (function, `0x0024D880`)
- `0x003B309A` → [MiReservePtes](../31/MiReservePtes_function_00318D20.md) (function, `0x00318D20`)
- `0x003B30DF` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x003B310B` → [MiControlAreaRequiresCharge](MiControlAreaRequiresCharge_function_003B36CC.md) (function, `0x003B36CC`)
- `0x003B3196` → [MiReferenceFileObjectForMap](../../page/88/MiReferenceFileObjectForMap_function_00885C00.md) (function, `0x00885C00`)
- `0x003B31D0` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x003B31EA` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x003B3200` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x003B3267` → [RtlAvlInsertNodeEx](../26/RtlAvlInsertNodeEx_function_00265790.md) (function, `0x00265790`)
- `0x003B3276` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x003B329D` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x003B32BA` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x003B3301` → [MiReferenceDataSubsections](MiReferenceDataSubsections_function_003B3768.md) (function, `0x003B3768`)
- `0x003B3335` → [MiGetPageTablesForLargeMap](MiGetPageTablesForLargeMap_function_003B48D4.md) (function, `0x003B48D4`)
- `0x003B33BF` → [MiReferenceActiveSubsection](../32/MiReferenceActiveSubsection_function_00325060.md) (function, `0x00325060`)
- `0x003B33DD` → [MiChargeCommit](../28/MiChargeCommit_function_00286EB0.md) (function, `0x00286EB0`)
- `0x003B3404` → [MiUnlockControlAreaFileObjectExclusive](../2E/MiUnlockControlAreaFileObjectExclusive_function_002E22D0.md) (function, `0x002E22D0`)
- `0x003B3425` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x003B3449` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x003B34BD` → [MiAddMappedPtes](../34/MiAddMappedPtes_function_00349030.md) (function, `0x00349030`)
- `0x003B34F4` → [MiRemoveFromSystemSpace](../29/MiRemoveFromSystemSpace_function_002962FC.md) (function, `0x002962FC`)
- `0x003B3544` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x003B3552` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x003B35A3` → [MiCreatePerSessionProtos](../../page/A6/MiCreatePerSessionProtos_function_00A666D8.md) (function, `0x00A666D8`)
- `0x003B35D6` → [MiUnmapLargePages](../3F/MiUnmapLargePages_function_003F8BFC.md) (function, `0x003F8BFC`)
- `0x003B35FA` → [MiDereferenceDataSubsections](../69/MiDereferenceDataSubsections_function_00692530.md) (function, `0x00692530`)
- `0x003B360B` → [MiDereferencePerSessionProtos](../../page/A2/MiDereferencePerSessionProtos_function_00A2EDE8.md) (function, `0x00A2EDE8`)
- `0x003B361F` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x003B3645` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x003B36B2` → [MiGetAnyMultiplexedVm](../44/MiGetAnyMultiplexedVm_function_00448BD0.md) (function, `0x00448BD0`)

### Direct callers
- [AlpcpCreateView](../../page/88/AlpcpCreateView_function_0088A9B8.md) at `0x0088AD69`
- [MiUpdateCfgSystemWideBitmapWorker](../../page/8C/MiUpdateCfgSystemWideBitmapWorker_function_008CE650.md) at `0x008CE73A`
- [MiMapImageInSystemSpace](../../page/94/MiMapImageInSystemSpace_function_00941DD8.md) at `0x00941F28`
- [KsepSdbMapToMemory](../../page/95/KsepSdbMapToMemory_function_0095B81C.md) at `0x0095B984`
- [MiMapViewInSystemSpace](../../page/98/MiMapViewInSystemSpace_function_009824D8.md) at `0x0098257D`
- [NtGetNlsSectionPtr](../../page/A1/NtGetNlsSectionPtr_function_00A195B0.md) at `0x00A19A6E`

### Static image references
- `0x003B3022` → RVA `0x00E3802E` (`.data`; read)
- `0x003B3074` → RVA `0x00E30088` (`.data`; read)
- `0x003B3093` → RVA `0x00E35E20` (`.data`; read)
- `0x003B31B7` → RVA `0x00E36040` (`.data`; read)
- `0x003B31F9` → RVA `0x00E37F80` (`.data`; read)
- `0x003B3205` → RVA `0x00E36048` (`.data`; read)
- `0x003B3212` → RVA `0x00E36050` (`.data`; read/write)
- `0x003B3409` → RVA `0x00E36040` (`.data`; read/write)
- `0x003B347B` → RVA `0x00010880` (`.rdata`; read)
- `0x003B34E9` → RVA `0x00E35E50` (`.data`; read/write)
- `0x003B3633` → RVA `0x00E36280` (`.data`; read)
- `0x003B3679` → RVA `0x00011C60` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x003B3196` → [MiReferenceFileObjectForMap](../../page/88/MiReferenceFileObjectForMap_function_00885C00.md) (`.text` → `PAGE`)
  - `0x003B3544` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x003B35A3` → [MiCreatePerSessionProtos](../../page/A6/MiCreatePerSessionProtos_function_00A666D8.md) (`.text` → `PAGE`)
  - `0x003B360B` → [MiDereferencePerSessionProtos](../../page/A2/MiDereferencePerSessionProtos_function_00A2EDE8.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x003B35AA` → [sub_006E710A](../6E/Unknown_function_006E710A.md) (`tail-transfer`)
  - `0x003B35BE` → [sub_006E710A + 0xA](../6E/Unknown_function_006E710A.md) (`tail-transfer`)
  - `0x003B3660` → [sub_006E710A + 0x24](../6E/Unknown_function_006E710A.md) (`tail-transfer`)
  - `0x003B3666` → [sub_006E710A + 0x4B](../6E/Unknown_function_006E710A.md) (`tail-transfer`)
  - `0x003B36A7` → [sub_006E710A + 0xF0](../6E/Unknown_function_006E710A.md) (`tail-transfer`)
  - `0x003B36C1` → [sub_006E710A + 0x7B](../6E/Unknown_function_006E710A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003B2F5C  48 8B C4                        mov rax, rsp
003B2F5F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
003B2F63  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
003B2F67  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
003B2F6B  55                              push rbp
003B2F6C  53                              push rbx
003B2F6D  56                              push rsi
003B2F6E  57                              push rdi
003B2F6F  41 54                           push r12
003B2F71  41 55                           push r13
003B2F73  41 56                           push r14
003B2F75  41 57                           push r15
003B2F77  48 8D 68 88                     lea rbp, [rax - 0x78]
003B2F7B  48 81 EC 38 01 00 00            sub rsp, 0x138
003B2F82  4C 8B F2                        mov r14, rdx
003B2F85  48 8B D9                        mov rbx, rcx
003B2F88  45 33 E4                        xor r12d, r12d
003B2F8B  48 8D 4D 98                     lea rcx, [rbp - 0x68]
003B2F8F  33 D2                           xor edx, edx
003B2F91  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
003B2F95  41 B8 90 00 00 00               mov r8d, 0x90
003B2F9B  E8 A0 3C 31 00                  call 0x1406c6c40
003B2FA0  48 8B 85 A8 00 00 00            mov rax, qword ptr [rbp + 0xa8]
003B2FA7  45 8B EC                        mov r13d, r12d
003B2FAA  41 8B F4                        mov esi, r12d
003B2FAD  44 88 A5 80 00 00 00            mov byte ptr [rbp + 0x80], r12b
003B2FB4  41 8B FC                        mov edi, r12d
003B2FB7  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
003B2FBC  45 8B FC                        mov r15d, r12d
003B2FBF  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
003B2FC4  4C 89 20                        mov qword ptr [rax], r12
003B2FC7  49 8B CE                        mov rcx, r14
003B2FCA  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
003B2FCF  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
003B2FD3  45 8D 65 03                     lea r12d, [r13 + 3]
003B2FD7  44 89 64 24 44                  mov dword ptr [rsp + 0x44], r12d
003B2FDC  C7 44 24 48 FF FF 07 00         mov dword ptr [rsp + 0x48], 0x7ffff
003B2FE4  E8 C7 1C EE FF                  call 0x140294cb0
003B2FE9  48 8B 95 90 00 00 00            mov rdx, qword ptr [rbp + 0x90]
003B2FF0  4C 8D 45 88                     lea r8, [rbp - 0x78]
003B2FF4  4C 8B F0                        mov r14, rax
003B2FF7  0F B7 C3                        movzx eax, bx
003B2FFA  49 8B CE                        mov rcx, r14
003B2FFD  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
003B3002  48 8B 12                        mov rdx, qword ptr [rdx]
003B3005  E8 76 A8 E9 FF                  call 0x14024d880
003B300A  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003B300F  48 85 C0                        test rax, rax
003B3012  0F 84 4C 05 00 00               je 0x1403b3564
003B3018  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
003B301F  41 8B D5                        mov edx, r13d
003B3022  0F B7 0D 05 50 A8 00            movzx ecx, word ptr [rip + 0xa85005]
003B3029  83 E0 08                        and eax, 8
003B302C  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
003B3033  48 F7 D8                        neg rax
003B3036  1B C0                           sbb eax, eax
003B3038  F7 D8                           neg eax
003B303A  83 C0 02                        add eax, 2
003B303D  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
003B3041  48 F7 C3 FF 0F 00 00            test rbx, 0xfff
003B3048  48 8B C3                        mov rax, rbx
003B304B  0F 95 C2                        setne dl
003B304E  48 C1 E8 0C                     shr rax, 0xc
003B3052  48 03 D0                        add rdx, rax
003B3055  33 C0                           xor eax, eax
003B3057  48 39 44 24 70                  cmp qword ptr [rsp + 0x70], rax
003B305C  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
003B3061  0F 95 C0                        setne al
003B3064  48 C1 EB 10                     shr rbx, 0x10
003B3068  48 03 C3                        add rax, rbx
003B306B  48 C1 E0 04                     shl rax, 4
003B306F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003B3074  48 8B 05 0D D0 A7 00            mov rax, qword ptr [rip + 0xa7d00d]
003B307B  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
003B307F  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
003B3083  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
003B3087  A8 20                           test al, 0x20
003B3089  0F 84 60 02 00 00               je 0x1403b32ef
003B308F  8B 54 24 58                     mov edx, dword ptr [rsp + 0x58]
003B3093  48 8D 0D 86 2D A8 00            lea rcx, [rip + 0xa82d86]
003B309A  E8 81 5C F6 FF                  call 0x140318d20
003B309F  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003B30A4  48 85 C0                        test rax, rax
003B30A7  0F 84 C5 04 00 00               je 0x1403b3572
003B30AD  48 8B F0                        mov rsi, rax
003B30B0  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003B30BA  48 C1 E6 19                     shl rsi, 0x19
003B30BE  48 8B C0                        mov rax, rax
003B30C1  48 C1 E0 19                     shl rax, 0x19
003B30C5  48 2B F0                        sub rsi, rax
003B30C8  48 C1 FE 10                     sar rsi, 0x10
003B30CC  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
003B30D1  BA 68 00 00 00                  mov edx, 0x68
003B30D6  41 B8 4D 69 56 77               mov r8d, 0x7756694d
003B30DC  8D 4A D8                        lea ecx, [rdx - 0x28]
003B30DF  E8 5C 84 FA FF                  call 0x14035b540
003B30E4  48 8B F8                        mov rdi, rax
003B30E7  48 85 C0                        test rax, rax
003B30EA  0F 84 0B 04 00 00               je 0x1403b34fb
003B30F0  8B 40 38                        mov eax, dword ptr [rax + 0x38]
003B30F3  41 8B CC                        mov ecx, r12d
003B30F6  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
003B30FA  83 E1 03                        and ecx, 3
003B30FD  C1 E1 03                        shl ecx, 3
003B3100  83 E0 E7                        and eax, 0xffffffe7
003B3103  0B C8                           or ecx, eax
003B3105  89 4F 38                        mov dword ptr [rdi + 0x38], ecx
003B3108  49 8B CE                        mov rcx, r14
003B310B  E8 BC 05 00 00                  call 0x1403b36cc
003B3110  8B D8                           mov ebx, eax
003B3112  85 C0                           test eax, eax
003B3114  0F 84 62 04 00 00               je 0x1403b357c
003B311A  83 F8 02                        cmp eax, 2
003B311D  0F 84 63 04 00 00               je 0x1403b3586
003B3123  4C 8B AD 88 00 00 00            mov r13, qword ptr [rbp + 0x88]
003B312A  B8 01 00 00 00                  mov eax, 1
003B312F  41 F7 45 38 00 00 00 10         test dword ptr [r13 + 0x38], 0x10000000
003B3137  0F 85 52 04 00 00               jne 0x1403b358f
003B313D  84 85 98 00 00 00               test byte ptr [rbp + 0x98], al
003B3143  74 04                           je 0x1403b3149
003B3145  83 4F 38 02                     or dword ptr [rdi + 0x38], 2
003B3149  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
003B314D  A8 20                           test al, 0x20
003B314F  0F 85 24 02 00 00               jne 0x1403b3379
003B3155  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
003B315A  49 8B CD                        mov rcx, r13
003B315D  48 C1 E0 0C                     shl rax, 0xc
003B3161  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
003B3165  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
003B316A  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
003B316E  48 8B 85 90 00 00 00            mov rax, qword ptr [rbp + 0x90]
003B3175  48 8B 00                        mov rax, qword ptr [rax]
003B3178  48 C1 E8 0C                     shr rax, 0xc
003B317C  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
003B3180  48 8B C6                        mov rax, rsi
003B3183  48 83 C8 02                     or rax, 2
003B3187  4C 89 7F 28                     mov qword ptr [rdi + 0x28], r15
003B318B  48 89 47 58                     mov qword ptr [rdi + 0x58], rax
003B318F  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
003B3193  89 47 60                        mov dword ptr [rdi + 0x60], eax
003B3196  E8 65 2A 4D 00                  call 0x140885c00
003B319B  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
003B319F  65 4C 8B 24 25 88 01 00 00      mov r12, qword ptr gs:[0x188]
003B31A8  83 7C 24 44 00                  cmp dword ptr [rsp + 0x44], 0
003B31AD  0F 84 76 04 00 00               je 0x1403b3629
003B31B3  48 83 CB FF                     or rbx, 0xffffffffffffffff
003B31B7  4C 8D 2D 82 2E A8 00            lea r13, [rip + 0xa82e82]
003B31BE  66 41 01 9C 24 E6 01 00 00      add word ptr [r12 + 0x1e6], bx
003B31C7  49 8B CD                        mov rcx, r13
003B31CA  45 33 C0                        xor r8d, r8d
003B31CD  33 D2                           xor edx, edx
003B31CF  90                              nop
003B31D0  E8 5B D0 E5 FF                  call 0x140210230
003B31D5  F0 49 0F BA 6D 00 00            lock bts qword ptr [r13], 0
003B31DC  4C 8B F8                        mov r15, rax
003B31DF  73 0E                           jae 0x1403b31ef
003B31E1  4D 8B C5                        mov r8, r13
003B31E4  48 8B D0                        mov rdx, rax
003B31E7  49 8B CD                        mov rcx, r13
003B31EA  E8 A1 CA E5 FF                  call 0x14020fc90
003B31EF  4D 85 FF                        test r15, r15
003B31F2  74 05                           je 0x1403b31f9
003B31F4  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
003B31F9  48 8D 0D 80 4D A8 00            lea rcx, [rip + 0xa84d80]
003B3200  E8 9B 06 F7 FF                  call 0x1403238a0
003B3205  48 8B 15 3C 2E A8 00            mov rdx, qword ptr [rip + 0xa82e3c]
003B320C  41 B9 01 00 00 00               mov r9d, 1
003B3212  44 01 0D 37 2E A8 00            add dword ptr [rip + 0xa82e37], r9d
003B3219  45 32 C0                        xor r8b, r8b
003B321C  44 8A F8                        mov r15b, al
003B321F  48 85 D2                        test rdx, rdx
003B3222  74 39                           je 0x1403b325d
003B3224  4C 8B 42 58                     mov r8, qword ptr [rdx + 0x58]
003B3228  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
003B322C  49 81 E0 00 F0 FF FF            and r8, 0xfffffffffffff000
003B3233  49 03 C0                        add rax, r8
003B3236  49 3B F0                        cmp rsi, r8
003B3239  73 16                           jae 0x1403b3251
003B323B  48 3B F0                        cmp rsi, rax
003B323E  73 11                           jae 0x1403b3251
003B3240  48 8B 02                        mov rax, qword ptr [rdx]
003B3243  48 85 C0                        test rax, rax
003B3246  0F 84 10 03 00 00               je 0x1403b355c
003B324C  48 8B D0                        mov rdx, rax
003B324F  EB D3                           jmp 0x1403b3224
003B3251  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
003B3255  48 85 C0                        test rax, rax
003B3258  75 F2                           jne 0x1403b324c
003B325A  45 8A C1                        mov r8b, r9b
003B325D  4C 8B CF                        mov r9, rdi
003B3260  48 8D 0D E1 2D A8 00            lea rcx, [rip + 0xa82de1]
003B3267  E8 24 25 EB FF                  call 0x140265790
003B326C  41 8A D7                        mov dl, r15b
003B326F  48 8D 0D 0A 4D A8 00            lea rcx, [rip + 0xa84d0a]
003B3276  E8 F5 B9 EC FF                  call 0x14027ec70
003B327B  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
003B327F  49 8D 4E 68                     lea rcx, [r14 + 0x68]
003B3283  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003B328C  4C 8D 7F 48                     lea r15, [rdi + 0x48]
003B3290  45 33 C0                        xor r8d, r8d
003B3293  33 D2                           xor edx, edx
003B3295  66 01 98 E6 01 00 00            add word ptr [rax + 0x1e6], bx
003B329C  90                              nop
003B329D  E8 8E CF E5 FF                  call 0x140210230
003B32A2  4C 8B E8                        mov r13, rax
003B32A5  49 8D 46 68                     lea rax, [r14 + 0x68]
003B32A9  F0 48 0F BA 28 00               lock bts qword ptr [rax], 0
003B32AF  73 0E                           jae 0x1403b32bf
003B32B1  4C 8B C0                        mov r8, rax
003B32B4  49 8B D5                        mov rdx, r13
003B32B7  48 8B C8                        mov rcx, rax
003B32BA  E8 D1 C9 E5 FF                  call 0x14020fc90
003B32BF  4D 85 ED                        test r13, r13
003B32C2  74 05                           je 0x1403b32c9
003B32C4  41 C6 45 0A 01                  mov byte ptr [r13 + 0xa], 1
003B32C9  41 F7 46 38 00 04 00 00         test dword ptr [r14 + 0x38], 0x400
003B32D1  0F 85 2A 01 00 00               jne 0x1403b3401
003B32D7  49 8D 46 08                     lea rax, [r14 + 8]
003B32DB  48 8B 10                        mov rdx, qword ptr [rax]
003B32DE  48 39 42 08                     cmp qword ptr [rdx + 8], rax
003B32E2  0F 84 0B 01 00 00               je 0x1403b33f3
003B32E8  B9 03 00 00 00                  mov ecx, 3
003B32ED  CD 29                           int 0x29
003B32EF  4C 8B C2                        mov r8, rdx
003B32F2  4C 8D 4C 24 44                  lea r9, [rsp + 0x44]
003B32F7  48 8B 95 90 00 00 00            mov rdx, qword ptr [rbp + 0x90]
003B32FE  49 8B CE                        mov rcx, r14
003B3301  E8 62 04 00 00                  call 0x1403b3768
003B3306  44 8B 64 24 44                  mov r12d, dword ptr [rsp + 0x44]
003B330B  8B D8                           mov ebx, eax
003B330D  85 C0                           test eax, eax
003B330F  0F 88 F0 01 00 00               js 0x1403b3505
003B3315  C6 85 80 00 00 00 01            mov byte ptr [rbp + 0x80], 1
003B331C  41 83 FC 03                     cmp r12d, 3
003B3320  0F 83 69 FD FF FF               jae 0x1403b308f
003B3326  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
003B332B  45 33 C9                        xor r9d, r9d
003B332E  45 8B C4                        mov r8d, r12d
003B3331  41 8D 51 08                     lea edx, [r9 + 8]
003B3335  E8 9A 15 00 00                  call 0x1403b48d4
003B333A  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
003B333F  48 8B F0                        mov rsi, rax
003B3342  48 85 C0                        test rax, rax
003B3345  0F 84 20 02 00 00               je 0x1403b356b
003B334B  48 8B D8                        mov rbx, rax
003B334E  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003B3358  48 C1 EB 09                     shr rbx, 9
003B335C  48 23 D8                        and rbx, rax
003B335F  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003B3369  48 8B C0                        mov rax, rax
003B336C  48 03 D8                        add rbx, rax
003B336F  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
003B3374  E9 58 FD FF FF                  jmp 0x1403b30d1
003B3379  0F BA E0 1B                     bt eax, 0x1b
003B337D  0F 82 14 02 00 00               jb 0x1403b3597
003B3383  49 8B 06                        mov rax, qword ptr [r14]
003B3386  4C 8B 78 30                     mov r15, qword ptr [rax + 0x30]
003B338A  4D 85 FF                        test r15, r15
003B338D  75 44                           jne 0x1403b33d3
003B338F  83 FB 02                        cmp ebx, 2
003B3392  0F 85 BD FD FF FF               jne 0x1403b3155
003B3398  48 F7 9D A0 00 00 00            neg qword ptr [rbp + 0xa0]
003B339F  49 8D 86 80 00 00 00            lea rax, [r14 + 0x80]
003B33A6  41 B0 11                        mov r8b, 0x11
003B33A9  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003B33AE  1B D2                           sbb edx, edx
003B33B0  48 8B C8                        mov rcx, rax
003B33B3  81 E2 00 01 00 00               and edx, 0x100
003B33B9  81 C2 88 00 00 00               add edx, 0x88
003B33BF  E8 9C 1C F7 FF                  call 0x140325060
003B33C4  8B D8                           mov ebx, eax
003B33C6  85 C0                           test eax, eax
003B33C8  0F 89 87 FD FF FF               jns 0x1403b3155
003B33CE  E9 2D 01 00 00                  jmp 0x1403b3500
003B33D3  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
003B33D7  45 33 C0                        xor r8d, r8d
003B33DA  49 8B D7                        mov rdx, r15
003B33DD  E8 CE 3A ED FF                  call 0x140286eb0
003B33E2  85 C0                           test eax, eax
003B33E4  75 A9                           jne 0x1403b338f
003B33E6  45 33 FF                        xor r15d, r15d
003B33E9  BB 2D 01 00 C0                  mov ebx, 0xc000012d
003B33EE  E9 0D 01 00 00                  jmp 0x1403b3500
003B33F3  49 89 17                        mov qword ptr [r15], rdx
003B33F6  49 89 47 08                     mov qword ptr [r15 + 8], rax
003B33FA  4C 89 7A 08                     mov qword ptr [rdx + 8], r15
003B33FE  4C 89 38                        mov qword ptr [rax], r15
003B3401  49 8B CE                        mov rcx, r14
003B3404  E8 C7 EE F2 FF                  call 0x1402e22d0
003B3409  F0 48 0F C1 1D 2E 2C A8 00      lock xadd qword ptr [rip + 0xa82c2e], rbx
003B3412  80 E3 06                        and bl, 6
003B3415  80 FB 02                        cmp bl, 2
003B3418  0F 84 2D 01 00 00               je 0x1403b354b
003B341E  48 8D 0D 1B 2C A8 00            lea rcx, [rip + 0xa82c1b]
003B3425  E8 D6 E1 F2 FF                  call 0x1402e1600
003B342A  B9 01 00 00 00                  mov ecx, 1
003B342F  90                              nop
003B3430  66 41 01 8C 24 E6 01 00 00      add word ptr [r12 + 0x1e6], cx
003B3439  75 13                           jne 0x1403b344e
003B343B  49 8D 84 24 98 00 00 00         lea rax, [r12 + 0x98]
003B3443  90                              nop
003B3444  48 39 00                        cmp qword ptr [rax], rax
003B3447  74 05                           je 0x1403b344e
003B3449  E8 32 F8 F2 FF                  call 0x1402e2c80
003B344E  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
003B3451  BF 01 00 00 00                  mov edi, 1
003B3456  40 84 C7                        test dil, al
003B3459  0F 85 0C 02 00 00               jne 0x1403b366b
003B345F  83 7C 24 44 03                  cmp dword ptr [rsp + 0x44], 3
003B3464  0F 82 0B 02 00 00               jb 0x1403b3675
003B346A  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
003B346F  33 D2                           xor edx, edx
003B3471  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
003B3476  48 85 C9                        test rcx, rcx
003B3479  74 19                           je 0x1403b3494
003B347B  48 8B 05 FE D3 C5 FF            mov rax, qword ptr [rip - 0x3a2c02]
003B3482  45 33 C0                        xor r8d, r8d
003B3485  03 D7                           add edx, edi
003B3487  4B 89 44 C5 00                  mov qword ptr [r13 + r8*8], rax
003B348C  44 8B C2                        mov r8d, edx
003B348F  4C 3B C1                        cmp r8, rcx
003B3492  72 F1                           jb 0x1403b3485
003B3494  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
003B3499  4C 8B C1                        mov r8, rcx
003B349C  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
003B34A0  48 8D 0D D9 4A A8 00            lea rcx, [rip + 0xa84ad9]
003B34A7  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003B34AB  4D 8B CE                        mov r9, r14
003B34AE  48 8B 85 90 00 00 00            mov rax, qword ptr [rbp + 0x90]
003B34B5  49 8B D5                        mov rdx, r13
003B34B8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003B34BD  E8 6E 5B F9 FF                  call 0x140349030
003B34C2  8B D8                           mov ebx, eax
003B34C4  85 C0                           test eax, eax
003B34C6  78 21                           js 0x1403b34e9
003B34C8  48 8B 85 A8 00 00 00            mov rax, qword ptr [rbp + 0xa8]
003B34CF  48 89 30                        mov qword ptr [rax], rsi
003B34D2  8B C3                           mov eax, ebx
003B34D4  48 81 C4 38 01 00 00            add rsp, 0x138
003B34DB  41 5F                           pop r15
003B34DD  41 5E                           pop r14
003B34DF  41 5D                           pop r13
003B34E1  41 5C                           pop r12
003B34E3  5F                              pop rdi
003B34E4  5E                              pop rsi
003B34E5  5B                              pop rbx
003B34E6  5D                              pop rbp
003B34E7  C3                              ret
003B34E8  CC                              int3
003B34E9  01 3D 61 29 A8 00               add dword ptr [rip + 0xa82961], edi
003B34EF  33 D2                           xor edx, edx
003B34F1  48 8B CE                        mov rcx, rsi
003B34F4  E8 03 2E EE FF                  call 0x1402962fc
003B34F9  EB D7                           jmp 0x1403b34d2
003B34FB  BB 9A 00 00 C0                  mov ebx, 0xc000009a
003B3500  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
003B3505  B8 01 00 00 00                  mov eax, 1
003B350A  01 05 40 29 A8 00               add dword ptr [rip + 0xa82940], eax
003B3510  4D 85 ED                        test r13, r13
003B3513  0F 85 A1 00 00 00               jne 0x1403b35ba
003B3519  80 BD 80 00 00 00 00            cmp byte ptr [rbp + 0x80], 0
003B3520  0F 85 BA 00 00 00               jne 0x1403b35e0
003B3526  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
003B352B  0F 85 D3 00 00 00               jne 0x1403b3604
003B3531  4D 85 FF                        test r15, r15
003B3534  0F 85 DB 00 00 00               jne 0x1403b3615
003B353A  48 85 FF                        test rdi, rdi
003B353D  74 93                           je 0x1403b34d2
003B353F  33 D2                           xor edx, edx
003B3541  48 8B CF                        mov rcx, rdi
003B3544  E8 27 F3 7C 00                  call 0x140b82870
003B3549  EB 87                           jmp 0x1403b34d2
003B354B  48 8D 0D EE 2A A8 00            lea rcx, [rip + 0xa82aee]
003B3552  E8 79 28 EB FF                  call 0x140265dd0
003B3557  E9 C2 FE FF FF                  jmp 0x1403b341e
003B355C  45 32 C0                        xor r8b, r8b
003B355F  E9 F9 FC FF FF                  jmp 0x1403b325d
003B3564  BB 17 00 00 C0                  mov ebx, 0xc0000017
003B3569  EB 9A                           jmp 0x1403b3505
003B356B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
003B3570  EB 93                           jmp 0x1403b3505
003B3572  BB 9A 00 00 C0                  mov ebx, 0xc000009a
003B3577  4C 8B E8                        mov r13, rax
003B357A  EB 89                           jmp 0x1403b3505
003B357C  BB 0B 06 00 C0                  mov ebx, 0xc000060b
003B3581  E9 7A FF FF FF                  jmp 0x1403b3500
003B3586  83 4F 38 04                     or dword ptr [rdi + 0x38], 4
003B358A  E9 94 FB FF FF                  jmp 0x1403b3123
003B358F  09 47 38                        or dword ptr [rdi + 0x38], eax
003B3592  E9 A6 FB FF FF                  jmp 0x1403b313d
003B3597  83 C8 FF                        or eax, 0xffffffff
003B359A  49 8B CE                        mov rcx, r14
003B359D  8B D0                           mov edx, eax
003B359F  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
003B35A3  E8 30 31 6B 00                  call 0x140a666d8
003B35A8  85 C0                           test eax, eax
003B35AA  0F 89 5A 3B 33 00               jns 0x1406e710a
003B35B0  BB 17 00 00 C0                  mov ebx, 0xc0000017
003B35B5  E9 46 FF FF FF                  jmp 0x1403b3500
003B35BA  41 83 FC 03                     cmp r12d, 3
003B35BE  0F 83 50 3B 33 00               jae 0x1406e7114
003B35C4  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
003B35C9  41 B8 08 00 00 00               mov r8d, 8
003B35CF  48 C1 E2 0C                     shl rdx, 0xc
003B35D3  48 8B CE                        mov rcx, rsi
003B35D6  E8 21 56 04 00                  call 0x1403f8bfc
003B35DB  E9 39 FF FF FF                  jmp 0x1403b3519
003B35E0  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
003B35E5  45 33 C9                        xor r9d, r9d
003B35E8  48 8B 95 90 00 00 00            mov rdx, qword ptr [rbp + 0x90]
003B35EF  41 83 FC 03                     cmp r12d, 3
003B35F3  49 8B CE                        mov rcx, r14
003B35F6  41 0F 92 C1                     setb r9b
003B35FA  E8 31 EF 2D 00                  call 0x140692530
003B35FF  E9 22 FF FF FF                  jmp 0x1403b3526
003B3604  8B 54 24 48                     mov edx, dword ptr [rsp + 0x48]
003B3608  49 8B CE                        mov rcx, r14
003B360B  E8 D8 B7 67 00                  call 0x140a2ede8
003B3610  E9 1C FF FF FF                  jmp 0x1403b3531
003B3615  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
003B3619  45 33 C0                        xor r8d, r8d
003B361C  49 8B D7                        mov rdx, r15
003B361F  E8 EC 4D E9 FF                  call 0x140248410
003B3624  E9 11 FF FF FF                  jmp 0x1403b353a
003B3629  48 8B C6                        mov rax, rsi
003B362C  48 C1 E8 1E                     shr rax, 0x1e
003B3630  0F B6 D8                        movzx ebx, al
003B3633  48 8D 05 46 2C A8 00            lea rax, [rip + 0xa82c46]
003B363A  48 C1 E3 04                     shl rbx, 4
003B363E  48 03 D8                        add rbx, rax
003B3641  48 8D 4B 0C                     lea rcx, [rbx + 0xc]
003B3645  E8 46 50 E9 FF                  call 0x140248690
003B364A  41 B9 01 00 00 00               mov r9d, 1
003B3650  45 32 C0                        xor r8b, r8b
003B3653  44 01 4B 08                     add dword ptr [rbx + 8], r9d
003B3657  44 8A F8                        mov r15b, al
003B365A  48 8B 13                        mov rdx, qword ptr [rbx]
003B365D  48 85 D2                        test rdx, rdx
003B3660  0F 85 C8 3A 33 00               jne 0x1406e712e
003B3666  E9 EA 3A 33 00                  jmp 0x1406e7155
003B366B  F0 41 01 7E 5C                  lock add dword ptr [r14 + 0x5c], edi
003B3670  E9 EA FD FF FF                  jmp 0x1403b345f
003B3675  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
003B3679  48 8D 3D E0 E5 C5 FF            lea rdi, [rip - 0x3a1a20]
003B3680  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
003B3685  45 33 E4                        xor r12d, r12d
003B3688  4C 8B FE                        mov r15, rsi
003B368B  48 8B 3C C7                     mov rdi, qword ptr [rdi + rax*8]
003B368F  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
003B3693  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
003B3697  48 8D 1C C1                     lea rbx, [rcx + rax*8]
003B369B  8B 42 2C                        mov eax, dword ptr [rdx + 0x2c]
003B369E  4C 8D 2C C1                     lea r13, [rcx + rax*8]
003B36A2  4C 39 64 24 58                  cmp qword ptr [rsp + 0x58], r12
003B36A7  0F 86 4D 3B 33 00               jbe 0x1406e71fa
003B36AD  41 8D 4C 24 04                  lea ecx, [r12 + 4]
003B36B2  E8 19 55 09 00                  call 0x140448bd0
003B36B7  4C 8B F7                        mov r14, rdi
003B36BA  48 8B F0                        mov rsi, rax
003B36BD  49 C1 E6 0C                     shl r14, 0xc
003B36C1  E9 BF 3A 33 00                  jmp 0x1406e7185
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInsertInSystemSpace(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned int v_stack_m134;
    unsigned __int8 v_stack_m138;
    unsigned int v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (312);
    v_r12 = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 120 - 120) = 0;
    result = memset(v_rsp - 120 - 104, a2, 144, a4);
    *(unsigned __int8 *)(v_rsp - 120 + 128) = 0;
    v_stack_m138 = 0;
    v_stack_m120 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 120 + 168)) = 0;
    v_stack_m110 = 0;
    *(unsigned __int64 *)(v_rsp - 120 - 128) = 0;
    v_stack_m134 = (unsigned int)(0 + 3);
    v_stack_m130 = 0x7FFFFULL;
    result = MiSectionControlArea(0, a2, 144, a4);
    v_stack_m108 = (unsigned __int16)(a1);
    result = MiOffsetToProtos(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 120 + 144)), v_rsp - 120 - 120, a4);
    v_stack_m118 = result;
    if (result == 0) goto loc_003B3564;
    result = (unsigned int)((*(unsigned __int64 *)(v_rsp - 120 + 160)) & (8));
    *(unsigned __int64 *)(v_rsp - 120 + 160) = result;
    result = -(result);
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) + (2));
    v_stack_m100 = (unsigned int)(result);
    a2 = (((a1) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (a1) >> (12);
    a2 = (a2) + (result);
    result = 0;
    v_stack_m110 = a2;
    result = (v_stack_m108 != 0) ? 1 : 0;
    v_rbx = (a1) >> (16);
    result = (result) + (v_rbx);
    result = (result) << (4);
    v_stack_m120 = result;
    *(unsigned __int64 *)(v_rsp - 120 - 128) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10997773) + *(unsigned __int16 *)(v_rip + 11030533) * 8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 56)))) & (32)) == 0) goto loc_003B32EF;
loc_003B308F:
    result = MiReservePtes(v_rip + 11021702, (unsigned int)(v_stack_m120), v_rsp - 120 - 120, a4);
    v_stack_m128 = result;
    if (result == 0) goto loc_003B3572;
    v_rsi = (result) << (25);
    result = (result) << (25);
    v_rsi = (v_rsi) - (result);
    v_rsi = (v_rsi) >> (16);
    v_stack_m108 = v_rsi;
loc_003B30D1:
    result = MiAllocatePool(104 - 40, 104, (unsigned int)(0x7756694DULL), a4);
    if (result == 0) goto loc_003B34FB;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(0 + 3))) & (3));
    a1 = (unsigned int)((a1) << (3));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 56))) & (0xFFFFFFE7ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    *(unsigned int *)(result + 56) = (unsigned int)(a1);
    result = MiControlAreaRequiresCharge(result, (unsigned int)(v_stack_m100), (unsigned int)(0x7756694DULL), a4);
    if ((unsigned int)(result) == 0) goto loc_003B357C;
    if (((unsigned int)(result)) == 2) goto loc_003B3586;
loc_003B3123:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 120 + 136) + 56)) & (0x10000000ULL)) != 0) goto loc_003B358F;
loc_003B313D:
    if (((*(unsigned __int8 *)(v_rsp - 120 + 152)) & (1)) != 0) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 56)))) & (32)) != 0) goto loc_003B3379;
loc_003B3155:
    result = (v_stack_m110) << (12);
    *(unsigned __int64 *)(result + 32) = result;
    *(unsigned __int64 *)(result + 48) = v_stack_m118;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 120 + 144))) >> (12);
    *(unsigned __int64 *)(result + 24) = result;
    result = (v_rsi) | (2);
    *(unsigned __int64 *)(result + 40) = 0;
    *(unsigned __int64 *)(result + 88) = result;
    *(unsigned int *)(result + 96) = (unsigned int)((unsigned int)(v_stack_m130));
    result = MiReferenceFileObjectForMap(*(unsigned __int64 *)(v_rsp - 120 + 136), (unsigned int)(v_stack_m100), (unsigned int)(0x7756694DULL), a4);
    *(unsigned __int64 *)(result + 64) = result;
    if (v_stack_m134 == 0) goto loc_003B3629;
    v_rbx = ((unsigned int)((unsigned int)(result))) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 11021954, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 11021954;
        a2 = result;
        a1 = v_rip + 11021954;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = MiLockWorkingSetExclusive(v_rip + 11029888, a2, a3, a4);
    a3 = 0;
    if (*(unsigned __int64 *)(v_rip + 11021884) == 0) goto loc_003B325D;
loc_003B3224:
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11021884) + 88)) & (0xFFFFFFFFFFFFF000ULL);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11021884) + 32)) + (a3);
    if (v_rsi >= a3) goto loc_003B3251;
    if (v_rsi >= result) goto loc_003B3251;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11021884)) == 0) goto loc_003B355C;
loc_003B324C:
    goto loc_003B3224;
loc_003B3251:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11021884)) + 8) != 0) goto loc_003B324C;
loc_003B325D:
    result = RtlAvlInsertNodeEx(v_rip + 11021793, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11021884)), 1, result);
    result = MiUnlockWorkingSetExclusive(v_rip + 11029770, (unsigned __int8)((unsigned __int8)(result)), 1, result);
    *(unsigned __int64 *)(v_rsp - 120 - 112) = result;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 104, a2, a3, result);
    result = result + 104;
    if (!(condition_is_above_or_equal)) {
        a3 = result + 104;
        a2 = result;
        a1 = result + 104;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, result);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (((*(unsigned int *)(result + 56)) & (0x400ULL)) != 0) goto loc_003B3401;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8)) == (result + 8)) goto loc_003B33F3;
loc_003B32EF:
    result = MiReferenceDataSubsections(result, *(unsigned __int64 *)(v_rsp - 120 + 144), *(unsigned __int64 *)(result + 8), v_stack_m134);
    if (sign_flag) goto loc_003B3505;
    *(unsigned __int8 *)(v_rsp - 120 + 128) = 1;
    if (((unsigned int)((unsigned int)(v_stack_m134))) >= 3) goto loc_003B308F;
    a4 = 0;
    result = MiGetPageTablesForLargeMap(v_stack_m120, a4 + 8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m134))), a4);
    v_stack_m108 = result;
    if (result == 0) goto loc_003B356B;
    v_rbx = (result) >> (9);
    v_rbx = (v_rbx) & (result);
    v_rbx = (v_rbx) + (result);
    v_stack_m128 = v_rbx;
    goto loc_003B30D1;
loc_003B3379:
    if (condition_is_below) goto loc_003B3597;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 48) != 0) goto loc_003B33D3;
loc_003B338F:
    if (((unsigned int)(v_rbx)) != 2) goto loc_003B3155;
    v_stack_m118 = result + 128;
    a2 = (unsigned int)((a4 + 8) & (256));
    a2 = (unsigned int)((a2) + (136));
    result = MiReferenceActiveSubsection(result + 128, a2, 17, a4);
    if (!sign_flag) goto loc_003B3155;
    goto loc_003B3500;
loc_003B33D3:
    a3 = 0;
    result = MiChargeCommit(*(unsigned __int64 *)(v_rsp - 120 - 128), *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 48), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_003B338F;
    v_r15 = 0;
    goto loc_003B3500;
loc_003B33F3:
    *(unsigned __int64 *)(v_r15) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 48);
    *(unsigned __int64 *)(v_r15 + 8) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 48) + 8) = 0;
    *(unsigned __int64 *)(result) = 0;
loc_003B3401:
    result = MiUnlockControlAreaFileObjectExclusive(result, *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 48), a3, a4);
    v_rbx = (unsigned __int8)(((unsigned int)(0xC000012DULL)) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_003B354B;
loc_003B341E:
    result = KeAbPostRelease(v_rip + 11021339, *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 48), a3, a4);
    if (((unsigned __int8)(v_rbx)) != 2) goto loc_003B344E;
    result = (unsigned int)(v_stack_m134) + 152;
    if ((*(unsigned __int64 *)((unsigned int)(v_stack_m134) + 152)) != ((unsigned int)(v_stack_m134) + 152)) {
        result = KiCheckForKernelApcDelivery(1, *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 48), a3, a4);
    }
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 56))))) != 0) goto loc_003B366B;
loc_003B345F:
    if (v_stack_m134 < 3) goto loc_003B3675;
    a2 = 0;
    if (v_stack_m110 == 0) goto loc_003B3494;
    a3 = 0;
loc_003B3485:
    a2 = (unsigned int)((a2) + (1));
    *(unsigned __int64 *)(v_stack_m128 + a3 * 8) = *(unsigned __int64 *)(v_rip - 3812354);
    if (((unsigned int)((unsigned int)(a2))) < v_stack_m110) goto loc_003B3485;
loc_003B3494:
    v_stack_m150 = (unsigned int)((unsigned int)(v_stack_m130));
    v_stack_m158 = *(unsigned __int64 *)(v_rsp - 120 + 144);
    result = MiAddMappedPtes(v_rip + 11029209, v_stack_m128, v_stack_m110, result);
    if (sign_flag) goto loc_003B34E9;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 120 + 168)) = result;
loc_003B34D2:
    v_rsp = (v_rsp) + (312);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_003B34E9:
    a2 = 0;
    result = MiRemoveFromSystemSpace(result, a2, v_stack_m110, result);
    goto loc_003B34D2;
loc_003B34FB:
loc_003B3500:
loc_003B3505:
    if (v_stack_p50 != 0) goto loc_003B35BA;
loc_003B3519:
    if ((*(unsigned __int8 *)(v_rsp - 120 + 128)) != 0) goto loc_003B35E0;
loc_003B3526:
    if (v_stack_p40 != 0) goto loc_003B3604;
loc_003B3531:
    if (0 != 0) goto loc_003B3615;
loc_003B353A:
    if (1 == 0) goto loc_003B34D2;
    a2 = 0;
    result = ExFreePoolWithTag(1, a2, v_stack_m110, result);
    goto loc_003B34D2;
loc_003B354B:
    result = ExfTryToWakePushLock(v_rip + 11021038, a2, v_stack_m110, result);
    goto loc_003B341E;
loc_003B355C:
    a3 = 0;
    goto loc_003B325D;
loc_003B3564:
    goto loc_003B3505;
loc_003B356B:
    goto loc_003B3505;
loc_003B3572:
    goto loc_003B3505;
loc_003B357C:
    goto loc_003B3500;
loc_003B3586:
    goto loc_003B3123;
loc_003B358F:
    goto loc_003B313D;
loc_003B3597:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_p48 = (unsigned int)(result);
    result = MiCreatePerSessionProtos(result, (unsigned int)((unsigned int)(result)), a3, result);
    goto loc_003B3500;
loc_003B35BA:
    a2 = (v_stack_p58) << (12);
    result = MiUnmapLargePages(result, a2, 8, result);
    goto loc_003B3519;
loc_003B35E0:
    a4 = 0;
    a4 = (((unsigned int)((unsigned int)(v_stack_m134))) < 3) ? 1 : 0;
    result = MiDereferenceDataSubsections(result, *(unsigned __int64 *)(v_rsp - 120 + 144), v_stack_p68, a4);
    goto loc_003B3526;
loc_003B3604:
    result = MiDereferencePerSessionProtos(result, (unsigned int)(v_stack_p48), v_stack_p68, a4);
    goto loc_003B3531;
loc_003B3615:
    a3 = 0;
    result = MiReturnCommit(*(unsigned __int64 *)(v_rsp - 120 - 128), 0, a3, a4);
    goto loc_003B353A;
loc_003B3629:
    result = (result) >> (30);
    v_rbx = ((unsigned __int8)(result)) << (4);
    v_rbx = (v_rbx) + (v_rip + 11021382);
    result = ExAcquireSpinLockExclusive(v_rbx + 12, 0, a3, a4);
    a3 = 0;
loc_003B366B:
    goto loc_003B345F;
loc_003B3675:
    v_r12 = 0;
    result = MiGetAnyMultiplexedVm(v_r12 + 4, v_stack_p60, a3, 1);
    v_r14 = (*(unsigned __int64 *)(v_rip - 3807776 + (unsigned int)(v_stack_p44) * 8)) << (12);
}
```

## 5. (Beta) C Style

```c
int64_t MiInsertInSystemSpace(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint32_t v_stack_m134;
    uint8_t v_stack_m138;
    uint32_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint8_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (312);
    local_r12 = 0;
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x78 - 0x78) = 0;
    result = memset(local_rsp - 120 - 104, Arg2, 144, Arg4);
    *(uint8_t *)(local_rsp - 0x78 + 0x80) = 0;
    v_stack_m138 = 0;
    v_stack_m120 = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x78 + 0xA8)) = 0;
    v_stack_m110 = 0;
    *(uint64_t *)(local_rsp - 0x78 - 0x80) = 0;
    v_stack_m134 = (uint32_t)(0 + 3);
    v_stack_m130 = 0x7FFFFULL;
    result = MiSectionControlArea(0, Arg2, 144, Arg4);
    v_stack_m108 = (uint16_t)(Arg1);
    result = MiOffsetToProtos(result, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x78 + 0x90)), local_rsp - 120 - 120, Arg4);
    v_stack_m118 = result;
    if (result == 0) goto loc_003B3564;
    result = (uint32_t)((*(uint64_t *)(local_rsp - 0x78 + 0xA0)) & (8));
    *(uint64_t *)(local_rsp - 0x78 + 0xA0) = result;
    result = -(result);
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) + (2));
    v_stack_m100 = (uint32_t)(result);
    Arg2 = (((Arg1) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (Arg1) >> (12);
    Arg2 = (Arg2) + (result);
    result = 0;
    v_stack_m110 = Arg2;
    result = (v_stack_m108 != 0) ? 1 : 0;
    local_rbx = (Arg1) >> (16);
    result = (result) + (local_rbx);
    result = (result) << (4);
    v_stack_m120 = result;
    *(uint64_t *)(local_rsp - 0x78 - 0x80) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xA7D00D) + *(uint16_t *)(v_rip + 0xA85005) * 8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x38)))) & (32)) == 0) goto loc_003B32EF;
loc_003B308F:
    result = MiReservePtes(v_rip + 11021702, (uint32_t)(v_stack_m120), local_rsp - 120 - 120, Arg4);
    v_stack_m128 = result;
    if (result == 0) goto loc_003B3572;
    local_rsi = (result) << (25);
    result = (result) << (25);
    local_rsi = (local_rsi) - (result);
    local_rsi = (local_rsi) >> (16);
    v_stack_m108 = local_rsi;
loc_003B30D1:
    result = MiAllocatePool(104 - 40, 104, (uint32_t)(0x7756694DULL), Arg4);
    if (result == 0) goto loc_003B34FB;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(0 + 3))) & (3));
    Arg1 = (uint32_t)((Arg1) << (3));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x38))) & (0xFFFFFFE7ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    *(uint32_t *)(result + 0x38) = (uint32_t)(Arg1);
    result = MiControlAreaRequiresCharge(result, (uint32_t)(v_stack_m100), (uint32_t)(0x7756694DULL), Arg4);
    if ((uint32_t)(result) == 0) goto loc_003B357C;
    if (((uint32_t)(result)) == 2) goto loc_003B3586;
loc_003B3123:
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x78 + 0x88) + 0x38)) & (0x10000000ULL)) != 0) goto loc_003B358F;
loc_003B313D:
    if (((*(uint8_t *)(local_rsp - 0x78 + 0x98)) & (1)) != 0) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x38)))) & (32)) != 0) goto loc_003B3379;
loc_003B3155:
    result = (v_stack_m110) << (12);
    *(uint64_t *)(result + 0x20) = result;
    *(uint64_t *)(result + 0x30) = v_stack_m118;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x78 + 0x90))) >> (12);
    *(uint64_t *)(result + 0x18) = result;
    result = (local_rsi) | (2);
    *(uint64_t *)(result + 0x28) = 0;
    *(uint64_t *)(result + 0x58) = result;
    *(uint32_t *)(result + 0x60) = (uint32_t)((uint32_t)(v_stack_m130));
    result = MiReferenceFileObjectForMap(*(uint64_t *)(local_rsp - 0x78 + 0x88), (uint32_t)(v_stack_m100), (uint32_t)(0x7756694DULL), Arg4);
    *(uint64_t *)(result + 0x40) = result;
    if (v_stack_m134 == 0) goto loc_003B3629;
    local_rbx = ((uint32_t)((uint32_t)(result))) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 11021954, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 11021954;
        Arg2 = result;
        Arg1 = v_rip + 11021954;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = MiLockWorkingSetExclusive(v_rip + 11029888, Arg2, Arg3, Arg4);
    Arg3 = 0;
    if (*(uint64_t *)(v_rip + 0xA82E3C) == 0) goto loc_003B325D;
loc_003B3224:
    Arg3 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA82E3C) + 0x58)) & (0xFFFFFFFFFFFFF000ULL);
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA82E3C) + 0x20)) + (Arg3);
    if (local_rsi >= Arg3) goto loc_003B3251;
    if (local_rsi >= result) goto loc_003B3251;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA82E3C)) == 0) goto loc_003B355C;
loc_003B324C:
    goto loc_003B3224;
loc_003B3251:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA82E3C)) + 0x8) != 0) goto loc_003B324C;
loc_003B325D:
    result = RtlAvlInsertNodeEx(v_rip + 11021793, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA82E3C)), 1, result);
    result = MiUnlockWorkingSetExclusive(v_rip + 11029770, (uint8_t)((uint8_t)(result)), 1, result);
    *(uint64_t *)(local_rsp - 0x78 - 0x70) = result;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 104, Arg2, Arg3, result);
    result = result + 104;
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 104;
        Arg2 = result;
        Arg1 = result + 104;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, result);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (((*(uint32_t *)(result + 0x38)) & (0x400ULL)) != 0) goto loc_003B3401;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8)) == (result + 8)) goto loc_003B33F3;
loc_003B32EF:
    result = MiReferenceDataSubsections(result, *(uint64_t *)(local_rsp - 0x78 + 0x90), *(uint64_t *)(result + 0x8), v_stack_m134);
    if (sign_flag) goto loc_003B3505;
    *(uint8_t *)(local_rsp - 0x78 + 0x80) = 1;
    if (((uint32_t)((uint32_t)(v_stack_m134))) >= 3) goto loc_003B308F;
    Arg4 = 0;
    result = MiGetPageTablesForLargeMap(v_stack_m120, Arg4 + 8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m134))), Arg4);
    v_stack_m108 = result;
    if (result == 0) goto loc_003B356B;
    local_rbx = (result) >> (9);
    local_rbx = (local_rbx) & (result);
    local_rbx = (local_rbx) + (result);
    v_stack_m128 = local_rbx;
    goto loc_003B30D1;
loc_003B3379:
    if (condition_is_below) goto loc_003B3597;
    if (*(uint64_t *)(*(uint64_t *)(result) + 0x30) != 0) goto loc_003B33D3;
loc_003B338F:
    if (((uint32_t)(local_rbx)) != 2) goto loc_003B3155;
    v_stack_m118 = result + 128;
    Arg2 = (uint32_t)((Arg4 + 8) & (256));
    Arg2 = (uint32_t)((Arg2) + (136));
    result = MiReferenceActiveSubsection(result + 128, Arg2, 17, Arg4);
    if (!sign_flag) goto loc_003B3155;
    goto loc_003B3500;
loc_003B33D3:
    Arg3 = 0;
    result = MiChargeCommit(*(uint64_t *)(local_rsp - 0x78 - 0x80), *(uint64_t *)(*(uint64_t *)(result) + 0x30), Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_003B338F;
    local_r15 = 0;
    goto loc_003B3500;
loc_003B33F3:
    *(uint64_t *)(local_r15) = *(uint64_t *)(*(uint64_t *)(result) + 0x30);
    *(uint64_t *)(local_r15 + 0x8) = result;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result) + 0x30) + 0x8) = 0;
    *(uint64_t *)(result) = 0;
loc_003B3401:
    result = MiUnlockControlAreaFileObjectExclusive(result, *(uint64_t *)(*(uint64_t *)(result) + 0x30), Arg3, Arg4);
    local_rbx = (uint8_t)(((uint32_t)(0xC000012DULL)) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_003B354B;
loc_003B341E:
    result = KeAbPostRelease(v_rip + 11021339, *(uint64_t *)(*(uint64_t *)(result) + 0x30), Arg3, Arg4);
    if (((uint8_t)(local_rbx)) != 2) goto loc_003B344E;
    result = (uint32_t)(v_stack_m134) + 152;
    if ((*(uint64_t *)((uint32_t)(v_stack_m134) + 0x98)) != ((uint32_t)(v_stack_m134) + 152)) {
        result = KiCheckForKernelApcDelivery(1, *(uint64_t *)(*(uint64_t *)(result) + 0x30), Arg3, Arg4);
    }
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x38))))) != 0) goto loc_003B366B;
loc_003B345F:
    if (v_stack_m134 < 3) goto loc_003B3675;
    Arg2 = 0;
    if (v_stack_m110 == 0) goto loc_003B3494;
    Arg3 = 0;
loc_003B3485:
    Arg2 = (uint32_t)((Arg2) + (1));
    *(uint64_t *)(v_stack_m128 + Arg3 * 8) = *(uint64_t *)(v_rip - 0x3A2C02);
    if (((uint32_t)((uint32_t)(Arg2))) < v_stack_m110) goto loc_003B3485;
loc_003B3494:
    v_stack_m150 = (uint32_t)((uint32_t)(v_stack_m130));
    v_stack_m158 = *(uint64_t *)(local_rsp - 0x78 + 0x90);
    result = MiAddMappedPtes(v_rip + 11029209, v_stack_m128, v_stack_m110, result);
    if (sign_flag) goto loc_003B34E9;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x78 + 0xA8)) = result;
loc_003B34D2:
    local_rsp = (local_rsp) + (312);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_003B34E9:
    Arg2 = 0;
    result = MiRemoveFromSystemSpace(result, Arg2, v_stack_m110, result);
    goto loc_003B34D2;
loc_003B34FB:
loc_003B3500:
loc_003B3505:
    if (v_stack_p50 != 0) goto loc_003B35BA;
loc_003B3519:
    if ((*(uint8_t *)(local_rsp - 0x78 + 0x80)) != 0) goto loc_003B35E0;
loc_003B3526:
    if (v_stack_p40 != 0) goto loc_003B3604;
loc_003B3531:
    if (0 != 0) goto loc_003B3615;
loc_003B353A:
    if (1 == 0) goto loc_003B34D2;
    Arg2 = 0;
    result = ExFreePoolWithTag(1, Arg2, v_stack_m110, result);
    goto loc_003B34D2;
loc_003B354B:
    result = ExfTryToWakePushLock(v_rip + 11021038, Arg2, v_stack_m110, result);
    goto loc_003B341E;
loc_003B355C:
    Arg3 = 0;
    goto loc_003B325D;
loc_003B3564:
    goto loc_003B3505;
loc_003B356B:
    goto loc_003B3505;
loc_003B3572:
    goto loc_003B3505;
loc_003B357C:
    goto loc_003B3500;
loc_003B3586:
    goto loc_003B3123;
loc_003B358F:
    goto loc_003B313D;
loc_003B3597:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_p48 = (uint32_t)(result);
    result = MiCreatePerSessionProtos(result, (uint32_t)((uint32_t)(result)), Arg3, result);
    goto loc_003B3500;
loc_003B35BA:
    Arg2 = (v_stack_p58) << (12);
    result = MiUnmapLargePages(result, Arg2, 8, result);
    goto loc_003B3519;
loc_003B35E0:
    Arg4 = 0;
    Arg4 = (((uint32_t)((uint32_t)(v_stack_m134))) < 3) ? 1 : 0;
    result = MiDereferenceDataSubsections(result, *(uint64_t *)(local_rsp - 0x78 + 0x90), v_stack_p68, Arg4);
    goto loc_003B3526;
loc_003B3604:
    result = MiDereferencePerSessionProtos(result, (uint32_t)(v_stack_p48), v_stack_p68, Arg4);
    goto loc_003B3531;
loc_003B3615:
    Arg3 = 0;
    result = MiReturnCommit(*(uint64_t *)(local_rsp - 0x78 - 0x80), 0, Arg3, Arg4);
    goto loc_003B353A;
loc_003B3629:
    result = (result) >> (30);
    local_rbx = ((uint8_t)(result)) << (4);
    local_rbx = (local_rbx) + (v_rip + 11021382);
    result = ExAcquireSpinLockExclusive(local_rbx + 12, 0, Arg3, Arg4);
    Arg3 = 0;
loc_003B366B:
    goto loc_003B345F;
loc_003B3675:
    local_r12 = 0;
    result = MiGetAnyMultiplexedVm(local_r12 + 4, v_stack_p60, Arg3, 1);
    local_r14 = (*(uint64_t *)(v_rip - 0x3A1A20 + (uint32_t)(v_stack_p44) * 8)) << (12);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003B2F5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
