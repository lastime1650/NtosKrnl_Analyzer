# CcSetDirtyInMask

- RVA: `0x003CB688`–`0x003CBBB2` (길이 `1,322` bytes)
- VA: `0x00000001403CB688`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008F818`
- 디코드: `318`개 명령, `1,322/1,322` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003CB755` → [CcGetPrivateVolumeCacheMap](../38/CcGetPrivateVolumeCacheMap_function_0038B930.md) (function, `0x0038B930`)
- `0x003CB790` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x003CB7CB` → [CcFindBitmapRangeToDirty](CcFindBitmapRangeToDirty_function_003CBBC0.md) (function, `0x003CBBC0`)
- `0x003CB80D` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CB88B` → [CcChargeDirtyPages](CcChargeDirtyPages_function_003CBEA0.md) (function, `0x003CBEA0`)
- `0x003CB894` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CB919` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x003CB92D` → [ExFreeToNPagedLookasideList](../38/ExFreeToNPagedLookasideList_function_0038D9D0.md) (function, `0x0038D9D0`)
- `0x003CB960` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003CBA10` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CBA4F` → [CcScheduleLazyWriteScan](CcScheduleLazyWriteScan_function_003CBD20.md) (function, `0x003CBD20`)
- `0x003CBA57` → [CcInsertIntoDirtySharedCacheMapList](CcInsertIntoDirtySharedCacheMapList_function_003CD9D8.md) (function, `0x003CD9D8`)
- `0x003CBA6C` → [ExAllocateFromNPagedLookasideList](../38/ExAllocateFromNPagedLookasideList_function_0038E6C0.md) (function, `0x0038E6C0`)
- `0x003CBAAD` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x003CBAF8` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003CBB24` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x003CBB2E` → [CcAllocateInitializeMbcb](../47/CcAllocateInitializeMbcb_function_0047E374.md) (function, `0x0047E374`)
- `0x003CBB90` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003CBBAC` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [CcFlushCachePostProcessOneRange](../35/CcFlushCachePostProcessOneRange_function_00359710.md) at `0x00359AC1`
- [CcReleaseByteRangeFromWrite](../35/CcReleaseByteRangeFromWrite_function_00359C90.md) at `0x00359D8A`
- [CcSetDirtyPinnedData](../35/CcSetDirtyPinnedData_function_0035A120.md) at `0x0035A3C2`
- [CcPurgeAndClearCacheSection](../38/CcPurgeAndClearCacheSection_function_0038A614.md) at `0x0038A75A`
- [CcMdlWriteComplete2](CcMdlWriteComplete2_function_003CA36C.md) at `0x003CA3F0`
- [CcMapAndCopyInToCache](CcMapAndCopyInToCache_function_003CA7F0.md) at `0x003CABFB`
- [CcMapAndCopyInToCache](CcMapAndCopyInToCache_function_003CA7F0.md) at `0x003CB3B0`
- [CcMapAndCopyInToCache$fin$1](../6D/CcMapAndCopyInToCache_fin_1_function_006D2AF9.md) at `0x006D2B8F`
- [CcPrepareMdlWrite$fin$0](../6D/CcPrepareMdlWrite_fin_0_function_006D3DF5.md) at `0x006D3EBA`

### Static image references
- `0x003CB926` → RVA `0x00E11A00` (`.data`; read)
- `0x003CBB66` → RVA `0x00F8F5F8` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x003CBA1F` → [sub_006E85B0](../6E/Unknown_function_006E85B0.md) (`tail-transfer`)
  - `0x003CBA2F` → [sub_006E85B0](../6E/Unknown_function_006E85B0.md) (`tail-transfer`)
  - `0x003CBB39` → [sub_006E85B0 + 0x28](../6E/Unknown_function_006E85B0.md) (`tail-transfer`)
  - `0x003CBB6C` → [sub_006E85B0 + 0x28](../6E/Unknown_function_006E85B0.md) (`tail-transfer`)
  - `0x003CBB75` → [sub_006E85B0 + 0x28](../6E/Unknown_function_006E85B0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003CB688  48 8B C4                        mov rax, rsp
003CB68B  48 89 58 08                     mov qword ptr [rax + 8], rbx
003CB68F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
003CB693  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
003CB697  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
003CB69B  55                              push rbp
003CB69C  56                              push rsi
003CB69D  57                              push rdi
003CB69E  41 54                           push r12
003CB6A0  41 55                           push r13
003CB6A2  41 56                           push r14
003CB6A4  41 57                           push r15
003CB6A6  48 8B EC                        mov rbp, rsp
003CB6A9  48 83 EC 70                     sub rsp, 0x70
003CB6AD  48 8B 02                        mov rax, qword ptr [rdx]
003CB6B0  48 8B D9                        mov rbx, rcx
003CB6B3  48 83 65 C8 00                  and qword ptr [rbp - 0x38], 0
003CB6B8  33 C9                           xor ecx, ecx
003CB6BA  83 65 C0 00                     and dword ptr [rbp - 0x40], 0
003CB6BE  45 33 C9                        xor r9d, r9d
003CB6C1  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
003CB6C5  0F 57 C0                        xorps xmm0, xmm0
003CB6C8  48 8D 48 FF                     lea rcx, [rax - 1]
003CB6CC  45 8B D0                        mov r10d, r8d
003CB6CF  49 03 CA                        add rcx, r10
003CB6D2  44 89 4D C4                     mov dword ptr [rbp - 0x3c], r9d
003CB6D6  48 33 C8                        xor rcx, rax
003CB6D9  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
003CB6DD  48 F7 C1 00 00 00 FE            test rcx, -0x2000000
003CB6E4  0F 85 AC 04 00 00               jne 0x1403cbb96
003CB6EA  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
003CB6F3  48 8B 88 C0 00 00 00            mov rcx, qword ptr [rax + 0xc0]
003CB6FA  0F B7 81 8A 00 00 00            movzx eax, word ptr [rcx + 0x8a]
003CB701  89 83 2C 02 00 00               mov dword ptr [rbx + 0x22c], eax
003CB707  44 8B 83 98 00 00 00            mov r8d, dword ptr [rbx + 0x98]
003CB70E  41 81 E0 00 00 00 40            and r8d, 0x40000000
003CB715  0F 85 E7 03 00 00               jne 0x1403cbb02
003CB71B  48 8B 02                        mov rax, qword ptr [rdx]
003CB71E  B9 00 10 00 00                  mov ecx, 0x1000
003CB723  4C 8B F8                        mov r15, rax
003CB726  49 C1 FF 0C                     sar r15, 0xc
003CB72A  4C 8D 60 FF                     lea r12, [rax - 1]
003CB72E  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
003CB732  48 99                           cqo
003CB734  4D 03 E2                        add r12, r10
003CB737  48 F7 F9                        idiv rcx
003CB73A  49 C1 FC 0C                     sar r12, 0xc
003CB73E  49 3B C4                        cmp rax, r12
003CB741  0F 8E 33 04 00 00               jle 0x1403cbb7a
003CB747  4C 8B AB 18 02 00 00            mov r13, qword ptr [rbx + 0x218]
003CB74E  48 8B CB                        mov rcx, rbx
003CB751  4C 89 6D D8                     mov qword ptr [rbp - 0x28], r13
003CB755  E8 D6 01 FC FF                  call 0x14038b930
003CB75A  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
003CB75E  48 8B F8                        mov rdi, rax
003CB761  45 85 C0                        test r8d, r8d
003CB764  0F 85 AD 03 00 00               jne 0x1403cbb17
003CB76A  48 8B 7D C8                     mov rdi, qword ptr [rbp - 0x38]
003CB76E  41 BE F9 02 00 00               mov r14d, 0x2f9
003CB774  48 81 7B 20 00 00 30 00         cmp qword ptr [rbx + 0x20], 0x300000
003CB77C  0F 87 E3 02 00 00               ja 0x1403cba65
003CB782  48 8D 8B 20 01 00 00            lea rcx, [rbx + 0x120]
003CB789  C7 45 C0 01 00 00 00            mov dword ptr [rbp - 0x40], 1
003CB790  E8 0B 2E E4 FF                  call 0x14020e5a0
003CB795  48 8B B3 A8 00 00 00            mov rsi, qword ptr [rbx + 0xa8]
003CB79C  48 85 F6                        test rsi, rsi
003CB79F  0F 84 89 03 00 00               je 0x1403cbb2e
003CB7A5  4D 3B FC                        cmp r15, r12
003CB7A8  75 0A                           jne 0x1403cb7b4
003CB7AA  4C 3B 7E 28                     cmp r15, qword ptr [rsi + 0x28]
003CB7AE  0F 84 3B 01 00 00               je 0x1403cb8ef
003CB7B4  49 81 FC 00 03 00 00            cmp r12, 0x300
003CB7BB  0F 83 8A 01 00 00               jae 0x1403cb94b
003CB7C1  4C 8D 45 C8                     lea r8, [rbp - 0x38]
003CB7C5  49 8B D7                        mov rdx, r15
003CB7C8  48 8B CE                        mov rcx, rsi
003CB7CB  E8 F0 03 00 00                  call 0x1403cbbc0
003CB7D0  4C 8B F0                        mov r14, rax
003CB7D3  48 85 C0                        test rax, rax
003CB7D6  0F 84 95 03 00 00               je 0x1403cbb71
003CB7DC  4C 8B 40 10                     mov r8, qword ptr [rax + 0x10]
003CB7E0  8B 48 18                        mov ecx, dword ptr [rax + 0x18]
003CB7E3  41 8B D0                        mov edx, r8d
003CB7E6  49 03 C8                        add rcx, r8
003CB7E9  4C 3B F9                        cmp r15, rcx
003CB7EC  0F 8C E3 01 00 00               jl 0x1403cb9d5
003CB7F2  41 8B 46 1C                     mov eax, dword ptr [r14 + 0x1c]
003CB7F6  49 03 C0                        add rax, r8
003CB7F9  4C 3B E0                        cmp r12, rax
003CB7FC  0F 8F E1 01 00 00               jg 0x1403cb9e3
003CB802  49 8D 8D 00 03 00 00            lea rcx, [r13 + 0x300]
003CB809  48 8D 55 E0                     lea rdx, [rbp - 0x20]
003CB80D  E8 8E 9F EA FF                  call 0x1402757a0
003CB812  83 7B 70 00                     cmp dword ptr [rbx + 0x70], 0
003CB816  0F 84 18 02 00 00               je 0x1403cba34
003CB81C  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
003CB820  41 8B CF                        mov ecx, r15d
003CB823  41 2B 4E 10                     sub ecx, dword ptr [r14 + 0x10]
003CB827  BF 01 00 00 00                  mov edi, 1
003CB82C  48 C1 E9 05                     shr rcx, 5
003CB830  48 8D 14 88                     lea rdx, [rax + rcx*4]
003CB834  41 8B CF                        mov ecx, r15d
003CB837  83 E1 1F                        and ecx, 0x1f
003CB83A  D3 E7                           shl edi, cl
003CB83C  4D 3B FC                        cmp r15, r12
003CB83F  7F 3D                           jg 0x1403cb87e
003CB841  44 8B 6D C4                     mov r13d, dword ptr [rbp - 0x3c]
003CB845  49 8B C4                        mov rax, r12
003CB848  49 2B C7                        sub rax, r15
003CB84B  48 FF C0                        inc rax
003CB84E  4C 03 F8                        add r15, rax
003CB851  8B 0A                           mov ecx, dword ptr [rdx]
003CB853  85 CF                           test edi, ecx
003CB855  0F 84 6E 01 00 00               je 0x1403cb9c9
003CB85B  8D 0C 3F                        lea ecx, [rdi + rdi]
003CB85E  85 C9                           test ecx, ecx
003CB860  0F 84 E5 02 00 00               je 0x1403cbb4b
003CB866  85 C9                           test ecx, ecx
003CB868  BF 01 00 00 00                  mov edi, 1
003CB86D  0F 45 F9                        cmovne edi, ecx
003CB870  48 83 E8 01                     sub rax, 1
003CB874  75 DB                           jne 0x1403cb851
003CB876  44 89 6D C4                     mov dword ptr [rbp - 0x3c], r13d
003CB87A  4C 8B 6D D8                     mov r13, qword ptr [rbp - 0x28]
003CB87E  44 8B 4D C4                     mov r9d, dword ptr [rbp - 0x3c]
003CB882  4D 8B C6                        mov r8, r14
003CB885  48 8B D6                        mov rdx, rsi
003CB888  48 8B CB                        mov rcx, rbx
003CB88B  E8 10 06 00 00                  call 0x1403cbea0
003CB890  48 8D 4D E0                     lea rcx, [rbp - 0x20]
003CB894  E8 47 74 F7 FF                  call 0x140342ce0
003CB899  F7 83 98 00 00 00 00 00 00 10   test dword ptr [rbx + 0x98], 0x10000000
003CB8A3  74 3E                           je 0x1403cb8e3
003CB8A5  44 8B 4D C4                     mov r9d, dword ptr [rbp - 0x3c]
003CB8A9  45 85 C9                        test r9d, r9d
003CB8AC  74 35                           je 0x1403cb8e3
003CB8AE  4C 8B 5D 58                     mov r11, qword ptr [rbp + 0x58]
003CB8B2  4D 85 DB                        test r11, r11
003CB8B5  0F 84 99 02 00 00               je 0x1403cbb54
003CB8BB  49 8B 83 20 02 00 00            mov rax, qword ptr [r11 + 0x220]
003CB8C2  41 8B D1                        mov edx, r9d
003CB8C5  C1 E2 0C                        shl edx, 0xc
003CB8C8  48 8B 88 38 06 00 00            mov rcx, qword ptr [rax + 0x638]
003CB8CF  48 85 C9                        test rcx, rcx
003CB8D2  74 0F                           je 0x1403cb8e3
003CB8D4  48 85 D2                        test rdx, rdx
003CB8D7  74 05                           je 0x1403cb8de
003CB8D9  F0 48 01 51 08                  lock add qword ptr [rcx + 8], rdx
003CB8DE  F0 48 FF 41 18                  lock inc qword ptr [rcx + 0x18]
003CB8E3  85 FF                           test edi, edi
003CB8E5  0F 84 7F FE FF FF               je 0x1403cb76a
003CB8EB  4C 89 66 28                     mov qword ptr [rsi + 0x28], r12
003CB8EF  48 8B 7D D0                     mov rdi, qword ptr [rbp - 0x30]
003CB8F3  44 8B 75 C0                     mov r14d, dword ptr [rbp - 0x40]
003CB8F7  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
003CB8FB  8B 4D 50                        mov ecx, dword ptr [rbp + 0x50]
003CB8FE  48 03 08                        add rcx, qword ptr [rax]
003CB901  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
003CB905  48 3B C8                        cmp rcx, rax
003CB908  0F 8F E3 00 00 00               jg 0x1403cb9f1
003CB90E  48 8B 7D C8                     mov rdi, qword ptr [rbp - 0x38]
003CB912  48 8D 8B 20 01 00 00            lea rcx, [rbx + 0x120]
003CB919  E8 A2 60 E8 FF                  call 0x1402519c0
003CB91E  48 85 FF                        test rdi, rdi
003CB921  74 0F                           je 0x1403cb932
003CB923  48 8B D7                        mov rdx, rdi
003CB926  48 8D 0D D3 60 A4 00            lea rcx, [rip + 0xa460d3]
003CB92D  E8 9E 20 FC FF                  call 0x14038d9d0
003CB932  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
003CB93A  48 83 C4 70                     add rsp, 0x70
003CB93E  41 5F                           pop r15
003CB940  41 5E                           pop r14
003CB942  41 5D                           pop r13
003CB944  41 5C                           pop r12
003CB946  5F                              pop rdi
003CB947  5E                              pop rsi
003CB948  5D                              pop rbp
003CB949  C3                              ret
003CB94A  CC                              int3
003CB94B  66 44 39 36                     cmp word ptr [rsi], r14w
003CB94F  0F 84 6C FE FF FF               je 0x1403cb7c1
003CB955  33 D2                           xor edx, edx
003CB957  41 B8 00 04 00 00               mov r8d, 0x400
003CB95D  48 8B CF                        mov rcx, rdi
003CB960  E8 DB B2 2F 00                  call 0x1406c6c40
003CB965  83 7E 50 00                     cmp dword ptr [rsi + 0x50], 0
003CB969  0F 85 4D 01 00 00               jne 0x1403cbabc
003CB96F  48 89 7E 58                     mov qword ptr [rsi + 0x58], rdi
003CB973  48 8D 46 10                     lea rax, [rsi + 0x10]
003CB977  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
003CB97B  48 8D 4E 60                     lea rcx, [rsi + 0x60]
003CB97F  33 FF                           xor edi, edi
003CB981  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
003CB985  48 39 02                        cmp qword ptr [rdx], rax
003CB988  75 38                           jne 0x1403cb9c2
003CB98A  48 89 01                        mov qword ptr [rcx], rax
003CB98D  41 83 C8 FF                     or r8d, 0xffffffff
003CB991  48 89 51 08                     mov qword ptr [rcx + 8], rdx
003CB995  49 B9 FF FF FF FF FF FF FF 7F   movabs r9, 0x7fffffffffffffff
003CB99F  48 89 0A                        mov qword ptr [rdx], rcx
003CB9A2  48 89 48 08                     mov qword ptr [rax + 8], rcx
003CB9A6  48 8D 8E 90 00 00 00            lea rcx, [rsi + 0x90]
003CB9AD  4C 89 4E 70                     mov qword ptr [rsi + 0x70], r9
003CB9B1  44 89 46 78                     mov dword ptr [rsi + 0x78], r8d
003CB9B5  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
003CB9B9  48 39 02                        cmp qword ptr [rdx], rax
003CB9BC  0F 84 C4 00 00 00               je 0x1403cba86
003CB9C2  B9 03 00 00 00                  mov ecx, 3
003CB9C7  CD 29                           int 0x29
003CB9C9  0B CF                           or ecx, edi
003CB9CB  89 0A                           mov dword ptr [rdx], ecx
003CB9CD  41 FF C5                        inc r13d
003CB9D0  E9 86 FE FF FF                  jmp 0x1403cb85b
003CB9D5  41 8B C7                        mov eax, r15d
003CB9D8  2B C2                           sub eax, edx
003CB9DA  41 89 46 18                     mov dword ptr [r14 + 0x18], eax
003CB9DE  E9 0F FE FF FF                  jmp 0x1403cb7f2
003CB9E3  41 8B C4                        mov eax, r12d
003CB9E6  2B C2                           sub eax, edx
003CB9E8  41 89 46 1C                     mov dword ptr [r14 + 0x1c], eax
003CB9EC  E9 11 FE FF FF                  jmp 0x1403cb802
003CB9F1  48 89 4B 30                     mov qword ptr [rbx + 0x30], rcx
003CB9F5  F7 83 98 00 00 00 00 00 00 40   test dword ptr [rbx + 0x98], 0x40000000
003CB9FF  0F 84 09 FF FF FF               je 0x1403cb90e
003CBA05  49 8D 8D 00 03 00 00            lea rcx, [r13 + 0x300]
003CBA0C  48 8D 55 E0                     lea rdx, [rbp - 0x20]
003CBA10  E8 8B 9D EA FF                  call 0x1402757a0
003CBA15  8B 83 98 00 00 00               mov eax, dword ptr [rbx + 0x98]
003CBA1B  0F BA E0 0A                     bt eax, 0xa
003CBA1F  0F 82 8B CB 31 00               jb 0x1406e85b0
003CBA25  0F BA E8 0A                     bts eax, 0xa
003CBA29  89 83 98 00 00 00               mov dword ptr [rbx + 0x98], eax
003CBA2F  E9 7C CB 31 00                  jmp 0x1406e85b0
003CBA34  8B 83 98 00 00 00               mov eax, dword ptr [rbx + 0x98]
003CBA3A  A8 02                           test al, 2
003CBA3C  0F 85 DA FD FF FF               jne 0x1403cb81c
003CBA42  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
003CBA46  45 33 C9                        xor r9d, r9d
003CBA49  45 33 C0                        xor r8d, r8d
003CBA4C  49 8B CD                        mov rcx, r13
003CBA4F  E8 CC 02 00 00                  call 0x1403cbd20
003CBA54  48 8B CB                        mov rcx, rbx
003CBA57  E8 7C 1F 00 00                  call 0x1403cd9d8
003CBA5C  4C 89 7E 20                     mov qword ptr [rsi + 0x20], r15
003CBA60  E9 B7 FD FF FF                  jmp 0x1403cb81c
003CBA65  48 8D 0D 94 5F A4 00            lea rcx, [rip + 0xa45f94]
003CBA6C  E8 4F 2C FC FF                  call 0x14038e6c0
003CBA71  48 85 C0                        test rax, rax
003CBA74  0F 84 EC 00 00 00               je 0x1403cbb66
003CBA7A  48 8B F8                        mov rdi, rax
003CBA7D  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
003CBA81  E9 FC FC FF FF                  jmp 0x1403cb782
003CBA86  48 89 01                        mov qword ptr [rcx], rax
003CBA89  48 89 51 08                     mov qword ptr [rcx + 8], rdx
003CBA8D  48 89 0A                        mov qword ptr [rdx], rcx
003CBA90  48 89 48 08                     mov qword ptr [rax + 8], rcx
003CBA94  48 8D 8B 20 01 00 00            lea rcx, [rbx + 0x120]
003CBA9B  4C 89 8E A0 00 00 00            mov qword ptr [rsi + 0xa0], r9
003CBAA2  44 89 86 A8 00 00 00            mov dword ptr [rsi + 0xa8], r8d
003CBAA9  66 44 89 36                     mov word ptr [rsi], r14w
003CBAAD  E8 0E 5F E8 FF                  call 0x1402519c0
003CBAB2  33 C0                           xor eax, eax
003CBAB4  89 45 C0                        mov dword ptr [rbp - 0x40], eax
003CBAB7  E9 B8 FC FF FF                  jmp 0x1403cb774
003CBABC  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
003CBAC0  33 D2                           xor edx, edx
003CBAC2  0F 10 00                        movups xmm0, xmmword ptr [rax]
003CBAC5  44 8D 42 60                     lea r8d, [rdx + 0x60]
003CBAC9  0F 11 07                        movups xmmword ptr [rdi], xmm0
003CBACC  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
003CBAD0  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
003CBAD4  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
003CBAD8  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
003CBADC  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
003CBAE0  0F 11 4F 30                     movups xmmword ptr [rdi + 0x30], xmm1
003CBAE4  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
003CBAE8  0F 11 47 40                     movups xmmword ptr [rdi + 0x40], xmm0
003CBAEC  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
003CBAF0  0F 11 4F 50                     movups xmmword ptr [rdi + 0x50], xmm1
003CBAF4  48 8B 4E 58                     mov rcx, qword ptr [rsi + 0x58]
003CBAF8  E8 43 B1 2F 00                  call 0x1406c6c40
003CBAFD  E9 6D FE FF FF                  jmp 0x1403cb96f
003CBB02  48 8B 0A                        mov rcx, qword ptr [rdx]
003CBB05  49 03 CA                        add rcx, r10
003CBB08  48 3B 4B 30                     cmp rcx, qword ptr [rbx + 0x30]
003CBB0C  0F 8E 20 FE FF FF               jle 0x1403cb932
003CBB12  E9 04 FC FF FF                  jmp 0x1403cb71b
003CBB17  48 8D 8B 20 01 00 00            lea rcx, [rbx + 0x120]
003CBB1E  41 BE 01 00 00 00               mov r14d, 1
003CBB24  E8 77 2A E4 FF                  call 0x14020e5a0
003CBB29  E9 C9 FD FF FF                  jmp 0x1403cb8f7
003CBB2E  E8 41 28 0B 00                  call 0x14047e374
003CBB33  48 8B F0                        mov rsi, rax
003CBB36  48 85 C0                        test rax, rax
003CBB39  0F 84 99 CA 31 00               je 0x1406e85d8
003CBB3F  48 89 83 A8 00 00 00            mov qword ptr [rbx + 0xa8], rax
003CBB46  E9 5A FC FF FF                  jmp 0x1403cb7a5
003CBB4B  48 83 C2 04                     add rdx, 4
003CBB4F  E9 12 FD FF FF                  jmp 0x1403cb866
003CBB54  65 4C 8B 1C 25 88 01 00 00      mov r11, qword ptr gs:[0x188]
003CBB5D  4C 89 5D 58                     mov qword ptr [rbp + 0x58], r11
003CBB61  E9 55 FD FF FF                  jmp 0x1403cb8bb
003CBB66  FF 05 8C 3A BC 00               inc dword ptr [rip + 0xbc3a8c]
003CBB6C  E9 67 CA 31 00                  jmp 0x1406e85d8
003CBB71  48 8B 7D C8                     mov rdi, qword ptr [rbp - 0x38]
003CBB75  E9 5E CA 31 00                  jmp 0x1406e85d8
003CBB7A  4C 21 4C 24 20                  and qword ptr [rsp + 0x20], r9
003CBB7F  BA 13 0D 00 00                  mov edx, 0xd13
003CBB84  B9 34 00 00 00                  mov ecx, 0x34
003CBB89  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
003CBB90  E8 CB 1A 13 00                  call 0x1404fd660
003CBB95  CC                              int3
003CBB96  4C 21 4C 24 20                  and qword ptr [rsp + 0x20], r9
003CBB9B  BA EA 0C 00 00                  mov edx, 0xcea
003CBBA0  B9 34 00 00 00                  mov ecx, 0x34
003CBBA5  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
003CBBAC  E8 AF 1A 13 00                  call 0x1404fd660
003CBBB1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcSetDirtyInMask(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (112);
    a1 = 0;
    a4 = 0;
    v_stack_m48 = 0;
    a1 = (*(unsigned __int64 *)(a2) - 1) + ((unsigned int)(a3));
    v_stack_m74 = 0;
    a1 = (a1) ^ (*(unsigned __int64 *)(a2));
    v_stack_m58 = v_xmm0;
    if (((a1) & (0xFFFFFFFFFE000000ULL)) != 0) goto loc_003CBB96;
    *(unsigned int *)(a1 + 556) = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 192) + 138));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 152))) & (0x40000000ULL));
    if (condition_is_not_equal) goto loc_003CBB02;
loc_003CB71B:
    v_r15 = (*(unsigned __int64 *)(a2)) >> (12);
    v_r12 = (*(unsigned __int64 *)(a2) - 1) + ((unsigned int)(a3));
    v_r12 = (v_r12) >> (12);
    if ((*(unsigned __int64 *)(a1 + 32)) <= v_r12) goto loc_003CBB7A;
    v_stack_m60 = *(unsigned __int64 *)(a1 + 536);
    result = CcGetPrivateVolumeCacheMap(a1, a2, a3, a4);
    v_stack_m68 = result;
    if (a3 != 0) goto loc_003CBB17;
loc_003CB76A:
loc_003CB774:
    if ((*(unsigned __int64 *)(a1 + 32)) > 0x300000ULL) goto loc_003CBA65;
loc_003CB782:
    v_stack_m78 = 1;
    result = ExAcquireFastMutex(a1 + 288, a2, a3, a4);
    if (*(unsigned __int64 *)(a1 + 168) == 0) goto loc_003CBB2E;
loc_003CB7A5:
    if (v_r15 != v_r12) goto loc_003CB7B4;
    if (v_r15 == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 40))) goto loc_003CB8EF;
loc_003CB7B4:
    if (v_r12 >= 768) goto loc_003CB94B;
loc_003CB7C1:
    result = CcFindBitmapRangeToDirty(*(unsigned __int64 *)(a1 + 168), v_r15, v_stack_m70, a4);
    if (result == 0) goto loc_003CBB71;
    a1 = ((unsigned int)(*(unsigned int *)(result + 24))) + (*(unsigned __int64 *)(result + 16));
    if (v_r15 < a1) goto loc_003CB9D5;
loc_003CB7F2:
    result = ((unsigned int)(*(unsigned int *)(result + 28))) + (*(unsigned __int64 *)(result + 16));
    if (v_r12 > result) goto loc_003CB9E3;
loc_003CB802:
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(a1 + 536) + 768, v_stack_m58, *(unsigned __int64 *)(result + 16), a4);
    if ((*(unsigned int *)(a1 + 112)) == 0) goto loc_003CBA34;
loc_003CB81C:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) - (*(unsigned int *)(result + 16)));
    a1 = (a1) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (31));
    v_rdi = (unsigned int)((1) << ((unsigned __int8)(a1)));
    if (v_r15 > v_r12) goto loc_003CB87E;
    result = (v_r12) - (v_r15);
    result = (result) + 1;
    v_r15 = (v_r15) + (result);
loc_003CB851:
    if ((((unsigned int)(v_rdi)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 40) + a1 * 4))))) == 0) goto loc_003CB9C9;
loc_003CB85B:
    if ((unsigned int)(v_rdi + v_rdi * 1) == 0) goto loc_003CBB4B;
loc_003CB866:
    v_rdi = 1;
    if ((unsigned int)(v_rdi + v_rdi * 1) != 0) { v_rdi = (unsigned int)(v_rdi + v_rdi * 1); }
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_003CB851;
    v_stack_m74 = (unsigned int)((unsigned int)(v_stack_m74));
loc_003CB87E:
    result = CcChargeDirtyPages(a1, *(unsigned __int64 *)(a1 + 168), result, (unsigned int)(v_stack_m74));
    result = KeReleaseInStackQueuedSpinLock(v_stack_m58, *(unsigned __int64 *)(a1 + 168), result, (unsigned int)(v_stack_m74));
    if (((*(unsigned int *)(a1 + 152)) & (0x10000000ULL)) == 0) goto loc_003CB8E3;
    if ((unsigned int)((unsigned int)(v_stack_m74)) == 0) goto loc_003CB8E3;
    if (v_stack_p20 == 0) goto loc_003CBB54;
loc_003CB8BB:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m74)))) << (12));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 544) + 1592) == 0) goto loc_003CB8E3;
    if (a2 != 0) {
    }
loc_003CB8E3:
    if ((unsigned int)(v_rdi) == 0) goto loc_003CB76A;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 40) = v_r12;
loc_003CB8EF:
loc_003CB8F7:
    a1 = ((unsigned int)(v_stack_p18)) + (*(unsigned __int64 *)(v_stack_p10));
    if (a1 > (*(unsigned __int64 *)(a1 + 48))) goto loc_003CB9F1;
loc_003CB90E:
    result = ExReleaseFastMutex(a1 + 288, a2, result, (unsigned int)(v_stack_m74));
    if (v_stack_m70 != 0) {
        a2 = v_stack_m70;
        a1 = v_rip + 10772691;
        result = ExFreeToNPagedLookasideList(a1, a2, result, (unsigned int)(v_stack_m74));
    }
    v_rsp = (v_rsp) + (112);
    return result;
loc_003CB94B:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 168))) == ((unsigned __int16)((unsigned int)(v_stack_m78)))) goto loc_003CB7C1;
    a2 = 0;
    result = memset(v_stack_m70, a2, (unsigned int)(0x400ULL), (unsigned int)(v_stack_m74));
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 168) + 80)) != 0) goto loc_003CBABC;
loc_003CB96F:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 88) = v_stack_m70;
    v_rdi = 0;
    v_stack_m70 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 16 + 8))) != (*(unsigned __int64 *)(a1 + 168) + 16)) goto loc_003CB9C2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 96) = *(unsigned __int64 *)(a1 + 168) + 16;
    a3 = (unsigned int)(((unsigned int)(0x400ULL)) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 96 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 16 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 16 + 8)) = *(unsigned __int64 *)(a1 + 168) + 96;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 16 + 8) = *(unsigned __int64 *)(a1 + 168) + 96;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 112) = (unsigned int)(v_stack_m74);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 168) + 120) = a3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 16 + 8))) == (*(unsigned __int64 *)(a1 + 168) + 16)) goto loc_003CBA86;
loc_003CB9C2:
loc_003CB9C9:
    a1 = (unsigned int)((3) | (0));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 16 + 8)) = (unsigned int)(a1);
    v_r13 = (unsigned int)((v_stack_m60) + 1);
    goto loc_003CB85B;
loc_003CB9D5:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) - ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 16 + 8))));
    *(unsigned int *)((unsigned int)(v_stack_m78) + 24) = (unsigned int)(result);
    goto loc_003CB7F2;
loc_003CB9E3:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 16 + 8))));
    *(unsigned int *)((unsigned int)(v_stack_m78) + 28) = (unsigned int)(result);
    goto loc_003CB802;
loc_003CB9F1:
    *(unsigned __int64 *)(v_stack_p8 + 48) = a1;
    if (((*(unsigned int *)(v_stack_p8 + 152)) & (0x40000000ULL)) == 0) goto loc_003CB90E;
    result = KeAcquireInStackQueuedSpinLock(v_r13 + 768, v_stack_m58, a3, (unsigned int)(v_stack_m74));
    *(unsigned int *)(v_stack_p8 + 152) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 152)));
loc_003CBA34:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 152)))) & (2)) != 0) goto loc_003CB81C;
    a4 = 0;
    a3 = 0;
    result = CcScheduleLazyWriteScan(v_r13, v_stack_m68, a3, a4);
    result = CcInsertIntoDirtySharedCacheMapList(v_stack_p8, v_stack_m68, a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 32) = v_r15;
    goto loc_003CB81C;
loc_003CBA65:
    result = ExAllocateFromNPagedLookasideList(v_rip + 10772372, v_stack_m68, a3, a4);
    if (result == 0) goto loc_003CBB66;
    v_stack_m70 = result;
    goto loc_003CB782;
loc_003CBA86:
    *(unsigned __int64 *)(v_rip + 10772372) = result;
    *(unsigned __int64 *)(v_rip + 10772372 + 8) = v_stack_m68;
    *(unsigned __int64 *)(v_stack_m68) = v_rip + 10772372;
    *(unsigned __int64 *)(result + 8) = v_rip + 10772372;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 160) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 168) + 168) = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 168)) = (unsigned __int16)((unsigned int)(v_stack_m78));
    result = ExReleaseFastMutex(v_stack_p8 + 288, v_stack_m68, a3, a4);
    result = 0;
    v_stack_m78 = 0;
    goto loc_003CB774;
loc_003CBABC:
    a2 = 0;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 64) = v_xmm0;
    *(unsigned __int64 *)(result + 80) = v_xmm1;
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 88), a2, a2 + 96, a4);
    goto loc_003CB96F;
loc_003CBB02:
    a1 = (*(unsigned __int64 *)(a2)) + ((unsigned int)(a3));
    if (a1 <= (*(unsigned __int64 *)(v_stack_p8 + 48))) goto loc_003CB932;
    goto loc_003CB71B;
loc_003CBB17:
    result = ExAcquireFastMutex(v_stack_p8 + 288, a2, a2 + 96, a4);
    goto loc_003CB8F7;
loc_003CBB2E:
    result = CcAllocateInitializeMbcb(v_stack_p8 + 288, a2, a2 + 96, a4);
    *(unsigned __int64 *)(v_stack_p8 + 168) = result;
    goto loc_003CB7A5;
loc_003CBB4B:
    a2 = (a2) + (4);
    goto loc_003CB866;
loc_003CBB54:
    v_stack_p20 = *(unsigned __int64 *)(gs_base + (0 + 392));
    goto loc_003CB8BB;
loc_003CBB66:
loc_003CBB71:
loc_003CBB7A:
    result = KeBugCheckEx(52, (unsigned int)(0xD13ULL), 0xFFFFFFFFC0000420ULL, a4);
loc_003CBB96:
    result = KeBugCheckEx(52, (unsigned int)(0xCEAULL), 0xFFFFFFFFC0000420ULL, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcSetDirtyInMask(void *Arg1, void *Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (112);
    Arg1 = 0;
    Arg4 = 0;
    v_stack_m48 = 0;
    Arg1 = (*(uint64_t *)(arg2) - 1) + ((uint32_t)(Arg3));
    v_stack_m74 = 0;
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg2));
    v_stack_m58 = v_xmm0;
    if (((Arg1) & (0xFFFFFFFFFE000000ULL)) != 0) goto loc_003CBB96;
    *(uint32_t *)(arg1 + 0x22C) = (uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC0) + 0x8A));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x98))) & (0x40000000ULL));
    if (condition_is_not_equal) goto loc_003CBB02;
loc_003CB71B:
    local_r15 = (*(uint64_t *)(arg2)) >> (12);
    local_r12 = (*(uint64_t *)(arg2) - 1) + ((uint32_t)(Arg3));
    local_r12 = (local_r12) >> (12);
    if ((*(uint64_t *)(arg1 + 0x20)) <= local_r12) goto loc_003CBB7A;
    v_stack_m60 = *(uint64_t *)(arg1 + 0x218);
    result = CcGetPrivateVolumeCacheMap(Arg1, Arg2, Arg3, Arg4);
    v_stack_m68 = result;
    if (Arg3 != 0) goto loc_003CBB17;
loc_003CB76A:
loc_003CB774:
    if ((*(uint64_t *)(arg1 + 0x20)) > 0x300000ULL) goto loc_003CBA65;
loc_003CB782:
    v_stack_m78 = 1;
    result = ExAcquireFastMutex(Arg1 + 288, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(arg1 + 0xA8) == 0) goto loc_003CBB2E;
loc_003CB7A5:
    if (local_r15 != local_r12) goto loc_003CB7B4;
    if (local_r15 == (*(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x28))) goto loc_003CB8EF;
loc_003CB7B4:
    if (local_r12 >= 768) goto loc_003CB94B;
loc_003CB7C1:
    result = CcFindBitmapRangeToDirty(*(uint64_t *)(arg1 + 0xA8), local_r15, v_stack_m70, Arg4);
    if (result == 0) goto loc_003CBB71;
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x18))) + (*(uint64_t *)(result + 0x10));
    if (local_r15 < Arg1) goto loc_003CB9D5;
loc_003CB7F2:
    result = ((uint32_t)(*(uint32_t *)(result + 0x1C))) + (*(uint64_t *)(result + 0x10));
    if (local_r12 > result) goto loc_003CB9E3;
loc_003CB802:
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(arg1 + 0x218) + 768, v_stack_m58, *(uint64_t *)(result + 0x10), Arg4);
    if ((*(uint32_t *)(arg1 + 0x70)) == 0) goto loc_003CBA34;
loc_003CB81C:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) - (*(uint32_t *)(result + 0x10)));
    Arg1 = (Arg1) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (31));
    local_rdi = (uint32_t)((1) << ((uint8_t)(Arg1)));
    if (local_r15 > local_r12) goto loc_003CB87E;
    result = (local_r12) - (local_r15);
    result = (result) + 1;
    local_r15 = (local_r15) + (result);
loc_003CB851:
    if ((((uint32_t)(local_rdi)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x28) + arg1 * 4))))) == 0) goto loc_003CB9C9;
loc_003CB85B:
    if ((uint32_t)(local_rdi + local_rdi * 1) == 0) goto loc_003CBB4B;
loc_003CB866:
    local_rdi = 1;
    if ((uint32_t)(local_rdi + local_rdi * 1) != 0) { local_rdi = (uint32_t)(local_rdi + local_rdi * 1); }
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_003CB851;
    v_stack_m74 = (uint32_t)((uint32_t)(v_stack_m74));
loc_003CB87E:
    result = CcChargeDirtyPages(Arg1, *(uint64_t *)(arg1 + 0xA8), result, (uint32_t)(v_stack_m74));
    result = KeReleaseInStackQueuedSpinLock(v_stack_m58, *(uint64_t *)(arg1 + 0xA8), result, (uint32_t)(v_stack_m74));
    if (((*(uint32_t *)(arg1 + 0x98)) & (0x10000000ULL)) == 0) goto loc_003CB8E3;
    if ((uint32_t)((uint32_t)(v_stack_m74)) == 0) goto loc_003CB8E3;
    if (v_stack_p20 == 0) goto loc_003CBB54;
loc_003CB8BB:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m74)))) << (12));
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x220) + 0x638) == 0) goto loc_003CB8E3;
    if (Arg2 != NULL) {
    }
loc_003CB8E3:
    if ((uint32_t)(local_rdi) == 0) goto loc_003CB76A;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x28) = local_r12;
loc_003CB8EF:
loc_003CB8F7:
    Arg1 = ((uint32_t)(v_stack_p18)) + (*(uint64_t *)(v_stack_p10));
    if (Arg1 > (*(uint64_t *)(arg1 + 0x30))) goto loc_003CB9F1;
loc_003CB90E:
    result = ExReleaseFastMutex(Arg1 + 288, Arg2, result, (uint32_t)(v_stack_m74));
    if (v_stack_m70 != 0) {
        Arg2 = v_stack_m70;
        Arg1 = v_rip + 10772691;
        result = ExFreeToNPagedLookasideList(Arg1, Arg2, result, (uint32_t)(v_stack_m74));
    }
    local_rsp = (local_rsp) + (112);
    return result;
loc_003CB94B:
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0xA8))) == ((uint16_t)((uint32_t)(v_stack_m78)))) goto loc_003CB7C1;
    Arg2 = 0;
    result = memset(v_stack_m70, Arg2, (uint32_t)(0x400ULL), (uint32_t)(v_stack_m74));
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x50)) != 0) goto loc_003CBABC;
loc_003CB96F:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x58) = v_stack_m70;
    local_rdi = 0;
    v_stack_m70 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10 + 0x8))) != (*(uint64_t *)(arg1 + 0xA8) + 16)) goto loc_003CB9C2;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x60) = *(uint64_t *)(arg1 + 0xA8) + 16;
    Arg3 = (uint32_t)(((uint32_t)(0x400ULL)) | (0xFFFFFFFFULL));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x60 + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10 + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10 + 0x8)) = *(uint64_t *)(arg1 + 0xA8) + 96;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10 + 0x8) = *(uint64_t *)(arg1 + 0xA8) + 96;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x70) = (uint32_t)(v_stack_m74);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x78) = Arg3;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10 + 0x8))) == (*(uint64_t *)(arg1 + 0xA8) + 16)) goto loc_003CBA86;
loc_003CB9C2:
loc_003CB9C9:
    Arg1 = (uint32_t)((3) | (0));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10 + 0x8)) = (uint32_t)(Arg1);
    local_r13 = (uint32_t)((v_stack_m60) + 1);
    goto loc_003CB85B;
loc_003CB9D5:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) - ((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10 + 0x8))));
    *(uint32_t *)((uint32_t)(v_stack_m78) + 0x18) = (uint32_t)(result);
    goto loc_003CB7F2;
loc_003CB9E3:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - ((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10 + 0x8))));
    *(uint32_t *)((uint32_t)(v_stack_m78) + 0x1C) = (uint32_t)(result);
    goto loc_003CB802;
loc_003CB9F1:
    *(void **)(v_stack_p8 + 0x30) = Arg1;
    if (((*(uint32_t *)(v_stack_p8 + 0x98)) & (0x40000000ULL)) == 0) goto loc_003CB90E;
    result = KeAcquireInStackQueuedSpinLock(local_r13 + 768, v_stack_m58, Arg3, (uint32_t)(v_stack_m74));
    *(uint32_t *)(v_stack_p8 + 0x98) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x98)));
loc_003CBA34:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x98)))) & (2)) != 0) goto loc_003CB81C;
    Arg4 = 0;
    Arg3 = 0;
    result = CcScheduleLazyWriteScan(local_r13, v_stack_m68, Arg3, Arg4);
    result = CcInsertIntoDirtySharedCacheMapList(v_stack_p8, v_stack_m68, Arg3, Arg4);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x20) = local_r15;
    goto loc_003CB81C;
loc_003CBA65:
    result = ExAllocateFromNPagedLookasideList(v_rip + 10772372, v_stack_m68, Arg3, Arg4);
    if (result == 0) goto loc_003CBB66;
    v_stack_m70 = result;
    goto loc_003CB782;
loc_003CBA86:
    *(uint64_t *)(v_rip + 0xA45F94) = result;
    *(uint64_t *)(v_rip + 0xA45F94 + 0x8) = v_stack_m68;
    *(uint64_t *)(v_stack_m68) = v_rip + 10772372;
    *(uint64_t *)(result + 0x8) = v_rip + 10772372;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0xA0) = 0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0xA8) + 0xA8) = 0;
    *(uint16_t *)(*(uint64_t *)(arg1 + 0xA8)) = (uint16_t)((uint32_t)(v_stack_m78));
    result = ExReleaseFastMutex(v_stack_p8 + 288, v_stack_m68, Arg3, Arg4);
    result = 0;
    v_stack_m78 = 0;
    goto loc_003CB774;
loc_003CBABC:
    Arg2 = 0;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x40) = v_xmm0;
    *(uint64_t *)(result + 0x50) = v_xmm1;
    result = memset(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x58), Arg2, Arg2 + 96, Arg4);
    goto loc_003CB96F;
loc_003CBB02:
    Arg1 = (*(uint64_t *)(arg2)) + ((uint32_t)(Arg3));
    if (Arg1 <= (*(uint64_t *)(v_stack_p8 + 0x30))) goto loc_003CB932;
    goto loc_003CB71B;
loc_003CBB17:
    result = ExAcquireFastMutex(v_stack_p8 + 288, Arg2, Arg2 + 96, Arg4);
    goto loc_003CB8F7;
loc_003CBB2E:
    result = CcAllocateInitializeMbcb(v_stack_p8 + 288, Arg2, Arg2 + 96, Arg4);
    *(uint64_t *)(v_stack_p8 + 0xA8) = result;
    goto loc_003CB7A5;
loc_003CBB4B:
    Arg2 = (Arg2) + (4);
    goto loc_003CB866;
loc_003CBB54:
    v_stack_p20 = *(uint64_t *)(gs_base + (0 + 0x188));
    goto loc_003CB8BB;
loc_003CBB66:
loc_003CBB71:
loc_003CBB7A:
    result = KeBugCheckEx(52, (uint32_t)(0xD13ULL), 0xFFFFFFFFC0000420ULL, Arg4);
loc_003CBB96:
    result = KeBugCheckEx(52, (uint32_t)(0xCEAULL), 0xFFFFFFFFC0000420ULL, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x98` | `32` | `R` |
| `Arg1` | `+ 0x98` | `32` | `W` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xA8` | `64` | `W` |
| `Arg1` | `+ 0x120` | `64` | `R` |
| `Arg1` | `+ 0x218` | `64` | `R` |
| `Arg1` | `+ 0x22C` | `32` | `W` |
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003CB688&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
