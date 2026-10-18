# DifRtlQueryRegistryValuesExWrapper

- RVA: `0x0063C290`–`0x0063C422` (길이 `402` bytes)
- VA: `0x000000014063C290`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2C24`
- 디코드: `116`개 명령, `402/402` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063C2CF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063C2F5` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063C337` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063C35D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063C376` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063C390` → [RtlQueryRegistryValuesEx](../../page/8C/RtlQueryRegistryValuesEx_function_008C8FF0.md) (function, `0x008C8FF0`)
- `0x0063C3BC` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063C3E2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063C3FB` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063C304` → RVA `0x00F048B8` (`.data`; read)
- `0x0063C324` → RVA `0x00F04980` (`.data`; read)
- `0x0063C330` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063C390` → [RtlQueryRegistryValuesEx](../../page/8C/RtlQueryRegistryValuesEx_function_008C8FF0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063C290  48 8B C4                        mov rax, rsp
0063C293  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0063C297  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063C29B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0063C29F  89 48 08                        mov dword ptr [rax + 8], ecx
0063C2A2  55                              push rbp
0063C2A3  41 54                           push r12
0063C2A5  41 55                           push r13
0063C2A7  41 56                           push r14
0063C2A9  41 57                           push r15
0063C2AB  48 8B EC                        mov rbp, rsp
0063C2AE  48 83 EC 60                     sub rsp, 0x60
0063C2B2  0F 57 C0                        xorps xmm0, xmm0
0063C2B5  B9 9D 00 00 00                  mov ecx, 0x9d
0063C2BA  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063C2BE  4D 8B F9                        mov r15, r9
0063C2C1  4D 8B E0                        mov r12, r8
0063C2C4  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063C2C8  4C 8B EA                        mov r13, rdx
0063C2CB  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0063C2CF  E8 60 97 E5 FF                  call 0x140495a34
0063C2D4  48 8B F0                        mov rsi, rax
0063C2D7  48 85 C0                        test rax, rax
0063C2DA  0F 84 9B 00 00 00               je 0x14063c37b
0063C2E0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063C2E3  A8 18                           test al, 0x18
0063C2E5  74 0A                           je 0x14063c2f1
0063C2E7  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063C2EB  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063C2EF  EB 0D                           jmp 0x14063c2fe
0063C2F1  A8 04                           test al, 4
0063C2F3  74 09                           je 0x14063c2fe
0063C2F5  E8 0E 79 E9 FF                  call 0x1404d3c08
0063C2FA  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063C2FE  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
0063C301  45 32 F6                        xor r14b, r14b
0063C304  44 38 35 AD 85 8C 00            cmp byte ptr [rip + 0x8c85ad], r14b
0063C30B  89 45 F8                        mov dword ptr [rbp - 8], eax
0063C30E  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0063C312  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0063C316  4C 89 6D F0                     mov qword ptr [rbp - 0x10], r13
0063C31A  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
0063C31E  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
0063C322  75 0C                           jne 0x14063c330
0063C324  F7 05 52 86 8C 00 00 08 00 00   test dword ptr [rip + 0x8c8652], 0x800
0063C32E  74 13                           je 0x14063c343
0063C330  48 8D 0D 49 7B 8C 00            lea rcx, [rip + 0x8c7b49]
0063C337  E8 E4 A2 BD FF                  call 0x140216620
0063C33C  44 8A F0                        mov r14b, al
0063C33F  84 C0                           test al, al
0063C341  74 38                           je 0x14063c37b
0063C343  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063C347  48 8B 1F                        mov rbx, qword ptr [rdi]
0063C34A  EB 19                           jmp 0x14063c365
0063C34C  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063C350  48 85 C0                        test rax, rax
0063C353  74 0D                           je 0x14063c362
0063C355  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063C359  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063C35D  E8 6E E7 07 00                  call 0x1406baad0
0063C362  48 8B 1B                        mov rbx, qword ptr [rbx]
0063C365  48 3B DF                        cmp rbx, rdi
0063C368  75 E2                           jne 0x14063c34c
0063C36A  45 84 F6                        test r14b, r14b
0063C36D  74 0C                           je 0x14063c37b
0063C36F  48 8D 0D 0A 7B 8C 00            lea rcx, [rip + 0x8c7b0a]
0063C376  E8 05 DB D0 FF                  call 0x140349e80
0063C37B  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0063C37F  4D 8B CF                        mov r9, r15
0063C382  8B 4D 30                        mov ecx, dword ptr [rbp + 0x30]
0063C385  4D 8B C4                        mov r8, r12
0063C388  49 8B D5                        mov rdx, r13
0063C38B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063C390  E8 5B CC 28 00                  call 0x1408c8ff0
0063C395  89 45 FC                        mov dword ptr [rbp - 4], eax
0063C398  48 85 F6                        test rsi, rsi
0063C39B  74 63                           je 0x14063c400
0063C39D  40 32 FF                        xor dil, dil
0063C3A0  40 38 3D 11 85 8C 00            cmp byte ptr [rip + 0x8c8511], dil
0063C3A7  75 0C                           jne 0x14063c3b5
0063C3A9  F7 05 CD 85 8C 00 00 08 00 00   test dword ptr [rip + 0x8c85cd], 0x800
0063C3B3  74 13                           je 0x14063c3c8
0063C3B5  48 8D 0D C4 7A 8C 00            lea rcx, [rip + 0x8c7ac4]
0063C3BC  E8 5F A2 BD FF                  call 0x140216620
0063C3C1  40 8A F8                        mov dil, al
0063C3C4  84 C0                           test al, al
0063C3C6  74 38                           je 0x14063c400
0063C3C8  48 83 C6 30                     add rsi, 0x30
0063C3CC  48 8B 1E                        mov rbx, qword ptr [rsi]
0063C3CF  EB 19                           jmp 0x14063c3ea
0063C3D1  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063C3D5  48 85 C0                        test rax, rax
0063C3D8  74 0D                           je 0x14063c3e7
0063C3DA  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063C3DE  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063C3E2  E8 E9 E6 07 00                  call 0x1406baad0
0063C3E7  48 8B 1B                        mov rbx, qword ptr [rbx]
0063C3EA  48 3B DE                        cmp rbx, rsi
0063C3ED  75 E2                           jne 0x14063c3d1
0063C3EF  40 84 FF                        test dil, dil
0063C3F2  74 0C                           je 0x14063c400
0063C3F4  48 8D 0D 85 7A 8C 00            lea rcx, [rip + 0x8c7a85]
0063C3FB  E8 80 DA D0 FF                  call 0x140349e80
0063C400  8B 45 FC                        mov eax, dword ptr [rbp - 4]
0063C403  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
0063C408  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0063C40C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0063C410  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0063C414  49 8B E3                        mov rsp, r11
0063C417  41 5F                           pop r15
0063C419  41 5E                           pop r14
0063C41B  41 5D                           pop r13
0063C41D  41 5C                           pop r12
0063C41F  5D                              pop rbp
0063C420  C3                              ret
0063C421  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifRtlQueryRegistryValuesExWrapper(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned int v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(157, a2, a3, a4);
    if (result == 0) goto loc_0063C37B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063C2F1;
    v_stack_m58 = v_stack_p0;
    goto loc_0063C2FE;
loc_0063C2F1:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m30 = (unsigned int)((unsigned int)(v_stack_p8));
    v_stack_m50 = a5;
    v_stack_m38 = a2;
    v_stack_m40 = a3;
    v_stack_m48 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9209261)) != 0) goto loc_0063C330;
    if (((*(unsigned int *)(v_rip + 9209426)) & (0x800ULL)) == 0) goto loc_0063C343;
loc_0063C330:
    result = ExAcquireRundownProtection(v_rip + 9206601, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063C37B;
loc_0063C343:
    goto loc_0063C365;
loc_0063C34C:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063C365:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063C34C;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9206538;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = a5;
    result = RtlQueryRegistryValuesEx((unsigned int)(v_stack_p8), a2, a3, a4);
    v_stack_m2C = (unsigned int)(result);
    if (result == 0) goto loc_0063C400;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9209105)) != 0) goto loc_0063C3B5;
    if (((*(unsigned int *)(v_rip + 9209293)) & (0x800ULL)) == 0) goto loc_0063C3C8;
loc_0063C3B5:
    result = ExAcquireRundownProtection(v_rip + 9206468, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063C400;
loc_0063C3C8:
    v_rsi = (result) + (48);
    goto loc_0063C3EA;
loc_0063C3D1:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063C3EA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063C3D1;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9206405;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m2C);
}
```

## 5. (Beta) C Style

```c
int64_t DifRtlQueryRegistryValuesExWrapper(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p0;
    uint32_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(157, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0063C37B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063C2F1;
    v_stack_m58 = v_stack_p0;
    goto loc_0063C2FE;
loc_0063C2F1:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m30 = (uint32_t)((uint32_t)(v_stack_p8));
    v_stack_m50 = Arg5;
    v_stack_m38 = Arg2;
    v_stack_m40 = Arg3;
    v_stack_m48 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C85AD)) != 0) goto loc_0063C330;
    if (((*(uint32_t *)(v_rip + 0x8C8652)) & (0x800ULL)) == 0) goto loc_0063C343;
loc_0063C330:
    result = ExAcquireRundownProtection(v_rip + 9206601, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063C37B;
loc_0063C343:
    goto loc_0063C365;
loc_0063C34C:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0063C365:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063C34C;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9206538;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = Arg5;
    result = RtlQueryRegistryValuesEx((uint32_t)(v_stack_p8), Arg2, Arg3, Arg4);
    v_stack_m2C = (uint32_t)(result);
    if (result == 0) goto loc_0063C400;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C8511)) != 0) goto loc_0063C3B5;
    if (((*(uint32_t *)(v_rip + 0x8C85CD)) & (0x800ULL)) == 0) goto loc_0063C3C8;
loc_0063C3B5:
    result = ExAcquireRundownProtection(v_rip + 9206468, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063C400;
loc_0063C3C8:
    local_rsi = (result) + (48);
    goto loc_0063C3EA;
loc_0063C3D1:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0063C3EA:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063C3D1;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9206405;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m2C);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063C290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063C290[BB_0063C290]
  bb_0063C2E0[BB_0063C2E0]
  bb_0063C2E7[BB_0063C2E7]
  bb_0063C2F1[BB_0063C2F1]
  bb_0063C2F5[BB_0063C2F5]
  bb_0063C2FE[BB_0063C2FE]
  bb_0063C324[BB_0063C324]
  bb_0063C330[BB_0063C330]
  bb_0063C343[BB_0063C343]
  bb_0063C34C[BB_0063C34C]
  bb_0063C355[BB_0063C355]
  bb_0063C362[BB_0063C362]
  bb_0063C365[BB_0063C365]
  bb_0063C36A[BB_0063C36A]
  bb_0063C36F[BB_0063C36F]
  bb_0063C37B[BB_0063C37B]
  bb_0063C39D[BB_0063C39D]
  bb_0063C3A9[BB_0063C3A9]
  bb_0063C3B5[BB_0063C3B5]
  bb_0063C3C8[BB_0063C3C8]
  bb_0063C3D1[BB_0063C3D1]
  bb_0063C3DA[BB_0063C3DA]
  bb_0063C3E7[BB_0063C3E7]
  bb_0063C3EA[BB_0063C3EA]
  bb_0063C3EF[BB_0063C3EF]
  bb_0063C3F4[BB_0063C3F4]
  bb_0063C400[BB_0063C400]
  bb_0063C421[BB_0063C421]
  bb_0063C290 -->|branch| bb_0063C37B
  bb_0063C290 -->|fallthrough| bb_0063C2E0
  bb_0063C2E0 -->|branch| bb_0063C2F1
  bb_0063C2E0 -->|fallthrough| bb_0063C2E7
  bb_0063C2E7 -->|branch| bb_0063C2FE
  bb_0063C2F1 -->|branch| bb_0063C2FE
  bb_0063C2F1 -->|fallthrough| bb_0063C2F5
  bb_0063C2F5 -->|flow| bb_0063C2FE
  bb_0063C2FE -->|branch| bb_0063C330
  bb_0063C2FE -->|fallthrough| bb_0063C324
  bb_0063C324 -->|branch| bb_0063C343
  bb_0063C324 -->|fallthrough| bb_0063C330
  bb_0063C330 -->|branch| bb_0063C37B
  bb_0063C330 -->|fallthrough| bb_0063C343
  bb_0063C343 -->|branch| bb_0063C365
  bb_0063C34C -->|branch| bb_0063C362
  bb_0063C34C -->|fallthrough| bb_0063C355
  bb_0063C355 -->|flow| bb_0063C362
  bb_0063C362 -->|flow| bb_0063C365
  bb_0063C365 -->|branch| bb_0063C34C
  bb_0063C365 -->|fallthrough| bb_0063C36A
  bb_0063C36A -->|branch| bb_0063C37B
  bb_0063C36A -->|fallthrough| bb_0063C36F
  bb_0063C36F -->|flow| bb_0063C37B
  bb_0063C37B -->|branch| bb_0063C400
  bb_0063C37B -->|fallthrough| bb_0063C39D
  bb_0063C39D -->|branch| bb_0063C3B5
  bb_0063C39D -->|fallthrough| bb_0063C3A9
  bb_0063C3A9 -->|branch| bb_0063C3C8
  bb_0063C3A9 -->|fallthrough| bb_0063C3B5
  bb_0063C3B5 -->|branch| bb_0063C400
  bb_0063C3B5 -->|fallthrough| bb_0063C3C8
  bb_0063C3C8 -->|branch| bb_0063C3EA
  bb_0063C3D1 -->|branch| bb_0063C3E7
  bb_0063C3D1 -->|fallthrough| bb_0063C3DA
  bb_0063C3DA -->|flow| bb_0063C3E7
  bb_0063C3E7 -->|flow| bb_0063C3EA
  bb_0063C3EA -->|branch| bb_0063C3D1
  bb_0063C3EA -->|fallthrough| bb_0063C3EF
  bb_0063C3EF -->|branch| bb_0063C400
  bb_0063C3EF -->|fallthrough| bb_0063C3F4
  bb_0063C3F4 -->|flow| bb_0063C400
```
