# KiDispatchException

- RVA: `0x003D7650`–`0x003D7E5F` (길이 `2,063` bytes)
- VA: `0x00000001403D7650`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00093C10`
- 디코드: `454`개 명령, `2,063/2,063` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x003D76AB` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003D7733` → [RtlGetExtendedContextLength3](../4E/RtlGetExtendedContextLength3_function_004EF028.md) (function, `0x004EF028`)
- `0x003D7753` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x003D777B` → [RtlInitializeExtendedContext2](../2F/RtlInitializeExtendedContext2_function_002F5D40.md) (function, `0x002F5D40`)
- `0x003D778D` → [KeContextFromKframes](KeContextFromKframes_function_003D9380.md) (function, `0x003D9380`)
- `0x003D77AE` → [KiPreprocessFault](KiPreprocessFault_function_003D7E70.md) (function, `0x003D7E70`)
- `0x003D77E7` → [KdTrap](../43/KdTrap_function_00431680.md) (function, `0x00431680`)
- `0x003D7808` → [KeContextToKframes](../4F/KeContextToKframes_function_004FD790.md) (function, `0x004FD790`)
- `0x003D7821` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003D78B7` → [KdIsThisAKdTrap](../../pagekd/B8/KdIsThisAKdTrap_function_00B8A130.md) (function, `0x00B8A130`)
- `0x003D790E` → [KdTrap](../43/KdTrap_function_00431680.md) (function, `0x00431680`)
- `0x003D7998` → [PsWow64GetProcessMachine](../../page/8D/PsWow64GetProcessMachine_function_008D2130.md) (function, `0x008D2130`)
- `0x003D79BD` → [RtlDispatchException](../2F/RtlDispatchException_function_002F22A0.md) (function, `0x002F22A0`)
- `0x003D79E0` → [KdTrap](../43/KdTrap_function_00431680.md) (function, `0x00431680`)
- `0x003D7A06` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003D7A26` → [DbgkForwardException](../../page/8A/DbgkForwardException_function_008A2D60.md) (function, `0x008A2D60`)
- `0x003D7AFB` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x003D7B1C` → [KeCopyExceptionRecord](../43/KeCopyExceptionRecord_function_00439750.md) (function, `0x00439750`)
- `0x003D7B7F` → [RtlpCopyExtendedContext](../3F/RtlpCopyExtendedContext_function_003F4DD0.md) (function, `0x003F4DD0`)
- `0x003D7BBC` → [KePopulateContinuationContext](KePopulateContinuationContext_function_003D9340.md) (function, `0x003D9340`)
- `0x003D7BEE` → [KiSetupForInstrumentationReturn](../45/KiSetupForInstrumentationReturn_function_00459300.md) (function, `0x00459300`)
- `0x003D7C1A` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x003D7CCF` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x003D7CFD` → [KeCopyExceptionRecord](../43/KeCopyExceptionRecord_function_00439750.md) (function, `0x00439750`)
- `0x003D7D3E` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x003D7D4D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003D7D85` → [KiTpHandleTrap](../4F/KiTpHandleTrap_function_004F86B0.md) (function, `0x004F86B0`)
- `0x003D7DFE` → [DbgkForwardException](../../page/8A/DbgkForwardException_function_008A2D60.md) (function, `0x008A2D60`)
- `0x003D7E13` → [DbgkForwardException](../../page/8A/DbgkForwardException_function_008A2D60.md) (function, `0x008A2D60`)
- `0x003D7E27` → [ZwTerminateProcess](../6A/ZwTerminateProcess_function_006AD650.md) (function, `0x006AD650`)
- `0x003D7E35` → [KiSetupForInstrumentationReturn](../45/KiSetupForInstrumentationReturn_function_00459300.md) (function, `0x00459300`)

### Direct callers
- [KiRaiseException](KiRaiseException_function_003D5CA0.md) at `0x003D5D9E`
- [KiInitializeUserApc](KiInitializeUserApc_function_003D8D38.md) at `0x003D9304`
- [KxExceptionDispatchOnExceptionStack](../6B/KxExceptionDispatchOnExceptionStack_function_006B1BC0.md) at `0x006B1BCD`
- [KiExceptionDispatch](../6C/KiExceptionDispatch_function_006C5900.md) at `0x006C5A40`
- [KiFastFailDispatch](../6C/KiFastFailDispatch_function_006C5E40.md) at `0x006C5F01`
- [PspInitializeThunkContext](../../page/8D/PspInitializeThunkContext_function_008D5418.md) at `0x008D57DB`
- [sub_00B18BDE](../../page/B1/Unknown_function_00B18BDE.md) at `0x00B18C4A`

### Static image references
- `0x003D7666` → RVA `0x00E0A740` (`.data`; read)
- `0x003D770D` → RVA `0x01201841` (`CFGRO`; read)
- `0x003D78CF` → RVA `0x00F55CA0` (`.data`; read)
- `0x003D7924` → RVA `0x00FC6B30` (`ALMOSTRO`; read)
- `0x003D7BDC` → RVA `0x00FC7490` (`ALMOSTRO`; read)
- `0x003D7D5E` → RVA `0x00FC6D00` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x003D78B7` → [KdIsThisAKdTrap](../../pagekd/B8/KdIsThisAKdTrap_function_00B8A130.md) (`.text` → `PAGEKD`)
  - `0x003D7998` → [PsWow64GetProcessMachine](../../page/8D/PsWow64GetProcessMachine_function_008D2130.md) (`.text` → `PAGE`)
  - `0x003D7A26` → [DbgkForwardException](../../page/8A/DbgkForwardException_function_008A2D60.md) (`.text` → `PAGE`)
  - `0x003D7AFB` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (`.text` → `PAGE`)
  - `0x003D7DFE` → [DbgkForwardException](../../page/8A/DbgkForwardException_function_008A2D60.md) (`.text` → `PAGE`)
  - `0x003D7E13` → [DbgkForwardException](../../page/8A/DbgkForwardException_function_008A2D60.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **11**
  - `0x003D785A` → [sub_006E9870 + 0x9](../6E/Unknown_function_006E9870.md) (`tail-transfer`)
  - `0x003D7863` → [sub_006E9870](../6E/Unknown_function_006E9870.md) (`tail-transfer`)
  - `0x003D786C` → [sub_006E9870 + 0x10](../6E/Unknown_function_006E9870.md) (`tail-transfer`)
  - `0x003D7879` → [sub_006E9870 + 0x10](../6E/Unknown_function_006E9870.md) (`tail-transfer`)
  - `0x003D7C5D` → [sub_006E9870 + 0x84](../6E/Unknown_function_006E9870.md) (`tail-transfer`)
  - `0x003D7C68` → [sub_006E9870 + 0x8B](../6E/Unknown_function_006E9870.md) (`tail-transfer`)
  - `0x003D7C75` → [sub_006E9870 + 0x8B](../6E/Unknown_function_006E9870.md) (`tail-transfer`)
  - `0x003D7DDC` → [sub_006E9870 + 0xB8](../6E/Unknown_function_006E9870.md) (`tail-transfer`)
  - `0x003D7DE7` → [sub_006E9870 + 0x6D](../6E/Unknown_function_006E9870.md) (`tail-transfer`)
  - `0x003D7E4D` → [sub_006E9870 + 0xB8](../6E/Unknown_function_006E9870.md) (`tail-transfer`)
  - `0x003D7E5A` → [sub_006E9870 + 0xA0](../6E/Unknown_function_006E9870.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003D7650  40 55                           push rbp
003D7652  53                              push rbx
003D7653  57                              push rdi
003D7654  41 54                           push r12
003D7656  41 56                           push r14
003D7658  41 57                           push r15
003D765A  48 81 EC A8 01 00 00            sub rsp, 0x1a8
003D7661  48 8D 6C 24 30                  lea rbp, [rsp + 0x30]
003D7666  48 8B 05 D3 30 A3 00            mov rax, qword ptr [rip + 0xa330d3]
003D766D  48 33 C5                        xor rax, rbp
003D7670  48 89 85 60 01 00 00            mov qword ptr [rbp + 0x160], rax
003D7677  41 8A F9                        mov dil, r9b
003D767A  44 88 4D 00                     mov byte ptr [rbp], r9b
003D767E  4D 8B E0                        mov r12, r8
003D7681  4C 8B FA                        mov r15, rdx
003D7684  48 89 55 28                     mov qword ptr [rbp + 0x28], rdx
003D7688  4C 8B F1                        mov r14, rcx
003D768B  48 89 4D 50                     mov qword ptr [rbp + 0x50], rcx
003D768F  4C 89 45 68                     mov qword ptr [rbp + 0x68], r8
003D7693  48 83 65 20 00                  and qword ptr [rbp + 0x20], 0
003D7698  83 65 10 00                     and dword ptr [rbp + 0x10], 0
003D769C  33 D2                           xor edx, edx
003D769E  41 B8 94 00 00 00               mov r8d, 0x94
003D76A4  48 8D 8D A4 00 00 00            lea rcx, [rbp + 0xa4]
003D76AB  E8 90 F5 2E 00                  call 0x1406c6c40
003D76B0  0F 57 C0                        xorps xmm0, xmm0
003D76B3  0F 11 85 40 01 00 00            movups xmmword ptr [rbp + 0x140], xmm0
003D76BA  0F 11 85 50 01 00 00            movups xmmword ptr [rbp + 0x150], xmm0
003D76C1  C6 45 01 00                     mov byte ptr [rbp + 1], 0
003D76C5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
003D76CE  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
003D76D2  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
003D76D9  48 89 55 30                     mov qword ptr [rbp + 0x30], rdx
003D76DD  65 FF 04 25 F0 87 00 00         inc dword ptr gs:[0x87f0]
003D76E5  80 BD D0 01 00 00 00            cmp byte ptr [rbp + 0x1d0], 0
003D76EC  0F 85 46 01 00 00               jne 0x1403d7838
003D76F2  41 BF 1F 00 10 00               mov r15d, 0x10001f
003D76F8  44 89 7D 04                     mov dword ptr [rbp + 4], r15d
003D76FC  33 FF                           xor edi, edi
003D76FE  40 38 7D 00                     cmp byte ptr [rbp], dil
003D7702  0F 85 1C 02 00 00               jne 0x1403d7924
003D7708  B9 9F 00 10 00                  mov ecx, 0x10009f
003D770D  40 38 3D 2D A1 E2 00            cmp byte ptr [rip + 0xe2a12d], dil
003D7714  44 0F 45 F9                     cmovne r15d, ecx
003D7718  44 89 7D 04                     mov dword ptr [rbp + 4], r15d
003D771C  48 BB D8 03 00 00 80 F7 FF FF   movabs rbx, 0xfffff780000003d8
003D7726  4C 8B CB                        mov r9, rbx
003D7729  4C 8B C7                        mov r8, rdi
003D772C  48 8D 55 10                     lea rdx, [rbp + 0x10]
003D7730  41 8B CF                        mov ecx, r15d
003D7733  E8 F0 78 11 00                  call 0x1404ef028
003D7738  44 8B 45 10                     mov r8d, dword ptr [rbp + 0x10]
003D773C  49 8D 40 0F                     lea rax, [r8 + 0xf]
003D7740  49 3B C0                        cmp rax, r8
003D7743  77 0A                           ja 0x1403d774f
003D7745  48 B8 F0 FF FF FF FF FF FF 0F   movabs rax, 0xffffffffffffff0
003D774F  48 83 E0 F0                     and rax, 0xfffffffffffffff0
003D7753  E8 08 32 2E 00                  call 0x1406ba960
003D7758  48 2B E0                        sub rsp, rax
003D775B  48 8D 5C 24 30                  lea rbx, [rsp + 0x30]
003D7760  48 89 5D 58                     mov qword ptr [rbp + 0x58], rbx
003D7764  80 7D 00 00                     cmp byte ptr [rbp], 0
003D7768  0F 85 DA 05 00 00               jne 0x1403d7d48
003D776E  4C 8B CF                        mov r9, rdi
003D7771  4C 8D 45 20                     lea r8, [rbp + 0x20]
003D7775  41 8B D7                        mov edx, r15d
003D7778  48 8B CB                        mov rcx, rbx
003D777B  E8 C0 E5 F1 FF                  call 0x1402f5d40
003D7780  4C 8B C3                        mov r8, rbx
003D7783  4C 8B 7D 28                     mov r15, qword ptr [rbp + 0x28]
003D7787  49 8B D7                        mov rdx, r15
003D778A  49 8B CC                        mov rcx, r12
003D778D  E8 EE 1B 00 00                  call 0x1403d9380
003D7792  BF 01 00 00 00                  mov edi, 1
003D7797  41 81 3E 03 00 00 80            cmp dword ptr [r14], 0x80000003
003D779E  0F 84 B3 05 00 00               je 0x1403d7d57
003D77A4  44 8A 45 00                     mov r8b, byte ptr [rbp]
003D77A8  48 8B D3                        mov rdx, rbx
003D77AB  49 8B CE                        mov rcx, r14
003D77AE  E8 BD 06 00 00                  call 0x1403d7e70
003D77B3  84 C0                           test al, al
003D77B5  75 3D                           jne 0x1403d77f4
003D77B7  44 8A 45 00                     mov r8b, byte ptr [rbp]
003D77BB  45 84 C0                        test r8b, r8b
003D77BE  0F 85 BA 00 00 00               jne 0x1403d787e
003D77C4  44 38 85 D0 01 00 00            cmp byte ptr [rbp + 0x1d0], r8b
003D77CB  0F 84 F9 01 00 00               je 0x1403d79ca
003D77D1  44 88 44 24 28                  mov byte ptr [rsp + 0x28], r8b
003D77D6  44 88 44 24 20                  mov byte ptr [rsp + 0x20], r8b
003D77DB  4C 8B CB                        mov r9, rbx
003D77DE  4D 8B C6                        mov r8, r14
003D77E1  49 8B D7                        mov rdx, r15
003D77E4  49 8B CC                        mov rcx, r12
003D77E7  E8 94 9E 05 00                  call 0x140431680
003D77EC  84 C0                           test al, al
003D77EE  0F 84 C3 01 00 00               je 0x1403d79b7
003D77F4  8A 45 00                        mov al, byte ptr [rbp]
003D77F7  88 44 24 20                     mov byte ptr [rsp + 0x20], al
003D77FB  44 8B 4B 30                     mov r9d, dword ptr [rbx + 0x30]
003D77FF  4C 8B C3                        mov r8, rbx
003D7802  49 8B D7                        mov rdx, r15
003D7805  49 8B CC                        mov rcx, r12
003D7808  E8 83 5F 12 00                  call 0x1404fd790
003D780D  80 7D 01 00                     cmp byte ptr [rbp + 1], 0
003D7811  0F 85 1A 06 00 00               jne 0x1403d7e31
003D7817  48 8B 8D 60 01 00 00            mov rcx, qword ptr [rbp + 0x160]
003D781E  48 33 CD                        xor rcx, rbp
003D7821  E8 1A 4E 2D 00                  call 0x1406ac640
003D7826  48 8D A5 78 01 00 00            lea rsp, [rbp + 0x178]
003D782D  41 5F                           pop r15
003D782F  41 5E                           pop r14
003D7831  41 5C                           pop r12
003D7833  5F                              pop rdi
003D7834  5B                              pop rbx
003D7835  5D                              pop rbp
003D7836  C3                              ret
003D7837  CC                              int3
003D7838  48 85 D2                        test rdx, rdx
003D783B  0F 84 B1 FE FF FF               je 0x1403d76f2
003D7841  48 83 BA 40 06 00 00 00         cmp qword ptr [rdx + 0x640], 0
003D7849  0F 84 A3 FE FF FF               je 0x1403d76f2
003D784F  41 8B 1E                        mov ebx, dword ptr [r14]
003D7852  8B CB                           mov ecx, ebx
003D7854  81 E9 02 00 00 10               sub ecx, 0x10000002
003D785A  0F 84 19 20 31 00               je 0x1406e9879
003D7860  83 E9 01                        sub ecx, 1
003D7863  0F 84 07 20 31 00               je 0x1406e9870
003D7869  83 F9 01                        cmp ecx, 1
003D786C  0F 85 0E 20 31 00               jne 0x1406e9880
003D7872  41 C7 06 05 00 00 C0            mov dword ptr [r14], 0xc0000005
003D7879  E9 02 20 31 00                  jmp 0x1406e9880
003D787E  4C 8B BB 98 00 00 00            mov r15, qword ptr [rbx + 0x98]
003D7885  4C 89 7D 18                     mov qword ptr [rbp + 0x18], r15
003D7889  4C 89 7D 48                     mov qword ptr [rbp + 0x48], r15
003D788D  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
003D7891  8B 80 FC 05 00 00               mov eax, dword ptr [rax + 0x5fc]
003D7897  40 84 C7                        test dil, al
003D789A  0F 84 81 03 00 00               je 0x1403d7c21
003D78A0  80 BD D0 01 00 00 00            cmp byte ptr [rbp + 0x1d0], 0
003D78A7  0F 84 48 05 00 00               je 0x1403d7df5
003D78AD  45 8B 0E                        mov r9d, dword ptr [r14]
003D78B0  44 89 4D 08                     mov dword ptr [rbp + 8], r9d
003D78B4  49 8B CE                        mov rcx, r14
003D78B7  E8 74 28 7B 00                  call 0x140b8a130
003D78BC  88 45 01                        mov byte ptr [rbp + 1], al
003D78BF  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
003D78C8  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
003D78CF  80 3D CA E3 B7 00 00            cmp byte ptr [rip + 0xb7e3ca], 0
003D78D6  0F 85 30 01 00 00               jne 0x1403d7a0c
003D78DC  48 83 BA 08 03 00 00 00         cmp qword ptr [rdx + 0x308], 0
003D78E4  0F 85 22 01 00 00               jne 0x1403d7a0c
003D78EA  41 81 F9 33 00 00 80            cmp r9d, 0x80000033
003D78F1  0F 84 15 01 00 00               je 0x1403d7a0c
003D78F7  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
003D78FC  44 88 44 24 20                  mov byte ptr [rsp + 0x20], r8b
003D7901  4C 8B CB                        mov r9, rbx
003D7904  4D 8B C6                        mov r8, r14
003D7907  48 8B 55 28                     mov rdx, qword ptr [rbp + 0x28]
003D790B  49 8B CC                        mov rcx, r12
003D790E  E8 6D 9D 05 00                  call 0x140431680
003D7913  84 C0                           test al, al
003D7915  0F 84 D1 04 00 00               je 0x1403d7dec
003D791B  4C 8B 7D 28                     mov r15, qword ptr [rbp + 0x28]
003D791F  E9 D0 FE FF FF                  jmp 0x1403d77f4
003D7924  48 F7 05 01 F2 BE 00 00 00 80 00  test qword ptr [rip + 0xbef201], 0x800000
003D792F  0F 84 E7 FD FF FF               je 0x1403d771c
003D7935  41 BF 5F 00 10 00               mov r15d, 0x10005f
003D793B  44 89 7D 04                     mov dword ptr [rbp + 4], r15d
003D793F  A1 EC 03 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000003ec]
003D7948  A8 02                           test al, 2
003D794A  0F 84 CC FD FF FF               je 0x1403d771c
003D7950  48 B9 08 07 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000708
003D795A  48 BB D8 03 00 00 80 F7 FF FF   movabs rbx, 0xfffff780000003d8
003D7964  48 8B 09                        mov rcx, qword ptr [rcx]
003D7967  48 0B 0B                        or rcx, qword ptr [rbx]
003D796A  48 0F BA E1 0B                  bt rcx, 0xb
003D796F  73 11                           jae 0x1403d7982
003D7971  F7 82 54 07 00 00 00 40 00 00   test dword ptr [rdx + 0x754], 0x4000
003D797B  75 05                           jne 0x1403d7982
003D797D  48 0F BA F1 0B                  btr rcx, 0xb
003D7982  48 8B F9                        mov rdi, rcx
003D7985  48 81 E7 FF FF F9 FF            and rdi, 0xfffffffffff9ffff
003D798C  41 F6 46 04 80                  test byte ptr [r14 + 4], 0x80
003D7991  48 0F 44 F9                     cmove rdi, rcx
003D7995  48 8B CA                        mov rcx, rdx
003D7998  E8 93 A7 4F 00                  call 0x1408d2130
003D799D  B9 4C 01 00 00                  mov ecx, 0x14c
003D79A2  66 3B C1                        cmp ax, cx
003D79A5  0F 85 7B FD FF FF               jne 0x1403d7726
003D79AB  48 81 E7 FF FF F9 FF            and rdi, 0xfffffffffff9ffff
003D79B2  E9 6F FD FF FF                  jmp 0x1403d7726
003D79B7  48 8B D3                        mov rdx, rbx
003D79BA  49 8B CE                        mov rcx, r14
003D79BD  E8 DE A8 F1 FF                  call 0x1402f22a0
003D79C2  84 C0                           test al, al
003D79C4  0F 85 2A FE FF FF               jne 0x1403d77f4
003D79CA  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
003D79CF  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
003D79D4  4C 8B CB                        mov r9, rbx
003D79D7  4D 8B C6                        mov r8, r14
003D79DA  49 8B D7                        mov rdx, r15
003D79DD  49 8B CC                        mov rcx, r12
003D79E0  E8 9B 9C 05 00                  call 0x140431680
003D79E5  84 C0                           test al, al
003D79E7  0F 85 07 FE FF FF               jne 0x1403d77f4
003D79ED  49 63 16                        movsxd rdx, dword ptr [r14]
003D79F0  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
003D79F4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003D79F9  4D 8B 4E 20                     mov r9, qword ptr [r14 + 0x20]
003D79FD  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
003D7A01  B9 1E 00 00 00                  mov ecx, 0x1e
003D7A06  E8 55 5C 12 00                  call 0x1404fd660
003D7A0B  CC                              int3
003D7A0C  84 C0                           test al, al
003D7A0E  0F 85 E3 FE FF FF               jne 0x1403d78f7
003D7A14  41 81 F9 33 00 00 80            cmp r9d, 0x80000033
003D7A1B  74 16                           je 0x1403d7a33
003D7A1D  45 33 C0                        xor r8d, r8d
003D7A20  40 8A D7                        mov dl, dil
003D7A23  49 8B CE                        mov rcx, r14
003D7A26  E8 35 B3 4C 00                  call 0x1408a2d60
003D7A2B  84 C0                           test al, al
003D7A2D  0F 85 E4 FD FF FF               jne 0x1403d7817
003D7A33  FA                              cli
003D7A34  41 0F BA B4 24 78 01 00 00 08   btr dword ptr [r12 + 0x178], 8
003D7A3E  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
003D7A47  49 8B 90 B8 8E 00 00            mov rdx, qword ptr [r8 + 0x8eb8]
003D7A4E  48 85 D2                        test rdx, rdx
003D7A51  0F 85 C9 02 00 00               jne 0x1403d7d20
003D7A57  FB                              sti
003D7A58  C7 85 A0 00 00 00 05 00 00 C0   mov dword ptr [rbp + 0xa0], 0xc0000005
003D7A62  83 65 0C 00                     and dword ptr [rbp + 0xc], 0
003D7A66  8B 45 04                        mov eax, dword ptr [rbp + 4]
003D7A69  90                              nop
003D7A6A  4C 89 7D 38                     mov qword ptr [rbp + 0x38], r15
003D7A6E  B9 40 00 10 00                  mov ecx, 0x100040
003D7A73  23 C1                           and eax, ecx
003D7A75  89 45 08                        mov dword ptr [rbp + 8], eax
003D7A78  3B C1                           cmp eax, ecx
003D7A7A  0F 84 FA 01 00 00               je 0x1403d7c7a
003D7A80  49 8D 7F D8                     lea rdi, [r15 - 0x28]
003D7A84  48 83 E7 F0                     and rdi, 0xfffffffffffffff0
003D7A88  48 89 7D 70                     mov qword ptr [rbp + 0x70], rdi
003D7A8C  48 8D 9F 60 FF FF FF            lea rbx, [rdi - 0xa0]
003D7A93  48 89 5D 78                     mov qword ptr [rbp + 0x78], rbx
003D7A97  4C 8D 43 E0                     lea r8, [rbx - 0x20]
003D7A9B  4C 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], r8
003D7AA2  4D 8D 88 30 FB FF FF            lea r9, [r8 - 0x4d0]
003D7AA9  4C 89 8D 88 00 00 00            mov qword ptr [rbp + 0x88], r9
003D7AB0  B8 30 FB FF FF                  mov eax, 0xfffffb30
003D7AB5  89 85 40 01 00 00               mov dword ptr [rbp + 0x140], eax
003D7ABB  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
003D7ABF  48 8B D1                        mov rdx, rcx
003D7AC2  49 2B D1                        sub rdx, r9
003D7AC5  89 95 44 01 00 00               mov dword ptr [rbp + 0x144], edx
003D7ACB  89 85 48 01 00 00               mov dword ptr [rbp + 0x148], eax
003D7AD1  C7 85 4C 01 00 00 D0 04 00 00   mov dword ptr [rbp + 0x14c], 0x4d0
003D7ADB  41 8B C7                        mov eax, r15d
003D7ADE  41 2B C0                        sub eax, r8d
003D7AE1  89 85 50 01 00 00               mov dword ptr [rbp + 0x150], eax
003D7AE7  8B C1                           mov eax, ecx
003D7AE9  41 2B C7                        sub eax, r15d
003D7AEC  89 85 54 01 00 00               mov dword ptr [rbp + 0x154], eax
003D7AF2  41 B8 10 00 00 00               mov r8d, 0x10
003D7AF8  49 8B C9                        mov rcx, r9
003D7AFB  E8 C0 16 51 00                  call 0x1408e91c0
003D7B00  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
003D7B04  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
003D7B08  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
003D7B0C  48 8B 80 F8 00 00 00            mov rax, qword ptr [rax + 0xf8]
003D7B13  48 89 07                        mov qword ptr [rdi], rax
003D7B16  49 8B D6                        mov rdx, r14
003D7B19  48 8B CB                        mov rcx, rbx
003D7B1C  E8 2F 1C 06 00                  call 0x140439750
003D7B21  81 7D 08 40 00 10 00            cmp dword ptr [rbp + 8], 0x100040
003D7B28  75 2D                           jne 0x1403d7b57
003D7B2A  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
003D7B2E  48 63 48 10                     movsxd rcx, dword ptr [rax + 0x10]
003D7B32  48 03 C8                        add rcx, rax
003D7B35  0F 10 01                        movups xmm0, xmmword ptr [rcx]
003D7B38  41 0F 11 07                     movups xmmword ptr [r15], xmm0
003D7B3C  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
003D7B40  41 0F 11 4F 10                  movups xmmword ptr [r15 + 0x10], xmm1
003D7B45  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
003D7B49  41 0F 11 47 20                  movups xmmword ptr [r15 + 0x20], xmm0
003D7B4E  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
003D7B52  41 0F 11 4F 30                  movups xmmword ptr [r15 + 0x30], xmm1
003D7B57  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
003D7B5D  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
003D7B61  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003D7B66  44 8B 4D 04                     mov r9d, dword ptr [rbp + 4]
003D7B6A  4C 8D 85 40 01 00 00            lea r8, [rbp + 0x140]
003D7B71  48 8D 7B E0                     lea rdi, [rbx - 0x20]
003D7B75  48 8B D7                        mov rdx, rdi
003D7B78  BB 01 00 00 00                  mov ebx, 1
003D7B7D  8A CB                           mov cl, bl
003D7B7F  E8 4C D2 01 00                  call 0x1403f4dd0
003D7B84  0F 10 85 40 01 00 00            movups xmm0, xmmword ptr [rbp + 0x140]
003D7B8B  0F 11 07                        movups xmmword ptr [rdi], xmm0
003D7B8E  0F 10 8D 50 01 00 00            movups xmm1, xmmword ptr [rbp + 0x150]
003D7B95  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
003D7B99  4C 8B 4D 40                     mov r9, qword ptr [rbp + 0x40]
003D7B9D  41 0F B7 81 E6 01 00 00         movzx eax, word ptr [r9 + 0x1e6]
003D7BA5  66 2B C3                        sub ax, bx
003D7BA8  66 41 89 81 E6 01 00 00         mov word ptr [r9 + 0x1e6], ax
003D7BB0  90                              nop
003D7BB1  89 5D 0C                        mov dword ptr [rbp + 0xc], ebx
003D7BB4  49 8B 8C 24 68 01 00 00         mov rcx, qword ptr [r12 + 0x168]
003D7BBC  E8 7F 17 00 00                  call 0x1403d9340
003D7BC1  4C 8D 97 30 FB FF FF            lea r10, [rdi - 0x4d0]
003D7BC8  4D 89 94 24 80 01 00 00         mov qword ptr [r12 + 0x180], r10
003D7BD0  8D 43 32                        lea eax, [rbx + 0x32]
003D7BD3  66 41 89 84 24 70 01 00 00      mov word ptr [r12 + 0x170], ax
003D7BDC  48 8B 05 AD F8 BE 00            mov rax, qword ptr [rip + 0xbef8ad]
003D7BE3  49 89 84 24 68 01 00 00         mov qword ptr [r12 + 0x168], rax
003D7BEB  49 8B CC                        mov rcx, r12
003D7BEE  E8 0D 17 08 00                  call 0x140459300
003D7BF3  90                              nop
003D7BF4  41 0F B7 81 E6 01 00 00         movzx eax, word ptr [r9 + 0x1e6]
003D7BFC  66 03 C3                        add ax, bx
003D7BFF  66 41 89 81 E6 01 00 00         mov word ptr [r9 + 0x1e6], ax
003D7C07  0F 85 8C 00 00 00               jne 0x1403d7c99
003D7C0D  90                              nop
003D7C0E  49 8D 81 98 00 00 00            lea rax, [r9 + 0x98]
003D7C15  48 39 00                        cmp qword ptr [rax], rax
003D7C18  74 7F                           je 0x1403d7c99
003D7C1A  E8 61 B0 F0 FF                  call 0x1402e2c80
003D7C1F  EB 78                           jmp 0x1403d7c99
003D7C21  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003D7C2A  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003D7C31  48 83 B9 10 03 00 00 00         cmp qword ptr [rcx + 0x310], 0
003D7C39  0F 85 60 01 00 00               jne 0x1403d7d9f
003D7C3F  0F B7 43 38                     movzx eax, word ptr [rbx + 0x38]
003D7C43  B9 F8 FF 00 00                  mov ecx, 0xfff8
003D7C48  66 23 C1                        and ax, cx
003D7C4B  66 83 F8 20                     cmp ax, 0x20
003D7C4F  0F 85 4B FC FF FF               jne 0x1403d78a0
003D7C55  41 8B 06                        mov eax, dword ptr [r14]
003D7C58  3D 03 00 00 80                  cmp eax, 0x80000003
003D7C5D  0F 84 91 1C 31 00               je 0x1406e98f4
003D7C63  3D 04 00 00 80                  cmp eax, 0x80000004
003D7C68  0F 85 8D 1C 31 00               jne 0x1406e98fb
003D7C6E  41 C7 06 1E 00 00 40            mov dword ptr [r14], 0x4000001e
003D7C75  E9 81 1C 31 00                  jmp 0x1406e98fb
003D7C7A  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
003D7C7E  8B 48 14                        mov ecx, dword ptr [rax + 0x14]
003D7C81  4C 8B 7D 18                     mov r15, qword ptr [rbp + 0x18]
003D7C85  4C 2B F9                        sub r15, rcx
003D7C88  4C 89 7D 38                     mov qword ptr [rbp + 0x38], r15
003D7C8C  49 83 E7 C0                     and r15, 0xffffffffffffffc0
003D7C90  4C 89 7D 38                     mov qword ptr [rbp + 0x38], r15
003D7C94  E9 E7 FD FF FF                  jmp 0x1403d7a80
003D7C99  83 65 0C 00                     and dword ptr [rbp + 0xc], 0
003D7C9D  E9 75 FB FF FF                  jmp 0x1403d7817
003D7CA2  83 7D 0C 00                     cmp dword ptr [rbp + 0xc], 0
003D7CA6  74 30                           je 0x1403d7cd8
003D7CA8  90                              nop
003D7CA9  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
003D7CAD  0F BF 81 E6 01 00 00            movsx eax, word ptr [rcx + 0x1e6]
003D7CB4  FF C0                           inc eax
003D7CB6  66 89 81 E6 01 00 00            mov word ptr [rcx + 0x1e6], ax
003D7CBD  66 85 C0                        test ax, ax
003D7CC0  75 12                           jne 0x1403d7cd4
003D7CC2  90                              nop
003D7CC3  48 8D 81 98 00 00 00            lea rax, [rcx + 0x98]
003D7CCA  48 39 00                        cmp qword ptr [rax], rax
003D7CCD  74 05                           je 0x1403d7cd4
003D7CCF  E8 AC AF F0 FF                  call 0x1402e2c80
003D7CD4  83 65 0C 00                     and dword ptr [rbp + 0xc], 0
003D7CD8  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
003D7CDC  81 BD A0 00 00 00 FD 00 00 C0   cmp dword ptr [rbp + 0xa0], 0xc00000fd
003D7CE6  75 2E                           jne 0x1403d7d16
003D7CE8  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
003D7CEC  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
003D7CF3  48 8D 95 A0 00 00 00            lea rdx, [rbp + 0xa0]
003D7CFA  49 8B CE                        mov rcx, r14
003D7CFD  E8 4E 1A 06 00                  call 0x140439750
003D7D02  8B 45 04                        mov eax, dword ptr [rbp + 4]
003D7D05  4C 8B 7D 48                     mov r15, qword ptr [rbp + 0x48]
003D7D09  4C 89 7D 18                     mov qword ptr [rbp + 0x18], r15
003D7D0D  4C 8B 65 68                     mov r12, qword ptr [rbp + 0x68]
003D7D11  E9 53 FD FF FF                  jmp 0x1403d7a69
003D7D16  BF 01 00 00 00                  mov edi, 1
003D7D1B  E9 D5 00 00 00                  jmp 0x1403d7df5
003D7D20  0F 0D 0A                        prefetchw byte ptr [rdx]
003D7D23  8B 02                           mov eax, dword ptr [rdx]
003D7D25  8B C8                           mov ecx, eax
003D7D27  0F BA F1 15                     btr ecx, 0x15
003D7D2B  F0 0F B1 0A                     lock cmpxchg dword ptr [rdx], ecx
003D7D2F  75 F4                           jne 0x1403d7d25
003D7D31  0F BA E0 15                     bt eax, 0x15
003D7D35  0F 83 1C FD FF FF               jae 0x1403d7a57
003D7D3B  49 8B C8                        mov rcx, r8
003D7D3E  E8 8D B4 E8 FF                  call 0x1402631d0
003D7D43  E9 0F FD FF FF                  jmp 0x1403d7a57
003D7D48  33 D2                           xor edx, edx
003D7D4A  48 8B CB                        mov rcx, rbx
003D7D4D  E8 EE EE 2E 00                  call 0x1406c6c40
003D7D52  E9 17 FA FF FF                  jmp 0x1403d776e
003D7D57  48 FF 8B F8 00 00 00            dec qword ptr [rbx + 0xf8]
003D7D5E  8B 05 9C EF BE 00               mov eax, dword ptr [rip + 0xbeef9c]
003D7D64  A8 02                           test al, 2
003D7D66  0F 84 38 FA FF FF               je 0x1403d77a4
003D7D6C  49 29 BC 24 68 01 00 00         sub qword ptr [r12 + 0x168], rdi
003D7D74  44 8A 8D D0 01 00 00            mov r9b, byte ptr [rbp + 0x1d0]
003D7D7B  44 8A 45 00                     mov r8b, byte ptr [rbp]
003D7D7F  48 8B D3                        mov rdx, rbx
003D7D82  49 8B CE                        mov rcx, r14
003D7D85  E8 26 09 12 00                  call 0x1404f86b0
003D7D8A  84 C0                           test al, al
003D7D8C  0F 85 62 FA FF FF               jne 0x1403d77f4
003D7D92  49 01 BC 24 68 01 00 00         add qword ptr [r12 + 0x168], rdi
003D7D9A  E9 05 FA FF FF                  jmp 0x1403d77a4
003D7D9F  41 81 3E 02 00 00 80            cmp dword ptr [r14], 0x80000002
003D7DA6  0F 85 93 FE FF FF               jne 0x1403d7c3f
003D7DAC  41 F7 84 24 78 01 00 00 00 00 04 00  test dword ptr [r12 + 0x178], 0x40000
003D7DB8  0F 84 81 FE FF FF               je 0x1403d7c3f
003D7DBE  FA                              cli
003D7DBF  41 0F BA B4 24 78 01 00 00 12   btr dword ptr [r12 + 0x178], 0x12
003D7DC9  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
003D7DD2  49 8B 90 B8 8E 00 00            mov rdx, qword ptr [r8 + 0x8eb8]
003D7DD9  48 85 D2                        test rdx, rdx
003D7DDC  0F 84 46 1B 31 00               je 0x1406e9928
003D7DE2  0F 0D 0A                        prefetchw byte ptr [rdx]
003D7DE5  8B 02                           mov eax, dword ptr [rdx]
003D7DE7  E9 F1 1A 31 00                  jmp 0x1406e98dd
003D7DEC  44 8B 4D 08                     mov r9d, dword ptr [rbp + 8]
003D7DF0  E9 1F FC FF FF                  jmp 0x1403d7a14
003D7DF5  44 8A C7                        mov r8b, dil
003D7DF8  40 8A D7                        mov dl, dil
003D7DFB  49 8B CE                        mov rcx, r14
003D7DFE  E8 5D AF 4C 00                  call 0x1408a2d60
003D7E03  84 C0                           test al, al
003D7E05  0F 85 0C FA FF FF               jne 0x1403d7817
003D7E0B  44 8A C7                        mov r8b, dil
003D7E0E  33 D2                           xor edx, edx
003D7E10  49 8B CE                        mov rcx, r14
003D7E13  E8 48 AF 4C 00                  call 0x1408a2d60
003D7E18  84 C0                           test al, al
003D7E1A  0F 85 F7 F9 FF FF               jne 0x1403d7817
003D7E20  41 8B 16                        mov edx, dword ptr [r14]
003D7E23  48 83 C9 FF                     or rcx, 0xffffffffffffffff
003D7E27  E8 24 58 2D 00                  call 0x1406ad650
003D7E2C  E9 E6 F9 FF FF                  jmp 0x1403d7817
003D7E31  FA                              cli
003D7E32  49 8B CC                        mov rcx, r12
003D7E35  E8 C6 14 08 00                  call 0x140459300
003D7E3A  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003D7E43  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
003D7E4A  4D 85 C0                        test r8, r8
003D7E4D  0F 84 D5 1A 31 00               je 0x1406e9928
003D7E53  41 0F 0D 08                     prefetchw byte ptr [r8]
003D7E57  41 8B 00                        mov eax, dword ptr [r8]
003D7E5A  E9 B1 1A 31 00                  jmp 0x1406e9910
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiDispatchException(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned int v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned int v_stack_m1A4;
    unsigned __int8 v_stack_m1A7;
    unsigned __int64 v_stack_m1A8;
    unsigned __int8 v_stack_m1B0;
    unsigned __int8 v_stack_m1B8;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_mF8;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p28;

    v_rsp = (v_rsp) - (424);
    result = (*(unsigned __int64 *)(v_rip + 10694867)) ^ (v_stack_m1A8);
    v_stack_m48 = result;
    v_stack_m1A8 = a4;
    v_stack_m180 = a2;
    v_stack_m158 = a1;
    v_stack_m140 = a3;
    a2 = 0;
    result = memset(v_stack_m104, a2, 148, a4);
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m1A7 = 0;
    v_stack_m168 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m178 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    if (a5 != 0) goto loc_003D7838;
loc_003D76F2:
    v_stack_m1A4 = (unsigned int)((unsigned int)(0x10001FULL));
    v_rdi = 0;
    if (v_stack_m1A8 != 0) goto loc_003D7924;
    v_r15 = (unsigned int)(0x10001FULL);
    if ((*(unsigned __int8 *)(v_rip + 14852397)) != 0) { v_r15 = (unsigned int)((unsigned int)(0x10009FULL)); }
    v_stack_m1A4 = (unsigned int)(v_r15);
loc_003D771C:
loc_003D7726:
    result = RtlGetExtendedContextLength3((unsigned int)((unsigned int)(v_r15)), v_stack_m198, 0, v_rbx);
    if (((unsigned int)(v_stack_m198) + 15) <= ((unsigned int)(v_stack_m198))) {
    }
    result = ((unsigned int)(v_stack_m198) + 15) & (-16);
    result = _chkstk((unsigned int)((unsigned int)(v_r15)), v_stack_m198, (unsigned int)(v_stack_m198), v_rbx);
    v_rsp = (v_rsp) - (result);
    v_stack_m150 = v_stack_m1A8;
    if (v_stack_m1A8 != 0) goto loc_003D7D48;
loc_003D776E:
    result = RtlInitializeExtendedContext2(v_stack_m1A8, (unsigned int)((unsigned int)(v_r15)), v_stack_m188, 0);
    result = KeContextFromKframes(a3, v_stack_m180, v_stack_m1A8, 0);
    if ((*(unsigned int *)(a1)) == 0x80000003ULL) goto loc_003D7D57;
loc_003D77A4:
    result = KiPreprocessFault(a1, v_stack_m1A8, v_stack_m1A8, 0);
    if ((unsigned __int8)(result) != 0) goto loc_003D77F4;
    if ((unsigned __int8)(v_stack_m1A8) != 0) goto loc_003D787E;
    if (a5 == ((unsigned __int8)(v_stack_m1A8))) goto loc_003D79CA;
    v_stack_m1B0 = (unsigned __int8)(v_stack_m1A8);
    v_stack_m1B8 = (unsigned __int8)(v_stack_m1A8);
    result = KdTrap(a3, v_stack_m180, a1, v_stack_m1A8);
    if ((unsigned __int8)(result) == 0) goto loc_003D79B7;
loc_003D77F4:
    v_stack_m1B8 = (unsigned __int8)(v_stack_m1A8);
    result = KeContextToKframes(a3, v_stack_m180, v_stack_m1A8, (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 48)));
    if (v_stack_m1A7 != 0) goto loc_003D7E31;
loc_003D7817:
    a1 = (v_stack_m48) ^ (v_stack_m1A8);
    result = _security_check_cookie(a1, v_stack_m180, v_stack_m1A8, (unsigned int)(*(unsigned int *)(v_stack_m1A8 + 48)));
    return result;
loc_003D7838:
    if (v_stack_m180 == 0) goto loc_003D76F2;
    if ((*(unsigned __int64 *)(v_stack_m180 + 1600)) == 0) goto loc_003D76F2;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) - (0x10000002ULL));
    a1 = (unsigned int)((a1) - (1));
    *(unsigned int *)(a1) = 0xC0000005ULL;
loc_003D787E:
    v_stack_m190 = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1)) + 152);
    v_stack_m160 = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1)) + 152);
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m178 + 1532))))) == 0) goto loc_003D7C21;
loc_003D78A0:
    if (a5 == 0) goto loc_003D7DF5;
    v_stack_m1A0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    result = KdIsThisAKdTrap(a1, v_stack_m180, v_stack_m1A8, (unsigned int)(*(unsigned int *)(a1)));
    v_stack_m1A7 = (unsigned __int8)(result);
    if ((*(unsigned __int8 *)(v_rip + 12051402)) != 0) goto loc_003D7A0C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 776)) != 0) goto loc_003D7A0C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) == 0x80000033ULL) goto loc_003D7A0C;
loc_003D78F7:
    v_stack_p28 = 0;
    v_stack_p20 = (unsigned __int8)(v_stack_m1A8);
    result = KdTrap(a3, v_stack_m180, a1, (unsigned int)(*(unsigned int *)(a1)));
    if ((unsigned __int8)(result) == 0) goto loc_003D7DEC;
    goto loc_003D77F4;
loc_003D7924:
    if (((*(unsigned __int64 *)(v_rip + 12513793)) & (0x800000ULL)) == 0) goto loc_003D771C;
    v_stack_m1A4 = (unsigned int)((unsigned int)(0x10005FULL));
    if ((((unsigned __int8)(result)) & (2)) == 0) goto loc_003D771C;
    a1 = (*(unsigned __int64 *)(a3)) | (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1))));
    if (condition_is_above_or_equal) goto loc_003D7982;
    if (((*(unsigned int *)(v_stack_m180 + 1876)) & (0x4000ULL)) == 0) {
    }
    v_rdi = (a1) & (0xFFFFFFFFFFF9FFFFULL);
    if (((*(unsigned __int8 *)(a1 + 4)) & (128)) == 0) { v_rdi = a1; }
    result = PsWow64GetProcessMachine(v_stack_m180, v_stack_m180, a1, (unsigned int)(*(unsigned int *)(a1)));
    if (((unsigned __int16)(result)) != 332) goto loc_003D7726;
    v_rdi = (v_rdi) & (0xFFFFFFFFFFF9FFFFULL);
    goto loc_003D7726;
loc_003D79B7:
    result = RtlDispatchException(a1, (unsigned int)(*(unsigned int *)(a1)), a1, (unsigned int)(*(unsigned int *)(a1)));
    if ((unsigned __int8)(result) != 0) goto loc_003D77F4;
loc_003D79CA:
    v_stack_p28 = (unsigned __int8)(v_rdi);
    v_stack_p20 = 0;
    result = KdTrap(a3, (unsigned int)(0x10005FULL), a1, (unsigned int)(*(unsigned int *)(a1)));
    if ((unsigned __int8)(result) != 0) goto loc_003D77F4;
    v_stack_p20 = *(unsigned __int64 *)(a1 + 40);
    result = KeBugCheckEx(30, (int)(*(unsigned int *)(a1)), *(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)(a1 + 32));
loc_003D7A0C:
    if ((unsigned __int8)(result) != 0) goto loc_003D78F7;
loc_003D7A14:
    if (((unsigned int)(*(unsigned __int64 *)(a1 + 32))) == 0x80000033ULL) goto loc_003D7A33;
    a3 = 0;
    result = DbgkForwardException(a1, (unsigned __int8)(v_rdi), a3, *(unsigned __int64 *)(a1 + 32));
    if ((unsigned __int8)(result) != 0) goto loc_003D7817;
loc_003D7A33:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_003D7D20;
loc_003D7A57:
    v_stack_m108 = 0xC0000005ULL;
loc_003D7A69:
    v_stack_m170 = (unsigned int)(0x10005FULL);
    result = (unsigned int)(((unsigned int)(v_stack_m1A4)) & ((unsigned int)((unsigned int)(0x100040ULL))));
    v_stack_m1A0 = (unsigned int)(result);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x100040ULL)))) goto loc_003D7C7A;
loc_003D7A80:
    v_rdi = ((unsigned int)(0x10005FULL) - 40) & (-16);
    v_stack_m138 = v_rdi;
    v_stack_m130 = v_rdi - 160;
    v_stack_m128 = v_rdi - 160 - 32;
    v_stack_m120 = v_rdi - 160 - 32 - 1232;
    v_stack_m68 = (unsigned int)((unsigned int)(0xFFFFFB30ULL));
    a2 = (v_stack_m190) - (v_rdi - 160 - 32 - 1232);
    v_stack_m64 = (unsigned int)(a2);
    v_stack_m60 = (unsigned int)((unsigned int)(0xFFFFFB30ULL));
    v_stack_m5C = 0x4D0ULL;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x10005FULL)))) - ((unsigned int)(v_rdi - 160 - 32)));
    v_stack_m58 = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m190))) - ((unsigned int)((unsigned int)(0x10005FULL))));
    v_stack_m54 = (unsigned int)(result);
    result = ProbeForWrite(v_rdi - 160 - 32 - 1232, a2, 16, v_rdi - 160 - 32 - 1232);
    *(unsigned __int64 *)(v_rdi + 24) = v_stack_m190;
    *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)(v_stack_m150 + 248);
    result = KeCopyExceptionRecord(v_rdi - 160, a1, 16, v_rdi - 160 - 32 - 1232);
    if (v_stack_m1A0 == 0x100040ULL) {
        result = v_stack_m188;
        a1 = (int)(*(unsigned int *)(result + 16));
        a1 = (a1) + (result);
        *(unsigned __int64 *)((unsigned int)(0x10005FULL)) = v_xmm0;
        *(unsigned __int64 *)((unsigned int)(0x10005FULL) + 16) = v_xmm1;
        *(unsigned __int64 *)((unsigned int)(0x10005FULL) + 32) = v_xmm0;
        *(unsigned __int64 *)((unsigned int)(0x10005FULL) + 48) = v_xmm1;
    }
    v_stack_p20 = v_stack_m188;
    result = RtlpCopyExtendedContext(1, v_rdi - 160 - 32, v_stack_m68, (unsigned int)(v_stack_m1A4));
    *(unsigned __int64 *)(v_rdi - 160 - 32) = v_xmm0;
    *(unsigned __int64 *)(v_rdi - 160 - 32 + 16) = v_xmm1;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m168 + 486)) - (1));
    *(unsigned __int16 *)(v_stack_m168 + 486) = (unsigned __int16)(result);
    v_stack_m19C = 1;
    result = KePopulateContinuationContext(*(unsigned __int64 *)(a3 + 360), v_rdi - 160 - 32, v_stack_m68, v_stack_m168);
    *(unsigned __int64 *)(a3 + 384) = v_rdi - 160 - 32 - 1232;
    *(unsigned __int16 *)(a3 + 368) = (unsigned __int16)(1 + 50);
    *(unsigned __int64 *)(a3 + 360) = *(unsigned __int64 *)(v_rip + 12515501);
    result = KiSetupForInstrumentationReturn(0, v_rdi - 160 - 32, v_stack_m68, v_stack_m168);
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m168 + 486)) + (1));
    *(unsigned __int16 *)(v_stack_m168 + 486) = (unsigned __int16)(result);
    if (condition_is_not_equal) goto loc_003D7C99;
    if ((*(unsigned __int64 *)(v_stack_m168 + 152)) == (v_stack_m168 + 152)) goto loc_003D7C99;
    result = KiCheckForKernelApcDelivery(0, v_rdi - 160 - 32, v_stack_m68, v_stack_m168);
    goto loc_003D7C99;
loc_003D7C21:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) != 0) goto loc_003D7D9F;
loc_003D7C3F:
    result = (unsigned __int16)((*(unsigned __int16 *)(1 + 56)) & ((unsigned __int16)((unsigned int)(0xFFF8ULL))));
    if (((unsigned __int16)(result)) != 32) goto loc_003D78A0;
    *(unsigned int *)(a1) = 0x4000001EULL;
loc_003D7C7A:
    v_r15 = (v_stack_m190) - ((unsigned int)(*(unsigned int *)(v_stack_m188 + 20)));
    v_stack_m170 = v_r15;
    v_r15 = (v_r15) & (-64);
    v_stack_m170 = v_r15;
    goto loc_003D7A80;
loc_003D7C99:
    goto loc_003D7817;
loc_003D7D20:
loc_003D7D25:
    if (condition_is_not_equal) goto loc_003D7D25;
    if (condition_is_above_or_equal) goto loc_003D7A57;
    result = KiRemoveSystemWorkPriorityKick(v_stack_m68, v_rdi - 160 - 32, v_stack_m68, v_stack_m168);
    goto loc_003D7A57;
loc_003D7D48:
    a2 = 0;
    result = memset(1, a2, v_stack_m68, v_stack_m168);
    goto loc_003D776E;
loc_003D7D57:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12513180)))) & (2)) == 0) goto loc_003D77A4;
    result = KiTpHandleTrap(a1, 1, v_stack_m1A8, a5);
    if ((unsigned __int8)(result) != 0) goto loc_003D77F4;
    goto loc_003D77A4;
loc_003D7D9F:
    if ((*(unsigned int *)(a1)) != 0x80000002ULL) goto loc_003D7C3F;
    if (((*(unsigned int *)(a3 + 376)) & (0x40000ULL)) == 0) goto loc_003D7C3F;
loc_003D7DEC:
    goto loc_003D7A14;
loc_003D7DF5:
    result = DbgkForwardException(a1, (unsigned __int8)(v_rdi - 160 - 32), (unsigned __int8)(v_rdi - 160 - 32), (unsigned int)(v_stack_m1A0));
    if ((unsigned __int8)(result) != 0) goto loc_003D7817;
    a2 = 0;
    result = DbgkForwardException(a1, a2, (unsigned __int8)(v_rdi - 160 - 32), (unsigned int)(v_stack_m1A0));
    if ((unsigned __int8)(result) != 0) goto loc_003D7817;
    a1 = (a1) | (-1);
    result = ZwTerminateProcess(a1, (unsigned int)(*(unsigned int *)(a1)), (unsigned __int8)(v_rdi - 160 - 32), (unsigned int)(v_stack_m1A0));
    goto loc_003D7817;
loc_003D7E31:
    result = KiSetupForInstrumentationReturn(0, (unsigned int)(*(unsigned int *)(a1)), (unsigned __int8)(v_rdi - 160 - 32), (unsigned int)(v_stack_m1A0));
}
```

## 5. (Beta) C Style

```c
int64_t KiDispatchException(void *Arg1, int64_t Arg2, void *Arg3, uint8_t Arg4, uint8_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint32_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint32_t v_stack_m1A4;
    uint8_t v_stack_m1A7;
    uint64_t v_stack_m1A8;
    uint8_t v_stack_m1B0;
    uint8_t v_stack_m1B8;
    uint64_t v_stack_m30;
    uint64_t v_stack_m48;
    uint32_t v_stack_m54;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_mF8;
    uint8_t v_stack_p20;
    uint8_t v_stack_p28;

    local_rsp = (local_rsp) - (424);
    result = (*(uint64_t *)(v_rip + 0xA330D3)) ^ (v_stack_m1A8);
    v_stack_m48 = result;
    v_stack_m1A8 = Arg4;
    v_stack_m180 = Arg2;
    v_stack_m158 = Arg1;
    v_stack_m140 = Arg3;
    Arg2 = 0;
    result = memset(v_stack_m104, Arg2, 148, Arg4);
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m1A7 = 0;
    v_stack_m168 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m178 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    if (Arg5 != 0) goto loc_003D7838;
loc_003D76F2:
    v_stack_m1A4 = (uint32_t)((uint32_t)(0x10001FULL));
    local_rdi = 0;
    if (v_stack_m1A8 != 0) goto loc_003D7924;
    local_r15 = (uint32_t)(0x10001FULL);
    if ((*(uint8_t *)(v_rip + 0xE2A12D)) != 0) { local_r15 = (uint32_t)((uint32_t)(0x10009FULL)); }
    v_stack_m1A4 = (uint32_t)(local_r15);
loc_003D771C:
loc_003D7726:
    result = RtlGetExtendedContextLength3((uint32_t)((uint32_t)(local_r15)), v_stack_m198, 0, local_rbx);
    if (((uint32_t)(v_stack_m198) + 15) <= ((uint32_t)(v_stack_m198))) {
    }
    result = ((uint32_t)(v_stack_m198) + 15) & (-16);
    result = _chkstk((uint32_t)((uint32_t)(local_r15)), v_stack_m198, (uint32_t)(v_stack_m198), local_rbx);
    local_rsp = (local_rsp) - (result);
    v_stack_m150 = v_stack_m1A8;
    if (v_stack_m1A8 != 0) goto loc_003D7D48;
loc_003D776E:
    result = RtlInitializeExtendedContext2(v_stack_m1A8, (uint32_t)((uint32_t)(local_r15)), v_stack_m188, 0);
    result = KeContextFromKframes(Arg3, v_stack_m180, v_stack_m1A8, 0);
    if ((*(uint32_t *)(arg1)) == 0x80000003ULL) goto loc_003D7D57;
loc_003D77A4:
    result = KiPreprocessFault(Arg1, v_stack_m1A8, v_stack_m1A8, 0);
    if ((uint8_t)(result) != 0) goto loc_003D77F4;
    if ((uint8_t)(v_stack_m1A8) != 0) goto loc_003D787E;
    if (Arg5 == ((uint8_t)(v_stack_m1A8))) goto loc_003D79CA;
    v_stack_m1B0 = (uint8_t)(v_stack_m1A8);
    v_stack_m1B8 = (uint8_t)(v_stack_m1A8);
    result = KdTrap(Arg3, v_stack_m180, Arg1, v_stack_m1A8);
    if ((uint8_t)(result) == 0) goto loc_003D79B7;
loc_003D77F4:
    v_stack_m1B8 = (uint8_t)(v_stack_m1A8);
    result = KeContextToKframes(Arg3, v_stack_m180, v_stack_m1A8, (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x30)));
    if (v_stack_m1A7 != 0) goto loc_003D7E31;
loc_003D7817:
    Arg1 = (v_stack_m48) ^ (v_stack_m1A8);
    result = _security_check_cookie(Arg1, v_stack_m180, v_stack_m1A8, (uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x30)));
    return result;
loc_003D7838:
    if (v_stack_m180 == 0) goto loc_003D76F2;
    if ((*(uint64_t *)(v_stack_m180 + 0x640)) == 0) goto loc_003D76F2;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) - (0x10000002ULL));
    Arg1 = (uint32_t)((Arg1) - (1));
    *(uint32_t *)(arg1) = 0xC0000005ULL;
loc_003D787E:
    v_stack_m190 = *(uint64_t *)((uint32_t)(*(uint32_t *)(arg1)) + 0x98);
    v_stack_m160 = *(uint64_t *)((uint32_t)(*(uint32_t *)(arg1)) + 0x98);
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m178 + 0x5FC))))) == 0) goto loc_003D7C21;
loc_003D78A0:
    if (Arg5 == 0) goto loc_003D7DF5;
    v_stack_m1A0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    result = KdIsThisAKdTrap(Arg1, v_stack_m180, v_stack_m1A8, (uint32_t)(*(uint32_t *)(arg1)));
    v_stack_m1A7 = (uint8_t)(result);
    if ((*(uint8_t *)(v_rip + 0xB7E3CA)) != 0) goto loc_003D7A0C;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x308)) != 0) goto loc_003D7A0C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) == 0x80000033ULL) goto loc_003D7A0C;
loc_003D78F7:
    v_stack_p28 = 0;
    v_stack_p20 = (uint8_t)(v_stack_m1A8);
    result = KdTrap(Arg3, v_stack_m180, Arg1, (uint32_t)(*(uint32_t *)(arg1)));
    if ((uint8_t)(result) == 0) goto loc_003D7DEC;
    goto loc_003D77F4;
loc_003D7924:
    if (((*(uint64_t *)(v_rip + 0xBEF201)) & (0x800000ULL)) == 0) goto loc_003D771C;
    v_stack_m1A4 = (uint32_t)((uint32_t)(0x10005FULL));
    if ((((uint8_t)(result)) & (2)) == 0) goto loc_003D771C;
    Arg1 = (*(uint64_t *)(arg3)) | (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg1))));
    if (condition_is_above_or_equal) goto loc_003D7982;
    if (((*(uint32_t *)(v_stack_m180 + 0x754)) & (0x4000ULL)) == 0) {
    }
    local_rdi = (Arg1) & (0xFFFFFFFFFFF9FFFFULL);
    if (((*(uint8_t *)(arg1 + 0x4)) & (128)) == 0) { local_rdi = Arg1; }
    result = PsWow64GetProcessMachine(v_stack_m180, v_stack_m180, Arg1, (uint32_t)(*(uint32_t *)(arg1)));
    if (((uint16_t)(result)) != 332) goto loc_003D7726;
    local_rdi = (local_rdi) & (0xFFFFFFFFFFF9FFFFULL);
    goto loc_003D7726;
loc_003D79B7:
    result = RtlDispatchException(Arg1, (uint32_t)(*(uint32_t *)(arg1)), Arg1, (uint32_t)(*(uint32_t *)(arg1)));
    if ((uint8_t)(result) != 0) goto loc_003D77F4;
loc_003D79CA:
    v_stack_p28 = (uint8_t)(local_rdi);
    v_stack_p20 = 0;
    result = KdTrap(Arg3, (uint32_t)(0x10005FULL), Arg1, (uint32_t)(*(uint32_t *)(arg1)));
    if ((uint8_t)(result) != 0) goto loc_003D77F4;
    v_stack_p20 = *(uint64_t *)(arg1 + 0x28);
    result = KeBugCheckEx(30, (int32_t)(*(uint32_t *)(arg1)), *(uint64_t *)(arg1 + 0x10), *(uint64_t *)(arg1 + 0x20));
loc_003D7A0C:
    if ((uint8_t)(result) != 0) goto loc_003D78F7;
loc_003D7A14:
    if (((uint32_t)(*(uint64_t *)(arg1 + 0x20))) == 0x80000033ULL) goto loc_003D7A33;
    Arg3 = 0;
    result = DbgkForwardException(Arg1, (uint8_t)(local_rdi), Arg3, *(uint64_t *)(arg1 + 0x20));
    if ((uint8_t)(result) != 0) goto loc_003D7817;
loc_003D7A33:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_003D7D20;
loc_003D7A57:
    v_stack_m108 = 0xC0000005ULL;
loc_003D7A69:
    v_stack_m170 = (uint32_t)(0x10005FULL);
    result = (uint32_t)(((uint32_t)(v_stack_m1A4)) & ((uint32_t)((uint32_t)(0x100040ULL))));
    v_stack_m1A0 = (uint32_t)(result);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x100040ULL)))) goto loc_003D7C7A;
loc_003D7A80:
    local_rdi = ((uint32_t)(0x10005FULL) - 40) & (-16);
    v_stack_m138 = local_rdi;
    v_stack_m130 = local_rdi - 160;
    v_stack_m128 = local_rdi - 160 - 32;
    v_stack_m120 = local_rdi - 160 - 32 - 1232;
    v_stack_m68 = (uint32_t)((uint32_t)(0xFFFFFB30ULL));
    Arg2 = (v_stack_m190) - (local_rdi - 160 - 32 - 1232);
    v_stack_m64 = (uint32_t)(Arg2);
    v_stack_m60 = (uint32_t)((uint32_t)(0xFFFFFB30ULL));
    v_stack_m5C = 0x4D0ULL;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x10005FULL)))) - ((uint32_t)(local_rdi - 160 - 32)));
    v_stack_m58 = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m190))) - ((uint32_t)((uint32_t)(0x10005FULL))));
    v_stack_m54 = (uint32_t)(result);
    result = ProbeForWrite(local_rdi - 160 - 32 - 1232, Arg2, 16, local_rdi - 160 - 32 - 1232);
    *(uint64_t *)(local_rdi + 0x18) = v_stack_m190;
    *(uint64_t *)(local_rdi) = *(uint64_t *)(v_stack_m150 + 0xF8);
    result = KeCopyExceptionRecord(local_rdi - 160, Arg1, 16, local_rdi - 160 - 32 - 1232);
    if (v_stack_m1A0 == 0x100040ULL) {
        result = v_stack_m188;
        Arg1 = (int32_t)(*(uint32_t *)(result + 0x10));
        Arg1 = (Arg1) + (result);
        *(uint64_t *)((uint32_t)(0x10005FULL)) = v_xmm0;
        *(uint64_t *)((uint32_t)(0x10005FULL) + 0x10) = v_xmm1;
        *(uint64_t *)((uint32_t)(0x10005FULL) + 0x20) = v_xmm0;
        *(uint64_t *)((uint32_t)(0x10005FULL) + 0x30) = v_xmm1;
    }
    v_stack_p20 = v_stack_m188;
    result = RtlpCopyExtendedContext(1, local_rdi - 160 - 32, v_stack_m68, (uint32_t)(v_stack_m1A4));
    *(uint64_t *)(local_rdi - 0xA0 - 0x20) = v_xmm0;
    *(uint64_t *)(local_rdi - 0xA0 - 0x20 + 0x10) = v_xmm1;
    result = (uint16_t)((*(uint16_t *)(v_stack_m168 + 0x1E6)) - (1));
    *(uint16_t *)(v_stack_m168 + 0x1E6) = (uint16_t)(result);
    v_stack_m19C = 1;
    result = KePopulateContinuationContext(*(uint64_t *)(arg3 + 0x168), local_rdi - 160 - 32, v_stack_m68, v_stack_m168);
    *(uint64_t *)(arg3 + 0x180) = local_rdi - 160 - 32 - 1232;
    *(uint16_t *)(arg3 + 0x170) = (uint16_t)(1 + 50);
    *(uint64_t *)(arg3 + 0x168) = *(uint64_t *)(v_rip + 0xBEF8AD);
    result = KiSetupForInstrumentationReturn(0, local_rdi - 160 - 32, v_stack_m68, v_stack_m168);
    result = (uint16_t)((*(uint16_t *)(v_stack_m168 + 0x1E6)) + (1));
    *(uint16_t *)(v_stack_m168 + 0x1E6) = (uint16_t)(result);
    if (condition_is_not_equal) goto loc_003D7C99;
    if ((*(uint64_t *)(v_stack_m168 + 0x98)) == (v_stack_m168 + 152)) goto loc_003D7C99;
    result = KiCheckForKernelApcDelivery(0, local_rdi - 160 - 32, v_stack_m68, v_stack_m168);
    goto loc_003D7C99;
loc_003D7C21:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) != 0) goto loc_003D7D9F;
loc_003D7C3F:
    result = (uint16_t)((*(uint16_t *)(1 + 0x38)) & ((uint16_t)((uint32_t)(0xFFF8ULL))));
    if (((uint16_t)(result)) != 32) goto loc_003D78A0;
    *(uint32_t *)(arg1) = 0x4000001EULL;
loc_003D7C7A:
    local_r15 = (v_stack_m190) - ((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x14)));
    v_stack_m170 = local_r15;
    local_r15 = (local_r15) & (-64);
    v_stack_m170 = local_r15;
    goto loc_003D7A80;
loc_003D7C99:
    goto loc_003D7817;
loc_003D7D20:
loc_003D7D25:
    if (condition_is_not_equal) goto loc_003D7D25;
    if (condition_is_above_or_equal) goto loc_003D7A57;
    result = KiRemoveSystemWorkPriorityKick(v_stack_m68, local_rdi - 160 - 32, v_stack_m68, v_stack_m168);
    goto loc_003D7A57;
loc_003D7D48:
    Arg2 = 0;
    result = memset(1, Arg2, v_stack_m68, v_stack_m168);
    goto loc_003D776E;
loc_003D7D57:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBEEF9C)))) & (2)) == 0) goto loc_003D77A4;
    result = KiTpHandleTrap(Arg1, 1, v_stack_m1A8, Arg5);
    if ((uint8_t)(result) != 0) goto loc_003D77F4;
    goto loc_003D77A4;
loc_003D7D9F:
    if ((*(uint32_t *)(arg1)) != 0x80000002ULL) goto loc_003D7C3F;
    if (((*(uint32_t *)(arg3 + 0x178)) & (0x40000ULL)) == 0) goto loc_003D7C3F;
loc_003D7DEC:
    goto loc_003D7A14;
loc_003D7DF5:
    result = DbgkForwardException(Arg1, (uint8_t)(local_rdi - 160 - 32), (uint8_t)(local_rdi - 160 - 32), (uint32_t)(v_stack_m1A0));
    if ((uint8_t)(result) != 0) goto loc_003D7817;
    Arg2 = 0;
    result = DbgkForwardException(Arg1, Arg2, (uint8_t)(local_rdi - 160 - 32), (uint32_t)(v_stack_m1A0));
    if ((uint8_t)(result) != 0) goto loc_003D7817;
    Arg1 = (Arg1) | (-1);
    result = ZwTerminateProcess(Arg1, (uint32_t)(*(uint32_t *)(arg1)), (uint8_t)(local_rdi - 160 - 32), (uint32_t)(v_stack_m1A0));
    goto loc_003D7817;
loc_003D7E31:
    result = KiSetupForInstrumentationReturn(0, (uint32_t)(*(uint32_t *)(arg1)), (uint8_t)(local_rdi - 160 - 32), (uint32_t)(v_stack_m1A0));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg3` | `+ 0x168` | `64` | `R` |
| `Arg3` | `+ 0x168` | `64` | `R/W` |
| `Arg3` | `+ 0x168` | `64` | `W` |
| `Arg3` | `+ 0x170` | `16` | `W` |
| `Arg3` | `+ 0x178` | `32` | `R` |
| `Arg3` | `+ 0x178` | `32` | `R/W` |
| `Arg3` | `+ 0x180` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D7650&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
