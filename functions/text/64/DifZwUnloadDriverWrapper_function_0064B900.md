# DifZwUnloadDriverWrapper

- RVA: `0x0064B900`–`0x0064BA5D` (길이 `349` bytes)
- VA: `0x000000014064B900`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `349/349` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064B92D` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064B955` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0064B983` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064B9AA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064B9C3` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064B9CB` → [ZwUnloadDriver](../6B/ZwUnloadDriver_function_006B0C10.md) (function, `0x006B0C10`)
- `0x0064B9F8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064BA1F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064BA38` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064B967` → RVA `0x00F048B8` (`.data`; read)
- `0x0064B970` → RVA `0x00F04980` (`.data`; read)
- `0x0064B97C` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064B900  4C 8B DC                        mov r11, rsp
0064B903  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0064B907  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0064B90B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0064B90F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0064B913  41 56                           push r14
0064B915  48 83 EC 40                     sub rsp, 0x40
0064B919  33 C0                           xor eax, eax
0064B91B  0F 57 C0                        xorps xmm0, xmm0
0064B91E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0064B923  48 8B E9                        mov rbp, rcx
0064B926  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0064B92A  8D 48 04                        lea ecx, [rax + 4]
0064B92D  E8 02 A1 E4 FF                  call 0x140495a34
0064B932  48 8B F0                        mov rsi, rax
0064B935  48 85 C0                        test rax, rax
0064B938  0F 84 8A 00 00 00               je 0x14064b9c8
0064B93E  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0064B941  A8 18                           test al, 0x18
0064B943  74 0C                           je 0x14064b951
0064B945  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0064B94A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0064B94F  EB 0E                           jmp 0x14064b95f
0064B951  84 C1                           test cl, al
0064B953  74 0A                           je 0x14064b95f
0064B955  E8 AE 82 E8 FF                  call 0x1404d3c08
0064B95A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0064B95F  40 32 FF                        xor dil, dil
0064B962  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0064B967  40 38 3D 4A 8F 8B 00            cmp byte ptr [rip + 0x8b8f4a], dil
0064B96E  75 0C                           jne 0x14064b97c
0064B970  F7 05 06 90 8B 00 00 08 00 00   test dword ptr [rip + 0x8b9006], 0x800
0064B97A  74 13                           je 0x14064b98f
0064B97C  48 8D 0D FD 84 8B 00            lea rcx, [rip + 0x8b84fd]
0064B983  E8 98 AC BC FF                  call 0x140216620
0064B988  40 8A F8                        mov dil, al
0064B98B  84 C0                           test al, al
0064B98D  74 39                           je 0x14064b9c8
0064B98F  4C 8D 76 20                     lea r14, [rsi + 0x20]
0064B993  49 8B 1E                        mov rbx, qword ptr [r14]
0064B996  EB 1A                           jmp 0x14064b9b2
0064B998  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064B99C  48 85 C0                        test rax, rax
0064B99F  74 0E                           je 0x14064b9af
0064B9A1  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064B9A5  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0064B9AA  E8 21 F1 06 00                  call 0x1406baad0
0064B9AF  48 8B 1B                        mov rbx, qword ptr [rbx]
0064B9B2  49 3B DE                        cmp rbx, r14
0064B9B5  75 E1                           jne 0x14064b998
0064B9B7  40 84 FF                        test dil, dil
0064B9BA  74 0C                           je 0x14064b9c8
0064B9BC  48 8D 0D BD 84 8B 00            lea rcx, [rip + 0x8b84bd]
0064B9C3  E8 B8 E4 CF FF                  call 0x140349e80
0064B9C8  48 8B CD                        mov rcx, rbp
0064B9CB  E8 40 52 06 00                  call 0x1406b0c10
0064B9D0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0064B9D4  48 85 F6                        test rsi, rsi
0064B9D7  74 64                           je 0x14064ba3d
0064B9D9  40 32 FF                        xor dil, dil
0064B9DC  40 38 3D D5 8E 8B 00            cmp byte ptr [rip + 0x8b8ed5], dil
0064B9E3  75 0C                           jne 0x14064b9f1
0064B9E5  F7 05 91 8F 8B 00 00 08 00 00   test dword ptr [rip + 0x8b8f91], 0x800
0064B9EF  74 13                           je 0x14064ba04
0064B9F1  48 8D 0D 88 84 8B 00            lea rcx, [rip + 0x8b8488]
0064B9F8  E8 23 AC BC FF                  call 0x140216620
0064B9FD  40 8A F8                        mov dil, al
0064BA00  84 C0                           test al, al
0064BA02  74 39                           je 0x14064ba3d
0064BA04  48 83 C6 30                     add rsi, 0x30
0064BA08  48 8B 1E                        mov rbx, qword ptr [rsi]
0064BA0B  EB 1A                           jmp 0x14064ba27
0064BA0D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064BA11  48 85 C0                        test rax, rax
0064BA14  74 0E                           je 0x14064ba24
0064BA16  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064BA1A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0064BA1F  E8 AC F0 06 00                  call 0x1406baad0
0064BA24  48 8B 1B                        mov rbx, qword ptr [rbx]
0064BA27  48 3B DE                        cmp rbx, rsi
0064BA2A  75 E1                           jne 0x14064ba0d
0064BA2C  40 84 FF                        test dil, dil
0064BA2F  74 0C                           je 0x14064ba3d
0064BA31  48 8D 0D 48 84 8B 00            lea rcx, [rip + 0x8b8448]
0064BA38  E8 43 E4 CF FF                  call 0x140349e80
0064BA3D  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0064BA41  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0064BA46  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0064BA4B  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0064BA50  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0064BA55  48 83 C4 40                     add rsp, 0x40
0064BA59  41 5E                           pop r14
0064BA5B  C3                              ret
0064BA5C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwUnloadDriverWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(result + 4, a2, a3, a4);
    if (result == 0) goto loc_0064B9C8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0064B951;
    v_stack_m28 = v_stack_p0;
    goto loc_0064B95F;
loc_0064B951:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)(v_stack_p0)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12))))) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9146186)) != 0) goto loc_0064B97C;
    if (((*(unsigned int *)(v_rip + 9146374)) & (0x800ULL)) == 0) goto loc_0064B98F;
loc_0064B97C:
    result = ExAcquireRundownProtection(v_rip + 9143549, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064B9C8;
loc_0064B98F:
    goto loc_0064B9B2;
loc_0064B998:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064B9B2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064B998;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9143485;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwUnloadDriver(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0064BA3D;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9146069)) != 0) goto loc_0064B9F1;
    if (((*(unsigned int *)(v_rip + 9146257)) & (0x800ULL)) == 0) goto loc_0064BA04;
loc_0064B9F1:
    result = ExAcquireRundownProtection(v_rip + 9143432, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064BA3D;
loc_0064BA04:
    v_rsi = (result) + (48);
    goto loc_0064BA27;
loc_0064BA0D:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064BA27:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0064BA0D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9143368;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwUnloadDriverWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(result + 4, a2, a3, a4);
    if (result == 0) goto loc_0064B9C8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0064B951;
    v_stack_m28 = v_stack_p0;
    goto loc_0064B95F;
loc_0064B951:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)(v_stack_p0)) & ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC))))) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8B8F4A)) != 0) goto loc_0064B97C;
    if (((*(uint32_t *)(v_rip + 0x8B9006)) & (0x800ULL)) == 0) goto loc_0064B98F;
loc_0064B97C:
    result = ExAcquireRundownProtection(v_rip + 9143549, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064B9C8;
loc_0064B98F:
    goto loc_0064B9B2;
loc_0064B998:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0064B9B2:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064B998;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9143485;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ZwUnloadDriver(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0064BA3D;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8B8ED5)) != 0) goto loc_0064B9F1;
    if (((*(uint32_t *)(v_rip + 0x8B8F91)) & (0x800ULL)) == 0) goto loc_0064BA04;
loc_0064B9F1:
    result = ExAcquireRundownProtection(v_rip + 9143432, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064BA3D;
loc_0064BA04:
    local_rsi = (result) + (48);
    goto loc_0064BA27;
loc_0064BA0D:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0064BA27:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0064BA0D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9143368;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064B900&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064B900[BB_0064B900]
  bb_0064B93E[BB_0064B93E]
  bb_0064B945[BB_0064B945]
  bb_0064B951[BB_0064B951]
  bb_0064B955[BB_0064B955]
  bb_0064B95F[BB_0064B95F]
  bb_0064B970[BB_0064B970]
  bb_0064B97C[BB_0064B97C]
  bb_0064B98F[BB_0064B98F]
  bb_0064B998[BB_0064B998]
  bb_0064B9A1[BB_0064B9A1]
  bb_0064B9AF[BB_0064B9AF]
  bb_0064B9B2[BB_0064B9B2]
  bb_0064B9B7[BB_0064B9B7]
  bb_0064B9BC[BB_0064B9BC]
  bb_0064B9C8[BB_0064B9C8]
  bb_0064B9D9[BB_0064B9D9]
  bb_0064B9E5[BB_0064B9E5]
  bb_0064B9F1[BB_0064B9F1]
  bb_0064BA04[BB_0064BA04]
  bb_0064BA0D[BB_0064BA0D]
  bb_0064BA16[BB_0064BA16]
  bb_0064BA24[BB_0064BA24]
  bb_0064BA27[BB_0064BA27]
  bb_0064BA2C[BB_0064BA2C]
  bb_0064BA31[BB_0064BA31]
  bb_0064BA3D[BB_0064BA3D]
  bb_0064BA5C[BB_0064BA5C]
  bb_0064B900 -->|branch| bb_0064B9C8
  bb_0064B900 -->|fallthrough| bb_0064B93E
  bb_0064B93E -->|branch| bb_0064B951
  bb_0064B93E -->|fallthrough| bb_0064B945
  bb_0064B945 -->|branch| bb_0064B95F
  bb_0064B951 -->|branch| bb_0064B95F
  bb_0064B951 -->|fallthrough| bb_0064B955
  bb_0064B955 -->|flow| bb_0064B95F
  bb_0064B95F -->|branch| bb_0064B97C
  bb_0064B95F -->|fallthrough| bb_0064B970
  bb_0064B970 -->|branch| bb_0064B98F
  bb_0064B970 -->|fallthrough| bb_0064B97C
  bb_0064B97C -->|branch| bb_0064B9C8
  bb_0064B97C -->|fallthrough| bb_0064B98F
  bb_0064B98F -->|branch| bb_0064B9B2
  bb_0064B998 -->|branch| bb_0064B9AF
  bb_0064B998 -->|fallthrough| bb_0064B9A1
  bb_0064B9A1 -->|flow| bb_0064B9AF
  bb_0064B9AF -->|flow| bb_0064B9B2
  bb_0064B9B2 -->|branch| bb_0064B998
  bb_0064B9B2 -->|fallthrough| bb_0064B9B7
  bb_0064B9B7 -->|branch| bb_0064B9C8
  bb_0064B9B7 -->|fallthrough| bb_0064B9BC
  bb_0064B9BC -->|flow| bb_0064B9C8
  bb_0064B9C8 -->|branch| bb_0064BA3D
  bb_0064B9C8 -->|fallthrough| bb_0064B9D9
  bb_0064B9D9 -->|branch| bb_0064B9F1
  bb_0064B9D9 -->|fallthrough| bb_0064B9E5
  bb_0064B9E5 -->|branch| bb_0064BA04
  bb_0064B9E5 -->|fallthrough| bb_0064B9F1
  bb_0064B9F1 -->|branch| bb_0064BA3D
  bb_0064B9F1 -->|fallthrough| bb_0064BA04
  bb_0064BA04 -->|branch| bb_0064BA27
  bb_0064BA0D -->|branch| bb_0064BA24
  bb_0064BA0D -->|fallthrough| bb_0064BA16
  bb_0064BA16 -->|flow| bb_0064BA24
  bb_0064BA24 -->|flow| bb_0064BA27
  bb_0064BA27 -->|branch| bb_0064BA0D
  bb_0064BA27 -->|fallthrough| bb_0064BA2C
  bb_0064BA2C -->|branch| bb_0064BA3D
  bb_0064BA2C -->|fallthrough| bb_0064BA31
  bb_0064BA31 -->|flow| bb_0064BA3D
```
