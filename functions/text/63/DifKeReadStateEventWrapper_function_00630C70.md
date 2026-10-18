# DifKeReadStateEventWrapper

- RVA: `0x00630C70`–`0x00630DCA` (길이 `346` bytes)
- VA: `0x0000000140630C70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `93`개 명령, `346/346` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00630C9F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00630CC7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00630CF5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00630D1C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00630D35` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00630D65` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00630D8C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00630DA5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00630CD9` → RVA `0x00F048B8` (`.data`; read)
- `0x00630CE2` → RVA `0x00F04980` (`.data`; read)
- `0x00630CEE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00630C70  4C 8B DC                        mov r11, rsp
00630C73  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00630C77  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00630C7B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00630C7F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00630C83  41 56                           push r14
00630C85  48 83 EC 40                     sub rsp, 0x40
00630C89  33 C0                           xor eax, eax
00630C8B  0F 57 C0                        xorps xmm0, xmm0
00630C8E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00630C93  48 8B E9                        mov rbp, rcx
00630C96  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00630C9A  B9 0D 01 00 00                  mov ecx, 0x10d
00630C9F  E8 90 4D E6 FF                  call 0x140495a34
00630CA4  48 8B F0                        mov rsi, rax
00630CA7  48 85 C0                        test rax, rax
00630CAA  0F 84 8A 00 00 00               je 0x140630d3a
00630CB0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00630CB3  A8 18                           test al, 0x18
00630CB5  74 0C                           je 0x140630cc3
00630CB7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00630CBC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00630CC1  EB 0E                           jmp 0x140630cd1
00630CC3  A8 04                           test al, 4
00630CC5  74 0A                           je 0x140630cd1
00630CC7  E8 3C 2F EA FF                  call 0x1404d3c08
00630CCC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00630CD1  40 32 FF                        xor dil, dil
00630CD4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00630CD9  40 38 3D D8 3B 8D 00            cmp byte ptr [rip + 0x8d3bd8], dil
00630CE0  75 0C                           jne 0x140630cee
00630CE2  F7 05 94 3C 8D 00 00 08 00 00   test dword ptr [rip + 0x8d3c94], 0x800
00630CEC  74 13                           je 0x140630d01
00630CEE  48 8D 0D 8B 31 8D 00            lea rcx, [rip + 0x8d318b]
00630CF5  E8 26 59 BE FF                  call 0x140216620
00630CFA  40 8A F8                        mov dil, al
00630CFD  84 C0                           test al, al
00630CFF  74 39                           je 0x140630d3a
00630D01  4C 8D 76 20                     lea r14, [rsi + 0x20]
00630D05  49 8B 1E                        mov rbx, qword ptr [r14]
00630D08  EB 1A                           jmp 0x140630d24
00630D0A  48 8D 43 F0                     lea rax, [rbx - 0x10]
00630D0E  48 85 C0                        test rax, rax
00630D11  74 0E                           je 0x140630d21
00630D13  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00630D17  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00630D1C  E8 AF 9D 08 00                  call 0x1406baad0
00630D21  48 8B 1B                        mov rbx, qword ptr [rbx]
00630D24  49 3B DE                        cmp rbx, r14
00630D27  75 E1                           jne 0x140630d0a
00630D29  40 84 FF                        test dil, dil
00630D2C  74 0C                           je 0x140630d3a
00630D2E  48 8D 0D 4B 31 8D 00            lea rcx, [rip + 0x8d314b]
00630D35  E8 46 91 D1 FF                  call 0x140349e80
00630D3A  8B 45 04                        mov eax, dword ptr [rbp + 4]
00630D3D  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00630D41  48 85 F6                        test rsi, rsi
00630D44  74 64                           je 0x140630daa
00630D46  40 32 FF                        xor dil, dil
00630D49  40 38 3D 68 3B 8D 00            cmp byte ptr [rip + 0x8d3b68], dil
00630D50  75 0C                           jne 0x140630d5e
00630D52  F7 05 24 3C 8D 00 00 08 00 00   test dword ptr [rip + 0x8d3c24], 0x800
00630D5C  74 13                           je 0x140630d71
00630D5E  48 8D 0D 1B 31 8D 00            lea rcx, [rip + 0x8d311b]
00630D65  E8 B6 58 BE FF                  call 0x140216620
00630D6A  40 8A F8                        mov dil, al
00630D6D  84 C0                           test al, al
00630D6F  74 39                           je 0x140630daa
00630D71  48 83 C6 30                     add rsi, 0x30
00630D75  48 8B 1E                        mov rbx, qword ptr [rsi]
00630D78  EB 1A                           jmp 0x140630d94
00630D7A  48 8D 43 F0                     lea rax, [rbx - 0x10]
00630D7E  48 85 C0                        test rax, rax
00630D81  74 0E                           je 0x140630d91
00630D83  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00630D87  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00630D8C  E8 3F 9D 08 00                  call 0x1406baad0
00630D91  48 8B 1B                        mov rbx, qword ptr [rbx]
00630D94  48 3B DE                        cmp rbx, rsi
00630D97  75 E1                           jne 0x140630d7a
00630D99  40 84 FF                        test dil, dil
00630D9C  74 0C                           je 0x140630daa
00630D9E  48 8D 0D DB 30 8D 00            lea rcx, [rip + 0x8d30db]
00630DA5  E8 D6 90 D1 FF                  call 0x140349e80
00630DAA  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00630DAE  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00630DB3  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00630DB8  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00630DBD  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00630DC2  48 83 C4 40                     add rsp, 0x40
00630DC6  41 5E                           pop r14
00630DC8  C3                              ret
00630DC9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeReadStateEventWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(269, a2, a3, a4);
    if (result == 0) goto loc_00630D3A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00630CC3;
    v_stack_m28 = v_stack_p0;
    goto loc_00630CD1;
loc_00630CC3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9255896)) != 0) goto loc_00630CEE;
    if (((*(unsigned int *)(v_rip + 9256084)) & (0x800ULL)) == 0) goto loc_00630D01;
loc_00630CEE:
    result = ExAcquireRundownProtection(v_rip + 9253259, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00630D3A;
loc_00630D01:
    goto loc_00630D24;
loc_00630D0A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00630D24:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00630D0A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9253195;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m18 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    if (result == 0) goto loc_00630DAA;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9255784)) != 0) goto loc_00630D5E;
    if (((*(unsigned int *)(v_rip + 9255972)) & (0x800ULL)) == 0) goto loc_00630D71;
loc_00630D5E:
    result = ExAcquireRundownProtection(v_rip + 9253147, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00630DAA;
loc_00630D71:
    v_rsi = (result) + (48);
    goto loc_00630D94;
loc_00630D7A:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00630D94:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00630D7A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9253083;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifKeReadStateEventWrapper(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

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
    result = DifGetAPIThunkContextById(269, a2, a3, a4);
    if (result == 0) goto loc_00630D3A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00630CC3;
    v_stack_m28 = v_stack_p0;
    goto loc_00630CD1;
loc_00630CC3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D3BD8)) != 0) goto loc_00630CEE;
    if (((*(uint32_t *)(v_rip + 0x8D3C94)) & (0x800ULL)) == 0) goto loc_00630D01;
loc_00630CEE:
    result = ExAcquireRundownProtection(v_rip + 9253259, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00630D3A;
loc_00630D01:
    goto loc_00630D24;
loc_00630D0A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00630D24:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00630D0A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9253195;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    v_stack_m18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    if (result == 0) goto loc_00630DAA;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D3B68)) != 0) goto loc_00630D5E;
    if (((*(uint32_t *)(v_rip + 0x8D3C24)) & (0x800ULL)) == 0) goto loc_00630D71;
loc_00630D5E:
    result = ExAcquireRundownProtection(v_rip + 9253147, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00630DAA;
loc_00630D71:
    local_rsi = (result) + (48);
    goto loc_00630D94;
loc_00630D7A:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00630D94:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00630D7A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9253083;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00630C70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00630C70[BB_00630C70]
  bb_00630CB0[BB_00630CB0]
  bb_00630CB7[BB_00630CB7]
  bb_00630CC3[BB_00630CC3]
  bb_00630CC7[BB_00630CC7]
  bb_00630CD1[BB_00630CD1]
  bb_00630CE2[BB_00630CE2]
  bb_00630CEE[BB_00630CEE]
  bb_00630D01[BB_00630D01]
  bb_00630D0A[BB_00630D0A]
  bb_00630D13[BB_00630D13]
  bb_00630D21[BB_00630D21]
  bb_00630D24[BB_00630D24]
  bb_00630D29[BB_00630D29]
  bb_00630D2E[BB_00630D2E]
  bb_00630D3A[BB_00630D3A]
  bb_00630D46[BB_00630D46]
  bb_00630D52[BB_00630D52]
  bb_00630D5E[BB_00630D5E]
  bb_00630D71[BB_00630D71]
  bb_00630D7A[BB_00630D7A]
  bb_00630D83[BB_00630D83]
  bb_00630D91[BB_00630D91]
  bb_00630D94[BB_00630D94]
  bb_00630D99[BB_00630D99]
  bb_00630D9E[BB_00630D9E]
  bb_00630DAA[BB_00630DAA]
  bb_00630DC9[BB_00630DC9]
  bb_00630C70 -->|branch| bb_00630D3A
  bb_00630C70 -->|fallthrough| bb_00630CB0
  bb_00630CB0 -->|branch| bb_00630CC3
  bb_00630CB0 -->|fallthrough| bb_00630CB7
  bb_00630CB7 -->|branch| bb_00630CD1
  bb_00630CC3 -->|branch| bb_00630CD1
  bb_00630CC3 -->|fallthrough| bb_00630CC7
  bb_00630CC7 -->|flow| bb_00630CD1
  bb_00630CD1 -->|branch| bb_00630CEE
  bb_00630CD1 -->|fallthrough| bb_00630CE2
  bb_00630CE2 -->|branch| bb_00630D01
  bb_00630CE2 -->|fallthrough| bb_00630CEE
  bb_00630CEE -->|branch| bb_00630D3A
  bb_00630CEE -->|fallthrough| bb_00630D01
  bb_00630D01 -->|branch| bb_00630D24
  bb_00630D0A -->|branch| bb_00630D21
  bb_00630D0A -->|fallthrough| bb_00630D13
  bb_00630D13 -->|flow| bb_00630D21
  bb_00630D21 -->|flow| bb_00630D24
  bb_00630D24 -->|branch| bb_00630D0A
  bb_00630D24 -->|fallthrough| bb_00630D29
  bb_00630D29 -->|branch| bb_00630D3A
  bb_00630D29 -->|fallthrough| bb_00630D2E
  bb_00630D2E -->|flow| bb_00630D3A
  bb_00630D3A -->|branch| bb_00630DAA
  bb_00630D3A -->|fallthrough| bb_00630D46
  bb_00630D46 -->|branch| bb_00630D5E
  bb_00630D46 -->|fallthrough| bb_00630D52
  bb_00630D52 -->|branch| bb_00630D71
  bb_00630D52 -->|fallthrough| bb_00630D5E
  bb_00630D5E -->|branch| bb_00630DAA
  bb_00630D5E -->|fallthrough| bb_00630D71
  bb_00630D71 -->|branch| bb_00630D94
  bb_00630D7A -->|branch| bb_00630D91
  bb_00630D7A -->|fallthrough| bb_00630D83
  bb_00630D83 -->|flow| bb_00630D91
  bb_00630D91 -->|flow| bb_00630D94
  bb_00630D94 -->|branch| bb_00630D7A
  bb_00630D94 -->|fallthrough| bb_00630D99
  bb_00630D99 -->|branch| bb_00630DAA
  bb_00630D99 -->|fallthrough| bb_00630D9E
  bb_00630D9E -->|flow| bb_00630DAA
```
